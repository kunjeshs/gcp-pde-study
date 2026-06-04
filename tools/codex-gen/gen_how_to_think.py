"""
gen_how_to_think.py — Bulk-generate "how_to_think" markdown for GCP PDE questions
                       missing from generated_explanations.json. Calls codex CLI.

Resume-safe. Checkpoints after every batch. Re-run picks up where it left off.

Usage:
    python gen_how_to_think.py \
        --bank      "C:/.../deduped_question_bank.json" \
        --existing  "C:/.../generated_explanations.json" \
        --out       "C:/.../generated_explanations.json"  # overwrite in place

Optional:
    --batch     25                 # questions per codex call
    --max       0                  # stop after N batches (0 = all)
    --model     gpt-5-codex        # codex model id (uses codex default profile if omitted)
    --log       gen.log            # progress log path
    --upgrade                      # also regenerate existing entries that are missing
                                   # the newer sections (Step 4 / Exam shortcut /
                                   # Tiny mental image / Final answer)

Every generated entry now includes the full teaching structure: the plain-English
rephrase, Steps 1-4, an "Exam shortcut" pattern cue, a one-line "Tiny mental image"
analogy, and a restated "Final answer". Output missing any of these is rejected and
retried on the next run.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import tempfile
import time
from pathlib import Path

SYS_PROMPT = """You are a staff data engineer who coaches candidates through the GCP Professional Data Engineer exam. You write "How to Think" markdown that teaches the reasoning, not just the answer.
Output ONLY a JSON object mapping each question id to {"how_to_think": {"markdown": "..."}}.
No prose outside JSON. No code fences. No commentary. No trailing text.

Markdown structure per entry (match exactly, include EVERY section below):

## How to Think

This question is really asking:

- "<one-line plain-English rephrase>"

### Step 1: Spot the main clue

- The key clue is: <decisive phrases from stem, bold decisive words>.
- That points toward <GCP concept/service category>.

### Step 2: Match the clue to the GCP service/concept

- The concept is **<exact GCP service/feature>**.
- Exam angle: <one sentence why GCP picks this over alternatives>.

### Step 3: Eliminate traps

- **Option A** is tempting because <surface appeal> - but fails because <concrete GCP limitation: cost / latency / scale / IAM scope / consistency / region / batch-vs-stream>.
- **Option B** ... - but fails because ...
- **Option C** ... - but fails because ...
- (Skip the correct option.)

### Step 4: Choose the answer

- <one bullet naming the correct option's chosen service/feature and the single decisive reason it wins>.
- <one bullet tying it back to every requirement in the stem so it clearly satisfies all of them>.

### Exam shortcut

If you see:
- <distinctive signal 1 from the stem>
- <distinctive signal 2 from the stem>
- <distinctive signal 3 from the stem>

Think: **<exact GCP service/feature>**

**Tiny mental image:** <one vivid, concrete real-world analogy in a single sentence that makes the concept stick>.

**Final answer:** <letter>. <correct option text, verbatim from input>

Hard rules:
- Name real GCP services exact: BigQuery, Dataflow, Pub/Sub, Cloud Storage, Bigtable, Spanner, Composer, Dataproc, Dataplex, Cloud SQL, Memorystore, Vertex AI, Looker, Data Fusion.
- Every trap reason cites a concrete GCP limit, not generic advice.
- ALL of the sections above are mandatory: How to Think, Step 1, Step 2, Step 3, Step 4, Exam shortcut, Tiny mental image, Final answer.
- The "Exam shortcut" signals must be reusable pattern cues (the kind that recur across questions), not a paraphrase of this one stem.
- The "Tiny mental image" must be a relatable analogy, max one sentence, not a restatement of the service definition.
- "Final answer" must use the correct option's letter and text verbatim from the input.
- Max 280 words per entry.
- No "in conclusion" filler. No content after the Final answer line.
- Use option letters and text from input verbatim.
"""


def load_json(p: Path):
    with p.open(encoding="utf-8") as f:
        return json.load(f)


def save_json(p: Path, data) -> None:
    tmp = p.with_suffix(p.suffix + ".tmp")
    with tmp.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    tmp.replace(p)


def trim(s: str, n: int) -> str:
    s = (s or "").strip()
    return s if len(s) <= n else s[: n - 1].rstrip() + "…"


def build_question_payload(q: dict) -> dict:
    opts = q.get("options") or []
    # Map options to letters A..D (or however many)
    letters = ["A", "B", "C", "D", "E", "F"]
    opt_map = {letters[i]: opts[i] for i in range(min(len(opts), len(letters)))}
    correct_text = ""
    ans = q.get("answer") or []
    if isinstance(ans, list) and ans:
        correct_text = ans[0]
    elif isinstance(ans, str):
        correct_text = ans
    # Find which letter matches answer
    correct_letter = ""
    for letter, opt_text in opt_map.items():
        if opt_text.strip() == correct_text.strip():
            correct_letter = letter
            break
    return {
        "id": q["id"],
        "q": trim(q.get("question", ""), 700),
        "opts": opt_map,
        "correct": correct_letter or "?",
        "correct_text": trim(correct_text, 220),
        "base": trim(q.get("explanation", ""), 300),
    }


# Sections every complete "How to Think" entry must contain. Used both to validate
# model output and to detect older/partial entries that need regenerating (--upgrade).
REQUIRED_SECTIONS = (
    "## How to Think",
    "### Step 1:",
    "### Step 2:",
    "### Step 3:",
    "### Step 4:",
    "### Exam shortcut",
    "**Tiny mental image:**",
    "**Final answer:**",
)


def is_complete(md: str) -> bool:
    """True only if the markdown contains every mandatory section."""
    if not isinstance(md, str):
        return False
    return all(section in md for section in REQUIRED_SECTIONS)


def collect_missing(bank: dict, existing: dict, upgrade: bool = False) -> list[dict]:
    """Questions needing generation.

    Default: only questions with no entry yet.
    upgrade=True: also re-include questions whose existing entry is incomplete
    (missing Step 4 / Exam shortcut / Tiny mental image / Final answer).
    """
    missing = []
    for topic in bank.get("topics", []):
        for q in topic.get("questions", []):
            qid = q.get("id")
            if not qid:
                continue
            if qid in existing:
                if not upgrade:
                    continue
                md = existing[qid].get("how_to_think", {}).get("markdown", "")
                if is_complete(md):
                    continue
            missing.append(build_question_payload(q))
    return missing


def call_codex(prompt: str, model: str, timeout: int = 600) -> str:
    """Run `codex exec` non-interactively. Prompt via stdin. Return last message."""
    out_path = Path(tempfile.gettempdir()) / f"codex-htt-{os.getpid()}-{int(time.time()*1000)}.txt"
    args = ["codex.cmd", "exec", "--skip-git-repo-check", "--output-last-message", str(out_path), "-"]
    if model:
        args.insert(2, "--model")
        args.insert(3, model)
    proc = subprocess.run(
        args,
        input=prompt,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        timeout=timeout,
        shell=False,
    )
    if not out_path.exists() or out_path.stat().st_size == 0:
        raise RuntimeError(
            f"codex empty output. exit={proc.returncode}\nstderr:\n{proc.stderr[-1200:]}"
        )
    text = out_path.read_text(encoding="utf-8", errors="replace")
    try:
        out_path.unlink()
    except OSError:
        pass
    return text


def extract_json(text: str) -> dict:
    """Best-effort JSON extraction. Codex may wrap in markdown fences."""
    text = text.strip()
    # Strip code fences
    m = re.search(r"```(?:json)?\s*(\{.*?\})\s*```", text, re.DOTALL)
    if m:
        text = m.group(1)
    # Find first { and last }
    s = text.find("{")
    e = text.rfind("}")
    if s == -1 or e == -1 or e < s:
        raise ValueError(f"no JSON object found in output: {text[:400]}")
    blob = text[s : e + 1]
    return json.loads(blob)


def build_batch_prompt(batch: list[dict]) -> str:
    body = json.dumps(batch, ensure_ascii=False, indent=1)
    return (
        SYS_PROMPT
        + "\n\nGenerate how_to_think for these questions. Return a single JSON object mapping id -> {\"how_to_think\": {\"markdown\": \"...\"}}. Nothing else.\n\n"
        + body
    )


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--bank", required=True)
    ap.add_argument("--existing", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--batch", type=int, default=25)
    ap.add_argument("--max", type=int, default=0)
    ap.add_argument("--model", default="gpt-5.5")
    ap.add_argument("--log", default="")
    ap.add_argument("--timeout", type=int, default=600)
    ap.add_argument(
        "--upgrade",
        action="store_true",
        help="Also regenerate existing entries that are missing newer sections "
        "(Step 4 / Exam shortcut / Tiny mental image / Final answer).",
    )
    args = ap.parse_args()

    bank_path = Path(args.bank)
    existing_path = Path(args.existing)
    out_path = Path(args.out)
    log_path = Path(args.log) if args.log else None

    def log(msg: str) -> None:
        line = f"[{time.strftime('%H:%M:%S')}] {msg}"
        print(line, flush=True)
        if log_path:
            with log_path.open("a", encoding="utf-8") as lf:
                lf.write(line + "\n")

    bank = load_json(bank_path)
    existing = load_json(existing_path) if existing_path.exists() else {}
    log(f"bank: {bank.get('total_questions', '?')} Qs, existing: {len(existing)} entries")

    missing = collect_missing(bank, existing, upgrade=args.upgrade)
    if args.upgrade:
        log(f"upgrade mode: regenerating new + incomplete entries -> {len(missing)} Qs")
    log(f"missing: {len(missing)} Qs")
    if not missing:
        log("nothing to do")
        return 0

    total_batches = (len(missing) + args.batch - 1) // args.batch
    if args.max:
        total_batches = min(total_batches, args.max)
    log(f"plan: {total_batches} batches of {args.batch}")

    done_in_run = 0
    fail_in_run = 0
    for i in range(total_batches):
        slice_ = missing[i * args.batch : (i + 1) * args.batch]
        if not slice_:
            break
        ids = [q["id"] for q in slice_]
        log(f"batch {i+1}/{total_batches} ({len(slice_)} Qs): {ids[0]}..{ids[-1]}")
        prompt = build_batch_prompt(slice_)
        try:
            raw = call_codex(prompt, args.model, timeout=args.timeout)
            data = extract_json(raw)
        except Exception as e:
            fail_in_run += 1
            log(f"  FAIL batch {i+1}: {e}")
            # save what we have so far
            save_json(out_path, existing)
            continue

        added = 0
        for qid in ids:
            entry = data.get(qid)
            if not entry:
                continue
            md = entry.get("how_to_think", {}).get("markdown")
            if not is_complete(md):
                # Reject partial output so we never overwrite a good entry with a
                # worse one, and so re-runs retry questions that came back short.
                continue
            existing[qid] = {"how_to_think": {"markdown": md}}
            added += 1
        done_in_run += added
        log(f"  added {added}/{len(slice_)}, total existing: {len(existing)}")
        save_json(out_path, existing)

    log(f"done. added={done_in_run} failed_batches={fail_in_run} total={len(existing)}")
    return 0 if fail_in_run == 0 else 2


if __name__ == "__main__":
    sys.exit(main())

"""
build.py — Build a paste-into-ChatGPT package to backfill the richer "How to Think"
content for every GCP PDE question that is still missing the newer sections
(Step 4 / Exam shortcut / Tiny mental image / Final answer).

Why this exists:
    The normal pipeline (tools/codex-gen/gen_how_to_think.py) calls the codex CLI,
    which needs network access to OpenAI. In environments where that egress is
    blocked, you can instead generate the content by hand in ChatGPT: paste each
    batch file, collect the JSON reply, drop the replies in ./outputs/, then run
    ingest.py to validate and merge them into assets/data/explanations.json.

It reuses SYS_PROMPT and the completeness/payload logic from gen_how_to_think.py
so there is a single source of truth for the structure.

Usage (from repo root):
    python tools/chatgpt-htt/build.py            # default batch size 20
    python tools/chatgpt-htt/build.py --batch 15

Outputs, written next to this script:
    batches/batch_01.md ... batch_NN.md   # each is a complete, self-contained prompt
    ALL_QUESTIONS.json                     # every payload in one file (upload option)
    outputs/                               # empty; put ChatGPT's JSON replies here
"""
from __future__ import annotations

import argparse
import glob
import importlib.util
import json
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
GEN = REPO / "tools" / "codex-gen" / "gen_how_to_think.py"


def load_gen():
    spec = importlib.util.spec_from_file_location("gen_how_to_think", GEN)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def load_bank() -> dict:
    """Assemble a bank ({'topics':[{'questions':[...]}]}) from the per-topic files."""
    topics = []
    for f in sorted(glob.glob(str(REPO / "assets" / "data" / "topics" / "*.json"))):
        d = json.load(open(f, encoding="utf-8"))
        topics.append({"questions": d.get("questions", [])})
    return {"topics": topics}


PASTE_HEADER = """<!--
HOW TO USE THIS FILE
1. Open a ChatGPT conversation (GPT-5 / o-series recommended).
2. Paste this ENTIRE file as one message.
3. ChatGPT replies with ONE JSON object. Save that reply verbatim as
   tools/chatgpt-htt/outputs/{name}.json  (just the JSON, no backticks).
4. Repeat for every batch file, then run:  python tools/chatgpt-htt/ingest.py
Each batch is self-contained: you do not need previous batches in the same chat.
-->

"""


def build_batch_markdown(mod, name: str, batch: list[dict]) -> str:
    body = json.dumps(batch, ensure_ascii=False, indent=1)
    ids = [q["id"] for q in batch]
    return (
        PASTE_HEADER.format(name=name)
        + mod.SYS_PROMPT
        + "\n\nGenerate how_to_think for the "
        + str(len(batch))
        + " questions below. Return a SINGLE JSON object mapping each id -> "
        + '{"how_to_think": {"markdown": "..."}}. '
        + "Include an entry for every one of these ids and nothing else:\n"
        + ", ".join(ids)
        + "\n\nQuestions:\n\n"
        + body
        + "\n"
    )


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--batch", type=int, default=20, help="questions per batch file")
    args = ap.parse_args()

    mod = load_gen()
    bank = load_bank()
    existing = json.load(open(REPO / "assets" / "data" / "explanations.json", encoding="utf-8"))
    missing = mod.collect_missing(bank, existing, upgrade=True)

    batches_dir = HERE / "batches"
    outputs_dir = HERE / "outputs"
    batches_dir.mkdir(exist_ok=True)
    outputs_dir.mkdir(exist_ok=True)
    # Clear any previous batch files so stale ones don't linger.
    for old in batches_dir.glob("batch_*.md"):
        old.unlink()

    total = (len(missing) + args.batch - 1) // args.batch
    width = max(2, len(str(total)))
    for i in range(total):
        sl = missing[i * args.batch : (i + 1) * args.batch]
        name = f"batch_{i + 1:0{width}d}"
        (batches_dir / f"{name}.md").write_text(
            build_batch_markdown(mod, name, sl), encoding="utf-8"
        )

    (HERE / "ALL_QUESTIONS.json").write_text(
        json.dumps(missing, ensure_ascii=False, indent=1), encoding="utf-8"
    )
    (outputs_dir / ".gitkeep").write_text("", encoding="utf-8")

    print(f"missing/incomplete questions: {len(missing)}")
    print(f"wrote {total} batch files of up to {args.batch} -> {batches_dir}")
    print(f"wrote ALL_QUESTIONS.json ({len(missing)} payloads)")
    print("next: paste each batch into ChatGPT, save replies to outputs/, run ingest.py")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

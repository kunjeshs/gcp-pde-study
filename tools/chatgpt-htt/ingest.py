"""
ingest.py — Merge ChatGPT's "How to Think" JSON replies back into explanations.json.

Drop each ChatGPT reply (the raw JSON object) into tools/chatgpt-htt/outputs/ as a
.json or .txt file, then run this from the repo root:

    python tools/chatgpt-htt/ingest.py            # validate + merge in place
    python tools/chatgpt-htt/ingest.py --dry-run  # report only, write nothing

It is tolerant: it strips ``` fences, accepts files that contain extra prose around
the JSON, and accepts either {id: {how_to_think:{markdown}}} or {id: {markdown}}.
Only entries that pass the full completeness check (Step 4 / Exam shortcut /
Tiny mental image / Final answer, etc.) are merged; everything else is reported so
you know exactly which ids still need a re-run.
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import re
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
GEN = REPO / "tools" / "codex-gen" / "gen_how_to_think.py"
EXPL = REPO / "assets" / "data" / "explanations.json"


def load_gen():
    spec = importlib.util.spec_from_file_location("gen_how_to_think", GEN)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def extract_json(text: str) -> dict:
    text = text.strip()
    m = re.search(r"```(?:json)?\s*(\{.*\})\s*```", text, re.DOTALL)
    if m:
        text = m.group(1)
    s, e = text.find("{"), text.rfind("}")
    if s == -1 or e == -1 or e < s:
        raise ValueError("no JSON object found")
    return json.loads(text[s : e + 1])


def get_markdown(entry) -> str | None:
    """Accept {how_to_think:{markdown}} or {markdown} or a bare string."""
    if isinstance(entry, str):
        return entry
    if isinstance(entry, dict):
        if isinstance(entry.get("how_to_think"), dict):
            return entry["how_to_think"].get("markdown")
        return entry.get("markdown")
    return None


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    mod = load_gen()
    existing = json.load(open(EXPL, encoding="utf-8"))

    files = sorted(p for p in (HERE / "outputs").glob("*") if p.suffix in {".json", ".txt"})
    if not files:
        print("no reply files in tools/chatgpt-htt/outputs/ (*.json or *.txt)")
        return 1

    merged, rejected, parse_fail = 0, [], []
    for f in files:
        try:
            data = extract_json(f.read_text(encoding="utf-8"))
        except Exception as e:
            parse_fail.append(f"{f.name}: {e}")
            continue
        for qid, entry in data.items():
            md = get_markdown(entry)
            if not mod.is_complete(md):
                rejected.append(qid)
                continue
            existing[qid] = {"how_to_think": {"markdown": md}}
            merged += 1

    complete_total = sum(
        1 for v in existing.values() if mod.is_complete(v.get("how_to_think", {}).get("markdown", ""))
    )
    print(f"reply files: {len(files)}")
    print(f"merged (complete) entries: {merged}")
    if rejected:
        print(f"rejected (incomplete, re-run these {len(rejected)} ids): {', '.join(rejected[:40])}"
              + (" ..." if len(rejected) > 40 else ""))
    if parse_fail:
        print("parse failures:\n  " + "\n  ".join(parse_fail))
    print(f"explanations.json now complete: {complete_total}/{len(existing)}")

    if args.dry_run:
        print("dry-run: nothing written")
        return 0
    if merged:
        EXPL.write_text(json.dumps(existing, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"wrote {EXPL.relative_to(REPO)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

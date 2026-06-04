"""
lib.py — Shared helper for completing "How to Think" entries directly (no external LLM).

The 536 incomplete entries already contain the rephrase + Step 1-3. We only author the
four missing trailing sections (Step 4 / Exam shortcut / Tiny mental image / Final answer)
and APPEND them, preserving the existing baseline content.

Each batch builds a dict { question_id: trailing_markdown } and calls append_entries(...).
It refuses to touch an id that is already complete, requires the trailing markdown to add
exactly the missing sections, and validates the merged result against is_complete.
"""
from __future__ import annotations

import importlib.util
import json
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
GEN = REPO / "tools" / "codex-gen" / "gen_how_to_think.py"
EXPL = REPO / "assets" / "data" / "explanations.json"

REQUIRED_TAIL = ("### Step 4:", "### Exam shortcut", "**Tiny mental image:**", "**Final answer:**")


def _gen():
    spec = importlib.util.spec_from_file_location("gen_how_to_think", GEN)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def append_entries(additions: dict[str, str]) -> None:
    mod = _gen()
    existing = json.load(open(EXPL, encoding="utf-8"))
    problems = []
    for qid, tail in additions.items():
        if qid not in existing:
            problems.append(f"{qid}: not in explanations.json")
            continue
        base = existing[qid].get("how_to_think", {}).get("markdown", "")
        if mod.is_complete(base):
            problems.append(f"{qid}: already complete - skipping to avoid duplication")
            continue
        missing = [s for s in REQUIRED_TAIL if s not in tail]
        if missing:
            problems.append(f"{qid}: trailing markdown missing {missing}")
            continue
    if problems:
        raise SystemExit("REFUSED:\n  " + "\n  ".join(problems))

    merged = 0
    for qid, tail in additions.items():
        base = existing[qid]["how_to_think"]["markdown"].rstrip()
        full = base + "\n\n" + tail.strip() + "\n"
        if not mod.is_complete(full):
            raise SystemExit(f"{qid}: merged result still fails is_complete()")
        existing[qid] = {"how_to_think": {"markdown": full}}
        merged += 1

    EXPL.write_text(json.dumps(existing, ensure_ascii=False, indent=2), encoding="utf-8")
    complete = sum(
        1 for v in existing.values()
        if mod.is_complete(v.get("how_to_think", {}).get("markdown", ""))
    )
    print(f"appended {merged} entries; explanations.json complete: {complete}/{len(existing)}")

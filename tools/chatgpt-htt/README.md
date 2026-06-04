# Backfill "How to Think" via ChatGPT

Use this when you want to regenerate the richer **How to Think** content but the
codex pipeline (`tools/codex-gen/gen_how_to_think.py`) can't reach OpenAI from your
environment. You drive ChatGPT by hand instead.

Every entry produced here includes the full teaching structure:

1. Plain-English rephrase ("This question is really asking…")
2. **Step 1** – spot the main clue
3. **Step 2** – match the clue to the GCP service/concept
4. **Step 3** – eliminate traps
5. **Step 4** – choose the answer
6. **Exam shortcut** – "If you see… Think: **service**"
7. **Tiny mental image** – a one-line analogy
8. **Final answer** – letter + text, verbatim

The structure/spec is shared with the codex generator via `SYS_PROMPT` in
`gen_how_to_think.py`, so both paths stay in sync.

## What's here

| File | Purpose |
|------|---------|
| `build.py` | Regenerates the batch files + `ALL_QUESTIONS.json` from the current data. |
| `batches/batch_NN.md` | **Paste-ready prompts.** Each is fully self-contained (prompt + ~20 questions). |
| `ALL_QUESTIONS.json` | All pending question payloads in one file, if you'd rather upload than paste. |
| `outputs/` | Drop ChatGPT's JSON replies here (git-ignored). |
| `ingest.py` | Validates the replies and merges complete entries into `explanations.json`. |

`build.py` only targets questions that are **missing the newer sections** — already
complete entries are skipped, so re-running never clobbers good content.

## Steps

1. **(Optional) Rebuild** if the question bank changed:
   ```
   python tools/chatgpt-htt/build.py            # default 20 questions/batch
   python tools/chatgpt-htt/build.py --batch 15 # smaller batches if replies truncate
   ```

2. **Generate in ChatGPT** (GPT-5 / o-series recommended). For each `batches/batch_NN.md`:
   - Paste the **entire** file as one message.
   - ChatGPT returns one JSON object. Save it verbatim as
     `tools/chatgpt-htt/outputs/batch_NN.json` (raw JSON; backticks/extra prose are
     tolerated by the ingester).

   Batches are independent — you can use a fresh chat per batch or run several in one.

3. **Merge**:
   ```
   python tools/chatgpt-htt/ingest.py --dry-run   # preview: merged / rejected / parse failures
   python tools/chatgpt-htt/ingest.py             # write to assets/data/explanations.json
   ```
   Only entries that pass the full completeness check are merged. Any id reported as
   *rejected* (came back incomplete) just needs that batch re-run.

4. **Verify & commit** the updated `assets/data/explanations.json`.

## Tips

- If replies get cut off, lower `--batch` and rebuild.
- The ingester accepts `{id: {how_to_think: {markdown}}}`, `{id: {markdown}}`, or
  `{id: "<markdown>"}`, with or without ```` ```json ```` fences.
- `ingest.py --dry-run` is safe to run anytime; it never writes.

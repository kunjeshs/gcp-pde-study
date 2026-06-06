# GCP PDE Study

Static study companion for the **Google Cloud Professional Data Engineer** exam.
HTML + vanilla JS + JSON. No server, no build step. Mobile-first, dark default, PWA-capable.

## What's inside

- 19 chapter pages (from official exam guide)
- 592 questions across all 19 topics, with answer + base explanation
- "How to Think" walkthroughs for all 592 questions (clue → GCP service → trap elimination); a personal-notes textarea remains as a fallback for any future questions without one
- Quiz mode (per-topic, resumable, shuffleable)
- Review (flagged + missed) and weak-areas views
- GCP services reference + scenario drills + cheat-sheet PDF
- Per-device progress in `localStorage` with JSON export / import

## Live preview locally

```bash
cd gcp-pde-study
python -m http.server 8000
# open http://localhost:8000
```

PWA service worker requires `http://` (not `file://`). Use the command above or any static server.

## Deploy to GitHub Pages

1. Create a new repo on GitHub: `gcp-pde-study`.
2. From this folder:
   ```bash
   git init
   git add .
   git commit -m "init: gcp-pde-study static site"
   git branch -M main
   git remote add origin https://github.com/<YOUR_USERNAME>/gcp-pde-study.git
   git push -u origin main
   ```
3. Repo → Settings → Pages → Source: **Deploy from a branch**, Branch: `main`, Folder: `/ (root)`.
4. Wait ~30s. Site goes live at `https://<YOUR_USERNAME>.github.io/gcp-pde-study/`.

The `.nojekyll` file is intentional — it tells GH Pages to serve files as-is, including any with leading underscores.

## Password gate

Client-side gate. SHA-256 hash of the password is stored in `assets/js/auth.js`.

**Default password: `gcp-pde`**. Change it before deploying.

To change the password:

1. Open `https://<YOUR_USERNAME>.github.io/gcp-pde-study/` (or local preview).
2. Open browser DevTools → Console.
3. Run:
   ```js
   (async (p) => {
     const b = new TextEncoder().encode(p);
     const h = await crypto.subtle.digest("SHA-256", b);
     return [...new Uint8Array(h)].map(x => x.toString(16).padStart(2,"0")).join("");
   })("YOUR_NEW_PASSWORD")
   ```
4. Copy the hex string. Paste into `assets/js/auth.js` as the value of `PASS_HASH`.
5. Commit and push.

To **disable** the gate (fully public site), set `PASS_HASH = ""` in `assets/js/auth.js`.

> Security note: the hash is visible to anyone who views the page source. This is a **friction gate**, not real security. The site content is exam-study material, not secrets, so this is acceptable.

## Re-generating "How to Think" walkthroughs

All 592 questions now ship with a structured "How to Think" walkthrough in `assets/data/explanations.json`, keyed by question id. The personal-notes textarea on the quiz page only appears for a question that has no walkthrough — so it stays as a safety net if new questions are added later.

If you add new questions and want walkthroughs for them, generate only the missing ones:

- **Option A — Codex CLI (ChatGPT Plus):** Run `tools/codex-gen/gen_how_to_think.py`. It is resume-safe and only fills ids missing from `explanations.json`. Requires an active ChatGPT subscription so the `codex` CLI can call a supported model. See the script header for args.
- **Option B — Manual web ChatGPT:** Use the `SYS_PROMPT` from the script in a fresh chat, then paste batches of ~25 questions. Save replies back to `assets/data/explanations.json` keyed by question id.
- **Option C — Anthropic API direct:** Adapt the script to call `messages.create` with a Claude model.

Each entry follows the exact format in the script's `SYS_PROMPT` (one-line rephrase → Step 1 clue → Step 2 GCP service match → Step 3 trap elimination). Merge new entries into `assets/data/explanations.json` and redeploy. No code change needed — the quiz page automatically picks up new ids.

## Repo layout

```
index.html              # home
login.html              # password gate
chapters.html           # chapter index
chapter.html            # ?slug=… chapter detail
question-bank.html      # full bank + topic filter + search
official-sample.html    # Google's 26 official sample questions + How-to-Think
quiz.html               # ?topic=… per-topic quiz
review.html             # flagged + missed
weak-areas.html         # topic scoreboard
services.html           # GCP services reference
exam-traps.html         # scenario drills
cheat-sheet.html        # PDF links
manifest.json           # PWA manifest
sw.js                   # service worker
assets/
  css/
    app.css             # global resets + topbar/nav
    redesign.css        # .pde-redesign tokens, hero, cards, tabs, TOC, drills
    theme-toggle.css    # data-theme=light/dark tokens + orbital day/night dial
    services.css        # .pde-services category-tinted rows
    overrides.css       # legacy classes (cards, buttons, quiz runner)
  js/
    app.js              # shared: theme, nav, auth gate, markdown, boot
    auth.js             # PASS_HASH constant
    data.js             # JSON fetcher + cache
    state.js            # localStorage wrapper (pde:* keys)
    retention.js        # SRS engine: due, mastery, weak-topic buckets
    quiz.js             # quiz runner (used by quiz / review / weak-areas)
  data/
    topics-manifest.json   # 19 topics + counts
    topics/<slug>.json     # per-topic question slice (lazy load)
    chapters.json
    services.json
    scenarios.json
    annotations.json
    explanations.json   # how-to-think walkthroughs (all 592 questions)
  pdf/
    cheatsheet.pdf
    exam-guide.pdf
  icons/
    icon-192.png
    icon-512.png
tools/
  codex-gen/
    gen_how_to_think.py    # bulk generator script
```

## State on this device

All progress, flags, attempt history, notes, and theme live in `localStorage` under the `pde:*` keys. Use the **Export / Import** links on the home page to back up or move between devices.

To wipe all progress: DevTools → Application → Local Storage → clear `pde:*` keys, or just `localStorage.clear()`.

## Not in v1

These flows from the original Flask app are not yet ported. Easy to add later:

- Daily plan
- Exam week schedule
- Readiness scorecard
- Placement test (initial calibration)

The data needed (chapters + bank + attempts) is already in the static bundle, so each is a small client-side page.

## License

Personal study material. Question text + explanations are from the original GCP PDE prep project — keep that license intact.

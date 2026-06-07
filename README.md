# GCP PDE Study

Static study companion for the **Google Cloud Professional Data Engineer** exam.
HTML + vanilla JS + JSON. No server, no build step. Mobile-first, dark default, PWA-capable.

## What's inside

- 19 chapter pages from the official exam guide — Learn, Decide, Drill tabs
- Scenario drills (the pattern, the temptation, the correct call)
- GCP services reference
- Google's 26 official sample questions, with how-to-think breakdowns
- Google's official PDE exam guide (PDF)

## Live preview locally

```bash
cd gcp-pde-study
python -m http.server 8000
# open http://localhost:8000
```

PWA service worker requires `http://` (not `file://`). Use the command above or any static server.

## Deploy to GitHub Pages

1. Push to a public repo (e.g. `gcp-pde-study`).
2. Repo → Settings → Pages → Source: **Deploy from a branch**, Branch: `main`, Folder: `/ (root)`.
3. Wait ~30s. Site goes live at `https://<USERNAME>.github.io/gcp-pde-study/`.

The `.nojekyll` file is intentional — it tells GH Pages to serve files as-is, including any with leading underscores.

## Repo layout

```
index.html              # home
chapters.html           # chapter index
chapter.html            # ?slug=… chapter detail (Learn / Decide / Drill tabs)
official-sample.html    # Google's 26 official sample questions
services.html           # GCP services reference
exam-traps.html         # scenario drills
exam-guide.html         # link to Google's official exam guide PDF
manifest.json           # PWA manifest
sw.js                   # service worker
assets/
  css/
    app.css             # global resets + topbar/nav
    redesign.css        # .pde-redesign tokens, hero, cards, tabs, TOC, drills
    theme-toggle.css    # data-theme=light/dark tokens + orbital day/night dial
    services.css        # .pde-services category-tinted rows
    overrides.css       # legacy classes (cards, buttons, drill option lists)
  js/
    app.js              # shared: theme, nav, markdown, boot
    data.js             # JSON fetcher + cache
    state.js            # localStorage wrapper (pde:* keys)
    theme-toggle.js     # day/night dial controller
  data/
    topics-manifest.json   # 19 topics
    chapters.json          # chapter Learn/Decide content
    services.json
    scenarios.json
    official-sample.json
  pdf/
    exam-guide.pdf
  icons/
    icon-192.png
    icon-512.png
```

## State on this device

Theme preference lives in `localStorage` under `pde:*` keys.

## License

Personal study material. Google's official exam guide and sample questions remain Google's; everything else under this repo is study notes.

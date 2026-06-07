// sw.js — service worker. Cache-first for shell, stale-while-revalidate for data.
// Bump VERSION on every deploy that changes shell files.

const VERSION = "pde-v11-public-2026-06-07";
const SHELL_CACHE = "shell-" + VERSION;
const DATA_CACHE = "data-" + VERSION;

const SHELL = [
  "./",
  "./index.html",
  "./chapters.html",
  "./chapter.html",
  "./official-sample.html",
  "./services.html",
  "./exam-traps.html",
  "./exam-guide.html",
  "./manifest.json",
  "./assets/css/app.css",
  "./assets/css/redesign.css",
  "./assets/css/services.css",
  "./assets/css/theme-toggle.css",
  "./assets/css/overrides.css",
  "./assets/js/app.js",
  "./assets/js/data.js",
  "./assets/js/state.js",
  "./assets/js/theme-toggle.js",
];

self.addEventListener("install", (event) => {
  event.waitUntil(
    caches.open(SHELL_CACHE).then((c) => c.addAll(SHELL).catch(() => {})).then(() => self.skipWaiting())
  );
});

self.addEventListener("activate", (event) => {
  event.waitUntil(
    caches.keys().then((keys) => Promise.all(
      keys.filter((k) => k !== SHELL_CACHE && k !== DATA_CACHE).map((k) => caches.delete(k))
    )).then(() => self.clients.claim())
  );
});

self.addEventListener("fetch", (event) => {
  const req = event.request;
  if (req.method !== "GET") return;
  const url = new URL(req.url);
  if (url.origin !== location.origin) return;

  // Data JSON: stale-while-revalidate
  if (url.pathname.includes("/assets/data/")) {
    event.respondWith((async () => {
      const cache = await caches.open(DATA_CACHE);
      const cached = await cache.match(req);
      const fetching = fetch(req).then((res) => {
        if (res.ok) cache.put(req, res.clone());
        return res;
      }).catch(() => cached);
      return cached || fetching;
    })());
    return;
  }

  // PDFs: cache on demand
  if (url.pathname.endsWith(".pdf")) {
    event.respondWith((async () => {
      const cache = await caches.open(DATA_CACHE);
      const cached = await cache.match(req);
      if (cached) return cached;
      const res = await fetch(req);
      if (res.ok) cache.put(req, res.clone());
      return res;
    })());
    return;
  }

  // Shell: cache-first, fallback to network, fallback to index
  event.respondWith((async () => {
    const cache = await caches.open(SHELL_CACHE);
    const cached = await cache.match(req);
    if (cached) return cached;
    try {
      const res = await fetch(req);
      if (res.ok) cache.put(req, res.clone());
      return res;
    } catch (_e) {
      return (await cache.match("./index.html")) || Response.error();
    }
  })());
});

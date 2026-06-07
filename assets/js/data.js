// data.js — fetch + in-memory cache for static JSON data.
// All paths relative to site root via BASE (auto-derived from <base>).

const cache = new Map();

function basePath() {
  const b = document.querySelector("base");
  if (b && b.href) return new URL(b.href).pathname.replace(/\/?$/, "/");
  const segs = location.pathname.split("/").filter(Boolean);
  if (segs.length > 0 && segs[segs.length - 1].endsWith(".html")) segs.pop();
  return "/" + segs.join("/") + (segs.length ? "/" : "");
}

const BASE = basePath();

async function get(path) {
  const url = BASE + "assets/data/" + path;
  if (cache.has(url)) return cache.get(url);
  const p = fetch(url, { cache: "force-cache" }).then((r) => {
    if (!r.ok) throw new Error("fetch " + url + " -> " + r.status);
    return r.json();
  });
  cache.set(url, p);
  return p;
}

export const Data = {
  base: BASE,
  url(p) { return BASE + p; },

  topicsManifest() { return get("topics-manifest.json"); },
  chapters() { return get("chapters.json"); },
  scenarios() { return get("scenarios.json"); },
  services() { return get("services.json"); },
};

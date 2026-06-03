// data.js — fetch + in-memory cache for static JSON data.
// All paths relative to site root via BASE (auto-derived from <base>).

const cache = new Map();

function basePath() {
  const b = document.querySelector("base");
  if (b && b.href) return new URL(b.href).pathname.replace(/\/?$/, "/");
  // fallback: derive from location
  const segs = location.pathname.split("/").filter(Boolean);
  // If hosted at /repo/<page>.html, base is /repo/
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
  topic(slug) { return get("topics/" + slug + ".json"); },
  chapters() { return get("chapters.json"); },
  scenarios() { return get("scenarios.json"); },
  services() { return get("services.json"); },
  annotations() { return get("annotations.json"); },
  explanations() { return get("explanations.json"); },

  // load all topics + return flat question list (for bank, review, weak-areas)
  async allQuestions() {
    const tm = await this.topicsManifest();
    const slugs = tm.topics.map((t) => t.slug);
    const all = await Promise.all(slugs.map((s) => this.topic(s)));
    const flat = [];
    all.forEach((t) => {
      (t.questions || []).forEach((q) => flat.push({ ...q, topic: t.topic, topicSlug: t.slug }));
    });
    return flat;
  },
};

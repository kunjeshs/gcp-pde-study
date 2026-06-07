// app.js — shared UI: theme toggle, nav, markdown render.

import { State } from "./state.js";

// ---- Theme ----------------------------------------------------------------
function applyTheme(t) {
  if (t === "light" || t === "dark") document.documentElement.setAttribute("data-theme", t);
  else document.documentElement.removeAttribute("data-theme");
  const lbl = document.querySelector(".theme-dial__label");
  if (lbl) lbl.textContent = (t === "light") ? "DAY" : "NIGHT";
}
function initTheme() {
  let t = State.getTheme();
  if (!t) t = "dark"; // default
  applyTheme(t);
}
function toggleTheme(ev) {
  const cur = document.documentElement.getAttribute("data-theme") || "dark";
  const next = cur === "dark" ? "light" : "dark";
  try {
    const x = (ev && ev.clientX) || window.innerWidth / 2;
    const y = (ev && ev.clientY) || window.innerHeight / 2;
    const sweepBg = (next === "dark") ? "#0e1114" : "#fafaf7";
    const sweep = document.createElement("div");
    sweep.className = "theme-sweep";
    sweep.style.setProperty("--sweep-x", x + "px");
    sweep.style.setProperty("--sweep-y", y + "px");
    sweep.style.setProperty("--sweep-color", sweepBg);
    document.body.appendChild(sweep);
    setTimeout(() => sweep.remove(), 700);
  } catch (_e) {}
  State.setTheme(next);
  applyTheme(next);
}

// ---- Nav ------------------------------------------------------------------
const NAV_ITEMS = [
  ["index.html", "Home"],
  ["chapters.html", "Chapters"],
  ["services.html", "Services"],
  ["official-sample.html", "Official Sample"],
  ["exam-traps.html", "Exam Traps"],
  ["exam-guide.html", "Exam Guide"],
];

function renderAppbar() {
  const slot = document.querySelector("[data-appbar]");
  if (!slot) return;
  const base = document.querySelector("base")?.getAttribute("href") || "./";
  const curFile = (location.pathname.split("/").pop() || "index.html").toLowerCase();
  const isChapter = curFile === "chapter.html";
  const navHTML = NAV_ITEMS.map(([href, label]) => {
    const active = (href.toLowerCase() === curFile || (href === "chapters.html" && isChapter))
      ? " class=\"nav-active\"" : "";
    return `<a href="${base}${href}"${active}>${label}</a>`;
  }).join("");

  slot.innerHTML = `
    <div class="brand">
      <a class="brand-link" href="${base}index.html">
        <span class="brand-mark">PDE</span>
        <div>
          <div class="brand-title">GCP Professional Data Engineer</div>
          <div class="brand-subtitle">Study Hub</div>
        </div>
      </a>
    </div>
    <nav class="nav" data-nav>
      ${navHTML}
    </nav>
    <div class="theme-dial-wrap">
      <button class="theme-dial" data-theme-toggle aria-label="Toggle theme" title="Toggle day/night theme">
        <span class="theme-dial__ring" aria-hidden="true"></span>
        <span class="theme-dial__core" aria-hidden="true">
          <span class="theme-dial__star s1"></span>
          <span class="theme-dial__star s2"></span>
          <span class="theme-dial__star s3"></span>
        </span>
        <span class="theme-dial__orbit" aria-hidden="true">
          <span class="theme-dial__body"></span>
        </span>
      </button>
      <span class="theme-dial__label">NIGHT</span>
    </div>
    <button class="menu-btn" aria-label="menu" data-menu-toggle>☰</button>`;

  slot.querySelector("[data-theme-toggle]")?.addEventListener("click", toggleTheme);
  slot.querySelector("[data-menu-toggle]")?.addEventListener("click", () => {
    slot.querySelector("[data-nav]")?.classList.toggle("open");
  });

  const cur = document.documentElement.getAttribute("data-theme") || "dark";
  const lbl = slot.querySelector(".theme-dial__label");
  if (lbl) lbl.textContent = (cur === "light") ? "DAY" : "NIGHT";
}

// ---- Tiny markdown renderer ----------------------------------------------
export function md(src) {
  if (!src) return "";
  if (typeof src !== "string") {
    try { src = JSON.stringify(src, null, 2); } catch (_e) { src = String(src); }
  }
  let s = src.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
  s = s.replace(/```([\s\S]*?)```/g, (_, code) => `<pre><code>${code.trim()}</code></pre>`);
  s = s.replace(/`([^`]+)`/g, "<code>$1</code>");
  s = s.replace(/^######\s+(.*)$/gm, "<h6>$1</h6>")
       .replace(/^#####\s+(.*)$/gm, "<h5>$1</h5>")
       .replace(/^####\s+(.*)$/gm, "<h4>$1</h4>")
       .replace(/^###\s+(.*)$/gm, "<h3>$1</h3>")
       .replace(/^##\s+(.*)$/gm, "<h2>$1</h2>")
       .replace(/^#\s+(.*)$/gm, "<h1>$1</h1>");
  s = s.replace(/\*\*([^*]+)\*\*/g, "<strong>$1</strong>")
       .replace(/(^|[^*])\*([^*\n]+)\*/g, "$1<em>$2</em>");
  s = s.replace(/\[([^\]]+)\]\(([^)\s]+)\)/g, '<a href="$2" target="_blank" rel="noopener">$1</a>');
  s = s.replace(/(?:^|\n)((?:[ \t]*[-*]\s+.+\n?)+)/g, (_, block) => {
    const items = block.trim().split(/\n/).map((l) => l.replace(/^[ \t]*[-*]\s+/, "").trim());
    return "\n<ul>" + items.map((i) => `<li>${i}</li>`).join("") + "</ul>\n";
  });
  s = s.replace(/(?:^|\n)((?:[ \t]*\d+\.\s+.+\n?)+)/g, (_, block) => {
    const items = block.trim().split(/\n/).map((l) => l.replace(/^[ \t]*\d+\.\s+/, "").trim());
    return "\n<ol>" + items.map((i) => `<li>${i}</li>`).join("") + "</ol>\n";
  });
  s = s.split(/\n{2,}/).map((p) => {
    const t = p.trim();
    if (!t) return "";
    if (/^<(h\d|ul|ol|pre|blockquote|table)/.test(t)) return t;
    return "<p>" + t.replace(/\n/g, "<br>") + "</p>";
  }).join("\n");
  return s;
}

// ---- DOM helpers ----------------------------------------------------------
export function el(html) {
  const t = document.createElement("template");
  t.innerHTML = html.trim();
  return t.content.firstElementChild;
}
export function qs(sel, root = document) { return root.querySelector(sel); }
export function qsa(sel, root = document) { return [...root.querySelectorAll(sel)]; }

// ---- Boot ----------------------------------------------------------------
export function boot({ chapter = false } = {}) {
  initTheme();
  if (!document.body.classList.contains("pde-redesign")) {
    document.body.classList.add("pde-redesign");
  }
  if (chapter) document.body.classList.add("pde-chapter");
  renderAppbar();
  return true;
}

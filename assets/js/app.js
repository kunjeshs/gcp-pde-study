// app.js — shared UI: theme toggle, nav, auth gate, markdown render.

import { State } from "./state.js";

// ---- Theme ----------------------------------------------------------------
function applyTheme(t) {
  // Original Flask app uses data-theme="light"|"dark" or auto (no attr)
  if (t === "light" || t === "dark") document.documentElement.setAttribute("data-theme", t);
  else document.documentElement.removeAttribute("data-theme");
  const btn = document.querySelector("[data-theme-toggle]");
  if (btn) btn.textContent = t === "light" ? "◑" : "◐";
}
function initTheme() {
  let t = State.getTheme();
  if (!t) {
    // No saved choice; default to dark to match original Flask app
    t = "dark";
  }
  applyTheme(t);
}
function toggleTheme() {
  const cur = document.documentElement.getAttribute("data-theme") || "dark";
  const next = cur === "dark" ? "light" : "dark";
  State.setTheme(next);
  applyTheme(next);
}

// ---- Auth gate ------------------------------------------------------------
// Password hash baked at build time. Edit assets/js/auth.js to set hash.
import { PASS_HASH } from "./auth.js";

export async function sha256Hex(text) {
  const buf = new TextEncoder().encode(text);
  const hash = await crypto.subtle.digest("SHA-256", buf);
  return [...new Uint8Array(hash)].map((b) => b.toString(16).padStart(2, "0")).join("");
}

export async function verifyPassword(pw) {
  if (!PASS_HASH) return true; // no gate configured -> open
  const h = await sha256Hex(pw);
  return h === PASS_HASH.toLowerCase();
}

function requireAuthOrRedirect() {
  if (!PASS_HASH) return true;
  if (State.isAuthed()) return true;
  const here = location.pathname + location.search + location.hash;
  const base = document.querySelector("base")?.getAttribute("href") || "./";
  location.replace(base + "login.html?next=" + encodeURIComponent(here));
  return false;
}

// ---- Nav (sticky bar) -----------------------------------------------------
const NAV_ITEMS = [
  ["index.html", "Home"],
  ["chapters.html", "Chapters"],
  ["question-bank.html", "Bank"],
  ["quiz.html", "Quiz"],
  ["review.html", "Review"],
  ["weak-areas.html", "Weak"],
  ["services.html", "Services"],
  ["exam-traps.html", "Traps"],
];

function renderAppbar() {
  const slot = document.querySelector("[data-appbar]");
  if (!slot) return;
  const base = document.querySelector("base")?.getAttribute("href") || "./";
  const curFile = (location.pathname.split("/").pop() || "index.html").toLowerCase();
  const navHTML = NAV_ITEMS.map(([href, label]) => {
    const active = href.toLowerCase() === curFile ? " class=\"nav-active\"" : "";
    return `<a href="${base}${href}"${active}>${label}</a>`;
  }).join("");
  slot.innerHTML = `
    <div class="brand">
      <a class="brand-link" href="${base}index.html" style="display:flex;gap:12px;align-items:center;text-decoration:none;color:inherit">
        <span class="brand-mark">PDE</span>
        <div>
          <div class="brand-title">GCP Professional Data Engineer</div>
          <div class="brand-subtitle">Study Hub</div>
        </div>
      </a>
    </div>
    <nav class="nav" data-nav>
      ${navHTML}
      <button class="button ghost sm" data-theme-toggle aria-label="toggle theme" title="Toggle theme" style="padding:6px 10px;min-height:0;font-size:.9rem">◐</button>
      ${PASS_HASH && State.isAuthed() ? `<button class="button ghost sm" data-signout title="Sign out" style="padding:6px 10px;min-height:0;font-size:.85rem">Sign out</button>` : ""}
    </nav>
    <button class="button ghost sm menu-btn" aria-label="menu" data-menu-toggle style="display:none;padding:6px 10px;min-height:0">☰</button>`;
  slot.querySelector("[data-theme-toggle]")?.addEventListener("click", toggleTheme);
  slot.querySelector("[data-menu-toggle]")?.addEventListener("click", () => {
    slot.querySelector("[data-nav]")?.classList.toggle("open");
  });
  slot.querySelector("[data-signout]")?.addEventListener("click", () => {
    State.signOut();
    location.replace(base + "login.html");
  });
}

// ---- Tiny markdown renderer (subset: headings, bold, italic, ul/ol, code, links, br) ----
export function md(src) {
  if (!src) return "";
  if (typeof src !== "string") {
    try { src = JSON.stringify(src, null, 2); } catch (_e) { src = String(src); }
  }
  // Escape HTML
  let s = src.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
  // Fenced code
  s = s.replace(/```([\s\S]*?)```/g, (_, code) => `<pre><code>${code.trim()}</code></pre>`);
  // Inline code
  s = s.replace(/`([^`]+)`/g, "<code>$1</code>");
  // Headings
  s = s.replace(/^######\s+(.*)$/gm, "<h6>$1</h6>")
       .replace(/^#####\s+(.*)$/gm, "<h5>$1</h5>")
       .replace(/^####\s+(.*)$/gm, "<h4>$1</h4>")
       .replace(/^###\s+(.*)$/gm, "<h3>$1</h3>")
       .replace(/^##\s+(.*)$/gm, "<h2>$1</h2>")
       .replace(/^#\s+(.*)$/gm, "<h1>$1</h1>");
  // Bold + italic
  s = s.replace(/\*\*([^*]+)\*\*/g, "<strong>$1</strong>")
       .replace(/(^|[^*])\*([^*\n]+)\*/g, "$1<em>$2</em>");
  // Links [text](url)
  s = s.replace(/\[([^\]]+)\]\(([^)\s]+)\)/g, '<a href="$2" target="_blank" rel="noopener">$1</a>');
  // Lists: group consecutive "- " or "* " lines
  s = s.replace(/(?:^|\n)((?:[ \t]*[-*]\s+.+\n?)+)/g, (_, block) => {
    const items = block.trim().split(/\n/).map((l) => l.replace(/^[ \t]*[-*]\s+/, "").trim());
    return "\n<ul>" + items.map((i) => `<li>${i}</li>`).join("") + "</ul>\n";
  });
  // Numbered lists
  s = s.replace(/(?:^|\n)((?:[ \t]*\d+\.\s+.+\n?)+)/g, (_, block) => {
    const items = block.trim().split(/\n/).map((l) => l.replace(/^[ \t]*\d+\.\s+/, "").trim());
    return "\n<ol>" + items.map((i) => `<li>${i}</li>`).join("") + "</ol>\n";
  });
  // Paragraphs: split by blank line
  s = s.split(/\n{2,}/).map((p) => {
    const t = p.trim();
    if (!t) return "";
    if (/^<(h\d|ul|ol|pre|blockquote|table)/.test(t)) return t;
    return "<p>" + t.replace(/\n/g, "<br>") + "</p>";
  }).join("\n");
  return s;
}

// ---- DOM helpers ---------------------------------------------------------
export function el(html) {
  const t = document.createElement("template");
  t.innerHTML = html.trim();
  return t.content.firstElementChild;
}
export function qs(sel, root = document) { return root.querySelector(sel); }
export function qsa(sel, root = document) { return [...root.querySelectorAll(sel)]; }

// ---- Boot ----------------------------------------------------------------
export function boot({ requireAuth = true } = {}) {
  initTheme();
  if (requireAuth && !requireAuthOrRedirect()) return false;
  renderAppbar();
  return true;
}

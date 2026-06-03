// quiz.js — quiz runner. Used by quiz.html, review.html, weak-areas.html.
// Drives a list of questions through a single-question UI with answer + explain.

import { State } from "./state.js";
import { Data } from "./data.js";
import { md, el, qs } from "./app.js";

const LETTERS = ["A", "B", "C", "D", "E", "F"];

function shuffleSeed(arr, seed) {
  const a = arr.slice();
  let s = seed | 0 || 1;
  for (let i = a.length - 1; i > 0; i--) {
    s = (s * 9301 + 49297) % 233280;
    const j = Math.floor((s / 233280) * (i + 1));
    [a[i], a[j]] = [a[j], a[i]];
  }
  return a;
}

export class Quiz {
  constructor(root, questions, opts = {}) {
    this.root = root;
    this.questions = questions;
    this.idx = 0;
    this.opts = Object.assign({ persistLastSeen: null, shuffle: false, seed: 0 }, opts);
    if (this.opts.shuffle) this.questions = shuffleSeed(this.questions, this.opts.seed || Date.now());
    this.explanationsP = Data.explanations().catch(() => ({}));
  }

  async start() {
    if (!this.questions.length) {
      this.root.innerHTML = `<div class="empty"><div class="big">∅</div>No questions.</div>`;
      return;
    }
    if (this.opts.persistLastSeen) {
      this.idx = Math.max(0, Math.min(this.questions.length - 1, State.getLastSeen(this.opts.persistLastSeen)));
    }
    this.render();
  }

  async render() {
    const q = this.questions[this.idx];
    if (!q) return;
    const stats = State.attemptStats(q.id);
    const flagged = State.isFlagged(q.id);

    // Multi-answer questions ("select N") use checkboxes; single-answer use radios.
    const correctIdxs = this.correctIndices();
    const multi = correctIdxs.length > 1;
    const optsHtml = (q.options || []).map((text, i) => `
      <label class="opt" data-i="${i}">
        <input type="${multi ? "checkbox" : "radio"}" name="opt" value="${i}">
        <span class="letter">${LETTERS[i]}.</span>
        <span class="text">${escapeHtml(text)}</span>
      </label>`).join("");

    const topicLabel = q.topic ? `<span class="badge">${escapeHtml(q.topic)}</span>` : "";
    const srcLabel = q.source ? `<span class="badge">${escapeHtml(q.source)}</span>` : "";

    this.root.innerHTML = `
      <div class="quiz-card">
        <div class="q-meta">
          ${topicLabel}${srcLabel}
          ${stats.tries ? `<span class="badge ${stats.ratio >= 0.6 ? "status-live" : "status-offline"}">${stats.correct}/${stats.tries}</span>` : ""}
          ${flagged ? `<span class="badge status-offline">⚑ flagged</span>` : ""}
          <span class="badge" style="background:transparent;color:var(--text-faint);font-weight:500">#${String(this.idx + 1).padStart(3, "0")} / ${String(this.questions.length).padStart(3, "0")}</span>
        </div>
        <p class="q-stem">${escapeHtml(q.question || "")}</p>
        ${multi ? `<p class="q-multi-hint">Select ${correctIdxs.length} answers.</p>` : ""}
        <div class="opt-list">${optsHtml}</div>
        <div class="cta-row">
          <button class="button primary" data-submit>Submit</button>
          <button class="button" data-skip>Skip</button>
          <button class="button ghost" data-flag>${flagged ? "Unflag" : "Flag"}</button>
        </div>
        <div id="explain-slot" class="hide explain"></div>
      </div>
      <div class="spacer"></div>
    `;

    this.root.querySelector("[data-submit]").addEventListener("click", () => this.submit());
    this.root.querySelector("[data-skip]").addEventListener("click", () => this.next());
    this.root.querySelector("[data-flag]").addEventListener("click", () => {
      State.toggleFlag(q.id);
      this.render();
    });

    // Bottom nav
    document.body.classList.add("has-quiz-nav");
    const nav = qs("[data-quiz-nav]") || document.body.appendChild(el(`<div class="quiz-nav" data-quiz-nav></div>`));
    nav.innerHTML = `
      <button class="button" data-prev ${this.idx === 0 ? "disabled" : ""} style="min-height:0;padding:7px 14px">← Prev</button>
      <div class="quiz-progress" data-pos="${this.idx + 1} / ${this.questions.length}"><span style="width:${((this.idx + 1) / this.questions.length) * 100}%"></span></div>
      <button class="button primary" data-next style="min-height:0;padding:7px 14px">${this.idx === this.questions.length - 1 ? "Finish" : "Next →"}</button>
    `;
    nav.querySelector("[data-prev]")?.addEventListener("click", () => this.prev());
    nav.querySelector("[data-next]")?.addEventListener("click", () => this.next());
  }

  pickedIndices() {
    return [...this.root.querySelectorAll('input[name="opt"]:checked')]
      .map((el) => parseInt(el.value, 10));
  }

  // Indices of every correct option (answer is an array of option texts).
  correctIndices() {
    const q = this.questions[this.idx];
    const ans = Array.isArray(q.answer) ? q.answer : (q.answer != null ? [q.answer] : []);
    const opts = (q.options || []).map((o) => (o || "").trim());
    const idxs = [];
    for (const a of ans) {
      const i = opts.indexOf((a || "").trim());
      if (i >= 0 && !idxs.includes(i)) idxs.push(i);
    }
    return idxs;
  }

  async submit() {
    const q = this.questions[this.idx];
    const picked = this.pickedIndices();
    if (!picked.length) { alert("Pick an option first."); return; }
    const correctIdxs = this.correctIndices();
    const correctSet = new Set(correctIdxs);
    const pickedSet = new Set(picked);
    // Correct only if every right option is chosen and nothing extra is.
    const correct = picked.length === correctIdxs.length && picked.every((i) => correctSet.has(i));
    State.recordAttempt(q.id, correct, picked.length === 1 ? picked[0] : picked);

    // Paint options: mark every correct one, and any wrong picks.
    this.root.querySelectorAll(".opt").forEach((node) => {
      const i = parseInt(node.dataset.i, 10);
      if (correctSet.has(i)) node.classList.add("correct");
      if (pickedSet.has(i) && !correctSet.has(i)) node.classList.add("wrong");
      if (pickedSet.has(i)) node.classList.add("picked");
      node.querySelector("input").disabled = true;
    });
    this.root.querySelector("[data-submit]").disabled = true;

    // Render explanation + how-to-think + user note
    const explanations = await this.explanationsP;
    const htt = explanations?.[q.id]?.how_to_think?.markdown;
    const slot = this.root.querySelector("#explain-slot");
    slot.classList.remove("hide");
    const answerLetters = correctIdxs.map((i) => LETTERS[i]).join(", ") || "?";
    slot.innerHTML = `
      <h3>Answer: ${answerLetters}</h3>
      ${q.explanation ? `<div class="md">${md(q.explanation)}</div>` : ""}
      ${htt
        ? `<hr><div class="md">${md(htt)}</div>`
        : `<hr>
           <h3>How to think (your notes)</h3>
           <p class="muted"><small>No pre-generated guide for this one yet. Write your reasoning — saved on this device.</small></p>
           <textarea data-note placeholder="Spot the clue → match GCP service → eliminate traps…">${escapeHtml(State.getNote(q.id))}</textarea>
           <div class="row" style="margin-top:6px"><button class="btn sm" data-save-note>Save note</button>
             <span class="faint" data-note-status></span></div>`}
    `;
    if (!htt) {
      slot.querySelector("[data-save-note]").addEventListener("click", () => {
        const t = slot.querySelector("[data-note]").value;
        State.setNote(q.id, t);
        slot.querySelector("[data-note-status]").textContent = "Saved.";
        setTimeout(() => { slot.querySelector("[data-note-status]").textContent = ""; }, 1200);
      });
    }
  }

  next() {
    if (this.opts.persistLastSeen) State.setLastSeen(this.opts.persistLastSeen, this.idx + 1);
    if (this.idx >= this.questions.length - 1) {
      this.finish();
      return;
    }
    this.idx++;
    this.render();
  }

  prev() {
    if (this.idx === 0) return;
    this.idx--;
    this.render();
  }

  finish() {
    let correct = 0, tries = 0;
    for (const q of this.questions) {
      const s = State.attemptStats(q.id);
      tries += s.tries > 0 ? 1 : 0;
      correct += s.tries > 0 && s.ratio > 0 ? 1 : 0;
    }
    this.root.innerHTML = `
      <div class="empty">
        <div class="big">✓</div>
        <h2>Quiz complete</h2>
        <p class="muted">${correct}/${this.questions.length} marked correct on this pass.</p>
        <p><a class="button" href="index.html">Home</a> <a class="button primary" href="${location.pathname}${location.search}">Restart</a></p>
      </div>`;
    document.body.classList.remove("has-quiz-nav");
    document.querySelector("[data-quiz-nav]")?.remove();
  }
}

function escapeHtml(s) {
  return (s || "").replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;");
}

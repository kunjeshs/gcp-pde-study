// state.js — localStorage wrapper. All user state lives here.
// Keys are namespaced under "pde:" so site coexists with other apps.

const NS = "pde:";
const K = {
  THEME: NS + "theme",
  AUTH: NS + "auth",
  FLAGS: NS + "flags",
  ATTEMPTS: NS + "attempts",
  PREFS: NS + "prefs",
  NOTES: NS + "notes",
  LAST_SEEN: NS + "lastSeen",
};

function read(key, def) {
  try {
    const v = localStorage.getItem(key);
    if (v === null) return def;
    return JSON.parse(v);
  } catch (_e) {
    return def;
  }
}
function write(key, val) {
  try { localStorage.setItem(key, JSON.stringify(val)); } catch (_e) {}
}
function del(key) { try { localStorage.removeItem(key); } catch (_e) {} }

export const State = {
  // ---- Theme
  getTheme() { return read(K.THEME, null); },
  setTheme(t) { write(K.THEME, t); },

  // ---- Auth (client-side gate)
  isAuthed() { return read(K.AUTH, false) === true; },
  setAuthed(ok) { write(K.AUTH, !!ok); },
  signOut() { del(K.AUTH); },

  // ---- Flags (per-device)
  getFlags() { return read(K.FLAGS, {}); },
  isFlagged(qid) { return !!this.getFlags()[qid]; },
  toggleFlag(qid, note = "") {
    const flags = this.getFlags();
    if (flags[qid]) delete flags[qid];
    else flags[qid] = { note, ts: Date.now() };
    write(K.FLAGS, flags);
    return !!flags[qid];
  },
  setFlagNote(qid, note) {
    const flags = this.getFlags();
    if (!flags[qid]) flags[qid] = { note: "", ts: Date.now() };
    flags[qid].note = note;
    write(K.FLAGS, flags);
  },

  // ---- Attempts (per-question result history)
  getAttempts() { return read(K.ATTEMPTS, {}); },
  recordAttempt(qid, correct, picked) {
    const all = this.getAttempts();
    const entry = all[qid] || { tries: 0, correct: 0, last: null, lastPick: null };
    entry.tries += 1;
    if (correct) entry.correct += 1;
    entry.last = Date.now();
    entry.lastPick = picked;
    all[qid] = entry;
    write(K.ATTEMPTS, all);
  },
  resetAttempts() { del(K.ATTEMPTS); },
  attemptStats(qid) {
    const a = this.getAttempts()[qid];
    if (!a) return { tries: 0, correct: 0, ratio: 0 };
    return { tries: a.tries, correct: a.correct, ratio: a.tries ? a.correct / a.tries : 0 };
  },

  // ---- Prefs (small map)
  getPrefs() { return read(K.PREFS, {}); },
  setPref(k, v) { const p = this.getPrefs(); p[k] = v; write(K.PREFS, p); },
  getPref(k, def) { const p = this.getPrefs(); return k in p ? p[k] : def; },

  // ---- User notes per question (for ungenerated how-to-think)
  getNote(qid) { return read(K.NOTES, {})[qid] || ""; },
  setNote(qid, text) {
    const all = read(K.NOTES, {});
    if (text && text.trim()) all[qid] = text;
    else delete all[qid];
    write(K.NOTES, all);
  },
  getAllNotes() { return read(K.NOTES, {}); },

  // ---- Last-seen position per topic
  getLastSeen(slug) { return read(K.LAST_SEEN, {})[slug] || 0; },
  setLastSeen(slug, idx) {
    const all = read(K.LAST_SEEN, {});
    all[slug] = idx;
    write(K.LAST_SEEN, all);
  },

  // ---- Export / import (backup)
  exportAll() {
    return {
      v: 1,
      ts: Date.now(),
      flags: this.getFlags(),
      attempts: this.getAttempts(),
      prefs: this.getPrefs(),
      notes: this.getAllNotes(),
    };
  },
  importAll(obj) {
    if (!obj || typeof obj !== "object") return false;
    if (obj.flags) write(K.FLAGS, obj.flags);
    if (obj.attempts) write(K.ATTEMPTS, obj.attempts);
    if (obj.prefs) write(K.PREFS, obj.prefs);
    if (obj.notes) write(K.NOTES, obj.notes);
    return true;
  },
};

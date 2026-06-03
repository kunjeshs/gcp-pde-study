/* retention.js — Pure-client retention engine for GCP PDE study app.
 *
 * Pack B (additive). Does not mutate the existing `quiz_state` localStorage
 * schema; reads it once on first load to seed `pde_srs`. Owns two new keys:
 *   - pde_progress : { qid: { topic, attempts, correct, last_seen_ts, last_correct_dates: [iso, iso] } }
 *   - pde_srs      : { qid: { step, correct_streak, wrong_count, mastered, due_at } }
 *
 * Mastery rule: mastered=true ONLY when wrong_count>=1 AND correct_streak>=2
 * AND the last two corrects are on different calendar dates
 * (toLocaleDateString comparison — uses host timezone).
 *
 * TIMEZONE CAVEAT: calendar-date comparison uses the browser's local
 * timezone via Date.prototype.toLocaleDateString(). A learner who travels
 * across timezones between two correct answers may see the same wall-clock
 * day evaluated as two distinct calendar dates (or vice versa). This is
 * acceptable for spaced-repetition heuristics but documented here so that
 * future server-side reconciliation does not assume UTC.
 *
 * No npm/node deps. ES module. Browser-only.
 */
(function (root, factory) {
  const mod = factory();
  // Always attach to window for the in-page test runner.
  root.Retention = mod;
  // Optional ES module export if loaded as <script type="module">.
  if (typeof exports === 'object' && typeof module === 'object') {
    module.exports = mod;
  }
})(typeof window !== 'undefined' ? window : this, function () {
  'use strict';

  // ── Constants ────────────────────────────────────────────────────────
  const LS_PROGRESS = 'pde_progress';
  const LS_SRS      = 'pde_srs';
  const LS_QUIZ     = 'quiz_state';        // legacy, additive read only
  const LS_MIGRATED = 'pde_srs_migrated';  // idempotency flag
  const LS_MISS_TAGS = 'pde_miss_tags';    // { qid: [{tags:[..], ts}] }
  const LS_ATTEMPTS  = 'pde_attempts_log'; // capped rolling array of attempts
  const LS_VISITS    = 'pde_chapter_visits'; // { topicSlug: { learn:ts, decide:ts, drill:ts, quiz:ts } }
  const ATTEMPTS_CAP = 500;
  const ATTEMPTS_MAX_AGE_DAYS = 28; // age-aware prune so 7d windows survive heavy days
  const CONFIDENCE_LEVELS = ['knew', 'mostly', 'guessed', 'no_idea'];
  const CONFIDENT_LEVELS  = ['knew', 'mostly'];
  const GUESS_LEVELS      = ['guessed', 'no_idea'];
  const MISS_TAGS = [
    'misread_requirement',
    'confused_services',
    'over_engineered',
    'ignored_cost',
    'ignored_latency',
    'missed_security',
    'multi_select_mistake',
    'guessed',
    // PM-iter2 additions:
    'concept_gap',
    'bad_elimination',
    'forgot_constraint',
    'misread_diagram'
  ];
  const MISS_TAG_ADVICE = {
    misread_requirement:  'Underline must / should / required and constraints before scanning options.',
    confused_services:    'Drill the must-know services list for this chapter; build a service-vs-service flashcard.',
    over_engineered:      'Pick the simplest option that meets the stated goal. Default managed > custom.',
    ignored_cost:         'Re-read for cost or budget hints. Match storage class / pricing tier to access pattern.',
    ignored_latency:      'Look for latency / real-time / low-latency. Match streaming or managed-cache patterns.',
    missed_security:      'Scan for IAM, encryption, compliance, audit clues. Default to least-privilege and CMEK.',
    multi_select_mistake: 'Read "Choose all that apply" carefully. Recount selections.',
    guessed:              'Mark this topic for an extra drill before moving on.',
    concept_gap:          'Open the Learn tab and re-read the targeted concept; add a flashcard.',
    bad_elimination:      'Cross out two options first, then read the rest against the prompt.',
    forgot_constraint:    'List every constraint before reading options. Re-check each constraint after picking.',
    misread_diagram:      'Re-trace diagrams, tables, and numbers. Convert each to a constraint statement.'
  };
  const MISS_TAG_LABELS = {
    misread_requirement:  'Misread requirement',
    confused_services:    'Confused services',
    over_engineered:      'Over-engineered',
    ignored_cost:         'Ignored cost',
    ignored_latency:      'Ignored latency',
    missed_security:      'Missed security/compliance clue',
    multi_select_mistake: 'Multi-select mistake',
    guessed:              'Guessed',
    concept_gap:          'Concept gap',
    bad_elimination:      'Bad elimination',
    forgot_constraint:    'Forgot constraint',
    misread_diagram:      'Misread diagram/table'
  };

  // Storage health (QA-P1): track last write success so UI can surface a banner.
  let __storageOk = true;
  let __storageReason = null;
  function getStorageHealth() {
    return { ok: !!__storageOk, reason: __storageReason };
  }

  const DAY_MS = 86400000;
  const STEP_INTERVALS_DAYS = [1, 3, 7, 14, 30]; // step 0..4
  const MAX_STEP = STEP_INTERVALS_DAYS.length - 1; // 4

  const Z_95 = 1.96; // two-sided 95% z-score for Wilson lower bound

  // ── localStorage helpers ─────────────────────────────────────────────
  function _read(key) {
    try {
      const raw = (typeof localStorage !== 'undefined') ? localStorage.getItem(key) : null;
      if (!raw) return {};
      const parsed = JSON.parse(raw);
      return (parsed && typeof parsed === 'object') ? parsed : {};
    } catch (e) {
      return {};
    }
  }
  function _write(key, obj) {
    try {
      if (typeof localStorage !== 'undefined') {
        localStorage.setItem(key, JSON.stringify(obj));
        __storageOk = true;
        __storageReason = null;
        return true;
      }
      __storageOk = false;
      __storageReason = 'localStorage unavailable';
      return false;
    } catch (e) {
      __storageOk = false;
      __storageReason = (e && e.name === 'QuotaExceededError') ? 'quota exceeded' : ('write error: ' + (e && e.message || 'unknown'));
      return false;
    }
  }
  function loadProgress() { return _read(LS_PROGRESS); }
  function loadSrs()      { return _read(LS_SRS); }
  function loadQuiz()     { return _read(LS_QUIZ); }

  function saveProgress(p) { _write(LS_PROGRESS, p); }
  function saveSrs(s)      { _write(LS_SRS, s); }

  // ── Calendar-date comparison (local timezone) ────────────────────────
  function _calDate(ts) {
    return new Date(ts).toLocaleDateString();
  }
  function _sameCalDay(a, b) {
    return _calDate(a) === _calDate(b);
  }

  // ── ISO local-midnight date ('YYYY-MM-DD') ───────────────────────────
  // Stable, locale-independent format for streak persistence.
  function _isoLocalDate(ts) {
    const d = (typeof ts === 'number') ? new Date(ts) : new Date();
    d.setHours(0, 0, 0, 0);
    return d.getFullYear() + '-' +
           String(d.getMonth() + 1).padStart(2, '0') + '-' +
           String(d.getDate()).padStart(2, '0');
  }
  function _isoLocalDateAddDays(isoStr, days) {
    // Parse YYYY-MM-DD in LOCAL time (not UTC).
    const parts = String(isoStr || '').split('-');
    if (parts.length !== 3) return null;
    const d = new Date(parseInt(parts[0], 10), parseInt(parts[1], 10) - 1, parseInt(parts[2], 10));
    d.setDate(d.getDate() + days);
    d.setHours(0, 0, 0, 0);
    return _isoLocalDate(d.getTime());
  }

  // ── SRS scheduling ───────────────────────────────────────────────────
  function _intervalForStep(step) {
    const idx = Math.max(0, Math.min(MAX_STEP, step));
    return STEP_INTERVALS_DAYS[idx] * DAY_MS;
  }

  function _ensureSrsEntry(srs, qid) {
    if (!srs[qid]) {
      srs[qid] = {
        step: 0,
        correct_streak: 0,
        wrong_count: 0,
        mastered: false,
        due_at: 0
      };
    }
    return srs[qid];
  }

  function _ensureProgressEntry(prog, qid, topic) {
    if (!prog[qid]) {
      prog[qid] = {
        topic: topic || null,
        attempts: 0,
        correct: 0,
        confident_attempts: 0, // QA-P1 split metric
        confident_correct: 0,  // QA-P1 split metric
        last_seen_ts: 0,
        last_correct_dates: []
      };
    } else {
      if (topic && !prog[qid].topic) prog[qid].topic = topic;
      // Backfill split-metric fields so existing entries gain them on first hit.
      if (typeof prog[qid].confident_attempts !== 'number') prog[qid].confident_attempts = 0;
      if (typeof prog[qid].confident_correct !== 'number') prog[qid].confident_correct  = 0;
    }
    return prog[qid];
  }

  // ── Migration: seed pde_srs from legacy quiz_state.wrong_ids ─────────
  function migrate(now) {
    now = (typeof now === 'number') ? now : Date.now();
    const srs  = loadSrs();
    const prog = loadProgress();
    const quiz = loadQuiz();

    let changed = false;
    Object.keys(quiz).forEach(function (topicSlug) {
      // Skip non-topic meta (e.g. _streak)
      if (topicSlug.charAt(0) === '_') return;
      const ts = quiz[topicSlug];
      if (!ts || typeof ts !== 'object') return;
      const wrongIds = Array.isArray(ts.wrong_ids) ? ts.wrong_ids : [];
      wrongIds.forEach(function (qid) {
        if (!qid) return;
        if (!srs[qid]) {
          srs[qid] = {
            step: 0,
            correct_streak: 0,
            wrong_count: 1,
            mastered: false,
            due_at: now + DAY_MS
          };
          changed = true;
        }
        if (!prog[qid]) {
          prog[qid] = {
            topic: topicSlug,
            attempts: 1,
            correct: 0,
            last_seen_ts: now,
            last_correct_dates: []
          };
          changed = true;
        }
      });
    });

    if (changed) {
      saveSrs(srs);
      saveProgress(prog);
    }
    // Idempotency marker (informational; logic is already idempotent).
    _write(LS_MIGRATED, { at: now, version: 1 });
    return { srs: srs, progress: prog, changed: changed };
  }

  // ── recordAnswer(qid, topic, correct, ts) ────────────────────────────
  function recordAnswer(qid, topic, correct, ts, opts) {
    if (!qid) return null;
    ts = (typeof ts === 'number') ? ts : Date.now();

    // Normalize confidence option (back-compat: string or {confidence}).
    let confidence = null;
    if (typeof opts === 'string') {
      confidence = opts;
    } else if (opts && typeof opts === 'object' && typeof opts.confidence === 'string') {
      confidence = opts.confidence;
    }
    if (confidence && CONFIDENCE_LEVELS.indexOf(confidence) === -1) confidence = null;
    const isGuess = (confidence === 'guessed' || confidence === 'no_idea');

    const srs  = loadSrs();
    const prog = loadProgress();

    const sEntry = _ensureSrsEntry(srs, qid);
    const pEntry = _ensureProgressEntry(prog, qid, topic);

    pEntry.attempts += 1;
    pEntry.last_seen_ts = ts;
    if (topic) pEntry.topic = topic;

    // QA-P1 split metric: only confident answers count toward confident accuracy.
    const isConfident = (CONFIDENT_LEVELS.indexOf(confidence) !== -1);
    if (isConfident) pEntry.confident_attempts += 1;

    if (correct && isGuess) {
      // Correct-but-guessed: count attempt, do not progress mastery, requeue 1d.
      // Confident accuracy untouched (this attempt was a guess).
      pEntry.correct += 1;
      sEntry.due_at = ts + DAY_MS;
    } else if (correct) {
      pEntry.correct += 1;
      if (isConfident) pEntry.confident_correct += 1;
      // Track last two distinct-date corrects (calendar date strings).
      const cal = _calDate(ts);
      const lastDates = Array.isArray(pEntry.last_correct_dates) ? pEntry.last_correct_dates.slice() : [];
      // Streak: count two corrects on the SAME day as a single streak step? Spec says
      // mastery requires last two corrects on DIFFERENT calendar dates, so increment
      // streak per correct, but mastery gate evaluates dates.
      sEntry.correct_streak = (sEntry.correct_streak || 0) + 1;
      // P1-1: only advance step once the learner has been wrong at least once.
      // First-time-correct on a brand-new qid stays at step 0 → 1d reinforcement.
      if ((sEntry.wrong_count || 0) >= 1) {
        sEntry.step = Math.min(MAX_STEP, (sEntry.step || 0) + 1);
      }
      sEntry.due_at = ts + _intervalForStep(sEntry.step);

      // Update date list (keep most-recent 2; preserve order oldest→newest).
      lastDates.push(cal);
      while (lastDates.length > 2) lastDates.shift();
      pEntry.last_correct_dates = lastDates;

      // Mastery check.
      const twoDistinct = (lastDates.length >= 2) && (lastDates[0] !== lastDates[1]);
      sEntry.mastered = !!(sEntry.wrong_count >= 1 && sEntry.correct_streak >= 2 && twoDistinct);
    } else {
      sEntry.wrong_count = (sEntry.wrong_count || 0) + 1;
      sEntry.step = 0;
      sEntry.correct_streak = 0;
      sEntry.mastered = false;
      sEntry.due_at = ts + DAY_MS;
    }

    saveSrs(srs);
    saveProgress(prog);
    _appendAttemptLog({ qid: qid, topic: topic || null, correct: !!correct, confidence: confidence, ts: ts });
    return { srs: sEntry, progress: pEntry, confidence: confidence, guessed_correct: !!(correct && isGuess) };
  }

  // Attempt log (capped rolling array, used for windowed metrics + calibration).
  function _loadAttempts() {
    try {
      const raw = (typeof localStorage !== 'undefined') ? localStorage.getItem(LS_ATTEMPTS) : null;
      if (!raw) return [];
      const parsed = JSON.parse(raw);
      return Array.isArray(parsed) ? parsed : [];
    } catch (e) { return []; }
  }
  function _saveAttempts(arr) {
    // Route through _write so storage health flips on any failure.
    return _write(LS_ATTEMPTS, arr);
  }
  function _appendAttemptLog(entry) {
    const arr = _loadAttempts();
    arr.push(entry);
    // QA-P2: age-aware prune. Drop entries older than ATTEMPTS_MAX_AGE_DAYS, then
    // also enforce the count cap as a safety belt. Preserves recent windows when
    // a learner has a heavy day.
    const now = (entry && typeof entry.ts === 'number') ? entry.ts : Date.now();
    const ageCutoff = now - (ATTEMPTS_MAX_AGE_DAYS * DAY_MS);
    let trimmed = arr.filter(function (e) {
      return e && typeof e.ts === 'number' && e.ts >= ageCutoff;
    });
    while (trimmed.length > ATTEMPTS_CAP) trimmed.shift();
    _saveAttempts(trimmed);
  }
  function loadAttemptsLog() { return _loadAttempts().slice(); }

  // Miss-tag store
  function _loadMissTags() { return _read(LS_MISS_TAGS); }
  function _saveMissTags(o) { _write(LS_MISS_TAGS, o); }
  function recordMissTags(qid, tags, ts) {
    if (!qid) return null;
    ts = (typeof ts === 'number') ? ts : Date.now();
    if (!Array.isArray(tags)) tags = [];
    const cleaned = tags.filter(function (t) { return MISS_TAGS.indexOf(t) !== -1; });
    if (cleaned.length === 0) return null;
    const store = _loadMissTags();
    if (!Array.isArray(store[qid])) store[qid] = [];
    store[qid].push({ tags: cleaned, ts: ts });
    while (store[qid].length > 20) store[qid].shift();
    _saveMissTags(store);
    return store[qid];
  }
  function getMissTagSummary() {
    const store = _loadMissTags();
    const counts = {};
    MISS_TAGS.forEach(function (t) { counts[t] = 0; });
    Object.keys(store).forEach(function (qid) {
      const arr = Array.isArray(store[qid]) ? store[qid] : [];
      arr.forEach(function (e) {
        const tags = Array.isArray(e && e.tags) ? e.tags : [];
        tags.forEach(function (t) {
          if (typeof counts[t] === 'number') counts[t] += 1;
        });
      });
    });
    const ranked = Object.keys(counts).map(function (t) { return { tag: t, count: counts[t] }; });
    ranked.sort(function (a, b) { return b.count - a.count; });
    return { counts: counts, ranked: ranked };
  }

  // Chapter visit tracking (Learn -> Decide -> Drill -> Quiz workflow dots).
  function recordChapterVisit(topicSlug, tab, ts) {
    if (!topicSlug || !tab) return null;
    ts = (typeof ts === 'number') ? ts : Date.now();
    const store = _read(LS_VISITS);
    if (!store[topicSlug]) store[topicSlug] = {};
    store[topicSlug][tab] = ts;
    _write(LS_VISITS, store);
    return store[topicSlug];
  }
  function getChapterVisits(topicSlug) {
    const store = _read(LS_VISITS);
    return (topicSlug ? (store[topicSlug] || {}) : store);
  }

  // ── getDueQuestions(now) ─────────────────────────────────────────────
  // Returns due items sorted overdue-most-first (smallest due_at first).
  function getDueQuestions(now) {
    now = (typeof now === 'number') ? now : Date.now();
    const srs = loadSrs();
    const out = [];
    Object.keys(srs).forEach(function (qid) {
      const e = srs[qid];
      if (!e) return;
      if ((e.due_at || 0) <= now) {
        out.push({
          qid: qid,
          due_at: e.due_at || 0,
          step: e.step || 0,
          mastered: !!e.mastered,
          overdue_ms: now - (e.due_at || 0)
        });
      }
    });
    out.sort(function (a, b) { return a.due_at - b.due_at; });
    return out;
  }

  // ── Wilson lower bound on a binomial proportion ──────────────────────
  function wilsonLower(correct, total, z) {
    if (!total || total <= 0) return 0;
    z = z || Z_95;
    const phat = correct / total;
    const z2 = z * z;
    const denom = 1 + z2 / total;
    const center = phat + z2 / (2 * total);
    const margin = z * Math.sqrt((phat * (1 - phat) + z2 / (4 * total)) / total);
    return (center - margin) / denom;
  }

  // ── _aggregateByTopic — internal ─────────────────────────────────────
  function _aggregateByTopic(prog) {
    const byTopic = {};
    Object.keys(prog).forEach(function (qid) {
      const p = prog[qid];
      if (!p || !p.topic) return;
      const t = p.topic;
      if (!byTopic[t]) byTopic[t] = { topic: t, attempts: 0, correct: 0, last_seen_ts: 0 };
      byTopic[t].attempts += (p.attempts || 0);
      byTopic[t].correct  += (p.correct || 0);
      if ((p.last_seen_ts || 0) > byTopic[t].last_seen_ts) {
        byTopic[t].last_seen_ts = p.last_seen_ts || 0;
      }
    });
    return byTopic;
  }

  // ── getWeakTopics(n, {minAttempts=3}) ────────────────────────────────
  function getWeakTopics(n, opts) {
    n = (typeof n === 'number' && n > 0) ? n : 3;
    const minAttempts = (opts && typeof opts.minAttempts === 'number') ? opts.minAttempts : 3;
    const prog = loadProgress();
    const byTopic = _aggregateByTopic(prog);

    const ranked = Object.keys(byTopic).map(function (t) {
      const row = byTopic[t];
      const wilson = wilsonLower(row.correct, row.attempts, Z_95);
      return {
        topic: t,
        attempts: row.attempts,
        correct: row.correct,
        accuracy: row.attempts ? (row.correct / row.attempts) : 0,
        wilson_lower: wilson,
        last_seen_ts: row.last_seen_ts
      };
    }).filter(function (r) { return r.attempts >= minAttempts; });

    ranked.sort(function (a, b) {
      if (a.wilson_lower !== b.wilson_lower) return a.wilson_lower - b.wilson_lower; // weakest first
      return b.last_seen_ts - a.last_seen_ts; // tie-break by recency desc
    });
    return ranked.slice(0, n);
  }

  // ── sessionStart() ───────────────────────────────────────────────────
  // Capture a per-qid {seen, correct, mastered} snapshot of pde_progress and
  // pde_srs at session-open. The returned object is then passed back to
  // getReadinessDelta() so the delta is computed from a true session-scoped
  // baseline (no prior-session inflation).
  function sessionStart(ts) {
    ts = (typeof ts === 'number') ? ts : Date.now();
    const prog = loadProgress();
    const srs  = loadSrs();
    const snapshot = {};
    Object.keys(prog).forEach(function (qid) {
      const p = prog[qid] || {};
      const s = srs[qid] || {};
      snapshot[qid] = {
        seen: p.attempts || 0,
        correct: p.correct || 0,
        mastered: !!s.mastered
      };
    });
    return { ts: ts, snapshot: snapshot };
  }

  // ── getReadinessDelta(sessionStart) ──────────────────────────────────
  // sessionStart is { ts, snapshot } as returned by sessionStart(). Backwards-
  // compatible: a bare number is treated as a timestamp with empty snapshot.
  function getReadinessDelta(sessionStartArg) {
    let snap = {};
    let ts = 0;
    if (typeof sessionStartArg === 'number') {
      ts = sessionStartArg;
    } else if (sessionStartArg && typeof sessionStartArg === 'object') {
      ts = sessionStartArg.ts || 0;
      snap = sessionStartArg.snapshot || {};
    }

    const prog = loadProgress();
    const srs  = loadSrs();
    let priorAttempts = 0, priorCorrect = 0;
    let nowAttempts = 0, nowCorrect = 0;
    let masteredToday = 0;

    Object.keys(prog).forEach(function (qid) {
      const p = prog[qid] || {};
      const before = snap[qid] || { seen: 0, correct: 0, mastered: false };
      nowAttempts += (p.attempts || 0);
      nowCorrect  += (p.correct || 0);
      priorAttempts += before.seen;
      priorCorrect  += before.correct;
      const isMasteredNow = !!(srs[qid] && srs[qid].mastered);
      if (isMasteredNow && !before.mastered) masteredToday += 1;
    });
    // Also count any qids that exist in snap but were cleared from prog (rare).
    Object.keys(snap).forEach(function (qid) {
      if (prog[qid]) return;
      priorAttempts += snap[qid].seen;
      priorCorrect  += snap[qid].correct;
    });

    const priorAcc = priorAttempts ? (priorCorrect / priorAttempts) : 0;
    const nowAcc   = nowAttempts ? (nowCorrect / nowAttempts) : 0;
    const sessionAttempts = Math.max(0, nowAttempts - priorAttempts);
    const sessionCorrect  = Math.max(0, nowCorrect  - priorCorrect);
    const sessionAccuracy = sessionAttempts ? (sessionCorrect / sessionAttempts) : 0;
    return {
      session_start: ts,
      prior_attempts: priorAttempts,
      prior_correct: priorCorrect,
      prior_accuracy: priorAcc,
      now_attempts: nowAttempts,
      now_correct: nowCorrect,
      now_accuracy: nowAcc,
      session_attempts: sessionAttempts,
      session_correct: sessionCorrect,
      session_accuracy: sessionAccuracy,
      mastered_today: masteredToday,
      delta: nowAcc - priorAcc
    };
  }

  // ── Streak helpers (P0-1) ────────────────────────────────────────────
  // pde_streak = { last_active_date: 'YYYY-MM-DD', count: int }
  const LS_STREAK = 'pde_streak';
  function getStreak() {
    const raw = _read(LS_STREAK);
    if (!raw || typeof raw !== 'object') return { last_active_date: null, count: 0 };
    return {
      last_active_date: raw.last_active_date || null,
      count: (typeof raw.count === 'number') ? raw.count : 0
    };
  }
  function bumpStreak(now) {
    const today = _isoLocalDate(now);
    const yesterday = _isoLocalDateAddDays(today, -1);
    const cur = getStreak();
    let next;
    if (cur.last_active_date === today) {
      next = cur; // idempotent same-day
    } else if (cur.last_active_date === yesterday) {
      next = { last_active_date: today, count: (cur.count || 0) + 1 };
    } else {
      next = { last_active_date: today, count: 1 };
    }
    _write(LS_STREAK, next);
    return next;
  }

  // ── getRecommendationReason(topic_slug) ──────────────────────────────
  function getRecommendationReason(topicSlug) {
    if (!topicSlug) return 'topic: no data';
    const prog = loadProgress();
    const byTopic = _aggregateByTopic(prog);
    // The progress store keys by topic name as recorded at recordAnswer time.
    // Caller may pass a slug or a name; match on either.
    let row = byTopic[topicSlug];
    if (!row) {
      const keys = Object.keys(byTopic);
      const match = keys.find(function (k) {
        return _slugify(k) === topicSlug || k === topicSlug;
      });
      if (match) row = byTopic[match];
    }
    if (!row || !row.attempts) {
      return topicSlug + ': no attempts yet';
    }
    const wilson = wilsonLower(row.correct, row.attempts, Z_95);
    const lastSeenLabel = _humanAgo(row.last_seen_ts, Date.now());
    return topicSlug + ': ' + row.correct + '/' + row.attempts + ' correct, last seen ' +
           lastSeenLabel + ', Wilson=' + wilson.toFixed(2);
  }

  function _slugify(s) {
    return String(s || '').toLowerCase()
      .replace(/[^a-z0-9]+/g, '-')
      .replace(/^-+|-+$/g, '');
  }

  function _humanAgo(ts, now) {
    if (!ts) return 'never';
    const diff = Math.max(0, now - ts);
    const d = Math.floor(diff / DAY_MS);
    if (d <= 0) {
      const h = Math.floor(diff / 3600000);
      if (h <= 0) return 'just now';
      return h + 'h ago';
    }
    return d + 'd ago';
  }

  // ── Cold-start daily plan (used by tests + future Pack D wiring) ─────
  // Reads chapter_content via a caller-supplied object (test runner passes
  // it in) and ranks topics by exam_weight. Falls back to topic order.
  const WEIGHT_RANK = {
    'very high': 5,
    'high': 4,
    'medium-high': 3.5,
    'medium': 3,
    'low-medium': 2,
    'low': 1
  };
  function coldStartDailyPlan(chapterContent, n) {
    n = (typeof n === 'number' && n > 0) ? n : 3;
    if (!chapterContent || !chapterContent.chapters) return [];
    const chapters = chapterContent.chapters;
    const rows = Object.keys(chapters).map(function (key, idx) {
      const cdata = chapters[key] || {};
      const w = (cdata.exam_weight || '').toString().toLowerCase().trim();
      const rank = WEIGHT_RANK[w];
      return {
        topic: key,
        exam_weight: cdata.exam_weight || null,
        rank: (typeof rank === 'number') ? rank : null,
        order: idx
      };
    });
    rows.sort(function (a, b) {
      const aHas = (a.rank !== null), bHas = (b.rank !== null);
      if (aHas && bHas) {
        if (b.rank !== a.rank) return b.rank - a.rank;     // high first
        return a.order - b.order;                           // tie → topic order
      }
      if (aHas) return -1;
      if (bHas) return 1;
      return a.order - b.order;
    });
    return rows.slice(0, n);
  }

  // ── Annotation placeholder helper ────────────────────────────────────
  // Returns the requested annotation field or the canonical placeholder
  // string. Tests assert this string.
  const ANNOTATION_PLACEHOLDER = 'annotation unavailable';
  function getAnnotationField(annotation, field) {
    if (!annotation || typeof annotation !== 'object') return ANNOTATION_PLACEHOLDER;
    const v = annotation[field];
    if (v === undefined || v === null || v === '') return ANNOTATION_PLACEHOLDER;
    return v;
  }

  // ── Topic state buckets + review queue + readiness snapshot ─────────
  function _weightRank(w) {
    const v = WEIGHT_RANK[String(w || '').toLowerCase().trim()];
    return (typeof v === 'number') ? v : 0;
  }
  function _topicAggregateWithMastery(prog, srs) {
    const byTopic = {};
    Object.keys(prog).forEach(function (qid) {
      const p = prog[qid];
      if (!p || !p.topic) return;
      const t = p.topic;
      if (!byTopic[t]) byTopic[t] = {
        topic: t, attempts: 0, correct: 0,
        confident_attempts: 0, confident_correct: 0,
        qids: [], mastered_qids: 0, last_seen_ts: 0
      };
      byTopic[t].attempts += (p.attempts || 0);
      byTopic[t].correct  += (p.correct || 0);
      byTopic[t].confident_attempts += (p.confident_attempts || 0);
      byTopic[t].confident_correct  += (p.confident_correct  || 0);
      byTopic[t].qids.push(qid);
      if (srs[qid] && srs[qid].mastered) byTopic[t].mastered_qids += 1;
      if ((p.last_seen_ts || 0) > byTopic[t].last_seen_ts) {
        byTopic[t].last_seen_ts = p.last_seen_ts || 0;
      }
    });
    return byTopic;
  }
  // Buckets: untested | urgent | developing | almost_mastered | mastered.
  function _bucketFor(row) {
    if (!row || !row.attempts) return 'untested';
    const wilson = wilsonLower(row.correct, row.attempts, Z_95);
    const allMastered = (row.qids.length > 0 && row.mastered_qids === row.qids.length);
    if (allMastered && row.attempts >= 3) return 'mastered';
    if (row.attempts >= 5 && wilson >= 0.80) return 'almost_mastered';
    if (row.attempts >= 3 && wilson < 0.55) return 'urgent';
    return 'developing';
  }

  function getTopicStates(chapterContent, allTopics) {
    const prog = loadProgress();
    const srs  = loadSrs();
    const agg  = _topicAggregateWithMastery(prog, srs);
    const chapters = (chapterContent && chapterContent.chapters) ? chapterContent.chapters : {};
    const titleBySlug = {};
    Object.keys(chapters).forEach(function (title) { titleBySlug[_slugify(title)] = title; });

    const seenTitles = {};
    const out = [];
    Object.keys(agg).forEach(function (topicKey) {
      const slug = _slugify(topicKey);
      const title = titleBySlug[slug] || topicKey;
      seenTitles[title] = true;
      const row = agg[topicKey];
      // Bucket + Wilson use confident counts when learner has any confident
      // attempts on the topic; otherwise fall back to totals so a brand-new
      // learner is not penalized for guessing while exploring.
      const useConfident = (row.confident_attempts || 0) >= 3;
      const wAtt = useConfident ? row.confident_attempts : row.attempts;
      const wCor = useConfident ? row.confident_correct  : row.correct;
      const wilson = wAtt ? wilsonLower(wCor, wAtt, Z_95) : 0;
      const accuracy = row.attempts ? (row.correct / row.attempts) : 0;
      const confidentAcc = row.confident_attempts ? (row.confident_correct / row.confident_attempts) : null;
      const cdata = chapters[title] || {};
      // Build a derived row for bucket evaluation that uses confident counts
      // when meaningful so guesses do not earn mastery.
      const bucketRow = {
        attempts: wAtt, correct: wCor,
        qids: row.qids, mastered_qids: row.mastered_qids
      };
      out.push({
        topic: title,
        slug: slug,
        attempts: row.attempts,
        correct: row.correct,
        confident_attempts: row.confident_attempts,
        confident_correct: row.confident_correct,
        accuracy: accuracy,
        confident_accuracy: confidentAcc,
        wilson_lower: wilson,
        mastered_qids: row.mastered_qids,
        seen_qids: row.qids.length,
        last_seen_ts: row.last_seen_ts,
        exam_weight: cdata.exam_weight || null,
        weight_rank: _weightRank(cdata.exam_weight),
        bucket: _bucketFor(bucketRow)
      });
    });

    if (Array.isArray(allTopics)) {
      allTopics.forEach(function (t) {
        if (!t || !t.topic) return;
        if (seenTitles[t.topic]) return;
        const cdata = chapters[t.topic] || {};
        out.push({
          topic: t.topic,
          slug: t.slug || _slugify(t.topic),
          attempts: 0,
          correct: 0,
          confident_attempts: 0,
          confident_correct: 0,
          accuracy: 0,
          confident_accuracy: null,
          wilson_lower: 0,
          mastered_qids: 0,
          seen_qids: 0,
          last_seen_ts: 0,
          exam_weight: cdata.exam_weight || null,
          weight_rank: _weightRank(cdata.exam_weight),
          bucket: 'untested'
        });
      });
    }
    return out;
  }

  function getReviewQueue(now, chapterContent) {
    now = (typeof now === 'number') ? now : Date.now();
    const due = getDueQuestions(now);
    if (due.length === 0) return [];
    const prog = loadProgress();
    const chapters = (chapterContent && chapterContent.chapters) ? chapterContent.chapters : {};
    const titleBySlug = {};
    Object.keys(chapters).forEach(function (title) { titleBySlug[_slugify(title)] = title; });
    return due.map(function (d) {
      const p = prog[d.qid] || {};
      const slug = _slugify(p.topic);
      const title = titleBySlug[slug] || p.topic || null;
      const cdata = title ? (chapters[title] || {}) : {};
      return {
        qid: d.qid,
        due_at: d.due_at,
        overdue_ms: d.overdue_ms,
        step: d.step,
        mastered: d.mastered,
        topic: title,
        topic_slug: slug,
        exam_weight: cdata.exam_weight || null,
        weight_rank: _weightRank(cdata.exam_weight)
      };
    }).sort(function (a, b) {
      if (b.overdue_ms !== a.overdue_ms) return b.overdue_ms - a.overdue_ms;
      return b.weight_rank - a.weight_rank;
    });
  }

  function getConfidenceCalibration() {
    const log = _loadAttempts();
    const out = {
      total: log.length,
      with_confidence: 0,
      knew_correct: 0, knew_wrong: 0,
      mostly_correct: 0, mostly_wrong: 0,
      guessed_correct: 0, guessed_wrong: 0,
      no_idea_correct: 0, no_idea_wrong: 0,
      confident_but_wrong: 0,
      guessed_but_correct: 0
    };
    log.forEach(function (e) {
      if (!e || typeof e !== 'object') return;
      const c = e.confidence;
      if (CONFIDENCE_LEVELS.indexOf(c) === -1) return;
      out.with_confidence += 1;
      const key = c + (e.correct ? '_correct' : '_wrong');
      if (typeof out[key] === 'number') out[key] += 1;
      if ((c === 'knew' || c === 'mostly') && !e.correct) out.confident_but_wrong += 1;
      if ((c === 'guessed' || c === 'no_idea') && e.correct) out.guessed_but_correct += 1;
    });
    return out;
  }

  function getRecentImprovement(days) {
    days = (typeof days === 'number' && days > 0) ? days : 7;
    const log = _loadAttempts();
    const now = Date.now();
    const windowMs = days * DAY_MS;
    let recentAtt = 0, recentCorr = 0, priorAtt = 0, priorCorr = 0;
    log.forEach(function (e) {
      if (!e) return;
      const age = now - (e.ts || 0);
      if (age < 0) return;
      if (age <= windowMs) {
        recentAtt += 1;
        if (e.correct) recentCorr += 1;
      } else if (age <= 2 * windowMs) {
        priorAtt += 1;
        if (e.correct) priorCorr += 1;
      }
    });
    const recentAcc = recentAtt ? (recentCorr / recentAtt) : 0;
    const priorAcc  = priorAtt  ? (priorCorr  / priorAtt)  : 0;
    return {
      days: days,
      recent_attempts: recentAtt, recent_correct: recentCorr, recent_accuracy: recentAcc,
      prior_attempts: priorAtt,   prior_correct: priorCorr,   prior_accuracy: priorAcc,
      delta: recentAcc - priorAcc
    };
  }

  function getReadinessSnapshot(chapterContent, allTopics) {
    const states = getTopicStates(chapterContent, allTopics);
    const sectionsMap = {};
    const bucket_counts = { urgent: 0, developing: 0, almost_mastered: 0, mastered: 0, untested: 0 };
    states.forEach(function (s) {
      if (typeof bucket_counts[s.bucket] === 'number') bucket_counts[s.bucket] += 1;
      const sec = (String(s.topic).match(/^(\d+)\./) || [])[1];
      if (!sec) return;
      if (!sectionsMap[sec]) {
        sectionsMap[sec] = {
          section: sec, topics: [], weighted_acc_num: 0, weighted_acc_den: 0,
          attempts: 0, correct: 0, mastered_topics: 0, weakest: null
        };
      }
      const b = sectionsMap[sec];
      b.topics.push(s);
      b.attempts += s.attempts;
      b.correct  += s.correct;
      if (s.bucket === 'mastered') b.mastered_topics += 1;
      const w = Math.max(1, s.weight_rank || 1);
      // Prefer confident accuracy when meaningful; otherwise use plain accuracy.
      const accForReadiness = (s.confident_attempts >= 3 && s.confident_accuracy !== null)
        ? s.confident_accuracy
        : (s.attempts ? s.accuracy : 0);
      b.weighted_acc_num += accForReadiness * w;
      b.weighted_acc_den += w;
      if (s.attempts >= 3) {
        if (!b.weakest || s.wilson_lower < (b.weakest.wilson_lower || 1)) b.weakest = s;
      }
    });
    const sections = Object.keys(sectionsMap).sort().map(function (k) {
      const b = sectionsMap[k];
      return {
        section: b.section,
        topic_count: b.topics.length,
        attempts: b.attempts,
        accuracy: b.attempts ? (b.correct / b.attempts) : 0,
        weighted_accuracy: b.weighted_acc_den ? (b.weighted_acc_num / b.weighted_acc_den) : 0,
        mastered_topics: b.mastered_topics,
        weakest_topic: b.weakest ? { topic: b.weakest.topic, slug: b.weakest.slug, wilson_lower: b.weakest.wilson_lower } : null
      };
    });
    const weak_high_weight = states.filter(function (s) {
      if (s.attempts < 3) return false;
      if (s.bucket === 'mastered') return false;
      if (s.weight_rank < 3.5) return false;
      return s.wilson_lower < 0.70;
    }).sort(function (a, b) {
      if (b.weight_rank !== a.weight_rank) return b.weight_rank - a.weight_rank;
      return a.wilson_lower - b.wilson_lower;
    });
    return {
      sections: sections,
      weak_high_weight: weak_high_weight,
      due_count: getDueQuestions(Date.now()).length,
      confidence: getConfidenceCalibration(),
      miss_tags: getMissTagSummary().ranked.filter(function (r) { return r.count > 0; }).slice(0, 3),
      improvement: getRecentImprovement(7),
      bucket_counts: bucket_counts,
      streak: getStreak()
    };
  }

  // ── Canonical topic id + slug-rename alias (QA-P2) ─────────────────
  // Pick a single canonical id (the slug) for any topic input. Falls back
  // gracefully when input is already a slug, a title, or a free-string.
  function canonicalTopicSlug(input, chapterContent) {
    if (!input) return null;
    const candidate = _slugify(input);
    if (!chapterContent || !chapterContent.chapters) return candidate;
    // If the candidate matches an existing chapter slug, accept.
    let known = null;
    Object.keys(chapterContent.chapters).forEach(function (title) {
      if (_slugify(title) === candidate) known = candidate;
    });
    if (known) return known;
    // Otherwise return the slugified input as best-effort.
    return candidate;
  }
  function topicTitleForSlug(slug, chapterContent) {
    if (!slug || !chapterContent || !chapterContent.chapters) return null;
    let title = null;
    Object.keys(chapterContent.chapters).forEach(function (t) {
      if (_slugify(t) === slug) title = t;
    });
    return title;
  }

  // ── Tag advice helpers (PM iter-2) ─────────────────────────────────
  function getMissTagAdvice(tag) {
    if (!tag) return null;
    return MISS_TAG_ADVICE[tag] || null;
  }
  function getMissTagLabel(tag) {
    if (!tag) return '';
    return MISS_TAG_LABELS[tag] || tag;
  }

  // ── Blended next-best-step priority (PM iter-2) ────────────────────
  // Order: severely-overdue (overdue >=2 days) > weak-high-weight > due-now
  // > weakest-by-Wilson > cold-start-high-weight. Returns one recommendation.
  // Each entry: { kind, slug?, count?, reason, severity }
  function getNextBestStep(now, chapterContent, allTopics) {
    now = (typeof now === 'number') ? now : Date.now();
    const queue = getReviewQueue(now, chapterContent);
    const states = getTopicStates(chapterContent, allTopics);

    const severelyOverdue = queue.filter(function (q) {
      return (q.overdue_ms || 0) >= 2 * DAY_MS;
    });
    if (severelyOverdue.length > 0) {
      return {
        kind: 'review_overdue',
        count: severelyOverdue.length,
        total_due: queue.length,
        reason: severelyOverdue.length + ' question' + (severelyOverdue.length === 1 ? '' : 's') + ' more than 2 days overdue.'
      };
    }
    // Weak high-weight: any topic with weight_rank >= 3.5, attempts >= 3, wilson < 0.7, not mastered.
    const weakHigh = states.filter(function (s) {
      if (s.attempts < 3) return false;
      if (s.bucket === 'mastered') return false;
      if (s.weight_rank < 3.5) return false;
      return s.wilson_lower < 0.70;
    }).sort(function (a, b) {
      if (b.weight_rank !== a.weight_rank) return b.weight_rank - a.weight_rank;
      return a.wilson_lower - b.wilson_lower;
    });
    if (weakHigh.length > 0) {
      const top = weakHigh[0];
      return {
        kind: 'weak_high_weight',
        slug: top.slug,
        topic: top.topic,
        weight: top.exam_weight,
        reason: 'Heavy exam weight (' + (top.exam_weight || '—') + ') and accuracy is shaky.'
      };
    }
    if (queue.length > 0) {
      return {
        kind: 'review_due',
        count: queue.length,
        reason: queue.length + ' question' + (queue.length === 1 ? '' : 's') + ' due now.'
      };
    }
    const weakest = (typeof getWeakTopics === 'function') ? (getWeakTopics(1, { minAttempts: 3 }) || []) : [];
    if (weakest.length > 0) {
      const w = weakest[0];
      const slug = canonicalTopicSlug(w.topic, chapterContent);
      return { kind: 'weakest', slug: slug, topic: w.topic, reason: 'Lowest accuracy among topics you have attempted.' };
    }
    // Cold start: highest exam weight untested topic.
    const cold = states.filter(function (s) { return s.attempts === 0; })
                       .sort(function (a, b) {
                         if (b.weight_rank !== a.weight_rank) return b.weight_rank - a.weight_rank;
                         return 0;
                       });
    if (cold.length > 0) {
      const top = cold[0];
      return { kind: 'cold_start', slug: top.slug, topic: top.topic, weight: top.exam_weight, reason: 'Cold start — open the highest-weight chapter first.' };
    }
    return { kind: 'idle', reason: 'Everything mastered. Take a break.' };
  }

  // ── Stale-learner detection ────────────────────────────────────────
  function getStalenessDays() {
    const log = _loadAttempts();
    if (log.length === 0) return null;
    const last = log[log.length - 1];
    if (!last || typeof last.ts !== 'number') return null;
    return Math.floor((Date.now() - last.ts) / DAY_MS);
  }

  // ── Test-only helpers ────────────────────────────────────────────────
  function _resetAll() {
    try {
      if (typeof localStorage !== 'undefined') {
        localStorage.removeItem(LS_PROGRESS);
        localStorage.removeItem(LS_SRS);
        localStorage.removeItem(LS_MIGRATED);
        localStorage.removeItem(LS_QUIZ);
        localStorage.removeItem(LS_MISS_TAGS);
        localStorage.removeItem(LS_ATTEMPTS);
        localStorage.removeItem(LS_VISITS);
      }
    } catch (e) { /* noop */ }
  }

  // ── Public API ───────────────────────────────────────────────────────
  return {
    // EXACT-SIGNATURES required by the spec
    recordAnswer: recordAnswer,
    getWeakTopics: getWeakTopics,
    getDueQuestions: getDueQuestions,
    getReadinessDelta: getReadinessDelta,
    getRecommendationReason: getRecommendationReason,

    // Additional public surface used by tests / future packs
    migrate: migrate,
    coldStartDailyPlan: coldStartDailyPlan,
    getAnnotationField: getAnnotationField,
    wilsonLower: wilsonLower,
    loadProgress: loadProgress,
    loadSrs: loadSrs,
    sessionStart: sessionStart,
    bumpStreak: bumpStreak,
    getStreak: getStreak,

    // Pack E additions
    recordMissTags: recordMissTags,
    getMissTagSummary: getMissTagSummary,
    recordChapterVisit: recordChapterVisit,
    getChapterVisits: getChapterVisits,
    getTopicStates: getTopicStates,
    getReviewQueue: getReviewQueue,
    getConfidenceCalibration: getConfidenceCalibration,
    getRecentImprovement: getRecentImprovement,
    getReadinessSnapshot: getReadinessSnapshot,
    loadAttemptsLog: loadAttemptsLog,
    // Pack F (iter-2) additions
    getStorageHealth: getStorageHealth,
    canonicalTopicSlug: canonicalTopicSlug,
    topicTitleForSlug: topicTitleForSlug,
    getMissTagAdvice: getMissTagAdvice,
    getMissTagLabel: getMissTagLabel,
    getNextBestStep: getNextBestStep,
    getStalenessDays: getStalenessDays,

    // Constants
    LS_KEYS: { progress: LS_PROGRESS, srs: LS_SRS, quiz: LS_QUIZ, migrated: LS_MIGRATED, miss_tags: LS_MISS_TAGS, attempts: LS_ATTEMPTS, visits: LS_VISITS },
    STEP_INTERVALS_DAYS: STEP_INTERVALS_DAYS,
    ANNOTATION_PLACEHOLDER: ANNOTATION_PLACEHOLDER,
    CONFIDENCE_LEVELS: CONFIDENCE_LEVELS,
    MISS_TAGS: MISS_TAGS,
    MISS_TAG_LABELS: MISS_TAG_LABELS,
    MISS_TAG_ADVICE: MISS_TAG_ADVICE,

    // Test-only
    _resetAll: _resetAll,
    _calDate: _calDate,
    _isoLocalDate: _isoLocalDate,
    _isoLocalDateAddDays: _isoLocalDateAddDays,
    _LS_STREAK: LS_STREAK
  };
});

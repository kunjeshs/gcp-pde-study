/* retention.js — Pure-client retention engine for GCP PDE study app.
 *
 * Owns three localStorage keys:
 *   - pde_progress : { qid: { topic, attempts, correct, last_seen_ts, last_correct_dates: [iso, iso] } }
 *   - pde_srs      : { qid: { step, correct_streak, wrong_count, mastered, due_at } }
 *   - pde_streak   : { last_active_date, count }
 *
 * Mastery rule: mastered=true ONLY when wrong_count>=1 AND correct_streak>=2
 * AND the last two corrects are on different calendar dates (local timezone).
 *
 * Browser-only. No deps. Attaches to window.Retention.
 */
(function (root, factory) {
  const mod = factory();
  root.Retention = mod;
  if (typeof exports === 'object' && typeof module === 'object') {
    module.exports = mod;
  }
})(typeof window !== 'undefined' ? window : this, function () {
  'use strict';

  const LS_PROGRESS = 'pde_progress';
  const LS_SRS      = 'pde_srs';
  const LS_QUIZ     = 'quiz_state';
  const LS_MIGRATED = 'pde_srs_migrated';
  const LS_STREAK   = 'pde_streak';

  const DAY_MS = 86400000;
  const STEP_INTERVALS_DAYS = [1, 3, 7, 14, 30];
  const MAX_STEP = STEP_INTERVALS_DAYS.length - 1;
  const Z_95 = 1.96;

  function _read(key) {
    try {
      const raw = (typeof localStorage !== 'undefined') ? localStorage.getItem(key) : null;
      if (!raw) return {};
      const parsed = JSON.parse(raw);
      return (parsed && typeof parsed === 'object') ? parsed : {};
    } catch (e) { return {}; }
  }
  function _write(key, obj) {
    try {
      if (typeof localStorage !== 'undefined') {
        localStorage.setItem(key, JSON.stringify(obj));
        return true;
      }
    } catch (e) {}
    return false;
  }
  function loadProgress() { return _read(LS_PROGRESS); }
  function loadSrs()      { return _read(LS_SRS); }
  function loadQuiz()     { return _read(LS_QUIZ); }
  function saveProgress(p) { _write(LS_PROGRESS, p); }
  function saveSrs(s)      { _write(LS_SRS, s); }

  function _calDate(ts) { return new Date(ts).toLocaleDateString(); }
  function _isoLocalDate(ts) {
    const d = (typeof ts === 'number') ? new Date(ts) : new Date();
    d.setHours(0, 0, 0, 0);
    return d.getFullYear() + '-' +
           String(d.getMonth() + 1).padStart(2, '0') + '-' +
           String(d.getDate()).padStart(2, '0');
  }
  function _isoLocalDateAddDays(isoStr, days) {
    const parts = String(isoStr || '').split('-');
    if (parts.length !== 3) return null;
    const d = new Date(parseInt(parts[0], 10), parseInt(parts[1], 10) - 1, parseInt(parts[2], 10));
    d.setDate(d.getDate() + days);
    d.setHours(0, 0, 0, 0);
    return _isoLocalDate(d.getTime());
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

  function _intervalForStep(step) {
    const idx = Math.max(0, Math.min(MAX_STEP, step));
    return STEP_INTERVALS_DAYS[idx] * DAY_MS;
  }
  function _ensureSrsEntry(srs, qid) {
    if (!srs[qid]) srs[qid] = { step: 0, correct_streak: 0, wrong_count: 0, mastered: false, due_at: 0 };
    return srs[qid];
  }
  function _ensureProgressEntry(prog, qid, topic) {
    if (!prog[qid]) {
      prog[qid] = { topic: topic || null, attempts: 0, correct: 0, last_seen_ts: 0, last_correct_dates: [] };
    } else if (topic && !prog[qid].topic) {
      prog[qid].topic = topic;
    }
    return prog[qid];
  }

  function migrate(now) {
    now = (typeof now === 'number') ? now : Date.now();
    const srs  = loadSrs();
    const prog = loadProgress();
    const quiz = loadQuiz();
    let changed = false;
    Object.keys(quiz).forEach(function (topicSlug) {
      if (topicSlug.charAt(0) === '_') return;
      const ts = quiz[topicSlug];
      if (!ts || typeof ts !== 'object') return;
      const wrongIds = Array.isArray(ts.wrong_ids) ? ts.wrong_ids : [];
      wrongIds.forEach(function (qid) {
        if (!qid) return;
        if (!srs[qid]) {
          srs[qid] = { step: 0, correct_streak: 0, wrong_count: 1, mastered: false, due_at: now + DAY_MS };
          changed = true;
        }
        if (!prog[qid]) {
          prog[qid] = { topic: topicSlug, attempts: 1, correct: 0, last_seen_ts: now, last_correct_dates: [] };
          changed = true;
        }
      });
    });
    if (changed) { saveSrs(srs); saveProgress(prog); }
    _write(LS_MIGRATED, { at: now, version: 1 });
    return { srs: srs, progress: prog, changed: changed };
  }

  function recordAnswer(qid, topic, correct, ts) {
    if (!qid) return null;
    ts = (typeof ts === 'number') ? ts : Date.now();

    const srs  = loadSrs();
    const prog = loadProgress();
    const sEntry = _ensureSrsEntry(srs, qid);
    const pEntry = _ensureProgressEntry(prog, qid, topic);

    pEntry.attempts += 1;
    pEntry.last_seen_ts = ts;
    if (topic) pEntry.topic = topic;

    if (correct) {
      pEntry.correct += 1;
      const cal = _calDate(ts);
      const lastDates = Array.isArray(pEntry.last_correct_dates) ? pEntry.last_correct_dates.slice() : [];
      sEntry.correct_streak = (sEntry.correct_streak || 0) + 1;
      if ((sEntry.wrong_count || 0) >= 1) {
        sEntry.step = Math.min(MAX_STEP, (sEntry.step || 0) + 1);
      }
      sEntry.due_at = ts + _intervalForStep(sEntry.step);
      lastDates.push(cal);
      while (lastDates.length > 2) lastDates.shift();
      pEntry.last_correct_dates = lastDates;
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
    return { srs: sEntry, progress: pEntry };
  }

  function getDueQuestions(now) {
    now = (typeof now === 'number') ? now : Date.now();
    const srs = loadSrs();
    const out = [];
    Object.keys(srs).forEach(function (qid) {
      const e = srs[qid];
      if (!e) return;
      if ((e.due_at || 0) <= now) {
        out.push({
          qid: qid, due_at: e.due_at || 0, step: e.step || 0,
          mastered: !!e.mastered, overdue_ms: now - (e.due_at || 0)
        });
      }
    });
    out.sort(function (a, b) { return a.due_at - b.due_at; });
    return out;
  }

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

  function _aggregateByTopic(prog) {
    const byTopic = {};
    Object.keys(prog).forEach(function (qid) {
      const p = prog[qid];
      if (!p || !p.topic) return;
      const t = p.topic;
      if (!byTopic[t]) byTopic[t] = { topic: t, attempts: 0, correct: 0, last_seen_ts: 0 };
      byTopic[t].attempts += (p.attempts || 0);
      byTopic[t].correct  += (p.correct || 0);
      if ((p.last_seen_ts || 0) > byTopic[t].last_seen_ts) byTopic[t].last_seen_ts = p.last_seen_ts || 0;
    });
    return byTopic;
  }

  function getWeakTopics(n, opts) {
    n = (typeof n === 'number' && n > 0) ? n : 3;
    const minAttempts = (opts && typeof opts.minAttempts === 'number') ? opts.minAttempts : 3;
    const prog = loadProgress();
    const byTopic = _aggregateByTopic(prog);
    const ranked = Object.keys(byTopic).map(function (t) {
      const row = byTopic[t];
      const wilson = wilsonLower(row.correct, row.attempts, Z_95);
      return {
        topic: t, attempts: row.attempts, correct: row.correct,
        accuracy: row.attempts ? (row.correct / row.attempts) : 0,
        wilson_lower: wilson, last_seen_ts: row.last_seen_ts
      };
    }).filter(function (r) { return r.attempts >= minAttempts; });
    ranked.sort(function (a, b) {
      if (a.wilson_lower !== b.wilson_lower) return a.wilson_lower - b.wilson_lower;
      return b.last_seen_ts - a.last_seen_ts;
    });
    return ranked.slice(0, n);
  }

  function getStreak() {
    const raw = _read(LS_STREAK);
    if (!raw || typeof raw !== 'object') return { last_active_date: null, count: 0 };
    return { last_active_date: raw.last_active_date || null, count: (typeof raw.count === 'number') ? raw.count : 0 };
  }
  function bumpStreak(now) {
    const today = _isoLocalDate(now);
    const yesterday = _isoLocalDateAddDays(today, -1);
    const cur = getStreak();
    let next;
    if (cur.last_active_date === today) next = cur;
    else if (cur.last_active_date === yesterday) next = { last_active_date: today, count: (cur.count || 0) + 1 };
    else next = { last_active_date: today, count: 1 };
    _write(LS_STREAK, next);
    return next;
  }

  /* Bucket: untested | urgent | developing | almost_mastered | mastered */
  function _bucketFor(row) {
    if (!row || !row.attempts) return 'untested';
    const wilson = wilsonLower(row.correct, row.attempts, Z_95);
    const allMastered = (row.qids && row.qids.length > 0 && row.mastered_qids === row.qids.length);
    if (allMastered && row.attempts >= 3) return 'mastered';
    if (row.attempts >= 5 && wilson >= 0.80) return 'almost_mastered';
    if (row.attempts >= 3 && wilson < 0.55) return 'urgent';
    return 'developing';
  }
  function _aggregateWithMastery(prog, srs) {
    const byTopic = {};
    Object.keys(prog).forEach(function (qid) {
      const p = prog[qid];
      if (!p || !p.topic) return;
      const t = p.topic;
      if (!byTopic[t]) byTopic[t] = {
        topic: t, attempts: 0, correct: 0, qids: [], mastered_qids: 0, last_seen_ts: 0
      };
      byTopic[t].attempts += (p.attempts || 0);
      byTopic[t].correct  += (p.correct || 0);
      byTopic[t].qids.push(qid);
      if (srs[qid] && srs[qid].mastered) byTopic[t].mastered_qids += 1;
      if ((p.last_seen_ts || 0) > byTopic[t].last_seen_ts) byTopic[t].last_seen_ts = p.last_seen_ts || 0;
    });
    return byTopic;
  }
  const WEIGHT_RANK = {
    'very high': 5, 'high': 4, 'medium-high': 3.5,
    'medium': 3, 'low-medium': 2, 'low': 1
  };
  function _weightRank(w) {
    const v = WEIGHT_RANK[String(w || '').toLowerCase().trim()];
    return (typeof v === 'number') ? v : 0;
  }

  function getTopicStates(chapters, allTopics) {
    chapters = chapters || {};
    const prog = loadProgress();
    const srs  = loadSrs();
    const agg  = _aggregateWithMastery(prog, srs);
    const titleBySlug = {};
    Object.keys(chapters).forEach(function (title) { titleBySlug[_slugify(title)] = title; });

    const seenTitles = {};
    const out = [];
    Object.keys(agg).forEach(function (topicKey) {
      const slug = _slugify(topicKey);
      const title = titleBySlug[slug] || topicKey;
      seenTitles[title] = true;
      const row = agg[topicKey];
      const wilson = row.attempts ? wilsonLower(row.correct, row.attempts, Z_95) : 0;
      const accuracy = row.attempts ? (row.correct / row.attempts) : 0;
      const cdata = chapters[title] || {};
      out.push({
        topic: title, slug: slug,
        attempts: row.attempts, correct: row.correct,
        accuracy: accuracy, wilson_lower: wilson,
        mastered_qids: row.mastered_qids, seen_qids: row.qids.length,
        last_seen_ts: row.last_seen_ts,
        exam_weight: cdata.exam_weight || null,
        weight_rank: _weightRank(cdata.exam_weight),
        bucket: _bucketFor(row)
      });
    });

    if (Array.isArray(allTopics)) {
      allTopics.forEach(function (t) {
        if (!t || !t.topic) return;
        if (seenTitles[t.topic]) return;
        const cdata = chapters[t.topic] || {};
        out.push({
          topic: t.topic, slug: t.slug || _slugify(t.topic),
          attempts: 0, correct: 0, accuracy: 0, wilson_lower: 0,
          mastered_qids: 0, seen_qids: 0, last_seen_ts: 0,
          exam_weight: cdata.exam_weight || null,
          weight_rank: _weightRank(cdata.exam_weight),
          bucket: 'untested'
        });
      });
    }
    return out;
  }

  function getReviewQueue(now, chapters) {
    now = (typeof now === 'number') ? now : Date.now();
    const due = getDueQuestions(now);
    if (due.length === 0) return [];
    const prog = loadProgress();
    chapters = chapters || {};
    const titleBySlug = {};
    Object.keys(chapters).forEach(function (title) { titleBySlug[_slugify(title)] = title; });
    return due.map(function (d) {
      const p = prog[d.qid] || {};
      const slug = _slugify(p.topic);
      const title = titleBySlug[slug] || p.topic || null;
      const cdata = title ? (chapters[title] || {}) : {};
      return {
        qid: d.qid, due_at: d.due_at, overdue_ms: d.overdue_ms,
        step: d.step, mastered: d.mastered,
        topic: title, topic_slug: slug,
        exam_weight: cdata.exam_weight || null,
        weight_rank: _weightRank(cdata.exam_weight)
      };
    }).sort(function (a, b) {
      if (b.overdue_ms !== a.overdue_ms) return b.overdue_ms - a.overdue_ms;
      return b.weight_rank - a.weight_rank;
    });
  }

  function getRecommendationReason(topicSlug) {
    if (!topicSlug) return 'topic: no data';
    const prog = loadProgress();
    const byTopic = _aggregateByTopic(prog);
    let row = byTopic[topicSlug];
    if (!row) {
      const match = Object.keys(byTopic).find(function (k) {
        return _slugify(k) === topicSlug || k === topicSlug;
      });
      if (match) row = byTopic[match];
    }
    if (!row || !row.attempts) return topicSlug + ': no attempts yet';
    const wilson = wilsonLower(row.correct, row.attempts, Z_95);
    return topicSlug + ': ' + row.correct + '/' + row.attempts + ' correct, last seen ' +
           _humanAgo(row.last_seen_ts, Date.now()) + ', Wilson=' + wilson.toFixed(2);
  }

  return {
    recordAnswer: recordAnswer,
    getWeakTopics: getWeakTopics,
    getDueQuestions: getDueQuestions,
    getReviewQueue: getReviewQueue,
    getTopicStates: getTopicStates,
    getRecommendationReason: getRecommendationReason,
    getStreak: getStreak,
    bumpStreak: bumpStreak,
    migrate: migrate,
    wilsonLower: wilsonLower,
    loadProgress: loadProgress,
    loadSrs: loadSrs,
    LS_KEYS: { progress: LS_PROGRESS, srs: LS_SRS, quiz: LS_QUIZ, streak: LS_STREAK },
    STEP_INTERVALS_DAYS: STEP_INTERVALS_DAYS,
    _resetAll: function () {
      try {
        if (typeof localStorage !== 'undefined') {
          [LS_PROGRESS, LS_SRS, LS_MIGRATED, LS_QUIZ, LS_STREAK].forEach(function (k) {
            localStorage.removeItem(k);
          });
        }
      } catch (e) {}
    }
  };
});

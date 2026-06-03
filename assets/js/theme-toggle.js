/* theme-toggle.js — day/night dial controller
 * Three states: 'light' | 'dark' | 'auto' (follow OS).
 * Persisted in localStorage.pde_theme. Long-press (700ms) toggles AUTO.
 * Pre-paint init lives inline in base.html <head> to prevent FOUC.
 */
(function () {
  var KEY = 'pde_theme';
  var LONG_PRESS_MS = 700;
  var root = document.documentElement;

  function readStored() {
    try { return localStorage.getItem(KEY) || 'auto'; } catch (e) { return 'auto'; }
  }
  function writeStored(v) {
    try { localStorage.setItem(KEY, v); } catch (e) {}
  }
  function systemTheme() {
    return window.matchMedia && window.matchMedia('(prefers-color-scheme: light)').matches
      ? 'light' : 'dark';
  }
  function effectiveTheme() {
    var explicit = root.getAttribute('data-theme');
    return explicit || systemTheme();
  }

  function applyTheme(mode, opts) {
    opts = opts || {};
    if (mode === 'auto') {
      root.removeAttribute('data-theme');
      root.classList.add('is-auto-theme');
    } else {
      root.setAttribute('data-theme', mode);
      root.classList.remove('is-auto-theme');
    }
    if (opts.persist !== false) writeStored(mode);
    updateLabel();
  }

  function updateLabel() {
    var label = document.querySelector('.theme-dial__label');
    if (!label) return;
    var stored = readStored();
    label.textContent = stored === 'auto' ? 'AUTO' : (effectiveTheme() === 'dark' ? 'NIGHT' : 'DAY');
  }

  function fireSweep(x, y, nextTheme) {
    if (window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
    var sweep = document.createElement('div');
    sweep.className = 'theme-sweep';
    sweep.style.setProperty('--sweep-x', x + 'px');
    sweep.style.setProperty('--sweep-y', y + 'px');
    sweep.style.setProperty('--sweep-color',
      nextTheme === 'dark' ? '#0b0f17' : '#f0f4f8');
    document.body.appendChild(sweep);
    setTimeout(function () { sweep.remove(); }, 700);
  }

  function init() {
    var dial = document.querySelector('.theme-dial');
    if (!dial) return;

    // Sync initial visual state (pre-paint script handled data-theme; ensure auto class + label)
    var stored = readStored();
    if (stored === 'auto') root.classList.add('is-auto-theme');
    updateLabel();

    var pressTimer = null;
    var longPressFired = false;

    dial.addEventListener('pointerdown', function () {
      longPressFired = false;
      dial.classList.add('is-pressing');
      pressTimer = setTimeout(function () {
        longPressFired = true;
        applyTheme('auto');
        dial.classList.remove('is-pressing');
        // brief flash on auto activation
        dial.animate(
          [{ transform: 'scale(1)' }, { transform: 'scale(1.18)' }, { transform: 'scale(1)' }],
          { duration: 260, easing: 'cubic-bezier(.4,0,.2,1)' }
        );
      }, LONG_PRESS_MS);
    });

    function endPress(e) {
      dial.classList.remove('is-pressing');
      if (pressTimer) { clearTimeout(pressTimer); pressTimer = null; }
      if (longPressFired) return; // auto already applied
      if (!e || e.type === 'pointerup') {
        var current = effectiveTheme();
        var next = current === 'dark' ? 'light' : 'dark';
        var rect = dial.getBoundingClientRect();
        var x = rect.left + rect.width / 2;
        var y = rect.top + rect.height / 2;
        fireSweep(x, y, next);
        applyTheme(next);
      }
    }
    dial.addEventListener('pointerup', endPress);
    dial.addEventListener('pointerleave', function () {
      dial.classList.remove('is-pressing');
      if (pressTimer) { clearTimeout(pressTimer); pressTimer = null; }
    });
    dial.addEventListener('pointercancel', function () {
      dial.classList.remove('is-pressing');
      if (pressTimer) { clearTimeout(pressTimer); pressTimer = null; }
    });

    // Keyboard support
    dial.addEventListener('keydown', function (e) {
      if (e.key === 'Enter' || e.key === ' ') {
        e.preventDefault();
        var current = effectiveTheme();
        var next = current === 'dark' ? 'light' : 'dark';
        var rect = dial.getBoundingClientRect();
        fireSweep(rect.left + rect.width / 2, rect.top + rect.height / 2, next);
        applyTheme(next);
      } else if (e.key.toLowerCase() === 'a') {
        e.preventDefault();
        applyTheme('auto');
      }
    });

    // React to system pref changes while in AUTO
    if (window.matchMedia) {
      var mq = window.matchMedia('(prefers-color-scheme: light)');
      var onChange = function () { if (readStored() === 'auto') updateLabel(); };
      if (mq.addEventListener) mq.addEventListener('change', onChange);
      else if (mq.addListener) mq.addListener(onChange);
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();

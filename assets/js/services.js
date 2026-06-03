/* services.js — /services tab controller.
 * Vanilla JS. Reads data from <script id="svc-data" type="application/json">.
 */
(function () {
  'use strict';

  var dataEl = document.getElementById('svc-data');
  if (!dataEl) return;

  var DATA;
  try { DATA = JSON.parse(dataEl.textContent || dataEl.innerText || '{}'); }
  catch (e) { console.error('services.js: bad data JSON', e); return; }

  var SERVICES   = DATA.services || {};
  var CATEGORIES = DATA.categories || [];
  var CAT_COLOR  = DATA.categoryColor || {};
  var IND_COLOR  = DATA.industryColor || {};

  var root           = document.querySelector('.pde-services');
  var searchInput    = document.getElementById('svc-search-input');
  var searchClear    = document.getElementById('svc-search-clear');
  var sectionTitle   = document.getElementById('svc-section-title');
  var sectionSub     = document.getElementById('svc-section-sub');
  var resultBar      = document.getElementById('svc-result-bar');
  var resultCount    = document.getElementById('svc-result-count');
  var resultContext  = document.getElementById('svc-result-context');
  var clearFilters   = document.getElementById('svc-clear-filters');
  var tagWrap        = document.getElementById('svc-tag-filters');
  var toolsHost      = document.getElementById('svc-tools');
  var casesHost      = document.getElementById('svc-cases');
  var emptyHost      = document.getElementById('svc-empty');

  var sideButtons    = root.querySelectorAll('.svc-cat[data-cat-id]');
  var mobileButtons  = root.querySelectorAll('.svc-mobile-cat[data-cat-id]');
  var tagButtons     = tagWrap ? tagWrap.querySelectorAll('.svc-tag[data-tag]') : [];

  // ── State ───────────────────────────────────────────────────────────
  var state = {
    tab: 'storage',
    filter: 'all',
    q: '',
    expanded: null
  };

  try {
    var saved = localStorage.getItem('pde_services_tab');
    if (saved && (SERVICES[saved] || saved === 'all')) state.tab = saved;
  } catch (e) {}

  // ── Helpers ─────────────────────────────────────────────────────────
  function allTools() {
    var out = [];
    Object.keys(SERVICES).forEach(function (k) {
      if (k !== 'cases') out = out.concat(SERVICES[k]);
    });
    return out;
  }

  function catLabel(id) {
    for (var i = 0; i < CATEGORIES.length; i++) {
      if (CATEGORIES[i].id === id) return CATEGORIES[i].label;
    }
    return id;
  }

  function findToolCategory(toolId) {
    var keys = Object.keys(SERVICES);
    for (var i = 0; i < keys.length; i++) {
      var k = keys[i];
      if (k === 'cases') continue;
      var arr = SERVICES[k];
      for (var j = 0; j < arr.length; j++) {
        if (arr[j].id === toolId) return k;
      }
    }
    return 'storage';
  }

  function escapeHtml(s) {
    return String(s == null ? '' : s)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;');
  }

  // SVG icons inline (lucide-shaped) — keeps things bundleless.
  var SVG = {
    chev:        '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"></polyline></svg>',
    scale:       '<svg viewBox="0 0 24 24" width="11" height="11" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m16 16 3-8 3 8c-.87.65-1.92 1-3 1s-2.13-.35-3-1z"></path><path d="m2 16 3-8 3 8c-.87.65-1.92 1-3 1s-2.13-.35-3-1z"></path><path d="M7 21h10"></path><path d="M12 3v18"></path><path d="M3 7h2c2 0 5-1 7-2 2 1 5 2 7 2h2"></path></svg>',
    zap:         '<svg viewBox="0 0 24 24" width="9" height="9" fill="currentColor" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"></polygon></svg>',
    shield:      '<svg viewBox="0 0 24 24" width="13" height="13" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path><line x1="12" y1="9" x2="12" y2="13"></line><line x1="12" y1="17" x2="12.01" y2="17"></line></svg>',
    dollar:      '<svg viewBox="0 0 24 24" width="13" height="13" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="12" y1="2" x2="12" y2="22"></line><path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"></path></svg>',
    terminal:    '<svg viewBox="0 0 24 24" width="13" height="13" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="4 17 10 11 4 5"></polyline><line x1="12" y1="19" x2="20" y2="19"></line></svg>',
    globe:       '<svg viewBox="0 0 24 24" width="13" height="13" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><line x1="2" y1="12" x2="22" y2="12"></line><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path></svg>',
    key:         '<svg viewBox="0 0 24 24" width="13" height="13" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="7.5" cy="15.5" r="5.5"></circle><path d="m21 2-9.6 9.6"></path><path d="m15.5 7.5 3 3L22 7l-3-3"></path></svg>',
    boxes:       '<svg viewBox="0 0 24 24" width="13" height="13" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2.97 12.92A2 2 0 0 0 2 14.63v3.24a2 2 0 0 0 .97 1.71l3 1.8a2 2 0 0 0 2.06 0L12 19.05V12L8.03 9.92a2 2 0 0 0-2.06 0z"></path><path d="m7 16.5-4.74-2.85"></path><path d="m7 16.5 5-3"></path><path d="M7 16.5v5.17"></path><path d="M12 13.06V19l3.97 2.38a2 2 0 0 0 2.06 0l3-1.8A2 2 0 0 0 22 17.87v-3.24a2 2 0 0 0-.97-1.71L17 10.92"></path></svg>',
    wrench:      '<svg viewBox="0 0 24 24" width="13" height="13" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"></path></svg>',
    ext:         '<svg viewBox="0 0 24 24" width="11" height="11" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path><polyline points="15 3 21 3 21 9"></polyline><line x1="10" y1="14" x2="21" y2="3"></line></svg>'
  };

  // ── Filtering ──────────────────────────────────────────────────────
  function filteredItems() {
    if (state.tab === 'cases') {
      var cases = SERVICES.cases || [];
      if (!state.q) return cases;
      var q = state.q;
      return cases.filter(function (i) {
        return (i.title || '').toLowerCase().indexOf(q) > -1
          || (i.company || '').toLowerCase().indexOf(q) > -1
          || (i.industry || '').toLowerCase().indexOf(q) > -1
          || (i.pde_takeaway || '').toLowerCase().indexOf(q) > -1;
      });
    }

    var isFiltered = state.q !== '' || state.filter !== 'all';
    var list = (isFiltered || state.tab === 'all') ? allTools() : (SERVICES[state.tab] || []);

    if (state.filter !== 'all') {
      list = list.filter(function (i) { return (i.tags || []).indexOf(state.filter) > -1; });
    }
    if (state.q) {
      var q2 = state.q;
      list = list.filter(function (i) {
        return (i.name || '').toLowerCase().indexOf(q2) > -1
          || (i.pde_snippet || '').toLowerCase().indexOf(q2) > -1
          || (i.best_for || '').toLowerCase().indexOf(q2) > -1;
      });
    }
    return list;
  }

  // ── Rendering ──────────────────────────────────────────────────────
  function renderTool(item) {
    var catKey = findToolCategory(item.id);
    var color  = CAT_COLOR[catKey] || 'blue';
    var isOpen = state.expanded === item.id;
    var isSv   = (item.managed || '').indexOf('Serverless') > -1;

    var pillHtml = isSv
      ? '<span class="svc-row__pill">' + SVG.zap + ' Serverless</span>'
      : '';

    var details = item.details || {};

    var head =
      '<button type="button" class="svc-row__head" data-row-toggle="' + escapeHtml(item.id) + '">' +
        '<span class="svc-row__icon">' + SVG.boxes + '</span>' +
        '<span class="svc-row__body">' +
          '<span class="svc-row__title-line">' +
            '<span class="svc-row__name">' + escapeHtml(item.name) + '</span>' +
            pillHtml +
          '</span>' +
          '<span class="svc-row__best">' + escapeHtml(item.best_for) + '</span>' +
        '</span>' +
        '<span class="svc-row__type">' + escapeHtml(item.type) + '</span>' +
        '<span class="svc-row__scale">' + SVG.scale + ' ' + escapeHtml(item.scaling) + '</span>' +
        '<span class="svc-row__chev">' + SVG.chev + '</span>' +
      '</button>';

    var detailRow = function (label, value, iconKey, iconClass) {
      if (!value) return '';
      return '' +
        '<div class="svc-detail-row">' +
          '<span class="svc-detail-row__icon ' + iconClass + '">' + SVG[iconKey] + '</span>' +
          '<div>' +
            '<p class="svc-detail-row__label">' + label + '</p>' +
            '<p class="svc-detail-row__value">' + escapeHtml(value) + '</p>' +
          '</div>' +
        '</div>';
    };

    var detail =
      '<div class="svc-row__detail">' +
        '<div class="svc-detail-grid">' +
          '<div>' +
            '<div class="svc-insight">' +
              '<p class="svc-insight__label">' + SVG.shield + ' Exam Insight</p>' +
              '<p class="svc-insight__body">' + escapeHtml(item.pde_snippet) + '</p>' +
            '</div>' +
            detailRow('Cost Model',         details.cost,         'dollar',   'svc-i--green') +
            detailRow('Coding Level',       details.coding,       'terminal', 'svc-i--blue') +
            detailRow('Availability / SLA', details.availability, 'globe',    'svc-i--indigo') +
          '</div>' +
          '<div>' +
            detailRow('Core IAM Roles',         details.iam,      'key',    'svc-i--purple') +
            detailRow('Open Source Equivalent', details.os_equiv, 'boxes',  'svc-i--slate') +
            detailRow('Common Troubleshooting', details.trouble,  'wrench', 'svc-i--red') +
            (item.url ? ('<a class="svc-detail-doc" href="' + escapeHtml(item.url) + '" target="_blank" rel="noopener noreferrer">Official Documentation ' + SVG.ext + '</a>') : '') +
          '</div>' +
        '</div>' +
      '</div>';

    return '' +
      '<div class="svc-row' + (isOpen ? ' is-open' : '') + '" data-row-id="' + escapeHtml(item.id) + '" data-color="' + color + '">' +
        head +
        detail +
      '</div>';
  }

  function renderCase(item) {
    var color = IND_COLOR[item.industry] || 'slate';
    return '' +
      '<article class="svc-case" data-color="' + color + '">' +
        '<div class="svc-case__meta">' +
          '<span class="svc-case__industry">' + escapeHtml(item.industry) + '</span>' +
          '<span class="svc-case__company">' + escapeHtml(item.company) + '</span>' +
        '</div>' +
        '<h3 class="svc-case__title">' + escapeHtml(item.title) + '</h3>' +
        '<div class="svc-case__arch">' +
          '<p class="svc-case__arch-label">Architecture</p>' +
          '<p class="svc-case__arch-body">' + escapeHtml(item.architecture) + '</p>' +
        '</div>' +
        '<div class="svc-case__takeaway">' +
          '<p class="svc-case__takeaway-label">' + SVG.shield + ' PDE Takeaway</p>' +
          '<p class="svc-case__takeaway-body">' + escapeHtml(item.pde_takeaway) + '</p>' +
        '</div>' +
        '<p class="svc-case__outcome">' + escapeHtml(item.outcome) + '</p>' +
        '<a class="svc-case__ref" href="' + escapeHtml(item.ref) + '" target="_blank" rel="noopener noreferrer">View case study ' + SVG.ext + '</a>' +
      '</article>';
  }

  function render() {
    // Sidebar active
    sideButtons.forEach(function (b) {
      b.classList.toggle('is-active', b.dataset.catId === state.tab);
    });
    mobileButtons.forEach(function (b) {
      b.classList.toggle('is-active', b.dataset.catId === state.tab);
    });

    // Tag active
    tagButtons.forEach(function (b) {
      b.classList.toggle('is-active', b.dataset.tag === state.filter);
    });

    // Header text
    sectionTitle.textContent = catLabel(state.tab);
    if (state.tab === 'cases') {
      sectionSub.textContent = 'Real company architectures mapped to PDE exam concepts.';
    } else if (state.tab === 'all') {
      sectionSub.textContent = 'Every GCP service covered in the Professional Data Engineer exam, in one place.';
    } else {
      sectionSub.textContent = 'Key services, exam insights, and decision frameworks for the Professional Data Engineer certification.';
    }

    // Tag bar visibility (hide on cases)
    tagWrap.classList.toggle('hidden', state.tab === 'cases');

    var items = filteredItems();
    var isFiltered = state.q !== '' || state.filter !== 'all';

    // Result bar
    if (isFiltered) {
      resultBar.classList.remove('hidden');
      resultCount.textContent = items.length + ' result' + (items.length === 1 ? '' : 's');
      var ctx = '';
      if (state.q)            ctx += ' for "' + searchInput.value + '"';
      if (state.filter !== 'all') ctx += ' · filtered by ' + state.filter;
      resultContext.textContent = ctx;
    } else {
      resultBar.classList.add('hidden');
    }

    // Lists
    if (state.tab === 'cases') {
      toolsHost.classList.add('hidden');
      casesHost.classList.remove('hidden');
      casesHost.innerHTML = items.map(renderCase).join('');
    } else {
      casesHost.classList.add('hidden');
      toolsHost.classList.remove('hidden');
      toolsHost.innerHTML = items.map(renderTool).join('');
    }

    emptyHost.classList.toggle('hidden', items.length > 0);
    toolsHost.classList.toggle('hidden', state.tab === 'cases' || items.length === 0);
    casesHost.classList.toggle('hidden', state.tab !== 'cases' || items.length === 0);

    searchClear.classList.toggle('hidden', !state.q);
  }

  // ── Events ─────────────────────────────────────────────────────────
  function setTab(tab) {
    state.tab = tab;
    state.filter = 'all';
    state.expanded = null;
    try { localStorage.setItem('pde_services_tab', tab); } catch (e) {}
    render();
  }

  sideButtons.forEach(function (b) {
    b.addEventListener('click', function () { setTab(b.dataset.catId); });
  });
  mobileButtons.forEach(function (b) {
    b.addEventListener('click', function () { setTab(b.dataset.catId); });
  });

  tagButtons.forEach(function (b) {
    b.addEventListener('click', function () {
      state.filter = b.dataset.tag;
      render();
    });
  });

  var searchDeb;
  searchInput.addEventListener('input', function () {
    clearTimeout(searchDeb);
    searchDeb = setTimeout(function () {
      state.q = (searchInput.value || '').toLowerCase().trim();
      render();
    }, 150);
  });
  searchClear.addEventListener('click', function () {
    searchInput.value = '';
    state.q = '';
    render();
    searchInput.focus();
  });
  clearFilters.addEventListener('click', function () {
    searchInput.value = '';
    state.q = '';
    state.filter = 'all';
    render();
  });

  // Row expand delegation
  toolsHost.addEventListener('click', function (e) {
    var btn = e.target.closest && e.target.closest('[data-row-toggle]');
    if (!btn) return;
    var id = btn.getAttribute('data-row-toggle');
    state.expanded = (state.expanded === id) ? null : id;
    render();
  });

  // Init
  render();
})();

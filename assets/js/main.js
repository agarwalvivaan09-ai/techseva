// TechSeva — site behaviour
(function () {
  // Mobile nav
  var toggle = document.querySelector('.nav-toggle');
  var links = document.querySelector('.nav-links');
  if (toggle && links) {
    toggle.addEventListener('click', function () {
      var open = links.classList.toggle('open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  }

  // Reveal on scroll
  var els = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } });
    }, { threshold: 0.12 });
    els.forEach(function (el) { io.observe(el); });
  } else { els.forEach(function (el) { el.classList.add('in'); }); }

  // Count-up stats
  document.querySelectorAll('[data-count]').forEach(function (el) {
    var target = parseFloat(el.getAttribute('data-count'));
    var suffix = el.getAttribute('data-suffix') || '';
    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
    var started = false;
    var run = function () {
      if (started) return; started = true;
      var t0 = performance.now(), dur = 1400;
      (function tick(now) {
        var p = Math.min(1, (now - t0) / dur), v = Math.round(target * (1 - Math.pow(1 - p, 3)));
        el.textContent = v + suffix;
        if (p < 1) requestAnimationFrame(tick);
      })(t0);
    };
    if ('IntersectionObserver' in window) {
      new IntersectionObserver(function (en, obs) { if (en[0].isIntersecting) { run(); obs.disconnect(); } }).observe(el);
    }
  });

  // Gallery photos: show placeholder icon if a photo file is missing
  document.querySelectorAll('.shot img').forEach(function (img) {
    var fail = function () { img.remove(); };
    if (img.complete && img.naturalWidth === 0) fail(); else img.addEventListener('error', fail);
  });

  // Forms -> pre-filled email (static site, no server)
  document.querySelectorAll('form[data-mailto]').forEach(function (form) {
    form.addEventListener('submit', function (ev) {
      ev.preventDefault();
      if (!form.reportValidity()) return;
      var to = form.getAttribute('data-mailto');
      var subject = form.getAttribute('data-subject') || 'TechSeva enquiry';
      var lines = [];
      new FormData(form).forEach(function (val, key) {
        if (String(val).trim()) lines.push(key + ': ' + val);
      });
      var name = form.querySelector('[name="Name"]');
      if (name && name.value) subject += ' — ' + name.value;
      window.location.href = 'mailto:' + to + '?subject=' + encodeURIComponent(subject) + '&body=' + encodeURIComponent(lines.join('\n'));
      var note = form.querySelector('.form-status');
      if (note) note.textContent = 'Your email app should now open with the details filled in. Just press send — we reply within 48 hours.';
    });
  });

  var y = document.getElementById('year'); if (y) y.textContent = new Date().getFullYear();
})();

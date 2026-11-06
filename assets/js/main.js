// TechSeva — site behaviour
(function () {
  var reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // ---------- Neural-network background ----------
  var cv = document.getElementById('net');
  if (cv && cv.getContext) {
    var ctx = cv.getContext('2d'), nodes = [], W, H, dpr, mouse = { x: -9999, y: -9999 };
    var cols = [[107, 228, 255], [139, 132, 255], [200, 123, 255], [255, 111, 181]];
    function colAt(x) {
      var t = Math.max(0, Math.min(.999, x / W)) * (cols.length - 1), i = Math.floor(t), f = t - i;
      var a = cols[i], b = cols[i + 1];
      return [a[0] + (b[0] - a[0]) * f, a[1] + (b[1] - a[1]) * f, a[2] + (b[2] - a[2]) * f];
    }
    function size() {
      dpr = Math.min(window.devicePixelRatio || 1, 2);
      W = window.innerWidth; H = window.innerHeight;
      cv.width = W * dpr; cv.height = H * dpr; ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
      var n = Math.round(Math.min(90, Math.max(34, W * H / 17000)));
      nodes = [];
      for (var i = 0; i < n; i++) nodes.push({ x: Math.random() * W, y: Math.random() * H, vx: (Math.random() - .5) * .22, vy: (Math.random() - .5) * .22, r: Math.random() * 1.4 + .6 });
    }
    var LINK = 150;
    function draw() {
      ctx.clearRect(0, 0, W, H);
      for (var i = 0; i < nodes.length; i++) {
        var a = nodes[i];
        a.x += a.vx; a.y += a.vy;
        if (a.x < -20) a.x = W + 20; if (a.x > W + 20) a.x = -20;
        if (a.y < -20) a.y = H + 20; if (a.y > H + 20) a.y = -20;
        for (var j = i + 1; j < nodes.length; j++) {
          var b = nodes[j], dx = a.x - b.x, dy = a.y - b.y, d = Math.sqrt(dx * dx + dy * dy);
          if (d < LINK) {
            var c = colAt((a.x + b.x) / 2);
            ctx.strokeStyle = 'rgba(' + (c[0] | 0) + ',' + (c[1] | 0) + ',' + (c[2] | 0) + ',' + (1 - d / LINK) * .36 + ')';
            ctx.lineWidth = .8; ctx.beginPath(); ctx.moveTo(a.x, a.y); ctx.lineTo(b.x, b.y); ctx.stroke();
          }
        }
        var md = Math.hypot(a.x - mouse.x, a.y - mouse.y);
        if (md < 180) {
          var cm = colAt(a.x);
          ctx.strokeStyle = 'rgba(' + (cm[0] | 0) + ',' + (cm[1] | 0) + ',' + (cm[2] | 0) + ',' + (1 - md / 180) * .45 + ')';
          ctx.beginPath(); ctx.moveTo(a.x, a.y); ctx.lineTo(mouse.x, mouse.y); ctx.stroke();
        }
        var cc = colAt(a.x);
        ctx.fillStyle = 'rgba(' + (cc[0] | 0) + ',' + (cc[1] | 0) + ',' + (cc[2] | 0) + ',.85)';
        ctx.beginPath(); ctx.arc(a.x, a.y, a.r, 0, 6.283); ctx.fill();
      }
    }
    var running = true;
    function loop() { if (running) draw(); requestAnimationFrame(loop); }
    size(); window.addEventListener('resize', size);
    window.addEventListener('pointermove', function (e) { mouse.x = e.clientX; mouse.y = e.clientY; });
    document.addEventListener('visibilitychange', function () { running = !document.hidden; });
    if (reduced) draw(); else loop();
  }

  // ---------- Mobile nav ----------
  var toggle = document.querySelector('.nav-toggle'), links = document.querySelector('.nav-links');
  if (toggle && links) toggle.addEventListener('click', function () {
    var open = links.classList.toggle('open'); toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
  });

  // ---------- Reveal ----------
  var els = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (en) {
      en.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } });
    }, { threshold: .1 });
    els.forEach(function (el) { io.observe(el); });
  } else els.forEach(function (el) { el.classList.add('in'); });

  // ---------- Gallery: hide missing photos ----------
  document.querySelectorAll('.shot img').forEach(function (img) {
    if (img.complete && img.naturalWidth === 0) img.remove(); else img.addEventListener('error', function () { img.remove(); });
  });

  // ---------- Forms -> pre-filled email ----------
  document.querySelectorAll('form[data-mailto]').forEach(function (form) {
    form.addEventListener('submit', function (ev) {
      ev.preventDefault();
      if (!form.reportValidity()) return;
      var subject = form.getAttribute('data-subject') || 'TechSeva enquiry', lines = [];
      new FormData(form).forEach(function (v, k) { if (String(v).trim()) lines.push(k + ': ' + v); });
      var n = form.querySelector('[name="Name"]'); if (n && n.value) subject += ' - ' + n.value;
      location.href = 'mailto:' + form.getAttribute('data-mailto') + '?subject=' + encodeURIComponent(subject) + '&body=' + encodeURIComponent(lines.join('\n'));
      var s = form.querySelector('.form-status');
      if (s) s.textContent = 'Your email app should open with everything filled in. Just press send.';
    });
  });

  var y = document.getElementById('year'); if (y) y.textContent = new Date().getFullYear();
})();

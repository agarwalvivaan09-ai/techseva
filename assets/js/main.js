// TechSeva — site behaviour
(function () {
  var reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // ---------- Neural-network background ----------
  var cv = document.getElementById('net');
  if (cv && cv.getContext) {
    var ctx = cv.getContext('2d'), nodes = [], pulses = [], waves = [], W, H, dpr, BASE_N;
    var mouse = { x: -9999, y: -9999, active: false };
    var cols = [[107, 228, 255], [139, 132, 255], [200, 123, 255], [255, 111, 181]];
    var LINK = 150, MR = 200;
    function colAt(x) {
      var t = Math.max(0, Math.min(.999, x / W)) * (cols.length - 1), i = Math.floor(t), f = t - i;
      var a = cols[i], b = cols[i + 1];
      return (a[0] + (b[0] - a[0]) * f | 0) + ',' + (a[1] + (b[1] - a[1]) * f | 0) + ',' + (a[2] + (b[2] - a[2]) * f | 0);
    }
    function mk(x, y, burst) {
      var ang = Math.random() * 6.283, sp = burst ? 1.5 + Math.random() * 2 : 0;
      var bvx = (Math.random() - .5) * .25, bvy = (Math.random() - .5) * .25;
      return { x: x, y: y, bvx: bvx, bvy: bvy, vx: bvx + Math.cos(ang) * sp, vy: bvy + Math.sin(ang) * sp, r: Math.random() * 1.3 + .7, life: burst ? 900 : -1, glow: 0 };
    }
    function size() {
      dpr = Math.min(window.devicePixelRatio || 1, 2);
      W = window.innerWidth; H = window.innerHeight;
      cv.width = W * dpr; cv.height = H * dpr; ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
      BASE_N = Math.round(Math.min(95, Math.max(36, W * H / 16000)));
      nodes = [];
      for (var i = 0; i < BASE_N; i++) nodes.push(mk(Math.random() * W, Math.random() * H));
    }
    function draw() {
      ctx.clearRect(0, 0, W, H);
      // shockwaves
      for (var w = waves.length - 1; w >= 0; w--) {
        var wv = waves[w]; wv.r += 7; wv.a *= .955;
        if (wv.a < .02) { waves.splice(w, 1); continue; }
        ctx.strokeStyle = 'rgba(' + colAt(wv.x) + ',' + wv.a + ')'; ctx.lineWidth = 1.2;
        ctx.beginPath(); ctx.arc(wv.x, wv.y, wv.r, 0, 6.283); ctx.stroke();
      }
      for (var i = nodes.length - 1; i >= 0; i--) {
        var n = nodes[i];
        if (n.life > 0 && --n.life === 0) { nodes.splice(i, 1); continue; }
        // mouse attraction (gentle, with orbit)
        if (mouse.active) {
          var dx = mouse.x - n.x, dy = mouse.y - n.y, d = Math.sqrt(dx * dx + dy * dy);
          if (d < MR && d > 1) {
            var f = (1 - d / MR) * .045;
            n.vx += dx / d * f - dy / d * f * .6; n.vy += dy / d * f + dx / d * f * .6;
            n.glow = Math.min(1, n.glow + .08);
          }
        }
        for (var k = 0; k < waves.length; k++) {
          var wv2 = waves[k], ex = n.x - wv2.x, ey = n.y - wv2.y, ed = Math.sqrt(ex * ex + ey * ey);
          if (Math.abs(ed - wv2.r) < 18 && ed > 1) { n.vx += ex / ed * wv2.a * 1.6; n.vy += ey / ed * wv2.a * 1.6; n.glow = 1; }
        }
        n.vx += (n.bvx - n.vx) * .03; n.vy += (n.bvy - n.vy) * .03;
        n.x += n.vx; n.y += n.vy; n.glow *= .97;
        if (n.x < -30) n.x = W + 30; if (n.x > W + 30) n.x = -30;
        if (n.y < -30) n.y = H + 30; if (n.y > H + 30) n.y = -30;
      }
      ctx.lineWidth = .8;
      for (i = 0; i < nodes.length; i++) {
        var a = nodes[i];
        for (var j = i + 1; j < nodes.length; j++) {
          var b = nodes[j], ddx = a.x - b.x, ddy = a.y - b.y, dd = ddx * ddx + ddy * ddy;
          if (dd < LINK * LINK) {
            var dist = Math.sqrt(dd), al = (1 - dist / LINK) * (.3 + Math.max(a.glow, b.glow) * .5);
            ctx.strokeStyle = 'rgba(' + colAt((a.x + b.x) / 2) + ',' + al + ')';
            ctx.beginPath(); ctx.moveTo(a.x, a.y); ctx.lineTo(b.x, b.y); ctx.stroke();
            if (pulses.length < 14 && Math.random() < .0004) pulses.push({ a: a, b: b, t: 0 });
          }
        }
        if (mouse.active) {
          var md = Math.hypot(a.x - mouse.x, a.y - mouse.y);
          if (md < MR) {
            ctx.strokeStyle = 'rgba(' + colAt(a.x) + ',' + (1 - md / MR) * .55 + ')';
            ctx.beginPath(); ctx.moveTo(a.x, a.y); ctx.lineTo(mouse.x, mouse.y); ctx.stroke();
          }
        }
      }
      // nodes
      for (i = 0; i < nodes.length; i++) {
        var c = nodes[i], cc = colAt(c.x);
        if (c.glow > .05) {
          ctx.fillStyle = 'rgba(' + cc + ',' + c.glow * .18 + ')';
          ctx.beginPath(); ctx.arc(c.x, c.y, c.r + 6 * c.glow, 0, 6.283); ctx.fill();
        }
        ctx.fillStyle = 'rgba(' + cc + ',' + (.75 + c.glow * .25) + ')';
        ctx.beginPath(); ctx.arc(c.x, c.y, c.r + c.glow, 0, 6.283); ctx.fill();
      }
      // data pulses travelling along links
      for (var p = pulses.length - 1; p >= 0; p--) {
        var pu = pulses[p]; pu.t += .018;
        var px = pu.a.x + (pu.b.x - pu.a.x) * pu.t, py = pu.a.y + (pu.b.y - pu.a.y) * pu.t;
        if (pu.t >= 1 || Math.hypot(pu.a.x - pu.b.x, pu.a.y - pu.b.y) > LINK) { pu.b.glow = 1; pulses.splice(p, 1); continue; }
        var pc = colAt(px);
        ctx.fillStyle = 'rgba(' + pc + ',.25)'; ctx.beginPath(); ctx.arc(px, py, 5, 0, 6.283); ctx.fill();
        ctx.fillStyle = 'rgba(255,255,255,.95)'; ctx.beginPath(); ctx.arc(px, py, 1.6, 0, 6.283); ctx.fill();
      }
      // cursor node
      if (mouse.active) {
        var mc = colAt(mouse.x);
        ctx.fillStyle = 'rgba(' + mc + ',.2)'; ctx.beginPath(); ctx.arc(mouse.x, mouse.y, 7, 0, 6.283); ctx.fill();
        ctx.fillStyle = 'rgba(' + mc + ',.95)'; ctx.beginPath(); ctx.arc(mouse.x, mouse.y, 2.2, 0, 6.283); ctx.fill();
      }
    }
    var running = true;
    function loop() { if (running) draw(); requestAnimationFrame(loop); }
    size(); window.addEventListener('resize', size);
    window.addEventListener('pointermove', function (e) { mouse.x = e.clientX; mouse.y = e.clientY; mouse.active = e.pointerType === 'mouse' || e.pointerType === 'pen'; }, { passive: true });
    document.addEventListener('pointerleave', function () { mouse.active = false; });
    document.documentElement.addEventListener('mouseleave', function () { mouse.active = false; });
    window.addEventListener('pointerdown', function (e) {
      if (e.target.closest('a,button,input,select,textarea,label,[data-blob]')) return;
      waves.push({ x: e.clientX, y: e.clientY, r: 4, a: .6 });
      for (var s = 0; s < 6; s++) nodes.push(mk(e.clientX, e.clientY, true));
      if (nodes.length > BASE_N + 40) nodes.splice(BASE_N, nodes.length - BASE_N - 40);
    });
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

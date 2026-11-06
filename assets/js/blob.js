// TechSeva — iridescent 3D blob (three.js). Mounts on every [data-blob] element.
(function () {
  if (!window.THREE) return;
  var THREE = window.THREE;
  var t = document.createElement('canvas');
  if (!(t.getContext('webgl') || t.getContext('experimental-webgl'))) return;
  var reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  var noise = [
    'vec3 mod289(vec3 x){return x-floor(x*(1./289.))*289.;}',
    'vec4 mod289(vec4 x){return x-floor(x*(1./289.))*289.;}',
    'vec4 permute(vec4 x){return mod289(((x*34.)+1.)*x);}',
    'vec4 taylorInvSqrt(vec4 r){return 1.79284291400159-.85373472095314*r;}',
    'float snoise(vec3 v){const vec2 C=vec2(1./6.,1./3.);const vec4 D=vec4(0.,.5,1.,2.);',
    'vec3 i=floor(v+dot(v,C.yyy));vec3 x0=v-i+dot(i,C.xxx);vec3 g=step(x0.yzx,x0.xyz);vec3 l=1.-g;',
    'vec3 i1=min(g.xyz,l.zxy);vec3 i2=max(g.xyz,l.zxy);vec3 x1=x0-i1+C.xxx;vec3 x2=x0-i2+C.yyy;vec3 x3=x0-D.yyy;',
    'i=mod289(i);vec4 p=permute(permute(permute(i.z+vec4(0.,i1.z,i2.z,1.))+i.y+vec4(0.,i1.y,i2.y,1.))+i.x+vec4(0.,i1.x,i2.x,1.));',
    'float n_=.142857142857;vec3 ns=n_*D.wyz-D.xzx;vec4 j=p-49.*floor(p*ns.z*ns.z);vec4 x_=floor(j*ns.z);vec4 y_=floor(j-7.*x_);',
    'vec4 x=x_*ns.x+ns.yyyy;vec4 y=y_*ns.x+ns.yyyy;vec4 h=1.-abs(x)-abs(y);vec4 b0=vec4(x.xy,y.xy);vec4 b1=vec4(x.zw,y.zw);',
    'vec4 s0=floor(b0)*2.+1.;vec4 s1=floor(b1)*2.+1.;vec4 sh=-step(h,vec4(0.));vec4 a0=b0.xzyw+s0.xzyw*sh.xxyy;vec4 a1=b1.xzyw+s1.xzyw*sh.zzww;',
    'vec3 p0=vec3(a0.xy,h.x);vec3 p1=vec3(a0.zw,h.y);vec3 p2=vec3(a1.xy,h.z);vec3 p3=vec3(a1.zw,h.w);',
    'vec4 norm=taylorInvSqrt(vec4(dot(p0,p0),dot(p1,p1),dot(p2,p2),dot(p3,p3)));p0*=norm.x;p1*=norm.y;p2*=norm.z;p3*=norm.w;',
    'vec4 m=max(.6-vec4(dot(x0,x0),dot(x1,x1),dot(x2,x2),dot(x3,x3)),0.);m=m*m;',
    'return 42.*dot(m*m,vec4(dot(p0,x0),dot(p1,x1),dot(p2,x2),dot(p3,x3)));}'
  ].join('\n');

  var vert = noise + [
    'uniform float uTime; uniform vec3 uMouse; uniform float uHover; uniform float uAmp;',
    'varying vec3 vPos; varying vec3 vView; varying vec3 vObj;',
    'void main(){',
    '  vec3 p = position; vec3 dir = normalize(position);',
    '  float n = snoise(p*0.62 + vec3(uTime*.12, uTime*.08, 0.)) * .36 * uAmp;',
    '  n += snoise(p*1.3 - vec3(0., uTime*.1, uTime*.06)) * .07 * uAmp;',
    '  float m = pow(max(dot(dir, uMouse), 0.), 5.);',
    '  n += m * .38 * uHover;',
    '  n += snoise(p*3. + uTime*.6) * .03 * uHover * m;',
    '  p += normal * n;',
    '  vObj = p;',
    '  vec4 mv = modelViewMatrix * vec4(p, 1.);',
    '  vPos = mv.xyz; vView = -mv.xyz;',
    '  gl_Position = projectionMatrix * mv;',
    '}'
  ].join('\n');

  var frag = [
    'uniform float uTime; uniform float uHover;',
    'varying vec3 vPos; varying vec3 vView; varying vec3 vObj;',
    'vec3 C1=vec3(.42,.89,1.), C2=vec3(.54,.52,1.), C3=vec3(.78,.48,1.), C4=vec3(1.,.45,.72);',
    'vec3 pal(float t){',
    '  t = clamp(t, 0., 1.) * 3.;',
    '  vec3 a = mix(C1, C2, smoothstep(0., 1., t));',
    '  a = mix(a, C3, smoothstep(1., 2., t));',
    '  return mix(a, C4, smoothstep(2., 3., t));',
    '}',
    'void main(){',
    '  vec3 n = normalize(cross(dFdx(vPos), dFdy(vPos)));',
    '  vec3 v = normalize(vView);',
    '  float ndv = max(dot(n, v), 0.);',
    '  float fr = pow(1. - ndv, 2.4);',
    '  float t = .5 + .5*sin(n.y*2.3 + n.x*1.7 + fr*2.6 + uTime*.25 + vObj.z*.9);',
    '  vec3 base = pal(t);',
    '  vec3 film = pal(.5 + .5*sin(ndv*5. - uTime*.3 + vObj.x));',
    '  vec3 col = mix(base, film, .22);',
    '  vec3 L = normalize(vec3(-.45, .75, .7));',
    '  float diff = .35 + .65*max(dot(n, L), 0.);',
    '  col = mix(col * vec3(.32, .26, .62), col, diff);',
    '  vec3 H = normalize(L + v);',
    '  float nh = max(dot(n, H), 0.);',
    '  col += vec3(1.) * pow(nh, 110.) * .7;',
    '  col += vec3(.85,.92,1.) * pow(nh, 14.) * .1;',
    '  vec3 L2 = normalize(vec3(.6, -.5, .4));',
    '  col += mix(C1, C4, .5+.5*sin(uTime*.2)) * pow(max(dot(n, normalize(L2+v)), 0.), 18.) * .22;',
    '  col = mix(col, mix(C1, C3, .5 + .5*n.x), fr * .45);',
    '  col += C2 * uHover * fr * .25;',
    '  col = col / (col + vec3(.75)) * 1.55;',
    '  float a = smoothstep(0., .18, ndv) * .12 + .88;',
    '  gl_FragColor = vec4(col, a);',
    '}'
  ].join('\n');

  var mouse = { x: 0, y: 0, cx: -1e4, cy: -1e4 };
  window.addEventListener('pointermove', function (e) {
    mouse.cx = e.clientX; mouse.cy = e.clientY;
    mouse.x = e.clientX / window.innerWidth - .5; mouse.y = e.clientY / window.innerHeight - .5;
  }, { passive: true });

  function mount(el) {
    var mini = el.getAttribute('data-blob') === 'mini';
    var renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true, premultipliedAlpha: false });
    renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, mini ? 3 : 2));
    var scene = new THREE.Scene();
    var camera = new THREE.PerspectiveCamera(35, 1, .1, 100);
    camera.position.z = mini ? 4.6 : 5.2;
    var uniforms = { uTime: { value: 0 }, uMouse: { value: new THREE.Vector3(0, 0, 1) }, uHover: { value: 0 }, uAmp: { value: 1 } };
    var mat = new THREE.ShaderMaterial({ extensions: { derivatives: true }, uniforms: uniforms, vertexShader: vert, fragmentShader: frag, transparent: true });
    var mesh = new THREE.Mesh(new THREE.IcosahedronGeometry(1.15, mini ? 28 : 72), mat);
    scene.add(mesh);
    el.innerHTML = ''; el.appendChild(renderer.domElement);
    el.classList.add('live');

    function resize() { var s = el.clientWidth; renderer.setSize(s, s, false); }
    resize(); window.addEventListener('resize', resize);

    // drag to spin (big blob only)
    var rotY = 0, rotX = .25, velY = mini ? .9 : .15, velX = 0, dragging = false, lx = 0, ly = 0, hoverT = 0, scale = 1;
    if (!mini) {
      el.addEventListener('pointerdown', function (e) { dragging = true; lx = e.clientX; ly = e.clientY; el.setPointerCapture(e.pointerId); el.classList.add('grab'); });
      el.addEventListener('pointermove', function (e) {
        if (!dragging) return;
        velY = (e.clientX - lx) * .006; velX = (e.clientY - ly) * .006; lx = e.clientX; ly = e.clientY;
      });
      var up = function () { dragging = false; el.classList.remove('grab'); };
      el.addEventListener('pointerup', up); el.addEventListener('pointercancel', up);
    } else {
      var a = el.closest('a') || el;
      a.addEventListener('pointerenter', function () { hoverT = 1; });
      a.addEventListener('pointerleave', function () { hoverT = 0; });
    }

    var visible = true;
    if ('IntersectionObserver' in window) new IntersectionObserver(function (en) { visible = en[0].isIntersecting; }).observe(el);

    var t0 = performance.now(), last = t0, q = new THREE.Quaternion(), dir = new THREE.Vector3();
    function frame(now) {
      requestAnimationFrame(frame);
      if (!visible || document.hidden) { last = now; return; }
      var dt = Math.min(.05, (now - last) / 1000); last = now;
      var time = (now - t0) / 1000;
      uniforms.uTime.value = time;

      var r = el.getBoundingClientRect();
      var ccx = r.left + r.width / 2, ccy = r.top + r.height / 2;
      var mx = (mouse.cx - ccx) / (r.width / 2), my = -(mouse.cy - ccy) / (r.height / 2);
      var dist = Math.sqrt(mx * mx + my * my);
      if (!mini) hoverT = dist < 1.15 ? 1 : Math.max(0, 1 - (dist - 1.15) * 1.5);
      uniforms.uHover.value += (hoverT - uniforms.uHover.value) * .08;

      // mouse direction in object space -> bulge toward cursor
      dir.set(mx, my, mini ? 1.2 : .9).normalize();
      q.copy(mesh.quaternion).invert();
      dir.applyQuaternion(q);
      uniforms.uMouse.value.lerp(dir, .15).normalize();

      if (!dragging) {
        var baseVel = mini ? .9 : .18;
        velY += (baseVel * dt - velY) * .04 + (mini ? 0 : mouse.x * .0006);
        velX *= .94;
      }
      rotY += velY; rotX += velX;
      rotX += ((mini ? .25 : .25 + mouse.y * .5) - rotX) * .03;
      mesh.rotation.set(rotX, rotY, 0);
      var target = 1 + uniforms.uHover.value * (mini ? .08 : .04);
      scale += (target - scale) * .1; mesh.scale.setScalar(scale);
      renderer.render(scene, camera);
    }
    if (reduced) { uniforms.uTime.value = 2; mesh.rotation.set(.25, .4, 0); renderer.render(scene, camera); }
    else requestAnimationFrame(frame);
  }

  document.querySelectorAll('[data-blob]').forEach(function (el) {
    var fallback = el.innerHTML;
    try {
      mount(el);
      var c = el.querySelector('canvas');
      if (c) c.addEventListener('webglcontextlost', function () { el.innerHTML = fallback; el.classList.remove('live'); });
    } catch (e) { el.innerHTML = fallback; el.classList.remove('live'); }
  });
})();

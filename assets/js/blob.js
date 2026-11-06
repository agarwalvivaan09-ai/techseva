// TechSeva — iridescent 3D blob (three.js)
(function () {
  var wrap = document.getElementById('blob');
  if (!wrap || !window.THREE) return;
  var THREE = window.THREE;
  var test = document.createElement('canvas');
  if (!(test.getContext('webgl') || test.getContext('experimental-webgl'))) return;

  var renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
  renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, 2));
  var scene = new THREE.Scene();
  var camera = new THREE.PerspectiveCamera(35, 1, .1, 100);
  camera.position.z = 5.2;

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

  var mat = new THREE.ShaderMaterial({
    extensions: { derivatives: true },
    uniforms: { uTime: { value: 0 } },
    vertexShader: noise + [
      'uniform float uTime; varying vec3 vPos; varying vec3 vView;',
      'void main(){',
      '  vec3 p = position;',
      '  float n = snoise(p*0.62 + vec3(uTime*.12, uTime*.08, 0.)) * .38;',
      '  n += snoise(p*1.3 - vec3(0., uTime*.1, uTime*.06)) * .07;',
      '  p += normal * n;',
      '  vec4 mv = modelViewMatrix * vec4(p, 1.);',
      '  vPos = mv.xyz; vView = -mv.xyz;',
      '  gl_Position = projectionMatrix * mv;',
      '}'
    ].join('\n'),
    fragmentShader: [
      'varying vec3 vPos; varying vec3 vView;',
      'vec3 pal(float t){',
      '  vec3 c1=vec3(.42,.89,1.), c2=vec3(.55,.52,1.), c3=vec3(.78,.48,1.), c4=vec3(1.,.44,.71);',
      '  t=(.5+.5*sin(t*3.14159))*2.999;',
      '  if(t<1.) return mix(c1,c2,t); if(t<2.) return mix(c2,c3,t-1.); return mix(c3,c4,t-2.);',
      '}',
      'void main(){',
      '  vec3 n = normalize(cross(dFdx(vPos), dFdy(vPos)));',
      '  vec3 v = normalize(vView);',
      '  float fr = pow(1. - max(dot(n, v), 0.), 2.2);',
      '  float t = n.y*.45 + n.x*.3 + fr*.7 - .1;',
      '  vec3 col = pal(t);',
      '  col = mix(col, vec3(.06,.05,.2), (1.-fr)*.15);',
      '  vec3 L = normalize(vec3(-.4, .7, .8));',
      '  vec3 H = normalize(L + v);',
      '  float spec = pow(max(dot(n, H), 0.), 60.);',
      '  float soft = pow(max(dot(n, H), 0.), 8.) * .25;',
      '  col += vec3(1.) * (spec*.9 + soft);',
      '  col += pal(t+.6) * fr * .25;',
      '  gl_FragColor = vec4(col, 1.);',
      '}'
    ].join('\n')
  });

  var mesh = new THREE.Mesh(new THREE.IcosahedronGeometry(1.15, 64), mat);
  scene.add(mesh);
  wrap.innerHTML = '';
  wrap.appendChild(renderer.domElement);

  function resize() { var s = wrap.clientWidth; renderer.setSize(s, s, false); }
  resize(); window.addEventListener('resize', resize);

  var tx = 0, ty = 0;
  window.addEventListener('pointermove', function (e) {
    tx = (e.clientX / window.innerWidth - .5) * .6; ty = (e.clientY / window.innerHeight - .5) * .6;
  });
  var reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var t0 = performance.now();
  function frame(now) {
    var t = (now - t0) / 1000;
    mat.uniforms.uTime.value = reduced ? 2 : t;
    mesh.rotation.y += ((reduced ? 0 : t * .15) + tx - mesh.rotation.y) * .05;
    mesh.rotation.x += (ty + .25 - mesh.rotation.x) * .05;
    renderer.render(scene, camera);
    if (!reduced) requestAnimationFrame(frame);
  }
  requestAnimationFrame(frame);
})();

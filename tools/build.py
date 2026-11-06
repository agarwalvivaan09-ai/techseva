#!/usr/bin/env python3
"""Generates the TechSeva static site. Edit CONTACT below, then re-run:
   python3 build.py /home/user/techseva
"""
import sys, os

OUT = sys.argv[1]
EMAIL = "mist2k26@gmail.com"
PHONE_DISPLAY = "+91 XXXXX XXXXX"   # <-- replace with real number
PHONE_TEL = "+910000000000"          # <-- replace (digits only, with +91)
CITY = "Kolkata, West Bengal"
SITE = "https://agarwalvivaan09-ai.github.io/techseva/"

NAV = [
    ("index.html", "Home"),
    ("about.html", "About"),
    ("what-we-accept.html", "What We Accept"),
    ("how-it-works.html", "How It Works"),
    ("impact.html", "Impact"),
    ("learn.html", "Learn"),
    ("get-involved.html", "Get Involved"),
    ("faq.html", "FAQ"),
]

I = {
 "check": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6 9 17l-5-5"/></svg>',
 "phone": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="5" y="2" width="14" height="20" rx="2"/><path d="M12 18h.01"/></svg>',
 "laptop": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="12" rx="2"/><path d="M2 20h20"/></svg>',
 "monitor": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="3" width="20" height="14" rx="2"/><path d="M8 21h8M12 17v4"/></svg>',
 "cable": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M17 21v-2a1 1 0 0 1-1-1v-1a2 2 0 0 1 2-2h2a2 2 0 0 1 2 2v1a1 1 0 0 1-1 1v2M19 15V6.5a3.5 3.5 0 0 0-7 0v11a3.5 3.5 0 0 1-7 0V9M7 3v2a1 1 0 0 1 1 1v1a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V6a1 1 0 0 1 1-1V3"/></svg>',
 "plug": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22v-5M9 8V2M15 8V2M18 8v5a4 4 0 0 1-4 4h-4a4 4 0 0 1-4-4V8z"/></svg>',
 "home": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m3 10 9-7 9 7v10a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><path d="M9 22V12h6v10"/></svg>',
 "truck": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 18V6a2 2 0 0 0-2-2H4a2 2 0 0 0-2 2v11a1 1 0 0 0 1 1h2M15 18H9M19 18h2a1 1 0 0 0 1-1v-3.65a1 1 0 0 0-.22-.62l-3.48-4.35A1 1 0 0 0 17.52 8H14"/><circle cx="17" cy="18" r="2"/><circle cx="7" cy="18" r="2"/></svg>',
 "recycle": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M7 19H4.8a1.8 1.8 0 0 1-1.6-2.7L7.2 9.5M11 19h8.2a1.8 1.8 0 0 0 1.6-2.7l-1.2-2.1M14 16l-3 3 3 3M8.3 13.6 7.2 9.5 3.1 10.6M9.3 5.6l1.1-1.9a1.8 1.8 0 0 1 3.1 0l3.9 6.8M13.4 9.5l3.3 1-1 4.1"/></svg>',
 "shield": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 13c0 5-3.5 7.5-7.7 9a1 1 0 0 1-.7 0C7.5 20.5 4 18 4 13V6a1 1 0 0 1 1-1c2 0 4.5-1.2 6.2-2.7a1.2 1.2 0 0 1 1.6 0C14.5 3.8 17 5 19 5a1 1 0 0 1 1 1z"/><path d="m9 12 2 2 4-4"/></svg>',
 "file": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M15 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7z"/><path d="M14 2v4a2 2 0 0 0 2 2h4M9 15l2 2 4-4"/></svg>',
 "users": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87M16 3.13a4 4 0 0 1 0 7.75"/></svg>',
 "school": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 10 12 5 2 10l10 5 10-5z"/><path d="M6 12v5c3 3 9 3 12 0v-5"/></svg>',
 "building": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="4" y="2" width="16" height="20" rx="2"/><path d="M9 22v-4h6v4M8 6h.01M16 6h.01M12 6h.01M12 10h.01M12 14h.01M16 10h.01M16 14h.01M8 10h.01M8 14h.01"/></svg>',
 "megaphone": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m3 11 18-5v12L3 14v-3z"/><path d="M11.6 16.8a3 3 0 1 1-5.8-1.6"/></svg>',
 "leaf": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M11 20A7 7 0 0 1 9.8 6.1C15.5 5 17 4.48 19 2c1 2 2 4.18 2 8 0 5.5-4.78 10-10 10Z"/><path d="M2 21c0-3 1.85-5.36 5.08-6C9.5 14.52 12 13 13 12"/></svg>',
 "alert": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m21.7 18-8-14a2 2 0 0 0-3.5 0l-8 14A2 2 0 0 0 4 21h16a2 2 0 0 0 1.7-3z"/><path d="M12 9v4M12 17h.01"/></svg>',
 "mail": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-10 6L2 7"/></svg>',
 "call": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z"/></svg>',
 "pin": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"/><circle cx="12" cy="10" r="3"/></svg>',
 "clock": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/></svg>',
 "battery": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="7" width="16" height="10" rx="2"/><path d="M22 11v2M6 11v2M10 11v2"/></svg>',
 "fridge": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="5" y="2" width="14" height="20" rx="2"/><path d="M5 10h14M9 5v2M9 13v3"/></svg>',
 "printer": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M6 9V2h12v7M6 18H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-2"/><rect x="6" y="14" width="12" height="8"/></svg>',
 "chip": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="4" y="4" width="16" height="16" rx="2"/><rect x="9" y="9" width="6" height="6"/><path d="M15 2v2M15 20v2M2 15h2M2 9h2M20 15h2M20 9h2M9 2v2M9 20v2"/></svg>',
 "tower": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="6" y="2" width="12" height="20" rx="2"/><path d="M10 6h4M10 10h4M12 17h.01"/></svg>',
 "ac": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="5" width="20" height="10" rx="2"/><path d="M6 11h12M8 19l-1 2M12 19v2M16 19l1 2"/></svg>',
 "oven": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="4" width="20" height="15" rx="2"/><rect x="5" y="7" width="10" height="9" rx="1"/><path d="M18 8h.01M18 11h.01M18 14h.01"/></svg>',
 "menu": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M4 7h16M4 12h16M4 17h16"/></svg>',
 "arrow": '<svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M12 5l7 7-7 7"/></svg>',
}
ARROW = I["arrow"]

def icon(name):
    return f'<div class="icon" aria-hidden="true">{I[name]}</div>'

def page(fname, title, desc, body, current=None):
    navlinks = "\n".join(
        f'        <li><a href="{h}"{" aria-current=\"page\"" if h == (current or fname) else ""}>{t}</a></li>'
        for h, t in NAV)
    html = f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <meta name="theme-color" content="#0b1440">
  <link rel="canonical" href="{SITE}{'' if fname == 'index.html' else fname}">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="TechSeva">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:image" content="{SITE}assets/img/logo-full.svg">
  <link rel="icon" href="favicon.svg" type="image/svg+xml">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Poppins:wght@500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
  <a class="skip" href="#main">Skip to content</a>
  <header class="site-header">
    <nav class="container nav" aria-label="Main">
      <a class="brand" href="index.html" aria-label="TechSeva home">
        <img src="assets/img/logo-mark.svg" alt="" width="42" height="42">
        <span><span class="brand-name">TECH SEVA</span><span class="brand-tag">E-WASTE SERVICE ORG</span></span>
      </a>
      <button class="nav-toggle" aria-label="Open menu" aria-expanded="false" aria-controls="nav-links">{I["menu"]}</button>
      <ul class="nav-links" id="nav-links">
{navlinks}
        <li><a class="btn btn-primary" href="contact.html#pickup">Request Pickup</a></li>
      </ul>
    </nav>
  </header>

  <main id="main">
{body}
  </main>

  <footer class="site-footer">
    <div class="container">
      <div class="footer-grid">
        <div class="footer-brand">
          <a class="brand" href="index.html"><img src="assets/img/logo-mark.svg" alt="" width="42" height="42"><span><span class="brand-name">TECH SEVA</span><span class="brand-tag">E-WASTE SERVICE ORG</span></span></a>
          <p>A student-led, community-driven nonprofit initiative collecting household e-waste in {CITY.split(",")[0]} and routing it to an authorised recycler.</p>
        </div>
        <div>
          <h4>Explore</h4>
          <ul>
            <li><a href="about.html">About Us</a></li>
            <li><a href="what-we-accept.html">What We Accept</a></li>
            <li><a href="how-it-works.html">How It Works</a></li>
            <li><a href="impact.html">Impact &amp; Certificates</a></li>
          </ul>
        </div>
        <div>
          <h4>Get Involved</h4>
          <ul>
            <li><a href="get-involved.html">Volunteer</a></li>
            <li><a href="get-involved.html#drives">Host a Drive</a></li>
            <li><a href="learn.html">E-Waste 101</a></li>
            <li><a href="faq.html">FAQ</a></li>
          </ul>
        </div>
        <div>
          <h4>Contact</h4>
          <ul>
            <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
            <li><a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></li>
            <li>{CITY}, India</li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <span>&copy; <span id="year">2026</span> TechSeva. Founded by Vivaan Agarwal.</span>
        <span>Recycling partner: Hulladek Recycling (CPCB-authorised)</span>
      </div>
    </div>
  </footer>
  <script src="assets/js/main.js" defer></script>
</body>
</html>
'''
    with open(os.path.join(OUT, fname), "w") as f:
        f.write(html)

def hero(eyebrow, h1, lead, crumb):
    return f'''    <section class="page-hero">
      <div class="container">
        <div class="crumbs"><a href="index.html">Home</a> / {crumb}</div>
        <div class="eyebrow">{eyebrow}</div>
        <h1>{h1}</h1>
        <p class="lead">{lead}</p>
      </div>
    </section>'''

CTA = f'''    <section>
      <div class="container">
        <div class="cta-band reveal">
          <div>
            <h2>Got a drawer full of old electronics?</h2>
            <p>Tell us what you have. We’ll arrange a free pickup or drop-off and make sure it’s recycled responsibly.</p>
          </div>
          <div class="actions">
            <a class="btn btn-light" href="contact.html#pickup">Request a pickup {ARROW}</a>
            <a class="btn btn-ghost" href="tel:{PHONE_TEL}">Call {PHONE_DISPLAY}</a>
          </div>
        </div>
      </div>
    </section>'''

GALLERY_ITEMS = [
    ("collection-ac.jpg", "ac", "Window air conditioner", "Large appliance — collected for dismantling"),
    ("collection-uv-cabinet.jpg", "oven", "UV-C disinfection cabinet", "Small household appliance"),
    ("collection-monitor.jpg", "monitor", "LCD computer monitor", "IT equipment — screens handled separately"),
    ("collection-cpu.jpg", "tower", "Desktop CPU cabinet", "IT equipment — routed for data-safe recycling"),
]

def gallery():
    items = "\n".join(f'''          <figure class="shot reveal">
            <div class="frame"><span class="ph" aria-hidden="true">{I[ic]}</span><img src="assets/img/{fn}" alt="{t} collected by TechSeva" loading="lazy" style="position:absolute;inset:0"></div>
            <figcaption><strong>{t}</strong>{c}</figcaption>
          </figure>''' for fn, ic, t, c in GALLERY_ITEMS)
    return f'''        <div class="gallery">
{items}
        </div>'''

# ======================================================== HOME
home = f'''    <section class="hero">
      <div class="container hero-grid">
        <div>
          <div class="eyebrow">Responsible e-waste recycling · {CITY.split(",")[0]}</div>
          <h1>Give your old electronics a <span class="grad-text">responsible</span> end.</h1>
          <p class="lead">TechSeva collects unused and broken electronics from homes, housing societies, schools and offices, and hands every kilo to a government-authorised recycler. Free, simple and fully documented.</p>
          <div class="hero-actions">
            <a class="btn btn-primary" href="contact.html#pickup">Request a free pickup {ARROW}</a>
            <a class="btn btn-ghost" href="what-we-accept.html">See what we accept</a>
          </div>
          <div class="hero-trust">
            <span>{I["check"]} Free collection</span>
            <span>{I["check"]} CPCB-authorised recycler</span>
            <span>{I["check"]} Recycling certificates</span>
          </div>
        </div>
        <div class="hero-art">
          <img src="assets/img/logo-full.svg" alt="TechSeva logo — E-Waste Service Org" width="440" height="440">
          <div class="hero-badge b1"><strong class="grad-text">317+ kg</strong>e-waste recycled</div>
          <div class="hero-badge b2"><strong>100%</strong>sent to authorised recycling</div>
        </div>
      </div>
    </section>

    <section>
      <div class="container">
        <div class="stats">
          <div class="stat reveal"><strong class="grad-text"><span data-count="317">317</span>+ kg</strong><span>E-waste collected and certified as recycled</span></div>
          <div class="stat reveal"><strong class="grad-text" data-count="2">2</strong><span>Documented collection drives with recycling certificates</span></div>
          <div class="stat reveal"><strong class="grad-text">100%</strong><span>Handed to a CPCB-authorised recycler</span></div>
          <div class="stat reveal"><strong class="grad-text">₹0</strong><span>Cost to donors, always</span></div>
        </div>
      </div>
    </section>

    <section class="section-alt">
      <div class="container split">
        <div class="reveal">
          <div class="eyebrow">The problem</div>
          <h2>The world’s fastest-growing waste stream is sitting in our drawers.</h2>
          <p class="lead">In 2022 the world generated a record <strong>62 million tonnes</strong> of e-waste, and only <strong>22.3%</strong> of it was documented as properly collected and recycled.</p>
          <p>Old phones, chargers and cables hold lead, mercury, cadmium and flame retardants that leak into soil and water when dumped or burned. They also hold copper, gold and other valuable metals that can be recovered and reused. TechSeva closes that gap, starting where the problem starts: our own homes.</p>
          <a class="btn btn-outline" href="learn.html">Learn about e-waste {ARROW}</a>
        </div>
        <div class="grid g2 reveal">
          <div class="card">{icon("alert")}<h3>Toxic if dumped</h3><p>Heavy metals and chemicals pollute land, water and air when e-waste is burned or landfilled.</p></div>
          <div class="card">{icon("chip")}<h3>Valuable if recycled</h3><p>Copper, aluminium, gold and rare metals can be recovered and returned to manufacturing.</p></div>
          <div class="card">{icon("shield")}<h3>Data at risk</h3><p>Old phones and drives often still hold personal data. They need careful handling.</p></div>
          <div class="card">{icon("home")}<h3>Stored indefinitely</h3><p>Most households keep unused gadgets for years because they don’t know where to send them.</p></div>
        </div>
      </div>
    </section>

    <section>
      <div class="container">
        <div class="section-head center reveal">
          <div class="eyebrow">How it works</div>
          <h2>Four steps from clutter to certified recycling</h2>
          <p class="lead">We’ve kept it simple. You tell us what you have, and we handle the rest.</p>
        </div>
        <div class="grid g4 steps">
          <div class="card step reveal"><h3>Tell us</h3><p>Fill in the pickup form or call us with a rough list of items and your location.</p></div>
          <div class="card step reveal"><h3>Prepare</h3><p>Back up and wipe your data, remove SIM and memory cards, and bag small items together.</p></div>
          <div class="card step reveal"><h3>We collect</h3><p>We pick up at a time that suits you, or you drop off at a collection drive.</p></div>
          <div class="card step reveal"><h3>Certified recycling</h3><p>Everything goes to Hulladek Recycling, a CPCB-authorised recycler, and we receive a recycling certificate.</p></div>
        </div>
        <p class="center mt-2"><a class="btn btn-outline" href="how-it-works.html">Full process &amp; guidelines {ARROW}</a></p>
      </div>
    </section>

    <section class="section-dark">
      <div class="container">
        <div class="section-head reveal">
          <div class="eyebrow">What we accept</div>
          <h2>If it has a plug, battery or circuit board, we probably take it.</h2>
        </div>
        <div class="grid g4">
          <div class="card reveal">{icon("phone")}<h3>Phones &amp; tablets</h3><p>Mobiles, feature phones, tablets, e-readers.</p></div>
          <div class="card reveal">{icon("laptop")}<h3>Computers</h3><p>Laptops, desktops, CPUs, keyboards, mice, hard drives.</p></div>
          <div class="card reveal">{icon("monitor")}<h3>Screens &amp; TVs</h3><p>LCD/LED monitors and televisions.</p></div>
          <div class="card reveal">{icon("cable")}<h3>Cables &amp; chargers</h3><p>Wires, adapters, power banks, extension boards.</p></div>
          <div class="card reveal">{icon("printer")}<h3>Office equipment</h3><p>Printers, scanners, routers, modems, UPS units.</p></div>
          <div class="card reveal">{icon("oven")}<h3>Small appliances</h3><p>Microwaves, toasters, irons, mixers, kettles.</p></div>
          <div class="card reveal">{icon("ac")}<h3>Large appliances</h3><p>ACs, fridges, washing machines (by arrangement).</p></div>
          <div class="card reveal">{icon("plug")}<h3>Everything else</h3><p>Speakers, remotes, cameras, toys with circuits, and more.</p></div>
        </div>
        <p class="mt-2"><a class="btn btn-light" href="what-we-accept.html">Full list &amp; what we can’t take {ARROW}</a></p>
      </div>
    </section>

    <section>
      <div class="container">
        <div class="section-head reveal">
          <div class="eyebrow">Recent collections</div>
          <h2>From homes and offices to the recycler</h2>
          <p class="lead">A few of the items picked up during our latest drive, from a window AC to an old desktop setup.</p>
        </div>
{gallery()}
      </div>
    </section>

    <section class="section-alt">
      <div class="container split">
        <div class="panel reveal">
          <p class="eyebrow">Our story</p>
          <p class="quote">“It started with a drawer full of old cables and broken gadgets. If I had this much e-waste lying around, so did everyone else.”</p>
          <p class="mb-0">Vivaan Agarwal, Founder</p>
        </div>
        <div class="reveal">
          <div class="eyebrow">About TechSeva</div>
          <h2>Small, local, and fully accountable.</h2>
          <p>TechSeva (<em>seva</em> means service) began as a student-led effort to collect e-waste from family, friends and neighbours. It has grown into a repeatable system of outreach, collection, logistics and certified recycling.</p>
          <p>Every drive is weighed and documented, and every kilo is backed by a certificate from our recycling partner.</p>
          <a class="btn btn-outline" href="about.html">Read our story {ARROW}</a>
        </div>
      </div>
    </section>

{CTA}'''
page("index.html", "TechSeva | Free E-Waste Collection & Responsible Recycling in Kolkata",
     "TechSeva is a student-led nonprofit e-waste initiative in Kolkata. We collect old electronics from homes, schools and offices for certified, responsible recycling.", home)

# ======================================================== ABOUT
about = hero("About us", "Service to the planet, one drawer at a time.",
             "TechSeva is a student-led nonprofit initiative that makes responsible e-waste disposal easy for households and communities in Kolkata.", "About") + f'''

    <section>
      <div class="container split">
        <div class="reveal">
          <div class="eyebrow">Our origin</div>
          <h2>The idea started with a drawer.</h2>
          <p>While cleaning his room, founder Vivaan Agarwal opened a drawer filled with old cables, broken devices and unused electronics that had sat there for years. It looked like clutter. When he asked whether he could just throw it all out, he learned that e-waste can be seriously harmful if it isn’t disposed of properly.</p>
          <p>That moment changed his perspective. If one drawer held this much e-waste, so did thousands of others. What looked like a small personal problem was part of a much larger one.</p>
          <p>That realisation became TechSeva: an initiative to collect e-waste directly from local households and make sure it is responsibly recycled.</p>
        </div>
        <div class="panel reveal">
          <p class="eyebrow">Key insight</p>
          <p class="quote">Environmental impact doesn’t have to begin at scale. It begins with a problem in your own surroundings, and a process that turns awareness into action.</p>
        </div>
      </div>
    </section>

    <section class="section-alt">
      <div class="container">
        <div class="grid g2">
          <div class="card reveal">{icon("leaf")}<h3>Our mission</h3><p>To make responsible e-waste disposal the default for every household, school and office in our community by removing the friction: free collection, clear guidance and verified recycling.</p></div>
          <div class="card reveal">{icon("recycle")}<h3>Our vision</h3><p>A city where no gadget ends up in a landfill, a drain or an open fire, and where recovered materials go back into the economy instead of polluting it.</p></div>
        </div>
      </div>
    </section>

    <section>
      <div class="container">
        <div class="section-head reveal">
          <div class="eyebrow">What we do</div>
          <h2>Four pillars of every TechSeva drive</h2>
        </div>
        <div class="grid g4 steps">
          <div class="card step reveal"><h3>Outreach</h3><p>We reach out to households and communities and help people find the unused electronics they’ve forgotten about.</p></div>
          <div class="card step reveal"><h3>Collection</h3><p>We collect e-waste directly from homes, societies and offices, or through drop-off drives.</p></div>
          <div class="card step reveal"><h3>Coordination</h3><p>We sort, weigh and coordinate safe transport of everything collected to our recycling partner.</p></div>
          <div class="card step reveal"><h3>Recycling</h3><p>An authorised recycler dismantles and processes the material and issues a certificate for each consignment.</p></div>
        </div>
      </div>
    </section>

    <section class="section-dark">
      <div class="container">
        <div class="section-head reveal">
          <div class="eyebrow">Our values</div>
          <h2>What we stand for</h2>
        </div>
        <div class="grid g3">
          <div class="card reveal">{icon("file")}<h3>Transparency</h3><p>Every consignment is weighed, and every recycling certificate is published on our Impact page.</p></div>
          <div class="card reveal">{icon("shield")}<h3>Responsibility</h3><p>We work only with recyclers authorised under India’s E-Waste (Management) Rules. No informal scrap dealers, ever.</p></div>
          <div class="card reveal">{icon("users")}<h3>Community</h3><p>We start with the people around us: families, neighbours, schools and local businesses.</p></div>
        </div>
      </div>
    </section>

    <section>
      <div class="container split">
        <div class="reveal">
          <div class="eyebrow">Founder</div>
          <h2>Vivaan Agarwal</h2>
          <p>Vivaan is a student in Kolkata with interests in economics, finance and entrepreneurship. He founded TechSeva to turn a personal realisation into a working system with measurable outcomes. He leads its outreach, partnerships and operations.</p>
          <p>Want to collaborate, invite TechSeva to your school or society, or just ask a question? He’d love to hear from you.</p>
          <div class="hero-actions" style="margin:24px 0 0">
            <a class="btn btn-primary" href="contact.html">Get in touch {ARROW}</a>
            <a class="btn btn-outline" href="https://agarwalvivaan09-ai.github.io/vivaan-dev/" target="_blank" rel="noopener">Vivaan’s website</a>
          </div>
        </div>
        <div class="card reveal">
          {icon("recycle")}
          <h3>Our recycling partner</h3>
          <p><strong>Hulladek Recycling</strong> is a Kolkata-based e-waste management company authorised by the Central Pollution Control Board (CPCB). It handles collection, dismantling and recycling of electronic waste, along with data destruction. Each TechSeva consignment is backed by a Hulladek recycling certificate.</p>
        </div>
      </div>
    </section>

{CTA}'''
page("about.html", "About TechSeva | Our Story, Mission & Founder",
     "How TechSeva began, our mission and values, and the people and partners behind Kolkata's student-led e-waste initiative.", about)

# ======================================================== WHAT WE ACCEPT
accept = hero("What we accept", "What can I give to TechSeva?",
              "Almost anything with a plug, battery or circuit board. Here’s the full list, plus the few things we can’t take.", "What We Accept") + f'''

    <section>
      <div class="container">
        <div class="grid g3">
          <div class="card reveal">{icon("laptop")}<h3>IT &amp; computing</h3>
            <ul class="checklist mt-2"><li>Laptops &amp; desktops / CPU cabinets</li><li>Keyboards, mice, webcams</li><li>Hard drives, SSDs, pen drives</li><li>Motherboards, RAM, graphics cards</li><li>Routers, modems, switches</li></ul></div>
          <div class="card reveal">{icon("phone")}<h3>Mobile &amp; personal</h3>
            <ul class="checklist mt-2"><li>Mobile &amp; feature phones</li><li>Tablets &amp; e-readers</li><li>Smartwatches &amp; fitness bands</li><li>Earphones, headphones, speakers</li><li>Cameras &amp; gaming consoles</li></ul></div>
          <div class="card reveal">{icon("monitor")}<h3>Screens &amp; display</h3>
            <ul class="checklist mt-2"><li>LCD / LED monitors</li><li>LED &amp; LCD televisions</li><li>Old CRT TVs &amp; monitors (by arrangement)</li><li>Projectors</li><li>Set-top boxes &amp; remotes</li></ul></div>
          <div class="card reveal">{icon("cable")}<h3>Cables &amp; power</h3>
            <ul class="checklist mt-2"><li>Chargers &amp; adapters</li><li>All kinds of cables &amp; wires</li><li>Extension boards</li><li>Power banks (terminals taped)</li><li>UPS &amp; inverters (by arrangement)</li></ul></div>
          <div class="card reveal">{icon("oven")}<h3>Small appliances</h3>
            <ul class="checklist mt-2"><li>Microwaves, OTGs, UV cabinets</li><li>Mixers, toasters, kettles</li><li>Irons, hair dryers, trimmers</li><li>Fans &amp; electric heaters</li><li>Electronic toys</li></ul></div>
          <div class="card reveal">{icon("fridge")}<h3>Large appliances</h3>
            <ul class="checklist mt-2"><li>Air conditioners (window &amp; split)</li><li>Refrigerators</li><li>Washing machines</li><li>Water purifiers</li><li><em>Please call ahead so we can arrange transport</em></li></ul></div>
        </div>
      </div>
    </section>

    <section class="section-alt">
      <div class="container split">
        <div class="reveal">
          <div class="eyebrow">What we can’t take</div>
          <h2>Please keep these out of your e-waste bag</h2>
          <p>These items need specialised handling that our collection drives aren’t equipped for. We’re happy to point you to the right place.</p>
          <ul class="xlist mt-2">
            <li><strong>Swollen, leaking or damaged batteries.</strong> These are a fire risk in transit.</li>
            <li><strong>Car / vehicle batteries</strong> and large lead-acid batteries.</li>
            <li><strong>Broken CFL bulbs and tube lights</strong> (they contain mercury).</li>
            <li><strong>Medical devices</strong> with biological contamination.</li>
            <li><strong>Non-electronic waste</strong>: plastic, paper, glass, furniture, clothes.</li>
            <li><strong>Gas cylinders, paint, chemicals</strong> or any hazardous liquids.</li>
          </ul>
        </div>
        <div class="reveal">
          <div class="callout warn">
            <strong>Batteries: handle with care.</strong>
            <p class="mb-0 mt-0" style="margin-top:8px">Lithium-ion batteries (in phones, laptops and power banks) can catch fire if punctured or short-circuited. Leave them inside the device if they’re intact, or tape over the terminals of loose batteries and pack them separately. Never put a swollen battery in a bag with other items.</p>
          </div>
          <div class="callout mt-2">
            <strong>Not sure about an item?</strong>
            <p class="mb-0" style="margin-top:8px">Email a photo to <a href="mailto:{EMAIL}">{EMAIL}</a> or call <a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a> and we’ll tell you within a day.</p>
          </div>
        </div>
      </div>
    </section>

    <section>
      <div class="container">
        <div class="section-head reveal">
          <div class="eyebrow">Working vs. broken</div>
          <h2>Does it matter if it still works?</h2>
          <p class="lead">No, we accept both. Working devices in good condition may be passed on for reuse where it’s safe to do so. Everything else is recycled.</p>
        </div>
      </div>
    </section>

{CTA}'''
page("what-we-accept.html", "What We Accept | TechSeva E-Waste Collection",
     "The full list of electronics TechSeva accepts for recycling, from phones and laptops to ACs and appliances, plus items we can't take and battery safety tips.", accept)

# ======================================================== HOW IT WORKS
how = hero("How it works", "Donating e-waste takes about ten minutes.",
           "Follow these steps and general guidelines to make your donation quick, safe and secure.", "How It Works") + f'''

    <section>
      <div class="container">
        <div class="grid g4 steps">
          <div class="card step reveal"><h3>Request</h3><p>Fill in the <a href="contact.html#pickup">pickup form</a>, email or call us. Share a rough list of items, approximate quantity and your area.</p></div>
          <div class="card step reveal"><h3>Prepare</h3><p>Back up and wipe your devices, remove SIM and memory cards, and bag small items together (see the checklist below).</p></div>
          <div class="card step reveal"><h3>Hand over</h3><p>We confirm a pickup slot, usually within a week, or share the date and venue of the next drop-off drive.</p></div>
          <div class="card step reveal"><h3>Recycled</h3><p>Items are weighed and sent to our CPCB-authorised partner. On request, we email you a confirmation of what was collected.</p></div>
        </div>
      </div>
    </section>

    <section class="section-alt">
      <div class="container">
        <div class="section-head reveal">
          <div class="eyebrow">Two ways to give</div>
          <h2>Pickup or drop-off: your choice</h2>
        </div>
        <div class="grid g2">
          <div class="card reveal">{icon("truck")}<h3>Doorstep pickup</h3>
            <p>Best for households with several items, large appliances, offices and housing societies.</p>
            <ul class="checklist mt-2"><li>Free within our service area in Kolkata</li><li>Scheduled at a time that suits you</li><li>Large items (AC, fridge) by prior arrangement</li></ul>
            <p class="mt-2"><a class="btn btn-primary" href="contact.html#pickup">Request pickup {ARROW}</a></p></div>
          <div class="card reveal">{icon("pin")}<h3>Collection drives</h3>
            <p>We regularly run drop-off drives at schools, societies and community spaces. Bring your items on the day.</p>
            <ul class="checklist mt-2"><li>Announced in advance with date &amp; venue</li><li>Ideal for small items: phones, cables, chargers</li><li>Want one in your area? <a href="get-involved.html#drives">Host a drive</a></li></ul>
            <p class="mt-2"><a class="btn btn-outline" href="contact.html">Ask about the next drive {ARROW}</a></p></div>
        </div>
      </div>
    </section>

    <section id="guidelines">
      <div class="container split" style="align-items:start">
        <div class="reveal">
          <div class="eyebrow">General instructions</div>
          <h2>Before you hand over your e-waste</h2>
          <ul class="checklist mt-2">
            <li><strong>Back up</strong> anything you want to keep: photos, contacts, documents.</li>
            <li><strong>Sign out</strong> of all accounts (Google, Apple ID, Samsung, iCloud) and turn off “Find My Device”.</li>
            <li><strong>Factory reset</strong> phones, tablets and laptops. See the data-safety guide below.</li>
            <li><strong>Remove</strong> SIM cards, memory cards and any discs from drives.</li>
            <li><strong>Tape battery terminals</strong> on loose batteries and keep them in a separate bag.</li>
            <li><strong>Bundle cables</strong> and chargers together with a rubber band or tie.</li>
            <li><strong>Bag small items</strong> together in a box or cloth bag. Please avoid plastic where you can.</li>
            <li><strong>Don’t dismantle</strong> devices yourself. Screens and batteries can be hazardous.</li>
            <li><strong>Keep large appliances</strong> unplugged and accessible for pickup.</li>
          </ul>
        </div>
        <div class="reveal">
          <div class="card">
            {icon("shield")}
            <h3>Data safety guide</h3>
            <p>You are responsible for wiping your personal data before donating. Here’s how:</p>
            <div class="table-wrap mt-2">
              <table>
                <tr><th>Device</th><th>What to do</th></tr>
                <tr><td>Android phone</td><td>Settings → System → Reset options → Erase all data (factory reset). Remove your Google account first.</td></tr>
                <tr><td>iPhone / iPad</td><td>Sign out of Apple ID, then Settings → General → Transfer or Reset → Erase All Content and Settings.</td></tr>
                <tr><td>Windows PC</td><td>Settings → System → Recovery → Reset this PC → Remove everything, with the “clean data” option.</td></tr>
                <tr><td>Mac</td><td>System Settings → General → Transfer or Reset → Erase All Content and Settings.</td></tr>
                <tr><td>Dead device</td><td>If it won’t power on, tell us. You can remove the hard drive or keep it, and we’ll flag it for secure handling.</td></tr>
              </table>
            </div>
          </div>
          <div class="callout mt-2"><strong>Tip:</strong> menu names vary slightly by brand and OS version. If you’re stuck, call us and we’ll walk you through it.</div>
        </div>
      </div>
    </section>

    <section class="section-dark">
      <div class="container">
        <div class="section-head reveal">
          <div class="eyebrow">After collection</div>
          <h2>What happens to your e-waste</h2>
        </div>
        <div class="grid g4 steps">
          <div class="card step reveal"><h3>Sorted &amp; weighed</h3><p>We categorise the items and record total weight for each consignment.</p></div>
          <div class="card step reveal"><h3>Transported</h3><p>The consignment goes to Hulladek Recycling, an authorised recycler.</p></div>
          <div class="card step reveal"><h3>Dismantled</h3><p>Devices are taken apart and hazardous parts are isolated for safe treatment.</p></div>
          <div class="card step reveal"><h3>Recovered</h3><p>Metals, plastics and glass are recovered, and a recycling certificate is issued.</p></div>
        </div>
      </div>
    </section>

{CTA}'''
page("how-it-works.html", "How It Works | Donate E-Waste to TechSeva",
     "Step-by-step guide to donating e-waste with TechSeva: pickup or drop-off, general instructions, data-wiping guide and what happens after collection.", how)

# ======================================================== IMPACT
impact = hero("Our impact", "Measured in kilograms, backed by certificates.",
              "We weigh every consignment and publish every recycling certificate. Here’s what TechSeva has achieved so far.", "Impact") + f'''

    <section>
      <div class="container">
        <div class="stats">
          <div class="stat reveal"><strong class="grad-text">317.8 kg</strong><span>Total e-waste recycled across certified consignments</span></div>
          <div class="stat reveal"><strong class="grad-text">2</strong><span>Recycling certificates issued by our partner</span></div>
          <div class="stat reveal"><strong class="grad-text">100%</strong><span>Sent to an authorised recycler. Nothing to landfill.</span></div>
          <div class="stat reveal"><strong class="grad-text">1</strong><span>CPCB-authorised recycling partner</span></div>
        </div>
      </div>
    </section>

    <section class="section-alt" id="certificates">
      <div class="container">
        <div class="section-head reveal">
          <div class="eyebrow">Proof &amp; certification</div>
          <h2>Recycling certificates</h2>
          <p class="lead">Each consignment collected by TechSeva is handed to Hulladek Recycling, which issues an official certificate confirming the weight received for recycling.</p>
        </div>
        <div class="grid g2">
          <div class="card cert reveal">
            {icon("file")}
            <div>
              <h3>Consignment 1: Household drive</h3>
              <dl><dt>Certificate no.</dt><dd>HUL/25-26/03002</dd><dt>Date</dt><dd>25 March 2026</dd><dt>Weight</dt><dd>196.60 kg</dd><dt>Material</dt><dd>E-waste</dd></dl>
              <a class="btn btn-outline" href="assets/docs/certificate-hulladek-1.pdf" target="_blank" rel="noopener">View certificate (PDF) {ARROW}</a>
            </div>
          </div>
          <div class="card cert reveal">
            {icon("file")}
            <div>
              <h3>Consignment 2: Delight Dairy drive</h3>
              <dl><dt>Certificate no.</dt><dd>HUL/26-27/10002</dd><dt>Date</dt><dd>15 September 2026</dd><dt>Weight</dt><dd>121.20 kg</dd><dt>Material</dt><dd>E-waste</dd></dl>
              <a class="btn btn-outline" href="assets/docs/certificate-hulladek-2.pdf" target="_blank" rel="noopener">View certificate (PDF) {ARROW}</a>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section>
      <div class="container">
        <div class="section-head reveal">
          <div class="eyebrow">From our drives</div>
          <h2>Items we’ve collected</h2>
        </div>
{gallery()}
      </div>
    </section>

    <section class="section-dark">
      <div class="container split">
        <div class="reveal">
          <div class="eyebrow">Why it matters</div>
          <h2>Every kilo kept out of the informal sector counts.</h2>
          <p>Much of India’s e-waste is handled informally, through open burning, acid baths and crude dismantling that expose workers and neighbourhoods to toxic fumes and heavy metals. Routing devices to an authorised recycler means hazardous parts are treated safely and valuable materials are recovered.</p>
          <p>Our goal for the coming year is to run regular drives with schools, housing societies and local businesses, and to cross <strong style="color:#fff">1,000 kg</strong> of certified recycling.</p>
        </div>
        <div class="grid g2 reveal">
          <div class="stat"><strong class="grad-text">62 Mt</strong><span>E-waste generated worldwide in 2022</span></div>
          <div class="stat"><strong class="grad-text">22.3%</strong><span>Documented as properly collected &amp; recycled</span></div>
          <div class="stat"><strong class="grad-text">82 Mt</strong><span>Projected global e-waste by 2030</span></div>
          <div class="stat"><strong class="grad-text">1 → 1,000</strong><span>Our next milestone: 1,000 kg recycled</span></div>
        </div>
      </div>
      <div class="container"><p class="sources mt-2" style="color:#8b93c4">Source: UN ITU/UNITAR <a style="color:#8b93c4" href="https://ewastemonitor.info/the-global-e-waste-monitor-2024/" target="_blank" rel="noopener">Global E-waste Monitor 2024</a>.</p></div>
    </section>

{CTA}'''
page("impact.html", "Impact & Recycling Certificates | TechSeva",
     "TechSeva has collected and certified 317+ kg of e-waste for recycling. See our recycling certificates from Hulladek Recycling and the items we've collected.", impact)

# ======================================================== LEARN
learn = hero("E-waste 101", "Everything you should know about e-waste.",
             "What counts as e-waste, why it’s dangerous, what the law says in India, and simple habits that make a difference.", "Learn") + f'''

    <section>
      <div class="container split" style="align-items:start">
        <div class="reveal">
          <div class="eyebrow">The basics</div>
          <h2>What is e-waste?</h2>
          <p>Electronic waste, or e-waste, is any discarded product with a plug, battery or circuit board. That covers phones, computers and TVs as well as fridges, ACs, toys and chargers. It’s the fastest-growing solid waste stream in the world.</p>
          <p>Globally, e-waste generation is rising about five times faster than documented e-waste recycling. India is among the world’s largest generators, with the Central Pollution Control Board reporting about <strong>1.6 million tonnes</strong> of e-waste generated in 2021–22.</p>
        </div>
        <div class="grid g2 reveal">
          <div class="stat"><strong class="grad-text">62 Mt</strong><span>Global e-waste in 2022</span></div>
          <div class="stat"><strong class="grad-text">22.3%</strong><span>Documented as properly recycled</span></div>
          <div class="stat"><strong class="grad-text">7.8 kg</strong><span>Average e-waste per person, worldwide</span></div>
          <div class="stat"><strong class="grad-text">1.6 Mt</strong><span>E-waste generated in India, 2021–22</span></div>
        </div>
      </div>
    </section>

    <section class="section-alt">
      <div class="container">
        <div class="section-head reveal">
          <div class="eyebrow">Why it’s dangerous</div>
          <h2>What’s inside your old gadgets</h2>
          <p class="lead">The same materials that make electronics work can harm people and the environment when they’re handled badly.</p>
        </div>
        <div class="table-wrap reveal">
          <table>
            <tr><th>Substance</th><th>Found in</th><th>Risk when dumped or burned</th></tr>
            <tr><td><strong>Lead</strong></td><td>Old CRT screens, solder, circuit boards</td><td>Damages the nervous system and kidneys; especially harmful to children</td></tr>
            <tr><td><strong>Mercury</strong></td><td>Older LCD backlights, switches, CFLs</td><td>Toxic to the brain; accumulates in fish and the food chain</td></tr>
            <tr><td><strong>Cadmium</strong></td><td>Rechargeable batteries, older chips</td><td>Linked to kidney and bone damage; carcinogenic</td></tr>
            <tr><td><strong>Brominated flame retardants</strong></td><td>Plastic casings, circuit boards</td><td>Release toxic dioxins when burned</td></tr>
            <tr><td><strong>Lithium-ion cells</strong></td><td>Phones, laptops, power banks</td><td>Fire and explosion risk if crushed or punctured</td></tr>
          </table>
        </div>
      </div>
    </section>

    <section>
      <div class="container split">
        <div class="reveal">
          <div class="eyebrow">The value inside</div>
          <h2>E-waste is also an “urban mine”</h2>
          <p>Electronics contain copper, aluminium, iron, gold, silver, palladium and rare earth elements. Proper recycling recovers these materials so they can be used again, which reduces the need for new mining and cuts emissions.</p>
          <p>When e-waste is landfilled or burned, those resources are lost for good, along with the energy that went into producing them.</p>
        </div>
        <div class="card reveal">
          {icon("file")}
          <h3>The law in India</h3>
          <p>India’s <strong>E-Waste (Management) Rules, 2022</strong>, in force from 1 April 2023, place Extended Producer Responsibility (EPR) on manufacturers and require e-waste to be processed only by registered recyclers. Consumers and bulk users are expected to hand over e-waste through authorised channels, not informal scrap dealers. TechSeva works only with a CPCB-authorised recycler.</p>
        </div>
      </div>
    </section>

    <section class="section-dark">
      <div class="container">
        <div class="section-head reveal">
          <div class="eyebrow">What you can do</div>
          <h2>Six habits that reduce e-waste</h2>
        </div>
        <div class="grid g3">
          <div class="card reveal">{icon("clock")}<h3>Use devices longer</h3><p>Keeping a phone or laptop even one extra year significantly lowers its lifetime footprint.</p></div>
          <div class="card reveal">{icon("chip")}<h3>Repair before replacing</h3><p>A new battery, screen or charger often gives a device years more life.</p></div>
          <div class="card reveal">{icon("users")}<h3>Pass it on</h3><p>Working devices can help a student, relative or local NGO.</p></div>
          <div class="card reveal">{icon("cable")}<h3>Skip extra accessories</h3><p>Reuse chargers and cables you already own instead of buying new ones.</p></div>
          <div class="card reveal">{icon("recycle")}<h3>Recycle the right way</h3><p>Never hand e-waste to the kabadiwala or put it in the dustbin. Use an authorised channel like TechSeva.</p></div>
          <div class="card reveal">{icon("megaphone")}<h3>Spread the word</h3><p>Tell family and friends. Most people simply don’t know where to send their old gadgets.</p></div>
        </div>
      </div>
    </section>

    <section>
      <div class="container">
        <p class="sources">Sources: <a href="https://ewastemonitor.info/the-global-e-waste-monitor-2024/" target="_blank" rel="noopener">Global E-waste Monitor 2024 (ITU &amp; UNITAR)</a>; <a href="https://cpcb.nic.in/e-waste/" target="_blank" rel="noopener">Central Pollution Control Board, Government of India</a>; <a href="https://moef.gov.in/" target="_blank" rel="noopener">Ministry of Environment, Forest and Climate Change: E-Waste (Management) Rules, 2022</a>.</p>
      </div>
    </section>

{CTA}'''
page("learn.html", "E-Waste 101 | Facts, Hazards & Rules in India | TechSeva",
     "Learn what e-waste is, why it's hazardous, what India's E-Waste (Management) Rules 2022 require, and simple habits that reduce electronic waste.", learn)

# ======================================================== GET INVOLVED
involved = hero("Get involved", "Help us collect more, recycle better, reach further.",
                "Whether you have an afternoon, a classroom, a housing society or a company, there’s a way to be part of TechSeva.", "Get Involved") + f'''

    <section>
      <div class="container">
        <div class="grid g2">
          <div class="card reveal">{icon("users")}<h3>Volunteer with us</h3>
            <p>Help with outreach, sorting and weighing at drives, social media, design or logistics. Students are especially welcome, and we can provide a volunteering certificate for your hours.</p>
            <p class="mt-2"><a class="btn btn-primary" href="#volunteer">Sign up to volunteer {ARROW}</a></p></div>
          <div class="card reveal" id="drives">{icon("pin")}<h3>Host a collection drive</h3>
            <p>Bring TechSeva to your housing society, school, college, club or place of worship. We provide posters, guidelines and on-the-day support, and handle the recycling.</p>
            <p class="mt-2"><a class="btn btn-outline" href="contact.html#pickup">Plan a drive {ARROW}</a></p></div>
          <div class="card reveal">{icon("school")}<h3>Schools &amp; colleges</h3>
            <p>Run a campus e-waste drive paired with a short awareness session for students. It works well for eco-clubs, community-service hours and Environment Day events.</p></div>
          <div class="card reveal">{icon("building")}<h3>Businesses &amp; offices</h3>
            <p>Clear out old IT equipment, cables and appliances responsibly, as we did with Delight Dairy. Ask us about organising a collection at your premises.</p></div>
        </div>
      </div>
    </section>

    <section class="section-alt">
      <div class="container split" style="align-items:start">
        <div class="reveal">
          <div class="eyebrow">Hosting a drive</div>
          <h2>How a TechSeva drive works</h2>
          <div class="grid steps" style="gap:16px">
            <div class="card step"><h3>Pick a date &amp; venue</h3><p>A society clubhouse, school lobby or office reception works well. Two to three hours is usually enough.</p></div>
            <div class="card step"><h3>Spread the word</h3><p>We share a ready-made poster and WhatsApp message with our guidelines one week ahead.</p></div>
            <div class="card step"><h3>Collect &amp; weigh</h3><p>Our team receives, sorts and weighs items on the day.</p></div>
            <div class="card step"><h3>Certified recycling</h3><p>We send the consignment to our recycler and share the final weight with you.</p></div>
          </div>
        </div>
        <div class="form-card reveal" id="volunteer">
          <h3>Volunteer sign-up</h3>
          <p class="form-note" style="margin-bottom:18px">Submitting opens your email app with this information filled in.</p>
          <form class="form" data-mailto="{EMAIL}" data-subject="TechSeva volunteer sign-up">
            <div class="row">
              <label>Full name<input name="Name" required autocomplete="name"></label>
              <label>Phone<input name="Phone" type="tel" autocomplete="tel"></label>
            </div>
            <label>Email<input name="Email" type="email" required autocomplete="email"></label>
            <div class="row">
              <label>School / organisation<input name="Organisation"></label>
              <label>Area of Kolkata<input name="Area"></label>
            </div>
            <label>I’d like to help with
              <select name="Interest">
                <option>Collection drives (on the ground)</option>
                <option>Outreach &amp; awareness</option>
                <option>Social media &amp; design</option>
                <option>Logistics &amp; transport</option>
                <option>Anything that’s needed</option>
              </select>
            </label>
            <label>Anything else?<textarea name="Message" placeholder="Availability, skills, ideas…"></textarea></label>
            <button class="btn btn-primary" type="submit">Send sign-up {ARROW}</button>
            <p class="form-status form-note" role="status"></p>
          </form>
        </div>
      </div>
    </section>

    <section>
      <div class="container">
        <div class="section-head reveal">
          <div class="eyebrow">No time? No problem.</div>
          <h2>Small ways to help</h2>
        </div>
        <div class="grid g3">
          <div class="card reveal">{icon("megaphone")}<h3>Share us</h3><p>Forward this website to your family and society WhatsApp groups.</p></div>
          <div class="card reveal">{icon("home")}<h3>Check your drawers</h3><p>Gather your own old gadgets and <a href="contact.html#pickup">request a pickup</a>.</p></div>
          <div class="card reveal">{icon("truck")}<h3>Lend logistics</h3><p>Have a vehicle or storage space? Help us move larger consignments.</p></div>
        </div>
      </div>
    </section>

{CTA}'''
page("get-involved.html", "Get Involved | Volunteer or Host an E-Waste Drive | TechSeva",
     "Volunteer with TechSeva, host an e-waste collection drive at your school, society or office, or partner with us to recycle responsibly in Kolkata.", involved)

# ======================================================== FAQ
def qa(q, a):
    return f'''          <details><summary>{q}</summary><div>{a}</div></details>'''

faqs = [
 ("General", [
  ("What is TechSeva?", "TechSeva is a student-led nonprofit initiative in Kolkata that collects e-waste from households, schools and businesses and sends it to a government-authorised recycler for safe processing."),
  ("Does it cost anything?", "No. Collection is free for households, and we never charge donors. For very large commercial volumes we may discuss logistics with you, but we’ll always say so upfront."),
  ("Do you pay for e-waste?", "No. TechSeva is a nonprofit service, not a scrap buyer. Our job is to make sure your e-waste is recycled responsibly, not to resell it."),
  ("Which areas do you cover?", f"We currently serve Kolkata and nearby areas. If you’re further away, <a href=\"contact.html\">contact us</a> anyway. We may be able to arrange a drive or point you to an authorised collection centre."),
 ]),
 ("Donating", [
  ("What items do you accept?", "Almost anything with a plug, battery or circuit board, from phones, laptops and cables to monitors, small appliances and ACs. See the <a href=\"what-we-accept.html\">full list</a>."),
  ("Is there a minimum quantity for pickup?", "No strict minimum. For a single charger or phone it’s usually easiest to drop it off at our next drive, but just ask and we’ll work something out."),
  ("Do you accept devices that still work?", "Yes. Working devices in good condition may be passed on for reuse where that’s safe. Everything else is recycled."),
  ("Can I donate batteries?", "Intact batteries, yes. Keep them inside the device, or tape the terminals of loose cells and pack them separately. We can’t accept swollen, leaking or damaged batteries, or vehicle batteries."),
  ("How soon can you pick up?", "Usually within a week of your request. Large appliances may need a little more time to arrange transport."),
 ]),
 ("Data & recycling", [
  ("Is my data safe?", "Please back up, sign out of all accounts and factory-reset your devices before handing them over. Our <a href=\"how-it-works.html#guidelines\">data-safety guide</a> shows how. Our recycling partner also offers data destruction as part of its process, but wiping your device first is always the best protection."),
  ("Who recycles the e-waste?", "Hulladek Recycling, a Kolkata-based e-waste management company authorised by the Central Pollution Control Board (CPCB)."),
  ("How do I know it’s actually recycled?", "Every consignment receives an official recycling certificate from our partner. We publish them on our <a href=\"impact.html#certificates\">Impact page</a>."),
  ("Can I get a certificate for my donation?", "For organisations and large donations, ask us and we’ll share the consignment certificate covering your items. Individuals can get an email confirmation of what was collected."),
 ]),
 ("Partnering", [
  ("Can my school or society host a drive?", "Yes, we’d love that. See <a href=\"get-involved.html#drives\">Host a drive</a> or <a href=\"contact.html#pickup\">get in touch</a>."),
  ("Can I volunteer?", "Absolutely. Sign up on the <a href=\"get-involved.html#volunteer\">Get Involved</a> page."),
 ]),
]
faq_body = hero("FAQ", "Frequently asked questions",
                "Quick answers about donating, data safety, recycling and partnering with TechSeva.", "FAQ") + '''

    <section>
      <div class="container">
''' + "\n".join(
    f'''        <div class="faq-group reveal"><h2>{g}</h2><div class="faq">
{chr(10).join(qa(q, a) for q, a in items)}
        </div></div>''' for g, items in faqs) + f'''
        <div class="callout mt-2" style="max-width:860px"><strong>Still have a question?</strong> Email <a href="mailto:{EMAIL}">{EMAIL}</a> or call <a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a>.</div>
      </div>
    </section>

{CTA}'''
page("faq.html", "FAQ | TechSeva E-Waste Collection",
     "Answers to common questions about donating e-waste to TechSeva: cost, accepted items, pickups, batteries, data safety and recycling certificates.", faq_body)

# ======================================================== CONTACT
contact = hero("Contact", "Let’s get your e-waste recycled.",
               "Request a pickup, plan a drive, or just ask a question. We usually reply within 48 hours.", "Contact") + f'''

    <section>
      <div class="container split" style="align-items:start">
        <div class="reveal">
          <div class="grid" style="gap:14px">
            <div class="card contact-tile">{icon("mail")}<div><small>Email</small><a href="mailto:{EMAIL}">{EMAIL}</a></div></div>
            <div class="card contact-tile">{icon("call")}<div><small>Phone / WhatsApp, for more details</small><a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></div></div>
            <div class="card contact-tile">{icon("pin")}<div><small>Service area</small><span class="v">{CITY}, India</span></div></div>
            <div class="card contact-tile">{icon("clock")}<div><small>Response time</small><span class="v">Within 48 hours · Pickups usually within a week</span></div></div>
          </div>
          <div class="callout mt-2">
            <strong>Before your pickup</strong>
            <ul style="margin:10px 0 0">
              <li>Back up and factory-reset your devices</li>
              <li>Remove SIM and memory cards</li>
              <li>Tape terminals of loose batteries</li>
              <li>Bundle cables and bag small items</li>
            </ul>
            <p class="mb-0" style="margin-top:10px"><a href="how-it-works.html#guidelines">Read the full guidelines →</a></p>
          </div>
        </div>
        <div class="form-card reveal" id="pickup">
          <h2 style="font-size:1.6rem">Request a pickup</h2>
          <p class="form-note" style="margin-bottom:18px">Fill this in and press send. It opens your email app with everything filled in. Prefer to talk? Call <a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a>.</p>
          <form class="form" data-mailto="{EMAIL}" data-subject="TechSeva pickup request">
            <div class="row">
              <label>Full name<input name="Name" required autocomplete="name"></label>
              <label>Phone<input name="Phone" type="tel" required autocomplete="tel"></label>
            </div>
            <label>Email<input name="Email" type="email" autocomplete="email"></label>
            <label>I am a
              <select name="Donor type">
                <option>Household</option>
                <option>Housing society / RWA</option>
                <option>School / college</option>
                <option>Business / office</option>
                <option>Other</option>
              </select>
            </label>
            <label>Pickup address / area<input name="Address" required autocomplete="street-address"></label>
            <label>What are you donating?<textarea name="Items" required placeholder="e.g. 2 old phones, 1 laptop, a bag of cables, 1 window AC"></textarea></label>
            <div class="row">
              <label>Approx. quantity
                <select name="Quantity">
                  <option>A few small items (fits in a bag)</option>
                  <option>A box or two</option>
                  <option>Includes large appliances</option>
                  <option>Bulk (office / society drive)</option>
                </select>
              </label>
              <label>Preferred dates / time<input name="Preferred time" placeholder="e.g. weekends, after 4pm"></label>
            </div>
            <label class="check-row"><input type="checkbox" name="Data wiped" value="Yes" required> I will back up and wipe personal data from my devices before handover.</label>
            <button class="btn btn-primary" type="submit">Send request {ARROW}</button>
            <p class="form-status form-note" role="status"></p>
          </form>
        </div>
      </div>
    </section>'''
page("contact.html", "Contact & Request a Pickup | TechSeva",
     "Contact TechSeva to request a free e-waste pickup in Kolkata, plan a collection drive or ask a question. Email or call us for more details.", contact)

# ======================================================== 404
nf = f'''    <section class="page-hero" style="min-height:60vh;display:grid;align-items:center">
      <div class="container center">
        <div class="eyebrow">Error 404</div>
        <h1 style="margin-inline:auto">This page has been recycled.</h1>
        <p class="lead" style="margin-inline:auto">We couldn’t find what you were looking for.</p>
        <p class="mt-2"><a class="btn btn-light" href="index.html">Back to home {ARROW}</a></p>
      </div>
    </section>'''
page("404.html", "Page not found | TechSeva", "This page could not be found.", nf, current="none")

# sitemap
with open(os.path.join(OUT, "sitemap.xml"), "w") as f:
    urls = "".join(f"  <url><loc>{SITE}{'' if h=='index.html' else h}</loc></url>\n" for h, _ in NAV + [("contact.html", "")])
    f.write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}</urlset>\n')
with open(os.path.join(OUT, "robots.txt"), "w") as f:
    f.write(f"User-agent: *\nAllow: /\nSitemap: {SITE}sitemap.xml\n")
print("built")

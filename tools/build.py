#!/usr/bin/env python3
"""Generates the TechSeva static site.

Edit the CONTACT block below, then run from the repo root:
    python3 tools/build.py .
"""
import sys, os

OUT = sys.argv[1] if len(sys.argv) > 1 else "."

# ---------------- CONTACT ----------------
EMAIL = "agarwalvivaan09@gmail.com"
PHONE_DISPLAY = "+91 98300 24550"
PHONE_TEL = "+919830024550"
INSTAGRAM_URL = "https://www.instagram.com/tech.seva_/"
INSTAGRAM_HANDLE = "@tech.seva_"
CITY = "Kolkata"
SITE = "https://agarwalvivaan09-ai.github.io/techseva/"
# -----------------------------------------

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

def svg(d):
    return f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">{d}</svg>'

I = {
 "phone": svg('<rect x="5" y="2" width="14" height="20" rx="2"/><path d="M12 18h.01"/>'),
 "laptop": svg('<rect x="3" y="4" width="18" height="12" rx="2"/><path d="M2 20h20"/>'),
 "monitor": svg('<rect x="2" y="3" width="20" height="14" rx="2"/><path d="M8 21h8M12 17v4"/>'),
 "cable": svg('<path d="M17 21v-2a1 1 0 0 1-1-1v-1a2 2 0 0 1 2-2h2a2 2 0 0 1 2 2v1a1 1 0 0 1-1 1v2M19 15V6.5a3.5 3.5 0 0 0-7 0v11a3.5 3.5 0 0 1-7 0V9M7 3v2a1 1 0 0 1 1 1v1a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V6a1 1 0 0 1 1-1V3"/>'),
 "printer": svg('<path d="M6 9V2h12v7M6 18H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-2"/><rect x="6" y="14" width="12" height="8"/>'),
 "oven": svg('<rect x="2" y="4" width="20" height="15" rx="2"/><rect x="5" y="7" width="10" height="9" rx="1"/><path d="M18 8h.01M18 11h.01M18 14h.01"/>'),
 "ac": svg('<rect x="2" y="5" width="20" height="10" rx="2"/><path d="M6 11h12M8 19l-1 2M12 19v2M16 19l1 2"/>'),
 "tower": svg('<rect x="6" y="2" width="12" height="20" rx="2"/><path d="M10 6h4M10 10h4M12 17h.01"/>'),
 "shield": svg('<path d="M20 13c0 5-3.5 7.5-7.7 9a1 1 0 0 1-.7 0C7.5 20.5 4 18 4 13V6a1 1 0 0 1 1-1c2 0 4.5-1.2 6.2-2.7a1.2 1.2 0 0 1 1.6 0C14.5 3.8 17 5 19 5a1 1 0 0 1 1 1z"/><path d="m9 12 2 2 4-4"/>'),
 "file": svg('<path d="M15 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7z"/><path d="M14 2v4a2 2 0 0 0 2 2h4M9 15l2 2 4-4"/>'),
 "users": svg('<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87M16 3.13a4 4 0 0 1 0 7.75"/>'),
 "school": svg('<path d="M22 10 12 5 2 10l10 5 10-5z"/><path d="M6 12v5c3 3 9 3 12 0v-5"/>'),
 "building": svg('<rect x="4" y="2" width="16" height="20" rx="2"/><path d="M9 22v-4h6v4M8 6h.01M16 6h.01M12 6h.01M12 10h.01M12 14h.01M16 10h.01M16 14h.01M8 10h.01M8 14h.01"/>'),
 "pin": svg('<path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"/><circle cx="12" cy="10" r="3"/>'),
 "alert": svg('<path d="m21.7 18-8-14a2 2 0 0 0-3.5 0l-8 14A2 2 0 0 0 4 21h16a2 2 0 0 0 1.7-3z"/><path d="M12 9v4M12 17h.01"/>'),
 "chip": svg('<rect x="4" y="4" width="16" height="16" rx="2"/><rect x="9" y="9" width="6" height="6"/><path d="M15 2v2M15 20v2M2 15h2M2 9h2M20 15h2M20 9h2M9 2v2M9 20v2"/>'),
 "recycle": svg('<path d="M7 19H4.8a1.8 1.8 0 0 1-1.6-2.7L7.2 9.5M11 19h8.2a1.8 1.8 0 0 0 1.6-2.7l-1.2-2.1M14 16l-3 3 3 3M8.3 13.6 7.2 9.5 3.1 10.6M9.3 5.6l1.1-1.9a1.8 1.8 0 0 1 3.1 0l3.9 6.8M13.4 9.5l3.3 1-1 4.1"/>'),
 "truck": svg('<path d="M14 18V6a2 2 0 0 0-2-2H4a2 2 0 0 0-2 2v11a1 1 0 0 0 1 1h2M15 18H9M19 18h2a1 1 0 0 0 1-1v-3.65a1 1 0 0 0-.22-.62l-3.48-4.35A1 1 0 0 0 17.52 8H14"/><circle cx="17" cy="18" r="2"/><circle cx="7" cy="18" r="2"/>'),
 "mail": svg('<rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-10 6L2 7"/>'),
 "call": svg('<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z"/>'),
 "insta": svg('<rect x="2" y="2" width="20" height="20" rx="5"/><circle cx="12" cy="12" r="4"/><path d="M17.5 6.5h.01"/>'),
 "clock": svg('<circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/>'),
 "menu": svg('<path d="M4 7h16M4 12h16M4 17h16"/>'),
 "arrow": svg('<path d="M5 12h14M12 5l7 7-7 7"/>'),
}
A = I["arrow"]

def ic(n):
    return f'<div class="ic" aria-hidden="true">{I[n]}</div>'

BRAND = '<span class="brand-blob" data-blob="mini"><img src="assets/img/blob.svg" alt="" width="40" height="40"></span><span><b>TECH SEVA</b><small>E-WASTE SERVICE ORG</small></span>'
BRAND_STATIC = '<img src="assets/img/logo-mark.svg" alt="" width="36" height="36"><span><b>TECH SEVA</b><small>E-WASTE SERVICE ORG</small></span>'

def page(fname, title, desc, body, current=None, extra_js='  <script src="assets/js/vendor/three.min.js" defer></script>\n  <script src="assets/js/blob.js" defer></script>\n'):
    navlinks = "\n".join(
        f'        <li><a href="{h}"{" aria-current=\"page\"" if h == (current or fname) else ""}>{t}</a></li>' for h, t in NAV)
    html = f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <meta name="theme-color" content="#060814">
  <link rel="canonical" href="{SITE}{'' if fname == 'index.html' else fname}">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="TechSeva">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <link rel="icon" href="favicon.svg" type="image/svg+xml">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Montserrat:wght@600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
  <canvas id="net" aria-hidden="true"></canvas>
  <a class="skip" href="#main">Skip to content</a>
  <header class="site-header">
    <nav class="container nav" aria-label="Main">
      <a class="brand" href="index.html" aria-label="TechSeva home">{BRAND}</a>
      <button class="nav-toggle" aria-label="Open menu" aria-expanded="false" aria-controls="nav-links">{I["menu"]}</button>
      <ul class="nav-links" id="nav-links">
{navlinks}
        <li><a class="btn btn-primary" href="contact.html">Contact</a></li>
      </ul>
    </nav>
  </header>

  <main id="main">
{body}
  </main>

  <footer class="site-footer">
    <div class="container">
      <div class="footer-grid">
        <div>
          <a class="brand" href="index.html">{BRAND_STATIC}</a>
          <p>A student-led nonprofit collecting household e-waste in {CITY} and routing it to an authorised recycler.</p>
        </div>
        <div>
          <h4>Organisation</h4>
          <ul>
            <li><a href="about.html">About</a></li>
            <li><a href="impact.html">Impact</a></li>
            <li><a href="learn.html">E-Waste 101</a></li>
            <li><a href="faq.html">FAQ</a></li>
          </ul>
        </div>
        <div>
          <h4>Donate</h4>
          <ul>
            <li><a href="what-we-accept.html">What We Accept</a></li>
            <li><a href="how-it-works.html">How It Works</a></li>
            <li><a href="contact.html#pickup">Request Pickup</a></li>
            <li><a href="get-involved.html">Get Involved</a></li>
          </ul>
        </div>
        <div>
          <h4>Contact</h4>
          <ul>
            <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
            <li><a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></li>
            <li><a href="{INSTAGRAM_URL}" target="_blank" rel="noopener">Instagram {INSTAGRAM_HANDLE}</a></li>
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
{extra_js}  <script src="assets/js/main.js" defer></script>
</body>
</html>
'''
    with open(os.path.join(OUT, fname), "w") as f:
        f.write(html)

def hero(label, h1, lead):
    return f'''    <section class="page-hero">
      <div class="container">
        <div class="label">{label}</div>
        <h1>{h1}</h1>
        <p class="lead">{lead}</p>
      </div>
    </section>'''

CTA = f'''    <section>
      <div class="container">
        <div class="cta reveal">
          <div>
            <h2>Have old electronics at home?</h2>
            <p>Tell us what you have. We’ll arrange a free pickup and make sure it’s recycled properly.</p>
          </div>
          <div class="actions" style="margin:0">
            <a class="btn btn-primary" href="contact.html#pickup">Request a pickup {A}</a>
            <a class="btn btn-ghost" href="tel:{PHONE_TEL}">Call us</a>
          </div>
        </div>
      </div>
    </section>'''

GALLERY = [
    ("collection-ac.jpg", "ac", "Window AC", "Large appliance"),
    ("collection-uv-cabinet.jpg", "oven", "UV-C cabinet", "Small appliance"),
    ("collection-monitor.jpg", "monitor", "LCD monitor", "IT equipment"),
    ("collection-cpu.jpg", "tower", "Desktop CPU", "IT equipment"),
]
def gallery():
    items = "\n".join(f'''          <figure class="shot reveal"><div class="frame" aria-hidden="true">{I[i]}<img src="assets/img/{f}" alt="{t} collected by TechSeva" loading="lazy"></div><figcaption><b>{t}</b>{c}</figcaption></figure>''' for f, i, t, c in GALLERY)
    return f'        <div class="gallery">\n{items}\n        </div>'

STATS = '''        <div class="stats reveal">
          <div class="stat"><b class="grad">317.8 kg</b><span>E-waste recycled</span></div>
          <div class="stat"><b class="grad">2</b><span>Certified consignments</span></div>
          <div class="stat"><b class="grad">100%</b><span>Sent to authorised recycler</span></div>
          <div class="stat"><b class="grad">₹0</b><span>Cost to donors</span></div>
        </div>'''

# ======================================================== HOME
home = f'''    <section class="hero">
      <div class="container hero-grid">
        <div>
          <div class="label">E-waste collection · {CITY}</div>
          <h1>Responsible recycling for the <span class="grad">electronics you no longer use.</span></h1>
          <p class="lead">TechSeva collects old and broken electronics from homes, schools and offices and hands every kilo to a government-authorised recycler. It’s free, and every consignment is certified.</p>
          <div class="actions">
            <a class="btn btn-primary" href="contact.html#pickup">Request a free pickup {A}</a>
            <a class="btn btn-ghost" href="what-we-accept.html">What we accept</a>
          </div>
        </div>
        <div class="blob-wrap" data-blob="hero" title="Drag to spin"><img src="assets/img/blob.svg" alt=""></div>
      </div>
    </section>

    <section style="padding-top:8px">
      <div class="container">
{STATS}
      </div>
    </section>

    <section>
      <div class="container">
        <div class="head reveal">
          <div class="label">Process</div>
          <h2>From your drawer to certified recycling</h2>
        </div>
        <div class="grid g4">
          <div class="card reveal"><span class="num">01</span><h3>Request</h3><p>Use the pickup form or call us with a rough list of items.</p></div>
          <div class="card reveal"><span class="num">02</span><h3>Prepare</h3><p>Back up and wipe your devices, and remove SIM and memory cards.</p></div>
          <div class="card reveal"><span class="num">03</span><h3>Collect</h3><p>We pick up from your door, or you drop off at a drive.</p></div>
          <div class="card reveal"><span class="num">04</span><h3>Recycle</h3><p>A CPCB-authorised recycler processes it and issues a certificate.</p></div>
        </div>
      </div>
    </section>

    <section>
      <div class="container split">
        <div class="reveal">
          <div class="label">What we accept</div>
          <h2>If it has a plug, battery or circuit board, send it our way.</h2>
          <p>Phones, laptops, monitors, cables, chargers, printers, routers, small kitchen appliances, and even ACs and fridges by arrangement. Working or broken.</p>
          <div class="actions"><a class="btn btn-ghost" href="what-we-accept.html">See the full list {A}</a></div>
        </div>
        <div class="grid g2 reveal">
          <div class="card">{ic("alert")}<h3>Toxic if dumped</h3><p>Lead, mercury and cadmium leach into soil and water.</p></div>
          <div class="card">{ic("chip")}<h3>Valuable if recycled</h3><p>Copper, gold and rare metals are recovered and reused.</p></div>
          <div class="card">{ic("shield")}<h3>Handled safely</h3><p>Data-safety guidance and an authorised recycler only.</p></div>
          <div class="card">{ic("file")}<h3>Fully documented</h3><p>Every consignment is weighed and certified.</p></div>
        </div>
      </div>
    </section>

    <section>
      <div class="container">
        <div class="head reveal">
          <div class="label">Recent collections</div>
          <h2>Picked up this season</h2>
        </div>
{gallery()}
      </div>
    </section>

{CTA}'''
page("index.html", "TechSeva | E-Waste Collection & Recycling in Kolkata",
     "TechSeva is a student-led nonprofit in Kolkata that collects old electronics from homes, schools and offices for certified, responsible recycling.",
     home)

# ======================================================== ABOUT
about = hero("About", "Service to the planet, one drawer at a time.",
             "<em>Seva</em> means service. TechSeva is a student-led nonprofit that makes responsible e-waste disposal easy for households and communities in Kolkata.") + f'''

    <section>
      <div class="container split">
        <div class="reveal">
          <div class="label">Origin</div>
          <h2>It started with a drawer.</h2>
          <p>While cleaning his room, founder Vivaan Agarwal found a drawer full of old cables, broken devices and unused electronics that had sat there for years. When he asked whether he could just throw it out, he learned that e-waste can be seriously harmful if it isn’t disposed of properly.</p>
          <p>If one drawer held this much, so did thousands of others. TechSeva grew from that idea: collect e-waste directly from local households and make sure every kilo is recycled responsibly.</p>
        </div>
        <div class="grid reveal">
          <div class="card glow"><h3>Mission</h3><p>Make responsible e-waste disposal the default for every home, school and office in our community through free collection, clear guidance and verified recycling.</p></div>
          <div class="card"><h3>Vision</h3><p>A city where no gadget ends up in a landfill, a drain or an open fire, and recovered materials go back into use.</p></div>
        </div>
      </div>
    </section>

    <section>
      <div class="container">
        <div class="head reveal"><div class="label">Principles</div><h2>How we operate</h2></div>
        <div class="grid g3">
          <div class="card reveal">{ic("file")}<h3>Transparency</h3><p>Every consignment is weighed, and every certificate is published.</p></div>
          <div class="card reveal">{ic("shield")}<h3>Responsibility</h3><p>Authorised recyclers only, never informal scrap dealers.</p></div>
          <div class="card reveal">{ic("users")}<h3>Community</h3><p>We start with the people around us: families, neighbours, schools and local businesses.</p></div>
        </div>
      </div>
    </section>

    <section>
      <div class="container grid g2">
        <div class="card reveal">
          <div class="label">Founder</div>
          <h3 style="font-size:1.3rem">Vivaan Agarwal</h3>
          <p>A student in Kolkata with interests in economics, finance and entrepreneurship. Vivaan leads TechSeva’s outreach, partnerships and operations.</p>
          <div class="actions" style="margin-top:18px"><a class="btn btn-ghost" href="https://agarwalvivaan09-ai.github.io/vivaan-agarwal-website-3.0/" target="_blank" rel="noopener">Personal website {A}</a></div>
        </div>
        <div class="card reveal">
          <div class="label">Recycling partner</div>
          <h3 style="font-size:1.3rem">Hulladek Recycling</h3>
          <p>A Kolkata-based e-waste management company authorised by the Central Pollution Control Board. Hulladek dismantles and recycles every TechSeva consignment and issues a certificate for each one.</p>
        </div>
      </div>
    </section>

{CTA}'''
page("about.html", "About | TechSeva",
     "The story, mission and people behind TechSeva, a student-led e-waste nonprofit in Kolkata.", about)

# ======================================================== WHAT WE ACCEPT
def cat(icon_, title, items):
    lis = "".join(f"<li>{x}</li>" for x in items)
    return f'<div class="card reveal">{ic(icon_)}<h3>{title}</h3><ul class="list" style="margin-top:12px">{lis}</ul></div>'

accept = hero("What we accept", "Working or broken, we take it.",
              "Almost anything with a plug, battery or circuit board. Here’s the list, plus the few items we can’t handle.") + f'''

    <section>
      <div class="container grid g3">
        {cat("laptop", "Computing", ["Laptops, desktops, CPUs", "Keyboards, mice, webcams", "Hard drives, pen drives", "Routers and modems"])}
        {cat("phone", "Mobile & personal", ["Phones and tablets", "Smartwatches", "Headphones, speakers", "Cameras, consoles"])}
        {cat("monitor", "Screens", ["LCD / LED monitors", "Televisions", "Projectors", "Set-top boxes, remotes"])}
        {cat("cable", "Cables & power", ["Chargers and adapters", "Cables of all kinds", "Extension boards", "Power banks (terminals taped)"])}
        {cat("oven", "Small appliances", ["Microwaves, OTGs, UV cabinets", "Mixers, kettles, toasters", "Irons, hair dryers", "Fans and heaters"])}
        {cat("ac", "Large appliances", ["Window and split ACs", "Refrigerators", "Washing machines", "Call ahead to arrange transport"])}
      </div>
    </section>

    <section>
      <div class="container split">
        <div class="reveal">
          <div class="label">Not accepted</div>
          <h2>Please keep these out</h2>
          <ul class="list no">
            <li>Swollen, leaking or damaged batteries</li>
            <li>Vehicle and large lead-acid batteries</li>
            <li>Broken CFLs and tube lights (they contain mercury)</li>
            <li>Contaminated medical devices</li>
            <li>Non-electronic waste: plastic, paper, furniture, clothes</li>
          </ul>
        </div>
        <div class="grid reveal">
          <div class="note warn"><strong>Battery safety.</strong> Lithium-ion batteries can catch fire if punctured. Leave intact batteries inside the device, or tape the terminals of loose ones and pack them separately.</div>
          <div class="note"><strong>Not sure about an item?</strong> Email a photo to <a href="mailto:{EMAIL}">{EMAIL}</a> and we’ll reply within a day.</div>
        </div>
      </div>
    </section>

{CTA}'''
page("what-we-accept.html", "What We Accept | TechSeva",
     "The electronics TechSeva accepts for recycling, items we can't take, and battery safety tips.", accept)

# ======================================================== HOW IT WORKS
how = hero("How it works", "Donating takes about ten minutes.",
           "Request a pickup, prepare your devices with the checklist below, and we handle the rest.") + f'''

    <section>
      <div class="container grid g2">
        <div class="card reveal">{ic("truck")}<h3>Doorstep pickup</h3><p>Best for multiple items, large appliances, offices and housing societies. Free within {CITY}. Usually scheduled within a week.</p><div class="actions" style="margin-top:18px"><a class="btn btn-primary" href="contact.html#pickup">Request pickup {A}</a></div></div>
        <div class="card reveal">{ic("pin")}<h3>Collection drives</h3><p>Drop-off days at schools, societies and community spaces, ideal for phones, cables and chargers. Want one near you? Host a drive.</p><div class="actions" style="margin-top:18px"><a class="btn btn-ghost" href="get-involved.html">Host a drive {A}</a></div></div>
      </div>
    </section>

    <section id="guidelines">
      <div class="container split">
        <div class="reveal">
          <div class="label">General instructions</div>
          <h2>Before you hand over</h2>
          <ul class="list">
            <li><strong>Back up</strong> photos, contacts and documents.</li>
            <li><strong>Sign out</strong> of Google / Apple ID and turn off Find My Device.</li>
            <li><strong>Factory reset</strong> phones, tablets and laptops.</li>
            <li><strong>Remove</strong> SIM cards, memory cards and discs.</li>
            <li><strong>Tape terminals</strong> of loose batteries and bag them separately.</li>
            <li><strong>Bundle cables</strong> and put small items in one bag or box.</li>
            <li><strong>Don’t dismantle</strong> devices. Screens and batteries can be hazardous.</li>
          </ul>
        </div>
        <div class="reveal">
          <div class="label">Data wipe</div>
          <div class="table-wrap">
            <table>
              <tr><th>Device</th><th>Steps</th></tr>
              <tr><td>Android</td><td>Remove Google account → Settings → System → Reset → Erase all data</td></tr>
              <tr><td>iPhone</td><td>Sign out of Apple ID → General → Transfer or Reset → Erase All</td></tr>
              <tr><td>Windows</td><td>Settings → System → Recovery → Reset this PC → Remove everything</td></tr>
              <tr><td>Mac</td><td>System Settings → General → Transfer or Reset → Erase All</td></tr>
              <tr><td>Dead device</td><td>Tell us. You can keep or remove the drive, and we’ll flag it for secure handling.</td></tr>
            </table>
          </div>
        </div>
      </div>
    </section>

    <section>
      <div class="container">
        <div class="head reveal"><div class="label">After collection</div><h2>Where it goes</h2></div>
        <div class="grid g4">
          <div class="card reveal"><span class="num">01</span><h3>Sorted</h3><p>Items are categorised and weighed.</p></div>
          <div class="card reveal"><span class="num">02</span><h3>Transported</h3><p>Sent to Hulladek Recycling.</p></div>
          <div class="card reveal"><span class="num">03</span><h3>Dismantled</h3><p>Hazardous parts are isolated and treated.</p></div>
          <div class="card reveal"><span class="num">04</span><h3>Certified</h3><p>Materials are recovered and a certificate is issued.</p></div>
        </div>
      </div>
    </section>

{CTA}'''
page("how-it-works.html", "How It Works | TechSeva",
     "How to donate e-waste to TechSeva: pickup or drop-off, general instructions and a data-wiping guide.", how)

# ======================================================== IMPACT
impact = hero("Impact", "Measured in kilograms. Backed by certificates.",
              "Every consignment is weighed and certified by our recycling partner.") + f'''

    <section style="padding-top:8px">
      <div class="container">
{STATS}
      </div>
    </section>

    <section id="certificates">
      <div class="container">
        <div class="head reveal"><div class="label">Certificates</div><h2>Recycling certificates</h2></div>
        <div class="grid g2">
          <div class="card cert reveal">{ic("file")}<h3>Consignment 01 · Household drive</h3>
            <dl><dt>Certificate</dt><dd>HUL/25-26/03002</dd><dt>Date</dt><dd>25 Mar 2026</dd><dt>Weight</dt><dd>196.60 kg</dd></dl>
            <a class="btn btn-ghost" href="assets/docs/certificate-hulladek-1.pdf" target="_blank" rel="noopener">View PDF {A}</a></div>
          <div class="card cert reveal">{ic("file")}<h3>Consignment 02 · Delight Dairy</h3>
            <dl><dt>Certificate</dt><dd>HUL/26-27/10002</dd><dt>Date</dt><dd>15 Sep 2026</dd><dt>Weight</dt><dd>121.20 kg</dd></dl>
            <a class="btn btn-ghost" href="assets/docs/certificate-hulladek-2.pdf" target="_blank" rel="noopener">View PDF {A}</a></div>
        </div>
      </div>
    </section>

    <section>
      <div class="container">
        <div class="head reveal"><div class="label">Collected</div><h2>From our drives</h2></div>
{gallery()}
        <p class="mt">Next milestone: <strong>1,000 kg</strong> of certified recycling through regular drives with schools, societies and businesses.</p>
      </div>
    </section>

{CTA}'''
page("impact.html", "Impact & Certificates | TechSeva",
     "TechSeva has recycled 317.8 kg of e-waste, certified by Hulladek Recycling. View the certificates.", impact)

# ======================================================== LEARN
learn = hero("E-waste 101", "Why e-waste matters.",
             "What it is, what’s inside it, and what the law in India requires.") + f'''

    <section style="padding-top:8px">
      <div class="container">
        <div class="stats reveal">
          <div class="stat"><b class="grad">62 Mt</b><span>Global e-waste, 2022</span></div>
          <div class="stat"><b class="grad">22.3%</b><span>Documented as recycled</span></div>
          <div class="stat"><b class="grad">82 Mt</b><span>Projected by 2030</span></div>
          <div class="stat"><b class="grad">1.6 Mt</b><span>India, 2021–22 (CPCB)</span></div>
        </div>
      </div>
    </section>

    <section>
      <div class="container split">
        <div class="reveal">
          <div class="label">The basics</div>
          <h2>The fastest-growing waste stream</h2>
          <p>E-waste is any discarded product with a plug, battery or circuit board. Worldwide it is growing about five times faster than documented recycling. Much of India’s e-waste is still handled informally through open burning and acid baths, which exposes workers and neighbourhoods to toxic fumes.</p>
          <p>The same devices also contain copper, gold and rare metals that proper recycling can recover. That’s why e-waste is often called an “urban mine”.</p>
        </div>
        <div class="card glow reveal">
          <div class="label">The law in India</div>
          <h3>E-Waste (Management) Rules, 2022</h3>
          <p>In force from 1 April 2023. The rules place Extended Producer Responsibility on manufacturers and require e-waste to be processed only by registered recyclers. Consumers should hand e-waste to authorised channels, not informal scrap dealers.</p>
        </div>
      </div>
    </section>

    <section>
      <div class="container">
        <div class="head reveal"><div class="label">Hazards</div><h2>What’s inside</h2></div>
        <div class="table-wrap reveal">
          <table>
            <tr><th>Substance</th><th>Found in</th><th>Risk</th></tr>
            <tr><td>Lead</td><td>Solder, old CRT screens</td><td>Damages the nervous system and kidneys</td></tr>
            <tr><td>Mercury</td><td>Older LCD backlights, CFLs</td><td>Toxic; builds up in the food chain</td></tr>
            <tr><td>Cadmium</td><td>Rechargeable batteries</td><td>Carcinogenic; harms kidneys and bones</td></tr>
            <tr><td>Brominated flame retardants</td><td>Plastic casings, boards</td><td>Release dioxins when burned</td></tr>
            <tr><td>Lithium-ion cells</td><td>Phones, laptops, power banks</td><td>Fire risk if crushed or punctured</td></tr>
          </table>
        </div>
        <p class="sources mt">Sources: <a href="https://ewastemonitor.info/the-global-e-waste-monitor-2024/" target="_blank" rel="noopener">Global E-waste Monitor 2024 (ITU &amp; UNITAR)</a> · <a href="https://cpcb.nic.in/e-waste/" target="_blank" rel="noopener">Central Pollution Control Board</a> · <a href="https://moef.gov.in/" target="_blank" rel="noopener">MoEFCC, E-Waste (Management) Rules 2022</a></p>
      </div>
    </section>

{CTA}'''
page("learn.html", "E-Waste 101 | TechSeva",
     "What e-waste is, why it's hazardous, and what India's E-Waste (Management) Rules 2022 require.", learn)

# ======================================================== GET INVOLVED
involved = hero("Get involved", "Help us collect more and reach further.",
                "Volunteer, host a drive, or bring TechSeva to your school or office.") + f'''

    <section>
      <div class="container grid g3">
        <div class="card reveal">{ic("users")}<h3>Volunteer</h3><p>Help with outreach, sorting at drives, design or logistics. Students can receive a volunteering certificate.</p></div>
        <div class="card reveal">{ic("school")}<h3>Schools &amp; societies</h3><p>Host a drop-off drive. We provide posters and on-the-day support, and handle the recycling.</p></div>
        <div class="card reveal">{ic("building")}<h3>Businesses</h3><p>Clear out old IT equipment and appliances responsibly, as Delight Dairy did.</p></div>
      </div>
    </section>

    <section id="volunteer">
      <div class="container split">
        <div class="reveal">
          <div class="label">Hosting a drive</div>
          <h2>How a drive works</h2>
          <ul class="list">
            <li><strong>Pick a date and venue.</strong> A clubhouse, school lobby or office reception for 2–3 hours.</li>
            <li><strong>Spread the word.</strong> We share a ready-made poster and WhatsApp message a week ahead.</li>
            <li><strong>Collect and weigh.</strong> Our team receives and sorts items on the day.</li>
            <li><strong>Certified recycling.</strong> We share the final weight with you.</li>
          </ul>
        </div>
        <div class="card reveal">
          <h3>Sign up</h3>
          <p class="form-note" style="margin-bottom:16px">This opens your email app with the details filled in.</p>
          <form class="form" data-mailto="{EMAIL}" data-subject="TechSeva - get involved">
            <div class="row">
              <label>Name<input name="Name" required autocomplete="name"></label>
              <label>Phone<input name="Phone" type="tel" autocomplete="tel"></label>
            </div>
            <label>Email<input name="Email" type="email" required autocomplete="email"></label>
            <label>I want to
              <select name="Interest"><option>Volunteer</option><option>Host a drive at my school / society</option><option>Organise a collection at my office</option><option>Something else</option></select>
            </label>
            <label>Message<textarea name="Message" placeholder="Organisation, area, availability…"></textarea></label>
            <button class="btn btn-primary" type="submit">Send {A}</button>
            <p class="form-status form-note" role="status"></p>
          </form>
        </div>
      </div>
    </section>'''
page("get-involved.html", "Get Involved | TechSeva",
     "Volunteer with TechSeva or host an e-waste collection drive at your school, society or office in Kolkata.", involved)

# ======================================================== FAQ
FAQ = [
 ("Does it cost anything?", "No. Collection is free for households, and we never charge donors."),
 ("Do you pay for e-waste?", "No. TechSeva is a nonprofit service, not a scrap buyer. Our job is to make sure your e-waste is recycled responsibly."),
 ("Which areas do you cover?", f"{CITY} and nearby areas. If you’re further away, contact us anyway and we may be able to arrange a drive."),
 ("Is there a minimum quantity?", "No. For one or two small items, dropping off at a drive is usually easiest, but just ask."),
 ("Do you accept working devices?", "Yes. Working devices in good condition may be passed on for reuse where safe; everything else is recycled."),
 ("Can I donate batteries?", "Intact ones, yes. Tape the terminals of loose batteries. We can’t accept swollen or leaking batteries, or vehicle batteries."),
 ("Is my data safe?", "Please back up and factory-reset devices before handover. Our <a href=\"how-it-works.html#guidelines\">data-wipe guide</a> shows how. Wiping it yourself first is always the best protection."),
 ("Who recycles the e-waste?", "Hulladek Recycling, a Kolkata-based recycler authorised by the Central Pollution Control Board."),
 ("How do I know it’s actually recycled?", "Each consignment gets an official certificate, published on our <a href=\"impact.html#certificates\">Impact page</a>."),
 ("Can my organisation get a certificate?", "Yes. For organisations and large donations we share the certificate covering your consignment."),
]
faq = hero("FAQ", "Questions, answered.", "Can’t find what you need? <a href=\"contact.html\">Contact us</a>.") + '''

    <section style="padding-top:8px">
      <div class="container">
        <div class="faq reveal">
''' + "\n".join(f'          <details><summary>{q}</summary><p>{a}</p></details>' for q, a in FAQ) + f'''
        </div>
      </div>
    </section>

{CTA}'''
page("faq.html", "FAQ | TechSeva", "Answers to common questions about donating e-waste to TechSeva.", faq)

# ======================================================== CONTACT
contact = hero("Contact", "Let’s get your e-waste recycled.",
               "Request a pickup or ask a question. We usually reply within 48 hours.") + f'''

    <section style="padding-top:8px">
      <div class="container split">
        <div class="reveal">
          <div class="contact-list">
            <a href="mailto:{EMAIL}">{I["mail"]}<span><small>Email</small>{EMAIL}</span></a>
            <a href="tel:{PHONE_TEL}">{I["call"]}<span><small>Phone · for more details</small>{PHONE_DISPLAY}</span></a>
            <a href="{INSTAGRAM_URL}" target="_blank" rel="noopener">{I["insta"]}<span><small>Instagram</small>{INSTAGRAM_HANDLE}</span></a>
            <div>{I["pin"]}<span><small>Service area</small>{CITY}, India</span></div>
          </div>
          <div class="note mt"><strong>Before pickup:</strong> back up and reset devices, remove SIM and memory cards, and tape loose battery terminals. <a href="how-it-works.html#guidelines">Full guidelines</a></div>
        </div>
        <div class="card reveal" id="pickup">
          <h3 style="font-size:1.3rem">Request a pickup</h3>
          <p class="form-note" style="margin-bottom:16px">This opens your email app with the details filled in.</p>
          <form class="form" data-mailto="{EMAIL}" data-subject="TechSeva pickup request">
            <div class="row">
              <label>Name<input name="Name" required autocomplete="name"></label>
              <label>Phone<input name="Phone" type="tel" required autocomplete="tel"></label>
            </div>
            <label>Pickup address / area<input name="Address" required autocomplete="street-address"></label>
            <label>Items<textarea name="Items" required placeholder="e.g. 2 phones, 1 laptop, a bag of cables, 1 window AC"></textarea></label>
            <div class="row">
              <label>I am a<select name="Donor type"><option>Household</option><option>Housing society</option><option>School / college</option><option>Business / office</option></select></label>
              <label>Preferred time<input name="Preferred time" placeholder="e.g. weekends"></label>
            </div>
            <label class="check"><input type="checkbox" name="Data wiped" value="Yes" required> I’ll back up and wipe my devices before handover.</label>
            <button class="btn btn-primary" type="submit">Send request {A}</button>
            <p class="form-status form-note" role="status"></p>
          </form>
        </div>
      </div>
    </section>'''
page("contact.html", "Contact | TechSeva",
     "Contact TechSeva to request a free e-waste pickup in Kolkata or ask a question.", contact)

# ======================================================== 404
nf = f'''    <section class="page-hero" style="min-height:60vh;display:grid;align-items:center">
      <div class="container center">
        <div class="label">404</div>
        <h1 style="margin-inline:auto">This page has been recycled.</h1>
        <p class="lead" style="margin-inline:auto">We couldn’t find what you were looking for.</p>
        <div class="actions" style="justify-content:center"><a class="btn btn-primary" href="index.html">Back to home {A}</a></div>
      </div>
    </section>'''
page("404.html", "Page not found | TechSeva", "This page could not be found.", nf, current="none")

with open(os.path.join(OUT, "sitemap.xml"), "w") as f:
    urls = "".join(f"  <url><loc>{SITE}{'' if h == 'index.html' else h}</loc></url>\n" for h, _ in NAV + [("contact.html", "")])
    f.write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}</urlset>\n')
with open(os.path.join(OUT, "robots.txt"), "w") as f:
    f.write(f"User-agent: *\nAllow: /\nSitemap: {SITE}sitemap.xml\n")
print("built")

# TechSeva: E-Waste Service Org

Website for **TechSeva**, a student-led nonprofit e-waste collection initiative in Kolkata founded by Vivaan Agarwal.

Plain HTML/CSS/JS with no build step needed to host. Works on GitHub Pages as-is.

Design: a dark theme with an animated neural-network background (`assets/js/main.js`) and an iridescent 3D blob in the hero (`assets/js/blob.js`, using three.js r128 from `assets/js/vendor/`).

## Pages
| Page | File |
|---|---|
| Home | `index.html` |
| About (story, mission, values, founder, partner) | `about.html` |
| What We Accept (+ what we can't take, battery safety) | `what-we-accept.html` |
| How It Works (steps, general instructions, data-wipe guide) | `how-it-works.html` |
| Impact (stats, recycling certificates, gallery) | `impact.html` |
| Learn: E-Waste 101 (hazards, India's rules, tips) | `learn.html` |
| Get Involved (volunteer form, host a drive) | `get-involved.html` |
| FAQ | `faq.html` |
| Contact (pickup request form) | `contact.html` |

Forms open the visitor's email app with the details pre-filled (no server needed).

## Editing contact details
All pages are generated from `tools/build.py`. Change `EMAIL`, `PHONE_DISPLAY`, `PHONE_TEL`, `INSTAGRAM_URL` and `INSTAGRAM_HANDLE` at the top, then run:

```bash
python3 tools/build.py .
```

## Adding photos
Drop these files into `assets/img/` and they appear automatically in the "Recent collections" gallery (an icon shows until then):

- `collection-ac.jpg`: window AC
- `collection-uv-cabinet.jpg`: Philips UV-C cabinet
- `collection-monitor.jpg`: LG monitor
- `collection-cpu.jpg`: desktop CPU cabinet

## Logo
`assets/img/logo-full.svg` (full logo) and `assets/img/logo-mark.svg` (icon, also `favicon.svg`).
To use the original PNG logo instead, add it as `assets/img/logo.png` and point the `<img>` tags at it.

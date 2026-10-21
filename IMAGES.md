# Image slots

Drop files with EXACTLY these names into `/images/`. The HTML
references them directly — rename them and the slots break.

PNG with transparent background preferred unless noted. Recommended
dimensions are the maximum the site uses; browsers auto-scale down.

---

## 1. Branding (needed first)

| Filename | What | Recommended size |
|---|---|---|
| `logo.svg` | Main FreshGarant logo (leaf + wordmark) | SVG, any size |
| `logo-mark.svg` | Icon only, no wordmark — favicon + headers | SVG, square |
| `favicon.ico` | Browser tab icon (optional, SVG works too) | 32×32 |
| `og-image.png` | Social preview (WhatsApp / Twitter / LinkedIn link cards) | 1200×630, JPG also OK |

> SVG placeholders for `logo.svg`, `logo-mark.svg` and `og-image.svg`
> are already in the repo — replace them when you have the real assets.

---

## 2. Hero triptych (home page — 3 phones fanned out)

**You deliver 3 plain Android screenshots.** No device frame, no
status-bar overlays, no shadow — just the raw screenshot straight from
the phone. The site adds the white phone frame, the rounded corners,
the shadow and the rotation in CSS.

| Filename | What to screenshot | Position on hero |
|---|---|---|
| `hero-shot-1.png` | AI Fridge-Scan screen (camera or result view) | Left, rotated outward |
| `hero-shot-2.png` | Home / Dashboard (showing "Use these first" + monthly savings) | Center, raised forward |
| `hero-shot-3.png` | AI Recipe screen OR Cook tab with generated recipes | Right, rotated outward |

- **Resolution:** 1080 × 2340 px (Android standard). Any aspect close to
  9:19.5 works — the CSS crops with `object-fit: cover`.
- **Format:** PNG or JPG, either is fine.
- **Story the triptych tells:** left = scan it, middle = the app,
  right = cook it. Same visual grammar as CircuitTrace / BuildExact.

---

## 3. Feature screenshots (features page + home sections)

Same recipe: plain Android screenshots, 1080 × 2340 px. The CSS wraps
them in a phone frame on the pages that use them.

| Filename | What |
|---|---|
| `shot-home.png` | Home dashboard with "Use these first" + stats |
| `shot-fridge-scan.png` | AI Fridge Scan intro / result screen |
| `shot-receipt-scan.png` | Receipt scan intro / result screen |
| `shot-recipes.png` | "What can I cook?" / cookable recipes list |
| `shot-weekplan.png` | AI weekly meal plan |
| `shot-shopping.png` | Shopping list showing an "X in fridge" chip |
| `shot-calendar.png` | Expiry calendar (month view with colored dots) |
| `shot-stats.png` | Statistics screen with the freshness ring |
| `shot-family.png` | Family / shared inventory |
| `shot-notification.png` | Lockscreen push notification (daily digest) |

---

## 4. Savings calculator (savings page)

| Filename | What | Size |
|---|---|---|
| `calc-illustration.png` | Side illustration: coins + fresh food basket | 800×800, transparent BG |

Optional — if omitted, the page just shows the sliders + numbers.

---

## 5. Download page

| Filename | What |
|---|---|
| `play-store-badge-en.png` | Official "Get it on Google Play" badge (English) |
| `play-store-badge-nl.png` | Official "Ontdek het op Google Play" badge (Dutch) |
| `qr-play-store.png` | QR code pointing at the Play Store listing (512×512 PNG, black on white) |

> Official Google badges: <https://play.google.com/intl/en_us/badges/>

---

## 6. Contact page

| Filename | What | Size |
|---|---|---|
| `founder-photo.png` | Optional founder photo for the contact card | 400×400, square |

---

## Workflow when you add or replace an image

1. Save with the exact filename above into `/images/`.
2. Open the affected HTML page in a browser to verify.
3. `git add images/<file>` → `git commit` → `git push`.
4. Cloudflare Pages auto-redeploys within ~1 minute.

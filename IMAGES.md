# Image slots

Drop files with EXACTLY these names into `public/images/`. The site code
references them directly — rename them and the slots break.

All PNG with transparent background unless noted. Recommended dimensions
are the maximum the site uses; browsers auto-scale down.

## Branding (needed first)

| Filename | What | Recommended size |
|---|---|---|
| `logo.svg` | Main FreshGarant logo (green leaf + wordmark) | SVG, any size |
| `logo-mark.svg` | Icon only (no wordmark) for favicons | SVG, square |
| `favicon.ico` | Browser tab icon | 32×32 |
| `og-image.png` | Social preview (link previews on WhatsApp/Twitter/LinkedIn) | 1200×630, JPG also OK |

## Hero (home page)

| Filename | What | Recommended size |
|---|---|---|
| `hero-phones.png` | 3 phones showing Home, Fridge Scan, Recipes | 1600×1200, transparent BG |
| `hero-background.png` | Optional soft gradient / leaves pattern behind the phones | 2000×1200, blur-friendly |

## Feature screenshots (home + features page)

Use real app screenshots. Approx 540×1170 (device aspect ratio).
Transparent BG — I'll frame them in CSS.

| Filename | What |
|---|---|
| `shot-home.png` | Home dashboard with "Use these first" + stats |
| `shot-fridge-scan.png` | AI Fridge Scan intro screen |
| `shot-receipt-scan.png` | Receipt scan intro screen |
| `shot-recipes.png` | What can I cook? / cookable recipes |
| `shot-weekplan.png` | AI weekly meal plan |
| `shot-shopping.png` | Shopping list with "X in fridge" chip |
| `shot-calendar.png` | Expiry calendar |
| `shot-stats.png` | Statistics with freshness score ring |
| `shot-family.png` | Family / shared inventory |
| `shot-notification.png` | Lockscreen push notification mockup |

## Savings calculator (savings page)

| Filename | What |
|---|---|
| `calc-illustration.png` | Side illustration: coins + fresh food | 800×800 |

## Download page

| Filename | What |
|---|---|
| `play-store-badge-en.png` | Official "Get it on Google Play" badge (English) |
| `play-store-badge-nl.png` | Official "Ontdek het op Google Play" badge (Dutch) |
| `qr-play-store.png` | QR code pointing to the Play Store listing |

> Google provides the official Play Store badges here:
> <https://play.google.com/intl/en_us/badges/>

## Contact / about

| Filename | What |
|---|---|
| `founder-photo.png` | Optional founder photo for contact page | 400×400, square |

---

**Workflow when you add an image:**
1. Save with exact filename above into `public/images/`.
2. `npm run dev` to see it live.
3. Commit + push → Cloudflare auto-redeploys.

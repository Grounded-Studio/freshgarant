# FreshGarant — Official website

Marketing site for FreshGarant, the AI-powered food expiry tracker.
Plain static HTML + CSS + a dash of vanilla JS. Deployed via
[Cloudflare Pages](https://pages.cloudflare.com/).

- **English:** `/` (default)
- **Dutch:** `/nl/`
- **Domain:** freshgarant.app (DNS via Strato → Cloudflare)

## No build step

There's no framework, no bundler, no `npm install`. Open the HTML files,
edit them, commit, push. Cloudflare Pages serves them as-is.

To preview locally, just open `index.html` in a browser — or run any
static server:

```bash
python -m http.server 8000
```

Then open <http://localhost:8000>.

## Deploy to Cloudflare Pages

1. Push this repo to GitHub (owner `Grounded-Studio`, name `freshgarant`).
2. Cloudflare Dashboard → **Pages** → **Create project** → **Connect to Git**.
3. Pick the `freshgarant` repo.
4. Framework preset: **None**.
5. Build command: *(leave empty)*
6. Output directory: `/` (root)
7. Save & deploy.
8. In Cloudflare → **Custom domains** → add `freshgarant.app`.
9. In **Strato** DNS panel, point `freshgarant.app` at the Cloudflare
   CNAME targets (apex + `www`).
10. Wait 5–10 min for DNS propagation.

Every `git push` to `main` triggers an automatic redeploy.

## Project structure

```
.
├── index.html             ← English home
├── features.html          ← English feature list
├── savings.html           ← English savings calculator
├── download.html
├── privacy.html
├── terms.html
├── contact.html
├── 404.html               ← bilingual not-found page
├── nl/                    ← Dutch mirrors of all pages
│   ├── index.html
│   ├── features.html
│   └── …
├── assets/
│   ├── css/global.css     ← one stylesheet for every page
│   └── js/savings-calc.js ← slider logic for the calculator
├── images/                ← logo + OG image + your product shots
├── _headers               ← Cloudflare security + cache headers
├── robots.txt
├── CNAME                  ← freshgarant.app
└── IMAGES.md              ← filename list for product screenshots
```

## Adding a new page

1. Copy an existing HTML file (e.g. `features.html` → `your-page.html`).
2. Edit the `<title>`, `<meta description>`, `<h1>` and body.
3. Update the `<link rel="canonical">` and both `hreflang` URLs.
4. Add a Dutch mirror in `nl/your-page.html` with the same tweaks.
5. Add navigation entries in the `<header>` of every page where you want
   it to appear, and in the footer `Product` / `Juridisch` columns.

## Editing shared chrome

Header, footer and nav live **inline** in each page. There's no
templating. When you change the nav structure, update every file — a
quick `rg` + search-and-replace does the trick.

## Image slots

See [`IMAGES.md`](./IMAGES.md) for the full list of placeholder
filenames the site expects under `/images/`. Drop PNG/JPG files with
those exact names — the pages pick them up automatically.

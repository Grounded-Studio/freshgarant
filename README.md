# FreshGarant — Official website

Marketing site for FreshGarant, the AI-powered food expiry tracker.
Built with [Astro 4](https://astro.build/), deployed via
[Cloudflare Pages](https://pages.cloudflare.com/).

- **English:** `/` (default)
- **Dutch:** `/nl/`
- **Domain:** freshgarant.app (DNS via Strato → Cloudflare)

## Local development

```bash
npm install
npm run dev
```

Open <http://localhost:4321>.

## Build

```bash
npm run build
```

Static output lands in `./dist/`.

## Deploy to Cloudflare Pages

1. Push this repo to GitHub (owner `Grounded-Studio`, name `freshgarant`).
2. Cloudflare Dashboard → **Pages** → **Create project** → **Connect to Git**.
3. Pick the `freshgarant` repo.
4. Framework preset: **Astro**.
5. Build command: `npm run build`
6. Output directory: `dist`
7. Save & deploy.
8. In Cloudflare → **Custom domains** → add `freshgarant.app`.
9. In **Strato** DNS panel, replace the current `freshgarant.app` →
   `grounded-studio.app` redirect with the two `CNAME` records
   Cloudflare gives you (one for apex, one for `www`).
10. Wait 5–10 min for DNS propagation.

## Project structure

```
.
├── public/images/         ← drop PNG/JPG assets here (see IMAGES.md)
├── src/
│   ├── i18n/strings.ts    ← all page copy, EN + NL side by side
│   ├── layouts/Base.astro ← shared <head>, nav, footer
│   ├── pages/             ← English pages (/, /features, /savings, …)
│   └── pages/nl/          ← Dutch mirrors (/nl/, /nl/features, …)
└── astro.config.mjs
```

## Adding new pages

1. Create `src/pages/your-page.astro` (English).
2. Create `src/pages/nl/your-page.astro` (Dutch mirror).
3. Add navigation entry in `src/layouts/Base.astro`.
4. Add strings in `src/i18n/strings.ts`.

## Image slots

See [`IMAGES.md`](./IMAGES.md) for the full list of placeholder filenames
the site expects in `public/images/`. Drop PNG/JPG files with those exact
names — the site auto-picks them up.

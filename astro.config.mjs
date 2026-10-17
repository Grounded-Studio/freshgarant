import { defineConfig } from 'astro/config';
import react from '@astrojs/react';

// FreshGarant marketing site.
// Static build (zero server), deployed via Cloudflare Pages.
// React is enabled as an "island" integration so interactive bits
// (like the Savings Calculator) can live inside otherwise-static pages
// without turning the whole site into an SPA.
//
// Note: @astrojs/sitemap v3 crashed on this i18n+trailingSlash combo.
// Removed for now — Google will discover all pages via internal links,
// and hreflang alternates are already emitted in <head> via Base.astro.
// Can re-add later when the plugin resolves the config conflict.
export default defineConfig({
  site: 'https://freshgarant.app',
  trailingSlash: 'never',
  integrations: [
    react(),
  ],
  i18n: {
    defaultLocale: 'en',
    locales: ['en', 'nl'],
    routing: {
      prefixDefaultLocale: false, // English at /, Dutch at /nl/
    },
  },
});

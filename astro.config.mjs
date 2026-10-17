import { defineConfig } from 'astro/config';
import react from '@astrojs/react';
import sitemap from '@astrojs/sitemap';

// FreshGarant marketing site.
// Static build (zero server), deployed via Cloudflare Pages.
// React is enabled as an "island" integration so interactive bits
// (like the Savings Calculator) can live inside otherwise-static pages
// without turning the whole site into an SPA.
export default defineConfig({
  site: 'https://freshgarant.app',
  trailingSlash: 'never',
  integrations: [
    react(),
    sitemap({
      // Lets Google know we serve the same content in English + Dutch.
      i18n: {
        defaultLocale: 'en',
        locales: {
          en: 'en-US',
          nl: 'nl-NL',
        },
      },
    }),
  ],
  i18n: {
    defaultLocale: 'en',
    locales: ['en', 'nl'],
    routing: {
      prefixDefaultLocale: false, // English at /, Dutch at /nl/
    },
  },
});

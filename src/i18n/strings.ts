/* ─────────────────────────────────────────────────────────────────────────
   All user-facing copy lives here, EN + NL side by side.
   Pages import `t(lang)` to get the right bundle. Adding a new string?
   Add it to BOTH `en` and `nl` with the same key — TypeScript will yell
   at the page files until you do.
   ──────────────────────────────────────────────────────────────────────── */

export type Lang = 'en' | 'nl';

const en = {
  // Nav
  nav: {
    home: 'Home',
    features: 'Features',
    savings: 'Savings',
    download: 'Download',
    contact: 'Contact',
    cta: 'Get the app',
  },

  // Footer
  footer: {
    tagline: 'Scan your groceries. Cook what’s fresh. Never waste food again.',
    product: 'Product',
    legal: 'Legal',
    links: {
      features: 'Features',
      savings: 'Savings calculator',
      download: 'Download',
      privacy: 'Privacy',
      terms: 'Terms',
      contact: 'Contact',
    },
    copyright: '© {year} Grounded Studio · Made with care in the Netherlands',
  },

  // Home / Hero
  home: {
    heroKicker: 'AI-POWERED FOOD TRACKER',
    heroTitle: 'Never waste food again.',
    heroLead:
      'FreshGarant scans your groceries, warns you before anything expires, and turns almost-expired ingredients into recipes you’ll actually cook. Free to start, no account needed.',
    ctaDownload: 'Get it on Google Play',
    ctaSeeFeatures: 'See all features',
    stat1Value: '40',
    stat1Label: 'free products',
    stat2Value: '1×',
    stat2Label: 'free trial per AI feature',
    stat3Value: '€12+',
    stat3Label: 'average saved / month',

    featuresKicker: 'WHAT IT DOES',
    featuresTitle: 'Three ways FreshGarant actually helps.',
    featuresSub:
      'Not another to-do list for food. A real workflow built around the moment food goes bad.',

    f1Emoji: '\u{1F4E6}',
    f1Title: 'Scan, don’t type',
    f1Body: 'Scan a barcode, a receipt or your whole fridge with AI. Products land in your inventory with name, category, storage and expiry date auto-filled.',
    f2Emoji: '\u{1F514}',
    f2Title: 'Reminders before it’s too late',
    f2Body: 'A single daily morning digest tells you what expires today, tomorrow and this week. Freeze-it hints for items you can save.',
    f3Emoji: '\u{1F373}',
    f3Title: 'Cook what’s fresh',
    f3Body: 'Tap the Cook tab — recipes are matched to your real fridge, prioritising items that expire soonest. Gemini AI generates one on the fly if nothing fits.',

    aiKicker: 'AI FEATURES',
    aiTitle: 'Gemini AI does the tedious parts.',
    aiSub:
      'Every free user gets one lifetime trial of every AI feature before any paywall. Experience the magic, then decide.',

    ai1Title: 'AI Fridge Scan',
    ai1Body: 'One photo of your fridge. Gemini recognises every product, suggests a category, storage location and expiry date. A full inventory in under a minute.',
    ai2Title: 'AI Receipt Scan',
    ai2Body: 'Photograph your grocery receipt and FreshGarant adds every item at once. Perfect after a big shop.',
    ai3Title: 'AI Recipes',
    ai3Body: 'Turn soon-to-expire ingredients into personalised recipes. Less waste, more flavour — fresh ideas every time.',
    ai4Title: 'AI Weekly Meal Plan',
    ai4Body: 'One tap generates a complete 7-day dinner menu around what you already have. Auto shopping list for anything missing.',

    savingsKicker: 'HOW MUCH DO YOU WASTE?',
    savingsTitle: 'The average household throws €540 of food in the bin each year.',
    savingsSub: 'Our calculator estimates what FreshGarant could realistically save you.',
    savingsCta: 'Open the savings calculator',

    finalCtaTitle: 'Ready to stop throwing food away?',
    finalCtaBody: 'Install FreshGarant free from the Play Store. Add your first few groceries in under a minute.',
    finalCtaBtn: 'Download FreshGarant',
  },

  // Image slot labels (visible when image is missing)
  slot: {
    heroPhones: 'hero-phones.png (3 phones mockup)',
    shotHome: 'shot-home.png',
    shotFridge: 'shot-fridge-scan.png',
    shotReceipt: 'shot-receipt-scan.png',
    shotRecipes: 'shot-recipes.png',
    shotWeekplan: 'shot-weekplan.png',
    shotCalendar: 'shot-calendar.png',
    shotStats: 'shot-stats.png',
    shotShopping: 'shot-shopping.png',
  },
};

const nl: typeof en = {
  nav: {
    home: 'Home',
    features: 'Functies',
    savings: 'Besparing',
    download: 'Download',
    contact: 'Contact',
    cta: 'Download de app',
  },

  footer: {
    tagline: 'Scan je boodschappen. Kook wat vers is. Nooit meer eten weggooien.',
    product: 'Product',
    legal: 'Juridisch',
    links: {
      features: 'Functies',
      savings: 'Besparings-calculator',
      download: 'Download',
      privacy: 'Privacy',
      terms: 'Voorwaarden',
      contact: 'Contact',
    },
    copyright: '© {year} Grounded Studio · Gemaakt met zorg in Nederland',
  },

  home: {
    heroKicker: 'AI-GEDREVEN VOEDSELTRACKER',
    heroTitle: 'Nooit meer eten weggooien.',
    heroLead:
      'FreshGarant scant je boodschappen, waarschuwt je voordat iets verloopt, en maakt van bijna-verlopen ingrediënten recepten die je echt gaat koken. Gratis starten, geen account nodig.',
    ctaDownload: 'Ontdek het op Google Play',
    ctaSeeFeatures: 'Bekijk alle functies',
    stat1Value: '40',
    stat1Label: 'gratis producten',
    stat2Value: '1×',
    stat2Label: 'gratis probeersel per AI-functie',
    stat3Value: '€12+',
    stat3Label: 'gemiddeld bespaard / maand',

    featuresKicker: 'WAT HET DOET',
    featuresTitle: 'Drie manieren waarop FreshGarant echt helpt.',
    featuresSub:
      'Niet nog een to-do lijst voor eten. Een echte workflow rond het moment dat eten slecht wordt.',

    f1Emoji: '\u{1F4E6}',
    f1Title: 'Scannen, niet typen',
    f1Body: 'Scan een barcode, een kassabon of je hele koelkast met AI. Producten komen binnen met naam, categorie, opslag en vervaldatum automatisch ingevuld.',
    f2Emoji: '\u{1F514}',
    f2Title: 'Meldingen vóór het te laat is',
    f2Body: 'Eén dagelijkse ochtend-samenvatting toont wat vandaag, morgen en deze week verloopt. Freeze-tips voor items die je nog kan redden.',
    f3Emoji: '\u{1F373}',
    f3Title: 'Kook wat vers is',
    f3Body: 'Tik op de Kook-tab — recepten gematcht met je echte koelkast, met voorrang voor items die het eerst verlopen. Gemini AI genereert on-the-fly een recept als er niks past.',

    aiKicker: 'AI-FUNCTIES',
    aiTitle: 'Gemini AI doet het saaie werk.',
    aiSub:
      'Elke free user krijgt één lifetime probeersel van elke AI-functie voor de paywall. Ervaar de magie, beslis dan.',

    ai1Title: 'AI Koelkast-scan',
    ai1Body: 'Eén foto van je koelkast. Gemini herkent elk product, stelt categorie, opslaglocatie en vervaldatum voor. Volledige voorraad in minder dan een minuut.',
    ai2Title: 'AI Kassabon-scan',
    ai2Body: 'Fotografeer je kassabon en FreshGarant voegt alle items in één keer toe. Perfect na een grote boodschappenronde.',
    ai3Title: 'AI Recepten',
    ai3Body: 'Maak van bijna-verlopen ingrediënten persoonlijke recepten. Minder verspilling, meer smaak — elke keer nieuwe ideeën.',
    ai4Title: 'AI Weekplanner',
    ai4Body: 'Eén tik genereert een compleet 7-daags avondeten-menu rond wat je al hebt. Automatische boodschappenlijst voor wat nog ontbreekt.',

    savingsKicker: 'HOEVEEL VERSPIL JIJ?',
    savingsTitle: 'Een gemiddeld huishouden gooit €540 aan eten per jaar weg.',
    savingsSub: 'Onze calculator schat wat FreshGarant jou realistisch zou kunnen besparen.',
    savingsCta: 'Open de besparings-calculator',

    finalCtaTitle: 'Klaar om geen eten meer weg te gooien?',
    finalCtaBody: 'Download FreshGarant gratis vanuit de Play Store. Voeg je eerste boodschappen toe in minder dan een minuut.',
    finalCtaBtn: 'Download FreshGarant',
  },

  slot: {
    heroPhones: 'hero-phones.png (3 telefoons mockup)',
    shotHome: 'shot-home.png',
    shotFridge: 'shot-fridge-scan.png',
    shotReceipt: 'shot-receipt-scan.png',
    shotRecipes: 'shot-recipes.png',
    shotWeekplan: 'shot-weekplan.png',
    shotCalendar: 'shot-calendar.png',
    shotStats: 'shot-stats.png',
    shotShopping: 'shot-shopping.png',
  },
};

export const t = (lang: Lang) => (lang === 'nl' ? nl : en);

export const PLAY_STORE_URL =
  'https://play.google.com/store/apps/details?id=nl.versgarant.versgarant';
export const CONTACT_EMAIL = 'contact@grounded-studio.app';

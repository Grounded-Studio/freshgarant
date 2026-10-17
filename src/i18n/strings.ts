/* ─────────────────────────────────────────────────────────────────────────
   All user-facing copy lives here, EN + NL side by side.
   Pages import `t(lang)` to get the right bundle. Adding a new string?
   Add it to BOTH `en` and `nl` with the same key — TypeScript will yell
   at the page files until you do.
   ──────────────────────────────────────────────────────────────────────── */

export type Lang = 'en' | 'nl';

const en = {
  nav: {
    home: 'Home',
    features: 'Features',
    savings: 'Savings',
    download: 'Download',
    contact: 'Contact',
    cta: 'Get the app',
  },

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

  // ── Savings calculator page ──────────────────────────────────────────
  savings: {
    heroKicker: 'SAVINGS CALCULATOR',
    heroTitle: 'How much could you save?',
    heroLead:
      'Tweak the sliders to match your household. We use conservative, published figures — no inflated marketing numbers.',

    weeklySpendLabel: 'Weekly grocery spend',
    wastePercentLabel: 'Of your groceries, how much do you throw away?',
    wasteHint: 'Dutch household average: around 14%',

    resultTitle: 'Your estimated savings with FreshGarant',
    perMonth: 'per month',
    perYear: 'per year',
    co2Saved: 'kg CO₂ prevented per year',
    co2Hint: 'Based on 2.5 kg CO₂-eq per kg of food waste (EPA average).',

    currentWasteLabel: 'What you currently throw away',
    newWasteLabel: 'With FreshGarant',

    reductionNote:
      'We assume a 50% reduction in food waste — the midpoint of studies on tracker-app users (range: 30–70%).',
    sourcesTitle: 'Where the numbers come from',
    sources: [
      'Milieu Centraal — Dutch household food waste averages',
      'EPA — greenhouse gas equivalents for food waste',
      'Independent studies on inventory-tracking app effectiveness',
    ],

    ctaBand: 'Ready to start saving?',
    ctaBtn: 'Download FreshGarant free',
  },

  // ── Features page ────────────────────────────────────────────────────
  features: {
    heroKicker: 'EVERY FEATURE',
    heroTitle: 'Everything FreshGarant does.',
    heroLead:
      'A complete tour of the app. Free features in green, PRO features in gold — plus one lifetime trial for every AI feature.',

    g1Title: 'Add groceries fast',
    g1Items: [
      { title: 'Barcode scanner', body: 'Auto-fills name, brand, category, storage, expiry.', pro: false },
      { title: 'Receipt scan (AI)', body: 'Photograph a receipt → every item added at once.', pro: true, trial: true },
      { title: 'Fridge scan (AI)', body: 'One photo of your fridge → Gemini detects every product.', pro: true, trial: true },
      { title: 'Manual add with quick-fill', body: 'Common items as one-tap chips. Up to 40 free, unlimited with PRO.', pro: false },
    ],

    g2Title: 'Never miss expiry',
    g2Items: [
      { title: 'Morning digest push', body: 'One daily reminder of what expires today, tomorrow, this week.', pro: false },
      { title: 'Freeze-it hints', body: 'Suggests freezing items that can still be saved.', pro: false },
      { title: 'Expiry calendar', body: 'Month view with coloured dots per expiry status.', pro: false },
      { title: 'Nearby-store alerts', body: 'Push when you’re near a saved supermarket with items on your list.', pro: false },
    ],

    g3Title: 'Use what you have',
    g3Items: [
      { title: 'Cook tab', body: 'Recipes matched to your real fridge, prioritising expiring items.', pro: false },
      { title: 'AI Recipe generation', body: 'Gemini turns your inventory into a custom recipe on demand.', pro: true, trial: true },
      { title: 'AI Weekly Meal Plan', body: 'A full 7-day dinner menu built around what you already have.', pro: true, trial: true },
      { title: 'Cook Mode', body: 'Fullscreen recipe view with per-step timers, screen stays on.', pro: true },
    ],

    g4Title: 'See your impact',
    g4Items: [
      { title: 'Instant savings reward', body: '“🎉 €2.49 saved!” snackbar every time you use food in time.', pro: false },
      { title: 'Monthly savings banner', body: 'What you saved this month, right on home.', pro: false },
      { title: 'Statistics (on-time use, streaks, trends)', body: 'Full dashboard: waste cost, best month, categories.', pro: true },
      { title: '18 achievements', body: 'Kitchen Master, AI Chef, Royal Streak and more.', pro: false },
      { title: 'Year in Review', body: 'Spotify-style recap: money saved, CO₂ prevented, longest streak.', pro: false },
    ],

    g5Title: 'Smart shopping',
    g5Items: [
      { title: 'Smart shopping list', body: 'Auto-suggestions, duplicates merge, supermarket-aisle sort.', pro: false },
      { title: '“X in fridge” chip', body: 'Shows how many of each item you already own — skip duplicates.', pro: false },
      { title: 'Price-drop alerts', body: 'Push when a product you track drops 8%+ in price.', pro: false },
      { title: 'Multi-store support', body: 'Save your supermarkets, split your list per store.', pro: false },
    ],

    g6Title: 'Together',
    g6Items: [
      { title: 'Family sharing', body: 'Realtime shared pantry — everyone sees the same products instantly.', pro: true },
      { title: 'Shared shopping list', body: 'One list, all household members.', pro: true },
      { title: 'Invite friends → PRO free', body: 'Both get 1 month PRO when they install via your code.', pro: false },
    ],

    g7Title: 'Nutrition & diets',
    g7Items: [
      { title: 'Calories & nutrition via barcode', body: 'Protein, carbs, fat, fibre, salt — via Open Food Facts.', pro: true },
      { title: 'Dietary tags', body: 'Vegan, vegetarian, gluten-free, lactose-free alerts.', pro: false },
    ],

    freeLabel: 'FREE',
    proLabel: 'PRO',
    trialLabel: '1 free trial',

    ctaTitle: 'Start with the free tier, upgrade when you need it.',
    ctaBtn: 'Download FreshGarant',
  },

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
    calcIllustration: 'calc-illustration.png',
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

  savings: {
    heroKicker: 'BESPARINGS-CALCULATOR',
    heroTitle: 'Hoeveel kan jij besparen?',
    heroLead:
      'Verschuif de sliders zodat ze bij jouw huishouden passen. We rekenen met conservatieve, gepubliceerde cijfers — geen opgeklopte marketing.',

    weeklySpendLabel: 'Wekelijkse boodschappen-uitgaven',
    wastePercentLabel: 'Hoeveel van je boodschappen gooi je weg?',
    wasteHint: 'Nederlands huishouden gemiddeld: ongeveer 14%',

    resultTitle: 'Jouw geschatte besparing met FreshGarant',
    perMonth: 'per maand',
    perYear: 'per jaar',
    co2Saved: 'kg CO₂ voorkomen per jaar',
    co2Hint: 'Gebaseerd op 2,5 kg CO₂-eq per kg voedselverspilling (EPA gemiddelde).',

    currentWasteLabel: 'Wat je nu weggooit',
    newWasteLabel: 'Met FreshGarant',

    reductionNote:
      'We rekenen met 50% minder voedselverspilling — het middenpunt van studies naar tracker-app gebruikers (bereik: 30–70%).',
    sourcesTitle: 'Waar de cijfers vandaan komen',
    sources: [
      'Milieu Centraal — gemiddelde Nederlandse huishoud-voedselverspilling',
      'EPA — broeikasgas-equivalenten voor voedselafval',
      'Onafhankelijke studies naar effectiviteit van inventaris-tracker apps',
    ],

    ctaBand: 'Klaar om te beginnen met besparen?',
    ctaBtn: 'Download FreshGarant gratis',
  },

  features: {
    heroKicker: 'ALLE FUNCTIES',
    heroTitle: 'Alles wat FreshGarant doet.',
    heroLead:
      'Een complete tour door de app. Gratis functies in groen, PRO-functies in goud — plus één lifetime probeersel voor elke AI-functie.',

    g1Title: 'Boodschappen snel toevoegen',
    g1Items: [
      { title: 'Barcode-scanner', body: 'Vult naam, merk, categorie, opslag en vervaldatum automatisch in.', pro: false },
      { title: 'Kassabon-scan (AI)', body: 'Fotografeer een kassabon → alle items in één keer toegevoegd.', pro: true, trial: true },
      { title: 'Koelkast-scan (AI)', body: 'Eén foto van je koelkast → Gemini herkent elk product.', pro: true, trial: true },
      { title: 'Handmatig met snelkeuze', body: 'Veelvoorkomende items als one-tap chips. Tot 40 gratis, onbeperkt met PRO.', pro: false },
    ],

    g2Title: 'Mis nooit meer een vervaldatum',
    g2Items: [
      { title: 'Ochtend-digest push', body: 'Eén dagelijkse herinnering van wat vandaag, morgen, deze week verloopt.', pro: false },
      { title: 'Freeze-it tips', body: 'Stelt voor items te bevriezen die je nog kan redden.', pro: false },
      { title: 'Vervalkalender', body: 'Maandoverzicht met gekleurde stippen per verval-status.', pro: false },
      { title: 'Melding bij winkel in buurt', body: 'Push als je in de buurt bent van een opgeslagen supermarkt met items op je lijst.', pro: false },
    ],

    g3Title: 'Gebruik wat je al hebt',
    g3Items: [
      { title: 'Kook-tab', body: 'Recepten gematcht met je echte koelkast, met voorrang voor bijna-verlopende items.', pro: false },
      { title: 'AI Recept-generatie', body: 'Gemini maakt on-demand een persoonlijk recept van je voorraad.', pro: true, trial: true },
      { title: 'AI Weekplanner', body: 'Een compleet 7-daags avondeten-menu rond wat je al hebt.', pro: true, trial: true },
      { title: 'Kook-modus', body: 'Fullscreen recept-weergave met timers per stap, scherm blijft aan.', pro: true },
    ],

    g4Title: 'Zie je impact',
    g4Items: [
      { title: 'Directe bespaar-beloning', body: '“🎉 €2,49 bespaard!” snackbar elke keer dat je eten op tijd gebruikt.', pro: false },
      { title: 'Maandelijkse besparing-banner', body: 'Wat je deze maand bespaarde, direct op home.', pro: false },
      { title: 'Statistieken (on-time, streaks, trends)', body: 'Volledig dashboard: verspillingskosten, beste maand, categorieën.', pro: true },
      { title: '18 prestaties', body: 'Keukenmeester, AI Chef, Royal Streak en meer.', pro: false },
      { title: 'Jaaroverzicht', body: 'Spotify-stijl recap: bespaard geld, CO₂ voorkomen, langste streak.', pro: false },
    ],

    g5Title: 'Slim winkelen',
    g5Items: [
      { title: 'Slimme boodschappenlijst', body: 'Automatische suggesties, dubbele items voegen samen, sorteer op supermarkt-gangpad.', pro: false },
      { title: '“X in koelkast” chip', body: 'Toont hoeveel je al hebt van elk item — geen dubbele boodschappen.', pro: false },
      { title: 'Prijs-daal meldingen', body: 'Push als een product dat je volgt 8%+ in prijs zakt.', pro: false },
      { title: 'Multi-store support', body: 'Sla je supermarkten op, verdeel je lijst per winkel.', pro: false },
    ],

    g6Title: 'Samen',
    g6Items: [
      { title: 'Familie delen', body: 'Realtime gedeelde voorraad — iedereen ziet dezelfde producten direct.', pro: true },
      { title: 'Gedeelde boodschappenlijst', body: 'Eén lijst, alle huisgenoten.', pro: true },
      { title: 'Vrienden uitnodigen → PRO gratis', body: 'Beide krijgen 1 maand PRO als ze installeren via jouw code.', pro: false },
    ],

    g7Title: 'Voeding & diëten',
    g7Items: [
      { title: 'Calorieën & voeding via barcode', body: 'Eiwit, koolhydraten, vet, vezels, zout — via Open Food Facts.', pro: true },
      { title: 'Dieet-tags', body: 'Vegan, vegetarisch, glutenvrij, lactosevrij meldingen.', pro: false },
    ],

    freeLabel: 'GRATIS',
    proLabel: 'PRO',
    trialLabel: '1 gratis probeersel',

    ctaTitle: "Begin gratis, upgrade wanneer je 't nodig hebt.",
    ctaBtn: 'Download FreshGarant',
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
    calcIllustration: 'calc-illustration.png',
  },
};

export const t = (lang: Lang) => (lang === 'nl' ? nl : en);

export const PLAY_STORE_URL =
  'https://play.google.com/store/apps/details?id=nl.versgarant.versgarant';
export const CONTACT_EMAIL = 'contact@grounded-studio.app';

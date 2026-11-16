"""Storage guides, batch B: chicken, milk, yoghurt, cheese, eggs, cream.
Fridge times from the Voedingscentrum Bewaarwijzer apply to an OPENED
product; an unopened pack follows the date on the pack."""

GUIDES_B = [
# ─────────────────────────────── CHICKEN ───────────────────────────────
{
 "key": "chicken", "emoji": "🍗",
 "sources": ["vc_bewaarwijzer", "vc_veilig", "vc_ontdooien", "fsa_campy", "fsa_chill", "fsa_cook"],
 "en": {
  "slug": "how-long-does-chicken-last", "name": "Chicken",
  "title": "How Long Does Chicken Last in the Fridge?",
  "desc": "Raw chicken keeps 2 days in the fridge once opened, never past its use-by date. Cooked chicken 2 days, frozen about 3 months. Safe storage tips.",
  "h1": "How long does chicken last in the fridge?",
  "answer": "Raw chicken keeps <strong>2 days in the fridge</strong> once the pack is opened, according to the Voedingscentrum, and never past its use-by date. Cooked chicken also keeps 2 days. In the freezer, raw or cooked chicken keeps about 3 months. Never wash raw chicken, and always cook it all the way through.",
  "table_head": ("", "How long", "Source"),
  "table": [
   ("Raw chicken, fridge (opened)", "2 days, and never past the use-by date", "Voedingscentrum"),
   ("Raw chicken, freezer", "About 3 months; meat is best within 2–3 months", "Voedingscentrum · FSA"),
   ("Cooked chicken, fridge", "2 days (48 hours)", "Voedingscentrum · FSA"),
   ("Cooked chicken, freezer", "About 3 months", "Voedingscentrum"),
   ("After defrosting", "Use within 24 hours", "FSA"),
   ("Out of the fridge", "Never more than 2 hours", "Voedingscentrum"),
  ],
  "body": """
<h2>Why chicken needs extra care</h2>
<p>Raw chicken often carries bacteria such as campylobacter, which the Food Standards Agency calls the main cause of bacterial food poisoning in the UK. A very small number of these bacteria can already make you ill. That is why chicken has a use-by date, and why storing, handling and cooking it correctly matters more than for most other food.</p>

<h2>How to store raw chicken</h2>
<ul>
  <li><strong>Bottom shelf, covered.</strong> Keep raw chicken in its packaging or a sealed container on the bottom shelf, so juices cannot drip onto other food.</li>
  <li><strong>Cold enough.</strong> The FSA advises a fridge between 0 and 5°C; the Voedingscentrum advises 4°C.</li>
  <li><strong>Use-by is a hard limit.</strong> Do not eat chicken after its use-by date, even if it looks and smells normal.</li>
  <li><strong>Once opened:</strong> the Voedingscentrum gives 2 days in the fridge.</li>
</ul>

<h2>Never wash raw chicken</h2>
<p>Rinsing chicken under the tap does not make it safer. The FSA warns that washing raw chicken splashes campylobacter onto your hands, worktop, clothes and utensils. Cooking kills the bacteria; washing only spreads them. Use a separate chopping board for raw meat, and wash your hands after touching it.</p>

<h2>Can you freeze chicken?</h2>
<p>Yes. You can freeze chicken right up until midnight on its use-by date, according to the FSA. The Voedingscentrum gives about 3 months in the freezer at −18°C; the FSA says meat is usually best within 2–3 months. Freeze it in portions and write the date on the bag.</p>
<p>Defrost chicken in the fridge, on a covered plate or in a bowl on the bottom shelf, starting a day before you need it. Once fully defrosted, use it within 24 hours. Small pieces can be defrosted in the microwave, but then cook them straight away.</p>

<h2>Cook chicken all the way through</h2>
<p>Poultry can carry bacteria all the way through the meat, so it must never be eaten pink. The FSA advises checking that the chicken is steaming hot all the way through, that none of the meat is pink when you cut into the thickest part, and that the juices run clear. With a thermometer, the middle should reach 70°C for 2 minutes.</p>

<h2>Cooked chicken and leftovers</h2>
<p>Let cooked chicken cool and put it in the fridge within 1–2 hours, covered. It keeps 2 days in the fridge, or about 3 months in the freezer. Leftovers can be eaten cold, or reheated once until steaming hot.</p>

<h2>How to tell if chicken has gone off</h2>
<p>The Voedingscentrum lists these signs: an unusual smell, a grey discolouration, a dried-out or sticky surface. If you notice any of them, throw it away. But a normal smell is no guarantee: the bacteria that cause food poisoning cannot be smelled, so never use a sniff test to decide on chicken past its use-by date.</p>

<h2>Tips to waste less chicken</h2>
<ul>
  <li>Freeze chicken on the day you buy it if you will not cook it within a day or two.</li>
  <li>Cook extra and use the leftovers the next day in a wrap, salad or soup.</li>
  <li>Log the use-by date in FreshGarant, so you get a reminder before it has to go.</li>
</ul>
""",
  "faq": [
   ("Can you eat chicken one day after the use-by date?", "No. The use-by date on chicken is about safety. Do not eat it afterwards, even if it looks and smells fine."),
   ("How long does cooked chicken last in the fridge?", "2 days, according to the Voedingscentrum; the FSA advises eating leftovers within 48 hours."),
   ("Should you wash raw chicken?", "No. Washing spreads campylobacter around your kitchen. Thorough cooking is what kills the bacteria."),
   ("Can you refreeze chicken?", "Not raw after defrosting. Cook it first; you can freeze the cooked dish and reheat it once."),
   ("How do I know chicken is cooked?", "It is steaming hot all the way through, no meat is pink in the thickest part and the juices run clear."),
  ],
  "related": ["mince", "leftovers", "fish"],
 },
 "nl": {
  "slug": "hoe-lang-is-kip-houdbaar", "name": "Kip",
  "title": "Hoe Lang Is Kip Houdbaar in de Koelkast?",
  "desc": "Rauwe kip blijft na openen 2 dagen goed in de koelkast, nooit na de TGT-datum. Bereide kip 2 dagen, ingevroren zo'n 3 maanden. Tips en bederf.",
  "h1": "Hoe lang is kip houdbaar in de koelkast?",
  "answer": "Rauwe kipfilet blijft volgens het Voedingscentrum <strong>2 dagen goed in de koelkast</strong> als de verpakking open is, en nooit na de TGT-datum. Bereide kip houd je ook 2 dagen. In de vriezer blijft rauwe of bereide kip zo'n 3 maanden goed. Was rauwe kip nooit, en bak hem altijd helemaal gaar.",
  "table_head": ("", "Hoe lang", "Bron"),
  "table": [
   ("Rauwe kip, koelkast (geopend)", "2 dagen, en nooit na de TGT-datum", "Voedingscentrum"),
   ("Rauwe kip, vriezer", "Ongeveer 3 maanden", "Voedingscentrum"),
   ("Bereide kip, koelkast", "2 dagen", "Voedingscentrum"),
   ("Bereide kip, vriezer", "Ongeveer 3 maanden", "Voedingscentrum"),
   ("Na het ontdooien", "Binnen 24 uur gebruiken", "FSA"),
   ("Buiten de koelkast", "Nooit langer dan 2 uur", "Voedingscentrum"),
  ],
  "body": """
<h2>Waarom kip extra aandacht nodig heeft</h2>
<p>Op rauwe kip zitten vaak bacteriën zoals campylobacter. Volgens de Britse Food Standards Agency (FSA) is dat de belangrijkste oorzaak van bacteriële voedselvergiftiging in het Verenigd Koninkrijk, en kan een heel klein aantal bacteriën je al ziek maken. Daarom staat er op kip een TGT-datum, en daarom is goed bewaren en goed garen bij kip extra belangrijk.</p>

<h2>Zo bewaar je rauwe kip</h2>
<ul>
  <li><strong>Onderin de koelkast, afgedekt.</strong> Dan kan vleessap niet op andere producten lekken. Het Voedingscentrum raadt aan rauw vlees op de koudste plek te bewaren.</li>
  <li><strong>Koud genoeg.</strong> Zet je koelkast op 4 °C.</li>
  <li><strong>De TGT-datum is een harde grens.</strong> Eet kip daarna niet meer, ook als hij er goed uitziet en normaal ruikt.</li>
  <li><strong>Na openen:</strong> volgens het Voedingscentrum 2 dagen in de koelkast.</li>
</ul>

<h2>Was rauwe kip nooit</h2>
<p>Kip afspoelen maakt hem niet veiliger. De FSA waarschuwt dat je met wassen campylobacter op je handen, aanrecht, kleding en keukengerei spat. Goed garen doodt de bacteriën; wassen verspreidt ze alleen. Gebruik een aparte snijplank voor rauw vlees en was je handen nadat je het hebt aangeraakt.</p>

<h2>Kun je kip invriezen?</h2>
<p>Ja. Vries kip in vóór de TGT-datum. Volgens het Voedingscentrum blijft kip zo'n 3 maanden goed in de vriezer op −18 °C. Te lang in de vriezer geeft een ranzige geur en smaak. Vries in porties in en zet de datum op het zakje.</p>
<p>Ontdooi kip in de koelkast: leg hem een dag van tevoren afgedekt op een bord of in een schaal onderin de koelkast. Is hij helemaal ontdooid, gebruik hem dan binnen 24 uur. Kleine stukken kun je in de magnetron ontdooien, maar bereid ze dan meteen.</p>

<h2>Kip altijd helemaal gaar</h2>
<p>Bij gevogelte kunnen bacteriën door het hele vlees zitten, dus kip mag nooit roze zijn. Controleer dat de kip door en door heet is, dat het vlees op het dikste punt niet meer roze is en dat het vocht helder is. Met een thermometer: de kern moet 2 minuten 70 °C halen.</p>

<h2>Bereide kip en restjes</h2>
<p>Laat bereide kip snel afkoelen en zet hem afgesloten in de koelkast; laat restjes nooit langer dan 2 uur buiten de koelkast staan. Bereide kip blijft 2 dagen goed in de koelkast, of zo'n 3 maanden in de vriezer. Je kunt hem koud eten of één keer door en door opwarmen.</p>

<h2>Hoe herken je bedorven kip?</h2>
<p>Het Voedingscentrum noemt deze signalen: een afwijkende geur, een grauwe verkleuring, of kip die uitgedroogd of plakkerig is. Zie je dat, gooi hem dan weg. Maar een normale geur is geen garantie: de bacteriën die je ziek maken ruik je niet. Is de TGT-datum voorbij, dan gaat de kip weg.</p>

<h2>Tips om minder kip te verspillen</h2>
<ul>
  <li>Vries kip op de dag van aankoop in als je hem niet binnen een à twee dagen gebruikt.</li>
  <li>Maak wat extra en gebruik de rest de volgende dag in een wrap, salade of soep.</li>
  <li>Zet de TGT-datum in FreshGarant, dan krijg je op tijd een seintje.</li>
</ul>
""",
  "faq": [
   ("Kun je kip een dag na de TGT-datum nog eten?", "Nee. De TGT-datum op kip gaat over veiligheid. Eet hem daarna niet meer, ook als hij er goed uitziet en ruikt."),
   ("Hoe lang is bereide kip houdbaar in de koelkast?", "2 dagen, volgens het Voedingscentrum. Zet hem snel na het afkoelen afgesloten in de koelkast."),
   ("Moet je rauwe kip wassen?", "Nee. Wassen verspreidt campylobacter door je keuken. Goed garen doodt de bacteriën."),
   ("Mag je ontdooide kip opnieuw invriezen?", "Rauw niet. Bereid hem eerst; het gerecht kun je daarna invriezen en één keer opwarmen."),
   ("Hoe weet ik dat kip gaar is?", "Hij is door en door heet, het vlees is op het dikste punt niet meer roze en het vocht is helder."),
  ],
  "related": ["mince", "leftovers", "fish"],
 },
},
# ─────────────────────────────── MILK ───────────────────────────────
{
 "key": "milk", "emoji": "🥛",
 "sources": ["vc_bewaarwijzer", "fsa_facts", "fsa_chill"],
 "en": {
  "slug": "how-long-does-milk-last", "name": "Milk",
  "title": "How Long Does Milk Last After Opening?",
  "desc": "Opened milk keeps about 1 week in the fridge and about 2 months in the freezer. Best before or use by, how to store milk and how to tell if it's off.",
  "h1": "How long does milk last after opening?",
  "answer": "Once opened, milk keeps <strong>about 1 week in the fridge</strong> at 4°C, according to the Voedingscentrum. An unopened carton follows the date on the pack. Milk can be frozen for about 2 months. Check the label first: milk with a <em>best before</em> date can still be fine after it, milk with a <em>use by</em> date cannot.",
  "table_head": ("", "How long", "Source"),
  "table": [
   ("Unopened", "Until the date on the pack", "Label"),
   ("Opened, fridge", "About 1 week", "Voedingscentrum"),
   ("Freezer", "About 2 months", "Voedingscentrum"),
   ("Past a best-before date", "Often still fine: look, smell and taste", "Voedingscentrum · FSA"),
   ("Past a use-by date", "Do not drink it", "FSA"),
  ],
  "body": """
<h2>Best before or use by? Check your carton</h2>
<p>Milk can carry either date, depending on how it is made. That matters, because the two dates mean very different things:</p>
<ul>
  <li><strong>Best before</strong> is about quality. The FSA says food with a best-before date can be eaten after the date, and you can use your senses to check it. The Voedingscentrum likewise says not to throw milk away straight after the best-before date: look, smell and taste a little.</li>
  <li><strong>Use by</strong> is about safety. The FSA warns that a sniff test is not safe for any food with a use-by date, because you cannot smell the bacteria that cause food poisoning.</li>
</ul>
<p>In the Netherlands most fresh milk carries a best-before date (THT). In the UK, both are common, so always look at which one your carton has.</p>

<h2>How long does opened milk last?</h2>
<p>The Voedingscentrum gives about 1 week in the fridge for opened semi-skimmed milk. Many cartons also say "once opened, use within x days": follow that instruction when it is on the pack. Long-life (UHT) milk can be kept in the cupboard until opened; after opening it belongs in the fridge as well.</p>

<h2>How to store milk</h2>
<ul>
  <li><strong>Back in the fridge straight away.</strong> The Voedingscentrum advises putting milk back quickly after use, at 4°C. That keeps it good for longer.</li>
  <li><strong>Not in the door if you can avoid it.</strong> The door is the warmest part of the fridge and warms up every time you open it.</li>
  <li><strong>Close the carton.</strong> Milk takes on smells from other food.</li>
</ul>

<h2>Can you freeze milk?</h2>
<p>Yes. The Voedingscentrum gives about 2 months in the freezer. Leave some room in the bottle or carton, because milk expands when it freezes. Defrost it in the fridge and shake well: the fat can separate, which is harmless. Defrosted milk is best for cooking, baking or smoothies.</p>

<h2>How to tell if milk has gone off</h2>
<p>The Voedingscentrum names these signs: milk that smells or tastes sour, or has lumps. If you see or smell any of these, pour it away. For milk with a best-before date, this check is exactly how you decide whether it is still good after the date. For milk with a use-by date, the date decides, not your nose.</p>

<h2>Tips to waste less milk</h2>
<ul>
  <li>Buy the size you actually use in a week.</li>
  <li>Milk that is nearly finished can go into pancakes, porridge, a white sauce or a smoothie.</li>
  <li>Freeze part of a large bottle if you will not finish it in time.</li>
  <li>Log it in FreshGarant with the date you opened it, so you know when to finish it.</li>
</ul>
""",
  "faq": [
   ("Can you drink milk after the best-before date?", "Often yes. Best before is about quality. Look, smell and taste a little: if it is not sour or lumpy, it is fine."),
   ("Can you drink milk after the use-by date?", "No. A use-by date is about safety, and you cannot smell the bacteria that cause food poisoning."),
   ("How long does opened milk last?", "About 1 week in the fridge at 4°C, according to the Voedingscentrum, unless the carton says otherwise."),
   ("Can you freeze milk?", "Yes, for about 2 months. Defrost it in the fridge and shake well before using."),
   ("Why does my milk go off before the date?", "The date only applies to an unopened pack stored cold. Once opened, or if it is left out or kept in a warm fridge door, it spoils sooner."),
  ],
  "related": ["yoghurt", "cream", "cheese"],
 },
 "nl": {
  "slug": "hoe-lang-is-melk-houdbaar", "name": "Melk",
  "title": "Hoe Lang Is Melk Houdbaar na Openen?",
  "desc": "Geopende melk blijft zo'n week goed in de koelkast en 2 maanden in de vriezer. Na de THT-datum? Kijk, ruik en proef. Zo bewaar je melk het best.",
  "h1": "Hoe lang is melk houdbaar na openen?",
  "answer": "Geopende melk blijft volgens het Voedingscentrum <strong>ongeveer 1 week goed in de koelkast</strong> bij 4 °C. Een gesloten pak houdt zich aan de datum op de verpakking. In de vriezer blijft melk zo'n 2 maanden goed. En na de THT-datum hoef je melk niet meteen weg te gooien: kijk, ruik en proef.",
  "table_head": ("", "Hoe lang", "Bron"),
  "table": [
   ("Gesloten pak", "Tot de datum op de verpakking", "Etiket"),
   ("Geopend, koelkast", "Ongeveer 1 week", "Voedingscentrum"),
   ("Vriezer", "Ongeveer 2 maanden", "Voedingscentrum"),
   ("Na de THT-datum", "Vaak nog goed: kijk, ruik en proef", "Voedingscentrum"),
   ("Na een TGT-datum", "Niet meer drinken", "FSA"),
  ],
  "body": """
<h2>THT of TGT? Kijk op het pak</h2>
<p>Op verse melk in Nederland staat meestal een THT-datum: ten minste houdbaar tot. Die gaat over kwaliteit. Het Voedingscentrum zegt daarom: gooi melk niet direct weg na de THT-datum, maar kijk, ruik en proef een beetje om de kwaliteit te beoordelen.</p>
<p>Staat er een TGT-datum (te gebruiken tot), dan gaat het om veiligheid. De Britse Food Standards Agency (FSA) waarschuwt dat je bij producten met zo'n datum niet op je neus kunt vertrouwen: de bacteriën die voedselvergiftiging veroorzaken ruik je niet.</p>

<h2>Hoe lang is geopende melk goed?</h2>
<p>Het Voedingscentrum houdt voor geopende halfvolle melk ongeveer 1 week in de koelkast aan. Staat er op het pak "na openen binnen x dagen gebruiken", volg dan dat advies. Houdbare melk (UHT) kun je tot het openen in de kast bewaren; daarna hoort ook die in de koelkast.</p>

<h2>Zo bewaar je melk</h2>
<ul>
  <li><strong>Direct terug in de koelkast.</strong> Volgens het Voedingscentrum blijft melk langer goed als je hem na gebruik snel terugzet, bij 4 °C.</li>
  <li><strong>Liever niet in de deur.</strong> De deur is de warmste plek van de koelkast en warmt op bij elke keer openen.</li>
  <li><strong>Pak goed sluiten.</strong> Melk neemt geuren van ander eten over.</li>
</ul>

<h2>Kun je melk invriezen?</h2>
<p>Ja. Volgens het Voedingscentrum blijft melk zo'n 2 maanden goed in de vriezer. Laat wat ruimte in de fles of het pak, want melk zet uit als hij bevriest. Ontdooi hem in de koelkast en schud goed: het vet kan zich afscheiden, maar dat is onschuldig. Ontdooide melk is het fijnst om mee te koken of bakken.</p>

<h2>Hoe herken je bedorven melk?</h2>
<p>Het Voedingscentrum noemt deze signalen: de melk ruikt of smaakt zuur, of klontert. Merk je dat, giet hem dan weg. Bij melk met een THT-datum is dit precies hoe je beoordeelt of hij na de datum nog goed is. Bij een TGT-datum beslist de datum, niet je neus.</p>

<h2>Tips om minder melk te verspillen</h2>
<ul>
  <li>Koop het formaat dat je in een week echt opmaakt.</li>
  <li>Melk die bijna op moet, kan in pannenkoeken, pap, een witte saus of een smoothie.</li>
  <li>Vries een deel van een grote fles in als je hem niet op tijd opkrijgt.</li>
  <li>Zet in FreshGarant de datum waarop je het pak opende, dan weet je wanneer het op moet.</li>
</ul>
""",
  "faq": [
   ("Kun je melk na de THT-datum nog drinken?", "Vaak wel. THT gaat over kwaliteit. Kijk, ruik en proef een beetje: is hij niet zuur of klonterig, dan is hij goed."),
   ("Hoe lang is geopende melk houdbaar?", "Ongeveer 1 week in de koelkast bij 4 °C, volgens het Voedingscentrum, tenzij het pak iets anders zegt."),
   ("Kun je melk invriezen?", "Ja, zo'n 2 maanden. Ontdooi hem in de koelkast en schud goed voor gebruik."),
   ("Waarom is mijn melk al zuur vóór de datum?", "De datum geldt alleen voor een gesloten pak dat koel is bewaard. Na openen, of als hij buiten of in een warme koelkastdeur staat, bederft hij sneller."),
   ("Is houdbare melk na openen ook lang goed?", "Nee. Houdbare melk kan tot het openen in de kast, maar na openen hoort hij in de koelkast en bederft hij net als verse melk."),
  ],
  "related": ["yoghurt", "cream", "cheese"],
 },
},
# ─────────────────────────────── YOGHURT ───────────────────────────────
{
 "key": "yoghurt", "emoji": "🥣",
 "sources": ["vc_bewaarwijzer", "fsa_facts"],
 "en": {
  "slug": "how-long-does-yoghurt-last", "name": "Yoghurt",
  "title": "How Long Does Yoghurt Last After Opening?",
  "desc": "Opened yoghurt keeps 5–7 days in the fridge. Can you eat it past the date, can you freeze it, and how to tell when yoghurt has gone off.",
  "h1": "How long does yoghurt last after opening?",
  "answer": "Opened yoghurt keeps <strong>5 to 7 days in the fridge</strong>, according to the Voedingscentrum. An unopened pot follows the date on the pack. Yoghurt with a best-before date is often still fine afterwards: look, smell and taste. Freezing is possible, but the texture changes.",
  "table_head": ("", "How long", "Source"),
  "table": [
   ("Unopened", "Until the date on the pack", "Label"),
   ("Opened, fridge", "5–7 days", "Voedingscentrum"),
   ("Freezer", "Less suitable: texture changes", "Voedingscentrum"),
   ("Past a best-before date", "Often still fine: look, smell and taste", "Voedingscentrum · FSA"),
   ("Past a use-by date", "Do not eat it", "FSA"),
  ],
  "body": """
<h2>Best before or use by?</h2>
<p>Like milk, yoghurt can carry either a best-before or a use-by date; the FSA notes that the manufacturer decides which one. A best-before date is about quality, so yoghurt is often fine for a while after it. The Voedingscentrum advises not to throw yoghurt away straight after that date, but to look, smell and taste a little first. A use-by date is about safety: then the date decides, because a sniff test cannot detect the bacteria that cause food poisoning.</p>

<h2>How long does opened yoghurt last?</h2>
<p>The Voedingscentrum gives 5 to 7 days in the fridge for opened yoghurt. If the pot says "once opened, eat within x days", follow that. Big tubs last as long as you keep them clean and cold, which brings us to the two most important habits.</p>

<h2>How to store yoghurt</h2>
<ul>
  <li><strong>Always use a clean spoon.</strong> The Voedingscentrum points out that a clean spoon prevents contamination with yeasts and moulds. Never eat straight from the tub and put it back.</li>
  <li><strong>Straight back into the fridge.</strong> Put yoghurt back quickly after use, at 4°C, so it stays good for longer.</li>
  <li><strong>Close the lid.</strong> Or cover the pot, so it does not dry out or take on smells.</li>
</ul>

<h2>Can you freeze yoghurt?</h2>
<p>You can, but the Voedingscentrum calls yoghurt less suitable for freezing because the structure changes: it can turn grainy or watery once defrosted. It is still fine to use in smoothies, sauces, curries or baking. Freeze small portions, for example in an ice cube tray, so you can take out exactly what you need.</p>

<h2>How to tell if yoghurt has gone off</h2>
<p>The Voedingscentrum lists these signs: lumps, yoghurt that turns watery, smells sour or tastes bitter. Note that yoghurt is naturally a little sour, so it is about a sour smell that is clearly off. A thin layer of liquid on top (whey) on its own is normal: stir it back in. Any mould means the whole pot goes in the bin. The FSA advises not eating food with visible mould, because removing the mouldy part does not guarantee that unseen toxins are gone.</p>

<h2>Tips to waste less yoghurt</h2>
<ul>
  <li>Finish an open tub first before opening a new one.</li>
  <li>Use yoghurt that needs to go in a marinade, dressing, curry, cake or smoothie.</li>
  <li>Log the opening date in FreshGarant, so you know when the 5–7 days are up.</li>
</ul>
""",
  "faq": [
   ("Can you eat yoghurt after the best-before date?", "Often yes. Look, smell and taste a little first. If it is not lumpy, bitter or clearly sour, it is fine."),
   ("How long does opened yoghurt last?", "5 to 7 days in the fridge, according to the Voedingscentrum, unless the pot says otherwise."),
   ("Is the liquid on top of yoghurt bad?", "No, that is whey and it is normal. Stir it back in. Watery yoghurt combined with lumps or an off smell is a different story."),
   ("Can you freeze yoghurt?", "Yes, but the texture changes. Use defrosted yoghurt in smoothies, sauces or baking."),
   ("Can you scrape mould off yoghurt?", "No. Throw the whole pot away. Removing the mouldy part does not guarantee that hidden toxins are gone."),
  ],
  "related": ["milk", "cream", "cheese"],
 },
 "nl": {
  "slug": "hoe-lang-is-yoghurt-houdbaar", "name": "Yoghurt",
  "title": "Hoe Lang Is Yoghurt Houdbaar na Openen?",
  "desc": "Geopende yoghurt blijft 5 tot 7 dagen goed in de koelkast. Kun je hem na de THT-datum eten, invriezen, en hoe herken je bedorven yoghurt?",
  "h1": "Hoe lang is yoghurt houdbaar na openen?",
  "answer": "Geopende yoghurt blijft volgens het Voedingscentrum <strong>5 tot 7 dagen goed in de koelkast</strong>. Een gesloten pak houdt zich aan de datum op de verpakking. Na de THT-datum is yoghurt vaak nog prima: kijk, ruik en proef. Invriezen kan, maar de structuur verandert.",
  "table_head": ("", "Hoe lang", "Bron"),
  "table": [
   ("Gesloten pak", "Tot de datum op de verpakking", "Etiket"),
   ("Geopend, koelkast", "5–7 dagen", "Voedingscentrum"),
   ("Vriezer", "Minder geschikt: de structuur verandert", "Voedingscentrum"),
   ("Na de THT-datum", "Vaak nog goed: kijk, ruik en proef", "Voedingscentrum"),
  ],
  "body": """
<h2>Na de THT-datum nog goed?</h2>
<p>Op yoghurt staat meestal een THT-datum: ten minste houdbaar tot. Die gaat over kwaliteit, niet over veiligheid. Het Voedingscentrum adviseert yoghurt daarom niet direct weg te gooien na de datum, maar eerst te kijken, ruiken en een beetje te proeven. Staat er een TGT-datum (te gebruiken tot), dan beslist de datum: bacteriën die je ziek maken kun je niet ruiken.</p>

<h2>Hoe lang is geopende yoghurt goed?</h2>
<p>Het Voedingscentrum houdt voor geopende yoghurt 5 tot 7 dagen in de koelkast aan. Staat er op het pak "na openen binnen x dagen gebruiken", volg dan dat advies. Een groot pak blijft net zo lang goed als je het schoon en koud houdt, en daar gaan de twee belangrijkste gewoontes over.</p>

<h2>Zo bewaar je yoghurt</h2>
<ul>
  <li><strong>Altijd een schone lepel.</strong> Volgens het Voedingscentrum voorkomt een schone lepel besmetting met gisten en schimmels. Eet dus niet uit het pak en zet het daarna terug.</li>
  <li><strong>Direct terug in de koelkast.</strong> Zet yoghurt na gebruik snel terug, bij 4 °C. Dan blijft hij langer goed.</li>
  <li><strong>Goed afsluiten.</strong> Dan droogt hij niet uit en neemt hij geen geuren over.</li>
</ul>

<h2>Kun je yoghurt invriezen?</h2>
<p>Het kan, maar het Voedingscentrum noemt yoghurt minder geschikt om in te vriezen, omdat de structuur verandert: na het ontdooien kan hij korrelig of waterig worden. Je kunt hem dan nog prima gebruiken in smoothies, sauzen, curry's of gebak. Vries kleine porties in, bijvoorbeeld in een ijsblokjesbakje.</p>

<h2>Hoe herken je bedorven yoghurt?</h2>
<p>Het Voedingscentrum noemt deze signalen: brokken, yoghurt die waterig wordt, zuur ruikt of bitter smaakt. Yoghurt is van nature een beetje zuur, dus het gaat om een duidelijk afwijkende zure lucht. Alleen een laagje vocht bovenop (wei) is normaal: roer het er gewoon doorheen. Zie je schimmel, gooi dan het hele pak weg. Volgens de Britse FSA garandeert wegschrapen niet dat onzichtbare gifstoffen weg zijn.</p>

<h2>Tips om minder yoghurt te verspillen</h2>
<ul>
  <li>Maak een open pak eerst op voordat je een nieuw pak opent.</li>
  <li>Yoghurt die op moet, kan in een marinade, dressing, curry, cake of smoothie.</li>
  <li>Zet de openingsdatum in FreshGarant, dan weet je wanneer de 5 tot 7 dagen voorbij zijn.</li>
</ul>
""",
  "faq": [
   ("Kun je yoghurt na de THT-datum nog eten?", "Vaak wel. Kijk, ruik en proef eerst een beetje. Is hij niet brokkelig, bitter of duidelijk zuur, dan is hij goed."),
   ("Hoe lang is geopende yoghurt houdbaar?", "5 tot 7 dagen in de koelkast, volgens het Voedingscentrum, tenzij het pak iets anders zegt."),
   ("Is het vocht bovenop yoghurt slecht?", "Nee, dat is wei en dat is normaal. Roer het erdoor. Waterige yoghurt mét brokken of een vieze lucht is iets anders."),
   ("Kun je yoghurt invriezen?", "Ja, maar de structuur verandert. Gebruik ontdooide yoghurt in smoothies, sauzen of gebak."),
   ("Kun je schimmel van yoghurt afscheppen?", "Nee. Gooi het hele pak weg; wegscheppen garandeert niet dat onzichtbare gifstoffen weg zijn."),
  ],
  "related": ["milk", "cream", "cheese"],
 },
},
# ─────────────────────────────── CHEESE ───────────────────────────────
{
 "key": "cheese", "emoji": "🧀",
 "sources": ["vc_bewaarwijzer", "fsa_facts"],
 "en": {
  "slug": "how-long-does-cheese-last", "name": "Cheese",
  "title": "How Long Does Cheese Last in the Fridge?",
  "desc": "Opened hard cheese keeps about 1 week, slices 4 days and grated cheese 2 days in the fridge. Freezing, mould and storage tips for cheese.",
  "h1": "How long does cheese last in the fridge?",
  "answer": "A piece of opened hard cheese, such as Gouda, keeps <strong>about 1 week in the fridge</strong>, according to the Voedingscentrum. Sliced cheese keeps 4 days and grated cheese 2 days. Hard cheese can be frozen for 2 to 4 months. Mould on hard cheese can be cut away generously; on soft or grated cheese it cannot.",
  "table_head": ("", "How long", "Source"),
  "table": [
   ("Hard cheese, piece (opened)", "About 1 week", "Voedingscentrum"),
   ("Sliced cheese (opened)", "4 days", "Voedingscentrum"),
   ("Grated cheese (opened)", "2 days", "Voedingscentrum"),
   ("Hard cheese, freezer", "2–4 months", "Voedingscentrum"),
   ("Hard cheese past best before", "Up to 2 months and possibly longer, if it looks fine and the pack is intact", "Voedingscentrum"),
  ],
  "body": """
<h2>Hard cheese keeps well</h2>
<p>Hard cheeses such as Gouda, Edam or mature cheddar contain little moisture, so they spoil slowly. The Voedingscentrum's storage guide gives about 1 week in the fridge for an opened piece of young-matured Gouda, and says unopened hard cheese can often be eaten up to 2 months after its best-before date, and possibly longer, as long as it still looks fine and the packaging is intact.</p>
<p>Slices and grated cheese have a much bigger surface and dry out or spoil faster: 4 days for slices and 2 days for grated cheese once opened.</p>

<h2>How to store cheese</h2>
<ul>
  <li><strong>In the fridge, in a closed wrap.</strong> The Voedingscentrum recommends cheese paper or (reusable) cling film, which stops the cheese from sweating.</li>
  <li><strong>Keep it covered.</strong> Exposed cheese dries out and picks up smells from other food.</li>
  <li><strong>Close sliced and grated packs properly</strong> after each use.</li>
</ul>

<h2>What to do with mould on cheese</h2>
<p>It depends on the cheese. For <strong>hard cheese</strong> such as Gouda or Edam, the Voedingscentrum says you can cut away mould generously, at least 1 centimetre around it, and eat the rest. That only applies to hard cheese. For soft cheese, cream cheese, sliced or grated cheese, mould can spread further than you can see: throw it away. The FSA adds that removing mould is never a full guarantee that unseen toxins are gone, which matters most for children, pregnant people, older people and anyone with a weakened immune system.</p>

<h2>Can you freeze cheese?</h2>
<p>Yes. The Voedingscentrum gives 2 to 4 months in the freezer for hard cheese. Freezing changes the texture: the cheese turns more crumbly, so frozen cheese is best for cooking, sauces, gratins or toasties. Grating cheese before you freeze it makes it easy to use straight from the freezer.</p>

<h2>How to tell if cheese has gone off</h2>
<p>For hard cheese, the Voedingscentrum names these signs: the cheese has dried out, has mould, or smells strange. A dried-out edge can be cut off; mould on hard cheese can be cut away generously, as above. Cheese that smells clearly off, or soft cheese with mould, goes in the bin.</p>

<h2>Tips to waste less cheese</h2>
<ul>
  <li>Buy a piece instead of slices if you do not eat cheese every day: it keeps longer.</li>
  <li>Grate leftover ends and freeze them for pasta, soup or a gratin.</li>
  <li>Log opened packs in FreshGarant, so sliced and grated cheese do not get forgotten.</li>
</ul>
""",
  "faq": [
   ("Can you eat cheese after the best-before date?", "Hard cheese often yes: up to 2 months and possibly longer if it still looks fine and the pack is intact. Look, smell and taste."),
   ("Can you cut mould off cheese?", "Only off hard cheese such as Gouda or Edam: cut at least 1 cm around it. Soft, sliced or grated cheese with mould goes in the bin."),
   ("How long do cheese slices last once opened?", "4 days in the fridge, according to the Voedingscentrum. Grated cheese keeps 2 days."),
   ("Can you freeze cheese?", "Yes, hard cheese for 2 to 4 months. It gets more crumbly, so use it for cooking."),
   ("Why does cheese sweat in the fridge?", "In airtight plastic, moisture gets trapped. Cheese paper or reusable wrap helps prevent this."),
  ],
  "related": ["milk", "yoghurt", "ham"],
 },
 "nl": {
  "slug": "hoe-lang-is-kaas-houdbaar", "name": "Kaas",
  "title": "Hoe Lang Is Kaas Houdbaar in de Koelkast?",
  "desc": "Een stuk geopende harde kaas blijft zo'n week goed, plakken 4 dagen en geraspte kaas 2 dagen. Over invriezen, schimmel en kaas goed bewaren.",
  "h1": "Hoe lang is kaas houdbaar in de koelkast?",
  "answer": "Een geopend stuk harde kaas, zoals Goudse, blijft volgens het Voedingscentrum <strong>ongeveer 1 week goed in de koelkast</strong>. Plakken kaas houd je 4 dagen en geraspte kaas 2 dagen. Harde kaas kun je 2 tot 4 maanden invriezen. Schimmel op harde kaas mag je ruim wegsnijden; bij zachte of geraspte kaas niet.",
  "table_head": ("", "Hoe lang", "Bron"),
  "table": [
   ("Harde kaas, stuk (geopend)", "Ongeveer 1 week", "Voedingscentrum"),
   ("Plakken kaas (geopend)", "4 dagen", "Voedingscentrum"),
   ("Geraspte kaas (geopend)", "2 dagen", "Voedingscentrum"),
   ("Harde kaas, vriezer", "2–4 maanden", "Voedingscentrum"),
   ("Harde kaas na de THT-datum", "Tot 2 maanden en mogelijk langer, als hij er goed uitziet en de verpakking heel is", "Voedingscentrum"),
  ],
  "body": """
<h2>Harde kaas blijft lang goed</h2>
<p>Harde kazen zoals Goudse, Edammer of oude kaas bevatten weinig vocht en bederven daardoor langzaam. Het Voedingscentrum houdt voor een geopend stuk jong belegen Goudse ongeveer 1 week in de koelkast aan. Ongeopende harde kaas kun je volgens de Bewaarwijzer vaak nog tot 2 maanden na de THT-datum eten, en mogelijk langer, zolang hij er goed uitziet en de verpakking heel is.</p>
<p>Plakken en geraspte kaas hebben een veel groter oppervlak en drogen sneller uit of bederven sneller: na openen 4 dagen voor plakken en 2 dagen voor geraspte kaas.</p>

<h2>Zo bewaar je kaas</h2>
<ul>
  <li><strong>In de koelkast, goed verpakt.</strong> Het Voedingscentrum raadt kaaspapier of (herbruikbaar) vershoudfolie aan; dat voorkomt dat de kaas gaat zweten.</li>
  <li><strong>Altijd afgedekt.</strong> Onverpakte kaas droogt uit en neemt geuren over.</li>
  <li><strong>Sluit pakjes plakken en geraspte kaas</strong> na elk gebruik goed af.</li>
</ul>

<h2>Schimmel op kaas: wat nu?</h2>
<p>Dat hangt af van de kaas. Bij <strong>harde kaas</strong> zoals Goudse of Edammer kun je schimmel volgens het Voedingscentrum ruim wegsnijden, minstens 1 centimeter eromheen, en de rest gewoon eten. Dat geldt alleen voor harde kaas. Bij zachte kaas, roomkaas, plakken of geraspte kaas kan schimmel verder zitten dan je ziet: gooi die weg. De Britse FSA voegt toe dat wegsnijden nooit helemaal garandeert dat onzichtbare gifstoffen weg zijn, wat vooral telt voor kinderen, zwangeren, ouderen en mensen met een verminderde weerstand.</p>

<h2>Kun je kaas invriezen?</h2>
<p>Ja. Het Voedingscentrum houdt voor harde kaas 2 tot 4 maanden in de vriezer aan. De structuur verandert wel: de kaas wordt brokkeliger. Ingevroren kaas is dus het fijnst om mee te koken, voor sauzen, ovenschotels of tosti's. Rasp de kaas vóór het invriezen, dan kun je hem zo uit de vriezer gebruiken.</p>

<h2>Hoe herken je bedorven kaas?</h2>
<p>Bij harde kaas noemt het Voedingscentrum: de kaas is uitgedroogd, beschimmeld of ruikt vreemd. Een uitgedroogd randje kun je afsnijden en schimmel op harde kaas ruim wegsnijden. Kaas die duidelijk vies ruikt, of zachte kaas met schimmel, gooi je weg.</p>

<h2>Tips om minder kaas te verspillen</h2>
<ul>
  <li>Koop een stuk in plaats van plakken als je niet elke dag kaas eet: een stuk blijft langer goed.</li>
  <li>Rasp kaaskorstjes en restjes en vries ze in voor pasta, soep of een ovenschotel.</li>
  <li>Zet geopende pakjes in FreshGarant, dan vergeet je de plakken en geraspte kaas niet.</li>
</ul>
""",
  "faq": [
   ("Kun je kaas na de THT-datum nog eten?", "Harde kaas vaak wel: tot 2 maanden en mogelijk langer, als hij er goed uitziet en de verpakking heel is. Kijk, ruik en proef."),
   ("Mag je schimmel van kaas afsnijden?", "Alleen bij harde kaas zoals Goudse of Edammer: snijd minstens 1 cm eromheen weg. Zachte kaas, plakken of geraspte kaas met schimmel gooi je weg."),
   ("Hoe lang zijn plakken kaas houdbaar na openen?", "4 dagen in de koelkast, volgens het Voedingscentrum. Geraspte kaas 2 dagen."),
   ("Kun je kaas invriezen?", "Ja, harde kaas 2 tot 4 maanden. Hij wordt brokkeliger, dus gebruik hem om mee te koken."),
   ("Waarom gaat kaas zweten in de koelkast?", "In luchtdicht plastic blijft vocht hangen. Kaaspapier of herbruikbaar folie helpt dat te voorkomen."),
  ],
  "related": ["milk", "yoghurt", "ham"],
 },
},
# ─────────────────────────────── EGGS ───────────────────────────────
{
 "key": "eggs", "emoji": "🥚",
 "sources": ["vc_bewaarwijzer", "fsa_facts"],
 "en": {
  "slug": "how-long-do-eggs-last", "name": "Eggs",
  "title": "How Long Do Eggs Last? Fridge, Best Before & Boiled",
  "desc": "Raw eggs keep about 4 weeks in the fridge, hard-boiled eggs 1 week in the shell. Eggs after the best-before date, the float test and freezing.",
  "h1": "How long do eggs last in the fridge?",
  "answer": "Raw eggs keep <strong>about 4 weeks in the fridge</strong>, according to the Voedingscentrum. A hard-boiled egg keeps up to a week in its shell, a peeled one 2 days. After the best-before date, eggs are still safe for a couple of days if you cook them thoroughly. You can freeze eggs out of their shell for about 3 months.",
  "table_head": ("", "How long", "Source"),
  "table": [
   ("Raw eggs, fridge", "About 4 weeks; try to eat them before the best-before date", "Voedingscentrum"),
   ("Hard-boiled, in shell", "Up to 1 week", "Voedingscentrum"),
   ("Hard-boiled, peeled", "2 days, in a closed container", "Voedingscentrum"),
   ("Soft-boiled", "No longer than 2 days", "Voedingscentrum"),
   ("Freezer (out of the shell, beaten)", "About 3 months", "Voedingscentrum · FSA"),
   ("Past the best-before date", "A couple of days, only if cooked thoroughly", "FSA · Voedingscentrum"),
  ],
  "body": """
<h2>Where to keep eggs</h2>
<p>The Voedingscentrum advises keeping eggs in their box in the fridge: that stops them drying out. The FSA says eggs should be stored in a cool, dry place, ideally the fridge, away from big temperature changes. Those changes cause condensation on the shell, which lets salmonella get from the outside into the egg more easily.</p>
<ul>
  <li><strong>In the box.</strong> Eggs easily take on smells, so keep them away from strong-smelling food.</li>
  <li><strong>Point down.</strong> Eggs have an air pocket at the blunt end; storing them point down keeps it intact, so they stay good longer.</li>
</ul>

<h2>Eggs after the best-before date</h2>
<p>Eggs have a best-before date, not a use-by date. The Voedingscentrum advises trying to eat them before that date: they are fresher and there is less chance of bacteria growing. The FSA says eggs are safe for a couple of days after the best-before date if they are cooked well, with both white and yolk fully set. So use older eggs for a hard-boiled egg, an omelette or baking, not for a soft-boiled egg or homemade mayonnaise.</p>

<h2>Does the float test work?</h2>
<p>Not for safety. The FSA explains that an egg floats because more air gets inside as it ages. The float test tells you roughly how old an egg is, not whether bacteria have grown inside it. Go by the date and how you store eggs instead.</p>

<h2>How long do boiled eggs last?</h2>
<p>According to the Voedingscentrum, a hard-boiled egg keeps up to a week in the fridge as long as it is still in its shell. Peeled, it keeps 2 days in a closed container. Keep a soft-boiled egg no longer than 2 days, because the yolk is not fully set and bacteria can grow. Cooling boiled eggs in cold water helps them dry out less.</p>

<h2>Can you freeze eggs?</h2>
<p>Yes, but not in their shell. The FSA advises cracking the eggs into a container, sealing it and freezing it. You can separate yolks and whites first, or beat the eggs so they are ready for scrambled eggs or an omelette. The Voedingscentrum gives about 3 months for beaten eggs in the freezer. Label the container. Hard-boiled eggs are less suitable for freezing.</p>

<h2>How to tell if an egg has gone off</h2>
<p>The Voedingscentrum names these signs: the egg has dried out or has an unusual smell. Crack doubtful eggs into a separate bowl first, so one bad egg does not ruin the rest of your dish.</p>

<h2>Tips to waste less eggs</h2>
<ul>
  <li>Use the oldest eggs first, and save them for dishes that are cooked thoroughly.</li>
  <li>Beat leftover eggs and freeze them in portions.</li>
  <li>Log the best-before date in FreshGarant, so you get a reminder in time.</li>
</ul>
""",
  "faq": [
   ("Can you eat eggs after the best-before date?", "For a couple of days, if you cook them thoroughly so white and yolk are fully set (FSA). Avoid soft-boiled or raw use."),
   ("Should eggs be kept in the fridge?", "Yes, ideally. Keep them in their box, away from strong smells and big temperature changes."),
   ("Does the egg float test show if an egg is safe?", "No. It shows roughly how old an egg is, not whether bacteria have grown inside."),
   ("How long do hard-boiled eggs last?", "Up to a week in the fridge in their shell, 2 days once peeled."),
   ("Can you freeze eggs?", "Yes, out of the shell: crack or beat them into a sealed container. They keep about 3 months."),
  ],
  "related": ["milk", "cheese", "leftovers"],
 },
 "nl": {
  "slug": "hoe-lang-zijn-eieren-houdbaar", "name": "Eieren",
  "title": "Hoe Lang Zijn Eieren Houdbaar? Koelkast, THT en Gekookt",
  "desc": "Rauwe eieren blijven zo'n 4 weken goed in de koelkast, hardgekookt 1 week in de schaal. Eieren na de THT-datum, de drijftest en invriezen.",
  "h1": "Hoe lang zijn eieren houdbaar?",
  "answer": "Rauwe eieren blijven volgens het Voedingscentrum <strong>ongeveer 4 weken goed in de koelkast</strong>. Een hardgekookt ei houd je tot een week in de schaal, gepeld 2 dagen. Eet je eieren na de THT-datum, verhit ze dan altijd door en door. Losgeklopt kun je eieren zo'n 3 maanden invriezen.",
  "table_head": ("", "Hoe lang", "Bron"),
  "table": [
   ("Rauwe eieren, koelkast", "Ongeveer 4 weken; liefst vóór de THT-datum opeten", "Voedingscentrum"),
   ("Hardgekookt, in de schaal", "Tot 1 week", "Voedingscentrum"),
   ("Hardgekookt, gepeld", "2 dagen, in een afsluitbaar bakje", "Voedingscentrum"),
   ("Zachtgekookt", "Niet langer dan 2 dagen", "Voedingscentrum"),
   ("Vriezer (losgeklopt)", "Ongeveer 3 maanden", "Voedingscentrum"),
   ("Na de THT-datum", "Alleen door en door verhit", "Voedingscentrum · FSA"),
  ],
  "body": """
<h2>Waar bewaar je eieren?</h2>
<p>Het Voedingscentrum raadt aan eieren in de doos in de koelkast te bewaren: dat voorkomt uitdroging. Ook de Britse Food Standards Agency (FSA) noemt de koelkast de beste plek, uit de buurt van grote temperatuurschommelingen. Die zorgen voor condens op de schaal, waardoor salmonella makkelijker van buiten het ei in kan komen.</p>
<ul>
  <li><strong>In de doos.</strong> Eieren nemen snel geuren over; bewaar ze niet bij sterk ruikende producten.</li>
  <li><strong>Met de punt naar beneden.</strong> Aan de stompe kant zit een luchtkamer. Met de punt omlaag blijft die heel en blijven eieren langer goed.</li>
</ul>

<h2>Eieren na de THT-datum</h2>
<p>Op eieren staat een THT-datum, geen TGT-datum. Het Voedingscentrum adviseert eieren liefst vóór de THT-datum op te eten: ze zijn dan verser en er is minder kans op uitgroei van ziekmakende bacteriën. Eet je ze na de datum, verhit ze dan altijd door en door: hardgekookt of goed doorbakken. Volgens de FSA kun je eieren nog een paar dagen na de datum veilig gebruiken als wit en dooier helemaal gestold zijn. Gebruik oudere eieren dus voor een hardgekookt ei, omelet of gebak, niet voor een zachtgekookt ei of zelfgemaakte mayonaise.</p>

<h2>Werkt de drijftest?</h2>
<p>Niet voor veiligheid. De FSA legt uit dat een ei gaat drijven omdat er met de tijd meer lucht in komt. De drijftest zegt dus iets over de leeftijd van een ei, niet over bacteriën die erin zijn gegroeid. Ga liever af op de datum en op hoe je de eieren bewaart.</p>

<h2>Hoe lang blijven gekookte eieren goed?</h2>
<p>Volgens het Voedingscentrum kun je een hardgekookt ei tot een week in de koelkast bewaren, zolang het nog in de schaal zit. Gepeld blijft het 2 dagen goed in een afsluitbaar bakje. Een zachtgekookt ei bewaar je liever niet langer dan 2 dagen, omdat de dooier niet helemaal gestold is en bacteriën kunnen uitgroeien. Dompel gekookte eieren in koud water, dan drogen ze minder uit.</p>

<h2>Kun je eieren invriezen?</h2>
<p>Ja, maar niet in de schaal. Breek de eieren in een bakje, sluit het af en vries in. Je kunt eiwit en dooier eerst scheiden, of de eieren losgeklopt invriezen, handig voor roerei of omelet. Het Voedingscentrum houdt voor losgeklopte eieren zo'n 3 maanden in de vriezer aan. Hardgekookte eieren zijn minder geschikt om in te vriezen.</p>

<h2>Hoe herken je een bedorven ei?</h2>
<p>Het Voedingscentrum noemt: het ei is uitgedroogd en heeft een afwijkende geur. Breek twijfelgevallen eerst apart in een kommetje, dan bederft één slecht ei niet je hele gerecht.</p>

<h2>Tips om minder eieren te verspillen</h2>
<ul>
  <li>Gebruik de oudste eieren eerst, en dan in gerechten die goed verhit worden.</li>
  <li>Klop eieren die op moeten los en vries ze in porties in.</li>
  <li>Zet de THT-datum in FreshGarant, dan krijg je op tijd een seintje.</li>
</ul>
""",
  "faq": [
   ("Kun je eieren na de THT-datum nog eten?", "Ja, als je ze door en door verhit: hardgekookt of goed doorbakken. Gebruik ze dan niet zachtgekookt of rauw."),
   ("Horen eieren in de koelkast?", "Ja, het liefst in de doos, uit de buurt van sterke geuren en grote temperatuurschommelingen."),
   ("Zegt de drijftest of een ei nog goed is?", "Nee. Hij zegt iets over de leeftijd van het ei, niet over bacteriën."),
   ("Hoe lang is een hardgekookt ei houdbaar?", "Tot een week in de koelkast in de schaal, en 2 dagen als het gepeld is."),
   ("Kun je eieren invriezen?", "Ja, zonder schaal: losgeklopt of gescheiden in een afgesloten bakje. Ze blijven zo'n 3 maanden goed."),
  ],
  "related": ["milk", "cheese", "leftovers"],
 },
},
# ─────────────────────────────── CREAM ───────────────────────────────
{
 "key": "cream", "emoji": "🍰",
 "sources": ["vc_bewaarwijzer", "fsa_facts"],
 "en": {
  "slug": "how-long-does-whipping-cream-last", "name": "Whipping cream",
  "title": "How Long Does Whipping Cream Last After Opening?",
  "desc": "Opened whipping cream keeps 4–6 days in the fridge, whipped cream too. Can you freeze cream, eat it past the date, and how to spot spoiled cream.",
  "h1": "How long does whipping cream last after opening?",
  "answer": "Opened whipping cream keeps <strong>4 to 6 days in the fridge</strong>, according to the Voedingscentrum, and whipped cream as well. An unopened carton follows the date on the pack. Whipped cream can be frozen for about 1 month; liquid cream is less suitable for freezing.",
  "table_head": ("", "How long", "Source"),
  "table": [
   ("Unopened", "Until the date on the pack", "Label"),
   ("Opened, liquid cream, fridge", "4–6 days", "Voedingscentrum"),
   ("Whipped cream, fridge", "4–6 days", "Voedingscentrum"),
   ("Whipped cream, freezer", "About 1 month", "Voedingscentrum"),
   ("Liquid cream, freezer", "Less suitable: texture changes", "Voedingscentrum"),
  ],
  "body": """
<h2>How long is opened cream good?</h2>
<p>The Voedingscentrum gives 4 to 6 days in the fridge for opened whipping cream, and the same for cream you have already whipped. If the carton says "once opened, use within x days", follow that instead. Long-life cream can be kept in the cupboard until opened; after that it belongs in the fridge.</p>

<h2>Past the date?</h2>
<p>Cream with a best-before date does not have to be thrown away the moment the date passes. The Voedingscentrum advises looking, smelling and tasting a little to judge the quality. If your cream carries a use-by date instead, the date decides: the FSA warns that you cannot smell the bacteria that cause food poisoning.</p>

<h2>How to store cream</h2>
<ul>
  <li><strong>Back in the fridge straight away</strong> after use, at 4°C. That keeps it good for longer.</li>
  <li><strong>Use a clean spoon</strong> when you scoop from a tub, to avoid contamination with yeasts and moulds.</li>
  <li><strong>Close the carton or cover the bowl,</strong> so the cream does not take on smells from the fridge.</li>
</ul>

<h2>Can you freeze cream?</h2>
<p>Whipped cream freezes well: the Voedingscentrum gives about 1 month. A practical trick is to pipe or spoon small dollops onto a tray, freeze them and then put them in a bag; they are perfect on hot chocolate or a dessert. Liquid cream is less suitable for freezing because the structure changes. Defrosted liquid cream is still fine in sauces, soups or baking, but it will not whip well any more.</p>

<h2>How to tell if cream has gone off</h2>
<p>The Voedingscentrum names these signs: lumps, cream that turns watery, or a sour smell. Any of these means the cream goes in the bin. Mould on the surface also means throwing the whole carton away.</p>

<h2>Tips to waste less cream</h2>
<ul>
  <li>Bought too much for a dessert? Whip the rest and freeze it in dollops.</li>
  <li>Use leftover cream in a pasta sauce, soup, scrambled eggs or a curry.</li>
  <li>Log the opening date in FreshGarant, so you know when the 4 to 6 days are up.</li>
</ul>
""",
  "faq": [
   ("How long does opened whipping cream last?", "4 to 6 days in the fridge, according to the Voedingscentrum, unless the carton says otherwise."),
   ("How long does whipped cream last in the fridge?", "Also 4 to 6 days, covered, at 4°C."),
   ("Can you freeze whipped cream?", "Yes, for about 1 month. Freeze small dollops on a tray, then put them in a bag."),
   ("Can you freeze liquid cream?", "It is less suitable: the structure changes and it will not whip well. Defrosted, it is still fine for sauces and soups."),
   ("Can you use cream after the best-before date?", "Often yes. Look, smell and taste a little first. Lumps, a watery texture or a sour smell mean it has gone off."),
  ],
  "related": ["milk", "yoghurt", "strawberries"],
 },
 "nl": {
  "slug": "hoe-lang-is-slagroom-houdbaar", "name": "Slagroom",
  "title": "Hoe Lang Is Slagroom Houdbaar na Openen?",
  "desc": "Geopende slagroom blijft 4 tot 6 dagen goed in de koelkast, geklopte slagroom ook. Kun je slagroom invriezen en hoe herken je bedorven slagroom?",
  "h1": "Hoe lang is slagroom houdbaar na openen?",
  "answer": "Geopende slagroom blijft volgens het Voedingscentrum <strong>4 tot 6 dagen goed in de koelkast</strong>, geklopte slagroom ook. Een gesloten pak houdt zich aan de datum op de verpakking. Geklopte slagroom kun je zo'n maand invriezen; ongeklopte slagroom is minder geschikt voor de vriezer.",
  "table_head": ("", "Hoe lang", "Bron"),
  "table": [
   ("Gesloten pak", "Tot de datum op de verpakking", "Etiket"),
   ("Geopend, ongeklopt, koelkast", "4–6 dagen", "Voedingscentrum"),
   ("Geklopt, koelkast", "4–6 dagen", "Voedingscentrum"),
   ("Geklopt, vriezer", "Ongeveer 1 maand", "Voedingscentrum"),
   ("Ongeklopt, vriezer", "Minder geschikt: de structuur verandert", "Voedingscentrum"),
  ],
  "body": """
<h2>Hoe lang is geopende slagroom goed?</h2>
<p>Het Voedingscentrum houdt voor geopende, ongeklopte slagroom 4 tot 6 dagen in de koelkast aan, en voor slagroom die je al hebt geklopt ook. Staat er op het pak "na openen binnen x dagen gebruiken", volg dan dat advies. Houdbare slagroom kan tot het openen in de kast; daarna hoort hij in de koelkast.</p>

<h2>Na de THT-datum?</h2>
<p>Op slagroom staat meestal een THT-datum. Die gaat over kwaliteit, niet over veiligheid. Het Voedingscentrum adviseert slagroom daarom niet direct weg te gooien als de datum voorbij is, maar eerst te kijken, ruiken en een beetje te proeven.</p>

<h2>Zo bewaar je slagroom</h2>
<ul>
  <li><strong>Direct terug in de koelkast</strong> na gebruik, bij 4 °C. Dan blijft hij langer goed.</li>
  <li><strong>Gebruik een schone lepel</strong> als je uit een bakje schept, om besmetting met gisten en schimmels te voorkomen.</li>
  <li><strong>Sluit het pak goed af of dek de kom af,</strong> zodat de slagroom geen geuren overneemt.</li>
</ul>

<h2>Kun je slagroom invriezen?</h2>
<p>Geklopte slagroom wel: het Voedingscentrum houdt zo'n maand aan. Handig: spuit of schep kleine toefjes op een bakplaat, vries ze in en doe ze daarna in een zakje. Perfect op warme chocolademelk of een toetje. Ongeklopte slagroom is minder geschikt om in te vriezen, omdat de structuur verandert. Ontdooid kun je hem nog gebruiken in sauzen, soep of gebak, maar stijf kloppen lukt dan niet meer goed.</p>

<h2>Hoe herken je bedorven slagroom?</h2>
<p>Het Voedingscentrum noemt deze signalen: brokken, slagroom die waterig wordt of zuur ruikt. Merk je een daarvan, gooi hem dan weg. Schimmel op het oppervlak betekent ook: het hele pak weg.</p>

<h2>Tips om minder slagroom te verspillen</h2>
<ul>
  <li>Te veel gekocht voor een toetje? Klop de rest op en vries hem in toefjes in.</li>
  <li>Gebruik overgebleven slagroom in een pastasaus, soep, roerei of curry.</li>
  <li>Zet de openingsdatum in FreshGarant, dan weet je wanneer de 4 tot 6 dagen om zijn.</li>
</ul>
""",
  "faq": [
   ("Hoe lang is geopende slagroom houdbaar?", "4 tot 6 dagen in de koelkast, volgens het Voedingscentrum, tenzij het pak iets anders zegt."),
   ("Hoe lang blijft geklopte slagroom goed?", "Ook 4 tot 6 dagen, afgedekt in de koelkast bij 4 °C."),
   ("Kun je geklopte slagroom invriezen?", "Ja, zo'n maand. Vries kleine toefjes in op een bakplaat en doe ze daarna in een zakje."),
   ("Kun je ongeklopte slagroom invriezen?", "Minder geschikt: de structuur verandert en kloppen lukt slecht. Ontdooid kun je hem nog in sauzen en soep gebruiken."),
   ("Kun je slagroom na de THT-datum nog gebruiken?", "Vaak wel. Kijk, ruik en proef eerst. Brokken, een waterige structuur of een zure lucht betekenen dat hij bedorven is."),
  ],
  "related": ["milk", "yoghurt", "strawberries"],
 },
},
]

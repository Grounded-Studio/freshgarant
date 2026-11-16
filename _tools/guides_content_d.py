"""Storage guides, batch D: fish, ham/cold cuts, strawberries, bananas,
avocado, tomatoes. Fridge times from the Voedingscentrum Bewaarwijzer apply
to an OPENED product; an unopened pack follows the date on the pack."""

GUIDES_D = [
# ─────────────────────────────── FISH ───────────────────────────────
{
 "key": "fish", "emoji": "🐟",
 "sources": ["vc_bewaarwijzer", "vc_verhitten", "vc_ontdooien", "fsa_chill"],
 "en": {
  "slug": "how-long-does-fish-last", "name": "Fish",
  "title": "How Long Does Fresh Fish Last in the Fridge?",
  "desc": "Fresh fish keeps 1 to 2 days in the fridge and is best eaten the same day. Raw salmon 2 days, cod 1 day; cooked fish 2 days. Freezing and defrosting.",
  "h1": "How long does fresh fish last in the fridge?",
  "answer": "Fresh fish keeps <strong>1 to 2 days in the fridge</strong>: the Voedingscentrum gives 2 days for raw salmon and 1 day for raw cod, and advises eating fresh fish preferably on the day you buy it. Never eat it past its use-by date. In the freezer, raw salmon keeps about 3 months and cod about 6 months. Cooked fish keeps 2 days.",
  "table_head": ("", "How long", "Source"),
  "table": [
   ("Raw salmon, fridge", "2 days, never past the use-by date", "Voedingscentrum"),
   ("Raw cod, fridge", "1 day, never past the use-by date", "Voedingscentrum"),
   ("Smoked salmon, fridge (opened)", "2 days", "Voedingscentrum"),
   ("Cooked fish, fridge", "2 days", "Voedingscentrum"),
   ("Raw salmon, freezer", "About 3 months", "Voedingscentrum"),
   ("Raw cod, freezer", "About 6 months", "Voedingscentrum"),
  ],
  "body": """
<h2>Fresh fish: best on the day you buy it</h2>
<p>Fish spoils faster than most meat. The Voedingscentrum advises keeping fresh fish as close to freezing point as possible and eating it preferably on the same day, or the next day at the latest. Its storage guide gives 2 days in the fridge for raw salmon and 1 day for raw cod. Fresh fish has a use-by date: do not eat it after that date, because of the risk of harmful bacteria.</p>

<h2>How to store fresh fish</h2>
<ul>
  <li><strong>In the coldest part of the fridge,</strong> usually the bottom shelf. The FSA advises a fridge between 0 and 5°C; the Voedingscentrum 4°C.</li>
  <li><strong>Wrapped and on ice.</strong> The Voedingscentrum's tip: wrap the fish in (reusable) cling film and cover it with plenty of ice cubes.</li>
  <li><strong>Keep it sealed,</strong> so the smell does not spread and juices do not drip onto other food.</li>
</ul>

<h2>Smoked salmon</h2>
<p>Once opened, smoked salmon keeps 2 days in the fridge, according to the Voedingscentrum. Keep it in the coldest spot, in a sealed container or its original packaging, and never eat it past the use-by date.</p>

<h2>Can you freeze fish?</h2>
<p>Yes. The Voedingscentrum gives about 3 months for raw salmon and about 6 months for raw cod in the freezer. Freeze fish on the day you buy it, well wrapped, and write the date on it. You can freeze food right up until midnight on its use-by date, according to the FSA.</p>
<p>Defrost fish in the fridge, ideally starting the day before. In a hurry? The Voedingscentrum advises the microwave on a low setting for delicate products like fish (about 100 watts), turning it once or twice. Once defrosted, use it within 24 hours.</p>

<h2>Cook fish thoroughly</h2>
<p>The Voedingscentrum advises heating fish, shellfish and crustaceans well, because especially shellfish and crustaceans can carry pathogens. Fish is cooked when the flesh is opaque and flakes easily.</p>

<h2>Cooked fish and leftovers</h2>
<p>Cooked fish keeps 2 days in the fridge and about 3 months in the freezer, according to the Voedingscentrum's figures for cooked cod. Cool it quickly and refrigerate it within 2 hours.</p>

<h2>How to tell if fish has gone off</h2>
<p>The Voedingscentrum names these signs: an unusual smell and taste, and for white fish like cod a dull colour. Do not eat fish that looks strange or smells off. Fresh fish smells mild, of the sea; a strong, sour or ammonia-like smell means it goes in the bin. And past the use-by date, the date decides.</p>

<h2>Tips to waste less fish</h2>
<ul>
  <li>Buy fish on the day you cook it, or freeze it straight away.</li>
  <li>Keep a few frozen fillets in the freezer for quick dinners.</li>
  <li>Log fish in FreshGarant with its use-by date, so it gets cooked in time.</li>
</ul>
""",
  "faq": [
   ("How long does raw salmon last in the fridge?", "2 days, according to the Voedingscentrum, and never past its use-by date. Fresher is better: ideally eat it the day you buy it."),
   ("How long does raw cod last in the fridge?", "1 day, according to the Voedingscentrum."),
   ("How long does smoked salmon last once opened?", "2 days in the fridge, in a sealed container."),
   ("Can you freeze fresh fish?", "Yes: salmon for about 3 months, cod about 6 months. Freeze it on the day you buy it."),
   ("How do you know if fish has gone off?", "An unusual smell or taste, or a dull colour. Fresh fish smells mild; a strong or sour smell means throw it away."),
  ],
  "related": ["chicken", "leftovers", "ham"],
 },
 "nl": {
  "slug": "hoe-lang-is-vis-houdbaar", "name": "Vis",
  "title": "Hoe Lang Is Verse Vis Houdbaar in de Koelkast?",
  "desc": "Verse vis blijft 1 tot 2 dagen goed in de koelkast en eet je het liefst dezelfde dag. Rauwe zalm 2 dagen, kabeljauw 1 dag. Invriezen en ontdooien.",
  "h1": "Hoe lang is verse vis houdbaar in de koelkast?",
  "answer": "Verse vis blijft <strong>1 tot 2 dagen goed in de koelkast</strong>: het Voedingscentrum geeft 2 dagen voor rauwe zalm en 1 dag voor rauwe kabeljauw, en adviseert verse vis het liefst dezelfde dag te eten. Eet hem nooit na de TGT-datum. In de vriezer blijft rauwe zalm zo'n 3 maanden goed en kabeljauw zo'n 6 maanden. Bereide vis houd je 2 dagen.",
  "table_head": ("", "Hoe lang", "Bron"),
  "table": [
   ("Rauwe zalm, koelkast", "2 dagen, nooit na de TGT-datum", "Voedingscentrum"),
   ("Rauwe kabeljauw, koelkast", "1 dag, nooit na de TGT-datum", "Voedingscentrum"),
   ("Gerookte zalm, koelkast (geopend)", "2 dagen", "Voedingscentrum"),
   ("Bereide vis, koelkast", "2 dagen", "Voedingscentrum"),
   ("Rauwe zalm, vriezer", "Ongeveer 3 maanden", "Voedingscentrum"),
   ("Rauwe kabeljauw, vriezer", "Ongeveer 6 maanden", "Voedingscentrum"),
  ],
  "body": """
<h2>Verse vis: het liefst dezelfde dag</h2>
<p>Vis bederft sneller dan de meeste soorten vlees. Het Voedingscentrum adviseert verse vis zo dicht mogelijk bij het vriespunt te bewaren en hem bij voorkeur dezelfde dag nog op te eten, eventueel de volgende dag. De Bewaarwijzer geeft 2 dagen in de koelkast voor rauwe zalm en 1 dag voor rauwe kabeljauw. Op verse vis staat een TGT-datum: eet hem daarna niet meer, vanwege de kans op ziekmakende bacteriën.</p>

<h2>Zo bewaar je verse vis</h2>
<ul>
  <li><strong>Op de koudste plek van de koelkast,</strong> meestal de onderste plank, bij 4 °C.</li>
  <li><strong>Verpakt en op ijs.</strong> De tip van het Voedingscentrum: wikkel de vis in (herbruikbaar) vershoudfolie en bedek hem met heel veel ijsblokjes.</li>
  <li><strong>Goed afgesloten,</strong> zodat de geur zich niet verspreidt en er geen vocht op ander eten lekt.</li>
</ul>

<h2>Gerookte zalm</h2>
<p>Geopende gerookte zalm blijft volgens het Voedingscentrum 2 dagen goed in de koelkast. Bewaar hem op de koudste plek, in een afsluitbaar bakje of de oorspronkelijke verpakking, en eet hem nooit na de TGT-datum.</p>

<h2>Kun je vis invriezen?</h2>
<p>Ja. Het Voedingscentrum houdt voor rauwe zalm zo'n 3 maanden in de vriezer aan en voor rauwe kabeljauw zo'n 6 maanden. Vries vis in op de dag dat je hem koopt, goed verpakt, en zet de datum erop.</p>
<p>Ontdooi vis in de koelkast, het liefst een dag van tevoren. Haast? Het Voedingscentrum raadt voor gevoelige producten zoals vis de magnetron op een laag vermogen aan (zo'n 100 watt), en tussendoor 1 of 2 keer omscheppen of keren. Gebruik ontdooide vis binnen 24 uur.</p>

<h2>Vis goed verhitten</h2>
<p>Het Voedingscentrum adviseert vis en schaal- en schelpdieren goed te verhitten, omdat vooral schaal- en schelpdieren ziekteverwekkers kunnen bevatten. Vis is gaar als het visvlees niet meer glazig is en makkelijk uit elkaar valt.</p>

<h2>Bereide vis en restjes</h2>
<p>Bereide vis blijft 2 dagen goed in de koelkast en zo'n 3 maanden in de vriezer, volgens de cijfers van het Voedingscentrum voor bereide kabeljauw. Laat hem snel afkoelen en zet hem binnen 2 uur in de koelkast.</p>

<h2>Hoe herken je bedorven vis?</h2>
<p>Het Voedingscentrum noemt deze signalen: een afwijkende geur en smaak, en bij witvis zoals kabeljauw een doffe kleur. Eet geen vis die er raar uitziet of vreemd ruikt. Verse vis ruikt mild, naar zee; een sterke, zure of ammoniakachtige lucht betekent weggooien. En na de TGT-datum beslist de datum.</p>

<h2>Tips om minder vis te verspillen</h2>
<ul>
  <li>Koop vis op de dag dat je hem klaarmaakt, of vries hem meteen in.</li>
  <li>Houd een paar diepvriesfilets in de vriezer voor snelle maaltijden.</li>
  <li>Zet vis met de TGT-datum in FreshGarant, dan wordt hij op tijd klaargemaakt.</li>
</ul>
""",
  "faq": [
   ("Hoe lang is rauwe zalm houdbaar in de koelkast?", "2 dagen, volgens het Voedingscentrum, en nooit na de TGT-datum. Het liefst eet je hem dezelfde dag."),
   ("Hoe lang is rauwe kabeljauw houdbaar?", "1 dag in de koelkast, volgens het Voedingscentrum."),
   ("Hoe lang is gerookte zalm houdbaar na openen?", "2 dagen in de koelkast, in een afsluitbaar bakje."),
   ("Kun je verse vis invriezen?", "Ja: zalm zo'n 3 maanden, kabeljauw zo'n 6 maanden. Vries hem in op de dag van aankoop."),
   ("Hoe herken je bedorven vis?", "Een afwijkende geur of smaak, of een doffe kleur. Verse vis ruikt mild; een sterke of zure lucht betekent weggooien."),
  ],
  "related": ["chicken", "leftovers", "ham"],
 },
},
# ─────────────────────────────── HAM / COLD CUTS ───────────────────────────────
{
 "key": "ham", "emoji": "🥓",
 "sources": ["vc_bewaarwijzer", "fsa_facts", "fsa_chill"],
 "en": {
  "slug": "how-long-does-ham-last", "name": "Ham and cold cuts",
  "title": "How Long Does Sliced Ham Last After Opening?",
  "desc": "Opened sliced ham and cold cuts keep 3 to 5 days in the fridge; 2 to 3 days for pregnant and vulnerable people because of listeria. Freezing tips.",
  "h1": "How long does sliced ham last after opening?",
  "answer": "Opened sliced ham and most cold cuts keep <strong>3 to 5 days in the fridge</strong>, according to the Voedingscentrum, and never past the use-by date. For older people, pregnant people, very young children and anyone with a weakened immune system, the advice is 2 to 3 days at most, because of listeria. Cold cuts can be frozen for about 3 months.",
  "table_head": ("", "How long", "Source"),
  "table": [
   ("Sliced ham, opened, fridge", "3–5 days, never past the use-by date", "Voedingscentrum"),
   ("Opened, for vulnerable groups", "2–3 days at most (listeria)", "Voedingscentrum"),
   ("Salami, opened, fridge", "5–7 days", "Voedingscentrum"),
   ("Cold cuts, freezer", "About 3 months", "Voedingscentrum"),
  ],
  "body": """
<h2>Why cold cuts need care: listeria</h2>
<p>Sliced ham, chicken slices, roast beef and other cold cuts are eaten without cooking, so any bacteria on them are not killed. The Voedingscentrum points out that cold cuts are sensitive to the growth of harmful bacteria, which cannot be seen, smelled or tasted. The best known is listeria, which, unlike most bacteria, can still grow slowly in the fridge. The FSA also mentions listeria as an example of bacteria that cold temperatures do not stop completely.</p>

<h2>How long do opened cold cuts last?</h2>
<p>The Voedingscentrum's storage guide gives 3 to 5 days in the fridge for opened ham and most cold cuts, such as chicken slices and sliced meatloaf. Dry-cured sausage like salami keeps a little longer: 5 to 7 days once opened. In all cases, do not eat them after the use-by date.</p>
<p><strong>Extra careful for vulnerable groups.</strong> For older people, pregnant people, very young children and people with a weakened immune system, the Voedingscentrum advises keeping opened cold cuts for no longer than 2 to 3 days, because of listeria.</p>

<h2>How to store cold cuts</h2>
<ul>
  <li><strong>In the coldest spot of the fridge,</strong> at 4°C, which is often the bottom shelf, the Voedingscentrum advises.</li>
  <li><strong>In a sealed container or the original packaging,</strong> so they do not dry out.</li>
  <li><strong>Use clean cutlery,</strong> and put the pack back in the fridge right after breakfast or lunch.</li>
  <li><strong>Write the opening date</strong> on the pack, because the 3–5 days start then.</li>
</ul>

<h2>Can you freeze ham and cold cuts?</h2>
<p>Yes. The Voedingscentrum gives about 3 months in the freezer for ham and most cold cuts. Freeze them in small portions, with baking paper between the slices, so you can take out exactly what you need. Defrost them in the fridge and eat them within a day or two. The texture can become slightly wetter, which makes defrosted ham ideal for toasted sandwiches, quiches or pasta.</p>

<h2>How to tell if ham has gone off</h2>
<p>The Voedingscentrum names these signs: a slightly sour, unusual smell, a grey discolouration, or a sticky, slimy surface. Do not eat cold cuts that look strange or smell off. But remember: listeria cannot be seen or smelled, so if the use-by date has passed, the pack goes in the bin, however it smells.</p>

<h2>Tips to waste less cold cuts</h2>
<ul>
  <li>Buy small packs if you do not eat cold cuts every day.</li>
  <li>Freeze part of a large pack straight away.</li>
  <li>Log the opening date in FreshGarant, so you get a reminder before the 3–5 days are up.</li>
</ul>
""",
  "faq": [
   ("How long does sliced ham last once opened?", "3 to 5 days in the fridge, according to the Voedingscentrum, and never past the use-by date."),
   ("How long can pregnant people keep opened cold cuts?", "2 to 3 days at most, because of listeria. The same applies to older people, very young children and people with a weakened immune system."),
   ("Can you eat ham past the use-by date?", "No. Bacteria like listeria cannot be seen or smelled."),
   ("Can you freeze sliced ham?", "Yes, for about 3 months. Freeze small portions with baking paper between the slices."),
   ("Is slimy ham safe?", "No. A slimy or sticky surface, a sour smell or grey colour means it has gone off."),
  ],
  "related": ["cheese", "bread", "chicken"],
 },
 "nl": {
  "slug": "hoe-lang-zijn-vleeswaren-houdbaar", "name": "Ham en vleeswaren",
  "title": "Hoe Lang Zijn Ham en Vleeswaren Houdbaar na Openen?",
  "desc": "Geopende ham en vleeswaren blijven 3 tot 5 dagen goed in de koelkast; voor zwangeren en kwetsbare groepen 2 tot 3 dagen vanwege listeria.",
  "h1": "Hoe lang zijn ham en vleeswaren houdbaar na openen?",
  "answer": "Geopende ham en de meeste vleeswaren blijven volgens het Voedingscentrum <strong>3 tot 5 dagen goed in de koelkast</strong>, en nooit na de TGT-datum. Voor ouderen, zwangeren, hele jonge kinderen en mensen met een verminderde weerstand is het advies maximaal 2 tot 3 dagen, vanwege de bacterie listeria. Vleeswaren kun je zo'n 3 maanden invriezen.",
  "table_head": ("", "Hoe lang", "Bron"),
  "table": [
   ("Ham, geopend, koelkast", "3–5 dagen, nooit na de TGT-datum", "Voedingscentrum"),
   ("Geopend, voor kwetsbare groepen", "Maximaal 2–3 dagen (listeria)", "Voedingscentrum"),
   ("Salami, geopend, koelkast", "5–7 dagen", "Voedingscentrum"),
   ("Vleeswaren, vriezer", "Ongeveer 3 maanden", "Voedingscentrum"),
  ],
  "body": """
<h2>Waarom vleeswaren extra aandacht nodig hebben: listeria</h2>
<p>Ham, kipfilet, rosbief en andere vleeswaren eet je zonder ze te verhitten, dus bacteriën erop worden niet gedood. Het Voedingscentrum wijst erop dat vleeswaren gevoelig zijn voor uitgroei van ziekmakende bacteriën, die je niet kunt zien, ruiken of proeven. De bekendste is listeria, die anders dan de meeste bacteriën ook in de koelkast langzaam kan doorgroeien. Ook de Britse Food Standards Agency noemt listeria als voorbeeld van een bacterie die door kou niet helemaal stopt.</p>

<h2>Hoe lang zijn geopende vleeswaren goed?</h2>
<p>De Bewaarwijzer van het Voedingscentrum geeft 3 tot 5 dagen in de koelkast voor geopende ham en de meeste vleeswaren, zoals kipfilet en gebraden gehakt. Droge worst zoals salami blijft iets langer goed: 5 tot 7 dagen na openen. Eet vleeswaren in alle gevallen niet na de TGT-datum.</p>
<p><strong>Extra voorzichtig voor kwetsbare groepen.</strong> Voor ouderen, zwangeren, hele jonge kinderen en mensen met een verminderde weerstand adviseert het Voedingscentrum geopende vleeswaren niet langer dan 2 tot 3 dagen te bewaren, vanwege de uitgroei van listeria.</p>

<h2>Zo bewaar je vleeswaren</h2>
<ul>
  <li><strong>Op de koudste plek van de koelkast,</strong> bij 4 °C; dat is vaak de onderste plank, zegt het Voedingscentrum.</li>
  <li><strong>In een afsluitbaar bakje of de plastic verpakking,</strong> zodat ze niet uitdrogen.</li>
  <li><strong>Gebruik schoon bestek</strong> en zet het pakje direct na het ontbijt of de lunch terug.</li>
  <li><strong>Zet de openingsdatum op het pakje,</strong> want de 3 tot 5 dagen beginnen dan.</li>
</ul>

<h2>Kun je ham en vleeswaren invriezen?</h2>
<p>Ja. Het Voedingscentrum houdt voor ham en de meeste vleeswaren zo'n 3 maanden in de vriezer aan. Vries ze in kleine porties in, met bakpapier tussen de plakjes, dan pak je precies wat je nodig hebt. Ontdooi ze in de koelkast en eet ze binnen een à twee dagen op. De structuur kan iets natter worden; ontdooide ham is daardoor ideaal voor tosti's, quiches of pasta.</p>

<h2>Hoe herken je bedorven vleeswaren?</h2>
<p>Het Voedingscentrum noemt deze signalen: een afwijkende, licht zure geur, een grauwe verkleuring of een plakkerig oppervlak. Eet geen vleeswaren die er raar uitzien of niet goed ruiken. Maar onthoud: listeria zie of ruik je niet. Is de TGT-datum voorbij, dan gaat het pakje weg, hoe het ook ruikt.</p>

<h2>Tips om minder vleeswaren te verspillen</h2>
<ul>
  <li>Koop kleine pakjes als je niet elke dag vleeswaren eet.</li>
  <li>Vries een deel van een groot pak meteen in.</li>
  <li>Zet de openingsdatum in FreshGarant, dan krijg je een seintje voordat de 3 tot 5 dagen om zijn.</li>
</ul>
""",
  "faq": [
   ("Hoe lang is geopende ham houdbaar?", "3 tot 5 dagen in de koelkast, volgens het Voedingscentrum, en nooit na de TGT-datum."),
   ("Hoe lang mogen zwangeren geopende vleeswaren bewaren?", "Maximaal 2 tot 3 dagen, vanwege listeria. Dat geldt ook voor ouderen, hele jonge kinderen en mensen met een verminderde weerstand."),
   ("Kun je ham na de TGT-datum nog eten?", "Nee. Bacteriën zoals listeria kun je niet zien of ruiken."),
   ("Kun je vleeswaren invriezen?", "Ja, zo'n 3 maanden. Vries kleine porties in met bakpapier tussen de plakjes."),
   ("Is plakkerige ham nog goed?", "Nee. Een plakkerig of slijmerig oppervlak, een zure geur of grauwe kleur betekent dat hij bedorven is."),
  ],
  "related": ["cheese", "bread", "chicken"],
 },
},
# ─────────────────────────────── STRAWBERRIES ───────────────────────────────
{
 "key": "strawberries", "emoji": "🍓",
 "sources": ["vc_bewaarwijzer", "fsa_facts"],
 "en": {
  "slug": "how-long-do-strawberries-last", "name": "Strawberries",
  "title": "How Long Do Strawberries Last? Fridge and Freezer",
  "desc": "Strawberries keep 1 to 3 days in the fridge and only 1 day in a fruit bowl. Frozen, 8 to 12 months. How to store them and what to do with mould.",
  "h1": "How long do strawberries last?",
  "answer": "Strawberries keep <strong>1 to 3 days in the fridge</strong> and only about 1 day in a fruit bowl, according to the Voedingscentrum. Leave the green tops on, keep them dry, and wash them just before eating. In the freezer they keep 8 to 12 months. Throw away mouldy strawberries and check the ones next to them.",
  "table_head": ("", "How long", "Source"),
  "table": [
   ("Fridge (vegetable drawer)", "1–3 days", "Voedingscentrum"),
   ("Fruit bowl", "About 1 day", "Voedingscentrum"),
   ("Freezer", "8–12 months", "Voedingscentrum"),
  ],
  "body": """
<h2>Strawberries are delicate</h2>
<p>Strawberries are among the most perishable fruits. The Voedingscentrum's storage guide gives just 1 to 3 days in the fridge, and about 1 day in a fruit bowl at room temperature. So if you will not eat them today, put them in the fridge.</p>

<h2>How to keep strawberries fresh for longer</h2>
<ul>
  <li><strong>Leave the green tops on.</strong> According to the Voedingscentrum, strawberries keep longer with their crowns still attached.</li>
  <li><strong>In a closed container in the vegetable drawer.</strong> That is the Voedingscentrum's preferred spot.</li>
  <li><strong>Keep them dry.</strong> Moisture speeds up mould. Put them on kitchen paper to absorb moisture.</li>
  <li><strong>Wash just before eating,</strong> not before storing. The FSA advises washing fruit under running water or in a bowl of fresh water before you eat it.</li>
</ul>

<h2>Mould on strawberries</h2>
<p>A soft or bruised strawberry is not immediately spoiled, says the Voedingscentrum. But throw away strawberries that are mouldy or clearly rotten, and check the strawberries that touched them extra carefully, because mould spreads quickly in a punnet. The FSA advises not eating fruit that contains mould, because cutting away the mouldy part does not guarantee that unseen toxins are gone.</p>

<h2>Can you freeze strawberries?</h2>
<p>Yes, and they keep a long time: 8 to 12 months, according to the Voedingscentrum. Cut off the tops first and cut the strawberries into pieces if you like, then freeze them in a sealed container or freezer bag. Freezing them on a tray first and then bagging them stops them from sticking together. Defrosted strawberries turn soft, so use them in smoothies, sauces, jam, yoghurt or baking rather than whole on a cake.</p>

<h2>Overripe strawberries</h2>
<p>The FSA notes that slightly mushy strawberries and other overripe fruit can be eaten normally, as long as there is no mould. Overripe fruit is great for cooking, baking and smoothies.</p>

<h2>Tips to waste fewer strawberries</h2>
<ul>
  <li>Sort through the punnet when you get home and eat the softest ones first.</li>
  <li>Freeze what you will not finish within two days.</li>
  <li>Log strawberries in FreshGarant, so you get a reminder before they go soft.</li>
</ul>
""",
  "faq": [
   ("How long do strawberries last in the fridge?", "1 to 3 days, according to the Voedingscentrum, in a closed container in the vegetable drawer."),
   ("Should you wash strawberries before storing them?", "No, wash them just before eating. Moisture makes them go mouldy faster."),
   ("Can you eat strawberries if one is mouldy?", "Throw away the mouldy ones and check the strawberries that touched them carefully. The rest can be eaten if they look fine."),
   ("Can you freeze strawberries?", "Yes, for 8 to 12 months. Remove the tops first."),
   ("Are soft strawberries safe?", "Yes, slightly mushy strawberries are fine as long as there is no mould. Use them in smoothies or sauces."),
  ],
  "related": ["bananas", "avocado", "cream"],
 },
 "nl": {
  "slug": "hoe-lang-zijn-aardbeien-houdbaar", "name": "Aardbeien",
  "title": "Hoe Lang Zijn Aardbeien Houdbaar? Koelkast en Vriezer",
  "desc": "Aardbeien blijven 1 tot 3 dagen goed in de koelkast en maar 1 dag op de fruitschaal. Ingevroren 8 tot 12 maanden. Bewaartips en wat te doen met schimmel.",
  "h1": "Hoe lang zijn aardbeien houdbaar?",
  "answer": "Aardbeien blijven volgens het Voedingscentrum <strong>1 tot 3 dagen goed in de koelkast</strong> en maar zo'n dag op de fruitschaal. Laat de kroontjes zitten, houd ze droog en was ze pas vlak voor het eten. In de vriezer blijven ze 8 tot 12 maanden goed. Gooi beschimmelde aardbeien weg en controleer de aardbeien ernaast.",
  "table_head": ("", "Hoe lang", "Bron"),
  "table": [
   ("Koelkast (groentelade)", "1–3 dagen", "Voedingscentrum"),
   ("Fruitschaal", "Ongeveer 1 dag", "Voedingscentrum"),
   ("Vriezer", "8–12 maanden", "Voedingscentrum"),
  ],
  "body": """
<h2>Aardbeien zijn kwetsbaar</h2>
<p>Aardbeien horen bij het snelst bederfelijke fruit. De Bewaarwijzer van het Voedingscentrum geeft maar 1 tot 3 dagen in de koelkast, en zo'n 1 dag op de fruitschaal. Eet je ze niet vandaag, zet ze dan in de koelkast.</p>

<h2>Zo blijven aardbeien langer goed</h2>
<ul>
  <li><strong>Laat de kroontjes zitten.</strong> Volgens het Voedingscentrum blijven aardbeien met kroontje langer goed.</li>
  <li><strong>In een gesloten verpakking in de groentelade.</strong> Dat is de plek die het Voedingscentrum aanraadt.</li>
  <li><strong>Houd ze droog.</strong> Vocht versnelt schimmel. Leg ze eventueel op keukenpapier om vocht op te nemen.</li>
  <li><strong>Was ze pas vlak voor het eten,</strong> niet vóór het bewaren. De Britse Food Standards Agency (FSA) adviseert fruit onder stromend water of in een kom schoon water te wassen voordat je het eet.</li>
</ul>

<h2>Schimmel op aardbeien</h2>
<p>Een zachte of gekneusde aardbei is niet meteen bedorven, zegt het Voedingscentrum. Maar is een aardbei beschimmeld of duidelijk rot, gooi hem dan weg en controleer de aardbeien die ermee in contact lagen extra goed: schimmel verspreidt zich snel in een bakje. De FSA raadt af fruit met schimmel te eten, omdat wegsnijden niet garandeert dat onzichtbare gifstoffen weg zijn.</p>

<h2>Kun je aardbeien invriezen?</h2>
<p>Ja, en dan blijven ze lang goed: 8 tot 12 maanden, volgens het Voedingscentrum. Snijd eerst de kroontjes eraf en snijd de aardbeien eventueel in stukjes. Vries ze in in een afsluitbaar bakje of diepvrieszakje. Vries je ze eerst los op een bakplaat, dan plakken ze niet aan elkaar. Ontdooide aardbeien worden zacht; gebruik ze in smoothies, saus, jam, yoghurt of gebak, niet heel op een taart.</p>

<h2>Overrijpe aardbeien</h2>
<p>Volgens de FSA kun je licht papperige aardbeien en ander overrijp fruit gewoon eten, zolang er geen schimmel op zit. Overrijp fruit is ideaal om mee te koken, bakken of er smoothies van te maken.</p>

<h2>Tips om minder aardbeien te verspillen</h2>
<ul>
  <li>Zoek het bakje thuis even door en eet de zachtste eerst.</li>
  <li>Vries in wat je niet binnen twee dagen opeet.</li>
  <li>Zet aardbeien in FreshGarant, dan krijg je een seintje voordat ze zacht worden.</li>
</ul>
""",
  "faq": [
   ("Hoe lang zijn aardbeien houdbaar in de koelkast?", "1 tot 3 dagen, volgens het Voedingscentrum, in een gesloten verpakking in de groentelade."),
   ("Moet je aardbeien wassen voor het bewaren?", "Nee, was ze pas vlak voor het eten. Door vocht gaan ze sneller schimmelen."),
   ("Kun je aardbeien eten als er één beschimmeld is?", "Gooi de beschimmelde weg en controleer de aardbeien die ermee in contact lagen goed. De rest kun je eten als ze er goed uitzien."),
   ("Kun je aardbeien invriezen?", "Ja, 8 tot 12 maanden. Haal eerst de kroontjes eraf."),
   ("Zijn zachte aardbeien nog goed?", "Ja, licht papperige aardbeien zijn prima zolang er geen schimmel op zit. Gebruik ze in een smoothie of saus."),
  ],
  "related": ["bananas", "avocado", "cream"],
 },
},
# ─────────────────────────────── BANANAS ───────────────────────────────
{
 "key": "bananas", "emoji": "🍌",
 "sources": ["vc_bewaarwijzer", "fsa_facts"],
 "en": {
  "slug": "how-long-do-bananas-last", "name": "Bananas",
  "title": "How Long Do Bananas Last? Storage Tips",
  "desc": "Bananas keep 3 to 7 days in a fruit bowl and 8 to 12 months peeled in the freezer. Keep them out of the fridge and away from other fruit.",
  "h1": "How long do bananas last?",
  "answer": "Bananas keep <strong>3 to 7 days in a fruit bowl</strong>, according to the Voedingscentrum. Keep them out of the fridge, because they do not cope well with cold, and away from other fruit. Peeled and frozen, bananas keep 8 to 12 months. Brown or black skin does not mean a banana has gone off.",
  "table_head": ("", "How long", "Source"),
  "table": [
   ("Fruit bowl", "3–7 days", "Voedingscentrum"),
   ("Fridge", "Not recommended: bananas do not cope well with cold", "Voedingscentrum"),
   ("Freezer (peeled)", "8–12 months", "Voedingscentrum"),
  ],
  "body": """
<h2>Keep bananas out of the fridge</h2>
<p>The Voedingscentrum's advice is clear: bananas do not cope well with cold, so store them outside the fridge. In a fruit bowl they keep 3 to 7 days, depending on how ripe they were when you bought them.</p>

<h2>Bananas and other fruit</h2>
<p>Bananas affect the fruit around them, and the other way round. According to the Voedingscentrum, a lot of other fruit ripens or spoils faster when stored next to bananas, and bananas ripen faster next to apples and pears. Use that to your advantage:</p>
<ul>
  <li><strong>Want them to last?</strong> Keep bananas apart from other fruit.</li>
  <li><strong>Want them to ripen?</strong> Put green bananas next to apples or pears.</li>
  <li><strong>Wrap the stems.</strong> The Voedingscentrum says covering the top of a bunch with (reusable) cling film helps bananas keep longer.</li>
</ul>

<h2>Brown or black bananas</h2>
<p>A black skin does not mean a banana has gone off, says the Voedingscentrum: check the flesh. If it smells normal, you can still use it. The FSA agrees that overripe fruit like brown bananas can be eaten normally, as long as there is no mould. Very ripe bananas are perfect for banana bread, pancakes, porridge or smoothies. Throw a banana away if it is mouldy or rotten.</p>

<h2>Can you freeze bananas?</h2>
<p>Yes, and frozen bananas keep 8 to 12 months, according to the Voedingscentrum. Remove the peel first and cut the banana into pieces if you like, then store it in a sealed container or freezer bag. Frozen banana pieces are great straight from the freezer in smoothies, or blended into instant "ice cream". Freeze bananas when they are ripe or overripe, so they are sweet.</p>

<h2>How to tell if a banana has gone off</h2>
<p>Look past the skin. Signs a banana is no longer good: mould, rotten or leaking flesh, or a fermented, alcohol-like smell. A soft, brown banana with flesh that smells normal is just very ripe.</p>

<h2>Tips to waste fewer bananas</h2>
<ul>
  <li>Buy bananas at different stages of ripeness, so they do not all ripen at once.</li>
  <li>Peel and freeze bananas the moment they get too ripe to eat.</li>
  <li>Log bananas in FreshGarant, so you remember to bake or freeze them in time.</li>
</ul>
""",
  "faq": [
   ("How long do bananas last?", "3 to 7 days in a fruit bowl, according to the Voedingscentrum."),
   ("Should you keep bananas in the fridge?", "No. Bananas do not cope well with cold. Keep them in a fruit bowl, away from other fruit."),
   ("Are black bananas safe to eat?", "Yes, if the flesh smells normal and there is no mould. They are perfect for baking or smoothies."),
   ("Can you freeze bananas?", "Yes, peeled, for 8 to 12 months."),
   ("Why do my bananas ripen so fast?", "Apples and pears nearby make bananas ripen faster. Keep them apart and wrap the stems."),
  ],
  "related": ["strawberries", "avocado", "tomatoes"],
 },
 "nl": {
  "slug": "hoe-lang-zijn-bananen-houdbaar", "name": "Bananen",
  "title": "Hoe Lang Zijn Bananen Houdbaar? Bewaartips",
  "desc": "Bananen blijven 3 tot 7 dagen goed op de fruitschaal en 8 tot 12 maanden zonder schil in de vriezer. Bewaar ze buiten de koelkast en apart van ander fruit.",
  "h1": "Hoe lang zijn bananen houdbaar?",
  "answer": "Bananen blijven volgens het Voedingscentrum <strong>3 tot 7 dagen goed op de fruitschaal</strong>. Bewaar ze buiten de koelkast, omdat ze niet goed tegen kou kunnen, en apart van ander fruit. Zonder schil ingevroren blijven bananen 8 tot 12 maanden goed. Een bruine of zwarte schil betekent niet dat een banaan bedorven is.",
  "table_head": ("", "Hoe lang", "Bron"),
  "table": [
   ("Fruitschaal", "3–7 dagen", "Voedingscentrum"),
   ("Koelkast", "Niet aan te raden: bananen kunnen niet goed tegen kou", "Voedingscentrum"),
   ("Vriezer (zonder schil)", "8–12 maanden", "Voedingscentrum"),
  ],
  "body": """
<h2>Bananen horen niet in de koelkast</h2>
<p>Het advies van het Voedingscentrum is duidelijk: bananen kunnen niet goed tegen kou, dus bewaar ze buiten de koelkast. Op de fruitschaal blijven ze 3 tot 7 dagen goed, afhankelijk van hoe rijp ze waren bij aankoop.</p>

<h2>Bananen en ander fruit</h2>
<p>Bananen beïnvloeden het fruit om zich heen, en andersom. Volgens het Voedingscentrum rijpt of bederft veel ander fruit sneller als je het bij bananen bewaart, en rijpen bananen sneller naast appels en peren. Daar kun je handig gebruik van maken:</p>
<ul>
  <li><strong>Langer bewaren?</strong> Leg bananen apart van ander fruit.</li>
  <li><strong>Laten rijpen?</strong> Leg groene bananen naast appels of peren.</li>
  <li><strong>Wikkel de steeltjes in.</strong> Volgens het Voedingscentrum blijven bananen langer goed als je de bovenkant van de tros inwikkelt met (herbruikbaar) vershoudfolie.</li>
</ul>

<h2>Bruine of zwarte bananen</h2>
<p>Een zwarte schil betekent niet meteen dat de banaan bedorven is, zegt het Voedingscentrum: controleer het vruchtvlees. Is dat normaal van geur, dan kun je de banaan nog gebruiken. Ook de Britse Food Standards Agency (FSA) zegt dat overrijp fruit zoals bruine bananen gewoon gegeten kan worden, zolang er geen schimmel op zit. Heel rijpe bananen zijn perfect voor bananenbrood, pannenkoeken, havermout of smoothies. Is de banaan beschimmeld of rot, gooi hem dan weg.</p>

<h2>Kun je bananen invriezen?</h2>
<p>Ja, en ingevroren bananen blijven volgens het Voedingscentrum 8 tot 12 maanden goed. Haal eerst de schil eraf, snijd de banaan eventueel in stukken en bewaar hem in een afsluitbaar bakje of diepvrieszakje. Bevroren stukjes banaan zijn heerlijk direct uit de vriezer in een smoothie, of gepureerd als snel "ijs". Vries bananen in als ze rijp of overrijp zijn, dan zijn ze lekker zoet.</p>

<h2>Hoe herken je een bedorven banaan?</h2>
<p>Kijk verder dan de schil. Tekenen dat een banaan niet meer goed is: schimmel, rot of lekkend vruchtvlees, of een gegiste, alcoholachtige lucht. Een zachte, bruine banaan met vruchtvlees dat normaal ruikt, is gewoon heel rijp.</p>

<h2>Tips om minder bananen te verspillen</h2>
<ul>
  <li>Koop bananen van verschillende rijpheid, zodat ze niet allemaal tegelijk rijp zijn.</li>
  <li>Pel en vries bananen in zodra ze te rijp zijn om zo te eten.</li>
  <li>Zet bananen in FreshGarant, dan denk je er op tijd aan om ze te bakken of in te vriezen.</li>
</ul>
""",
  "faq": [
   ("Hoe lang zijn bananen houdbaar?", "3 tot 7 dagen op de fruitschaal, volgens het Voedingscentrum."),
   ("Moeten bananen in de koelkast?", "Nee. Bananen kunnen niet goed tegen kou. Bewaar ze op de fruitschaal, apart van ander fruit."),
   ("Kun je zwarte bananen nog eten?", "Ja, als het vruchtvlees normaal ruikt en er geen schimmel op zit. Ideaal om mee te bakken of voor smoothies."),
   ("Kun je bananen invriezen?", "Ja, zonder schil, 8 tot 12 maanden."),
   ("Waarom worden mijn bananen zo snel rijp?", "Appels en peren in de buurt laten bananen sneller rijpen. Leg ze apart en wikkel de steeltjes in."),
  ],
  "related": ["strawberries", "avocado", "tomatoes"],
 },
},
# ─────────────────────────────── AVOCADO ───────────────────────────────
{
 "key": "avocado", "emoji": "🥑",
 "sources": ["vc_bewaarwijzer", "fsa_facts"],
 "en": {
  "slug": "how-long-do-avocados-last", "name": "Avocado",
  "title": "How Long Do Avocados Last? Ripening and Storage",
  "desc": "Avocados keep 1 to 6 days in a fruit bowl, depending on ripeness, and longer in the fridge once ripe. Storing half an avocado and freezing tips.",
  "h1": "How long do avocados last?",
  "answer": "Avocados keep <strong>1 to 6 days in a fruit bowl</strong>, depending on how ripe they are, according to the Voedingscentrum. Let them ripen at room temperature, then move them to the fridge, where they keep longer. Keep half an avocado with its stone in, covered, in the fridge. Mashed or in pieces, avocado can be frozen for 8 to 12 months.",
  "table_head": ("", "How long", "Source"),
  "table": [
   ("Fruit bowl", "1–6 days, depending on ripeness", "Voedingscentrum"),
   ("Fridge (once ripe)", "Keeps longer than in the fruit bowl", "Voedingscentrum"),
   ("Half avocado", "In the fridge, with the stone in, covered", "Voedingscentrum"),
   ("Freezer (mashed or in pieces)", "8–12 months", "Voedingscentrum"),
  ],
  "body": """
<h2>Ripen first, then the fridge</h2>
<p>How long an avocado keeps depends on how ripe it is when you buy it. Avocados keep ripening after picking, the Voedingscentrum explains: you can let them ripen in the fruit bowl first and then keep them in the fridge, where they last longer. In the fruit bowl, the storage guide gives 1 to 6 days.</p>
<ul>
  <li><strong>Hard avocado:</strong> leave it in the fruit bowl until it gives slightly when you press gently.</li>
  <li><strong>Need it faster?</strong> Avocados ripen faster next to apples, bananas and pears, in the fruit bowl or in a closed bag, according to the Voedingscentrum.</li>
  <li><strong>Ripe avocado:</strong> into the fridge, to slow it down.</li>
</ul>

<h2>How to keep half an avocado</h2>
<p>The Voedingscentrum's tip: leave the stone in the half you are keeping, cover it with (reusable) cling film and put it in the fridge. That limits browning of the flesh. Eat it within a day or so.</p>

<h2>Brown flesh: spoiled or not?</h2>
<p>Brown discolouration of the flesh does not necessarily mean the avocado has gone off, says the Voedingscentrum. A soft or bruised spot can be cut away if the rest of the avocado is still good. But throw it away if it is mouldy, slimy, rotten or smells off. The FSA also advises not eating food that clearly contains mould.</p>

<h2>Can you freeze avocado?</h2>
<p>Yes. The Voedingscentrum says you can mash avocado or cut it into pieces and freeze it, for 8 to 12 months. The texture does change, so after freezing it is best for guacamole or smoothies rather than slices on toast. A squeeze of lemon or lime juice before freezing helps keep the colour.</p>

<h2>How to tell if an avocado has gone off</h2>
<p>Signs from the Voedingscentrum: mould, slimy or rotten flesh, or an unusual smell. Dark stringy fibres or a few brown spots alone are not a reason to throw the whole avocado away: cut them out and use the rest.</p>

<h2>Tips to waste fewer avocados</h2>
<ul>
  <li>Buy avocados at different stages of ripeness, so you always have one ready.</li>
  <li>Put ripe avocados in the fridge straight away.</li>
  <li>Mash and freeze avocados that are about to go over, for guacamole later.</li>
  <li>Log avocados in FreshGarant, so you catch them at the right moment.</li>
</ul>
""",
  "faq": [
   ("How long do avocados last?", "1 to 6 days in the fruit bowl, depending on ripeness. Ripe avocados keep longer in the fridge."),
   ("Should you keep avocados in the fridge?", "Once they are ripe, yes. Let hard avocados ripen at room temperature first."),
   ("How do you keep half an avocado?", "Leave the stone in, cover it with cling film and put it in the fridge."),
   ("Is a brown avocado still good?", "Brown flesh is not necessarily spoiled. Cut away brown or bruised spots; throw it away if it is mouldy, slimy or smells off."),
   ("Can you freeze avocado?", "Yes, mashed or in pieces, for 8 to 12 months. Use it for guacamole or smoothies."),
  ],
  "related": ["tomatoes", "bananas", "lettuce"],
 },
 "nl": {
  "slug": "hoe-lang-is-avocado-houdbaar", "name": "Avocado",
  "title": "Hoe Lang Is een Avocado Houdbaar? Rijpen en Bewaren",
  "desc": "Een avocado blijft 1 tot 6 dagen goed op de fruitschaal, afhankelijk van de rijpheid, en rijp langer in de koelkast. Een halve avocado bewaren en invriezen.",
  "h1": "Hoe lang is een avocado houdbaar?",
  "answer": "Een avocado blijft volgens het Voedingscentrum <strong>1 tot 6 dagen goed op de fruitschaal</strong>, afhankelijk van hoe rijp hij is. Laat hem eerst op kamertemperatuur rijpen en bewaar hem daarna in de koelkast, waar hij langer goed blijft. Een halve avocado bewaar je met pit, afgedekt, in de koelkast. Gepureerd of in stukjes kun je avocado 8 tot 12 maanden invriezen.",
  "table_head": ("", "Hoe lang", "Bron"),
  "table": [
   ("Fruitschaal", "1–6 dagen, afhankelijk van de rijpheid", "Voedingscentrum"),
   ("Koelkast (als hij rijp is)", "Langer houdbaar dan op de fruitschaal", "Voedingscentrum"),
   ("Halve avocado", "In de koelkast, met pit, afgedekt", "Voedingscentrum"),
   ("Vriezer (gepureerd of in stukjes)", "8–12 maanden", "Voedingscentrum"),
  ],
  "body": """
<h2>Eerst laten rijpen, dan de koelkast</h2>
<p>Hoe lang je een avocado kunt bewaren, hangt af van hoe rijp hij is bij aankoop. Avocado's zijn narijpers, legt het Voedingscentrum uit: je kunt ze eerst laten rijpen op de fruitschaal en daarna in de koelkast bewaren, waar ze langer houdbaar zijn. Op de fruitschaal geeft de Bewaarwijzer 1 tot 6 dagen.</p>
<ul>
  <li><strong>Harde avocado:</strong> laat hem op de fruitschaal liggen tot hij bij zacht drukken een beetje meegeeft.</li>
  <li><strong>Sneller rijp?</strong> Avocado's rijpen sneller samen met appels, bananen en peren, op de fruitschaal of in een afgesloten zak, aldus het Voedingscentrum.</li>
  <li><strong>Rijpe avocado:</strong> de koelkast in, om het rijpen af te remmen.</li>
</ul>

<h2>Een halve avocado bewaren</h2>
<p>De tip van het Voedingscentrum: laat de pit in de helft die je bewaart, dek hem af met (herbruikbaar) vershoudfolie en zet hem in de koelkast. Dat voorkomt verkleuren van het vruchtvlees. Eet hem binnen een dag of zo op.</p>

<h2>Bruin vruchtvlees: bedorven of niet?</h2>
<p>Een bruine verkleuring van het vruchtvlees hoeft niet direct bederf te betekenen, zegt het Voedingscentrum. Een zachte of beurse plek kun je wegsnijden als de rest van de avocado nog goed is. Maar is de avocado beschimmeld, slijmerig, rot of ruikt hij afwijkend, gooi hem dan weg.</p>

<h2>Kun je avocado invriezen?</h2>
<p>Ja. Volgens het Voedingscentrum kun je avocado pureren of in stukjes snijden en invriezen, voor 8 tot 12 maanden. De structuur verandert wel, dus ingevroren avocado gebruik je het best in guacamole of smoothies, niet in plakjes op brood. Een scheutje citroen- of limoensap voor het invriezen helpt de kleur te behouden.</p>

<h2>Hoe herken je een bedorven avocado?</h2>
<p>Signalen volgens het Voedingscentrum: schimmel, slijmerig of rot vruchtvlees, of een afwijkende geur. Donkere draadjes of een paar bruine plekjes zijn alleen geen reden om de hele avocado weg te gooien: snijd ze weg en gebruik de rest.</p>

<h2>Tips om minder avocado's te verspillen</h2>
<ul>
  <li>Koop avocado's van verschillende rijpheid, dan heb je er altijd een klaar.</li>
  <li>Leg rijpe avocado's meteen in de koelkast.</li>
  <li>Pureer en vries avocado's in die bijna over hun beste tijd zijn, voor guacamole later.</li>
  <li>Zet avocado's in FreshGarant, dan vang je ze op het juiste moment.</li>
</ul>
""",
  "faq": [
   ("Hoe lang is een avocado houdbaar?", "1 tot 6 dagen op de fruitschaal, afhankelijk van de rijpheid. Rijpe avocado's blijven langer goed in de koelkast."),
   ("Moet een avocado in de koelkast?", "Als hij rijp is wel. Laat harde avocado's eerst op kamertemperatuur rijpen."),
   ("Hoe bewaar je een halve avocado?", "Laat de pit erin, dek hem af met vershoudfolie en zet hem in de koelkast."),
   ("Is een bruine avocado nog goed?", "Bruin vruchtvlees is niet per se bedorven. Snijd bruine of beurse plekken weg; gooi hem weg als hij beschimmeld, slijmerig of vies ruikt."),
   ("Kun je avocado invriezen?", "Ja, gepureerd of in stukjes, 8 tot 12 maanden. Gebruik hem voor guacamole of smoothies."),
  ],
  "related": ["tomatoes", "bananas", "lettuce"],
 },
},
# ─────────────────────────────── TOMATOES ───────────────────────────────
{
 "key": "tomatoes", "emoji": "🍅",
 "sources": ["vc_bewaarwijzer", "fsa_facts"],
 "en": {
  "slug": "how-long-do-tomatoes-last", "name": "Tomatoes",
  "title": "How Long Do Tomatoes Last? Fridge or Counter",
  "desc": "Tomatoes keep about 1 week outside the fridge, where they keep their flavour. Freezing (blanched, 3 months), cut tomatoes and when to throw them away.",
  "h1": "How long do tomatoes last?",
  "answer": "Tomatoes keep <strong>about 1 week in a fruit bowl</strong>, according to the Voedingscentrum. Keep them outside the fridge, because they lose their flavour in the cold. Store a cut tomato covered, cut side down. Blanched tomatoes can be frozen for about 3 months, for sauces and soups.",
  "table_head": ("", "How long", "Source"),
  "table": [
   ("Fruit bowl / counter", "About 1 week", "Voedingscentrum"),
   ("Fridge", "Not recommended: tomatoes lose their flavour", "Voedingscentrum"),
   ("Freezer (after blanching)", "About 3 months", "Voedingscentrum"),
  ],
  "body": """
<h2>Keep tomatoes out of the fridge</h2>
<p>The Voedingscentrum advises storing tomatoes outside the fridge, because they lose their flavour in the cold. In a fruit bowl or on the counter, out of direct sunlight, they keep about a week. Only very ripe tomatoes you cannot eat in time are better off in the fridge for a day; let them come back to room temperature before eating for the best taste.</p>

<h2>How to keep a cut tomato</h2>
<p>The Voedingscentrum's tip: put a cut tomato with the cut side down on a saucer, in a sealed container, or wrap it in (reusable) cling film, so it does not dry out. Use it within a day or two.</p>

<h2>Soft or spoiled?</h2>
<p>A soft tomato can be overripe but still usable, for example in a sauce, says the Voedingscentrum. But throw a tomato away if it is mouldy, slimy, leaking, rotten or smells off. The FSA advises not eating food that clearly contains mould, because cutting the mould away does not guarantee that unseen toxins are gone.</p>

<h2>Do not eat unripe green tomatoes</h2>
<p>Only eat tomatoes when they are ripe. The Voedingscentrum warns that unripe, green tomatoes contain the toxin tomatine, which can be harmful. This applies to unripe tomatoes, not to varieties that are naturally green when ripe. Let unripe tomatoes ripen on the counter first.</p>

<h2>Can you freeze tomatoes?</h2>
<p>Raw tomatoes are less suitable for freezing, says the Voedingscentrum: after freezing they are only good for sauces or soup. Blanched, they keep about 3 months in the freezer. Score a cross in the skin, dip them in boiling water for a moment and then in cold water, peel them and freeze them whole or chopped. Even easier: cook a batch of tomato sauce and freeze that in portions.</p>

<h2>Tins and passata</h2>
<p>Tinned tomatoes and passata keep a long time unopened. Once opened, the FSA advises not storing food in the opened tin: tip the contents into a storage container, cover it and put it in the fridge.</p>

<h2>Tips to waste fewer tomatoes</h2>
<ul>
  <li>Buy tomatoes at different stages of ripeness.</li>
  <li>Turn soft tomatoes into sauce, soup or shakshuka.</li>
  <li>Log tomatoes in FreshGarant, so the last ones do not get forgotten in the fruit bowl.</li>
</ul>
""",
  "faq": [
   ("How long do tomatoes last?", "About a week in the fruit bowl or on the counter, according to the Voedingscentrum."),
   ("Should tomatoes go in the fridge?", "No, they lose their flavour in the cold. Keep them outside the fridge."),
   ("Can you eat soft tomatoes?", "Yes, overripe tomatoes are great in sauces. Throw them away if they are mouldy, slimy, leaking or smell off."),
   ("Can you freeze tomatoes?", "Yes, blanched, for about 3 months. Use them in sauces or soups afterwards."),
   ("Are green tomatoes safe to eat?", "Unripe green tomatoes contain tomatine, which can be harmful. Only eat ripe tomatoes."),
  ],
  "related": ["avocado", "lettuce", "soup"],
 },
 "nl": {
  "slug": "hoe-lang-zijn-tomaten-houdbaar", "name": "Tomaten",
  "title": "Hoe Lang Zijn Tomaten Houdbaar? Koelkast of Fruitschaal",
  "desc": "Tomaten blijven zo'n week goed buiten de koelkast, waar ze hun smaak houden. Invriezen (geblancheerd, 3 maanden), aangesneden tomaat en wanneer weggooien.",
  "h1": "Hoe lang zijn tomaten houdbaar?",
  "answer": "Tomaten blijven volgens het Voedingscentrum <strong>ongeveer 1 week goed op de fruitschaal</strong>. Bewaar ze buiten de koelkast, want in de kou verliezen ze hun smaak. Een aangesneden tomaat bewaar je afgedekt, met het snijvlak naar beneden. Geblancheerd kun je tomaten zo'n 3 maanden invriezen, voor sauzen en soep.",
  "table_head": ("", "Hoe lang", "Bron"),
  "table": [
   ("Fruitschaal / aanrecht", "Ongeveer 1 week", "Voedingscentrum"),
   ("Koelkast", "Niet aan te raden: tomaten verliezen hun smaak", "Voedingscentrum"),
   ("Vriezer (na blancheren)", "Ongeveer 3 maanden", "Voedingscentrum"),
  ],
  "body": """
<h2>Tomaten horen niet in de koelkast</h2>
<p>Het Voedingscentrum adviseert tomaten buiten de koelkast te bewaren, omdat ze in de koelkast hun smaak verliezen. Op de fruitschaal of het aanrecht, uit de volle zon, blijven ze ongeveer een week goed. Alleen heel rijpe tomaten die je niet op tijd opkrijgt, kunnen beter een dag in de koelkast; laat ze voor het eten weer op kamertemperatuur komen voor de beste smaak.</p>

<h2>Een aangesneden tomaat bewaren</h2>
<p>De tip van het Voedingscentrum: leg een aangesneden tomaat met het snijvlak op een schoteltje, in een afsluitbaar bakje, of verpak hem in (herbruikbaar) vershoudfolie om uitdrogen te voorkomen. Gebruik hem binnen een dag of twee.</p>

<h2>Zacht of bedorven?</h2>
<p>Een zachte tomaat kan overrijp maar nog bruikbaar zijn, bijvoorbeeld voor saus, zegt het Voedingscentrum. Maar is de tomaat beschimmeld, slijmerig, lekt het vruchtvlees, is hij rot of ruikt hij afwijkend, gooi hem dan weg. De Britse Food Standards Agency raadt af eten met zichtbare schimmel te eten, omdat wegsnijden niet garandeert dat onzichtbare gifstoffen weg zijn.</p>

<h2>Eet geen onrijpe groene tomaten</h2>
<p>Eet tomaten alleen als ze rijp zijn. Het Voedingscentrum waarschuwt dat in onrijpe, groene tomaten de gifstof tomatine zit, die schadelijk voor je kan zijn. Dat gaat over onrijpe tomaten, niet over rassen die rijp groen zijn. Laat onrijpe tomaten eerst op het aanrecht rijpen.</p>

<h2>Kun je tomaten invriezen?</h2>
<p>Rauwe tomaten zijn minder geschikt om in te vriezen, zegt het Voedingscentrum: na het invriezen zijn ze alleen nog goed voor sauzen of soep. Geblancheerd blijven ze zo'n 3 maanden goed in de vriezer. Kerf een kruisje in de schil, dompel ze even in kokend water en daarna in koud water, pel ze en vries ze heel of in stukjes in. Nog makkelijker: kook een pan tomatensaus en vries die in porties in.</p>

<h2>Blikken en passata</h2>
<p>Tomaten uit blik en passata blijven ongeopend lang goed. Na openen adviseert de FSA eten niet in het geopende blik te bewaren: doe de inhoud in een bakje, dek het af en zet het in de koelkast.</p>

<h2>Tips om minder tomaten te verspillen</h2>
<ul>
  <li>Koop tomaten van verschillende rijpheid.</li>
  <li>Maak van zachte tomaten saus, soep of shakshuka.</li>
  <li>Zet tomaten in FreshGarant, dan raken de laatste niet vergeten op de fruitschaal.</li>
</ul>
""",
  "faq": [
   ("Hoe lang zijn tomaten houdbaar?", "Ongeveer een week op de fruitschaal of het aanrecht, volgens het Voedingscentrum."),
   ("Moeten tomaten in de koelkast?", "Nee, in de kou verliezen ze hun smaak. Bewaar ze buiten de koelkast."),
   ("Kun je zachte tomaten nog eten?", "Ja, overrijpe tomaten zijn prima voor saus. Gooi ze weg als ze beschimmeld, slijmerig, lekkend of vies ruikend zijn."),
   ("Kun je tomaten invriezen?", "Ja, geblancheerd, zo'n 3 maanden. Gebruik ze daarna in sauzen of soep."),
   ("Zijn groene tomaten gevaarlijk?", "In onrijpe groene tomaten zit tomatine, dat schadelijk kan zijn. Eet alleen rijpe tomaten."),
  ],
  "related": ["avocado", "lettuce", "soup"],
 },
},
]

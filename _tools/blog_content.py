"""Blog articles for freshgarant.app (EN + NL). Rendered by build_blog.py.

Food-safety numbers are deliberately conservative (in line with the Dutch
Voedingscentrum guidance) and every article says to follow the packaging.
"""

PUBLISHED = "2026-10-26"

ARTICLES = [
  {
    "key": "tht-tgt",
    "en": {
      "slug": "best-before-vs-use-by",
      "title": "Best Before vs Use By: What's the Difference?",
      "desc": "Best before is about quality, use by is about safety. What the two dates on your food mean, and when you can still eat something after the date.",
      "kicker": "LABELS",
      "intro": "Two dates, two very different meanings. Mixing them up is one of the biggest reasons good food ends up in the bin — and occasionally why bad food doesn't.",
      "body": """
<h2>Best before: about quality</h2>
<p>A <strong>best before</strong> date tells you until when the manufacturer guarantees the product keeps its full quality — taste, texture, colour — when stored as instructed. After that date the product is usually still perfectly safe to eat. It may just be a little less crisp, crunchy or flavourful.</p>
<p>You'll find it on products that don't spoil quickly: pasta, rice, cereal, crisps, tins, jars, chocolate, flour, frozen food and also eggs.</p>
<h3>Past the best before date? Check it yourself</h3>
<ul>
  <li><strong>Look:</strong> any mould, discolouration or a bulging lid or tin? Throw it away.</li>
  <li><strong>Smell:</strong> does it smell sour, musty or off? Don't eat it.</li>
  <li><strong>Taste:</strong> a small bite — if it tastes normal, it's fine.</li>
</ul>
<p>Dry products like pasta or rice can often last months past the date if the pack is closed and dry.</p>

<h2>Use by: about safety</h2>
<p>A <strong>use by</strong> date is a safety limit. It's used for perishable food where harmful bacteria can grow even when the product still looks and smells fine: fresh meat, minced meat, poultry, fish, ready meals, fresh dairy and pre-cut salads.</p>
<p><strong>Don't eat a product after its use by date</strong>, even if it looks good. Bacteria such as Listeria or Salmonella don't always change the smell or taste.</p>
<h3>Save it before the date</h3>
<p>Many use-by products can go into the freezer <em>before</em> the date. Freezing pauses the clock: thaw it in the fridge and eat it within a day.</p>

<h2>Quick overview</h2>
<table>
  <thead><tr><th></th><th>Best before</th><th>Use by</th></tr></thead>
  <tbody>
    <tr><td>Meaning</td><td>Best quality until</td><td>Safe until</td></tr>
    <tr><td>After the date</td><td>Usually still fine — look, smell, taste</td><td>Don't eat it</td></tr>
    <tr><td>Typical products</td><td>Pasta, rice, tins, cereal, eggs</td><td>Meat, fish, poultry, fresh dairy</td></tr>
    <tr><td>Freezing</td><td>Rarely needed</td><td>Before the date, to make it last</td></tr>
  </tbody>
</table>

<h2>Opened is a different story</h2>
<p>Both dates only apply to <strong>unopened</strong> packs stored as the label says. Once opened, the clock speeds up. The label often says "once opened, consume within 3 days" — that rule beats the printed date.</p>

<h2>Never miss a date again</h2>
<p>FreshGarant keeps track of every date in your fridge, freezer and pantry, and sends you one morning reminder of what expires today, tomorrow and this week — with freeze-it tips for food you can still save.</p>
""",
    },
    "nl": {
      "slug": "tht-tgt-verschil",
      "title": "THT en TGT: wat is het verschil?",
      "desc": "Tenminste houdbaar tot gaat over kwaliteit, te gebruiken tot over veiligheid. Wat de data op je eten betekenen en wanneer je iets na de datum nog kunt eten.",
      "kicker": "ETIKETTEN",
      "intro": "Twee data, twee heel verschillende betekenissen. Ze door elkaar halen is een van de grootste redenen dat goed eten in de prullenbak belandt — en soms dat bedorven eten dat níet doet.",
      "body": """
<h2>THT — tenminste houdbaar tot: over kwaliteit</h2>
<p>De <strong>THT</strong>-datum zegt tot wanneer de fabrikant garandeert dat het product z'n volle kwaliteit houdt — smaak, geur, kleur, knapperigheid — als je het bewaart zoals op de verpakking staat. Daarna is het product meestal nog prima te eten. Het is hooguit iets minder knapperig of smaakvol.</p>
<p>Je vindt THT op producten die niet snel bederven: pasta, rijst, ontbijtgranen, chips, blik, potten, chocolade, meel, diepvriesproducten en ook eieren.</p>
<h3>THT verstreken? Check het zelf</h3>
<ul>
  <li><strong>Kijk:</strong> schimmel, verkleuring of een bolle deksel of bolle blik? Weggooien.</li>
  <li><strong>Ruik:</strong> ruikt het zuur, muf of vreemd? Niet eten.</li>
  <li><strong>Proef:</strong> een klein hapje — smaakt het normaal, dan is het goed.</li>
</ul>
<p>Droge producten als pasta en rijst zijn in een gesloten, droge verpakking vaak nog maanden na de datum goed.</p>

<h2>TGT — te gebruiken tot: over veiligheid</h2>
<p>De <strong>TGT</strong>-datum is een veiligheidsgrens. Die staat op snel bederfelijke producten waarin ziekmakende bacteriën kunnen groeien, ook als het product er nog goed uitziet en goed ruikt: vers vlees, gehakt, kip, vis, kant-en-klaarmaaltijden, verse zuivel en voorgesneden salades.</p>
<p><strong>Eet een product niet meer na de TGT-datum</strong>, ook niet als het er goed uitziet. Bacteriën als Listeria of Salmonella veranderen de geur of smaak niet altijd.</p>
<h3>Red het vóór de datum</h3>
<p>Veel TGT-producten kun je <em>vóór</em> de datum invriezen. Invriezen zet de klok stil: laat het daarna in de koelkast ontdooien en eet het binnen een dag op.</p>

<h2>Snel overzicht</h2>
<table>
  <thead><tr><th></th><th>THT</th><th>TGT</th></tr></thead>
  <tbody>
    <tr><td>Betekenis</td><td>Beste kwaliteit tot</td><td>Veilig tot</td></tr>
    <tr><td>Na de datum</td><td>Meestal nog goed — kijk, ruik, proef</td><td>Niet meer eten</td></tr>
    <tr><td>Typische producten</td><td>Pasta, rijst, blik, ontbijtgranen, eieren</td><td>Vlees, vis, kip, verse zuivel</td></tr>
    <tr><td>Invriezen</td><td>Zelden nodig</td><td>Vóór de datum, om het langer te bewaren</td></tr>
  </tbody>
</table>

<h2>Geopend is een ander verhaal</h2>
<p>Beide data gelden alleen voor een <strong>ongeopende</strong> verpakking die je bewaart zoals op het etiket staat. Na openen gaat de klok sneller. Staat er "na openen binnen 3 dagen gebruiken", dan gaat die regel vóór de gedrukte datum.</p>

<h2>Mis nooit meer een datum</h2>
<p>FreshGarant houdt elke datum in je koelkast, vriezer en voorraadkast bij en stuurt je één ochtendmelding met wat vandaag, morgen en deze week verloopt — met invriestips voor eten dat je nog kunt redden.</p>
""",
    },
  },
  {
    "key": "fridge",
    "en": {
      "slug": "how-long-does-food-last-in-the-fridge",
      "title": "How Long Does Food Last in the Fridge? (Chart)",
      "desc": "How many days chicken, mince, fish, leftovers, milk, cheese and more stay good in the fridge — in one clear chart, plus tips to make food last longer.",
      "kicker": "STORAGE",
      "intro": "The date on the pack is one thing — but how long is that chicken good once it's in your fridge, or those leftovers from last night? Here's a clear, conservative chart.",
      "body": """
<p>These times assume a fridge at <strong>4 °C or colder</strong>. Always follow the packaging first: a use-by date or a "once opened, consume within…" instruction beats this chart.</p>

<h2>Meat, fish and leftovers</h2>
<table>
  <thead><tr><th>Product</th><th>In the fridge</th></tr></thead>
  <tbody>
    <tr><td>Minced meat (raw)</td><td>1 day</td></tr>
    <tr><td>Fresh fish (raw)</td><td>1 day</td></tr>
    <tr><td>Chicken and other poultry (raw)</td><td>1–2 days</td></tr>
    <tr><td>Steak, pork chops (raw)</td><td>2–3 days</td></tr>
    <tr><td>Sliced deli meat, once opened</td><td>2–3 days</td></tr>
    <tr><td>Leftovers and home-cooked meals</td><td>max. 2 days</td></tr>
    <tr><td>Cooked rice</td><td>1 day — cool it quickly</td></tr>
    <tr><td>Homemade soup</td><td>2 days</td></tr>
  </tbody>
</table>

<h2>Dairy and eggs</h2>
<table>
  <thead><tr><th>Product</th><th>In the fridge</th></tr></thead>
  <tbody>
    <tr><td>Milk, once opened</td><td>3–4 days</td></tr>
    <tr><td>Yogurt, once opened</td><td>3–5 days</td></tr>
    <tr><td>Soft cheese (brie, mozzarella)</td><td>about 1 week, or per pack</td></tr>
    <tr><td>Hard cheese, wrapped</td><td>3–4 weeks</td></tr>
    <tr><td>Butter</td><td>until the best before date</td></tr>
    <tr><td>Eggs</td><td>until the best before date</td></tr>
  </tbody>
</table>

<h2>Fruit and vegetables</h2>
<table>
  <thead><tr><th>Product</th><th>In the fridge</th></tr></thead>
  <tbody>
    <tr><td>Cut fruit and vegetables</td><td>2–3 days</td></tr>
    <tr><td>Bagged salad, once opened</td><td>1–2 days</td></tr>
    <tr><td>Leafy greens (spinach, lettuce)</td><td>3–5 days</td></tr>
    <tr><td>Broccoli, courgette, peppers</td><td>about 1 week</td></tr>
    <tr><td>Carrots</td><td>2–3 weeks</td></tr>
  </tbody>
</table>
<p>Not everything belongs in the fridge: bananas, tomatoes, potatoes, onions and bread keep better outside it.</p>

<h2>Five ways to make food last longer</h2>
<ol>
  <li><strong>Keep your fridge at 4 °C.</strong> Many fridges run warmer than you think — a cheap thermometer tells you.</li>
  <li><strong>Raw meat and fish on the bottom shelf</strong>, so juices can't drip onto other food.</li>
  <li><strong>Cool leftovers quickly</strong> and put them in the fridge within two hours, in a closed container.</li>
  <li><strong>First in, first out:</strong> put new groceries at the back and older ones at the front.</li>
  <li><strong>Freeze in time</strong> — before the use-by date, not after.</li>
</ol>

<h2>Let your phone remember</h2>
<p>Scan a barcode or tap a common item, and FreshGarant fills in a sensible expiry date for you. Every morning you see what to use first — so the chicken gets cooked before day three.</p>
""",
    },
    "nl": {
      "slug": "hoe-lang-houdbaar-koelkast",
      "title": "Hoe lang is eten houdbaar in de koelkast? (Tabel)",
      "desc": "Hoeveel dagen kip, gehakt, vis, restjes, melk, kaas en meer goed blijven in de koelkast — in één duidelijke tabel, plus tips om eten langer goed te houden.",
      "kicker": "BEWAREN",
      "intro": "De datum op de verpakking is één ding — maar hoe lang is die kipfilet goed als hij eenmaal in je koelkast ligt, of de restjes van gisteravond? Hier een duidelijke, voorzichtige tabel.",
      "body": """
<p>Deze tijden gaan uit van een koelkast van <strong>4 °C of kouder</strong>. Volg altijd eerst de verpakking: een TGT-datum of "na openen binnen … gebruiken" gaat voor deze tabel.</p>

<h2>Vlees, vis en restjes</h2>
<table>
  <thead><tr><th>Product</th><th>In de koelkast</th></tr></thead>
  <tbody>
    <tr><td>Gehakt (rauw)</td><td>1 dag</td></tr>
    <tr><td>Verse vis (rauw)</td><td>1 dag</td></tr>
    <tr><td>Kip en ander gevogelte (rauw)</td><td>1–2 dagen</td></tr>
    <tr><td>Biefstuk, karbonade (rauw)</td><td>2–3 dagen</td></tr>
    <tr><td>Vleeswaren, na openen</td><td>2–3 dagen</td></tr>
    <tr><td>Restjes en zelfgekookte maaltijden</td><td>max. 2 dagen</td></tr>
    <tr><td>Gekookte rijst</td><td>1 dag — snel laten afkoelen</td></tr>
    <tr><td>Zelfgemaakte soep</td><td>2 dagen</td></tr>
  </tbody>
</table>

<h2>Zuivel en eieren</h2>
<table>
  <thead><tr><th>Product</th><th>In de koelkast</th></tr></thead>
  <tbody>
    <tr><td>Melk, na openen</td><td>3–4 dagen</td></tr>
    <tr><td>Yoghurt, na openen</td><td>3–5 dagen</td></tr>
    <tr><td>Zachte kaas (brie, mozzarella)</td><td>ongeveer 1 week, of volgens verpakking</td></tr>
    <tr><td>Harde kaas, verpakt</td><td>3–4 weken</td></tr>
    <tr><td>Roomboter</td><td>tot de THT-datum</td></tr>
    <tr><td>Eieren</td><td>tot de THT-datum</td></tr>
  </tbody>
</table>

<h2>Groente en fruit</h2>
<table>
  <thead><tr><th>Product</th><th>In de koelkast</th></tr></thead>
  <tbody>
    <tr><td>Gesneden groente en fruit</td><td>2–3 dagen</td></tr>
    <tr><td>Zak sla, na openen</td><td>1–2 dagen</td></tr>
    <tr><td>Bladgroente (spinazie, sla)</td><td>3–5 dagen</td></tr>
    <tr><td>Broccoli, courgette, paprika</td><td>ongeveer 1 week</td></tr>
    <tr><td>Wortels</td><td>2–3 weken</td></tr>
  </tbody>
</table>
<p>Niet alles hoort in de koelkast: bananen, tomaten, aardappelen, uien en brood blijven daarbuiten juist beter.</p>

<h2>Vijf manieren om eten langer goed te houden</h2>
<ol>
  <li><strong>Zet je koelkast op 4 °C.</strong> Veel koelkasten zijn warmer dan je denkt — een goedkope thermometer laat het zien.</li>
  <li><strong>Rauw vlees en vis op de onderste plank</strong>, zodat vocht niet op ander eten druppelt.</li>
  <li><strong>Laat restjes snel afkoelen</strong> en zet ze binnen twee uur in een afgesloten bakje in de koelkast.</li>
  <li><strong>Eerst erin, eerst eruit:</strong> nieuwe boodschappen achteraan, oudere vooraan.</li>
  <li><strong>Vries op tijd in</strong> — vóór de TGT-datum, niet erna.</li>
</ol>

<h2>Laat je telefoon het onthouden</h2>
<p>Scan een barcode of tik een vast product aan, en FreshGarant vult zelf een logische houdbaarheidsdatum in. Elke ochtend zie je wat je eerst moet opmaken — zodat de kip gekookt wordt vóór dag drie.</p>
""",
    },
  },
  {
    "key": "freeze",
    "en": {
      "slug": "what-food-can-you-freeze",
      "title": "What Food Can You Freeze, and for How Long?",
      "desc": "Bread, meat, fish, leftovers, fruit and more: how long food keeps in the freezer, what not to freeze, and how to thaw safely.",
      "kicker": "FREEZER",
      "intro": "Your freezer is the easiest way to stop throwing food away. Almost anything can go in — if you know how long it keeps and how to thaw it.",
      "body": """
<p>At <strong>−18 °C</strong> bacteria stop growing, so frozen food stays safe for a long time. The times below are about <em>quality</em>: after that, food is still safe but can get dry or lose flavour ("freezer burn").</p>

<h2>How long food keeps in the freezer</h2>
<table>
  <thead><tr><th>Product</th><th>In the freezer</th></tr></thead>
  <tbody>
    <tr><td>Bread and rolls</td><td>up to 3 months</td></tr>
    <tr><td>Minced meat, sausages</td><td>up to 3 months</td></tr>
    <tr><td>Chicken and other poultry</td><td>up to 6 months</td></tr>
    <tr><td>Beef and pork (lean)</td><td>6–9 months</td></tr>
    <tr><td>Fatty fish (salmon, mackerel)</td><td>2–3 months</td></tr>
    <tr><td>Lean fish (cod, pollock)</td><td>up to 6 months</td></tr>
    <tr><td>Cooked meals, soups, sauces</td><td>2–3 months</td></tr>
    <tr><td>Butter</td><td>up to 6 months</td></tr>
    <tr><td>Grated hard cheese</td><td>up to 3 months</td></tr>
    <tr><td>Vegetables (blanched)</td><td>8–12 months</td></tr>
    <tr><td>Fruit (berries, banana slices)</td><td>8–12 months</td></tr>
  </tbody>
</table>

<h2>What you'd better not freeze</h2>
<ul>
  <li><strong>Lettuce, cucumber, radish:</strong> they turn limp and watery.</li>
  <li><strong>Raw eggs in their shell:</strong> they can crack. Beat them first.</li>
  <li><strong>Mayonnaise and creamy sauces:</strong> they separate.</li>
  <li><strong>Fizzy drinks:</strong> the can or bottle can burst.</li>
</ul>

<h2>Freezing tips</h2>
<ol>
  <li><strong>Freeze before the use-by date</strong> — freezing pauses the clock, it doesn't turn it back.</li>
  <li><strong>Portion it:</strong> freeze in the amounts you'll use, so you never thaw more than you need.</li>
  <li><strong>Squeeze out the air</strong> and use freezer bags or boxes against freezer burn.</li>
  <li><strong>Write the date on it.</strong> Two months later nobody remembers.</li>
  <li><strong>Cool cooked food first</strong>, then freeze it.</li>
</ol>

<h2>Thawing safely</h2>
<ul>
  <li><strong>In the fridge</strong> is safest: overnight for most products.</li>
  <li><strong>In the microwave</strong> on the defrost setting, and cook it straight away.</li>
  <li><strong>Not on the counter</strong> for meat, fish or poultry — the outside warms up while the inside is still frozen.</li>
  <li>Eat thawed food within a day, and <strong>don't refreeze raw food</strong> once thawed. Once you've cooked it, you can freeze the cooked dish again.</li>
</ul>

<h2>Let FreshGarant remind you</h2>
<p>FreshGarant's morning reminder suggests freezing items that are about to expire, and tracks your freezer separately — so you know what's in there and how long it's been.</p>
""",
    },
    "nl": {
      "slug": "wat-kun-je-invriezen",
      "title": "Wat kun je invriezen, en hoe lang?",
      "desc": "Brood, vlees, vis, restjes, fruit en meer: hoe lang eten goed blijft in de vriezer, wat je beter niet invriest en hoe je veilig ontdooit.",
      "kicker": "VRIEZER",
      "intro": "Je vriezer is de makkelijkste manier om geen eten meer weg te gooien. Bijna alles kan erin — als je weet hoe lang het goed blijft en hoe je het ontdooit.",
      "body": """
<p>Bij <strong>−18 °C</strong> groeien bacteriën niet meer, dus ingevroren eten blijft lang veilig. De tijden hieronder gaan over <em>kwaliteit</em>: daarna is het nog veilig, maar kan het uitdrogen of smaak verliezen ("vriesbrand").</p>

<h2>Hoe lang eten goed blijft in de vriezer</h2>
<table>
  <thead><tr><th>Product</th><th>In de vriezer</th></tr></thead>
  <tbody>
    <tr><td>Brood en broodjes</td><td>tot 3 maanden</td></tr>
    <tr><td>Gehakt, worst</td><td>tot 3 maanden</td></tr>
    <tr><td>Kip en ander gevogelte</td><td>tot 6 maanden</td></tr>
    <tr><td>Rund- en varkensvlees (mager)</td><td>6–9 maanden</td></tr>
    <tr><td>Vette vis (zalm, makreel)</td><td>2–3 maanden</td></tr>
    <tr><td>Magere vis (kabeljauw, koolvis)</td><td>tot 6 maanden</td></tr>
    <tr><td>Gekookte maaltijden, soep, saus</td><td>2–3 maanden</td></tr>
    <tr><td>Roomboter</td><td>tot 6 maanden</td></tr>
    <tr><td>Geraspte harde kaas</td><td>tot 3 maanden</td></tr>
    <tr><td>Groente (geblancheerd)</td><td>8–12 maanden</td></tr>
    <tr><td>Fruit (bessen, plakjes banaan)</td><td>8–12 maanden</td></tr>
  </tbody>
</table>

<h2>Wat je beter niet invriest</h2>
<ul>
  <li><strong>Sla, komkommer, radijs:</strong> die worden slap en waterig.</li>
  <li><strong>Rauwe eieren in de schaal:</strong> die kunnen barsten. Klop ze eerst los.</li>
  <li><strong>Mayonaise en romige sauzen:</strong> die gaan schiften.</li>
  <li><strong>Frisdrank met prik:</strong> blik of fles kan knappen.</li>
</ul>

<h2>Tips voor invriezen</h2>
<ol>
  <li><strong>Vries in vóór de TGT-datum</strong> — invriezen zet de klok stil, maar draait hem niet terug.</li>
  <li><strong>Verdeel in porties</strong> die je in één keer gebruikt, dan ontdooi je nooit te veel.</li>
  <li><strong>Knijp de lucht eruit</strong> en gebruik vriezakjes of -bakjes tegen vriesbrand.</li>
  <li><strong>Schrijf de datum erop.</strong> Twee maanden later weet niemand het meer.</li>
  <li><strong>Laat gekookt eten eerst afkoelen</strong> en vries het daarna in.</li>
</ol>

<h2>Veilig ontdooien</h2>
<ul>
  <li><strong>In de koelkast</strong> is het veiligst: voor de meeste producten een nacht.</li>
  <li><strong>In de magnetron</strong> op de ontdooistand, en daarna direct bereiden.</li>
  <li><strong>Niet op het aanrecht</strong> bij vlees, vis of kip — de buitenkant wordt warm terwijl de binnenkant nog bevroren is.</li>
  <li>Eet ontdooid eten binnen een dag op en <strong>vries rauw ontdooid eten niet opnieuw in</strong>. Heb je het gekookt, dan mag het gerecht wel weer de vriezer in.</li>
</ul>

<h2>Laat FreshGarant je eraan herinneren</h2>
<p>De ochtendmelding van FreshGarant stelt voor om bijna-verlopen producten in te vriezen, en houdt je vriezer apart bij — zodat je weet wat erin zit en hoe lang al.</p>
""",
    },
  },
  {
    "key": "tips",
    "en": {
      "slug": "reduce-food-waste-at-home",
      "title": "10 Ways to Reduce Food Waste at Home",
      "desc": "Ten practical tips to waste less food and save money: smarter shopping, better storage, cooking with leftovers and knowing what's in your fridge.",
      "kicker": "TIPS",
      "intro": "In the Netherlands every person throws away about 34 kilos of food a year, according to the Voedingscentrum. Most of it is food that simply expired unnoticed. These ten habits make the biggest difference.",
      "body": """
<h2>Before you shop</h2>
<ol>
  <li><strong>Check what you already have.</strong> Most double purchases happen because nobody looked in the fridge first.</li>
  <li><strong>Plan a few meals.</strong> You don't need a full week — three planned dinners already cut impulse buys.</li>
  <li><strong>Make a list, and stick to it.</strong> Especially for fresh products with a short life.</li>
</ol>

<h2>At home</h2>
<ol start="4">
  <li><strong>First in, first out.</strong> Put new groceries at the back, older ones at the front.</li>
  <li><strong>Know the difference between best before and use by.</strong> Best before food is often fine after the date; use by food isn't. <a href="/blog/best-before-vs-use-by.html">Read the difference</a>.</li>
  <li><strong>Store food in the right place.</strong> Some things last longer outside the fridge, others only inside it. <a href="/blog/how-long-does-food-last-in-the-fridge.html">See the fridge chart</a>.</li>
  <li><strong>Freeze in time.</strong> Bread, meat and leftovers can almost all go in the freezer before they expire. <a href="/blog/what-food-can-you-freeze.html">What you can freeze</a>.</li>
</ol>

<h2>In the kitchen</h2>
<ol start="8">
  <li><strong>Cook with what needs to go first.</strong> Build tonight's meal around the item that expires soonest.</li>
  <li><strong>Make a "use it up" meal once a week</strong> — soup, stir-fry, omelette or pasta take almost anything.</li>
  <li><strong>Cook smaller portions, or plan leftovers.</strong> Leftovers keep about two days in the fridge, or months in the freezer.</li>
</ol>

<h2>How much could you save?</h2>
<p>Food that expires unnoticed is money in the bin. Our <a href="/savings.html">savings calculator</a> estimates what you could save based on your own grocery spending.</p>

<h2>Let an app do the remembering</h2>
<p>FreshGarant brings tips 1, 4, 7 and 8 together: it knows what's in your fridge, freezer and pantry, warns you before anything expires, and suggests recipes with the items that need to go first.</p>
""",
    },
    "nl": {
      "slug": "voedselverspilling-tegengaan-tips",
      "title": "Voedselverspilling tegengaan: 10 tips voor thuis",
      "desc": "Tien praktische tips om minder eten weg te gooien en geld te besparen: slimmer boodschappen doen, beter bewaren, koken met restjes en weten wat er in je koelkast ligt.",
      "kicker": "TIPS",
      "intro": "Volgens het Voedingscentrum gooit iedere Nederlander zo'n 34 kilo eten per jaar weg. Het meeste daarvan is eten dat ongemerkt over de datum ging. Deze tien gewoontes maken het grootste verschil.",
      "body": """
<h2>Vóór je boodschappen doet</h2>
<ol>
  <li><strong>Kijk wat je al in huis hebt.</strong> De meeste dubbele aankopen gebeuren omdat niemand eerst in de koelkast keek.</li>
  <li><strong>Plan een paar maaltijden.</strong> Een hele week hoeft niet — drie geplande avondmaaltijden voorkomen al veel impulsaankopen.</li>
  <li><strong>Maak een lijstje, en houd je eraan.</strong> Zeker voor verse producten die snel bederven.</li>
</ol>

<h2>Thuis</h2>
<ol start="4">
  <li><strong>Eerst erin, eerst eruit.</strong> Nieuwe boodschappen achteraan, oudere vooraan.</li>
  <li><strong>Ken het verschil tussen THT en TGT.</strong> THT-producten zijn na de datum vaak nog goed; TGT-producten niet. <a href="/nl/blog/tht-tgt-verschil.html">Lees het verschil</a>.</li>
  <li><strong>Bewaar eten op de juiste plek.</strong> Sommige producten blijven buiten de koelkast langer goed, andere alleen erin. <a href="/nl/blog/hoe-lang-houdbaar-koelkast.html">Bekijk de koelkasttabel</a>.</li>
  <li><strong>Vries op tijd in.</strong> Brood, vlees en restjes kunnen bijna allemaal de vriezer in vóór ze verlopen. <a href="/nl/blog/wat-kun-je-invriezen.html">Wat je kunt invriezen</a>.</li>
</ol>

<h2>In de keuken</h2>
<ol start="8">
  <li><strong>Kook met wat eerst op moet.</strong> Bouw de maaltijd van vanavond rond het product dat het eerst verloopt.</li>
  <li><strong>Maak één keer per week een "restjesmaaltijd"</strong> — soep, wokgerecht, omelet of pasta kan bijna alles hebben.</li>
  <li><strong>Kook kleinere porties, of plan je restjes.</strong> Restjes blijven zo'n twee dagen goed in de koelkast, of maanden in de vriezer.</li>
</ol>

<h2>Hoeveel kun jij besparen?</h2>
<p>Eten dat ongemerkt verloopt, is geld in de prullenbak. Onze <a href="/nl/savings.html">besparings-calculator</a> schat wat jij kunt besparen op basis van je eigen boodschappen.</p>

<h2>Laat een app het onthouden</h2>
<p>FreshGarant combineert tip 1, 4, 7 en 8: de app weet wat er in je koelkast, vriezer en voorraadkast ligt, waarschuwt je voordat iets verloopt en stelt recepten voor met de producten die als eerste op moeten.</p>
""",
    },
  },
]

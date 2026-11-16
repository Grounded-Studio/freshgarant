"""Storage guides, batch C: bread, lettuce, potatoes, cooked pasta, soup,
leftovers. Fridge times from the Voedingscentrum Bewaarwijzer apply to an
OPENED product; an unopened pack follows the date on the pack."""

GUIDES_C = [
# ─────────────────────────────── BREAD ───────────────────────────────
{
 "key": "bread", "emoji": "🍞",
 "sources": ["vc_bewaarwijzer", "fsa_facts"],
 "en": {
  "slug": "how-long-does-bread-last", "name": "Bread",
  "title": "How Long Does Bread Last? Counter and Freezer",
  "desc": "Bread keeps 2 to 4 days at room temperature and 1 to 3 months in the freezer. How to store bread, freeze it in slices and what to do with mould.",
  "h1": "How long does bread last?",
  "answer": "Bread keeps <strong>2 to 4 days at room temperature</strong>, according to the Voedingscentrum: about 2–4 days for white bread and 4 days for wholemeal. In the freezer it keeps 1 to 3 months. The Voedingscentrum's best tip: freeze bread in portions straight after buying and take out what you need each day. Mouldy bread goes in the bin.",
  "table_head": ("", "How long", "Source"),
  "table": [
   ("White bread, room temperature", "2–4 days", "Voedingscentrum"),
   ("Wholemeal bread, room temperature", "About 4 days", "Voedingscentrum"),
   ("White bread, freezer", "About 1 month", "Voedingscentrum"),
   ("Wholemeal bread, freezer", "1–3 months", "Voedingscentrum"),
   ("Bread with mould", "Throw the whole loaf away", "FSA"),
  ],
  "body": """
<h2>How long does bread stay fresh?</h2>
<p>The Voedingscentrum's storage guide gives 2 to 4 days at room temperature for white bread and about 4 days for wholemeal bread. Bread rarely becomes unsafe within that time; it mostly goes stale and dry. The real risk comes later, when mould appears.</p>

<h2>Freeze it: fresh bread every day</h2>
<p>The Voedingscentrum's main tip is simple: freeze bread in portions straight after buying, and take out what you need each day. Slices defrost in a few minutes on the counter or go straight into the toaster. This way you never have to throw away the end of a loaf.</p>
<ul>
  <li><strong>White bread:</strong> about 1 month in the freezer.</li>
  <li><strong>Wholemeal bread:</strong> 1 to 3 months.</li>
  <li><strong>Mind the dryness:</strong> bread is safe in the freezer, but it does dry out. The longer it is frozen, the drier it gets, so wrap it well.</li>
</ul>

<h2>How to store bread at room temperature</h2>
<ul>
  <li><strong>Closed, in a bread bin or bag,</strong> so it does not dry out.</li>
  <li><strong>Cool and dry,</strong> away from the oven and direct sunlight. Warmth and moisture help mould grow.</li>
  <li><strong>Cut side down</strong> on a board, if you keep a loaf unwrapped for a short time.</li>
</ul>

<h2>Mould on bread: throw it away</h2>
<p>It is tempting to tear off the mouldy corner, but mould on bread can spread through the soft crumb further than you can see. The FSA advises not eating food that clearly contains mould, because removing the mouldy part does not guarantee that unseen toxins are gone. That applies to the whole loaf or bag, not just the slice with the spot. This advice matters most for children, pregnant people, people over 65 and anyone with a weakened immune system.</p>

<h2>How to tell if bread has gone off</h2>
<p>The Voedingscentrum names these signs: bread that tastes or smells musty, is dry, or has mould. Dry bread is not spoiled; it is just stale. Musty-smelling or mouldy bread is.</p>

<h2>What to do with stale bread</h2>
<p>Stale bread is perfect for cooking. The Voedingscentrum suggests toasting it or making a toasted sandwich. Other ideas: croutons for soup or salad, breadcrumbs (blitz and freeze them), French toast, bread pudding or a summer salad with tomatoes.</p>

<h2>Tips to waste less bread</h2>
<ul>
  <li>Freeze half the loaf on the day you buy it.</li>
  <li>Buy smaller loaves if you live alone.</li>
  <li>Log your bread in FreshGarant, so you get a reminder to use or freeze it in time.</li>
</ul>
""",
  "faq": [
   ("How long does bread last at room temperature?", "2 to 4 days for white bread and about 4 days for wholemeal, according to the Voedingscentrum."),
   ("Can you freeze bread?", "Yes: white bread about 1 month, wholemeal 1 to 3 months. Freeze it in slices so you can take out what you need."),
   ("Can you cut mould off bread?", "No. Mould can spread through the crumb further than you can see. Throw the loaf away."),
   ("Is stale bread safe to eat?", "Yes. Dry or stale bread is not spoiled. Toast it, or use it for croutons or breadcrumbs."),
   ("Should you keep bread in the fridge?", "The Voedingscentrum lists room temperature and the freezer for bread. To keep it longer, freeze it."),
  ],
  "related": ["cheese", "ham", "leftovers"],
 },
 "nl": {
  "slug": "hoe-lang-is-brood-houdbaar", "name": "Brood",
  "title": "Hoe Lang Is Brood Houdbaar? Broodtrommel en Vriezer",
  "desc": "Brood blijft 2 tot 4 dagen goed buiten de koelkast en 1 tot 3 maanden in de vriezer. Zo bewaar je brood en wat doe je met schimmel?",
  "h1": "Hoe lang is brood houdbaar?",
  "answer": "Brood blijft volgens het Voedingscentrum <strong>2 tot 4 dagen goed buiten de koelkast</strong>: wit brood 2 à 4 dagen en volkorenbrood zo'n 4 dagen. In de vriezer blijft brood 1 tot 3 maanden goed. De beste tip van het Voedingscentrum: vries brood direct na aankoop in porties in en haal er elke dag uit wat je nodig hebt. Beschimmeld brood gooi je weg.",
  "table_head": ("", "Hoe lang", "Bron"),
  "table": [
   ("Wit brood, buiten de koelkast", "2–4 dagen", "Voedingscentrum"),
   ("Volkorenbrood, buiten de koelkast", "Ongeveer 4 dagen", "Voedingscentrum"),
   ("Wit brood, vriezer", "Ongeveer 1 maand", "Voedingscentrum"),
   ("Volkorenbrood, vriezer", "1–3 maanden", "Voedingscentrum"),
   ("Brood met schimmel", "Het hele brood weggooien", "FSA"),
  ],
  "body": """
<h2>Hoe lang blijft brood vers?</h2>
<p>De Bewaarwijzer van het Voedingscentrum geeft 2 tot 4 dagen buiten de koelkast voor wit brood en ongeveer 4 dagen voor volkorenbrood. In die tijd wordt brood zelden onveilig; het wordt vooral oud en droog. Het echte risico komt later, als er schimmel op komt.</p>

<h2>Invriezen: elke dag vers brood</h2>
<p>De belangrijkste tip van het Voedingscentrum: vries brood direct na aankoop in porties in en haal er elke dag uit wat je nodig hebt. Sneetjes zijn op het aanrecht in een paar minuten ontdooid, of gaan zo de broodrooster in. Zo hoef je nooit meer een kontje weg te gooien.</p>
<ul>
  <li><strong>Wit brood:</strong> ongeveer 1 maand in de vriezer.</li>
  <li><strong>Volkorenbrood:</strong> 1 tot 3 maanden.</li>
  <li><strong>Let op uitdroging:</strong> brood kan veilig in de vriezer, maar droogt wel uit. Hoe langer het ingevroren is, hoe droger. Verpak het dus goed.</li>
</ul>

<h2>Zo bewaar je brood buiten de vriezer</h2>
<ul>
  <li><strong>Afgesloten, in een broodtrommel of zak,</strong> zodat het niet uitdroogt.</li>
  <li><strong>Koel en droog,</strong> uit de buurt van de oven en direct zonlicht. Warmte en vocht helpen schimmel groeien.</li>
  <li><strong>Met het snijvlak naar beneden</strong> op een plank, als je een brood even onverpakt laat liggen.</li>
</ul>

<h2>Schimmel op brood: weggooien</h2>
<p>Het is verleidelijk om het beschimmelde hoekje eraf te scheuren, maar schimmel kan zich door het zachte kruim verder verspreiden dan je ziet. De Britse Food Standards Agency (FSA) raadt af eten met zichtbare schimmel te eten, omdat wegsnijden niet garandeert dat onzichtbare gifstoffen weg zijn. Dat geldt voor het hele brood of de hele zak, niet alleen voor het sneetje met de plek. Dit advies telt het zwaarst voor kinderen, zwangeren, 65-plussers en mensen met een verminderde weerstand.</p>

<h2>Hoe herken je bedorven brood?</h2>
<p>Het Voedingscentrum noemt deze signalen: het brood smaakt en ruikt muf, is droog of beschimmeld. Droog brood is niet bedorven, alleen oud. Muf ruikend of beschimmeld brood wel.</p>

<h2>Wat doe je met oud brood?</h2>
<p>Oud brood is prima om mee te koken. Het Voedingscentrum raadt aan het te roosteren of er een tosti van te maken. Andere ideeën: croutons voor soep of salade, paneermeel (fijnmalen en invriezen), wentelteefjes, broodpudding of een zomerse salade met tomaat.</p>

<h2>Tips om minder brood te verspillen</h2>
<ul>
  <li>Vries een half brood in op de dag dat je het koopt.</li>
  <li>Koop een half brood als je alleen woont.</li>
  <li>Zet je brood in FreshGarant, dan krijg je op tijd een seintje om het op te maken of in te vriezen.</li>
</ul>
""",
  "faq": [
   ("Hoe lang is brood houdbaar buiten de koelkast?", "Wit brood 2 tot 4 dagen en volkorenbrood ongeveer 4 dagen, volgens het Voedingscentrum."),
   ("Kun je brood invriezen?", "Ja: wit brood ongeveer 1 maand, volkoren 1 tot 3 maanden. Vries het in sneetjes in, dan pak je wat je nodig hebt."),
   ("Mag je schimmel van brood afhalen?", "Nee. Schimmel kan verder door het kruim zitten dan je ziet. Gooi het brood weg."),
   ("Kun je oud brood nog eten?", "Ja. Droog of oud brood is niet bedorven. Rooster het, of maak er croutons, paneermeel of wentelteefjes van."),
   ("Moet brood in de koelkast?", "Het Voedingscentrum noemt voor brood buiten de koelkast en de vriezer. Wil je het langer bewaren, vries het dan in."),
  ],
  "related": ["cheese", "ham", "leftovers"],
 },
},
# ─────────────────────────────── LETTUCE ───────────────────────────────
{
 "key": "lettuce", "emoji": "🥬",
 "sources": ["vc_bewaarwijzer", "fsa_facts"],
 "en": {
  "slug": "how-long-does-lettuce-last", "name": "Lettuce",
  "title": "How Long Does Lettuce Last in the Fridge?",
  "desc": "A whole head of lettuce keeps 2–5 days in the fridge, bagged salad 2 days once opened. How to keep lettuce crisp, and when wilted salad has gone off.",
  "h1": "How long does lettuce last in the fridge?",
  "answer": "A whole head of lettuce keeps <strong>2 to 5 days in the fridge</strong>, according to the Voedingscentrum. Bagged, pre-cut salad keeps 2 days once opened, and never past its use-by date. Lettuce cannot be frozen. Wilted lettuce is not automatically spoiled; slimy, mouldy or bad-smelling lettuce is.",
  "table_head": ("", "How long", "Source"),
  "table": [
   ("Whole head of lettuce, fridge", "2–5 days", "Voedingscentrum"),
   ("Bagged mixed salad, opened", "2 days, and never past the use-by date", "Voedingscentrum"),
   ("Freezer", "Not suitable", "Voedingscentrum"),
  ],
  "body": """
<h2>Whole lettuce versus bagged salad</h2>
<p>A whole head of lettuce keeps 2 to 5 days in the fridge, according to the Voedingscentrum's storage guide. Pre-cut, bagged salad is more delicate: 2 days once opened. Cutting damages the leaves, so bacteria can grow more easily. That is why bagged salad often has a use-by date, and the Voedingscentrum says not to eat pre-cut vegetables after that date because of the risk of harmful bacteria.</p>

<h2>How to keep lettuce fresh for longer</h2>
<ul>
  <li><strong>Trim the stem and give it water.</strong> The Voedingscentrum suggests cutting a thin slice off the bottom and placing the head in a small bowl of water in the fridge.</li>
  <li><strong>Or use a damp tea towel.</strong> Wrapping the base of the lettuce in a damp tea towel also helps.</li>
  <li><strong>Keep it away from apples, bananas and pears.</strong> Lettuce stored next to them spoils faster.</li>
  <li><strong>Close opened bags,</strong> or move the leaves to a container with a piece of kitchen paper.</li>
</ul>

<h2>Should you wash lettuce?</h2>
<p>The FSA advises washing fruit and vegetables with water before you eat them, to remove dirt and bacteria from the outside: under a running tap or in a bowl of fresh water. Bagged salad that says "washed and ready to eat" does not need washing again. Wash lettuce just before eating rather than before storing it, so it stays dry in the fridge.</p>

<h2>Can you freeze lettuce?</h2>
<p>No. The Voedingscentrum calls lettuce unsuitable for freezing: the leaves turn limp and watery once defrosted. Spinach and other cooking greens are a different story, but salad leaves are best eaten fresh.</p>

<h2>Wilted or spoiled?</h2>
<p>Wilted lettuce is not automatically spoiled, the Voedingscentrum points out. You can often revive limp leaves in a bowl of ice-cold water for a few minutes. But throw lettuce away if it is mouldy, slimy or smells off. For bagged salad past its use-by date, the date decides.</p>

<h2>Tips to waste less lettuce</h2>
<ul>
  <li>Buy a whole head instead of a bag if you will not finish it within two days.</li>
  <li>Plan salads early in the week, and save sturdier vegetables for later.</li>
  <li>Log bagged salad in FreshGarant with its use-by date, so it does not get forgotten at the back of the fridge.</li>
</ul>
""",
  "faq": [
   ("How long does a head of lettuce last?", "2 to 5 days in the fridge, according to the Voedingscentrum."),
   ("How long does bagged salad last once opened?", "2 days, and never past its use-by date."),
   ("Can you eat wilted lettuce?", "Yes, wilted is not spoiled. A few minutes in ice-cold water often crisps it up again. Slimy, mouldy or smelly lettuce goes in the bin."),
   ("Can you freeze lettuce?", "No, salad leaves turn limp and watery after freezing."),
   ("Why does my lettuce go off so fast?", "Storing it next to apples, bananas or pears speeds up spoiling. Keep it apart, and keep the base moist."),
  ],
  "related": ["tomatoes", "avocado", "strawberries"],
 },
 "nl": {
  "slug": "hoe-lang-is-sla-houdbaar", "name": "Sla",
  "title": "Hoe Lang Is Sla Houdbaar in de Koelkast?",
  "desc": "Een krop sla blijft 2 tot 5 dagen goed in de koelkast, gesneden sla na openen 2 dagen. Zo houd je sla knapperig, en wanneer is slappe sla bedorven?",
  "h1": "Hoe lang is sla houdbaar in de koelkast?",
  "answer": "Een krop sla blijft volgens het Voedingscentrum <strong>2 tot 5 dagen goed in de koelkast</strong>. Voorgesneden sla uit een zak houd je na openen 2 dagen, en nooit na de TGT-datum. Sla kun je niet invriezen. Slappe sla is niet meteen bedorven; slijmerige, beschimmelde of vies ruikende sla wel.",
  "table_head": ("", "Hoe lang", "Bron"),
  "table": [
   ("Krop sla, koelkast", "2–5 dagen", "Voedingscentrum"),
   ("Gemengde sla uit een zak, geopend", "2 dagen, en nooit na de TGT-datum", "Voedingscentrum"),
   ("Vriezer", "Niet geschikt", "Voedingscentrum"),
  ],
  "body": """
<h2>Krop sla of zak sla?</h2>
<p>Een krop sla blijft volgens de Bewaarwijzer van het Voedingscentrum 2 tot 5 dagen goed in de koelkast. Voorgesneden sla uit een zak is kwetsbaarder: 2 dagen na openen. Door het snijden raken de blaadjes beschadigd, waardoor bacteriën makkelijker groeien. Daarom staat er op zakken sla vaak een TGT-datum, en het Voedingscentrum zegt: voorgesneden groenten niet eten na de TGT-datum, vanwege de kans op ziekmakende bacteriën.</p>

<h2>Zo blijft sla langer goed</h2>
<ul>
  <li><strong>Snijd de onderkant bij en zet hem in water.</strong> Het Voedingscentrum raadt aan een dun plakje van de onderkant af te snijden en de krop in een kommetje water in de koelkast te zetten.</li>
  <li><strong>Of gebruik een vochtige theedoek.</strong> De onderkant van de sla in een vochtige theedoek wikkelen helpt ook.</li>
  <li><strong>Niet bij appels, bananen en peren.</strong> Daarnaast bederft sla sneller.</li>
  <li><strong>Sluit geopende zakken goed af,</strong> of doe de blaadjes in een bakje met een stukje keukenpapier.</li>
</ul>

<h2>Moet je sla wassen?</h2>
<p>De Britse Food Standards Agency (FSA) adviseert groente en fruit vóór het eten met water te wassen, onder de kraan of in een kom schoon water, om vuil en bacteriën aan de buitenkant te verwijderen. Sla uit een zak met "gewassen en klaar voor gebruik" hoeft niet nog eens gewassen te worden. Was sla vlak voor het eten en niet vóór het bewaren, dan blijft hij droog in de koelkast.</p>

<h2>Kun je sla invriezen?</h2>
<p>Nee. Het Voedingscentrum noemt sla niet geschikt om in te vriezen: na het ontdooien worden de blaadjes slap en waterig. Spinazie en andere kookgroente zijn een ander verhaal, maar sla eet je het best vers.</p>

<h2>Slap of bedorven?</h2>
<p>Verlepte sla is niet meteen bedorven, zegt het Voedingscentrum. Slappe blaadjes knappen vaak weer op na een paar minuten in ijskoud water. Is de sla beschimmeld, slijmerig of ruikt hij afwijkend, gooi hem dan weg. Bij zakken sla na de TGT-datum beslist de datum.</p>

<h2>Tips om minder sla te verspillen</h2>
<ul>
  <li>Koop een krop in plaats van een zak als je hem niet binnen twee dagen opmaakt.</li>
  <li>Plan salades aan het begin van de week en bewaar steviger groente voor later.</li>
  <li>Zet zakken sla met hun TGT-datum in FreshGarant, dan raken ze niet vergeten achterin de koelkast.</li>
</ul>
""",
  "faq": [
   ("Hoe lang is een krop sla houdbaar?", "2 tot 5 dagen in de koelkast, volgens het Voedingscentrum."),
   ("Hoe lang is een zak sla houdbaar na openen?", "2 dagen, en nooit na de TGT-datum."),
   ("Kun je slappe sla nog eten?", "Ja, slap is niet bedorven. Een paar minuten in ijskoud water maakt hem vaak weer knapperig. Slijmerige, beschimmelde of vies ruikende sla gooi je weg."),
   ("Kun je sla invriezen?", "Nee, sla wordt na het invriezen slap en waterig."),
   ("Waarom bederft mijn sla zo snel?", "Naast appels, bananen of peren bederft sla sneller. Bewaar hem apart en houd de onderkant vochtig."),
  ],
  "related": ["tomatoes", "avocado", "strawberries"],
 },
},
# ─────────────────────────────── POTATOES ───────────────────────────────
{
 "key": "potatoes", "emoji": "🥔",
 "sources": ["vc_bewaarwijzer", "fsa_facts", "fsa_chill"],
 "en": {
  "slug": "how-long-do-potatoes-last", "name": "Potatoes",
  "title": "How Long Do Potatoes Last? Raw and Cooked",
  "desc": "Raw potatoes keep about a month in a cool, dark place. Cooked potatoes keep 2 days in the fridge and about 3 months frozen. Green spots and sprouts.",
  "h1": "How long do potatoes last?",
  "answer": "Raw potatoes keep <strong>about 1 month in a cool, dark, dry place</strong>, according to the Voedingscentrum. Cooked potatoes keep 2 days in the fridge and about 3 months in the freezer. Remove sprouts and cut away green parts generously before cooking. Raw potatoes are not suitable for freezing.",
  "table_head": ("", "How long", "Source"),
  "table": [
   ("Raw potatoes, cool dark place", "About 1 month", "Voedingscentrum"),
   ("Raw potatoes, freezer", "Not suitable (cook or parboil them first)", "Voedingscentrum · FSA"),
   ("Cooked potatoes, fridge", "2 days", "Voedingscentrum"),
   ("Cooked potatoes, freezer", "About 3 months", "Voedingscentrum"),
  ],
  "body": """
<h2>Where to store raw potatoes</h2>
<p>The Voedingscentrum advises storing potatoes in a dry, dark and cool place, where they keep about a month. In a warm spot they start to sprout; light turns them green. A cellar, a cool cupboard or a paper bag in a dark corner works well.</p>

<h2>Potatoes in the fridge? The sources differ</h2>
<p>This is a point where the two food safety bodies give different advice:</p>
<ul>
  <li><strong>The UK Food Standards Agency</strong> says you can store potatoes in the fridge or in a cool, dark, dry place. It refers to a study, reviewed by an expert committee, which found that keeping potatoes in a home fridge does not materially increase the sugars that form acrylamide when frying or roasting.</li>
  <li><strong>The Dutch Voedingscentrum</strong> says you can keep potatoes in the fridge if you have no cool, dark place, but only potatoes for boiling, not for frying or roasting, because more sugars form in the fridge that can turn into acrylamide.</li>
</ul>
<p>The cautious choice: a cool, dark cupboard first; the fridge if you have nothing better, ideally for potatoes you plan to boil.</p>

<h2>Sprouts and green spots</h2>
<p>Sprouted potatoes can still be eaten: remove the sprouts and cut off the spot. Green and damaged parts are different. The FSA explains that green, damaged and sprouted parts can contain high levels of natural toxins called glycoalkaloids, which can cause stomach pain, vomiting and diarrhoea. Poisoning is extremely rare, but cut green parts away generously. Storing potatoes cool, dark and dry prevents this.</p>

<h2>Cooked potatoes</h2>
<p>Leftover boiled potatoes keep 2 days in the fridge, according to the Voedingscentrum. Let them cool quickly, put them in a closed container and never leave them out of the fridge for more than 2 hours.</p>

<h2>Can you freeze potatoes?</h2>
<p>Not raw: the Voedingscentrum calls raw potatoes unsuitable for freezing. Cooked potatoes do freeze well, for about 3 months. The FSA adds that you can freeze cooked potatoes or potatoes parboiled for 5 minutes, and roast them straight from the freezer with a little oil, until steaming hot all the way through.</p>

<h2>How to tell if potatoes have gone off</h2>
<p>The Voedingscentrum names these signs: potatoes that are mouldy, dried out or rotten. Soft, wrinkly potatoes that are otherwise fine can still be used, for example for mash or soup.</p>

<h2>Tips to waste less potatoes</h2>
<ul>
  <li>Buy a smaller bag if you do not eat potatoes several times a week.</li>
  <li>Cook extra and use the leftovers for fried potatoes, a potato salad or a frittata.</li>
  <li>Parboil and freeze potatoes that are starting to sprout, ready for roasting.</li>
</ul>
""",
  "faq": [
   ("How long do raw potatoes last?", "About a month in a cool, dark, dry place, according to the Voedingscentrum."),
   ("Can you eat sprouted potatoes?", "Yes, remove the sprouts and cut away the spot. Cut green or damaged parts away generously."),
   ("Can you keep potatoes in the fridge?", "The FSA says yes. The Voedingscentrum says only for potatoes you boil, not for frying or roasting. A cool, dark cupboard is the safe first choice."),
   ("How long do cooked potatoes last in the fridge?", "2 days, in a closed container."),
   ("Can you freeze potatoes?", "Not raw. Cooked or parboiled potatoes freeze well for about 3 months."),
  ],
  "related": ["leftovers", "soup", "pasta"],
 },
 "nl": {
  "slug": "hoe-lang-zijn-aardappelen-houdbaar", "name": "Aardappelen",
  "title": "Hoe Lang Zijn Aardappelen Houdbaar? Rauw en Gekookt",
  "desc": "Rauwe aardappelen blijven zo'n maand goed op een koele, donkere plek. Gekookte aardappelen 2 dagen in de koelkast. Over groene plekken en uitlopers.",
  "h1": "Hoe lang zijn aardappelen houdbaar?",
  "answer": "Rauwe aardappelen blijven volgens het Voedingscentrum <strong>ongeveer 1 maand goed op een koele, donkere en droge plek</strong>. Gekookte aardappelen houd je 2 dagen in de koelkast en zo'n 3 maanden in de vriezer. Verwijder uitlopers en snijd groene plekken ruim weg. Rauwe aardappelen zijn niet geschikt om in te vriezen.",
  "table_head": ("", "Hoe lang", "Bron"),
  "table": [
   ("Rauwe aardappelen, koel en donker", "Ongeveer 1 maand", "Voedingscentrum"),
   ("Rauwe aardappelen, vriezer", "Niet geschikt (eerst koken of voorkoken)", "Voedingscentrum · FSA"),
   ("Gekookte aardappelen, koelkast", "2 dagen", "Voedingscentrum"),
   ("Gekookte aardappelen, vriezer", "Ongeveer 3 maanden", "Voedingscentrum"),
  ],
  "body": """
<h2>Waar bewaar je rauwe aardappelen?</h2>
<p>Het Voedingscentrum adviseert aardappelen op een droge, donkere en koele plek te bewaren; daar blijven ze ongeveer een maand goed. Op een warme plek gaan ze uitlopen, en door licht worden ze groen. Een kelder, een koel kastje of een papieren zak in een donkere hoek werkt goed.</p>

<h2>Aardappelen in de koelkast? De bronnen verschillen</h2>
<p>Hier geven twee voedselveiligheidsinstanties een ander advies:</p>
<ul>
  <li><strong>Het Voedingscentrum</strong> zegt dat je aardappelen in de koelkast kunt bewaren als je geen koele, donkere plek hebt, maar alleen aardappelen om te koken, niet om te frituren of bakken. In de koelkast ontstaan sneller suikers die bij frituren of bakken kunnen omzetten in de schadelijke stof acrylamide.</li>
  <li><strong>De Britse Food Standards Agency (FSA)</strong> zegt dat je aardappelen in de koelkast of op een koele, donkere plek kunt bewaren. Ze verwijst naar een onderzoek, beoordeeld door een deskundigencommissie, waaruit bleek dat bewaren in de koelkast thuis die suikers niet wezenlijk laat toenemen.</li>
</ul>
<p>De voorzichtige keuze: eerst een koel, donker kastje; de koelkast als je niets beters hebt, en dan het liefst voor aardappelen die je kookt.</p>

<h2>Uitlopers en groene plekken</h2>
<p>Uitgelopen aardappelen kun je nog eten als je de uitlopers verwijdert en het plekje eraf snijdt. Groene plekken snijd je ruim weg. Volgens de FSA kunnen groene, beschadigde en uitgelopen delen veel natuurlijke gifstoffen (glycoalkaloïden) bevatten, die buikpijn, braken en diarree kunnen geven. Vergiftiging is extreem zeldzaam, maar wegsnijden is verstandig. Koel, donker en droog bewaren voorkomt het.</p>

<h2>Gekookte aardappelen</h2>
<p>Gekookte aardappelen die over zijn, blijven volgens het Voedingscentrum 2 dagen goed in de koelkast. Laat ze snel afkoelen, bewaar ze in een afgesloten bakje en laat ze nooit langer dan 2 uur buiten de koelkast staan.</p>

<h2>Kun je aardappelen invriezen?</h2>
<p>Rauw niet: het Voedingscentrum noemt rauwe aardappelen niet geschikt om in te vriezen. Gekookte aardappelen kunnen wel, zo'n 3 maanden. De FSA voegt toe dat je ook 5 minuten voorgekookte aardappelen kunt invriezen en ze zo uit de vriezer met wat olie in de oven kunt bakken, tot ze door en door heet zijn.</p>

<h2>Hoe herken je bedorven aardappelen?</h2>
<p>Het Voedingscentrum noemt: de aardappelen zijn beschimmeld, uitgedroogd of verrot. Zachte, gerimpelde aardappelen die verder goed zijn, kun je nog gebruiken, bijvoorbeeld voor puree of soep.</p>

<h2>Tips om minder aardappelen te verspillen</h2>
<ul>
  <li>Koop een kleinere zak als je niet vaak aardappelen eet.</li>
  <li>Kook wat extra en maak van de rest gebakken aardappeltjes, aardappelsalade of een frittata.</li>
  <li>Kook aardappelen die beginnen uit te lopen voor en vries ze in, klaar om te bakken.</li>
</ul>
""",
  "faq": [
   ("Hoe lang zijn rauwe aardappelen houdbaar?", "Ongeveer een maand op een koele, donkere en droge plek, volgens het Voedingscentrum."),
   ("Kun je uitgelopen aardappelen nog eten?", "Ja, verwijder de uitlopers en snijd het plekje eraf. Groene of beschadigde delen snijd je ruim weg."),
   ("Mogen aardappelen in de koelkast?", "Volgens het Voedingscentrum alleen aardappelen om te koken, niet om te frituren of bakken. De FSA vindt de koelkast wel prima. Een koel, donker kastje is de veilige eerste keus."),
   ("Hoe lang zijn gekookte aardappelen houdbaar?", "2 dagen in de koelkast, in een afgesloten bakje."),
   ("Kun je aardappelen invriezen?", "Rauw niet. Gekookte of voorgekookte aardappelen kun je zo'n 3 maanden invriezen."),
  ],
  "related": ["leftovers", "soup", "pasta"],
 },
},
# ─────────────────────────────── PASTA ───────────────────────────────
{
 "key": "pasta", "emoji": "🍝",
 "sources": ["vc_bewaarwijzer", "vc_veilig", "fsa_chill", "fsa_cook"],
 "en": {
  "slug": "how-long-does-cooked-pasta-last", "name": "Cooked pasta",
  "title": "How Long Does Cooked Pasta Last in the Fridge?",
  "desc": "Cooked pasta keeps 2 days in the fridge and about 3 months in the freezer. Dry pasta lasts over a year. How to store, freeze and reheat pasta.",
  "h1": "How long does cooked pasta last in the fridge?",
  "answer": "Cooked pasta keeps <strong>2 days in the fridge</strong>, according to the Voedingscentrum, and about 3 months in the freezer. Cool it quickly and get it into the fridge within 2 hours. Dry, uncooked pasta keeps for longer than a year, and often up to a year past its best-before date.",
  "table_head": ("", "How long", "Source"),
  "table": [
   ("Cooked pasta, fridge", "2 days (48 hours)", "Voedingscentrum · FSA"),
   ("Cooked pasta, freezer", "About 3 months", "Voedingscentrum"),
   ("Cooked pasta, out of the fridge", "Into the fridge within 2 hours", "Voedingscentrum · FSA"),
   ("Dry pasta, pantry", "Longer than 1 year", "Voedingscentrum"),
   ("Dry pasta past best before", "Up to 1 year and possibly longer, if it looks fine and the pack is intact", "Voedingscentrum"),
  ],
  "body": """
<h2>How long is cooked pasta good?</h2>
<p>The Voedingscentrum gives 2 days in the fridge for cooked pasta, the same as for other leftovers. The FSA's general rule for leftovers matches: eat them within 48 hours, or freeze them if you think you will not manage that. Pasta with a sauce follows the shortest time of its ingredients, so pasta with fish or chicken should not be kept longer than the pasta itself.</p>

<h2>How to store cooked pasta</h2>
<ul>
  <li><strong>Cool it fast.</strong> The Voedingscentrum's rule for leftovers: let them cool quickly and never leave them out of the fridge for more than 2 hours. The FSA also says to get cooked food into the fridge within one to two hours.</li>
  <li><strong>Small portions cool faster.</strong> Spread the pasta out in shallow containers. Placing the container in a layer of cold water speeds this up.</li>
  <li><strong>Closed container.</strong> A drizzle of oil stops plain pasta from sticking together.</li>
  <li><strong>Write the date on it,</strong> so you know when the 2 days are up.</li>
</ul>

<h2>Can you freeze cooked pasta?</h2>
<p>Yes. The Voedingscentrum gives about 3 months in the freezer. Pasta in a sauce, like lasagne or a pasta bake, freezes best. Plain pasta can turn a bit soft; cook it slightly al dente if you plan to freeze it. Freeze it in portions, defrost in the fridge and reheat until steaming hot.</p>

<h2>Reheating pasta</h2>
<p>Leftover pasta can be eaten cold, for example as a pasta salad, if it was cooled and refrigerated properly. If you reheat it, the FSA advises heating it until steaming hot all the way through, and only once. Stir halfway in the microwave, because food can be hot at the edges and still cold in the middle. Dishes like lasagne heat more evenly in smaller portions.</p>

<h2>Dry pasta</h2>
<p>Uncooked dry pasta hardly spoils. The Voedingscentrum gives more than a year in a cool, dry, dark place, and says it is often fine up to a year past the best-before date, and possibly longer, as long as it looks normal and the pack is intact. Keep opened packs well closed to keep pantry insects out. Signs it has gone off: a musty or rancid smell, or insects.</p>

<h2>Tips to waste less pasta</h2>
<ul>
  <li>Weigh dry pasta before cooking: the Voedingscentrum recommends kitchen scales or a measuring cup for the right portions.</li>
  <li>Turn leftovers into a pasta salad, frittata or pasta bake the next day.</li>
  <li>Log leftovers in FreshGarant with a 2-day date, so they get eaten in time.</li>
</ul>
""",
  "faq": [
   ("How long does cooked pasta last in the fridge?", "2 days, according to the Voedingscentrum; the FSA's rule for leftovers is 48 hours."),
   ("Can you freeze cooked pasta?", "Yes, for about 3 months. Pasta in a sauce freezes best."),
   ("Can you eat cold pasta?", "Yes, if it was cooled quickly and kept in the fridge, within 2 days."),
   ("How often can you reheat pasta?", "Once, until steaming hot all the way through."),
   ("Does dry pasta expire?", "It hardly spoils. It often keeps up to a year past the best-before date if the pack is intact and it smells normal."),
  ],
  "related": ["rice", "leftovers", "mince"],
 },
 "nl": {
  "slug": "hoe-lang-is-gekookte-pasta-houdbaar", "name": "Gekookte pasta",
  "title": "Hoe Lang Is Gekookte Pasta Houdbaar in de Koelkast?",
  "desc": "Gekookte pasta blijft 2 dagen goed in de koelkast en zo'n 3 maanden in de vriezer. Droge pasta ruim een jaar. Zo bewaar, vries en warm je pasta op.",
  "h1": "Hoe lang is gekookte pasta houdbaar in de koelkast?",
  "answer": "Gekookte pasta blijft volgens het Voedingscentrum <strong>2 dagen goed in de koelkast</strong> en zo'n 3 maanden in de vriezer. Laat hem snel afkoelen en zet hem binnen 2 uur in de koelkast. Droge, ongekookte pasta blijft langer dan een jaar goed, en vaak nog tot een jaar na de THT-datum.",
  "table_head": ("", "Hoe lang", "Bron"),
  "table": [
   ("Gekookte pasta, koelkast", "2 dagen", "Voedingscentrum"),
   ("Gekookte pasta, vriezer", "Ongeveer 3 maanden", "Voedingscentrum"),
   ("Gekookte pasta, buiten de koelkast", "Binnen 2 uur in de koelkast", "Voedingscentrum"),
   ("Droge pasta, voorraadkast", "Langer dan 1 jaar", "Voedingscentrum"),
   ("Droge pasta na de THT-datum", "Tot 1 jaar en mogelijk langer, als hij er goed uitziet en de verpakking heel is", "Voedingscentrum"),
  ],
  "body": """
<h2>Hoe lang is gekookte pasta goed?</h2>
<p>Het Voedingscentrum houdt voor gekookte pasta 2 dagen in de koelkast aan, net als voor andere restjes. Ook de Britse Food Standards Agency (FSA) zegt: eet restjes binnen 48 uur, of vries ze in als dat niet lukt. Pasta met saus houdt zich aan het ingrediënt met de kortste houdbaarheid; pasta met vis of kip bewaar je dus niet langer dan de pasta zelf.</p>

<h2>Zo bewaar je gekookte pasta</h2>
<ul>
  <li><strong>Laat hem snel afkoelen.</strong> De regel van het Voedingscentrum voor restjes: snel afkoelen en nooit langer dan 2 uur buiten de koelkast.</li>
  <li><strong>Kleine porties koelen sneller af.</strong> Verdeel de pasta over ondiepe bakjes. Zet het bakje in een laagje koud water, dan gaat het nog sneller.</li>
  <li><strong>Afgesloten bakje.</strong> Een scheutje olie voorkomt dat kale pasta aan elkaar plakt.</li>
  <li><strong>Zet de datum erop,</strong> dan weet je wanneer de 2 dagen om zijn.</li>
</ul>

<h2>Kun je gekookte pasta invriezen?</h2>
<p>Ja. Volgens het Voedingscentrum blijft gekookte pasta zo'n 3 maanden goed in de vriezer. Pasta in saus, zoals lasagne of een ovenschotel, vriest het best in. Kale pasta kan wat zacht worden; kook hem iets beetgaarder als je hem wilt invriezen. Vries in porties in, ontdooi in de koelkast en warm door en door op.</p>

<h2>Pasta opwarmen</h2>
<p>Pasta die over is kun je koud eten, bijvoorbeeld als pastasalade, als hij goed is afgekoeld en in de koelkast heeft gestaan. Warm je hem op, dan adviseert het Voedingscentrum restjes door en door te verhitten tot ze stomend heet zijn, en liever niet een tweede keer. Schep om in de magnetron: soms blijven er delen koud.</p>

<h2>Droge pasta</h2>
<p>Ongekookte droge pasta kan nauwelijks bederven. Het Voedingscentrum houdt langer dan een jaar aan op een koele, droge en donkere plek, en zegt dat hij vaak nog tot een jaar na de THT-datum goed is, en mogelijk langer, zolang hij er normaal uitziet en de verpakking heel is. Sluit aangebroken pakken goed af tegen ongedierte. Tekenen van bederf: een muffe of ranzige geur, of insecten.</p>

<h2>Tips om minder pasta te verspillen</h2>
<ul>
  <li>Weeg droge pasta af: het Voedingscentrum raadt een keukenweegschaal of maatbeker aan voor de juiste porties.</li>
  <li>Maak van restjes de volgende dag een pastasalade, frittata of ovenschotel.</li>
  <li>Zet restjes in FreshGarant met een houdbaarheid van 2 dagen, dan worden ze op tijd opgegeten.</li>
</ul>
""",
  "faq": [
   ("Hoe lang is gekookte pasta houdbaar in de koelkast?", "2 dagen, volgens het Voedingscentrum."),
   ("Kun je gekookte pasta invriezen?", "Ja, zo'n 3 maanden. Pasta in saus vriest het best in."),
   ("Kun je koude pasta eten?", "Ja, als hij snel is afgekoeld en in de koelkast heeft gestaan, binnen 2 dagen."),
   ("Hoe vaak mag je pasta opwarmen?", "Liefst één keer, door en door heet."),
   ("Kan droge pasta bederven?", "Nauwelijks. Hij is vaak nog tot een jaar na de THT-datum goed als de verpakking heel is en hij normaal ruikt."),
  ],
  "related": ["rice", "leftovers", "mince"],
 },
},
# ─────────────────────────────── SOUP ───────────────────────────────
{
 "key": "soup", "emoji": "🍲",
 "sources": ["vc_bewaarwijzer", "vc_veilig", "vc_verhitten", "fsa_chill", "fsa_cook"],
 "en": {
  "slug": "how-long-does-soup-last", "name": "Soup",
  "title": "How Long Does Homemade Soup Last in the Fridge?",
  "desc": "Homemade soup keeps 2 days in the fridge and about 3 months in the freezer. How to cool soup quickly, freeze it in portions and reheat it safely.",
  "h1": "How long does homemade soup last in the fridge?",
  "answer": "Homemade soup keeps <strong>2 days in the fridge</strong>, according to the Voedingscentrum, and about 3 months in the freezer. Cool it quickly, get it into the fridge within 2 hours and reheat it until steaming hot, only once. Unopened shop-bought soup can often be eaten up to 2 months past its best-before date.",
  "table_head": ("", "How long", "Source"),
  "table": [
   ("Homemade soup, fridge", "2 days (48 hours)", "Voedingscentrum · FSA"),
   ("Homemade soup, freezer", "About 3 months", "Voedingscentrum"),
   ("Out of the fridge", "Into the fridge within 2 hours", "Voedingscentrum · FSA"),
   ("Reheating", "Once, until steaming hot", "FSA · Voedingscentrum"),
   ("Shop-bought soup past best before (unopened)", "Up to 2 months and possibly longer, if it looks fine and the pack is intact", "Voedingscentrum"),
  ],
  "body": """
<h2>How long is homemade soup good?</h2>
<p>The Voedingscentrum gives 2 days in the fridge for homemade soup, whether it is a thick soup with meat and vegetables or a clear chicken soup. The FSA's rule for leftovers matches: eat them within 48 hours or freeze them. That makes soup one of the best dishes to cook in bulk, as long as you freeze what you will not eat within two days.</p>

<h2>Cool a big pan of soup quickly</h2>
<p>A large pan of soup holds its heat for hours, and bacteria can grow while it slowly cools. The FSA calls the range between 8 and 63°C the danger zone. Both sources advise cooling food quickly and getting it into the fridge within two hours.</p>
<ul>
  <li><strong>Divide it into smaller containers.</strong> Small portions cool much faster than one big pan.</li>
  <li><strong>Use cold water.</strong> The Voedingscentrum's tip: place the pan or container in a layer of cold water.</li>
  <li><strong>Do not put a hot pan straight into the fridge;</strong> the FSA advises cooling cooked food first, then refrigerating it within one to two hours.</li>
</ul>

<h2>Can you freeze soup?</h2>
<p>Yes, soup freezes very well: the Voedingscentrum gives about 3 months. Freeze it in portions, in containers or freezer bags laid flat, and leave some room because liquid expands. Write the name and date on it. Soups with pasta or potato pieces can turn a bit soft; you can also freeze the soup base and add those when reheating.</p>

<h2>Reheating soup</h2>
<p>Heat soup until it is steaming hot all the way through, stirring well. The Voedingscentrum advises against reheating leftovers a second time, because each time the food passes through room temperature, bacteria get another chance to grow. So only heat up what you will eat now, and leave the rest in the fridge or freezer.</p>

<h2>Shop-bought soup</h2>
<p>For unopened soup in a pouch, tin or carton, the Voedingscentrum says it can often be eaten up to 2 months after its best-before date, and possibly longer, if it still looks fine and the packaging is intact. Bulging tins or pouches go in the bin. Once opened, shop-bought soup counts as a leftover: 2 days in the fridge. Fresh chilled soups usually carry a use-by date; then the date decides.</p>

<h2>How to tell if soup has gone off</h2>
<p>A sour smell, bubbles or fizzing in soup that is not boiling, or mould mean the soup has spoiled. But bacteria that cause food poisoning cannot always be smelled, so go by time: more than 2 days in the fridge means it goes.</p>

<h2>Tips to waste less with soup</h2>
<ul>
  <li>Soup is the perfect home for vegetables that are past their best.</li>
  <li>Freeze single portions for easy lunches.</li>
  <li>Log soup in FreshGarant when you put it in the fridge or freezer, so you know how long it has been there.</li>
</ul>
""",
  "faq": [
   ("How long does homemade soup last in the fridge?", "2 days, according to the Voedingscentrum; the FSA's rule for leftovers is 48 hours."),
   ("Can you freeze soup?", "Yes, for about 3 months. Freeze it in portions and leave room for it to expand."),
   ("How do you cool soup quickly?", "Divide it into smaller containers and place the pan or containers in cold water. Get it into the fridge within 2 hours."),
   ("Can you reheat soup more than once?", "Better not. Heat only what you will eat, until steaming hot."),
   ("Can you eat shop-bought soup past the date?", "Unopened soup with a best-before date often for up to 2 months if the pack is intact. Fresh soup with a use-by date: no."),
  ],
  "related": ["leftovers", "chicken", "potatoes"],
 },
 "nl": {
  "slug": "hoe-lang-is-soep-houdbaar", "name": "Soep",
  "title": "Hoe Lang Is Zelfgemaakte Soep Houdbaar in de Koelkast?",
  "desc": "Zelfgemaakte soep blijft 2 dagen goed in de koelkast en zo'n 3 maanden in de vriezer. Zo laat je soep snel afkoelen, vries je hem in en warm je op.",
  "h1": "Hoe lang is zelfgemaakte soep houdbaar in de koelkast?",
  "answer": "Zelfgemaakte soep blijft volgens het Voedingscentrum <strong>2 dagen goed in de koelkast</strong> en zo'n 3 maanden in de vriezer. Laat hem snel afkoelen, zet hem binnen 2 uur in de koelkast en warm hem door en door op, het liefst maar één keer. Ongeopende soep uit de winkel is vaak nog tot 2 maanden na de THT-datum goed.",
  "table_head": ("", "Hoe lang", "Bron"),
  "table": [
   ("Zelfgemaakte soep, koelkast", "2 dagen", "Voedingscentrum"),
   ("Zelfgemaakte soep, vriezer", "Ongeveer 3 maanden", "Voedingscentrum"),
   ("Buiten de koelkast", "Binnen 2 uur in de koelkast", "Voedingscentrum"),
   ("Opwarmen", "Door en door heet, liefst één keer", "Voedingscentrum"),
   ("Soep uit de winkel na de THT-datum (gesloten)", "Tot 2 maanden en mogelijk langer, als hij er goed uitziet en de verpakking heel is", "Voedingscentrum"),
  ],
  "body": """
<h2>Hoe lang is zelfgemaakte soep goed?</h2>
<p>Het Voedingscentrum houdt voor zelfgemaakte soep 2 dagen in de koelkast aan, of het nu gaat om gebonden soep met vlees en groenten of om heldere kippensoep. Ook de Britse Food Standards Agency (FSA) zegt: eet restjes binnen 48 uur of vries ze in. Soep is daardoor ideaal om in grote hoeveelheden te maken, zolang je invriest wat je niet binnen twee dagen opeet.</p>

<h2>Een grote pan soep snel laten afkoelen</h2>
<p>Een grote pan soep blijft urenlang warm, en terwijl hij langzaam afkoelt kunnen bacteriën groeien. Daarom adviseert het Voedingscentrum restjes snel te laten afkoelen en nooit langer dan 2 uur buiten de koelkast te laten staan.</p>
<ul>
  <li><strong>Verdeel de soep over kleinere bakjes.</strong> Kleine porties koelen veel sneller af dan één grote pan.</li>
  <li><strong>Gebruik koud water.</strong> De tip van het Voedingscentrum: zet de pan of het bakje in een laagje koud water.</li>
  <li><strong>Laat soep eerst afkoelen</strong> voordat hij de koelkast of vriezer in gaat.</li>
</ul>

<h2>Kun je soep invriezen?</h2>
<p>Ja, soep vriest uitstekend in: het Voedingscentrum houdt zo'n 3 maanden aan. Vries in porties in, in bakjes of plat in diepvrieszakken, en laat wat ruimte omdat vloeistof uitzet. Zet de naam en datum erop. Soep met pasta of stukjes aardappel kan wat zacht worden; je kunt ook de bouillon of basis invriezen en die bij het opwarmen toevoegen.</p>

<h2>Soep opwarmen</h2>
<p>Warm soep door en door op tot hij stomend heet is, en roer goed. Het Voedingscentrum raadt af kliekjes een tweede keer op te warmen, omdat het eten dan meerdere keren op kamertemperatuur komt en bacteriën kunnen uitgroeien. Warm dus alleen op wat je nu eet, en laat de rest in de koelkast of vriezer.</p>

<h2>Soep uit de winkel</h2>
<p>Voor ongeopende soep in zak, blik of pak zegt het Voedingscentrum dat je hem vaak nog tot 2 maanden na de THT-datum kunt eten, en mogelijk langer, als hij er goed uitziet en de verpakking heel is. Bolle blikken of zakken gooi je weg. Is de soep open, dan geldt hij als restje: 2 dagen in de koelkast. Op verse soep uit het koelvak staat meestal een TGT-datum; dan beslist de datum.</p>

<h2>Hoe herken je bedorven soep?</h2>
<p>Een zure lucht, belletjes of bruisen in soep die niet kookt, of schimmel: dan is de soep bedorven. Maar bacteriën die je ziek maken ruik je niet altijd, dus ga uit van de tijd: langer dan 2 dagen in de koelkast betekent weggooien.</p>

<h2>Tips om minder te verspillen met soep</h2>
<ul>
  <li>Soep is de perfecte bestemming voor groente die over zijn beste tijd is.</li>
  <li>Vries losse porties in voor een makkelijke lunch.</li>
  <li>Zet soep in FreshGarant als hij de koelkast of vriezer in gaat, dan weet je hoe lang hij er al staat.</li>
</ul>
""",
  "faq": [
   ("Hoe lang is zelfgemaakte soep houdbaar in de koelkast?", "2 dagen, volgens het Voedingscentrum."),
   ("Kun je soep invriezen?", "Ja, zo'n 3 maanden. Vries in porties in en laat ruimte omdat soep uitzet."),
   ("Hoe laat je soep snel afkoelen?", "Verdeel hem over kleinere bakjes en zet de pan of bakjes in koud water. Binnen 2 uur in de koelkast."),
   ("Mag je soep vaker opwarmen?", "Liever niet. Warm alleen op wat je eet, door en door heet."),
   ("Kun je soep uit de winkel na de datum nog eten?", "Gesloten soep met een THT-datum vaak nog tot 2 maanden, als de verpakking heel is. Verse soep met een TGT-datum niet."),
  ],
  "related": ["leftovers", "chicken", "potatoes"],
 },
},
# ─────────────────────────────── LEFTOVERS ───────────────────────────────
{
 "key": "leftovers", "emoji": "🥡",
 "sources": ["vc_bewaarwijzer", "vc_veilig", "vc_verhitten", "fsa_chill", "fsa_cook"],
 "en": {
  "slug": "how-long-do-leftovers-last", "name": "Leftovers",
  "title": "How Long Do Leftovers Last in the Fridge?",
  "desc": "Leftovers keep 2 days (48 hours) in the fridge and about 3 months in the freezer. Cool them fast, refrigerate within 2 hours, reheat once.",
  "h1": "How long do leftovers last in the fridge?",
  "answer": "Leftovers keep <strong>2 days in the fridge</strong>: the Voedingscentrum gives 2 days and the FSA says eat them within 48 hours. In the freezer they keep about 3 months. Cool leftovers quickly, get them into the fridge within 2 hours, and reheat them only once, until steaming hot. Rice is the exception: eat it within 24 hours.",
  "table_head": ("", "How long", "Source"),
  "table": [
   ("Leftovers, fridge", "2 days (48 hours)", "Voedingscentrum · FSA"),
   ("Leftovers, freezer", "About 3 months", "Voedingscentrum"),
   ("Out of the fridge", "Into the fridge within 2 hours", "Voedingscentrum · FSA"),
   ("Reheating", "Once only, steaming hot all the way through", "FSA"),
   ("Cooked rice", "Within 24 hours (FSA) · max. 2 days (Voedingscentrum)", "FSA · Voedingscentrum"),
  ],
  "body": """
<h2>The 2-day rule</h2>
<p>For most cooked leftovers, both sources agree: the Voedingscentrum gives 2 days in the fridge, and the FSA says to eat leftovers within 48 hours or freeze them if you think you will not manage that. The fridge slows bacteria down, but does not stop them. If you will not eat it within two days, freeze it on day one, not on day two.</p>

<h2>Step 1: cool quickly</h2>
<p>The FSA calls the range between 8 and 63°C the danger zone: at those temperatures bacteria grow fastest. So leftovers should not stand on the stove or counter for hours.</p>
<ul>
  <li><strong>Within 2 hours into the fridge.</strong> The Voedingscentrum says never leave leftovers out of the fridge for more than 2 hours; the FSA says within one to two hours.</li>
  <li><strong>Divide into small portions.</strong> They cool much faster than a full pan.</li>
  <li><strong>Use cold water.</strong> Place the pan or container in a layer of cold water.</li>
  <li><strong>Cover them</strong> and put the date on the container.</li>
</ul>

<h2>Step 2: store them cold</h2>
<p>The FSA advises a fridge between 0 and 5°C, the Voedingscentrum 4°C. Keep cooked leftovers separate from raw meat, and preferably above it, so nothing can drip onto them.</p>

<h2>Step 3: reheat once, until steaming hot</h2>
<p>Reheat leftovers until they are steaming hot all the way through, not just warm. The FSA advises reheating only once, because every temperature change gives bacteria another chance to grow. The Voedingscentrum also advises against reheating leftovers a second time. In the microwave, stir halfway: food can be hot at the edges and still cold in the middle. Leftovers can also be eaten cold, if they were cooked properly, cooled and refrigerated within two hours.</p>

<h2>Freezing leftovers</h2>
<p>A freezer works like a pause button, says the FSA: most bacteria cannot grow in it. The Voedingscentrum gives about 3 months for leftovers in the freezer at −18°C. Freeze them as soon as possible, in portions, and label them with name and date. Defrost in the fridge and use them within 24 hours of defrosting. Food you cooked from frozen ingredients can be frozen again once cooked, but reheat it only once after that.</p>

<h2>Exceptions to keep in mind</h2>
<ul>
  <li><strong>Rice:</strong> the FSA advises eating it within 24 hours, because of Bacillus cereus.</li>
  <li><strong>Takeaway food:</strong> it may already have been reheated, so eat it soon and do not reheat it again.</li>
  <li><strong>Vulnerable people</strong> (pregnant people, young children, older people, people with a weakened immune system) should be extra strict with timing.</li>
</ul>

<h2>Tips to waste fewer leftovers</h2>
<ul>
  <li>Cook the right amount, or plan the leftovers as tomorrow's lunch.</li>
  <li>Freeze single portions straight away for busy evenings.</li>
  <li>Log leftovers in FreshGarant with a 2-day date, so they do not get lost at the back of the fridge.</li>
</ul>
""",
  "faq": [
   ("How long do leftovers last in the fridge?", "2 days: the Voedingscentrum says 2 days and the FSA 48 hours."),
   ("Can you eat leftovers after 3 days?", "No. That is longer than both sources advise. Freeze leftovers on day one if you will not eat them in time."),
   ("Can you put hot food in the fridge?", "Cool it first, but get it into the fridge within 1 to 2 hours. Dividing it into small portions helps."),
   ("How many times can you reheat leftovers?", "Once, until steaming hot all the way through."),
   ("How long can you freeze leftovers?", "About 3 months, according to the Voedingscentrum. Defrost in the fridge and use within 24 hours."),
  ],
  "related": ["rice", "soup", "pasta"],
 },
 "nl": {
  "slug": "hoe-lang-zijn-restjes-houdbaar", "name": "Restjes",
  "title": "Hoe Lang Zijn Restjes Houdbaar in de Koelkast?",
  "desc": "Restjes blijven 2 dagen goed in de koelkast en zo'n 3 maanden in de vriezer. Snel afkoelen, binnen 2 uur in de koelkast en liefst één keer opwarmen.",
  "h1": "Hoe lang zijn restjes houdbaar in de koelkast?",
  "answer": "Restjes blijven volgens het Voedingscentrum <strong>2 dagen goed in de koelkast</strong>, afgedekt. Wil je ze langer bewaren, vries ze dan in: zo'n 3 maanden. Laat restjes snel afkoelen, zet ze binnen 2 uur in de koelkast en warm ze door en door op, liefst maar één keer. Rijst is een uitzondering: de Britse FSA adviseert die binnen 24 uur te eten.",
  "table_head": ("", "Hoe lang", "Bron"),
  "table": [
   ("Restjes, koelkast", "2 dagen", "Voedingscentrum"),
   ("Restjes, vriezer", "Ongeveer 3 maanden", "Voedingscentrum"),
   ("Buiten de koelkast", "Nooit langer dan 2 uur", "Voedingscentrum"),
   ("Opwarmen", "Door en door heet, liefst één keer", "Voedingscentrum"),
   ("Gekookte rijst", "Max. 2 dagen · Brits advies: binnen 24 uur", "Voedingscentrum · FSA"),
  ],
  "body": """
<h2>De 2-dagenregel</h2>
<p>Het Voedingscentrum is duidelijk: bewaar restjes maximaal 2 dagen afgedekt in de koelkast, en vries ze in als je ze langer wilt bewaren. De Britse Food Standards Agency (FSA) zegt hetzelfde: eet restjes binnen 48 uur. De koelkast remt bacteriën af, maar stopt ze niet. Eet je het niet binnen twee dagen op, vries het dan op dag één in, niet op dag twee.</p>

<h2>Stap 1: snel afkoelen</h2>
<p>Bacteriën groeien het snelst tussen ongeveer 8 en 63 °C, de gevarenzone volgens de FSA. Restjes horen dus niet urenlang op het fornuis of aanrecht te staan.</p>
<ul>
  <li><strong>Binnen 2 uur in de koelkast.</strong> Laat kliekjes niet langer dan 2 uur buiten de koelkast staan, zegt het Voedingscentrum.</li>
  <li><strong>Verdeel in kleine porties.</strong> Die koelen veel sneller af dan een volle pan.</li>
  <li><strong>Gebruik koud water.</strong> Kliekjes koelen sneller af als je het bakje of de pan in een laagje koud water zet.</li>
  <li><strong>Dek ze af</strong> en zet de datum op het bakje.</li>
</ul>

<h2>Stap 2: koud bewaren</h2>
<p>Zet je koelkast op 4 °C, adviseert het Voedingscentrum. Bewaar bereide restjes apart van rauw vlees, en liefst erboven, zodat er niets op kan lekken.</p>

<h2>Stap 3: door en door opwarmen</h2>
<p>Verhit restjes en kliekjes altijd door en door tot ze stomend heet zijn: daarmee dood je de bacteriën. Schep goed om tijdens het verhitten, want in de magnetron blijven soms delen koud. Warm kliekjes liever niet voor een tweede keer op, zegt het Voedingscentrum: dan komt het eten meerdere keren op kamertemperatuur en kunnen bacteriën uitgroeien. Restjes mag je ook koud eten, als ze goed gaar waren, snel zijn afgekoeld en binnen twee uur in de koelkast stonden.</p>

<h2>Restjes invriezen</h2>
<p>Een vriezer werkt als een pauzeknop, zegt de FSA: de meeste bacteriën kunnen er niet groeien. Het Voedingscentrum houdt voor restjes zo'n 3 maanden in de vriezer aan, op ten minste −18 °C. Vries ze zo snel mogelijk in, in kleine porties, en zet als geheugensteuntje de datum op het bakje. Ontdooi in de koelkast en gebruik ze binnen 24 uur na het ontdooien.</p>

<h2>Uitzonderingen om te onthouden</h2>
<ul>
  <li><strong>Rijst:</strong> de FSA adviseert gekookte rijst binnen 24 uur te eten, vanwege de bacterie Bacillus cereus.</li>
  <li><strong>Afhaaleten:</strong> dat kan al eens opgewarmd zijn. Eet het snel op en warm het niet nog eens op.</li>
  <li><strong>Kwetsbare mensen</strong> (zwangeren, jonge kinderen, ouderen, mensen met een verminderde weerstand) zijn beter extra streng met de tijd.</li>
</ul>

<h2>Tips om minder restjes te verspillen</h2>
<ul>
  <li>Kook de juiste hoeveelheid, of plan de restjes als lunch voor morgen.</li>
  <li>Vries losse porties meteen in voor drukke avonden.</li>
  <li>Zet restjes in FreshGarant met een houdbaarheid van 2 dagen, dan raken ze niet zoek achterin de koelkast.</li>
</ul>
""",
  "faq": [
   ("Hoe lang zijn restjes houdbaar in de koelkast?", "Maximaal 2 dagen, afgedekt, volgens het Voedingscentrum."),
   ("Kun je restjes na 3 dagen nog eten?", "Nee. Dat is langer dan het Voedingscentrum en de FSA adviseren. Vries restjes op dag één in als je ze niet op tijd opeet."),
   ("Mag warm eten in de koelkast?", "Laat het eerst afkoelen, maar zet het binnen 2 uur in de koelkast. Kleine porties en koud water helpen."),
   ("Hoe vaak mag je restjes opwarmen?", "Liefst één keer, door en door heet."),
   ("Hoe lang kun je restjes invriezen?", "Zo'n 3 maanden, volgens het Voedingscentrum. Ontdooi in de koelkast en gebruik ze binnen 24 uur."),
  ],
  "related": ["rice", "soup", "pasta"],
 },
},
]

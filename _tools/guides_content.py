"""Content for the food storage guides (/guides/ and /nl/gidsen/).

Every number must come from a source listed in SOURCES and be checked on the
source page. When sources differ, show both and advise the safer one.
Text is HTML; build_guides.py turns it into pages.
"""

CHECKED = {"en": "16 November 2026", "nl": "16 november 2026", "iso": "2026-11-16"}

SOURCES = {
    "fsa_facts": {
        "url": "https://www.gov.uk/government/publications/home-food-fact-checker/home-food-fact-checker",
        "en": "Food Standards Agency (UK): Home food fact checker",
        "nl": "Food Standards Agency (VK): Home food fact checker",
    },
    "fsa_chill": {
        "url": "https://www.gov.uk/government/publications/how-to-chill-freeze-and-defrost-food-safely/how-to-chill-freeze-and-defrost-food-safely",
        "en": "Food Standards Agency (UK): How to chill, freeze and defrost food safely",
        "nl": "Food Standards Agency (VK): How to chill, freeze and defrost food safely",
    },
    "fsa_cook": {
        "url": "https://www.gov.uk/government/publications/cooking-your-food/cooking-your-food",
        "en": "Food Standards Agency (UK): Cooking your food",
        "nl": "Food Standards Agency (VK): Cooking your food",
    },
    "fsa_burgers": {
        "url": "https://www.gov.uk/government/publications/burgers/burgers",
        "en": "Food Standards Agency (UK): Burgers",
        "nl": "Food Standards Agency (VK): Burgers",
    },
    "fsa_campy": {
        "url": "https://www.gov.uk/government/publications/campylobacter/campylobacter",
        "en": "Food Standards Agency (UK): Campylobacter",
        "nl": "Food Standards Agency (VK): Campylobacter",
    },
    "vc_bewaarwijzer": {
        "url": "https://www.voedingscentrum.nl/nl/thema/kopen-koken-bewaren/eten-bewaren.aspx",
        "en": "Voedingscentrum (Netherlands Nutrition Centre): Bewaarwijzer storage guide",
        "nl": "Voedingscentrum: Bewaarwijzer",
    },
    "vc_veilig": {
        "url": "https://www.voedingscentrum.nl/nl/veilig-eten-voedselinfectie-voorkomen/veilig-bewaren.aspx",
        "en": "Voedingscentrum: Veilig bewaren (safe storage)",
        "nl": "Voedingscentrum: Veilig bewaren",
    },
    "vc_verhitten": {
        "url": "https://www.voedingscentrum.nl/nl/veilig-eten-voedselinfectie-voorkomen/verhitten.aspx",
        "en": "Voedingscentrum: Veilig verhitten (safe heating)",
        "nl": "Voedingscentrum: Veilig verhitten",
    },
    "vc_ontdooien": {
        "url": "https://www.voedingscentrum.nl/nl/gezonde-recepten/kookhulp/ontdooien-hoe-ontdooi-ik-vlees-kip-gehakt-vis.aspx",
        "en": "Voedingscentrum: Hoe ontdooi ik? (defrosting)",
        "nl": "Voedingscentrum: Hoe ontdooi ik?",
    },
}

# Related reading from the blog (shown under "Related guides" until more
# guides exist).
BLOG_RELATED = {
    "en": [("/blog/how-long-does-food-last-in-the-fridge.html", "How long does food last in the fridge? (chart)"),
           ("/blog/what-food-can-you-freeze.html", "What food can you freeze?"),
           ("/blog/best-before-vs-use-by.html", "Best before vs use by: what's the difference?")],
    "nl": [("/nl/blog/hoe-lang-houdbaar-koelkast.html", "Hoe lang is eten houdbaar in de koelkast? (tabel)"),
           ("/nl/blog/wat-kun-je-invriezen.html", "Wat kun je invriezen?"),
           ("/nl/blog/tht-tgt-verschil.html", "THT en TGT: wat is het verschil?")],
}

GUIDES = [
# ─────────────────────────────── COOKED RICE ───────────────────────────────
{
 "key": "rice", "emoji": "🍚",
 "sources": ["fsa_facts", "fsa_chill", "vc_bewaarwijzer", "vc_veilig", "vc_verhitten"],
 "en": {
  "slug": "how-long-does-cooked-rice-last",
  "name": "Cooked rice",
  "title": "How Long Does Cooked Rice Last in the Fridge?",
  "desc": "Cooked rice keeps 1 day in the fridge (FSA) and about 3 months in the freezer. How to cool, store, freeze and reheat rice safely.",
  "h1": "How long does cooked rice last in the fridge?",
  "answer": "Eat cooked rice <strong>within 24 hours</strong>, as the UK Food Standards Agency advises; the Dutch Voedingscentrum gives a maximum of 2 days. Cool it and put it in the fridge within an hour, reheat it only once, and make sure it is steaming hot. In the freezer, cooked rice keeps about 3 months.",
  "table_head": ("", "How long", "Source"),
  "table": [
   ("Cooked rice, fridge", "1 day (24 hours) · max. 2 days", "FSA · Voedingscentrum"),
   ("Cooked rice, freezer", "About 3 months", "Voedingscentrum"),
   ("Cooked rice, room temperature", "Into the fridge within 1 hour · never more than 2 hours out", "FSA · Voedingscentrum"),
   ("Reheating", "Once only, steaming hot all the way through", "FSA"),
   ("Uncooked white rice, pantry", "Longer than 1 year; often fine up to 1 year past the best-before date if it looks normal", "Voedingscentrum"),
  ],
  "body": """
<h2>Why cooked rice needs extra care</h2>
<p>Uncooked rice can contain spores of a bacterium called <strong>Bacillus cereus</strong>. According to the Food Standards Agency, these spores can survive cooking. The longer cooked rice stays at room temperature, the more likely it is that the bacteria or their toxins make the rice unsafe to eat.</p>
<p>That is also why reheating does not fix rice that has been left out. As the FSA puts it, it is not the reheating that causes the problem, but the way the rice was stored before it was reheated.</p>

<h2>How to store cooked rice safely</h2>
<ol>
  <li><strong>Cool it fast.</strong> Chill leftover rice as quickly as possible, ideally within one hour. Do not leave it to cool in the rice cooker, steamer or pan.</li>
  <li><strong>Use small portions.</strong> Dividing rice into smaller, shallow containers helps it cool faster. Placing the container in a little cold water speeds this up even more.</li>
  <li><strong>Cover it and put it in the fridge.</strong> The FSA advises a fridge between 0 and 5°C; the Voedingscentrum advises setting it to 4°C.</li>
  <li><strong>Write the date on it.</strong> Then you know exactly when it has to be eaten.</li>
</ol>

<h2>How long is cooked rice good in the fridge?</h2>
<p>The UK Food Standards Agency says to keep rice in the fridge for no more than one day before you eat or reheat it. The Dutch Voedingscentrum lists a maximum of 2 days for cooked rice. If you want the safest option, eat it the next day at the latest.</p>
<p>Cold rice is fine to eat, for example in a rice salad, as long as it was cooled quickly and kept in the fridge.</p>

<h2>Can you freeze cooked rice?</h2>
<p>Yes. Freezing is the best way to keep rice longer than a day. The FSA advises getting rice into the freezer within an hour of cooking, so bacteria cannot multiply and produce toxins. Freeze it in portions so it cools quickly and you only defrost what you need.</p>
<p>The Voedingscentrum gives about 3 months for cooked rice in the freezer, which should be set to −18°C. Defrost frozen rice in the fridge, then reheat it until it is steaming hot and eat it straight away.</p>

<h2>How to reheat rice</h2>
<ul>
  <li><strong>Only once.</strong> Never reheat rice more than once.</li>
  <li><strong>Steaming hot all the way through.</strong> Stir halfway in the microwave: food can be hot at the edges and still cold in the middle.</li>
  <li><strong>Takeaway rice needs extra care.</strong> Restaurants sometimes cook rice in advance and reheat it before serving, so eat takeaway rice soon after it arrives and do not reheat it again.</li>
</ul>

<h2>How to tell if rice has gone off</h2>
<p>Rice that smells sour, feels slimy or shows mould has clearly spoiled, so throw it away. But the reverse is not true: the bacteria and toxins that cause food poisoning cannot be seen or smelled. Rice that looks and smells fine can still be unsafe if it was left out too long or kept too long. Go by time, not by smell.</p>

<h2>Tips to waste less rice</h2>
<ul>
  <li><strong>Cook the right amount.</strong> The Voedingscentrum recommends a measuring cup or kitchen scales to get portions right.</li>
  <li><strong>Freeze the leftovers straight away</strong> instead of putting them in the fridge "for later".</li>
  <li><strong>Plan a rice dish for the next day,</strong> such as fried rice or a rice salad, so the leftovers get used within the safe window.</li>
  <li><strong>Log it in FreshGarant</strong> with a 1-day date, so you get a reminder before it has to go.</li>
</ul>
""",
  "faq": [
   ("Can you eat cooked rice the next day?", "Yes, if it was cooled quickly (ideally within an hour) and kept in the fridge. The FSA advises eating it within 24 hours; the Voedingscentrum gives a maximum of 2 days."),
   ("Can you reheat rice twice?", "No. The FSA advises never reheating rice more than once, and making sure it is steaming hot all the way through when you do."),
   ("Is 3-day-old rice safe to eat?", "No. Three days is longer than both the FSA advice (one day) and the Voedingscentrum maximum (2 days), so throw it away."),
   ("How long can cooked rice sit out?", "As short as possible. The FSA advises getting it into the fridge within an hour; the Voedingscentrum says never leave leftovers out of the fridge for more than 2 hours."),
   ("Can you freeze cooked rice?", "Yes. Freeze it within an hour of cooking, in portions. It keeps about 3 months. Defrost it in the fridge and reheat it until steaming hot."),
   ("Can you eat rice cold?", "Yes, as long as it was cooled quickly and kept in the fridge, and you eat it within the same time limits."),
  ],
  "related": ["leftovers", "pasta", "mince"],
 },
 "nl": {
  "slug": "hoe-lang-is-gekookte-rijst-houdbaar",
  "name": "Gekookte rijst",
  "title": "Hoe Lang Is Gekookte Rijst Houdbaar in de Koelkast?",
  "desc": "Gekookte rijst blijft max. 2 dagen goed in de koelkast en zo'n 3 maanden in de vriezer. Zo koel, bewaar, vries en warm je rijst veilig op.",
  "h1": "Hoe lang is gekookte rijst houdbaar in de koelkast?",
  "answer": "Volgens het Voedingscentrum kun je gekookte rijst <strong>maximaal 2 dagen</strong> in de koelkast bewaren. De Britse Food Standards Agency is strenger en adviseert binnen 24 uur. Laat rijst snel afkoelen, warm hem maar één keer op en zorg dat hij gloeiend heet is. In de vriezer blijft gekookte rijst zo'n 3 maanden goed.",
  "table_head": ("", "Hoe lang", "Bron"),
  "table": [
   ("Gekookte rijst, koelkast", "Max. 2 dagen · Britse advies: binnen 24 uur", "Voedingscentrum · FSA"),
   ("Gekookte rijst, vriezer", "Ongeveer 3 maanden", "Voedingscentrum"),
   ("Gekookte rijst, buiten de koelkast", "Nooit langer dan 2 uur · Brits advies: binnen 1 uur koelen", "Voedingscentrum · FSA"),
   ("Opwarmen", "Maar één keer, door en door heet", "FSA · Voedingscentrum"),
   ("Ongekookte witte rijst, voorraadkast", "Langer dan 1 jaar; vaak nog tot 1 jaar na de THT-datum goed als hij er normaal uitziet", "Voedingscentrum"),
  ],
  "body": """
<h2>Waarom gekookte rijst extra aandacht nodig heeft</h2>
<p>In ongekookte rijst kunnen sporen zitten van de bacterie <strong>Bacillus cereus</strong>. Volgens de Britse Food Standards Agency (FSA) overleven die sporen het koken. Hoe langer gekookte rijst op kamertemperatuur staat, hoe groter de kans dat de bacterie of de gifstoffen die ze maakt de rijst onveilig maken.</p>
<p>Daarom maakt opwarmen het ook niet goed. Het probleem zit volgens de FSA niet in het opwarmen zelf, maar in hoe de rijst daarvoor is bewaard.</p>

<h2>Zo bewaar je gekookte rijst veilig</h2>
<ol>
  <li><strong>Laat hem snel afkoelen.</strong> Koel rijst die over is zo snel mogelijk, liefst binnen een uur. Laat hem niet afkoelen in de rijstkoker of pan.</li>
  <li><strong>Verdeel in kleine porties.</strong> In kleine, ondiepe bakjes koelt rijst sneller af. Zet het bakje in een laagje koud water, dan gaat het nog sneller.</li>
  <li><strong>Goed afgesloten in de koelkast.</strong> Het Voedingscentrum adviseert je koelkast op 4 °C te zetten.</li>
  <li><strong>Zet de datum erop.</strong> Dan weet je precies tot wanneer je hem kunt eten.</li>
</ol>

<h2>Hoe lang blijft gekookte rijst goed in de koelkast?</h2>
<p>Het Voedingscentrum noemt in de Bewaarwijzer maximaal 2 dagen voor gekookte rijst. De Britse FSA adviseert rijst niet langer dan één dag in de koelkast te bewaren voordat je hem eet of opwarmt. Wil je het zekere voor het onzekere: eet hem uiterlijk de volgende dag op.</p>
<p>Koude rijst eten mag gewoon, bijvoorbeeld in een rijstsalade, zolang hij snel is afgekoeld en in de koelkast heeft gestaan.</p>

<h2>Kun je gekookte rijst invriezen?</h2>
<p>Ja. Invriezen is de beste manier om rijst langer dan een paar dagen te bewaren. De FSA adviseert rijst binnen een uur na het koken in de vriezer te zetten, zodat bacteriën zich niet kunnen vermenigvuldigen. Vries in porties in: dan koelt het snel af en ontdooi je alleen wat je nodig hebt.</p>
<p>Volgens het Voedingscentrum blijft gekookte rijst zo'n 3 maanden goed in de vriezer, die op ten minste −18 °C moet staan. Ontdooi rijst in de koelkast, warm hem daarna door en door op en eet hem meteen.</p>

<h2>Zo warm je rijst op</h2>
<ul>
  <li><strong>Maar één keer.</strong> Warm rijst nooit vaker dan één keer op. Ook het Voedingscentrum raadt af restjes een tweede keer op te warmen.</li>
  <li><strong>Gloeiend heet, ook in het midden.</strong> Schep tussendoor om in de magnetron: soms blijven er delen koud.</li>
  <li><strong>Pas op met afhaalrijst.</strong> Restaurants koken rijst soms van tevoren en warmen hem op voor het serveren. Eet afhaalrijst dus snel op en warm hem niet nog eens op.</li>
</ul>

<h2>Hoe herken je bedorven rijst?</h2>
<p>Ruikt rijst zuur, voelt hij slijmerig of zie je schimmel, gooi hem dan weg. Maar andersom geldt het niet: de bacteriën en gifstoffen die voedselvergiftiging veroorzaken kun je niet zien of ruiken. Rijst die er goed uitziet en normaal ruikt, kan toch onveilig zijn als hij te lang buiten heeft gestaan of te lang is bewaard. Ga dus uit van de tijd, niet van je neus.</p>

<h2>Tips om minder rijst te verspillen</h2>
<ul>
  <li><strong>Kook de juiste hoeveelheid.</strong> Het Voedingscentrum raadt een maatbeker of keukenweegschaal aan om de juiste porties te bepalen.</li>
  <li><strong>Vries restjes meteen in</strong> in plaats van ze "voor later" in de koelkast te zetten.</li>
  <li><strong>Plan voor de volgende dag een rijstgerecht,</strong> zoals nasi of een rijstsalade, zodat de restjes op tijd op zijn.</li>
  <li><strong>Zet ze in FreshGarant</strong> met een houdbaarheid van 1 of 2 dagen, dan krijg je op tijd een seintje.</li>
</ul>
""",
  "faq": [
   ("Kun je gekookte rijst de volgende dag nog eten?", "Ja, als hij snel is afgekoeld en in de koelkast heeft gestaan. Het Voedingscentrum houdt maximaal 2 dagen aan; de Britse FSA adviseert binnen 24 uur."),
   ("Mag je rijst twee keer opwarmen?", "Nee. Warm rijst maar één keer op en zorg dat hij door en door heet is. Zowel de FSA als het Voedingscentrum raden een tweede keer opwarmen af."),
   ("Is rijst van 3 dagen oud nog goed?", "Nee. Dat is langer dan de 2 dagen van het Voedingscentrum en de 1 dag van de FSA. Gooi hem weg."),
   ("Hoe lang mag gekookte rijst buiten de koelkast staan?", "Zo kort mogelijk. Het Voedingscentrum zegt nooit langer dan 2 uur; de FSA adviseert rijst binnen een uur te koelen."),
   ("Kun je gekookte rijst invriezen?", "Ja. Vries hem binnen een uur na het koken in, in porties. Hij blijft zo'n 3 maanden goed. Ontdooi in de koelkast en warm hem gloeiend heet op."),
   ("Mag je rijst koud eten?", "Ja, als hij snel is afgekoeld en in de koelkast heeft gestaan, en je hem binnen dezelfde termijn opeet."),
  ],
  "related": ["leftovers", "pasta", "mince"],
 },
},
# ─────────────────────────────── MINCE ───────────────────────────────
{
 "key": "mince", "emoji": "🥩",
 "sources": ["vc_bewaarwijzer", "vc_veilig", "vc_ontdooien", "vc_verhitten", "fsa_chill", "fsa_cook", "fsa_burgers", "fsa_facts"],
 "en": {
  "slug": "how-long-does-mince-last",
  "name": "Mince (ground beef)",
  "title": "How Long Does Mince (Ground Beef) Last in the Fridge?",
  "desc": "Raw mince keeps 1 day in the fridge and never past its use-by date; cooked mince 2 days. Freezing, defrosting and spotting spoiled mince.",
  "h1": "How long does mince (ground beef) last in the fridge?",
  "answer": "Once opened, raw mince keeps <strong>1 day in the fridge</strong> according to the Voedingscentrum, and never past its use-by date. Cooked mince, such as bolognese, keeps 2 days. In the freezer, raw or cooked mince keeps about 3 months. Defrost it in the fridge and use it within 24 hours.",
  "table_head": ("", "How long", "Source"),
  "table": [
   ("Raw mince, fridge (opened)", "1 day, and never past the use-by date", "Voedingscentrum · FSA"),
   ("Raw mince, freezer", "About 3 months; meat is best within 2–3 months", "Voedingscentrum · FSA"),
   ("Cooked mince, fridge", "2 days (48 hours)", "Voedingscentrum · FSA"),
   ("Cooked mince, freezer", "About 3 months", "Voedingscentrum"),
   ("After defrosting", "Use within 24 hours", "FSA"),
   ("Out of the fridge", "As short as possible; never more than 2 hours", "FSA · Voedingscentrum"),
  ],
  "body": """
<h2>Why mince goes off faster than a steak</h2>
<p>Bacteria such as E. coli and salmonella sit on the <em>surface</em> of meat. On a steak, searing the outside kills them. When meat is minced, those surface bacteria get spread all the way through. The Food Standards Agency explains that this is why mince and burgers must be cooked right through, and it is also why mince spoils faster than a whole piece of meat.</p>

<h2>How to store raw mince</h2>
<ul>
  <li><strong>Bottom shelf, covered.</strong> Keep raw meat in its packaging or a sealed container on the bottom shelf, so juices cannot drip onto other food.</li>
  <li><strong>Cold enough.</strong> The FSA advises a fridge between 0 and 5°C; the Voedingscentrum advises 4°C.</li>
  <li><strong>Respect the use-by date.</strong> Mince has a use-by date because harmful bacteria can grow. Do not eat it after that date, even if it looks and smells fine.</li>
  <li><strong>Use it quickly.</strong> The Voedingscentrum gives 1 day in the fridge for raw mince.</li>
</ul>

<h2>Can you freeze mince?</h2>
<p>Yes, and it is the easiest way to avoid throwing mince away. The FSA says you can freeze food right up until midnight on the use-by date. The Voedingscentrum gives about 3 months for raw mince in the freezer; the FSA says meat is usually best eaten within 2–3 months. After that it is not unsafe, but it can taste and smell rancid.</p>
<ul>
  <li>Freeze in small portions, so you only defrost what you need.</li>
  <li>Wrap it well or use a freezer bag against freezer burn.</li>
  <li>Write the date on it, and keep your freezer at −18°C.</li>
</ul>

<h2>How to defrost mince safely</h2>
<p>Defrost mince in the fridge: take it out of the freezer a day before you need it, and put it on a covered plate or in a bowl on the bottom shelf. The FSA advises using food within 24 hours once it is fully defrosted, because from then on it goes off just like fresh mince. Short on time? Use the defrost setting of the microwave and cook the mince straight away.</p>
<p>Defrosted raw mince should not go back into the freezer as it is. Cook it first: you can freeze the cooked dish, but then only reheat it once.</p>

<h2>Cooking mince: always all the way through</h2>
<p>Unlike a whole steak, mince and burgers should never be eaten pink. The FSA advises checking that mince is steaming hot all the way through, that none of the meat is pink when you cut into it, and that the juices run clear. With a food thermometer, the middle should reach 70°C for 2 minutes.</p>

<h2>Cooked mince and leftovers</h2>
<p>Bolognese, chilli or meatballs: cool them and put them in the fridge within 1–2 hours. Cooked mince keeps 2 days in the fridge (the FSA says eat leftovers within 48 hours) or about 3 months in the freezer. Reheat leftovers only once, until steaming hot.</p>

<h2>How to tell if mince has gone off</h2>
<p>The Voedingscentrum names these signs: an unusual smell, a grey discolouration or a sticky surface. If you see any of these, throw it away. But do not rely on a sniff test for food with a use-by date: the FSA points out that you cannot smell the bacteria that cause food poisoning. Past the use-by date means in the bin, however it smells.</p>

<h2>Tips to waste less mince</h2>
<ul>
  <li>Freeze mince on the day you buy it if you will not cook it within a day.</li>
  <li>Cook a big batch of sauce and freeze it in portions.</li>
  <li>Log the use-by date in FreshGarant, so you get a reminder the day before.</li>
</ul>
""",
  "faq": [
   ("Can you eat mince one day after the use-by date?", "No. A use-by date is about safety. Do not eat mince after it, even if it looks and smells normal."),
   ("How long does cooked mince last in the fridge?", "2 days. The Voedingscentrum gives 2 days for cooked mince, and the FSA advises eating leftovers within 48 hours."),
   ("Can you refreeze defrosted mince?", "Not raw. Cook it first; you can then freeze the cooked dish, but reheat it only once."),
   ("Can mince be pink in the middle?", "No. Mince and burgers must be cooked until steaming hot all the way through, with no pink meat and clear juices."),
   ("Is grey mince safe to eat?", "The Voedingscentrum lists grey discolouration, an unusual smell and stickiness as signs of spoilage. When in doubt, throw it out, and never eat it past the use-by date."),
   ("How long can raw mince stay out of the fridge?", "As short as possible. Never leave food that spoils quickly, like meat, out of the fridge for more than 2 hours."),
  ],
  "related": ["chicken", "leftovers", "rice"],
 },
 "nl": {
  "slug": "hoe-lang-is-gehakt-houdbaar",
  "name": "Gehakt",
  "title": "Hoe Lang Is Gehakt Houdbaar in de Koelkast?",
  "desc": "Rauw gehakt blijft 1 dag goed in de koelkast en nooit na de TGT-datum; bereid gehakt 2 dagen. Over invriezen, ontdooien en bedorven gehakt.",
  "h1": "Hoe lang is gehakt houdbaar in de koelkast?",
  "answer": "Rauw gehakt blijft na openen volgens het Voedingscentrum <strong>1 dag goed in de koelkast</strong>, en nooit na de TGT-datum. Bereid gehakt, zoals bolognesesaus, houd je 2 dagen. In de vriezer blijft rauw of bereid gehakt zo'n 3 maanden goed. Ontdooi het in de koelkast en gebruik het binnen 24 uur.",
  "table_head": ("", "Hoe lang", "Bron"),
  "table": [
   ("Rauw gehakt, koelkast (geopend)", "1 dag, en nooit na de TGT-datum", "Voedingscentrum"),
   ("Rauw gehakt, vriezer", "Ongeveer 3 maanden", "Voedingscentrum"),
   ("Bereid gehakt, koelkast", "2 dagen", "Voedingscentrum"),
   ("Bereid gehakt, vriezer", "Ongeveer 3 maanden", "Voedingscentrum"),
   ("Na het ontdooien", "Binnen 24 uur gebruiken", "FSA"),
   ("Buiten de koelkast", "Zo kort mogelijk, nooit langer dan 2 uur", "Voedingscentrum"),
  ],
  "body": """
<h2>Waarom gehakt sneller bederft dan een biefstuk</h2>
<p>Bacteriën zoals E. coli en salmonella zitten aan de <em>buitenkant</em> van vlees. Bij een biefstuk dood je ze door de buitenkant dicht te schroeien. Bij gehakt worden die bacteriën door het malen door het hele vlees verspreid. Daarom moet gehakt helemaal gaar, en daarom bederft het ook sneller dan een heel stuk vlees.</p>

<h2>Zo bewaar je rauw gehakt</h2>
<ul>
  <li><strong>Onderin de koelkast, afgedekt.</strong> Dan kan vleessap niet op andere producten lekken. Het Voedingscentrum raadt aan rauw vlees op de koudste plek te bewaren.</li>
  <li><strong>Koud genoeg.</strong> Zet je koelkast op 4 °C.</li>
  <li><strong>Let op de TGT-datum.</strong> Op gehakt staat "te gebruiken tot" (TGT). Eet het daarna niet meer, vanwege de kans op ziekmakende bacteriën, ook als het er nog goed uitziet.</li>
  <li><strong>Gebruik het snel.</strong> Het Voedingscentrum houdt voor rauw gehakt 1 dag in de koelkast aan.</li>
</ul>

<h2>Kun je gehakt invriezen?</h2>
<p>Ja, en dat is de makkelijkste manier om geen gehakt weg te gooien. Vries het in vóór de TGT-datum. Volgens het Voedingscentrum blijft rauw gehakt zo'n 3 maanden goed in de vriezer. Te lang in de vriezer geeft een ranzige geur en smaak.</p>
<ul>
  <li>Vries in kleine porties in, dan ontdooi je alleen wat je nodig hebt.</li>
  <li>Verpak het goed, bijvoorbeeld in een vriezerzakje, tegen uitdrogen.</li>
  <li>Zet de datum op het zakje en houd je vriezer op ten minste −18 °C.</li>
</ul>

<h2>Gehakt veilig ontdooien</h2>
<p>De beste manier volgens het Voedingscentrum: haal het gehakt een dag van tevoren uit de vriezer en leg het afgedekt op een bord of in een schaal onderin de koelkast. Zorg dat er geen dooiwater op andere producten lekt. Vergeten? Kleine porties kun je ontdooien in de magnetron, op de ontdooistand, en daarna meteen bereiden.</p>
<p>Ontdooid gehakt gaat net zo snel achteruit als vers gehakt; de Britse FSA adviseert het binnen 24 uur te gebruiken. Vries rauw ontdooid gehakt niet opnieuw in. Bereid het eerst; het gerecht kun je daarna wel invriezen.</p>

<h2>Gehakt altijd helemaal gaar</h2>
<p>Alleen vlees uit één stuk, zoals biefstuk, kun je rosé eten. Voor gemalen vlees zoals gehakt, hamburgers en worst geldt volgens het Voedingscentrum: controleer of het volledig gaar is voordat je het eet. Het vlees is dan niet meer roze en door en door heet.</p>

<h2>Bereid gehakt en restjes</h2>
<p>Bolognesesaus, chili of gehaktballen: laat ze snel afkoelen en zet ze afgesloten in de koelkast. Laat restjes niet langer dan 2 uur buiten de koelkast staan. Bereid gehakt blijft 2 dagen goed in de koelkast of zo'n 3 maanden in de vriezer. Warm restjes door en door op tot ze stomend heet zijn, en liever niet een tweede keer.</p>

<h2>Hoe herken je bedorven gehakt?</h2>
<p>Het Voedingscentrum noemt deze signalen: een afwijkende geur, een grauwe verkleuring of een plakkerig oppervlak. Eet geen vlees dat er raar uitziet of niet goed ruikt. Maar vertrouw bij gehakt niet alleen op je neus: de bacteriën die je ziek maken ruik je niet. Is de TGT-datum voorbij, dan gaat het weg, hoe het ook ruikt.</p>

<h2>Tips om minder gehakt te verspillen</h2>
<ul>
  <li>Vries gehakt in op de dag dat je het koopt als je het niet binnen een dag gebruikt.</li>
  <li>Maak een grote pan saus en vries die in porties in.</li>
  <li>Zet de TGT-datum in FreshGarant, dan krijg je de dag ervoor een seintje.</li>
</ul>
""",
  "faq": [
   ("Kun je gehakt een dag na de TGT-datum nog eten?", "Nee. De TGT-datum gaat over veiligheid. Eet gehakt daarna niet meer, ook als het er normaal uitziet en ruikt."),
   ("Hoe lang is bereid gehakt houdbaar in de koelkast?", "2 dagen, volgens het Voedingscentrum. Zet het snel na het afkoelen afgesloten in de koelkast."),
   ("Mag je ontdooid gehakt opnieuw invriezen?", "Rauw niet. Bereid het eerst; het gerecht kun je daarna wel invriezen."),
   ("Mag gehakt nog roze zijn vanbinnen?", "Nee. Gehakt moet helemaal gaar zijn. Alleen vlees uit één stuk, zoals biefstuk, kan rosé."),
   ("Is grauw gehakt nog goed?", "Het Voedingscentrum noemt een grauwe verkleuring, een afwijkende geur en een plakkerig oppervlak als tekenen van bederf. Twijfel je, gooi het dan weg, en eet het nooit na de TGT-datum."),
   ("Hoe lang mag rauw gehakt buiten de koelkast liggen?", "Zo kort mogelijk, en nooit langer dan 2 uur. Dat geldt voor al het eten dat snel bederft, zoals vlees."),
  ],
  "related": ["chicken", "leftovers", "rice"],
 },
},
]


from guides_content_b import GUIDES_B  # noqa: E402
from guides_content_c import GUIDES_C  # noqa: E402
from guides_content_d import GUIDES_D  # noqa: E402

GUIDES = GUIDES + GUIDES_B + GUIDES_C + GUIDES_D
# Shown on the homepages (keys, in this order).
HOME_PICKS = ["rice", "chicken", "mince", "eggs", "bread", "leftovers"]

from guides_content_extra import apply as _apply_extra  # noqa: E402
_apply_extra(GUIDES)

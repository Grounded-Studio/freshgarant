"""Generate the blog pages (EN + NL) from blog_content.py.

Run from the site root:  python -I _tools/build_blog.py
Writes blog/*.html and nl/blog/*.html. Edit the text in blog_content.py,
not in the generated HTML.
"""
import html
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from blog_content import ARTICLES, PUBLISHED  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://freshgarant.app"
CSS_V = "2026102605"
PLAY = "https://play.google.com/store/apps/details?id=app.rork.versgarant"

T = {
  "en": {
    "prefix": "", "home": "/", "nav": [("/", "Home"), ("/features.html", "Features"), ("/savings.html", "Savings"), ("/blog/", "Blog"), ("/download.html", "Download")],
    "blog_title": "Blog — Food Storage & Food Waste Tips | FreshGarant",
    "blog_h1": "Tips to keep food fresh and waste less",
    "blog_desc": "Practical guides on expiry dates, how long food lasts in the fridge and freezer, and how to reduce food waste at home.",
    "blog_lead": "Clear answers to the questions everyone has in front of the fridge: is this still good, can I freeze it, and how do I stop throwing food away?",
    "kicker": "BLOG", "read": "Read article →", "min": "min read",
    "related": "Read next", "updated": "Published",
    "note": "These are general guidelines for food stored at the right temperature. Always follow the instructions on the packaging, and when in doubt, throw it out. Sources: Voedingscentrum (Netherlands Nutrition Centre) and the EU rules on date marking.",
    "cta_h": "Never forget what's in your fridge",
    "cta_p": "FreshGarant tracks every expiry date and reminds you in time. Free on Android.",
    "cta_btn": "Download FreshGarant free →",
    "tagline": "Scan your groceries. Cook what's fresh. Never waste food again.",
    "product": "Product", "legal": "Legal",
    "f_product": [("/features.html", "All features"), ("/savings.html", "Savings calculator"), ("/blog/", "Blog"), ("/download.html", "Download the app")],
    "f_legal": [("/privacy.html", "Privacy"), ("/terms.html", "Terms"), ("/delete-data.html", "Delete your data"), ("/contact.html", "Contact")],
    "copy": "© 2026 Grounded Studio · Made with care in the Netherlands",
    "also": 'Also by us: <a href="https://buildexact.app/">BuildExact</a> · <a href="https://circuittrace.app/">Circuit Trace</a>',
    "date": "26 October 2026", "lang_name": "en",
  },
  "nl": {
    "prefix": "/nl", "home": "/nl/", "nav": [("/nl/", "Home"), ("/nl/features.html", "Functies"), ("/nl/savings.html", "Besparing"), ("/nl/blog/", "Blog"), ("/nl/download.html", "Download")],
    "blog_title": "Blog — Tips voor bewaren en minder verspillen | FreshGarant",
    "blog_h1": "Tips om eten vers te houden en minder te verspillen",
    "blog_desc": "Praktische uitleg over THT en TGT, hoe lang eten goed blijft in koelkast en vriezer, en hoe je voedselverspilling thuis tegengaat.",
    "blog_lead": "Duidelijke antwoorden op de vragen die iedereen heeft voor de koelkast: is dit nog goed, kan ik het invriezen, en hoe gooi ik minder weg?",
    "kicker": "BLOG", "read": "Lees artikel →", "min": "min lezen",
    "related": "Lees ook", "updated": "Gepubliceerd",
    "note": "Dit zijn algemene richtlijnen voor eten dat op de juiste temperatuur is bewaard. Volg altijd de aanwijzingen op de verpakking, en twijfel je: weggooien. Bronnen: Voedingscentrum en de EU-regels voor datumaanduiding.",
    "cta_h": "Vergeet nooit meer wat er in je koelkast ligt",
    "cta_p": "FreshGarant houdt elke houdbaarheidsdatum bij en waarschuwt je op tijd. Gratis voor Android.",
    "cta_btn": "Download FreshGarant gratis →",
    "tagline": "Scan je boodschappen. Kook wat vers is. Nooit meer eten weggooien.",
    "product": "Product", "legal": "Juridisch",
    "f_product": [("/nl/features.html", "Alle functies"), ("/nl/savings.html", "Besparings-calculator"), ("/nl/blog/", "Blog"), ("/nl/download.html", "App downloaden")],
    "f_legal": [("/nl/privacy.html", "Privacy"), ("/nl/terms.html", "Voorwaarden"), ("/nl/delete-data.html", "Gegevens verwijderen"), ("/nl/contact.html", "Contact")],
    "copy": "© 2026 Grounded Studio · Gemaakt met zorg in Nederland",
    "also": 'Ook van ons: <a href="https://buildexact.app/nl/">BuildExact</a> · <a href="https://circuittrace.app/">Circuit Trace</a>',
    "date": "26 oktober 2026", "lang_name": "nl",
  },
}

ICON = '<img src="/assets/icons/icon_favicon_64.webp" alt="FreshGarant" width="34" height="34" /><span>FreshGarant</span>'


def url_of(lang, slug=None):
    base = f"{T[lang]['prefix']}/blog/"
    return base + (f"{slug}.html" if slug else "")


def head(lang, title, desc, path_en, path_nl, og_type, ld):
    path = path_en if lang == "en" else path_nl
    e = html.escape
    return f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}" />
<meta name="theme-color" content="#2E7D32" />
<link rel="icon" type="image/png" sizes="64x64" href="/assets/icons/icon_favicon_64.png" />
<link rel="apple-touch-icon" sizes="512x512" href="/assets/icons/icon_512.png" />
<link rel="canonical" href="{SITE}{path}" />
<link rel="alternate" hreflang="en" href="{SITE}{path_en}" />
<link rel="alternate" hreflang="x-default" href="{SITE}{path_en}" />
<link rel="alternate" hreflang="nl" href="{SITE}{path_nl}" />
<meta property="og:title" content="{e(title)}" />
<meta property="og:description" content="{e(desc)}" />
<meta property="og:url" content="{SITE}{path}" />
<meta property="og:image" content="{SITE}/assets/images/og-image.jpg" />
<meta property="og:type" content="{og_type}" />
<meta name="twitter:card" content="summary_large_image" />
<link rel="preload" href="/assets/fonts/inter-latin.woff2" as="font" type="font/woff2" crossorigin />
<link rel="stylesheet" href="/assets/css/global.css?v={CSS_V}" />
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
</head>
<body>

<header class="site-header">
  <div class="container">
    <a href="{T[lang]['home']}" class="brand-mark">{ICON}</a>
    <nav class="site-nav">
{nav(lang)}
      <div class="lang-switch"><a href="{path_en}"{' class="active"' if lang == 'en' else ''}>EN</a><a href="{path_nl}"{' class="active"' if lang == 'nl' else ''}>NL</a></div>
    </nav>
  </div>
</header>
"""


def nav(lang):
    out = []
    for href, label in T[lang]["nav"]:
        active = ' class="active"' if href.endswith("/blog/") else ""
        out.append(f'      <a href="{href}"{active}>{label}</a>')
    return "\n".join(out)


def foot(lang):
    t = T[lang]
    li = lambda items: "".join(f'<li><a href="{h}">{l}</a></li>' for h, l in items)
    return f"""
<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div><div class="brand-mark" style="color: #fff;">{ICON}</div><p class="footer-tagline">{t['tagline']}</p></div>
      <div class="footer-col"><h4>{t['product']}</h4><ul>{li(t['f_product'])}</ul></div>
      <div class="footer-col"><h4>{t['legal']}</h4><ul>{li(t['f_legal'])}</ul></div>
    </div>
    <div class="footer-bottom"><span>{t['copy']}</span><span>{t['also']}</span></div>
  </div>
</footer>

</body>
</html>
"""


def cta(lang):
    t = T[lang]
    return f"""
<section class="section-tight">
  <div class="container">
    <div class="cta-band">
      <h2>{t['cta_h']}</h2>
      <p>{t['cta_p']}</p>
      <a href="{PLAY}" class="btn btn-primary" target="_blank" rel="noopener">{t['cta_btn']}</a>
    </div>
  </div>
</section>
</main>
"""


def minutes(body):
    words = len(re.sub(r"<[^>]+>", " ", body).split())
    return max(2, round(words / 200))


def crumbs(lang, items):
    """Visible breadcrumb trail; the last item (href None) is the current page."""
    lis = "".join(
        f'<li><a href="{h}">{html.escape(n)}</a></li>' if h else f'<li><span aria-current="page">{html.escape(n)}</span></li>'
        for n, h in items)
    aria = "Breadcrumb" if lang == "en" else "Kruimelpad"
    return f'    <nav class="breadcrumb" aria-label="{aria}"><ol>{lis}</ol></nav>'


def breadcrumb(lang, items):
    return {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": SITE + u} for i, (n, u) in enumerate(items)]}


def article_page(lang, art):
    t, a = T[lang], art[lang]
    other = "nl" if lang == "en" else "en"
    path_en, path_nl = url_of("en", art["en"]["slug"]), url_of("nl", art["nl"]["slug"])
    path = url_of(lang, a["slug"])
    body = a["body"].strip().replace("<table>", '<div class="table-wrap"><table>').replace("</table>", "</table></div>")
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "Article", "headline": a["title"], "description": a["desc"], "inLanguage": lang,
         "datePublished": PUBLISHED, "dateModified": PUBLISHED, "mainEntityOfPage": SITE + path,
         "image": SITE + "/assets/images/og-image.jpg",
         "author": {"@type": "Organization", "name": "Grounded Studio", "url": "https://grounded-studio.app/"},
         "publisher": {"@type": "Organization", "name": "Grounded Studio", "url": "https://grounded-studio.app/",
                       "logo": {"@type": "ImageObject", "url": SITE + "/assets/icons/icon_512.png"}}},
        breadcrumb(lang, [("Home", t["home"]), ("Blog", url_of(lang)), (a["title"], path)]),
    ]}
    related = "".join(
        f'<li><a href="{url_of(lang, o[lang]["slug"])}">{html.escape(o[lang]["title"])}</a></li>'
        for o in ARTICLES if o is not art)
    return head(lang, f"{a['title']} | FreshGarant", a["desc"], path_en, path_nl, "article", ld) + f"""
<main>
<section class="section">
  <div class="container">
{crumbs(lang, [("Home", t["home"]), ("Blog", url_of(lang)), (a["title"], None)])}
    <span class="section-kicker">{a['kicker']}</span>
    <h1>{html.escape(a['title'])}</h1>
    <p class="blog-meta">{t['updated']} {t['date']} · {minutes(a['body'])} {t['min']}</p>
    <p class="blog-lead">{a['intro']}</p>

    <article class="prose" style="margin-top: 32px;">
{body}
    </article>

    <p class="blog-note">{t['note']}</p>

    <div class="prose blog-related">
      <h2>{t['related']}</h2>
      <ul>{related}</ul>
    </div>
  </div>
</section>
""" + cta(lang) + foot(lang)


def index_page(lang):
    t = T[lang]
    cards = "\n".join(f"""      <a class="feature-card blog-card" href="{url_of(lang, art[lang]['slug'])}">
        <span class="section-kicker">{art[lang]['kicker']}</span>
        <h3>{html.escape(art[lang]['title'])}</h3>
        <p>{html.escape(art[lang]['desc'])}</p>
        <span class="read-more">{t['read']}</span>
      </a>""" for art in ARTICLES)
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "Blog", "name": t["blog_h1"], "description": t["blog_desc"], "inLanguage": lang, "url": SITE + url_of(lang),
         "publisher": {"@type": "Organization", "name": "Grounded Studio", "url": "https://grounded-studio.app/"},
         "blogPost": [{"@type": "BlogPosting", "headline": art[lang]["title"], "url": SITE + url_of(lang, art[lang]["slug"]),
                       "datePublished": PUBLISHED} for art in ARTICLES]},
        breadcrumb(lang, [("Home", t["home"]), ("Blog", url_of(lang))]),
    ]}
    return head(lang, t["blog_title"], t["blog_desc"], url_of("en"), url_of("nl"), "website", ld) + f"""
<main>
<section class="section">
  <div class="container">
{crumbs(lang, [("Home", t["home"]), ("Blog", None)])}
    <span class="section-kicker">{t['kicker']}</span>
    <h1 class="section-title">{t['blog_h1']}</h1>
    <p class="section-sub">{t['blog_lead']}</p>
    <div class="grid grid-2 feature-grid">
{cards}
    </div>
  </div>
</section>
""" + cta(lang) + foot(lang)


def write(rel, text):
    full = os.path.join(ROOT, rel)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    print("wrote", rel)


for lang in ("en", "nl"):
    write(f"{T[lang]['prefix'].lstrip('/')}/blog/index.html".lstrip("/"), index_page(lang))
    for art in ARTICLES:
        write(f"{T[lang]['prefix'].lstrip('/')}/blog/{art[lang]['slug']}.html".lstrip("/"), article_page(lang, art))

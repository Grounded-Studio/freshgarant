"""Generate the food storage guides (EN /guides/, NL /nl/gidsen/).

Run from the site root:  python -I _tools/build_guides.py
Text lives in guides_content.py; layout, header and footer are shared with
the blog (build_blog.py).
"""
import html
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_blog as B  # noqa: E402
from guides_content import BLOG_RELATED, CHECKED, GUIDES, HOME_PICKS, SOURCES  # noqa: E402

SITE, PLAY = B.SITE, B.PLAY
BY_KEY = {g["key"]: g for g in GUIDES}

U = {
  "en": {
    "dir": "/guides/", "home": "/", "crumb": "Guides",
    "index_title": "Food Storage Guides: How Long Does Food Last? | FreshGarant",
    "index_desc": "How long food lasts in the fridge, freezer and pantry, product by product, based on official food safety sources.",
    "index_h1": "How long does food last? Storage guides per product",
    "index_lead": "Fridge, freezer, pantry, after opening and after cooking: clear answers per product, based on official food safety sources.",
    "kicker": "STORAGE GUIDE", "short": "Short answer", "overview": "At a glance",
    "faq": "Frequently asked questions", "related": "Related guides", "sources": "Sources",
    "checked": "Checked against the sources on",
    "note": "This is general guidance for food stored at the right temperature. Always follow the use-by date and the storage instructions on the packaging, and when in doubt, throw it out.",
    "cta_h": "Let FreshGarant remind you before it goes off",
    "cta_p": "Log your food once and get a reminder in time. Free on Android.",
    "cta_btn": "Get it on Google Play →", "read": "Read guide →",
  },
  "nl": {
    "dir": "/nl/gidsen/", "home": "/nl/", "crumb": "Gidsen",
    "index_title": "Houdbaarheid per Product: Bewaargidsen | FreshGarant",
    "index_desc": "Hoe lang eten goed blijft in de koelkast, vriezer en voorraadkast, per product, op basis van officiële bronnen voor voedselveiligheid.",
    "index_h1": "Hoe lang is eten houdbaar? Bewaargidsen per product",
    "index_lead": "Koelkast, vriezer, voorraadkast, na openen en na bereiden: duidelijke antwoorden per product, op basis van officiële bronnen.",
    "kicker": "BEWAARGIDS", "short": "Kort antwoord", "overview": "In één oogopslag",
    "faq": "Veelgestelde vragen", "related": "Verwante gidsen", "sources": "Bronnen",
    "checked": "Gecontroleerd aan de hand van de bronnen op",
    "note": "Dit zijn algemene richtlijnen voor eten dat op de juiste temperatuur is bewaard. Volg altijd de TGT-datum en de bewaaradviezen op de verpakking, en twijfel je: weggooien.",
    "cta_h": "Laat FreshGarant je waarschuwen voordat het bederft",
    "cta_p": "Zet je eten één keer in de app en krijg op tijd een seintje. Gratis voor Android.",
    "cta_btn": "Ontdek het op Google Play →", "read": "Lees de gids →",
  },
}


def url(lang, g=None):
    return U[lang]["dir"] + (f"{g[lang]['slug']}.html" if g else "")


def other(lang):
    return "nl" if lang == "en" else "en"


def guide_page(lang, g):
    u, a, e = U[lang], g[lang], html.escape
    path_en, path_nl = url("en", g), url("nl", g)
    faq_ld = {"@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": ans}} for q, ans in a["faq"]]}
    art_ld = {"@type": "Article", "headline": a["h1"], "description": a["desc"], "inLanguage": lang,
              "datePublished": CHECKED["iso"], "dateModified": CHECKED["iso"], "mainEntityOfPage": SITE + url(lang, g),
              "image": SITE + "/assets/images/og-image.jpg",
              "author": {"@type": "Organization", "name": "Grounded Studio", "url": "https://grounded-studio.app"},
              "publisher": {"@type": "Organization", "name": "FreshGarant", "logo": {"@type": "ImageObject", "url": SITE + "/assets/icons/icon_512.png"}}}
    bc = B.breadcrumb(lang, [("Home", u["home"]), (u["crumb"], u["dir"]), (a["name"], url(lang, g))])
    ld = {"@context": "https://schema.org", "@graph": [art_ld, faq_ld, bc]}
    th = "".join(f"<th>{e(h)}</th>" for h in a["table_head"])
    rows = "\n".join(f"    <tr><td><strong>{e(r[0])}</strong></td><td>{e(r[1])}</td><td>{e(r[2])}</td></tr>" for r in a["table"])
    faq = "\n".join(f"      <details><summary>{e(q)}</summary><p>{e(ans)}</p></details>" for q, ans in a["faq"])
    rel = [(url(lang, BY_KEY[k]), BY_KEY[k][lang]["h1"]) for k in a["related"] if k in BY_KEY] + BLOG_RELATED[lang]
    rel_html = "".join(f'<li><a href="{h}">{e(t)}</a></li>' for h, t in rel[:5])
    src = "".join(f'<li><a href="{SOURCES[s]["url"]}" target="_blank" rel="noopener">{e(SOURCES[s][lang])}</a></li>' for s in g["sources"])
    head = B.head(lang, f"{a['title']} | FreshGarant", a["desc"], path_en, path_nl, "article", ld)
    head = head.replace(B.nav(lang), B.nav(lang, None))
    return head + f"""
<main>
<section class="section">
  <div class="container">
{B.crumbs(lang, [("Home", u["home"]), (u["crumb"], u["dir"]), (a["name"], None)])}
    <span class="section-kicker">{u['kicker']}</span>
    <h1>{e(a['h1'])}</h1>
    <div class="guide-answer"><strong>{u['short']}:</strong> {a['answer']}</div>

    <article class="prose" style="margin-top: 32px;">
<h2>{u['overview']}</h2>
<div class="table-wrap"><table class="guide-table">
  <thead><tr>{th}</tr></thead>
  <tbody>
{rows}
  </tbody>
</table></div>
{a['body']}
<h2>{u['faq']}</h2>
    </article>
    <div class="faq guide-faq">
{faq}
    </div>

    <div class="prose blog-related">
      <h2>{u['related']}</h2>
      <ul>{rel_html}</ul>
      <h2>{u['sources']}</h2>
      <ul class="guide-sources">{src}</ul>
    </div>
    <p class="blog-note">{u['note']} {u['checked']} {CHECKED[lang]}.</p>
  </div>
</section>

<section class="section-tight">
  <div class="container">
    <div class="cta-band">
      <h2>{u['cta_h']}</h2>
      <p>{u['cta_p']}</p>
      <a href="{PLAY}" class="btn btn-primary" target="_blank" rel="noopener">{u['cta_btn']}</a>
    </div>
  </div>
</section>
</main>
""" + B.foot(lang)


def index_page(lang):
    u, e = U[lang], html.escape
    cards = "\n".join(f"""      <a class="feature-card blog-card" href="{url(lang, g)}">
        <span class="guide-emoji" aria-hidden="true">{g['emoji']}</span>
        <h3>{e(g[lang]['h1'])}</h3>
        <p>{e(g[lang]['desc'])}</p>
        <span class="read-more">{u['read']}</span>
      </a>""" for g in GUIDES)
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "CollectionPage", "name": u["index_h1"], "description": u["index_desc"], "inLanguage": lang, "url": SITE + u["dir"],
         "hasPart": [{"@type": "Article", "headline": g[lang]["h1"], "url": SITE + url(lang, g)} for g in GUIDES]},
        B.breadcrumb(lang, [("Home", u["home"]), (u["crumb"], u["dir"])])]}
    head = B.head(lang, u["index_title"], u["index_desc"], U["en"]["dir"], U["nl"]["dir"], "website", ld)
    head = head.replace(B.nav(lang), B.nav(lang, None))
    return head + f"""
<main>
<section class="section">
  <div class="container">
{B.crumbs(lang, [("Home", u["home"]), (u["crumb"], None)])}
    <span class="section-kicker">{u['kicker']}</span>
    <h1>{e(u['index_h1'])}</h1>
    <p class="blog-lead">{e(u['index_lead'])}</p>
    <div class="grid grid-2 feature-grid" style="margin-top: 32px;">
{cards}
    </div>
  </div>
</section>
</main>
""" + B.foot(lang)


def main():
    for g in GUIDES:
        for lang in ("en", "nl"):
            d = g[lang]["desc"]
            assert len(d) <= 150, (g["key"], lang, len(d))
            words = len(re.sub(r"<[^>]+>", " ", g[lang]["answer"] + g[lang]["body"] + " ".join(q + " " + a for q, a in g[lang]["faq"]) + " ".join(" ".join(r) for r in g[lang]["table"])).split())
            print(f"{lang} {g['key']}: {words} words, desc {len(d)}")
            B.write(url(lang, g).lstrip("/"), guide_page(lang, g))
    for lang in ("en", "nl"):
        B.write(U[lang]["dir"].lstrip("/") + "index.html", index_page(lang))
    home_block()


HOME = {
    "en": ("HOW LONG DOES IT LAST?", "Storage guides per product",
           "Fridge, freezer and pantry: clear answers based on official food safety sources.", "All storage guides →", "index.html"),
    "nl": ("HOE LANG IS HET HOUDBAAR?", "Bewaargidsen per product",
           "Koelkast, vriezer en voorraadkast: duidelijke antwoorden op basis van officiële bronnen.", "Alle bewaargidsen →", "nl/index.html"),
}


def home_block():
    """Fill <!-- GUIDES:START --> … <!-- GUIDES:END --> on both homepages."""
    for lang, (kicker, title, sub, all_label, page) in HOME.items():
        cards = "\n".join(f"""      <a class="feature-card blog-card" href="{url(lang, BY_KEY[k])}">
        <span class="guide-emoji" aria-hidden="true">{BY_KEY[k]['emoji']}</span>
        <h3>{html.escape(BY_KEY[k][lang]['h1'])}</h3>
        <span class="read-more">{U[lang]['read']}</span>
      </a>""" for k in HOME_PICKS)
        block = f"""<!-- GUIDES:START -->
<section class="section">
  <div class="container">
    <span class="section-kicker">{kicker}</span>
    <h2 class="section-title">{title}</h2>
    <p class="section-sub">{sub}</p>
    <div class="grid grid-3 feature-grid">
{cards}
    </div>
    <p style="margin-top: 24px;"><a href="{U[lang]['dir']}" style="font-weight: 700;">{all_label}</a></p>
  </div>
</section>
<!-- GUIDES:END -->"""
        full = os.path.join(B.ROOT, page)
        with open(full, encoding="utf-8", newline="") as f:
            s = f.read()
        assert "<!-- GUIDES:START -->" in s, page
        s = re.sub(r"<!-- GUIDES:START -->.*?<!-- GUIDES:END -->", lambda m: block, s, count=1, flags=re.S)
        with open(full, "w", encoding="utf-8", newline="") as f:
            f.write(s)
        print("homepage guides block", page)


if __name__ == "__main__":
    main()
    # Cross-promo block for the other Grounded Studio apps (re-added after every build).
    import subprocess, sys
    _xp = r"C:\meten_weten_bouw\scripts\cross_promo.py"
    if os.path.exists(_xp):
        subprocess.run([sys.executable, "-I", _xp, "freshgarant"], check=False)

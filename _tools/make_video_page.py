"""Watch page for the FreshGarant video (video.html).

Google only indexes a video when it is the main content of a page; on the
homepage it is one section among many ("Video isn't on a watch page").
This page has the video at the top plus VideoObject structured data.
Header/footer are taken from download.html so they stay in sync.

Run from the site root:  python -I _tools/make_video_page.py
"""
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://freshgarant.app"
YT = "qDHaiyUZwjI"             # main video: 2.2.9, everything new (2026-11-23)
YT_OLD = "a66ORi159Go"         # earlier promo, kept below the main video
PLAY = "https://play.google.com/store/apps/details?id=app.rork.versgarant"

TITLE = "FreshGarant Video: How Long Does Food Keep? Everything New"
DESC = ("Watch how FreshGarant fills in how long food keeps, moves the date when you open something and freezes "
        "what expires today with one tap. Plus storage guides, leftovers, your week in one card and backups.")
THUMB = "/assets/images/video-new-thumb-1280.webp?v=20261128"

src = open(os.path.join(ROOT, "download.html"), encoding="utf-8").read()
css = re.search(r'<link rel="stylesheet" href="(/assets/css/global\.css\?v=\d+)"', src).group(1)
header = src[src.index('<header class="site-header">'):src.index("</header>") + len("</header>")]
header = header.replace(' class="active"', "", 1).replace('href="/download.html" class="active">EN', 'href="/video.html" class="active">EN')
header = header.replace('<a href="/download.html" class="active">EN</a>', '<a href="/video.html" class="active">EN</a>')
header = re.sub(r'<div class="lang-switch">.*?</div>', '<div class="lang-switch">\n        <a href="/video.html" class="active">EN</a>\n        <a href="/nl/">NL</a>\n      </div>', header, flags=re.S)
footer = src[src.index('<footer class="site-footer">'):src.index("</footer>") + len("</footer>")]
beacon = re.search(r"<!-- Cloudflare Web Analytics -->.*?<!-- End Cloudflare Web Analytics -->", src).group(0)

video_ld = {
    "@context": "https://schema.org", "@type": "VideoObject",
    "name": "How long does food keep? FreshGarant 2.2.9 – everything new",
    "description": DESC,
    "thumbnailUrl": [f"{SITE}{THUMB}", f"https://i.ytimg.com/vi/{YT}/maxresdefault.jpg"],
    "uploadDate": "2026-11-23T15:25:55-08:00", "duration": "PT1M55S",
    "embedUrl": f"https://www.youtube-nocookie.com/embed/{YT}",
    "contentUrl": f"https://www.youtube.com/watch?v={YT}",
    "publisher": {"@type": "Organization", "name": "Grounded Studio", "url": "https://grounded-studio.app/",
                  "logo": {"@type": "ImageObject", "url": f"{SITE}/assets/icons/icon_512.png"}},
}
crumbs_ld = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
    {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{SITE}/"},
    {"@type": "ListItem", "position": 2, "name": "Video", "item": f"{SITE}/video.html"}]}

page = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>{TITLE}</title>
<meta name="description" content="{DESC}" />
<meta name="theme-color" content="#2E7D32" />
<link rel="icon" type="image/png" sizes="64x64" href="/assets/icons/icon_favicon_64.png" />
<link rel="apple-touch-icon" sizes="512x512" href="/assets/icons/icon_512.png" />
<link rel="canonical" href="{SITE}/video.html" />
<meta property="og:title" content="{TITLE}" />
<meta property="og:description" content="{DESC}" />
<meta property="og:image" content="{SITE}{THUMB}" />
<meta property="og:type" content="video.other" />
<meta property="og:locale" content="en_US" />
<meta property="og:video" content="https://www.youtube.com/embed/{YT}" />
<meta property="og:site_name" content="FreshGarant" />
<link rel="preload" href="/assets/fonts/inter-latin.woff2" as="font" type="font/woff2" crossorigin />
<link rel="stylesheet" href="{css}" />
<script type="application/ld+json">{json.dumps(video_ld, ensure_ascii=False)}</script>
<script type="application/ld+json">{json.dumps(crumbs_ld, ensure_ascii=False)}</script>
</head>
<body>

{header}

<main>
<section class="section video-section">
  <div class="container">
    <nav class="breadcrumb" aria-label="Breadcrumb"><ol><li><a href="/">Home</a></li><li><span aria-current="page">Video</span></li></ol></nav>
    <h1 class="section-title" style="text-align:center;">How long does food keep?</h1>
    <div class="yt-video" style="margin-top: 28px;">
      <iframe src="https://www.youtube-nocookie.com/embed/{YT}?rel=0" title="How long does food keep? FreshGarant 2.2.9, everything new" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen loading="eager"></iframe>
    </div>
    <p class="yt-note">Plays from YouTube in privacy-enhanced mode. <a href="https://www.youtube.com/watch?v={YT}" target="_blank" rel="noopener">Watch on YouTube</a></p>

    <div class="prose" style="max-width: 720px; margin: 40px auto 0;">
      <h2>What you'll see</h2>
      <p>{DESC}</p>
      <ul>
        <li><strong>Shelf life, filled in:</strong> type what it is and FreshGarant fills in how long it keeps, also without a date on the pack.</li>
        <li><strong>Opened something?</strong> The date moves along by itself.</li>
        <li><strong>Expires today?</strong> Freeze it with one tap, with the right new date.</li>
        <li><strong>How long does it keep?</strong> On every product, with a link to the <a href="/guides/">storage guide</a>.</li>
        <li><strong>Leftovers, your week and backups:</strong> save dinner leftovers in one tap, get your week in one card every Sunday and take everything to a new phone.</li>
        <li><strong>What's for dinner?</strong> One fridge photo, three dinners with what you already have.</li>
      </ul>
      <h2>Earlier video: never waste food again</h2>
      <p>The full tour: use these first, your kitchen at a glance, adding in seconds, AI recipes, the weekly meal plan and the smart shopping list.</p>
      <div class="yt-video" style="margin: 18px 0 8px;">
        <iframe src="https://www.youtube-nocookie.com/embed/{YT_OLD}?rel=0" title="FreshGarant: never waste food again" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen loading="lazy"></iframe>
      </div>
      <p><a class="btn btn-primary" href="{PLAY}" target="_blank" rel="noopener" style="color:#fff; text-decoration:none;">Download FreshGarant free →</a></p>
    </div>
  </div>
</section>
</main>

{footer}

{beacon}
</body>
</html>
"""
with open(os.path.join(ROOT, "video.html"), "w", encoding="utf-8", newline="\n") as f:
    f.write(page)
print("wrote video.html")

# Cross-promo block for the other Grounded Studio apps (re-added after every build).
import subprocess as _sp, sys as _sys, os as _os  # noqa: E402
_XP = r"C:\meten_weten_bouw\scripts\cross_promo.py"
if _os.path.exists(_XP):
    _sp.run([_sys.executable, "-I", _XP, "freshgarant"], check=False)

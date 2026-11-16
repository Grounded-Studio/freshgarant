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
YT = "a66ORi159Go"
PLAY = "https://play.google.com/store/apps/details?id=app.rork.versgarant"

TITLE = "FreshGarant Video: Never Waste Food Again"
DESC = ("Watch how FreshGarant tracks expiry dates in your fridge, freezer and pantry, reminds you before food goes off and helps reduce food waste.")

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
    "name": "FreshGarant – Never Waste Food Again | Expiry Tracker, AI Recipes & Meal Planner",
    "description": DESC,
    "thumbnailUrl": [f"{SITE}/assets/images/video-thumb-1280.webp?v=20261114", f"https://i.ytimg.com/vi/{YT}/maxresdefault.jpg"],
    "uploadDate": "2026-11-12T13:52:30-08:00", "duration": "PT1M39S",
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
<meta property="og:image" content="{SITE}/assets/images/video-thumb-1280.webp?v=20261114" />
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
    <h1 class="section-title" style="text-align:center;">Never waste food again</h1>
    <div class="yt-video" style="margin-top: 28px;">
      <iframe src="https://www.youtube-nocookie.com/embed/{YT}?rel=0" title="FreshGarant: never waste food again" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen loading="eager"></iframe>
    </div>
    <p class="yt-note">Plays from YouTube in privacy-enhanced mode. <a href="https://www.youtube.com/watch?v={YT}" target="_blank" rel="noopener">Watch on YouTube</a></p>

    <div class="prose" style="max-width: 720px; margin: 40px auto 0;">
      <h2>What you'll see</h2>
      <p>{DESC}</p>
      <ul>
        <li><strong>Use these first:</strong> the home screen shows what expires today, tomorrow and this week.</li>
        <li><strong>My kitchen:</strong> your fridge, freezer and pantry at a glance.</li>
        <li><strong>Add in seconds:</strong> quick add, receipt scan, barcode or one photo of your fridge.</li>
        <li><strong>Cook what needs to go:</strong> AI recipes and a weekly meal plan built from your own stock.</li>
        <li><strong>Smart shopping list</strong> that knows what's already at home, and a running total of what you save.</li>
      </ul>
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

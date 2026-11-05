"""Phone mockups for the website: an app screenshot inside a modern device
frame (thin black bezel, metal rim, punch-hole camera, side buttons) on a
transparent background. The page adds the drop shadow with CSS.

Sources: the promo recording frames (promo/frames) and the app tour
(screenshots/tour) of the app project next door.

Run from the site root:  python -I _tools/make_devices.py
Writes assets/devices/<lang>/<name>.webp
"""
import os

from PIL import Image, ImageDraw, ImageFilter

SITE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
APP = os.path.dirname(SITE)

# name -> (source per language). Source paths are relative to the app root;
# {lang} is filled in.
SHOTS = {
    # Home + What's-for-dinner come from the promo recording (they show the
    # new home card); everything else from the app tour, which ran with
    # nothing else on the emulator.
    "home": "promo/frames/{lang}/home.png",
    "tonight": "promo/frames/{lang}/tonight_results.png",
    "tonight-dish": "promo/frames/{lang}/tonight_dish.png",
    "kitchen": "screenshots/tour/{lang}/10_my_kitchen_0.png",
    "add": "screenshots/tour/{lang}/04_add_menu_0.png",
    "calendar": "screenshots/tour/{lang}/11_calendar_0.png",
    "stores": "screenshots/tour/{lang}/22_stores_0.png",
    "shopping": "screenshots/tour/{lang}/02_shopping_list_0.png",
    "recipe": "screenshots/tour/{lang}/15_recipe_detail_0.png",
    "fridge-scan": "screenshots/tour/{lang}/20_ai_fridge_scan_0.png",
    "receipt-scan": "screenshots/tour/{lang}/21_receipt_scan_0.png",
}

SCREEN_W = 560  # screen width in the output (2x for ~280 px on the page)


def device(screen: Image.Image) -> Image.Image:
    sw = SCREEN_W
    sh = round(screen.height * sw / screen.width)
    screen = screen.convert("RGB").resize((sw, sh), Image.LANCZOS)
    bezel, rim, btn = 14, 5, 6
    w = sw + 2 * (bezel + rim)
    h = sh + 2 * (bezel + rim)
    out = Image.new("RGBA", (w + 2 * btn, h), (0, 0, 0, 0))
    ox = btn
    d = ImageDraw.Draw(out)
    r_out, r_in = 78, 64
    # Side buttons (right: power; left: volume up/down).
    for x0, y0, bh in ((ox + w - 2, h * 0.26, h * 0.10), (ox - btn + 2, h * 0.20, h * 0.07),
                       (ox - btn + 2, h * 0.29, h * 0.07)):
        d.rounded_rectangle((x0, y0, x0 + btn, y0 + bh), 3, fill=(52, 56, 62, 255))
    # Metal rim: a vertical gradient, then the black bezel on top.
    rim_img = Image.new("RGBA", (w, h))
    rd = ImageDraw.Draw(rim_img)
    top, bot = (92, 98, 106), (38, 41, 46)
    for y in range(h):
        t = y / (h - 1)
        rd.line((0, y, w, y), fill=tuple(int(top[i] + (bot[i] - top[i]) * t) for i in range(3)) + (255,))
    mask = Image.new("L", (w, h), 0)
    ImageDraw.Draw(mask).rounded_rectangle((0, 0, w - 1, h - 1), r_out, fill=255)
    out.paste(rim_img, (ox, 0), mask)
    d = ImageDraw.Draw(out)
    d.rounded_rectangle((ox + rim, rim, ox + w - rim - 1, h - rim - 1), r_out - rim, fill=(8, 9, 11, 255))
    # Faint highlight along the rim.
    d.rounded_rectangle((ox + 1, 1, ox + w - 2, h - 2), r_out - 1, outline=(150, 156, 164, 110), width=1)
    # Screen with rounded corners.
    smask = Image.new("L", (sw, sh), 0)
    ImageDraw.Draw(smask).rounded_rectangle((0, 0, sw - 1, sh - 1), r_in, fill=255)
    sx, sy = ox + rim + bezel, rim + bezel
    out.paste(screen, (sx, sy), smask)
    # Punch-hole camera.
    cx, cy, cr = ox + w // 2, sy + 22, 9
    d.ellipse((cx - cr, cy - cr, cx + cr, cy + cr), fill=(6, 6, 8, 255))
    d.ellipse((cx - 4, cy - 4, cx + 1, cy + 1), fill=(40, 50, 70, 255))
    return out


def main():
    for lang in ("en", "nl"):
        dst = os.path.join(SITE, "assets", "devices", lang)
        os.makedirs(dst, exist_ok=True)
        for name, src in SHOTS.items():
            path = os.path.join(APP, src.format(lang=lang))
            img = device(Image.open(path))
            p = os.path.join(dst, name + ".webp")
            img.save(p, "WEBP", quality=84, method=6)
            print(lang, name, img.size, os.path.getsize(p) // 1024, "KB")


if __name__ == "__main__":
    main()

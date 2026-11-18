"""Photos du site : téléchargées une fois, passées en noir et blanc, recadrées et servies depuis /assets/img/.

Chaque adresse images.unsplash.com rencontrée dans une page devient un fichier local :
    /assets/img/<nom>-<largeur>x<hauteur>.webp
Le nom vient du texte alternatif de la photo (une fois pour toutes, dans images.json).
Ajouter `&bc=color` à l'adresse pour garder la couleur (annonces d'exemple).
"""
import hashlib
import html
import json
import pathlib
import re
import subprocess
import unicodedata
import urllib.parse

from PIL import Image, ImageFilter, ImageOps

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent
OUT = ROOT / "assets" / "img"
CACHE = HERE / ".img-cache"
NAMES_FILE = HERE / "images.json"
URL_RE = re.compile(r'https://images\.unsplash\.com/(photo-[0-9a-z-]+)\?([^"\'\s)<>]*)')
MAX_W = 2400
NAMES = json.loads(NAMES_FILE.read_text(encoding="utf-8")) if NAMES_FILE.exists() else {}
_orig = {}


def slugify(text, words=6):
    t = unicodedata.normalize("NFKD", html.unescape(text)).encode("ascii", "ignore").decode().lower()
    parts = [p for p in re.split(r"[^a-z0-9]+", t) if p and p not in {"un", "une", "le", "la", "les", "de", "du", "des", "d", "l", "et", "en", "sur", "a", "au"}]
    return "-".join(parts[:words]) or "photo"


def register(pid, alt):
    """Donne un nom de fichier stable à une photo (premier texte alternatif rencontré)."""
    if pid in NAMES:
        return
    base = slugify(alt) if alt else "photo"
    name = base
    if name in NAMES.values() or name == "photo":
        name = f"{base}-{hashlib.sha1(pid.encode()).hexdigest()[:4]}"
    NAMES[pid] = name
    NAMES_FILE.write_text(json.dumps(NAMES, ensure_ascii=False, indent=1, sort_keys=True) + "\n", encoding="utf-8")


def original(pid):
    if pid not in _orig:
        CACHE.mkdir(exist_ok=True)
        f = CACHE / f"{pid}.jpg"
        if not f.exists() or f.stat().st_size < 2000:
            url = f"https://images.unsplash.com/{pid}?ixlib=rb-4.1.0&fit=max&fm=jpg&q=90&w={MAX_W}"
            subprocess.run(["curl", "-sS", "--fail", "--retry", "3", "-o", str(f), url], check=True)
        _orig[pid] = Image.open(f).convert("RGB")
    return _orig[pid]


_LUT = [max(0, min(255, round((v - 128) * 1.06 + 128))) for v in range(256)]


def treat(im, color):
    if color:
        return im
    g = ImageOps.grayscale(im).point(_LUT)
    return g.convert("RGB")


def variant(pid, w, h=None, color=False):
    """Chemin public de la photo recadrée au centre en w x h (créée si besoin)."""
    if pid not in NAMES:
        register(pid, "")
    src = original(pid)
    ow, oh = src.size
    if h is None:
        h = round(w * oh / ow)
    scale = min(1, ow / w, oh / h)  # jamais d'agrandissement
    tw, th = max(1, round(w * scale)), max(1, round(h * scale))
    name = f"{NAMES[pid]}-{tw}x{th}{'-c' if color else ''}.webp"
    out = OUT / name
    if not out.exists():
        OUT.mkdir(parents=True, exist_ok=True)
        ratio = tw / th
        if ow / oh > ratio:
            cw, ch = round(oh * ratio), oh
        else:
            cw, ch = ow, round(ow / ratio)
        x, y = (ow - cw) // 2, (oh - ch) // 2
        im = src.crop((x, y, x + cw, y + ch)).resize((tw, th), Image.LANCZOS)
        im = treat(im, color)
        if tw <= 1200:
            im = im.filter(ImageFilter.UnsharpMask(radius=0.7, percent=30, threshold=2))
        im.save(out, "WEBP", quality=80, method=6)
    return "/assets/img/" + name


def scan(doc):
    """Enregistre le nom de chaque photo à partir des balises <img> d'une page."""
    for tag in re.findall(r"<img [^>]*>", doc):
        m = URL_RE.search(tag)
        if not m:
            continue
        alt = re.search(r'alt="([^"]*)"', tag)
        if alt and alt.group(1).strip():
            register(m.group(1), alt.group(1))


def localize(doc, site=""):
    """Remplace toutes les adresses Unsplash d'une page par les fichiers locaux."""
    def rep(m):
        q = dict(urllib.parse.parse_qsl(html.unescape(m.group(2))))
        w = int(q.get("w", 1600))
        h = int(q["h"]) if "h" in q else None
        return variant(m.group(1), w, h, color=q.get("bc") == "color")
    doc = URL_RE.sub(rep, doc)
    if site:
        doc = re.sub(r'(<script type="application/ld\+json">)(.*?)(</script>)',
                     lambda m: m.group(1) + m.group(2).replace('"/assets/img/', f'"{site}/assets/img/') + m.group(3), doc, flags=re.S)
    return doc


def used():
    """Fichiers réellement référencés (pour nettoyer les variantes devenues inutiles)."""
    keep = set()
    for f in ROOT.rglob("*.html"):
        if "_build" in f.parts:
            continue
        keep.update(re.findall(r"/assets/img/([\w.-]+\.webp)", f.read_text(encoding="utf-8")))
    return keep

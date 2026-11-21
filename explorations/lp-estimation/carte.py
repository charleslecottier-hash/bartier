"""Carte de la zone d'intervention, préparée à la génération des pages.

La commune de l'artisan est situé avec le service de géocodage de l'IGN, puis le plan IGN (style gris, adouci ici)
est rendu dans Chromium par map_render.js. La page publiée n'affiche qu'une image : aucun service de cartes
n'est appelé par le navigateur du visiteur.

Le plan IGN est sous Licence Ouverte 2.0 (Etalab) : usage commercial libre, en citant la source (« © IGN »).
Le résultat est gardé dans .cache/ : une nouvelle génération ne refait la carte que si la commune ou le rayon change.
"""
import hashlib
import json
import math
import pathlib
import shutil
import subprocess
from urllib.parse import urlencode

HERE = pathlib.Path(__file__).resolve().parent
CACHE = HERE / ".cache"
GEOCODE = "https://data.geopf.fr/geocodage/search"
STYLE = "https://data.geopf.fr/annexes/ressources/vectorTiles/styles/PLAN.IGN/gris.json"
W, H, R = 760, 520, 140  # taille de la carte (px CSS, rendue en x2) et rayon du cercle de la zone (px CSS)
VERSION = 1  # à augmenter quand le style change, pour refaire les cartes en cache

# éléments du plan qui chargent la carte sans aider à se repérer
DROP = {"toponyme_routier_numero_lin", "toponyme_routier_borne", "toponyme_routier_odonyme_lin", "toponyme_routier_liaison_lin",
        "bati_ponc", "toponyme_bati_ponc", "oro_relief", "oro_courbe", "oro_lin", "oro_ponc", "toponyme_oro_ponc", "toponyme_oro_lin",
        "toponyme_ocs_ponc", "toponyme_ocs_lin", "toponyme_limite_ponc", "toponyme_parcellaire_adresse_ponc", "ocs_nature_sol_surf"}


def _get(url):
    r = subprocess.run(["curl", "-sSf", "--max-time", "25", url], capture_output=True)
    if r.returncode:
        raise RuntimeError(r.stderr.decode()[:160].strip() or "réseau indisponible")
    return r.stdout


def geocode(ville, code_postal=""):
    q = {"q": ville, "type": "municipality", "limit": 1}
    if code_postal:
        q["postcode"] = code_postal
    feats = json.loads(_get(f"{GEOCODE}?{urlencode(q)}"))["features"]
    if not feats:
        raise RuntimeError(f"commune introuvable : {ville}")
    (lon, lat), p = feats[0]["geometry"]["coordinates"], feats[0]["properties"]
    return dict(nom=p["name"], dep=p.get("depcode", ""), lon=lon, lat=lat)


def style(nom):
    """Plan IGN gris, plus clair et plus calme : fond gris très pâle, réseaux estompés, eau légèrement bleutée,
    sans numéros de route ni pictogrammes. Le nom de la commune de l'artisan est retiré : la page l'affiche par-dessus."""
    s = json.loads(_get(STYLE))
    keep = []
    for l in s["layers"]:
        sl = l.get("source-layer", "")
        if sl in DROP:
            continue
        p = l.setdefault("paint", {})
        if l["id"] == "bckgrd":
            p["fill-color"] = "#F1F3F6"
        elif sl == "hydro_surf":
            p.pop("fill-pattern", None)
            p["fill-color"], p["fill-outline-color"] = "#D3DDE7", "#D3DDE7"
        elif l["type"] == "fill":
            p["fill-opacity"] = 0.35
        elif l["type"] == "line":
            p["line-opacity"] = 0.75 if sl.startswith("hydro") else 0.42
            if sl.startswith("hydro"):
                p["line-color"] = "#BFCEDC"
        elif l["type"] == "symbol":
            p["icon-opacity"] = 0.6
            if "text-field" in l.get("layout", {}):
                p["text-color"] = "#4A5263" if sl == "toponyme_localite_ponc" else "#7C8494"
                p["text-halo-color"], p["text-halo-width"] = "#F1F3F6", 1.5
            if sl == "toponyme_localite_ponc":
                f = l.get("filter")
                expr = bool(f) and '["get"' in json.dumps(f)  # filtre en expressions ou à l'ancienne syntaxe
                cond = (["!", ["in", ["get", "texte"], ["literal", [nom, nom.upper()]]]] if expr else ["!in", "texte", nom, nom.upper()])
                l["filter"] = ["all", f, cond] if f else cond
        keep.append(l)
    s["layers"] = keep
    return s


def zoom(lat, km):
    """Niveau de zoom où le rayon de la zone mesure R pixels (tuiles de 512 px)."""
    return math.log2(40075016.686 * math.cos(math.radians(lat)) * R / (512 * km * 1000))


def prepare(cfg, out):
    """Renvoie la zone {nom, dep, lat, lon, km, url} et copie la carte dans out/assets/ (url vide si elle n'a pas pu être faite)."""
    ville, km = cfg.get("ville", "").strip(), cfg.get("rayon_km")
    if not ville or not km:
        return None, "sans carte (champs « ville » et « rayon_km » vides)"
    CACHE.mkdir(exist_ok=True)
    key = f"{ville}|{cfg.get('code_postal', '')}|{km}|{VERSION}"
    tag = hashlib.sha1(key.encode()).hexdigest()[:10]
    meta_f = CACHE / "zones.json"
    metas = json.loads(meta_f.read_text(encoding="utf-8")) if meta_f.exists() else {}
    z = metas.get(key)
    png = CACHE / f"carte-{tag}.png"
    try:
        if not z:
            z = geocode(ville, cfg.get("code_postal", ""))
            z["km"] = km
            z["file"] = png.name
            metas[key] = z
            meta_f.write_text(json.dumps(metas, ensure_ascii=False, indent=1), encoding="utf-8")
        png = CACHE / z["file"]
        if not png.exists():
            if not shutil.which("node"):
                raise RuntimeError("Node absent")
            jf = CACHE / "jobs.json"
            jf.write_text(json.dumps([{"out": str(png), "lon": z["lon"], "lat": z["lat"], "zoom": zoom(z["lat"], km),
                                       "w": W, "h": H, "style": style(z["nom"])}]), encoding="utf-8")
            r = subprocess.run(["node", str(HERE / "map_render.js"), str(jf)], capture_output=True, text=True, cwd=HERE)
            jf.unlink()
            if r.returncode or not png.exists():
                png.unlink(missing_ok=True)  # une carte ratée ne doit pas rester en cache
                raise RuntimeError((r.stderr.strip().splitlines() or ["rendu impossible"])[-1][:160])
    except (RuntimeError, OSError, KeyError, ValueError) as err:
        return (dict(z, url="") if z else None), f"carte impossible ({err})"
    from PIL import Image
    dst = out / "assets" / "carte.webp"
    Image.open(png).convert("RGB").save(dst, "WEBP", quality=80, method=6)
    return dict(z, url="/assets/carte.webp"), f"carte faite ({z['nom']}, {km} km, {dst.stat().st_size // 1024} Ko)"

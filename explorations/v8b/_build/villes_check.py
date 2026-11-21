"""Contrôle qualité des fiches ville (villes_new/<slug>.py) avant publication.

    python3 villes_check.py                 # toutes les fiches de villes_new/
    python3 villes_check.py bordeaux nice   # certaines fiches
    python3 villes_check.py --net bordeaux  # vérifie aussi que chaque lien répond

Une fiche en erreur, ou marquée DRAFT, n'est pas publiée (villes.py ne charge que les fiches qui passent).
Les pages ville ne valent que par leur contenu local et sourcé : ce contrôle bloque les fiches trop minces,
les copies d'une autre ville, les chiffres sans source et les promesses que Bartier & Co ne peut pas tenir.
"""
import importlib.util
import pathlib
import re
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
NEW = HERE / "villes_new"
sys.path.insert(0, str(HERE))

REQ = ["slug", "name", "cp", "insee", "lat", "lon", "dept", "depcode", "region", "wiki", "wikidata", "verified", "tldr", "hook", "title",
       "desc", "figures_intro", "figures", "answer", "facts", "trades_intro", "trades", "steps_intro", "steps", "aides_intro", "aides", "faq"]
TRADES = ["toiture", "facade", "fenetres", "charpente", "isolation"]
BANNED = [("—", "tiret cadratin"), ("–", "tiret demi-cadratin"), ("!", "point d’exclamation"), ("nos artisans", "promesse de présence"),
          ("n’hésitez", "formule creuse"), ("n'hésitez", "formule creuse"), ("incontournable", "mot creux"), ("véritable", "mot creux"),
          ("sous 48", "promesse de délai"), ("sous 24 h", "promesse de délai"), ("présents partout", "promesse de présence"),
          ("partout à", "promesse de présence"), ("nos clients", "preuve inventée"), ("avis client", "preuve inventée"),
          ("ce n’est pas", "tournure « pas X mais Y »"), ("ce n'est pas", "tournure « pas X mais Y »"), ("il est important de", "amorce"),
          ("wikipedia.org/wiki/", None)]
TEL = re.compile(r"(?<![\d+])0[1-9](?: \d{2}){4}(?!\d)")
NUM = re.compile(r"\d[\d  ]*(?:,\d+)?\s?(?:<small>)?\s?(?:%|€|ans\b|jours\b|km\b|m²|hectares\b|ha\b|mm\b|°C)")
TAG = re.compile(r"<[^>]+>")


def load(path):
    spec = importlib.util.spec_from_file_location("ville_" + path.stem, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def plain(s):
    return re.sub(r"\s+", " ", TAG.sub(" ", s)).strip()


def text_of(c):
    parts = [c["answer"]] + [b for _, b in c["facts"]] + [p for k in TRADES for p in c["trades"].get(k, [])] + [a for _, a in c["faq"]]
    return plain(" ".join(parts)).lower()


def shingles(t, n=6):
    w = re.findall(r"[a-zàâçéèêëîïôûùüÿœ’']+", t)
    return {" ".join(w[i:i + n]) for i in range(len(w) - n + 1)}


def others():
    """Textes des autres villes (fiches publiées et nouvelles), pour repérer les copies."""
    import villes_data
    out = {c["slug"]: shingles(text_of(c)) for c in villes_data.CITIES}
    for p in sorted(NEW.glob("*.py")):
        try:
            out[p.stem] = shingles(text_of(load(p).CITY))
        except Exception:
            pass
    return out


def links(s):
    return re.findall(r'href="([^"]+)"', s)


def check(path, net=False, pool=None):
    err, warn = [], []
    try:
        mod = load(path)
        c = mod.CITY
    except Exception as x:
        return [f"le fichier ne s’importe pas : {x}"], [], None
    if getattr(mod, "DRAFT", None):
        warn.append(f"marquée brouillon : {mod.DRAFT}")
    if not getattr(mod, "REVIEWED", None):
        warn.append("pas encore contre-vérifiée (pas de ligne REVIEWED) : non publiée")
    for k in REQ:
        if k not in c:
            err.append(f"champ manquant : {k}")
    if err:
        return err, warn, c
    if c["slug"] != path.stem:
        err.append(f"slug « {c['slug']} » différent du nom de fichier")
    if not re.fullmatch(r"[a-z0-9-]+", c["slug"]):
        err.append("slug invalide")
    if c["title"] != f"Devis travaux {c.get('a') or 'à ' + c['name']} : toiture, façade, fenêtres, isolation":
        warn.append("titre différent du modèle « Devis travaux à <ville> : toiture, façade, fenêtres, isolation »")
    if re.search(r"(?:^|\s)(?:à|de) (?:Le|Les) [A-ZÉ]", plain(" ".join([c["title"], c["desc"], c["answer"], c["tldr"]]))) or " à Le " in str(c) or " à Les " in str(c):
        err.append("« à Le … » : ajoutez la préposition de la ville (champ a=\"au Havre\") et écrivez « au Havre », « du Havre »")
    n = len(plain(c["desc"]))
    if not 120 <= n <= 165:
        err.append(f"desc : {n} caractères (visez 140 à 160)")
    if len(c["figures"]) != 4 or any(len(f) != 3 or "href" not in f[2] for f in c["figures"]):
        err.append("figures : 4 chiffres attendus, chacun avec sa source S(…)")
    insee = sum("insee.fr" in f[2] for f in c["figures"])
    if insee < 2:
        warn.append(f"figures : {insee} chiffre(s) Insee (au moins 2 attendus)")
    if not 5 <= len(c["facts"]) <= 6:
        err.append(f"facts : {len(c['facts'])} (5 ou 6 attendus)")
    nolink = [a for a, b in c["facts"] if "href" not in b]
    if nolink:
        err.append("facts sans source : " + ", ".join(nolink))
    for k in TRADES:
        ps = c["trades"].get(k)
        if not ps or len(ps) != 2:
            err.append(f"trades[{k}] : 2 paragraphes attendus")
        elif any(len(plain(p)) < 60 for p in ps):
            warn.append(f"trades[{k}] : paragraphe très court")
    if not 4 <= len(c["steps"]) <= 5:
        err.append(f"steps : {len(c['steps'])} (4 ou 5 attendus)")
    import villes_data
    if not c["aides"] or c["aides"][-1] != villes_data.NATIONAL:
        err.append("aides : NATIONAL doit être la dernière")
    if c["aides"] and not TEL.search(c["aides"][0][1]):
        err.append("aides : la première (Espace Conseil France Rénov’) doit donner un téléphone au format 03 59 00 03 59")
    if len(c["aides"]) < 3:
        warn.append("aides : moins de deux aides locales")
    if not 5 <= len(c["faq"]) <= 6:
        err.append(f"faq : {len(c['faq'])} (5 ou 6 attendues)")
    if not re.fullmatch(r"Q\d+", c["wikidata"]):
        err.append("wikidata : identifiant Q… attendu")
    if not (41 < c["lat"] < 51.5 and -5.5 < c["lon"] < 10):
        err.append("coordonnées hors de la France métropolitaine")
    if not re.fullmatch(r"\d{5}", c["insee"] if c["depcode"][:2] != "2A" else "20000"):
        warn.append("code Insee à vérifier")
    # style et promesses
    allt = " ".join([c["tldr"], c["hook"], c["desc"], c["answer"], c["figures_intro"], c["trades_intro"], c["steps_intro"], c["aides_intro"]]
                    + [x for f in c["figures"] for x in f[:2]] + [x for f in c["facts"] for x in f] + [p for k in TRADES for p in c["trades"].get(k, [])]
                    + [x for s in c["steps"] for x in s] + [x for s in c["aides"][:-1] for x in s] + [x for q in c["faq"] for x in q])
    low = allt.lower()
    for w, why in BANNED:
        if why and w.lower() in low:
            err.append(f"« {w} » : {why}")
        if why is None and w in allt:
            err.append("Wikipedia citée comme source d’un fait")
    if re.search(r"\s-\s", plain(allt)):
        warn.append("tiret entre espaces (remplacez par une virgule, deux-points ou parenthèses)")
    if "'" in plain(allt).replace("href=", ""):
        warn.append("apostrophe droite ' : utilisez ’")
    # chiffres sans source : un paragraphe chiffré doit avoir un lien, ou reprendre un chiffre déjà sourcé
    sourced = set()
    for item in [f[0] + f[2] for f in c["figures"]] + [b for _, b in c["facts"]] + [p for k in TRADES for p in c["trades"][k]] + [b for _, b in c["aides"]]:
        if "href" in item:
            sourced |= {re.sub(r"\D", "", m) for m in NUM.findall(item)}
    for where, item in [(f"trades[{k}]", p) for k in TRADES for p in c["trades"][k]] + [("aides", b) for _, b in c["aides"][:-1]] + [("faq", a) for _, a in c["faq"]] + [("answer", c["answer"])]:
        if "href" in item:
            continue
        for m in NUM.findall(item):
            if re.sub(r"\D", "", m) not in sourced:
                warn.append(f"{where} : « {plain(m)} » sans source dans le paragraphe ni ailleurs dans la fiche")
    # copie d'une autre ville
    me = shingles(text_of(c))
    for slug, sh in (pool or {}).items():
        if slug == c["slug"] or not me or not sh:
            continue
        j = len(me & sh) / len(me | sh)
        if j > 0.12:
            err.append(f"texte trop proche de la fiche « {slug} » ({j:.0%} de passages communs)")
        elif j > 0.06:
            warn.append(f"passages communs avec « {slug} » ({j:.0%})")
    # liens
    urls = sorted(set(links(allt)) | {c["wiki"]})
    if len(urls) < 8:
        warn.append(f"seulement {len(urls)} sources différentes")
    if net:
        for u in urls:
            r = subprocess.run(["curl", "-sS", "-o", "/dev/null", "-L", "--max-time", "20", "-A", "Mozilla/5.0", "-w", "%{http_code}", u],
                               capture_output=True, text=True)
            code = r.stdout.strip()
            if code not in ("200", "202", "203", "206"):
                (warn if code in ("403", "429", "000") else err).append(f"lien {code} : {u}")
    return err, warn, c


def ok(path, pool=None):
    """Pour villes.py : la fiche est-elle publiable ? Elle doit passer ce contrôle, ne pas être un brouillon,
    et avoir été contre-vérifiée (ligne REVIEWED = "<date>" ajoutée après la relecture de ville-verificateur)."""
    err, _, _ = check(path, pool=pool)
    try:
        mod = load(path)
        draft, reviewed, when = getattr(mod, "DRAFT", None), getattr(mod, "REVIEWED", None), getattr(mod, "PUBLISH", "")
    except Exception:
        draft, reviewed, when = True, None, ""
    import datetime
    later = bool(when) and datetime.date.today().isoformat() < when  # publication programmée (vagues espacées)
    if later:
        print(f"  {path.stem} : publication programmée le {when}")
    return not err and not draft and bool(reviewed) and not later


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    net = "--net" in sys.argv
    files = [NEW / f"{a}.py" for a in args] if args else sorted(NEW.glob("*.py"))
    pool = others()
    bad = 0
    for p in files:
        if not p.exists():
            print(f"{p.stem} : fichier introuvable ({p})")
            bad += 1
            continue
        err, warn, c = check(p, net=net, pool=pool)
        state = "ERREUR" if err else ("à revoir" if warn else "ok")
        print(f"{p.stem} : {state}")
        for x in err:
            print("  ✗", x)
        for x in warn:
            print("  ·", x)
        bad += bool(err)
    sys.exit(1 if bad else 0)

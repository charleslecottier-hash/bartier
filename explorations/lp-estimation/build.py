"""Pages d'estimation pour les clients artisans de Bartier & Co (une page par métier, au nom du client).

    python3 build.py                      # toutes les fiches de clients/
    python3 build.py clients/exemple.json # une seule fiche

Chaque fiche produit dist/<slug>/ : une page par métier (/<métier>/), les polices, le logo et un vercel.json.
Ce dossier se déploie seul, sur le domaine du client. Rien n'est relié au site bartierandco.com.
"""
import base64
import hashlib
import html
import json
import pathlib
import re
import shutil
import subprocess
import sys
import unicodedata
from urllib.parse import quote, urlparse

import icons
from metiers import COMMON, M

HERE = pathlib.Path(__file__).resolve().parent
FONTS = HERE.parent / "v8b" / "assets" / "fonts"
ORDER = ["toiture", "facade", "fenetres", "charpente", "isolation"]
GEO = "https://geo.api.gouv.fr"  # API publique de l'État : nom de la commune à partir du code postal
MISS = {"travaux": "le type de travaux", "couverture": "votre couverture actuelle", "gouttieres": "la réponse sur les gouttières",
        "support": "le type de mur", "hauteur": "la hauteur de la maison", "fissures": "la réponse sur les fissures", "materiau": "le matériau",
        "vitrage": "le vitrage actuel", "volets": "la réponse sur les volets", "signes": "ce que vous avez remarqué",
        "combles": "l’accès aux combles", "maison": "le type de maison", "acces": "l’accès aux combles", "chauffage": "votre chauffage",
        "logement": "le type de logement", "annee": "l’année de construction", "delai": "le délai", "statut": "votre situation"}
SVG = {  # pictogrammes au trait (grille de 24)
    "phone": '<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8.1 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z"/>',
    "alert": '<path d="M10.3 3.9 1.8 18a2 2 0 0 0 1.7 3h17a2 2 0 0 0 1.7-3L13.7 3.9a2 2 0 0 0-3.4 0z M12 9v4 M12 17h.01"/>',
    "arrow": '<path d="M5 12h14 M13 6l6 6-6 6"/>',
    "down": '<path d="M12 5v14 M6 13l6 6 6-6"/>',
    "back": '<path d="M15 18l-6-6 6-6"/>',
    "check": '<path d="M20 6 9 17l-5-5"/>',
    "lock": '<path d="M5 11h14v10H5z M8 11V7a4 4 0 0 1 8 0v4"/>',
    "pin": '<path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0z"/><circle cx="12" cy="10" r="3"/>',
    "minus": '<path d="M5 12h14"/>',
    "plus": '<path d="M12 5v14 M5 12h14"/>',
    "share": '<path d="M12 3v12 M8 7l4-4 4 4 M5 12v7a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1v-7"/>',
    "wa": '<path d="M3.5 20.5l1.3-4.2A8.5 8.5 0 1 1 8 19.4z M9 8.5c0 3.5 3 6.5 6.5 6.5l1-1.5-2-1-1 .8c-1-.4-2.4-1.8-2.8-2.8l.8-1-1-2z"/>',
}


def clover_bg(col="#0A1424", op=".06"):
    """Fond : trèfles à quatre feuilles en motif, dessinés en SVG (aucune image externe)."""
    leaf = "M0 0C-3-3-5-8-2-9-.8-9.4 0-8.5 0-7.5 0-8.5.8-9.4 2-9 5-8 3-3 0 0Z"
    def clover(x, y, r, k):
        leaves = "".join(f'<path d="{leaf}" transform="rotate({a})"/>' for a in (0, 90, 180, 270))
        return (f'<g transform="translate({x} {y}) rotate({r}) scale({k})" fill="{col}" fill-opacity="{op}">{leaves}'
                f'<path d="M0 0q2 5 6 8" fill="none" stroke="{col}" stroke-opacity="{op}" stroke-width="1.6" stroke-linecap="round"/></g>')
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="168" height="168" viewBox="0 0 168 168">'
           f'{clover(38, 40, 14, 1.25)}{clover(122, 120, -24, 1.05)}{clover(124, 34, 52, .7)}{clover(40, 128, -60, .8)}</svg>')
    return "data:image/svg+xml," + svg.replace("%", "%25").replace("#", "%23").replace("<", "%3C").replace(">", "%3E").replace('"', "'")


def who(cfg, photo_url=""):
    """Avatar et nom de la personne qui rappelle, d'après la fiche (« contact »)."""
    c = cfg.get("contact", {})
    pre, role = c.get("prenom", "").strip(), c.get("role", "").strip()
    name = pre or cfg["entreprise"]
    ini = "".join(w[0] for w in re.split(r"[\s-]+", name) if w)[:2].upper()
    av = f'<img src="{photo_url}" alt="" width="96" height="96">' if photo_url else f"<span>{html.escape(ini)}</span>"
    title = f"{pre}, {role}" if pre and role else name
    return av, title, bool(pre)


def stars(cfg):
    r = cfg.get("avis") or {}
    if not r.get("note") or not r.get("nombre"):
        return ""
    note = f'{float(r["note"]):.1f}'.replace(".", ",")
    inner = f'<span class="es-stars" aria-hidden="true">★★★★★</span><b>{note}</b>/5 · {int(r["nombre"])} avis Google'
    return (f'<a class="es-rev" href="{a(r["lien"])}" target="_blank" rel="noopener">{inner}</a>' if r.get("lien")
            else f'<p class="es-rev">{inner}</p>')


def slug(t):
    t = unicodedata.normalize("NFKD", t).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", "-", t).strip("-")


def euro(n):
    return f"{int(round(n)):,}".replace(",", "\u202f") + "\u00a0€"


def example(m, cfg, key):
    """Estimation d'exemple affichée en haut de page : première option chiffrée, quantité proposée par défaut."""
    opts = cfg_js(key, m, cfg)["opts"]
    label = next(o[0] for o in m["steps"][0]["qs"][0]["opts"] if opts[o[0]]["lines"])
    focus = next(o[2] for o in m["steps"][0]["qs"][0]["opts"] if o[0] == label)
    qty = m["steps"][1]["qs"][0]["val"]
    lines, groups = opts[label]["lines"], {}
    for x in lines:
        g = groups.setdefault(x.get("g") or id(x), [x["lo"], x["hi"]])
        g[0], g[1] = min(g[0], x["lo"]), max(g[1], x["hi"])
    lo = sum(g[0] for g in groups.values()) * qty
    hi = sum(g[1] for g in groups.values()) * qty
    step = 10 if lo < 1000 else 100
    if lo == hi:
        amount = "environ " + euro(round(lo / 100) * 100)
    else:
        amount = euro(lo // step * step) + " à " + euro(-(-hi // step) * step)
    unit = m["qty"]["many"] if qty > 1 else m["qty"]["one"]
    return focus, amount, f"{label} · {qty} {unit}"


def faq_html(m, cfg, key):
    ent = cfg["entreprise"]
    own = bool(cfg.get("tarifs", {}).get(key))
    c = cfg.get("contact", {})
    pre, role, rappel = c.get("prenom", "").strip(), c.get("role", "").strip(), cfg.get("rappel", "").strip()
    who_txt = (f"{pre}, {role} de {ent}." if pre and role else f"{pre}, de {ent}." if pre else f"{ent}.") + (f" {rappel}." if rappel else "")
    qa = [("L’estimation est-elle gratuite ?", "Oui. Elle est gratuite et ne vous engage à rien."),
          ("D’où viennent les prix ?", f"Des tarifs indicatifs de {ent}, pose comprise." if own else
           f"Des prix moyens publiés par {m['sources']}, pose comprise. Chaque ligne de l’estimation cite sa source et sa date."),
          ("Le prix final sera-t-il le même ?", "C’est une fourchette indicative. Le prix ferme se donne sur devis, après une visite : l’état du support, l’accès et les finitions changent le montant.")]
    qa += [(q, r.replace("{tel}", cfg.get("telephone", ""))) for q, r in m.get("faq", [])]
    qa += [("Qui va me rappeler ?", who_txt + " Votre numéro ne sert qu’à ce projet : il n’est ni vendu ni cédé."),
           ("Je suis locataire, puis-je faire l’estimation ?", "Oui. Les travaux sur le bâti se décident avec le propriétaire : faites l’estimation, puis transmettez-la-lui.")]
    items = "".join(f"<details><summary>{e(q)}</summary><p>{e(r)}</p></details>" for q, r in qa)
    return f'<section class="es-faq" aria-labelledby="es-faq-h"><h2 id="es-faq-h">Vos questions</h2><div class="es-faq-list">{items}</div></section>'


def og_html(m, cfg, key, accent, photo_file=None):
    """Page 1200 × 630 rendue en image : titre, maison du métier, exemple d'estimation, nom de l'artisan."""
    font = base64.b64encode((FONTS / "host-grotesk-latin.woff2").read_bytes()).decode()
    focus, amount, label = example(m, cfg, key)
    h1 = re.sub(r"<mark>(.*?)</mark>", lambda x: "<mark>" + x.group(1).replace(" ", "\u00a0") + "</mark>", fr(m["h1"]))
    zone = f" · {e(cfg['zone'])}" if cfg.get("zone") else ""
    if photo_file:
        mime = "image/webp" if photo_file.suffix == ".webp" else "image/png" if photo_file.suffix == ".png" else "image/jpeg"
        photo = f'<img src="data:{mime};base64,{base64.b64encode(photo_file.read_bytes()).decode()}" alt="">'
    else:
        photo = icons.house(focus, None, accent, s=16)
    return f"""<!doctype html><html lang="fr"><head><meta charset="utf-8"><style>
@font-face{{font-family:H;font-weight:300 600;src:url(data:font/woff2;base64,{font}) format("woff2")}}
*{{margin:0;box-sizing:border-box}}
body{{width:1200px;height:630px;overflow:hidden;font-family:H,sans-serif;color:#0A1424;background:#F4F5F7 url("{clover_bg()}") 0 0/168px 168px repeat;display:grid;grid-template-columns:600px 1fr;align-items:center;padding:56px 64px}}
.pill{{display:inline-block;padding:10px 20px;border-radius:999px;background:#FFE15A;font-size:22px;font-weight:500}}
h1{{margin-top:24px;font-size:76px;font-weight:600;line-height:1.04;letter-spacing:-.04em}}
mark{{display:inline-block;margin:4px 0;padding:0 12px 4px;border-radius:8px;background:#0A1424;color:#fff}}
em{{font-style:italic;text-decoration:underline;text-decoration-color:#16A34A;text-decoration-thickness:6px;text-underline-offset:8px}}
.by{{margin-top:28px;font-size:24px;color:#2B3444}}.by b{{font-weight:500;color:#0A1424}}
.art{{position:relative;height:518px;border-radius:28px;background:linear-gradient(180deg,#fff,#EDF0F4);border:1px solid rgba(10,20,36,.1);display:grid;place-items:center}}
.art svg{{width:400px;height:auto;margin-top:-40px}}.art img{{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;border-radius:27px}}
.tag{{position:absolute;left:24px;bottom:24px;padding:16px 22px;border-radius:16px;background:#fff;box-shadow:0 0 0 1px rgba(10,20,36,.1),0 18px 40px -20px rgba(10,20,36,.5)}}
.tag span{{display:block;font-size:18px;color:#5B6475}}.tag b{{display:block;margin:2px 0;font-size:34px;font-weight:600;letter-spacing:-.02em}}.tag i{{font-style:normal;font-size:18px;color:#2B3444}}
</style></head><body><div><p class="pill">{e(m["pill"])}</p><h1>{h1}</h1><p class="by"><b>{e(cfg["entreprise"])}</b>{zone}</p></div>
<div class="art">{photo}<div class="tag"><span>Exemple d’estimation</span><b>{e(amount)}</b><i>{e(label)}</i></div></div></body></html>"""


def photo_of(m, cfg, key):
    """Photo du haut de page : celle du client si sa fiche en donne une (ses vrais chantiers), sinon la photo libre de droits du métier."""
    own = cfg.get("photos", {}).get(key)
    if own:
        return dict(own=own, alt=f"Un chantier de {cfg['entreprise']}", pos="center")
    return dict(m["photo"], own=None)


def favicon(accent):
    svg = (f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'><rect width='32' height='32' rx='8' fill='{accent}'/>"
           "<path d='M16 7l9 7.5V25h-6v-6h-6v6H7V14.5z' fill='white'/></svg>")
    return "data:image/svg+xml," + quote(svg, safe="/:=' ")


def ico(k, cls=""):
    c = f' class="{cls}"' if cls else ""
    return f'<svg{c} viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false">{SVG[k]}</svg>'


def fr(s):
    """Typographie française : espace insécable avant ? ! : ; » et après «, entre un nombre et son unité."""
    s = re.sub(r" ([?!:;»])", "\u00a0\\1", s).replace("« ", "«\u00a0")
    return re.sub(r"(\d) (?=[A-Za-zÀ-ÿ€%])", "\\1\u00a0", s)


def e(s):
    return html.escape(fr(str(s)), quote=False)


def a(s):
    return html.escape(str(s), quote=True)


def need(cfg, warn):
    lg = cfg.get("legal", {})
    for k, lab in [("raison_sociale", "raison sociale"), ("forme", "forme juridique"), ("siege", "siège"), ("siret", "SIRET"),
                   ("directeur_publication", "directeur de la publication"), ("email", "e-mail de contact"), ("hebergeur", "hébergeur")]:
        if not str(lg.get(k, "")).strip():
            warn.append(f"mentions légales : {lab} manquant")
    if not cfg.get("telephone"):
        warn.append("téléphone manquant")
    if not cfg.get("envoi") and not cfg.get("whatsapp"):
        warn.append("aucune réception des demandes : renseignez « envoi » (adresse qui reçoit les demandes) ou « whatsapp »")


# ——— Questions ———
CK = f'<span class="es-ck" aria-hidden="true">{ico("check")}</span>'


def q_html(q, sid, accent, cfg):
    n = q["name"]
    miss = a(MISS.get(n, "une réponse"))
    if q["t"] == "cards":
        opts = "".join(
            f'<button type="button" class="es-opt" data-q="{n}" data-v="{a(o[0])}" data-slug="{slug(o[0])}" aria-pressed="false">{CK}'
            f'<span class="es-ico">{icons.house(o[2], o[3], accent)}</span>'
            f'<span class="es-ot"><b>{e(o[0])}</b><span>{e(o[1])}</span></span></button>'
            for o in q["opts"])
        return f'<div class="es-opts" role="group" aria-labelledby="{sid}" data-req="{n}" data-miss="{miss}">{opts}</div>'
    if q["t"] == "tiles":
        opts = "".join(
            f'<button type="button" class="es-tile" data-q="{n}" data-v="{a(lab)}" aria-pressed="false">{CK}<span class="es-sw">{icons.swatch(sw)}</span><span>{e(lab)}</span></button>'
            for lab, sw in q["opts"])
        return f'<div class="es-tiles" role="group" aria-labelledby="{sid}" data-req="{n}" data-miss="{miss}">{opts}</div>'
    if q["t"] == "range":
        units = list(q["units"]) if q.get("units") else q["unit"]
        lo = units[0] if isinstance(units, list) and q["min"] == 0 and units[0] else f'{q["min"]} {units if isinstance(units, str) else units[1 if q["min"] < 2 else 2]}'
        hi = f'{q["max"]} {units if isinstance(units, str) else units[2]}'
        return (f'<div class="es-field es-rangef"><label class="es-lab" for="es-{n}">{e(q["label"])}</label>'
                f'<div class="es-stepper"><button type="button" class="es-sb" data-step="-1" aria-label="Moins">{ico("minus")}</button>'
                f'<output for="es-{n}" aria-live="polite"></output>'
                f'<button type="button" class="es-sb" data-step="1" aria-label="Plus">{ico("plus")}</button></div>'
                f'<input class="es-range" type="range" id="es-{n}" data-q="{n}" min="{q["min"]}" max="{q["max"]}" step="{q["step"]}" value="{q["val"]}" data-units="{a(json.dumps(units, ensure_ascii=False))}">'
                f'<div class="es-mm" aria-hidden="true"><span>{e(lo)}</span><span>{e(hi)}</span></div></div>')
    if q["t"] in ("seg", "chips"):
        lid = f"es-l-{n}"
        multi = ' data-multi' if q.get("multi") else ""
        btns = "".join(
            f'<button type="button" class="es-chip" data-q="{n}" data-v="{a(o)}" aria-pressed="false"{multi}{" data-excl" if o == q.get("excl") else ""}>{e(o)}</button>'
            for o in q["opts"])
        show = f' data-show="{a(json.dumps(q["show"], ensure_ascii=False))}" hidden' if q.get("show") else ""
        return (f'<div class="es-field" data-req="{n}" data-miss="{miss}"{show}><p class="es-lab" id="{lid}">{e(q["label"])}</p>'
                f'<div class="es-seg" role="group" aria-labelledby="{lid}">{btns}</div></div>')
    if q["t"] == "cp":
        zone = (f'<p class="es-note es-zone" hidden>Ce code postal semble hors de la zone habituelle de {e(cfg["entreprise"])}'
                f'{" (" + e(cfg["zone"]) + ")" if cfg.get("zone") else ""}. Vous pouvez continuer : nous vous dirons si nous pouvons intervenir.</p>'
                if cfg.get("departements") else "")
        return (f'<div class="es-field"><label class="es-lab" for="es-cp">{e(q["label"])}</label>'
                f'<div class="es-cp-row"><input class="es-in es-in-cp" id="es-cp" name="code_postal" inputmode="numeric" autocomplete="postal-code" maxlength="5" placeholder="Ex. 69003">'
                f'<span class="es-cp-hint" aria-live="polite"></span></div></div>{zone}'
                '<p class="es-note es-tenant" hidden>Les travaux sur le bâti se décident avec le propriétaire. Faites l’estimation, puis transmettez-la-lui.</p>')
    raise ValueError(q["t"])


def steps_html(m, cfg, accent, photo_url=""):
    out = []
    allsteps = m["steps"] + COMMON
    for i, st in enumerate(allsteps):
        sid = f"es-q{i + 1}"
        auto = " data-auto" if st.get("auto") else ""
        body = "".join(q_html(q, sid, accent, cfg) for q in st["qs"])
        if i == 1:  # rappel du projet choisi, avec son illustration
            body = '<div class="es-ctx" hidden><span class="es-ctx-ico"></span><span><small>Votre projet</small><b class="es-ctx-t"></b></span></div>' + body
        out.append(f'<div class="es-step" role="group" aria-labelledby="{sid}"{auto}><h2 class="es-q" id="{sid}" tabindex="-1">{e(st["title"])}</h2>'
                   f'<p class="es-sub">{e(re.sub(r"\.$", "", st["sub"]) if st["sub"].count(". ") == 0 else st["sub"])}</p>{body}</div>')
    sid = f"es-q{len(allsteps) + 1}"
    out.append(
        f'<div class="es-step es-contact" role="group" aria-labelledby="{sid}"><h2 class="es-q" id="{sid}" tabindex="-1" data-h>Votre estimation est prête</h2>'
        '<p class="es-sub" data-s></p><ul class="es-recap" aria-label="Vos réponses"></ul>'
        f'<div class="es-teaser" aria-hidden="true"><p class="es-t-k">Estimation indicative</p><p class="es-blur">0 000 € à 0 000 €</p>'
        f'<p class="es-lock">{ico("lock")}Affichée dès que vous validez</p></div>'
        + who_card(cfg, photo_url) +
        '<div class="es-two">'
        '<div><label class="es-lab" for="es-prenom">Prénom</label><input class="es-in" id="es-prenom" name="prenom" autocomplete="given-name" maxlength="60"></div>'
        '<div><label class="es-lab" for="es-tel">Téléphone</label><input class="es-in" id="es-tel" name="telephone" type="tel" inputmode="tel" autocomplete="tel" maxlength="20" placeholder="06 12 34 56 78"></div>'
        '</div>'
        '<input class="es-hp" name="site_web" tabindex="-1" autocomplete="off" aria-hidden="true">'
        f'<p class="es-priv">{ico("lock")}<span class="es-consent">{e("En validant, vous acceptez d’être rappelé par " + cfg["entreprise"] + " au sujet de ce projet. Vos coordonnées ne servent qu’à cela : elles ne sont ni vendues ni cédées.")}</span></p></div>')
    return "".join(out), len(allsteps) + 1


def who_card(cfg, photo_url=""):
    av, title, person = who(cfg, photo_url)
    line = cfg.get("rappel") or "Rappel gratuit, sans engagement"
    head = f"{title}, vous rappelle" if person and "," in title else f"{title} vous rappelle"
    return f'<div class="es-who es-who-card"><span class="es-av">{av}</span><p><b>{e(head)}</b><span>{e(line)}</span></p></div>'


SHORT = {"couverture": "Couverture", "velux": "Fenêtres de toit", "gouttieres": "Gouttières à refaire", "support": "Mur", "hauteur": "Hauteur",
         "fissures": "Fissures", "materiau": "Matériau", "vitrage": "Vitrage actuel", "volets": "Volets à changer", "signes": "Signes",
         "combles": "Combles accessibles", "maison": "Maison", "acces": "Accès", "chauffage": "Chauffage", "logement": "Logement", "annee": "Construction"}


def details_keys(m):
    return [[q["name"], SHORT.get(q["name"], q.get("label", q["name"]))] for st in m["steps"] for q in st["qs"] if q["name"] not in ("travaux", m["qty"]["name"])]


def cfg_js(key, m, cfg):
    own = cfg.get("tarifs", {}).get(key, {})
    opts = {}
    for st in m["steps"]:
        for q in st["qs"]:
            if q["name"] != "travaux":
                continue
            for o in q["opts"]:
                lines = [dict(x) for x in o[4]]
                if o[0] in own and lines:
                    lo, hi = own[o[0]]
                    lines = [dict(lines[0], lo=lo, hi=hi, src=None, approx=False)]
                    lines[0].pop("if", None), lines[0].pop("g", None)
                for x in lines:
                    x["l"], x["u"] = fr(x["l"]), fr(x["u"])
                opts[o[0]] = dict(lines=lines, gl=fr(o[5]) if len(o) > 5 else "", vt=fr(m.get("visite_txt", {}).get(o[0], "")))
    tel = cfg.get("telephone", "")
    recap = [q["name"] for st in m["steps"] for q in st["qs"] if q["t"] == "tiles"]
    _, title, person = who(cfg)
    return dict(key=key, nom=m["nom"], ent=cfg["entreprise"], who=title if person else cfg["entreprise"], tel=tel, telh="+33" + re.sub(r"\D", "", tel)[1:] if tel else "",
                wa=re.sub(r"\D", "", cfg.get("whatsapp", "")), envoi=cfg.get("envoi", ""), deps=cfg.get("departements", []), zone=cfg.get("zone", ""),
                horaires=fr(cfg.get("horaires", "")), px=cfg.get("meta_pixel", ""), qty=m["qty"], opts=opts, recap=recap, geo=GEO,
                visite=[dict(r, txt=fr(r["txt"])) for r in m.get("visite", [])], notes=[dict(r, txt=fr(r["txt"])) for r in m.get("notes", [])],
                varie=fr(m["varie"]), aides=fr(m.get("aides", "")), details=details_keys(m), own=bool(own))


# ——— Pied de page : conditions, mentions légales, confidentialité ———
def legal_html(m, cfg, key):
    lg = cfg.get("legal", {})
    ent = cfg["entreprise"]
    f = lambda k: e(lg.get(k)) if str(lg.get(k, "")).strip() else "<i>[à compléter]</i>"
    srcs, seen = [], set()
    for st in m["steps"]:
        for q in st["qs"]:
            if q["name"] == "travaux":
                for o in q["opts"]:
                    for x in o[4]:
                        if x["src"][1] not in seen:
                            seen.add(x["src"][1])
                            srcs.append(f'<a href="{a(x["src"][1])}" target="_blank" rel="noopener">{e(x["src"][0])}</a>')
    own = bool(cfg.get("tarifs", {}).get(key))
    base = (f"les tarifs indicatifs de {e(ent)}, et à défaut des prix moyens publiés, pose comprise ({', '.join(srcs)})" if own
            else f"des prix moyens publiés, pose comprise ({', '.join(srcs)})")
    cond = (f"<p>Le calculateur multiplie la quantité que vous indiquez par {base}. Il ne voit pas votre chantier : l’état du support, l’accès, "
            "les finitions et les options changent le prix. Le résultat est une fourchette indicative, sans valeur contractuelle. "
            "Seul un devis signé, établi après une visite, engage sur un prix. L’estimation est gratuite et sans engagement.</p>")
    capital = f" au capital de {f('capital')}" if str(lg.get("capital", "")).strip() else ""
    rcs = f", RCS {f('rcs')}" if str(lg.get("rcs", "")).strip() else ""
    tva = f". TVA intracommunautaire {f('tva')}" if str(lg.get("tva", "")).strip() else ""
    ment = [f"<p>Éditeur : {f('raison_sociale')}, {f('forme')}{capital}. Siège : {f('siege')}. SIRET {f('siret')}{rcs}{tva}.</p>",
            f"<p>Directeur de la publication : {f('directeur_publication')}. Contact : {e(cfg.get('telephone', ''))}, {f('email')}.</p>"]
    if str(lg.get("assurance_decennale", "")).strip():
        ment.append(f"<p>Assurance décennale : {f('assurance_decennale')}.</p>")
    if str(lg.get("mediateur", "")).strip():
        ment.append(f"<p>Médiateur de la consommation : {f('mediateur')}.</p>")
    ment.append(f"<p>Hébergeur : {f('hebergeur')}.</p>")
    px = bool(cfg.get("meta_pixel"))
    priv = (f"<p>Responsable du traitement : {f('raison_sociale')}. Le prénom, le téléphone, le code postal et vos réponses servent à vous recontacter "
            "au sujet de votre projet et à préparer un devis, à votre demande. Ils sont conservés trois ans après le dernier contact, puis supprimés. "
            "Ils ne sont ni vendus ni cédés.</p>")
    if cfg.get("envoi"):
        priv += "<p>Votre demande transite par un prestataire technique qui agit pour notre compte et ne l’utilise pas pour lui-même.</p>"
    if cfg.get("whatsapp"):
        priv += "<p>Si vous envoyez votre demande par WhatsApp, elle passe par ce service, édité par Meta.</p>"
    priv += ("<p>Pendant votre visite, vos réponses restent dans votre navigateur (stockage de session), pour ne pas les perdre si la page se recharge. "
             "Elles s’effacent quand vous fermez l’onglet.</p>")
    priv += "<p>Le nom de votre commune s’affiche grâce à l’API publique de l’État (geo.api.gouv.fr), qui ne reçoit que le code postal.</p>"
    priv += (f"<p>Vous pouvez accéder à vos données, les rectifier, les effacer ou vous opposer à leur traitement en écrivant à {f('email')}. "
             "En cas de difficulté, vous pouvez saisir la CNIL (cnil.fr).</p>")
    priv += ("<p>Avec votre accord seulement, un cookie de Meta mesure l’efficacité de nos annonces. Sans accord, rien n’est déposé. "
             '<button type="button" class="es-cc-open">Changer mon choix</button></p>' if px else "<p>Ce site ne dépose aucun cookie et n’utilise aucun outil de mesure.</p>")
    return (f'<details><summary>Conditions d’utilisation</summary>{cond}</details>'
            f'<details id="mentions-legales"><summary>Mentions légales</summary>{"".join(ment)}</details>'
            f'<details id="confidentialite"><summary>Confidentialité</summary>{priv}</details>')


CSS = """
@font-face{font-family:"Host Grotesk";font-style:normal;font-weight:300 600;font-display:swap;src:url(/assets/fonts/host-grotesk-latin-ext.woff2) format("woff2");unicode-range:U+0100-02BA,U+02BD-02C5,U+02C7-02CC,U+02CE-02D7,U+02DD-02FF,U+0304,U+0308,U+0329,U+1D00-1DBF,U+1E00-1E9F,U+1EF2-1EFF,U+2020,U+20A0-20AB,U+20AD-20C0,U+2113,U+2C60-2C7F,U+A720-A7FF}
@font-face{font-family:"Host Grotesk";font-style:normal;font-weight:300 600;font-display:swap;src:url(/assets/fonts/host-grotesk-latin.woff2) format("woff2");unicode-range:U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+0304,U+0308,U+0329,U+2000-206F,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD}
:root{--bg:#F4F5F7;--ink:#0A1424;--ink2:#2B3444;--muted:#5B6475;--line:rgba(10,20,36,.1);--line2:rgba(10,20,36,.18);--soft:#F1F3F6;--go:#15803D;--go-h:#116B33;--go-bar:#16A34A;--go-bg:#EDF8F1;--go-ring:rgba(22,163,74,.2);--sun:#FFE15A;--ease:cubic-bezier(.2,.8,.2,1);--f:"Host Grotesk",system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;color-scheme:light}
*{box-sizing:border-box;margin:0}
html{-webkit-text-size-adjust:100%}
body{min-height:100vh;display:flex;flex-direction:column;font:400 16px/1.5 var(--f);color:var(--ink);background:var(--bg) url("__CLOVER__") 0 0/168px 168px repeat;-webkit-font-smoothing:antialiased}
a{color:inherit}
button{font:inherit;color:inherit;cursor:pointer;-webkit-tap-highlight-color:transparent;touch-action:manipulation}
:focus-visible{outline:2px solid var(--ink);outline-offset:3px}
[hidden]{display:none!important}
svg{display:block}
.es-hdr{display:flex;align-items:center;justify-content:space-between;gap:12px;width:100%;max-width:1180px;margin:0 auto;padding:12px 16px}
.es-logo{display:flex;align-items:center;min-height:44px}
.es-logo img{display:block;height:36px;width:auto;max-width:180px;object-fit:contain}
.es-name{font-weight:500;font-size:1.06rem;line-height:1.2}
.es-call{display:inline-flex;align-items:center;gap:8px;flex:none;min-height:44px;padding:0 16px;border-radius:999px;background:var(--go);color:#fff;text-decoration:none;font-weight:500;font-size:.95rem;font-variant-numeric:tabular-nums;box-shadow:inset 0 1px 0 rgba(255,255,255,.18),0 6px 16px -10px rgba(10,20,36,.6);transition:background .2s}
.es-call:hover{background:var(--go-h)}
.es-call svg{width:18px;height:18px}
.es-call .es-short{display:none}
@media (max-width:380px){.es-call .es-num{display:none}.es-call .es-short{display:inline}}
.es-main{flex:1;display:grid;gap:32px;width:100%;max-width:1180px;margin:0 auto;padding:4px 16px 48px}
.es-kick{display:flex;align-items:center;gap:8px;margin-bottom:16px;font-size:.9rem;color:var(--ink2)}
.es-kick svg{width:18px;height:18px;color:var(--muted)}
.es-pill{display:inline-flex;align-items:center;gap:8px;padding:8px 16px;border-radius:999px;background:var(--sun);font-size:.86rem;font-weight:500;line-height:1.3}
.es-pill svg{flex:none;width:18px;height:18px}
.es-h{margin-top:16px;font-weight:600;font-size:clamp(2.45rem,10.6vw,4.2rem);line-height:1.04;letter-spacing:-.04em}
.es-h mark{display:inline-block;margin:.05em 0;padding:.01em .15em .05em;border-radius:.11em;background:var(--ink);color:#fff}
.es-h em{font-style:italic;text-decoration:underline;text-decoration-color:var(--go-bar);text-decoration-thickness:.085em;text-underline-offset:.1em}
.es-lead{margin-top:16px;max-width:40ch;font-size:1.06rem;line-height:1.55;color:var(--ink2)}
.es-cta{display:flex;flex-direction:column;align-items:center;justify-content:center;gap:2px;width:100%;min-height:72px;margin-top:24px;padding:12px 20px;border-radius:16px;background:var(--go);color:#fff;text-decoration:none;box-shadow:inset 0 1px 0 rgba(255,255,255,.18),0 16px 32px -18px rgba(10,20,36,.6);transition:background .2s,transform .2s}
.es-cta:hover{background:var(--go-h)}
.es-cta:active{transform:scale(.985)}
.es-cta b{display:inline-flex;align-items:center;gap:8px;font-size:1.22rem;font-weight:600}
.es-cta b svg{width:20px;height:20px}
.es-cta small{font-size:.86rem;opacity:.9}
.es-trust{display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;gap:12px 20px;margin-top:20px;padding:12px 16px;border:1px solid var(--line);border-radius:16px;background:rgba(255,255,255,.88)}
.es-who{display:flex;align-items:center;gap:12px}
.es-who p{line-height:1.3}
.es-who b{display:block;font-weight:500}
.es-who p span{display:block;font-size:.88rem;color:var(--muted)}
.es-av{flex:none;display:grid;place-items:center;width:48px;height:48px;overflow:hidden;border-radius:50%;background:var(--ink);color:#fff;font-weight:500;letter-spacing:.02em;box-shadow:0 0 0 3px #fff,0 0 0 4px var(--line)}
.es-av img{width:100%;height:100%;object-fit:cover}
.es-av span{font-size:1.05rem;line-height:1}
.es-rev{display:inline-flex;align-items:center;gap:8px;font-size:.9rem;color:var(--ink2);text-decoration:none}
.es-rev b{color:var(--ink)}
.es-stars{color:#E8A317;letter-spacing:1px}
.es-who-card{margin-top:16px;padding:12px 16px;border-radius:16px;background:var(--go-bg)}
.es-photo{margin-top:12px}
.es-facts{display:flex;flex-wrap:wrap;gap:8px 20px;margin-top:16px;padding:0;list-style:none;font-size:.9rem;color:var(--ink2)}
.es-facts li{display:inline-flex;align-items:center;gap:8px}
.es-facts svg{flex:none;width:18px;height:18px;color:var(--muted)}
.es-scene{position:relative;margin:24px 0 0;padding:16px 16px 64px;overflow:hidden;border:1px solid var(--line);border-radius:20px;background:linear-gradient(180deg,#FFFFFF,#EDF0F4)}
.es-scene-art{display:block;max-width:250px;margin:0 auto}
.es-scene-art svg{width:100%;height:auto}
.es-photo{aspect-ratio:4/3;padding:0;background:#DCE1E8}
.es-photo img{display:block;width:100%;height:100%;object-fit:cover}
.es-photo-own{position:absolute;top:12px;left:12px;padding:4px 12px;border-radius:999px;background:rgba(10,20,36,.72);color:#fff;font-size:.8rem}
.es-photo .es-tag{display:flex;align-items:center;gap:12px;right:auto;max-width:calc(100% - 24px)}
.es-tag-ico{flex:none;display:grid;place-items:center;width:56px;height:48px;border-radius:8px;background:linear-gradient(180deg,#F8F9FB,#EDF0F4)}
.es-tag-ico svg{width:50px;height:auto}
.es-tag-t{display:grid;gap:2px}
.es-tag{position:absolute;left:12px;bottom:12px;display:grid;gap:2px;padding:12px 16px;border-radius:12px;background:#fff;box-shadow:0 0 0 1px var(--line),0 14px 30px -16px rgba(10,20,36,.5)}
.es-tag-k{font-size:.78rem;color:var(--muted)}
.es-tag b{font-size:1.25rem;font-weight:600;line-height:1.2;letter-spacing:-.02em;font-variant-numeric:tabular-nums}
.es-tag span:last-child{font-size:.82rem;color:var(--ink2)}
.es-faq{grid-column:1/-1;width:100%;max-width:760px;margin:16px auto 0}
.es-faq h2{font-size:1.6rem;font-weight:500;letter-spacing:-.02em}
.es-faq-list{margin-top:16px;padding:0 20px;border:1px solid var(--line);border-radius:20px;background:#fff}
.es-faq details+details{border-top:1px solid var(--line)}
.es-faq summary{display:flex;align-items:center;justify-content:space-between;gap:16px;min-height:60px;padding:12px 0;font-weight:500;cursor:pointer;list-style:none}
.es-faq summary::-webkit-details-marker{display:none}
.es-faq summary::after{content:"+";flex:none;font-size:1.3rem;font-weight:400;color:var(--muted)}
.es-faq details[open] summary::after{content:"−"}
.es-faq details p{padding-bottom:16px;color:var(--ink2)}
.es-card{position:relative;border:1px solid var(--line);border-radius:20px;background:#fff;box-shadow:0 1px 2px rgba(10,20,36,.04),0 30px 70px -44px rgba(10,20,36,.45);scroll-margin-top:0}
.es-head{position:sticky;top:0;z-index:4;display:flex;flex-wrap:wrap;align-items:baseline;justify-content:space-between;row-gap:8px;padding:16px 20px 12px;border-radius:20px 20px 0 0;background:rgba(255,255,255,.94);-webkit-backdrop-filter:blur(10px);backdrop-filter:blur(10px);font-size:.86rem;color:var(--muted);font-variant-numeric:tabular-nums}
.es-pct{font-weight:500;color:var(--ink2)}
.es-bar{flex-basis:100%;height:6px;overflow:hidden;border-radius:6px;background:#E6E9EE}
.es-bar i{display:block;width:0;height:100%;border-radius:inherit;background:var(--go-bar);transition:width .5s var(--ease)}
.es-body{padding:4px 20px 24px}
@media (max-width:959px){.es-card{display:flex;flex-direction:column;min-height:100vh;min-height:100svh}.es-body{flex:1}}
.es-step{display:none}
.es-step.is-on{display:block}
.es-fwd{animation:es-fwd .4s var(--ease)}
.es-bwd{animation:es-bwd .4s var(--ease)}
@keyframes es-fwd{from{opacity:0;transform:translateX(28px)}}
@keyframes es-bwd{from{opacity:0;transform:translateX(-28px)}}
.es-q{font-size:clamp(1.5rem,6.2vw,1.9rem);font-weight:500;line-height:1.16;letter-spacing:-.02em;text-wrap:balance;outline:none}
.es-sub{margin-top:8px;font-size:.98rem;color:var(--muted)}
.es-opts{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-top:20px}
.es-opt{position:relative;display:flex;flex-direction:column;overflow:hidden;padding:0;border:1.5px solid var(--line);border-radius:16px;background:#fff;text-align:left;transition:border-color .15s,box-shadow .15s,transform .15s}
.es-opt:active,.es-tile:active,.es-chip:active,.es-sb:active{transform:scale(.97)}
.es-ico{display:grid;place-items:center;aspect-ratio:4/3;background:linear-gradient(180deg,#F8F9FB,#EDF0F4);transition:background .2s}
.es-ico svg{width:88%;height:auto}
.es-ot{display:block;padding:12px}
.es-ot b{display:block;font-size:.98rem;font-weight:500;line-height:1.25}
.es-ot span{display:block;margin-top:4px;font-size:.84rem;line-height:1.35;color:var(--muted)}
.es-opt:last-child:nth-child(odd){grid-column:1/-1;flex-direction:row;align-items:center}
.es-opt:last-child:nth-child(odd) .es-ico{flex:0 0 46%;align-self:stretch;aspect-ratio:auto;padding:8px 0}
.es-opt:last-child:nth-child(odd) .es-ico svg{width:auto;max-width:92%;height:auto;max-height:132px}
.es-ck{position:absolute;top:8px;left:8px;z-index:1;display:grid;place-items:center;width:24px;height:24px;border:1.5px solid var(--line2);border-radius:50%;background:rgba(255,255,255,.9);color:#fff}
.es-ck svg{width:14px;height:14px;opacity:0}
.es-opt:hover,.es-tile:hover,.es-chip:hover,.es-sb:hover{border-color:var(--line2)}
.es-opt[aria-pressed="true"],.es-tile[aria-pressed="true"]{border-color:var(--go);box-shadow:0 0 0 3px var(--go-ring)}
.es-opt[aria-pressed="true"] .es-ico{background:linear-gradient(180deg,#F2FAF5,#E3F3E9)}
[aria-pressed="true"]>.es-ck{border-color:var(--go);background:var(--go);animation:es-pop .35s var(--ease)}
[aria-pressed="true"]>.es-ck svg{opacity:1}
@keyframes es-pop{50%{transform:scale(1.22)}}
.es-tiles{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px;margin-top:20px}
.es-tile{position:relative;display:flex;flex-direction:column;gap:8px;padding:8px 8px 12px;border:1.5px solid var(--line);border-radius:16px;background:#fff;font-size:.88rem;font-weight:500;line-height:1.25;text-align:center;transition:border-color .15s,box-shadow .15s,transform .15s}
.es-tile .es-ck{top:12px;left:12px}
.es-sw{display:block;aspect-ratio:4/3;overflow:hidden;border-radius:8px;box-shadow:inset 0 0 0 1px rgba(10,20,36,.06)}
.es-sw svg{width:100%;height:100%}
.es-field{margin-top:24px}
.es-lab{display:block;margin-bottom:12px;font-size:1rem;font-weight:500}
.es-seg{display:flex;flex-wrap:wrap;gap:8px}
.es-chip{flex:1 1 auto;min-height:52px;padding:0 16px;border:1.5px solid var(--line);border-radius:12px;background:#fff;font-size:.95rem;font-weight:500;text-align:center;transition:border-color .15s,box-shadow .15s,background .15s,transform .15s}
.es-chip[aria-pressed="true"]{border-color:var(--go);background:var(--go-bg);color:#0B4D24;box-shadow:0 0 0 3px var(--go-ring)}
.es-ctx{display:flex;align-items:center;gap:16px;margin-top:20px;padding:8px 16px 8px 8px;border:1px solid var(--line);border-radius:16px}
.es-ctx-ico{flex:none;display:grid;place-items:center;width:112px;height:84px;border-radius:8px;background:linear-gradient(180deg,#F8F9FB,#EDF0F4)}
.es-ctx-ico svg{width:100px;height:auto}
.es-ctx small{display:block;font-size:.82rem;color:var(--muted)}
.es-ctx b{display:block;font-weight:500;line-height:1.25}
.es-rangef{margin-top:20px;padding:20px 16px 12px;border-radius:16px;background:var(--soft)}
.es-rangef .es-lab{margin:0;text-align:center;font-weight:500;color:var(--ink2)}
.es-stepper{display:grid;grid-template-columns:52px minmax(0,1fr) 52px;align-items:center;gap:8px;margin-top:8px}
.es-stepper output{font-size:clamp(2.1rem,9vw,2.6rem);font-weight:500;line-height:1.1;letter-spacing:-.03em;text-align:center;white-space:nowrap;font-variant-numeric:tabular-nums}
.es-sb{display:grid;place-items:center;width:52px;height:52px;border:1.5px solid var(--line);border-radius:50%;background:#fff;transition:border-color .15s,transform .15s}
.es-sb svg{width:20px;height:20px}
.es-range{-webkit-appearance:none;appearance:none;width:100%;height:44px;margin:8px 0 0;background:transparent;cursor:pointer;--p:50%}
.es-range::-webkit-slider-runnable-track{height:8px;border-radius:8px;background:linear-gradient(to right,var(--go-bar) var(--p),#DCE0E6 var(--p))}
.es-range::-moz-range-track{height:8px;border-radius:8px;background:#DCE0E6}
.es-range::-moz-range-progress{height:8px;border-radius:8px;background:var(--go-bar)}
.es-range::-webkit-slider-thumb{-webkit-appearance:none;width:32px;height:32px;margin-top:-12px;border:4px solid var(--go);border-radius:50%;background:#fff;box-shadow:0 4px 12px -2px rgba(10,20,36,.35)}
.es-range::-moz-range-thumb{width:24px;height:24px;border:4px solid var(--go);border-radius:50%;background:#fff}
.es-mm{display:flex;justify-content:space-between;font-size:.8rem;color:var(--muted)}
.es-in{width:100%;height:56px;padding:0 16px;border:1.5px solid var(--line2);border-radius:12px;background:#fff;font:inherit;font-size:1.08rem;transition:border-color .15s,box-shadow .15s}
.es-in:focus{border-color:var(--go);outline:none;box-shadow:0 0 0 3px var(--go-ring)}
.es-in[aria-invalid="true"]{border-color:#B42318}
.es-cp-row{display:flex;flex-wrap:wrap;align-items:center;gap:8px 16px}
.es-in-cp{width:168px;font-size:1.25rem;font-weight:500;letter-spacing:.06em;font-variant-numeric:tabular-nums}
.es-cp-hint{font-size:.95rem;font-weight:500;color:var(--muted)}
.es-cp-hint.is-ok{color:var(--go)}
.es-cp-hint.is-ok::before{content:"✓ "}
.es-cp-hint.is-warn{color:#B45309}
.es-two{display:grid;gap:16px;margin-top:20px}
@media (min-width:640px){.es-two{grid-template-columns:1fr 1fr}}
.es-hp{position:absolute;left:-9999px;width:1px;height:1px;opacity:0}
.es-priv{display:flex;gap:8px;margin-top:12px;font-size:.84rem;line-height:1.45;color:var(--muted)}
.es-priv svg{flex:none;width:18px;height:18px;margin-top:0}
.es-note{margin-top:16px;padding:12px 16px;border-radius:12px;background:var(--soft);font-size:.92rem;line-height:1.45;color:var(--ink2)}
.es-zone{background:#FFF7E0}
.es-recap{display:flex;flex-wrap:wrap;gap:8px;margin-top:16px;padding:0;list-style:none}
.es-recap li{padding:4px 12px;border-radius:999px;background:var(--soft);font-size:.82rem;color:var(--ink2)}
.es-teaser{margin-top:16px;padding:16px 20px;border:1.5px dashed var(--line2);border-radius:16px;background:linear-gradient(180deg,#FBFCFD,#F3F5F8)}
.es-t-k{font-size:.8rem;color:var(--muted)}
.es-blur{margin-top:4px;font-size:1.7rem;font-weight:500;letter-spacing:-.02em;filter:blur(9px);-webkit-user-select:none;user-select:none}
.es-lock{display:flex;align-items:center;gap:8px;margin-top:8px;font-size:.86rem;font-weight:500;color:var(--ink2)}
.es-lock svg{width:18px;height:18px}
.es-err{margin-top:16px;font-size:.94rem;color:#B42318}
.es-nav{position:sticky;bottom:0;z-index:4;display:flex;gap:8px;padding:12px 16px calc(12px + env(safe-area-inset-bottom));border-top:1px solid var(--line);border-radius:0 0 20px 20px;background:rgba(255,255,255,.94);-webkit-backdrop-filter:blur(10px);backdrop-filter:blur(10px)}
.es-back{display:grid;place-items:center;flex:none;width:56px;height:56px;border:1.5px solid var(--line2);border-radius:12px;background:#fff;color:var(--ink2)}
.es-back svg{width:20px;height:20px}
.es-next{display:inline-flex;flex:1;align-items:center;justify-content:center;gap:8px;min-height:56px;padding:0 20px;border:0;border-radius:12px;background:var(--go);color:#fff;font-size:1.06rem;font-weight:500;box-shadow:inset 0 1px 0 rgba(255,255,255,.18);transition:background .2s,opacity .2s}
.es-next:hover{background:var(--go-h)}
.es-next.is-off{opacity:.42}
.es-next span{white-space:nowrap}
.es-next svg{width:20px;height:20px}
.es-res{padding-top:8px}
.es-rcpt-top{display:flex;justify-content:space-between;align-items:baseline;gap:12px;padding-bottom:12px;border-bottom:1.5px dashed var(--line2);font-size:.85rem;color:var(--muted)}
.es-rcpt-ent{font-weight:500;color:var(--ink)}
.es-rid{display:flex;align-items:center;gap:16px;margin-top:16px}
.es-rid-ico{flex:none;display:grid;place-items:center;width:76px;height:64px;border-radius:12px;background:linear-gradient(180deg,#F8F9FB,#EDF0F4)}
.es-rid-ico svg{width:68px;height:auto}
.es-res-k{font-size:.88rem;color:var(--muted)}
.es-rid-t{font-weight:500;line-height:1.25}
.es-amount{margin-top:16px!important}
.es-amount{margin-top:2px;font-size:clamp(2.2rem,9.4vw,3.2rem);font-weight:600;line-height:1.05;letter-spacing:-.04em;font-variant-numeric:tabular-nums}
.es-amount-f{margin-top:8px;font-size:.94rem;color:var(--ink2)}
.es-lines{margin-top:16px;padding:0;list-style:none;border-top:1.5px dashed var(--line2)}
.es-lines li{display:grid;grid-template-columns:minmax(0,1fr) auto;gap:2px 12px;padding:12px 0;border-bottom:1.5px dashed var(--line2);font-size:.95rem}
.es-val{font-weight:500;text-align:right;white-space:nowrap;font-variant-numeric:tabular-nums}
.es-calc{grid-column:1/-1;font-size:.85rem;color:var(--muted)}
.es-calc a{color:var(--muted)}
.es-h3{margin-top:24px;font-size:1rem;font-weight:500}
.es-list{margin-top:8px;padding-left:20px;font-size:.95rem;color:var(--ink2)}
.es-p{margin-top:8px;font-size:.95rem;color:var(--ink2)}
.es-box{margin-top:24px;padding:20px;border-radius:16px;background:var(--ink);color:#fff}
.es-box-k{font-size:.86rem;color:#A9B4C6}
.es-box-h{margin-top:4px;font-size:1.3rem;font-weight:500;line-height:1.2;letter-spacing:-.01em}
.es-box-p{margin-top:8px;font-size:.95rem;color:#D5DBE5}
.es-acts{display:flex;flex-wrap:wrap;gap:8px;margin-top:16px}
.es-btn{display:inline-flex;flex:1 1 auto;align-items:center;justify-content:center;gap:8px;min-height:56px;padding:0 20px;border-radius:12px;font-weight:500;text-decoration:none}
.es-btn svg{width:20px;height:20px}
.es-btn-wa{background:#25D366;color:#0A1424}
.es-btn-call{background:#fff;color:var(--ink)}
.es-box[data-state="sending"] .es-s-sent,.es-box[data-state="sending"] .es-s-manual,.es-box[data-state="sent"] .es-s-sending,.es-box[data-state="sent"] .es-s-manual,.es-box[data-state="manual"] .es-s-sending,.es-box[data-state="manual"] .es-s-sent{display:none}
.es-after{display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;gap:8px 16px;margin-top:16px}
.es-share{display:inline-flex;align-items:center;gap:8px;min-height:48px;padding:0 16px;border:1.5px solid var(--line2);border-radius:12px;background:#fff;font-weight:500;transition:border-color .15s,transform .15s}
.es-share:hover{border-color:var(--ink2)}
.es-share svg{width:18px;height:18px}
.es-ico svg{transition:transform .3s var(--ease)}
@media (hover:hover){.es-opt:hover .es-ico svg{transform:translateY(-3px)}}
.es-again{min-height:44px;margin-top:0;padding:0;border:0;background:none;color:var(--muted);text-decoration:underline;text-underline-offset:3px}
@media (min-width:640px){.es-head{padding:20px 28px 16px}.es-body{padding:8px 28px 28px}.es-nav{padding:16px 28px}.es-opts{gap:12px}}
@media (min-width:960px){.es-main{grid-template-columns:minmax(0,1fr) 540px;align-items:start;gap:72px;padding:36px 32px 96px}.es-intro{padding-top:36px}.es-scene-art{max-width:270px}.es-photo{aspect-ratio:3/2}.es-cta{display:none}.es-lead{font-size:1.12rem}}
.es-ftr{padding:28px 16px 40px;border-top:1px solid var(--line);font-size:.86rem;color:var(--muted);text-align:center}
.es-by{display:flex;flex-wrap:wrap;align-items:center;justify-content:center;gap:8px}
.es-by img{height:28px;width:auto;max-width:150px;object-fit:contain}
.es-by b{color:var(--ink);font-weight:500}
.es-ftr>p+p{margin-top:8px}
.es-legal{max-width:640px;margin:16px auto 0;text-align:left}
.es-legal details{border-top:1px solid var(--line)}
.es-legal details:last-child{border-bottom:1px solid var(--line)}
.es-legal summary{display:flex;align-items:center;justify-content:space-between;min-height:48px;cursor:pointer;color:var(--ink2);font-weight:500;list-style:none}
.es-legal summary::-webkit-details-marker{display:none}
.es-legal summary::after{content:"+";font-size:1.2rem;color:var(--muted)}
.es-legal details[open] summary::after{content:"−"}
.es-legal details p{padding-bottom:12px;line-height:1.5}
.es-legal a,.es-cc-open{color:var(--ink2);text-decoration:underline;text-underline-offset:2px}
.es-cc-open{padding:0;border:0;background:none;font-size:inherit}
.es-cc{position:fixed;left:12px;right:12px;bottom:12px;z-index:10;display:grid;gap:12px;max-width:560px;margin:0 auto;padding:16px;border-radius:16px;background:var(--ink);color:#fff;font-size:.9rem;line-height:1.45;box-shadow:0 20px 50px -20px rgba(10,20,36,.6)}
.es-cc div{display:grid;grid-template-columns:1fr 1fr;gap:8px}
.es-cc button{min-height:46px;border:1.5px solid #fff;border-radius:12px;background:transparent;color:#fff;font-weight:500}
@media (prefers-reduced-motion:reduce){*{animation:none!important;transition:none!important}}
"""

JS = r"""(function(){
var C=__CFG__,ICO=__ICO__,d=document,RM=!!(window.matchMedia&&matchMedia("(prefers-reduced-motion: reduce)").matches);
var f=d.getElementById("es-form");if(!f)return;
var steps=[].slice.call(f.querySelectorAll(".es-step")),N=steps.length,cur=0,A={},done=false,started=false;
var bar=f.querySelector(".es-bar i"),pct=f.querySelector(".es-pct"),num=f.querySelector(".es-num-step"),back=f.querySelector(".es-back"),next=f.querySelector(".es-next"),nextL=next.querySelector("span"),nav=f.querySelector(".es-nav"),head=f.querySelector(".es-head"),err=f.querySelector(".es-err"),res=f.querySelector(".es-res");
var qs=new URLSearchParams(location.search),track={};["utm_source","utm_medium","utm_campaign","utm_content","utm_term","fbclid","gclid"].forEach(function(k){if(qs.get(k))track[k]=qs.get(k).slice(0,200)});
function each(l,fn){[].forEach.call(l,fn)}
function dl(ev,p){var o={event:ev,metier:C.key};for(var k in p)o[k]=p[k];(window.dataLayer=window.dataLayer||[]).push(o)}
function begin(){if(!started){started=true;dl("estimation_debut",{})}}
var SK="es-"+C.key;
function save(x){try{var o={A:A,cur:cur,t:Date.now()};for(var k in x)o[k]=x[k];sessionStorage.setItem(SK,JSON.stringify(o))}catch(e){}}
function load(){try{var o=JSON.parse(sessionStorage.getItem(SK));return o&&o.A&&Date.now()-o.t<72e5?o:null}catch(e){return null}}
function esc(s){return String(s).replace(/[&<>"]/g,function(c){return{"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]})}
function nb(n){return Math.round(n).toLocaleString("fr-FR").replace(/\s/g,"\u202f")}
function eur(n){return nb(n)+"\u00a0€"}
function lab(v,u){if(Array.isArray(u)){if(v===0&&u[0])return u[0];return v+"\u00a0"+(v>1?u[2]:u[1])}return v+"\u00a0"+u}
function val(k){var x=f.querySelector("[name="+k+"]");return x?(x.value||"").trim():""}
function toCard(){var y=Math.round(f.getBoundingClientRect().top+scrollY);if(Math.abs(scrollY-y)>4&&(innerWidth<960||scrollY>y))scrollTo({top:y,behavior:RM?"auto":"smooth"})}
/* curseurs et boutons − / + */
each(f.querySelectorAll(".es-range"),function(r){var box=r.closest(".es-field"),o=box.querySelector("output"),u=JSON.parse(r.getAttribute("data-units"));
  function up(){var v=+r.value;A[r.getAttribute("data-q")]=v;o.textContent=lab(v,u);r.style.setProperty("--p",(100*(v-r.min)/(r.max-r.min))+"%")}
  r.addEventListener("input",function(){up();begin()});
  each(box.querySelectorAll("[data-step]"),function(b){b.addEventListener("click",function(){r.value=Math.min(+r.max,Math.max(+r.min,+r.value+(+r.step)*(+b.getAttribute("data-step"))));up();begin()})});
  up()});
function missing(i){var bad=[];each(steps[i].querySelectorAll("[data-req]"),function(x){if(x.hidden)return;var v=A[x.getAttribute("data-req")];if(v===undefined||v===""||(Array.isArray(v)&&!v.length))bad.push(x.getAttribute("data-miss"))});return bad}
function refresh(){each(f.querySelectorAll("[data-show]"),function(x){var s=JSON.parse(x.getAttribute("data-show"));x.hidden=s[1].indexOf(A[s[0]])<0});
  var t=f.querySelector(".es-tenant");if(t)t.hidden=A.statut!=="Locataire";
  next.classList.toggle("is-off",missing(cur).length>0)}
/* choix */
f.addEventListener("click",function(ev){var b=ev.target.closest("button[data-q]");if(!b||!f.contains(b))return;
  var k=b.getAttribute("data-q"),g=f.querySelectorAll('button[data-q="'+k+'"]'),multi=b.hasAttribute("data-multi");
  if(multi){var on=b.getAttribute("aria-pressed")!=="true",ex=b.hasAttribute("data-excl");
    each(g,function(x){if(x===b)x.setAttribute("aria-pressed",on?"true":"false");else if(on&&(ex||x.hasAttribute("data-excl")))x.setAttribute("aria-pressed","false")});
    var sel=[].filter.call(g,function(x){return x.getAttribute("aria-pressed")==="true"}).map(function(x){return x.getAttribute("data-v")});if(sel.length)A[k]=sel;else delete A[k]}
  else{each(g,function(x){x.setAttribute("aria-pressed",x===b?"true":"false")});A[k]=b.getAttribute("data-v")}
  begin();err.hidden=true;refresh();save();
  if(navigator.vibrate)try{navigator.vibrate(8)}catch(x){}
  var st=steps[cur];if(st&&st.hasAttribute("data-auto")&&!multi)setTimeout(function(){if(steps[cur]===st)go(1)},320)});
/* calcul */
function rows(){var o=C.opts[A.travaux];if(!o)return[];var ac=A.acces,out=[],g={};
  o.lines.forEach(function(l){if(l["if"]&&ac&&ac!=="Je ne sais pas"&&ac!==l["if"][1])return;
    var c={l:l.l,lo:l.lo,hi:l.hi,u:l.u,src:l.src,approx:l.approx};
    if(l.g){if(g[l.g]){g[l.g].lo=Math.min(g[l.g].lo,l.lo);g[l.g].hi=Math.max(g[l.g].hi,l.hi);g[l.g].l=o.gl;return}g[l.g]=c}out.push(c)});
  return out}
function qn(){return +A[C.qty.name]||0}
function ql(){var n=qn();return n+"\u00a0"+(n>1?C.qty.many:C.qty.one)}
function rnd(x,up){var s=x<1000?10:100;return(up?Math.ceil(x/s):Math.floor(x/s))*s}
function estimate(){var R=rows(),n=qn(),lo=0,hi=0;R.forEach(function(r){r.tlo=r.lo*n;r.thi=r.hi*n;lo+=r.tlo;hi+=r.thi});
  var fx=lo===hi;return{rows:R,fixed:fx,lo:fx?Math.round(lo/100)*100:rnd(lo,false),hi:fx?Math.round(hi/100)*100:rnd(hi,true)}}
function amount(E,a,b){a=a===undefined?E.lo:a;b=b===undefined?E.hi:b;return E.fixed?"environ "+eur(a):eur(a)+" à "+eur(b)}
function rowAmount(r){return r.lo===r.hi?"environ "+eur(Math.round(r.tlo/100)*100):eur(rnd(r.tlo,false))+" à "+eur(rnd(r.thi,true))}
function rowUnit(r){return(r.lo===r.hi?(r.approx?"environ ":"")+nb(r.lo):nb(r.lo)+" à "+nb(r.hi))+"\u00a0"+r.u}
function dep(cp){var x=cp.slice(0,2)==="97"?cp.slice(0,3):cp.slice(0,2);if(x==="20")x=+cp<20200?"2A":"2B";return x}
function outZone(){return!!(C.deps.length&&A.code_postal&&C.deps.indexOf(dep(A.code_postal))<0&&C.deps.indexOf(A.code_postal.slice(0,2))<0)}
function place(){return A.code_postal?A.code_postal+(A.commune?" "+A.commune.split(",")[0]:""):""}
/* code postal : nom de la commune, zone d'intervention */
var cpIn=f.querySelector("#es-cp"),cpHint=f.querySelector(".es-cp-hint"),zoneN=f.querySelector(".es-zone");
if(cpIn)cpIn.addEventListener("input",function(){var v=cpIn.value.replace(/\D/g,"").slice(0,5);if(cpIn.value!==v)cpIn.value=v;A.commune="";cpHint.textContent="";cpHint.className="es-cp-hint";
  if(v.length<5){if(zoneN)zoneN.hidden=true;return}
  A.code_postal=v;if(zoneN)zoneN.hidden=!outZone();
  if(window.fetch)fetch(C.geo+"/communes?codePostal="+v+"&fields=nom&format=json").then(function(r){return r.ok?r.json():null}).then(function(l){if(!l||cpIn.value!==v)return;
    if(l.length){var n=l.map(function(x){return x.nom});A.commune=n.slice(0,3).join(", ");cpHint.textContent=n.slice(0,2).join(", ")+(n.length>2?"…":"");cpHint.className="es-cp-hint is-ok"}
    else{cpHint.textContent="Code postal introuvable, vérifiez-le";cpHint.className="es-cp-hint is-warn"}}).catch(function(){})});
/* téléphone : 06 12 34 56 78 */
var telIn=f.querySelector("#es-tel");if(telIn)telIn.addEventListener("input",function(){var g=telIn.value.replace(/\D/g,"");if(/^0/.test(g)&&g.length<=10){var fm=g.replace(/(\d{2})(?=\d)/g,"$1 ");if(fm!==telIn.value)telIn.value=fm}});
function prep(){var st=steps[N-1],h=st.querySelector("[data-h]"),s=st.querySelector("[data-s]"),t=st.querySelector(".es-teaser"),rc=st.querySelector(".es-recap");
  var items=[A.travaux,ql()];C.recap.forEach(function(k){var v=A[k];if(v&&v!=="Je ne sais pas")items.push(v)});if(place())items.push(place());
  rc.innerHTML=items.filter(Boolean).map(function(x){return"<li>"+esc(x)+"</li>"}).join("");
  if(rows().length){h.textContent="Votre estimation est prête";s.textContent="Indiquez votre prénom et votre numéro\u00a0: elle s’affiche aussitôt.";t.hidden=false;t.querySelector(".es-blur").textContent=amount(estimate())}
  else{h.textContent="Votre demande est prête";s.textContent="Ce type de travaux se chiffre sur place. Indiquez votre prénom et votre numéro pour fixer une visite.";t.hidden=true}}
/* étapes */
function show(i,dir,push){cur=i;each(steps,function(s,j){s.classList.toggle("is-on",j===i);s.classList.remove("es-fwd","es-bwd")});
  var st=steps[i];if(dir&&!RM){void st.offsetWidth;st.classList.add(dir>0?"es-fwd":"es-bwd")}
  var p=Math.round(100*(i+1)/(N+1));bar.style.width=p+"%";pct.textContent=p+"\u00a0%";var rem=N-i;num.textContent=rem===1?"Dernière étape":rem===2?"Avant-dernière étape":rem===3?"Plus que 3 étapes":"Étape "+(i+1)+" sur "+N;
  back.hidden=i===0;nav.hidden=i===0&&st.hasAttribute("data-auto");err.hidden=true;
  if(i===N-1)prep();refresh();
  var cx=st.querySelector(".es-ctx"),sel=f.querySelector('.es-opt[aria-pressed="true"]');if(cx&&sel){cx.querySelector(".es-ctx-ico").innerHTML=sel.querySelector(".es-ico").innerHTML;cx.querySelector(".es-ctx-t").textContent=A.travaux;cx.hidden=false}
  nextL.textContent=i===N-1?(rows().length?"Voir mon estimation":"Envoyer ma demande"):"Suivant";
  if(push)try{history.pushState({es:i},"")}catch(x){}
  if(!done)save();
  if(dir){toCard();var h=st.querySelector(".es-q");if(h)try{h.focus({preventScroll:true})}catch(x){}}}
try{history.replaceState({es:0},"")}catch(x){}
addEventListener("popstate",function(ev){if(done)return;var s=ev.state&&typeof ev.state.es==="number"?ev.state.es:0;if(s!==cur)show(s,s<cur?-1:1,false)});
back.addEventListener("click",function(){if(history.state&&typeof history.state.es==="number"&&history.state.es>0)history.back();else if(cur>0)show(cur-1,-1,false)});
each(d.querySelectorAll("[data-start]"),function(b){b.addEventListener("click",function(ev){ev.preventDefault();begin();toCard()})});
function check(i){var st=steps[i],bad=missing(i);
  var cp=st.querySelector("[name=code_postal]");if(cp){var ok=/^\d{5}$/.test(cp.value.trim());if(ok){A.code_postal=cp.value.trim();cp.removeAttribute("aria-invalid")}else{cp.setAttribute("aria-invalid","true");bad.push("un code postal à 5 chiffres")}}
  var pr=st.querySelector("[name=prenom]");if(pr){var tel=st.querySelector("[name=telephone]");
    if(pr.value.trim().length<2){pr.setAttribute("aria-invalid","true");bad.push("votre prénom")}else pr.removeAttribute("aria-invalid");
    var tg=tel.value.replace(/\D/g,"");if(!/^0[1-9]\d{8}$/.test(tg)&&!/^(33|0033)[1-9]\d{8}$/.test(tg)){tel.setAttribute("aria-invalid","true");bad.push("un numéro de téléphone valide (10 chiffres)")}else tel.removeAttribute("aria-invalid");
}
  return bad}
function go(dir){if(dir<=0)return;var bad=check(cur);
  if(bad.length){err.textContent="Il manque "+bad.join(", ")+".";err.hidden=false;var x=steps[cur].querySelector('[aria-invalid="true"]');if(x)x.focus();return}
  if(cur===N-1){submit();return}
  dl("estimation_etape",{etape:cur+1});show(cur+1,1,true)}
next.addEventListener("click",function(){go(1)});
f.addEventListener("submit",function(ev){ev.preventDefault();go(1)});
f.addEventListener("input",function(){if(err.hidden)return;var bad=check(cur);if(bad.length)err.textContent="Il manque "+bad.join(", ")+".";else err.hidden=true});
/* résultat */
function render(E,pr,telf,state){var sel=f.querySelector('.es-opt[aria-pressed="true"] .es-ico'),pic=sel?sel.innerHTML:"",o=C.opts[A.travaux]||{},date=new Date().toLocaleDateString("fr-FR",{day:"numeric",month:"long",year:"numeric"});
  var h='<div class="es-rcpt-top"><span class="es-rcpt-ent">'+esc(C.ent)+'</span><span>'+esc(date)+'</span></div>'
   +'<div class="es-rid">'+(pic?'<span class="es-rid-ico">'+pic+'</span>':'')+'<div><p class="es-res-k">Estimation pour '+esc(pr)+(place()?" · "+esc(place()):"")+'</p><p class="es-rid-t">'+esc(A.travaux)+'</p></div></div>';
  if(E.rows.length){h+='<p class="es-amount" data-count>'+amount(E)+'</p><p class="es-amount-f">Pose comprise, pour '+ql()+'. Fourchette indicative, sans valeur contractuelle.</p><ul class="es-lines">';
    E.rows.forEach(function(r){h+='<li><span>'+esc(r.l)+'</span><span class="es-val">'+rowAmount(r)+'</span><span class="es-calc">'+ql()+" × "+rowUnit(r)+" · "+(r.src?'Source\u00a0: <a href="'+esc(r.src[1])+'" target="_blank" rel="noopener">'+esc(r.src[0])+"</a>":"Tarif de "+esc(C.ent))+'</span></li>'});h+="</ul>"}
  else h+='<p class="es-amount">À chiffrer sur place</p><p class="es-amount-f">'+esc(o.vt||"Ce type de travaux se chiffre après une visite.")+'</p>';
  C.notes.forEach(function(n){if(A[n.q]===n.eq)h+='<p class="es-note">'+esc(n.txt)+"</p>"});
  var vis=[];C.visite.forEach(function(r){var v=A[r.q];if((r.gt!==undefined&&v>r.gt)||(r.eq!==undefined&&v===r.eq))vis.push(r.txt.replace("{v}",v).replace("(s)",v>1?"s":""))});
  if(vis.length){h+='<p class="es-h3">À chiffrer à la visite</p><ul class="es-list">';vis.forEach(function(v){h+="<li>"+esc(v)+"</li>"});h+="</ul>"}
  h+='<p class="es-h3">Ce qui fait varier le prix</p><p class="es-p">'+esc(C.varie)+'</p>';
  if(C.aides)h+='<p class="es-note">'+esc(C.aides)+'</p>';
  if(A.statut==="Locataire")h+='<p class="es-note">Les travaux sur le bâti se décident avec le propriétaire\u00a0: transmettez-lui cette estimation.</p>';
  if(outZone())h+='<p class="es-note es-zone">Votre chantier semble hors de la zone habituelle de '+esc(C.ent)+(C.zone?" ("+esc(C.zone)+")":"")+'. Nous vous dirons rapidement si nous pouvons intervenir.</p>';
  var call=C.tel?'<a class="es-btn es-btn-call" href="tel:'+C.telh+'">'+ICO.phone+"Appeler le "+esc(C.tel)+"</a>":"";
  h+='<div class="es-box" data-state="'+state+'"><p class="es-box-k">Prochaine étape</p>'
   +'<div class="es-s-sending"><p class="es-box-h">Envoi de votre demande…</p></div>'
   +'<div class="es-s-sent"><p class="es-box-h">C’est noté, '+esc(pr)+'.</p><p class="es-box-p">'+esc(C.who)+" vous rappelle au "+esc(telf)+(C.horaires?", "+esc(C.horaires):"")+' pour fixer une visite et vous remettre un devis.</p>'
     +(C.wa?'<p class="es-box-p es-photo">En attendant, envoyez quelques photos du chantier\u00a0: la visite sera mieux préparée.</p>':"")
     +'<div class="es-acts">'+(C.wa?'<a class="es-btn es-btn-wa" target="_blank" rel="noopener" data-wa-photo>'+ICO.wa+"Envoyer des photos</a>":"")+call+"</div></div>"
   +'<div class="es-s-manual">'+(C.wa?'<p class="es-box-h">Envoyez votre demande à '+esc(C.ent)+'</p><p class="es-box-p">Votre message est déjà rédigé. Ajoutez-y quelques photos du chantier si vous pouvez\u00a0: la visite sera mieux préparée.</p><div class="es-acts"><a class="es-btn es-btn-wa" target="_blank" rel="noopener" data-wa>'+ICO.wa+"Envoyer sur WhatsApp</a>"+call+"</div>"
     :'<p class="es-box-h">Appelez '+esc(C.ent)+' pour fixer la visite</p><div class="es-acts">'+call+"</div>")+"</div></div>"
   +'<div class="es-after"><button type="button" class="es-share">'+ICO.share+'<span>Partager l’estimation</span></button><button type="button" class="es-again">Refaire une estimation</button></div>';
  return h}
function countUp(el,E){if(RM||!el||!window.requestAnimationFrame)return;var t0=0,D=1100;
  function step(t){if(!t0)t0=t;var k=Math.min(1,(t-t0)/D),q=1-Math.pow(1-k,3);el.textContent=k<1?amount(E,Math.round(E.lo*q/10)*10,Math.round(E.hi*q/10)*10):amount(E);if(k<1)requestAnimationFrame(step)}
  requestAnimationFrame(step)}
function finish(pr,tel,state,anim){var E=estimate(),dg=tel.replace(/\D/g,""),telf=dg.length===10?dg.replace(/(\d{2})(?=\d)/g,"$1\u00a0"):tel;
  var est=E.rows.length?amount(E):"à chiffrer sur place";
  var det=C.details.map(function(k){var v=A[k[0]];if(v===undefined||v===0)return null;return k[1]+"\u00a0: "+(Array.isArray(v)?v.join(", "):v)}).filter(Boolean);
  var msg="Bonjour, j’ai fait l’estimation "+C.nom+" sur votre site. Travaux\u00a0: "+A.travaux+", "+ql()+". Estimation\u00a0: "+est+". "+det.join(". ")+". "+A.delai+", "+(A.statut||"").toLowerCase()+", code postal "+place()+". "+pr+", "+telf+".";
  res.innerHTML=render(E,pr,telf,state);res.hidden=false;each(steps,function(s){s.classList.remove("is-on")});
  head.hidden=true;nav.hidden=true;err.hidden=true;done=true;
  try{history.replaceState({es:"fin"},"")}catch(x){}
  toCard();if(anim)countUp(res.querySelector("[data-count]"),E);
  var wa=res.querySelector("[data-wa]");if(wa)wa.href="https://wa.me/"+C.wa+"?text="+encodeURIComponent(msg);
  var wp=res.querySelector("[data-wa-photo]");if(wp)wp.href="https://wa.me/"+C.wa+"?text="+encodeURIComponent("Bonjour, voici des photos pour mon estimation "+C.nom+" ("+A.travaux+", code postal "+place()+"). "+pr+", "+telf+".");
  res.querySelector(".es-again").addEventListener("click",function(){try{sessionStorage.removeItem(SK)}catch(x){}location.href=location.pathname+location.search});
  var sh=res.querySelector(".es-share"),url=location.origin+location.pathname,txt="Estimation "+C.nom+" ("+C.ent+")\u00a0: "+A.travaux+", "+ql()+". "+(E.rows.length?est+", pose comprise, fourchette indicative.":"À chiffrer sur place.");
  sh.addEventListener("click",function(){if(navigator.share){navigator.share({title:"Estimation "+C.nom,text:txt,url:url}).catch(function(){})}
    else if(navigator.clipboard){navigator.clipboard.writeText(txt+" "+url).then(function(){sh.querySelector("span").textContent="Copié, vous pouvez le coller"})}});
  return{E:E,est:est,det:det,msg:msg,box:res.querySelector(".es-box")}}
function submit(){if(val("site_web"))return;var pr=val("prenom"),tel=val("telephone"),st0=C.envoi?"sending":"manual",R=finish(pr,tel,st0,true),est=R.est,det=R.det,msg=R.msg,box=R.box;
  save({done:1,pr:pr,tel:tel,st:C.envoi?"manual":st0});
  dl("estimation_demande",{travaux:A.travaux,delai:A.delai,statut:A.statut,estimation:est});
  if(window.fbq)window.fbq("track","Lead");
  if(!C.envoi)return;
  var body={type:"estimation",_subject:"Demande d’estimation "+C.nom+" · "+place(),message:msg,metier:C.key,entreprise:C.ent,fields:{travaux:A.travaux,quantite:ql(),estimation:est,details:det,delai:A.delai,statut:A.statut,code_postal:A.code_postal,commune:A.commune||"",prenom:pr,telephone:tel},
    consent:{text:f.querySelector(".es-consent").textContent,at:new Date().toISOString()},page:location.pathname,tracking:track,site_web:""};
  var fin=false,end=function(ok){if(fin)return;fin=true;box.setAttribute("data-state",ok?"sent":"manual");save({done:1,pr:pr,tel:tel,st:ok?"sent":"manual"});dl("estimation_envoi",{envoi:ok?"auto":"manuel"})},t=setTimeout(function(){end(false)},8000);
  try{fetch(C.envoi,{method:"POST",headers:{"Content-Type":"application/json","Accept":"application/json"},body:JSON.stringify(body)}).then(function(r){clearTimeout(t);end(r.ok)}).catch(function(){clearTimeout(t);end(false)})}catch(x){clearTimeout(t);end(false)}}
function restore(S){started=true;for(var k in S){var v=S[k];A[k]=v;
    (Array.isArray(v)?v:[v]).forEach(function(x){var b=f.querySelector('button[data-q="'+k+'"][data-v="'+String(x).replace(/["\\]/g,"\\$&")+'"]');if(b)b.setAttribute("aria-pressed","true")});
    var r=f.querySelector('.es-range[data-q="'+k+'"]');if(r){r.value=v;r.dispatchEvent(new Event("input"))}}
  if(cpIn&&A.code_postal)cpIn.value=A.code_postal}
var S0=load(),pj=(qs.get("projet")||"").replace(/[^a-z0-9-]/g,""),ob=pj&&f.querySelector('.es-opt[data-slug="'+pj+'"]');
if(S0&&(S0.done||!ob)){restore(S0.A);if(S0.done){var pi=f.querySelector("#es-prenom"),ti=f.querySelector("#es-tel");if(pi)pi.value=S0.pr;if(ti)ti.value=S0.tel;finish(S0.pr,S0.tel,S0.st||"manual",false)}
  else{show(S0.cur||0,0,false);try{history.replaceState({es:S0.cur||0},"")}catch(x){}}}
else if(ob){each(f.querySelectorAll(".es-opt"),function(x){x.setAttribute("aria-pressed",x===ob?"true":"false")});A.travaux=ob.getAttribute("data-v");started=true;dl("estimation_debut",{projet:pj});show(1,0,false);try{history.pushState({es:1},"")}catch(x){}}
else show(0,0,false);
})();"""

PIXEL_JS = r"""(function(){var C=__PX__,K="es-consent",d=document,bar=d.getElementById("es-cc");if(!bar)return;
function load(){if(window.fbq)return;!function(f,b,e,v,n,t,s){if(f.fbq)return;n=f.fbq=function(){n.callMethod?n.callMethod.apply(n,arguments):n.queue.push(arguments)};if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version="2.0";n.queue=[];t=b.createElement(e);t.async=!0;t.src=v;s=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s)}(window,d,"script","https://connect.facebook.net/en_US/fbevents.js");window.fbq("init",C);window.fbq("track","PageView")}
var v=null;try{v=JSON.parse(localStorage.getItem(K))}catch(x){}
if(v&&Date.now()-v.t<1.5e10){if(v.ok)load()}else bar.hidden=false;
[].forEach.call(bar.querySelectorAll("button"),function(b){b.addEventListener("click",function(){var ok=b.getAttribute("data-cc")==="1";try{localStorage.setItem(K,JSON.stringify({ok:ok,t:Date.now()}))}catch(x){}bar.hidden=true;if(ok)load();else if(window.fbq)location.reload()})});
[].forEach.call(d.querySelectorAll(".es-cc-open"),function(b){b.addEventListener("click",function(){bar.hidden=false})})})();"""


def page(key, cfg, logo_url, photo_url="", photo_urls=None):
    m = M[key]
    accent = cfg.get("accent", "#2D5BE3")
    ent = cfg["entreprise"]
    tel = cfg.get("telephone", "")
    telh = "+33" + re.sub(r"\D", "", tel)[1:] if tel else ""
    steps, n = steps_html(m, cfg, accent, photo_url)
    logo = f'<img src="{logo_url}" alt="{a(ent)}" width="180" height="36">' if logo_url else f'<span class="es-name">{e(ent)}</span>'
    call = (f'<a class="es-call" href="tel:{telh}">{ico("phone")}<span class="es-num">{e(tel)}</span><span class="es-short">Appeler</span></a>' if tel else "")
    own = bool(cfg.get("tarifs", {}).get(key))
    facts = [f"Calculé avec les tarifs de {ent}" if own else f"Calculé avec les prix publiés par {m['sources']}"] + list(cfg.get("atouts", []))
    facts_html = "".join(f"<li>{ico('check')}{e(x)}</li>" for x in facts)
    kick = f'<p class="es-kick">{ico("pin")}{e(m["artisan"].capitalize())} · {e(cfg["zone"])}</p>' if cfg.get("zone") else ""
    lead = "Répondez à 6 questions : le prix de vos travaux s’affiche tout de suite."
    ex_focus, ex_amount, ex_label = example(m, cfg, key)
    ph = photo_of(m, cfg, key)
    if ph["own"]:
        img = f'<img src="{photo_urls[key][0][0]}" alt="{a(ph["alt"])}" width="1200" height="900" decoding="async">'
    else:
        srcset = ", ".join(f"{u} {w}w" for u, w, _ in photo_urls[key])
        u0, w0, h0 = photo_urls[key][-1]
        img = (f'<img src="{photo_urls[key][0][0]}" srcset="{srcset}" sizes="(min-width: 960px) 520px, calc(100vw - 32px)" '
               f'alt="{a(ph["alt"])}" width="{w0}" height="{h0}" decoding="async" style="object-position:{ph["pos"]}">')
    cap = f'<span class="es-photo-own">Un chantier de {e(cfg["entreprise"])}</span>' if ph["own"] else ""
    scene = (f'<figure class="es-scene es-photo">{img}{cap}'
             f'<figcaption class="es-tag"><span class="es-tag-ico" aria-hidden="true">{icons.house(ex_focus, None, accent, s=8)}</span>'
             f'<span class="es-tag-t"><span class="es-tag-k">Exemple d’estimation</span><b>{e(ex_amount)}</b><span>{e(ex_label)}</span></span></figcaption></figure>')
    av, title, person = who(cfg, photo_url)
    trust = (f'<div class="es-trust"><div class="es-who"><span class="es-av">{av}</span><p><b>{e(title)}</b>'
             f'<span>{e(cfg.get("rappel") or ("Vous rappelle personnellement" if person else "Rappel gratuit, sans engagement"))}</span></p></div>{stars(cfg)}</div>')
    by = f'<img src="{logo_url}" alt="{a(ent)}" width="150" height="28">' if logo_url else f"<b>{e(ent)}</b>"
    cc = ('<div class="es-cc" id="es-cc" role="dialog" aria-label="Cookies" hidden><p>Acceptez-vous un cookie de Meta qui mesure l’efficacité de nos annonces ? '
          'Sans accord, rien n’est déposé.</p><div><button type="button" data-cc="0">Refuser</button><button type="button" data-cc="1">Accepter</button></div></div>') if cfg.get("meta_pixel") else ""
    cfg_json = json.dumps(cfg_js(key, m, cfg), ensure_ascii=False, separators=(",", ":"))
    ico_json = json.dumps({"phone": ico("phone"), "wa": ico("wa"), "share": ico("share")}, ensure_ascii=False)
    js = JS.replace("__CFG__", cfg_json).replace("__ICO__", ico_json)
    scripts = [js] + ([PIXEL_JS.replace("__PX__", json.dumps(cfg["meta_pixel"]))] if cfg.get("meta_pixel") else [])
    hashes = " ".join("'sha256-" + base64.b64encode(hashlib.sha256(s.encode()).digest()).decode() + "'" for s in scripts)
    env_origin = ""
    if cfg.get("envoi"):
        u = urlparse(cfg["envoi"])
        env_origin = f" {u.scheme}://{u.netloc}" if u.netloc else ""
    fb = " https://connect.facebook.net" if cfg.get("meta_pixel") else ""
    csp = (f"default-src 'self'; script-src 'self' {hashes}{fb}; style-src 'self' 'unsafe-inline'; img-src 'self' data:{' https://www.facebook.com' if fb else ''}; "
           f"font-src 'self'; connect-src 'self' {GEO}{env_origin}{' https://www.facebook.com' + fb if fb else ''}; form-action 'none'; base-uri 'self'; object-src 'none'")
    title = f"{m['title']} | {ent}"
    h1 = re.sub(r"<mark>(.*?)</mark>", lambda x: "<mark>" + x.group(1).replace(" ", "\u00a0") + "</mark>", fr(m["h1"]))
    dom = cfg.get("domaine", "").rstrip("/")
    og_tags = (f'\n<meta property="og:url" content="{a(dom)}/{m["slug"]}/">\n<meta property="og:image" content="{a(dom)}/{m["slug"]}/og.png">'
               '\n<meta property="og:image:width" content="1200">\n<meta property="og:image:height" content="630">'
               '\n<meta name="twitter:card" content="summary_large_image">') if dom else ""
    return f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta http-equiv="Content-Security-Policy" content="{csp}">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{e(title)}</title>
<meta name="description" content="{a(fr(m['desc']))}">
<meta name="robots" content="noindex, nofollow">
<meta name="theme-color" content="#F4F5F7">
<meta property="og:type" content="website">
<meta property="og:locale" content="fr_FR">
<meta property="og:title" content="{a(fr(title))}">
<meta property="og:description" content="{a(fr(m['desc']))}">{og_tags}
<link rel="icon" href="{favicon(accent)}" type="image/svg+xml">
<link rel="preload" href="/assets/fonts/host-grotesk-latin.woff2" as="font" type="font/woff2" crossorigin>
<style>{CSS.strip().replace("__CLOVER__", clover_bg())}</style>
</head>
<body>
<header class="es-hdr"><span class="es-logo">{logo}</span>{call}</header>
<main class="es-main">
  <div class="es-intro">
    {kick}<p class="es-pill">{ico('alert')}{e(m['pill'])}</p>
    <h1 class="es-h">{h1}</h1>
    <p class="es-lead">{e(lead)}</p>
    <a class="es-cta" href="#estimation" data-start><b>Calculer mon prix{ico('down')}</b><small>Gratuit · 1 minute · sans engagement</small></a>
    {scene}
    {trust}
    <ul class="es-facts">{facts_html}</ul>
  </div>
  <section class="es-quiz" id="estimation" aria-label="Estimation">
    <form class="es-card" id="es-form" novalidate>
      <div class="es-head"><span class="es-num-step">Étape 1 sur {n}</span><span class="es-pct">0 %</span><div class="es-bar" aria-hidden="true"><i></i></div></div>
      <div class="es-body">
        {steps}
        <div class="es-res" hidden aria-live="polite"></div>
        <p class="es-err" role="alert" hidden></p>
        <noscript><p class="es-note">Le calculateur a besoin de JavaScript. Vous pouvez aussi appeler le {e(tel)}.</p></noscript>
      </div>
      <div class="es-nav"><button type="button" class="es-back" aria-label="Question précédente" hidden>{ico('back')}</button><button type="button" class="es-next"><span>Suivant</span>{ico('arrow')}</button></div>
    </form>
  </section>
  {faq_html(m, cfg, key)}
</main>
<footer class="es-ftr">
  <p class="es-by">Proposé par {by}</p>
  <p>Estimations indicatives, sans valeur contractuelle</p>
  <div class="es-legal">{legal_html(m, cfg, key)}</div>
</footer>
{cc}
{''.join(f'<script>{s}</script>' for s in scripts)}
</body>
</html>
"""


def build(path):
    cfg = json.loads(pathlib.Path(path).read_text(encoding="utf-8"))
    warn = []
    need(cfg, warn)
    if not re.fullmatch(r"[a-z0-9][a-z0-9-]*", cfg.get("slug", "")):
        raise SystemExit(f"{path} : slug invalide (minuscules, chiffres et tirets)")
    out = HERE / "dist" / cfg["slug"]
    if out.exists():
        shutil.rmtree(out)
    (out / "assets" / "fonts").mkdir(parents=True)
    for fnt in ("host-grotesk-latin.woff2", "host-grotesk-latin-ext.woff2"):
        shutil.copy(FONTS / fnt, out / "assets" / "fonts" / fnt)
    logo_url = ""
    if cfg.get("logo"):
        src = (pathlib.Path(path).parent / cfg["logo"]).resolve()
        dst = out / "assets" / ("logo" + src.suffix.lower())
        shutil.copy(src, dst)
        logo_url = "/assets/" + dst.name
    photo_url = ""
    if cfg.get("contact", {}).get("photo"):
        src = (pathlib.Path(path).parent / cfg["contact"]["photo"]).resolve()
        dst = out / "assets" / ("contact" + src.suffix.lower())
        shutil.copy(src, dst)
        photo_url = "/assets/" + dst.name
    keys = [k for k in ORDER if k in cfg.get("metiers", ORDER)]
    (out / "assets" / "photos").mkdir(parents=True)
    photo_urls = {}
    for k in keys:
        ph = photo_of(M[k], cfg, k)
        if ph["own"]:
            src = (pathlib.Path(path).parent / ph["own"]).resolve()
            name = f"{M[k]['slug']}{src.suffix.lower()}"
            shutil.copy(src, out / "assets" / "photos" / name)
            photo_urls[k] = [(f"/assets/photos/{name}", 1200, 900)]
        else:
            photo_urls[k] = []
            for w, h_ in ph["sizes"]:
                name = f"{ph['base']}-{w}.webp"
                shutil.copy(HERE / "photos" / name, out / "assets" / "photos" / name)
                photo_urls[k].append((f"/assets/photos/{name}", w, h_))
    for k in keys:
        d = out / M[k]["slug"]
        d.mkdir(parents=True)
        (d / "index.html").write_text(page(k, cfg, logo_url, photo_url, photo_urls), encoding="utf-8")
    if shutil.which("node"):
        jobs = [{"out": str(out / M[k]["slug"] / "og.png"),
                 "html": og_html(M[k], cfg, k, cfg.get("accent", "#2D5BE3"), out / photo_urls[k][-1][0].lstrip("/"))} for k in keys]
        jf = out / "og_jobs.json"
        jf.write_text(json.dumps(jobs, ensure_ascii=False), encoding="utf-8")
        r = subprocess.run(["node", str(HERE / "og_render.js"), str(jf)], capture_output=True, text=True)
        jf.unlink()
        print("  images d’aperçu :", "faites" if r.returncode == 0 else "impossibles (" + (r.stderr.strip().splitlines() or ["?"])[-1][:120] + ")")
    if not cfg.get("domaine"):
        warn.append("domaine manquant : sans lui, les liens partagés n’affichent pas d’image d’aperçu")
    sec = [{"key": "X-Robots-Tag", "value": "noindex, nofollow"}, {"key": "X-Content-Type-Options", "value": "nosniff"},
           {"key": "X-Frame-Options", "value": "DENY"}, {"key": "Referrer-Policy", "value": "strict-origin-when-cross-origin"},
           {"key": "Strict-Transport-Security", "value": "max-age=63072000"},
           {"key": "Permissions-Policy", "value": "camera=(), microphone=(), geolocation=(), payment=()"},
           {"key": "Content-Security-Policy", "value": "frame-ancestors 'none'"}]
    (out / "vercel.json").write_text(json.dumps({
        "cleanUrls": False, "trailingSlash": True,
        "redirects": [{"source": "/", "destination": f"/{M[keys[0]]['slug']}/", "permanent": False}],
        "headers": [{"source": "/(.*)", "headers": sec},
                    {"source": "/assets/fonts/(.*)", "headers": [{"key": "Cache-Control", "value": "public, max-age=31536000, immutable"}]}]}, indent=2), encoding="utf-8")
    (out / "robots.txt").write_text("User-agent: *\nDisallow:\n", encoding="utf-8")
    print(f"{cfg['slug']} : {len(keys)} pages ({', '.join('/' + M[k]['slug'] + '/' for k in keys)}) dans {out.relative_to(HERE)}")
    for k in keys:
        print(f"  liens {M[k]['slug']} :", ", ".join(f"?projet={slug(o[0])}" for o in M[k]["steps"][0]["qs"][0]["opts"]))
    for w in warn:
        print("  à compléter :", w)


if __name__ == "__main__":
    files = sys.argv[1:] or sorted(str(p) for p in (HERE / "clients").glob("*.json"))
    for p in files:
        build(p)

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
import sys
from urllib.parse import urlparse

import icons
from metiers import COMMON, M

HERE = pathlib.Path(__file__).resolve().parent
FONTS = HERE.parent / "v8b" / "assets" / "fonts"
ORDER = ["toiture", "facade", "fenetres", "charpente", "isolation"]
MISS = {"travaux": "le type de travaux", "couverture": "votre couverture actuelle", "gouttieres": "la réponse sur les gouttières",
        "support": "le type de mur", "hauteur": "la hauteur de la maison", "fissures": "la réponse sur les fissures", "materiau": "le matériau",
        "vitrage": "le vitrage actuel", "volets": "la réponse sur les volets", "signes": "ce que vous avez remarqué",
        "combles": "l’accès aux combles", "maison": "le type de maison", "acces": "l’accès aux combles", "chauffage": "votre chauffage",
        "logement": "le type de logement", "annee": "l’année de construction", "delai": "le délai", "statut": "votre situation"}
SVG = {  # pictogrammes au trait (grille de 24)
    "phone": '<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8.1 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z"/>',
    "alert": '<path d="M10.3 3.9 1.8 18a2 2 0 0 0 1.7 3h17a2 2 0 0 0 1.7-3L13.7 3.9a2 2 0 0 0-3.4 0z M12 9v4 M12 17h.01"/>',
    "arrow": '<path d="M5 12h14 M13 6l6 6-6 6"/>',
    "back": '<path d="M15 18l-6-6 6-6"/>',
    "check": '<path d="M20 6 9 17l-5-5"/>',
    "lock": '<path d="M5 11h14v10H5z M8 11V7a4 4 0 0 1 8 0v4"/>',
    "wa": '<path d="M3.5 20.5l1.3-4.2A8.5 8.5 0 1 1 8 19.4z M9 8.5c0 3.5 3 6.5 6.5 6.5l1-1.5-2-1-1 .8c-1-.4-2.4-1.8-2.8-2.8l.8-1-1-2z"/>',
}


def ico(k, cls=""):
    c = f' class="{cls}"' if cls else ""
    return f'<svg{c} viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false">{SVG[k]}</svg>'


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
def q_html(q, sid, accent):
    n = q["name"]
    miss = a(MISS.get(n, "une réponse"))
    if q["t"] == "cards":
        opts = "".join(
            f'<button type="button" class="es-opt" data-q="{n}" data-v="{a(o[0])}" aria-pressed="false">'
            f'<span class="es-ico">{icons.house(o[2], o[3], accent)}</span>'
            f'<span class="es-ot"><b>{e(o[0])}</b><span>{e(o[1])}</span></span><span class="es-ck">{ico("check")}</span></button>'
            for o in q["opts"])
        return f'<div class="es-opts" role="group" aria-labelledby="{sid}" data-req="{n}" data-miss="{miss}">{opts}</div>'
    if q["t"] == "tiles":
        opts = "".join(
            f'<button type="button" class="es-tile" data-q="{n}" data-v="{a(lab)}" aria-pressed="false"><span class="es-sw">{icons.swatch(sw)}</span><span>{e(lab)}</span></button>'
            for lab, sw in q["opts"])
        return f'<div class="es-tiles" role="group" aria-labelledby="{sid}" data-req="{n}" data-miss="{miss}">{opts}</div>'
    if q["t"] == "range":
        units = list(q["units"]) if q.get("units") else q["unit"]
        lo = units[0] if isinstance(units, list) and q["min"] == 0 and units[0] else f'{q["min"]} {units if isinstance(units, str) else units[1 if q["min"] < 2 else 2]}'
        hi = f'{q["max"]} {units if isinstance(units, str) else units[2]}'
        return (f'<div class="es-field"><div class="es-rh"><label for="es-{n}">{e(q["label"])}</label><output for="es-{n}" aria-live="polite"></output></div>'
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
        return (f'<div class="es-field"><label class="es-lab" for="es-cp">{e(q["label"])}</label>'
                f'<input class="es-in es-in-cp" id="es-cp" name="code_postal" inputmode="numeric" autocomplete="postal-code" maxlength="5" placeholder="Ex. 69003"></div>'
                '<p class="es-note es-tenant" hidden>Les travaux sur le bâti se décident avec le propriétaire. Faites l’estimation, puis transmettez-la-lui.</p>')
    raise ValueError(q["t"])


def steps_html(m, cfg, accent):
    out = []
    allsteps = m["steps"] + COMMON
    for i, st in enumerate(allsteps):
        sid = f"es-q{i + 1}"
        auto = " data-auto" if st.get("auto") else ""
        body = "".join(q_html(q, sid, accent) for q in st["qs"])
        out.append(f'<div class="es-step" role="group" aria-labelledby="{sid}"{auto}><h2 class="es-q" id="{sid}">{e(st["title"])}</h2>'
                   f'<p class="es-sub">{e(st["sub"])}</p>{body}</div>')
    ent = e(cfg["entreprise"])
    sid = f"es-q{len(allsteps) + 1}"
    out.append(
        f'<div class="es-step es-contact" role="group" aria-labelledby="{sid}"><h2 class="es-q" id="{sid}" data-h>Votre estimation est prête</h2>'
        f'<p class="es-sub" data-s></p>'
        f'<div class="es-teaser" aria-hidden="true"><span class="es-blur">0 000 € à 0 000 €</span><span class="es-lock">{ico("lock")}Affichée juste après</span></div>'
        '<div class="es-two">'
        '<div><label class="es-lab" for="es-prenom">Prénom</label><input class="es-in" id="es-prenom" name="prenom" autocomplete="given-name" maxlength="60"></div>'
        '<div><label class="es-lab" for="es-tel">Téléphone</label><input class="es-in" id="es-tel" name="telephone" type="tel" inputmode="tel" autocomplete="tel" maxlength="20" placeholder="06 12 34 56 78"></div>'
        '</div>'
        f'<label class="es-consent"><input type="checkbox" name="consentement"><span>{e("J’accepte d’être rappelé par " + cfg["entreprise"] + " au sujet de ce projet.")}</span></label>'
        '<input class="es-hp" name="site_web" tabindex="-1" autocomplete="off" aria-hidden="true">'
        f'<p class="es-priv">{ico("lock")}<span>Vos coordonnées ne servent qu’à vous recontacter pour ce projet. Elles ne sont ni vendues ni cédées.</span></p></div>')
    return "".join(out), len(allsteps) + 1


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
    return dict(key=key, nom=m["nom"], ent=cfg["entreprise"], tel=tel, telh="+33" + re.sub(r"\D", "", tel)[1:] if tel else "",
                wa=re.sub(r"\D", "", cfg.get("whatsapp", "")), envoi=cfg.get("envoi", ""), deps=cfg.get("departements", []), zone=cfg.get("zone", ""),
                horaires=fr(cfg.get("horaires", "")), px=cfg.get("meta_pixel", ""), qty=m["qty"], opts=opts,
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
:root{--ink:#0A1424;--ink2:#2B3444;--muted:#5B6475;--line:rgba(10,20,36,.12);--soft:#F3F5F8;--go:#15803D;--go-h:#116B33;--go-bar:#16A34A;--go-bg:#EEF8F1;--sun:#FFE15A;--r:14px;--f:"Host Grotesk",system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;color-scheme:light}
*{box-sizing:border-box;margin:0}
html{-webkit-text-size-adjust:100%}
body{min-height:100vh;display:flex;flex-direction:column;font:400 16px/1.5 var(--f);color:var(--ink);background:#fff;-webkit-font-smoothing:antialiased}
main{flex:1}
a{color:inherit}
button{font:inherit;color:inherit;cursor:pointer;-webkit-tap-highlight-color:transparent}
:focus-visible{outline:2px solid var(--ink);outline-offset:3px}
[hidden]{display:none!important}
svg{display:block}
.es-hdr{display:flex;align-items:center;justify-content:space-between;gap:12px;width:100%;max-width:1120px;margin:0 auto;padding:12px 16px}
.es-logo{display:flex;align-items:center;min-height:44px}
.es-logo img{display:block;height:36px;width:auto;max-width:180px;object-fit:contain}
.es-name{font-weight:600;font-size:1.06rem;letter-spacing:-.01em;line-height:1.2}
.es-call{display:inline-flex;align-items:center;gap:8px;flex:none;min-height:44px;padding:0 16px;border-radius:999px;background:var(--go);color:#fff;text-decoration:none;font-weight:600;font-size:.95rem;font-variant-numeric:tabular-nums;transition:background .2s}
.es-call:hover{background:var(--go-h)}
.es-call svg{width:18px;height:18px}
.es-call .es-short{display:none}
@media (max-width:380px){.es-call .es-num{display:none}.es-call .es-short{display:inline}}
.es-hero{display:grid;gap:32px;width:100%;max-width:1120px;margin:0 auto;padding:20px 16px 48px}
.es-kick{margin-bottom:12px;font-size:.9rem;color:var(--muted)}
.es-pill{display:inline-flex;align-items:center;gap:8px;padding:8px 14px;border-radius:999px;background:var(--sun);font-size:.86rem;font-weight:500;line-height:1.3}
.es-pill svg{width:16px;height:16px;flex:none}
.es-h{margin-top:16px;font-weight:600;font-size:clamp(2.3rem,10.4vw,4.4rem);line-height:1.08;letter-spacing:-.035em;text-wrap:balance}
.es-h mark{padding:0 .14em;border-radius:.1em;background:var(--ink);color:#fff;-webkit-box-decoration-break:clone;box-decoration-break:clone}
.es-h em{font-style:italic;text-decoration:underline;text-decoration-color:var(--go-bar);text-decoration-thickness:.09em;text-underline-offset:.12em}
.es-lead{margin-top:16px;max-width:38ch;font-size:1.08rem;line-height:1.5;color:var(--ink2)}
.es-cta{display:flex;flex-direction:column;align-items:center;justify-content:center;gap:2px;width:100%;max-width:440px;min-height:72px;margin-top:24px;padding:12px 20px;border:0;border-radius:16px;background:var(--go);color:#fff;box-shadow:0 14px 30px -16px rgba(10,20,36,.5);transition:background .2s,transform .2s}
.es-cta:hover{background:var(--go-h)}
.es-cta:active{transform:scale(.985)}
.es-cta b{display:inline-flex;align-items:center;gap:8px;font-size:1.22rem;font-weight:600}
.es-cta b svg{width:22px;height:22px}
.es-cta small{font-size:.86rem;opacity:.9}
.es-facts{display:flex;flex-wrap:wrap;gap:8px 18px;margin-top:20px;padding:0;list-style:none;font-size:.9rem;color:var(--ink2)}
.es-facts li{display:inline-flex;align-items:center;gap:6px}
.es-facts svg{width:16px;height:16px;color:var(--go)}
.es-art{max-width:340px;padding:16px 20px;border-radius:24px;background:var(--soft)}
.es-art svg{width:100%;height:auto}
@media (min-width:900px){.es-hero{grid-template-columns:minmax(0,1.2fr) minmax(0,.8fr);align-items:center;gap:56px;padding:56px 32px 88px}.es-art{max-width:none;padding:24px;border-radius:28px}}
.es-wrap{width:100%;max-width:760px;margin:0 auto;padding:8px 16px 48px;display:none}
.is-quiz .es-wrap{display:block}
.is-quiz .es-hero{display:none}
.es-card{padding:20px;border:1px solid var(--line);border-radius:20px;background:#fff;box-shadow:0 24px 60px -36px rgba(10,20,36,.35)}
@media (min-width:760px){.es-card{padding:32px}.es-wrap{padding-top:24px}}
.es-top{display:flex;justify-content:space-between;align-items:baseline;font-size:.86rem;color:var(--muted);font-variant-numeric:tabular-nums}
.es-pct{font-weight:600;color:var(--go)}
.es-bar{height:8px;margin-top:8px;overflow:hidden;border-radius:8px;background:var(--soft)}
.es-bar i{display:block;width:0;height:100%;border-radius:inherit;background:var(--go-bar);transition:width .45s cubic-bezier(.2,.7,.2,1)}
.es-step{display:none;margin-top:24px}
.es-step.is-on{display:block;animation:es-in .35s cubic-bezier(.2,.7,.2,1)}
@keyframes es-in{from{opacity:0;transform:translateY(8px)}}
.es-q{font-size:clamp(1.45rem,5.6vw,1.95rem);font-weight:600;line-height:1.15;letter-spacing:-.025em;text-wrap:balance}
.es-sub{margin-top:6px;font-size:.98rem;color:var(--muted)}
.es-opts{display:grid;gap:10px;margin-top:20px}
@media (min-width:640px){.es-opts{grid-template-columns:1fr 1fr}}
.es-opt{position:relative;display:grid;grid-template-columns:72px minmax(0,1fr);align-items:center;gap:14px;min-height:88px;padding:8px 44px 8px 8px;border:1.5px solid var(--line);border-radius:var(--r);background:#fff;text-align:left;transition:border-color .15s,background .15s}
.es-opt:hover,.es-tile:hover,.es-chip:hover{border-color:rgba(10,20,36,.32)}
.es-ico{display:grid;place-items:center;width:72px;height:68px;border-radius:10px;background:var(--soft)}
.es-ico svg{width:64px;height:auto}
.es-ot b{display:block;font-size:1rem;font-weight:600;line-height:1.25}
.es-ot span{display:block;margin-top:2px;font-size:.88rem;line-height:1.35;color:var(--muted)}
.es-ck{position:absolute;top:50%;right:12px;display:grid;place-items:center;width:22px;height:22px;margin-top:-11px;border:1.5px solid var(--line);border-radius:50%;color:#fff}
.es-ck svg{width:14px;height:14px;opacity:0}
.es-opt[aria-pressed="true"],.es-tile[aria-pressed="true"],.es-chip[aria-pressed="true"]{border-color:var(--go);background:var(--go-bg)}
.es-opt[aria-pressed="true"] .es-ck{border-color:var(--go);background:var(--go)}
.es-opt[aria-pressed="true"] .es-ck svg{opacity:1}
.es-tiles{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:10px;margin-top:20px}
.es-tile{display:flex;flex-direction:column;gap:8px;padding:8px 8px 10px;border:1.5px solid var(--line);border-radius:var(--r);background:#fff;font-size:.9rem;font-weight:500;line-height:1.25;text-align:center}
.es-sw{display:block;aspect-ratio:4/3;overflow:hidden;border-radius:8px}
.es-sw svg{width:100%;height:100%}
.es-field{margin-top:24px}
.es-lab{display:block;margin-bottom:10px;font-size:1rem;font-weight:600}
.es-seg{display:flex;flex-wrap:wrap;gap:8px}
.es-chip{min-height:48px;padding:0 16px;border:1.5px solid var(--line);border-radius:12px;background:#fff;font-size:.95rem;font-weight:500}
.es-chip[aria-pressed="true"]{color:#0B4D24}
.es-rh{display:flex;justify-content:space-between;align-items:baseline;gap:12px}
.es-rh label{font-weight:600}
.es-rh output{font-size:1.9rem;font-weight:600;letter-spacing:-.03em;font-variant-numeric:tabular-nums;white-space:nowrap}
.es-range{-webkit-appearance:none;appearance:none;width:100%;height:40px;margin:4px 0 0;background:transparent;cursor:pointer;--p:50%}
.es-range::-webkit-slider-runnable-track{height:8px;border-radius:8px;background:linear-gradient(to right,var(--go-bar) var(--p),#E3E7ED var(--p))}
.es-range::-moz-range-track{height:8px;border-radius:8px;background:#E3E7ED}
.es-range::-moz-range-progress{height:8px;border-radius:8px;background:var(--go-bar)}
.es-range::-webkit-slider-thumb{-webkit-appearance:none;width:30px;height:30px;margin-top:-11px;border:4px solid var(--go);border-radius:50%;background:#fff;box-shadow:0 4px 10px -2px rgba(10,20,36,.3)}
.es-range::-moz-range-thumb{width:22px;height:22px;border:4px solid var(--go);border-radius:50%;background:#fff}
.es-mm{display:flex;justify-content:space-between;font-size:.82rem;color:var(--muted)}
.es-in{width:100%;height:54px;padding:0 14px;border:1.5px solid var(--line);border-radius:12px;background:#fff;font:inherit;font-size:1.06rem}
.es-in:focus{border-color:var(--go);outline:none;box-shadow:0 0 0 3px rgba(22,163,74,.2)}
.es-in[aria-invalid="true"]{border-color:#B42318}
.es-in-cp{max-width:200px;font-variant-numeric:tabular-nums;letter-spacing:.04em}
.es-two{display:grid;gap:14px;margin-top:20px}
@media (min-width:640px){.es-two{grid-template-columns:1fr 1fr}}
.es-consent{display:flex;align-items:flex-start;gap:10px;margin-top:16px;font-size:.9rem;line-height:1.45;color:var(--ink2);cursor:pointer}
.es-consent input{flex:none;width:20px;height:20px;margin-top:1px;accent-color:var(--go)}
.es-hp{position:absolute;left:-9999px;width:1px;height:1px;opacity:0}
.es-priv{display:flex;gap:8px;margin-top:12px;font-size:.84rem;line-height:1.45;color:var(--muted)}
.es-priv svg{flex:none;width:16px;height:16px;margin-top:2px}
.es-note{margin-top:16px;padding:12px 14px;border-radius:12px;background:var(--soft);font-size:.92rem;line-height:1.45;color:var(--ink2)}
.es-teaser{display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;gap:8px 16px;margin-top:18px;padding:16px 18px;border-radius:16px;background:var(--soft)}
.es-blur{font-size:1.6rem;font-weight:600;letter-spacing:-.02em;filter:blur(8px);-webkit-user-select:none;user-select:none}
.es-lock{display:inline-flex;align-items:center;gap:6px;font-size:.86rem;font-weight:500;color:var(--ink2)}
.es-lock svg{width:16px;height:16px}
.es-err{margin-top:16px;font-size:.94rem;color:#B42318}
.es-nav{display:flex;justify-content:space-between;align-items:center;gap:12px;margin-top:28px;padding-top:16px;border-top:1px solid var(--line)}
.es-prev{display:inline-flex;align-items:center;gap:4px;min-height:48px;padding:0 8px 0 0;border:0;background:none;font-weight:500;color:var(--muted)}
.es-prev svg{width:20px;height:20px}
.es-next{display:inline-flex;align-items:center;gap:8px;min-height:54px;padding:0 22px;border:0;border-radius:14px;background:var(--go);color:#fff;font-size:1.05rem;font-weight:600;transition:background .2s}
.es-next:hover{background:var(--go-h)}
.es-next svg{width:20px;height:20px}
.es-next span{white-space:nowrap}
@media (max-width:420px){.es-prev{width:48px;justify-content:center;padding:0;border:1.5px solid var(--line);border-radius:12px}.es-prev span{display:none}.es-next{flex:1;justify-content:center}}
.es-res-k{font-size:.92rem;color:var(--muted)}
.es-amount{margin-top:4px;font-size:clamp(2.1rem,9vw,3.1rem);font-weight:600;line-height:1.05;letter-spacing:-.035em;font-variant-numeric:tabular-nums}
.es-amount-f{margin-top:8px;font-size:.94rem;color:var(--ink2)}
.es-lines{margin-top:20px;padding:0;list-style:none;border-top:1px solid var(--line)}
.es-lines li{display:grid;grid-template-columns:minmax(0,1fr) auto;gap:2px 12px;padding:12px 0;border-bottom:1px solid var(--line);font-size:.95rem}
.es-val{font-weight:600;text-align:right;white-space:nowrap;font-variant-numeric:tabular-nums}
.es-calc{grid-column:1/-1;font-size:.85rem;color:var(--muted)}
.es-h3{margin-top:24px;font-size:1rem;font-weight:600}
.es-list{margin-top:6px;padding-left:20px;font-size:.95rem;color:var(--ink2)}
.es-p{margin-top:6px;font-size:.95rem;color:var(--ink2)}
.es-box{margin-top:28px;padding:20px;border-radius:16px;background:var(--ink);color:#fff}
.es-box-k{font-size:.86rem;color:#A9B4C6}
.es-box-h{margin-top:4px;font-size:1.3rem;font-weight:600;line-height:1.2;letter-spacing:-.015em}
.es-box-p{margin-top:6px;font-size:.95rem;color:#D5DBE5}
.es-acts{display:flex;flex-wrap:wrap;gap:10px;margin-top:16px}
.es-btn{display:inline-flex;align-items:center;justify-content:center;gap:8px;min-height:52px;padding:0 18px;border-radius:12px;font-weight:600;text-decoration:none}
.es-btn svg{width:20px;height:20px}
.es-btn-wa{background:#25D366;color:#0A1424}
.es-btn-call{background:#fff;color:var(--ink)}
.es-box[data-state="sending"] .es-s-sent,.es-box[data-state="sending"] .es-s-manual,.es-box[data-state="sent"] .es-s-sending,.es-box[data-state="sent"] .es-s-manual,.es-box[data-state="manual"] .es-s-sending,.es-box[data-state="manual"] .es-s-sent{display:none}
.es-again{min-height:44px;margin-top:12px;border:0;background:none;color:var(--muted);text-decoration:underline;text-underline-offset:3px}
.es-ftr{padding:28px 16px 40px;border-top:1px solid var(--line);font-size:.86rem;color:var(--muted);text-align:center}
.es-by{display:flex;align-items:center;justify-content:center;gap:10px;flex-wrap:wrap}
.es-by img{height:28px;width:auto;max-width:150px;object-fit:contain}
.es-by b{color:var(--ink);font-weight:600}
.es-ftr>p+p{margin-top:8px}
.es-legal{max-width:640px;margin:14px auto 0;text-align:left}
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
.es-cc button{min-height:46px;border:1.5px solid #fff;border-radius:10px;background:transparent;color:#fff;font-weight:600}
@media (prefers-reduced-motion:reduce){*{animation:none!important;transition:none!important}}
"""

JS = r"""(function(){
var C=__CFG__,d=document;
var f=d.getElementById("es-form");if(!f)return;
var steps=[].slice.call(f.querySelectorAll(".es-step")),N=steps.length,cur=-1,A={},done=false;
var bar=f.querySelector(".es-bar i"),pct=f.querySelector(".es-pct"),num=f.querySelector(".es-num-step"),prev=f.querySelector(".es-prev"),next=f.querySelector(".es-next"),nextL=next.querySelector("span"),err=f.querySelector(".es-err"),res=f.querySelector(".es-res");
var qs=new URLSearchParams(location.search),track={};["utm_source","utm_medium","utm_campaign","utm_content","utm_term","fbclid","gclid"].forEach(function(k){if(qs.get(k))track[k]=qs.get(k).slice(0,200)});
function each(l,fn){[].forEach.call(l,fn)}
function dl(ev,p){var o={event:ev,metier:C.key};for(var k in p)o[k]=p[k];(window.dataLayer=window.dataLayer||[]).push(o)}
function esc(s){return String(s).replace(/[&<>"]/g,function(c){return{"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]})}
function nb(n){return Math.round(n).toLocaleString("fr-FR").replace(/\s/g,"\u202f")}
function eur(n){return nb(n)+"\u00a0€"}
function lab(v,u){if(Array.isArray(u)){if(v===0&&u[0])return u[0];return v+"\u00a0"+(v>1?u[2]:u[1])}return v+"\u00a0"+u}
function val(k){var x=f.querySelector("[name="+k+"]");return x?(x.value||"").trim():""}
each(f.querySelectorAll(".es-range"),function(r){var o=f.querySelector('output[for="'+r.id+'"]'),u=JSON.parse(r.getAttribute("data-units"));
  function up(){var v=+r.value;A[r.getAttribute("data-q")]=v;o.textContent=lab(v,u);r.style.setProperty("--p",(100*(v-r.min)/(r.max-r.min))+"%")}
  r.addEventListener("input",up);up()});
function refresh(){each(f.querySelectorAll("[data-show]"),function(x){var s=JSON.parse(x.getAttribute("data-show"));x.hidden=s[1].indexOf(A[s[0]])<0});
  var t=f.querySelector(".es-tenant");if(t)t.hidden=A.statut!=="Locataire"}
f.addEventListener("click",function(ev){var b=ev.target.closest("button[data-q]");if(!b||!f.contains(b))return;
  var k=b.getAttribute("data-q"),g=f.querySelectorAll('button[data-q="'+k+'"]'),multi=b.hasAttribute("data-multi");
  if(multi){var on=b.getAttribute("aria-pressed")!=="true",ex=b.hasAttribute("data-excl");
    each(g,function(x){if(x===b)x.setAttribute("aria-pressed",on?"true":"false");else if(on&&(ex||x.hasAttribute("data-excl")))x.setAttribute("aria-pressed","false")});
    var sel=[].filter.call(g,function(x){return x.getAttribute("aria-pressed")==="true"}).map(function(x){return x.getAttribute("data-v")});if(sel.length)A[k]=sel;else delete A[k]}
  else{each(g,function(x){x.setAttribute("aria-pressed",x===b?"true":"false")});A[k]=b.getAttribute("data-v")}
  err.hidden=true;refresh();
  var st=steps[cur];if(st&&st.hasAttribute("data-auto")&&!multi)setTimeout(function(){if(steps[cur]===st)go(1)},260)});
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
function amount(E){return E.fixed?"environ "+eur(E.lo):eur(E.lo)+" à "+eur(E.hi)}
function rowAmount(r){return r.lo===r.hi?"environ "+eur(Math.round(r.tlo/100)*100):eur(rnd(r.tlo,false))+" à "+eur(rnd(r.thi,true))}
function rowUnit(r){return(r.lo===r.hi?(r.approx?"environ ":"")+nb(r.lo):nb(r.lo)+" à "+nb(r.hi))+"\u00a0"+r.u}
function outZone(){if(!C.deps.length||!A.code_postal)return false;var cp=A.code_postal,dep=cp.slice(0,2)==="97"?cp.slice(0,3):cp.slice(0,2);if(dep==="20")dep=+cp<20200?"2A":"2B";return C.deps.indexOf(dep)<0&&C.deps.indexOf(cp.slice(0,2))<0}
function prep(){var st=steps[N-1],h=st.querySelector("[data-h]"),s=st.querySelector("[data-s]"),t=st.querySelector(".es-teaser");
  if(rows().length){h.textContent="Votre estimation est prête";s.textContent="Indiquez votre prénom et votre numéro\u00a0: elle s’affiche aussitôt, et "+C.ent+" vous rappelle pour la confirmer.";t.hidden=false;t.querySelector(".es-blur").textContent=amount(estimate())}
  else{h.textContent="Votre demande est prête";s.textContent="Ce type de travaux se chiffre sur place. Indiquez votre prénom et votre numéro\u00a0: "+C.ent+" vous rappelle pour fixer une visite.";t.hidden=true}}
function show(i,push){cur=i;each(steps,function(s,j){s.classList.toggle("is-on",j===i)});
  var p=Math.round(100*(i+1)/(N+1));bar.style.width=p+"%";pct.textContent=p+"\u00a0%";num.textContent="Étape "+(i+1)+" sur "+N;
  err.hidden=true;refresh();if(i===N-1)prep();
  nextL.textContent=i===N-1?(rows().length?"Voir mon estimation":"Envoyer ma demande"):"Suivant";
  if(push)history.pushState({es:i},"");
  var c=d.getElementById("estimation"),y=c.getBoundingClientRect().top+scrollY-8;if(scrollY>y)scrollTo(0,y)}
function intro(){d.body.classList.remove("is-quiz");cur=-1;scrollTo(0,0)}
function start(){d.body.classList.add("is-quiz");show(0,true);scrollTo(0,0);dl("estimation_debut",{})}
each(d.querySelectorAll("[data-start]"),function(b){b.addEventListener("click",start)});
addEventListener("popstate",function(ev){if(done)return;var s=ev.state&&typeof ev.state.es==="number"?ev.state.es:-1;if(s<0)intro();else{d.body.classList.add("is-quiz");show(s,false)}});
prev.addEventListener("click",function(){if(history.state&&typeof history.state.es==="number")history.back();else if(cur>0)show(cur-1,false);else intro()});
function check(i){var st=steps[i],bad=[];
  each(st.querySelectorAll("[data-req]"),function(x){if(x.hidden)return;var v=A[x.getAttribute("data-req")];if(v===undefined||v===""||(Array.isArray(v)&&!v.length))bad.push(x.getAttribute("data-miss"))});
  var cp=st.querySelector("[name=code_postal]");if(cp){var ok=/^\d{5}$/.test(cp.value.trim());if(ok){A.code_postal=cp.value.trim();cp.removeAttribute("aria-invalid")}else{cp.setAttribute("aria-invalid","true");bad.push("un code postal à 5 chiffres")}}
  var pr=st.querySelector("[name=prenom]");if(pr){var tel=st.querySelector("[name=telephone]"),ok2=st.querySelector("[name=consentement]");
    if(pr.value.trim().length<2){pr.setAttribute("aria-invalid","true");bad.push("votre prénom")}else pr.removeAttribute("aria-invalid");
    if(tel.value.replace(/\D/g,"").length<10){tel.setAttribute("aria-invalid","true");bad.push("un numéro de téléphone")}else tel.removeAttribute("aria-invalid");
    if(!ok2.checked)bad.push("votre accord pour être rappelé")}
  return bad}
function go(dir){if(dir<=0)return;var bad=check(cur);
  if(bad.length){err.textContent="Il manque "+bad.join(", ")+".";err.hidden=false;var x=steps[cur].querySelector('[aria-invalid="true"]');if(x)x.focus();return}
  if(cur===N-1){submit();return}
  dl("estimation_etape",{etape:cur+1});show(cur+1,true)}
next.addEventListener("click",function(){go(1)});
f.addEventListener("submit",function(ev){ev.preventDefault();go(1)});
f.addEventListener("input",function(){if(err.hidden||cur<0)return;var bad=check(cur);if(bad.length)err.textContent="Il manque "+bad.join(", ")+".";else err.hidden=true});
function render(E,pr,telf){var o=C.opts[A.travaux]||{},h='<p class="es-res-k">Votre estimation, '+esc(pr)+'</p>';
  if(E.rows.length){h+='<p class="es-amount">'+amount(E)+'</p><p class="es-amount-f">Fourchette indicative, pose comprise, pour '+ql()+'.</p><ul class="es-lines">';
    E.rows.forEach(function(r){h+='<li><span>'+esc(r.l)+'</span><span class="es-val">'+rowAmount(r)+'</span><span class="es-calc">'+ql()+" × "+rowUnit(r)+" · "+(r.src?'Source\u00a0: <a href="'+esc(r.src[1])+'" target="_blank" rel="noopener">'+esc(r.src[0])+"</a>":"Tarif de "+esc(C.ent))+'</span></li>'});h+="</ul>"}
  else h+='<p class="es-amount">À chiffrer sur place</p><p class="es-amount-f">'+esc(o.vt||"Ce type de travaux se chiffre après une visite.")+'</p>';
  C.notes.forEach(function(n){if(A[n.q]===n.eq)h+='<p class="es-note">'+esc(n.txt)+"</p>"});
  var vis=[];C.visite.forEach(function(r){var v=A[r.q];if((r.gt!==undefined&&v>r.gt)||(r.eq!==undefined&&v===r.eq))vis.push(r.txt.replace("{v}",v).replace("(s)",v>1?"s":""))});
  if(vis.length){h+='<p class="es-h3">Chiffré à la visite</p><ul class="es-list">';vis.forEach(function(v){h+="<li>"+esc(v)+"</li>"});h+="</ul>"}
  h+='<p class="es-h3">Ce qui fait varier le prix</p><p class="es-p">'+esc(C.varie)+'</p>';
  if(C.aides)h+='<p class="es-note">'+esc(C.aides)+'</p>';
  if(A.statut==="Locataire")h+='<p class="es-note">Les travaux sur le bâti se décident avec le propriétaire\u00a0: transmettez-lui cette estimation.</p>';
  if(outZone())h+='<p class="es-note">Votre chantier semble hors de la zone habituelle de '+esc(C.ent)+(C.zone?" ("+esc(C.zone)+")":"")+'. Nous vous dirons rapidement si nous pouvons intervenir.</p>';
  var call=C.tel?'<a class="es-btn es-btn-call" href="tel:'+C.telh+'">'+ICO.phone+"Appeler le "+esc(C.tel)+"</a>":"";
  h+='<div class="es-box" data-state="'+(C.envoi?"sending":"manual")+'"><p class="es-box-k">Prochaine étape</p>'
   +'<div class="es-s-sending"><p class="es-box-h">Envoi de votre demande…</p></div>'
   +'<div class="es-s-sent"><p class="es-box-h">C’est noté, '+esc(pr)+'.</p><p class="es-box-p">'+esc(C.ent)+" vous rappelle au "+esc(telf)+(C.horaires?", "+esc(C.horaires):"")+' pour fixer une visite et vous remettre un devis.</p><div class="es-acts">'+call+"</div></div>"
   +'<div class="es-s-manual">'+(C.wa?'<p class="es-box-h">Envoyez votre demande à '+esc(C.ent)+'</p><p class="es-box-p">Votre message est déjà rédigé, il ne reste qu’à l’envoyer.</p><div class="es-acts"><a class="es-btn es-btn-wa" target="_blank" rel="noopener" data-wa>'+ICO.wa+"Envoyer sur WhatsApp</a>"+call+"</div>"
     :'<p class="es-box-h">Appelez '+esc(C.ent)+' pour fixer la visite</p><div class="es-acts">'+call+"</div>")+"</div></div>"
   +'<button type="button" class="es-again">Refaire une estimation</button>';
  return h}
var ICO=__ICO__;
function submit(){if(val("site_web"))return;var E=estimate(),pr=val("prenom"),tel=val("telephone"),dg=tel.replace(/\D/g,""),telf=dg.length===10?dg.replace(/(\d{2})(?=\d)/g,"$1\u00a0"):tel;
  var est=E.rows.length?amount(E):"à chiffrer sur place";
  var det=C.details.map(function(k){var v=A[k[0]];if(v===undefined||v===0)return null;return k[1]+"\u00a0: "+(Array.isArray(v)?v.join(", "):v)}).filter(Boolean);
  var msg="Bonjour, j’ai fait l’estimation "+C.nom+" sur votre site. Travaux\u00a0: "+A.travaux+", "+ql()+". Estimation\u00a0: "+est+". "+det.join(". ")+". "+A.delai+", "+(A.statut||"").toLowerCase()+", code postal "+A.code_postal+". "+pr+", "+telf+".";
  res.innerHTML=render(E,pr,telf);res.hidden=false;each(steps,function(s){s.classList.remove("is-on")});
  f.querySelector(".es-top").hidden=true;f.querySelector(".es-bar").hidden=true;f.querySelector(".es-nav").hidden=true;err.hidden=true;done=true;
  try{history.replaceState({es:"fin"},"")}catch(x){}
  var c=d.getElementById("estimation");scrollTo(0,c.getBoundingClientRect().top+scrollY-8);
  var wa=res.querySelector("[data-wa]");if(wa)wa.href="https://wa.me/"+C.wa+"?text="+encodeURIComponent(msg);
  res.querySelector(".es-again").addEventListener("click",function(){location.href=location.pathname+location.search});
  dl("estimation_demande",{travaux:A.travaux,delai:A.delai,statut:A.statut,estimation:est});
  if(window.fbq)window.fbq("track","Lead");
  var box=res.querySelector(".es-box");if(!C.envoi)return;
  var body={type:"estimation",metier:C.key,entreprise:C.ent,fields:{travaux:A.travaux,quantite:ql(),estimation:est,details:det,delai:A.delai,statut:A.statut,code_postal:A.code_postal,prenom:pr,telephone:tel},
    consent:{text:f.querySelector(".es-consent span").textContent,at:new Date().toISOString()},page:location.pathname,tracking:track,site_web:""};
  var fin=false,end=function(ok){if(fin)return;fin=true;box.setAttribute("data-state",ok?"sent":"manual");dl("estimation_envoi",{envoi:ok?"auto":"manuel"})},t=setTimeout(function(){end(false)},8000);
  try{fetch(C.envoi,{method:"POST",headers:{"Content-Type":"application/json","Accept":"application/json"},body:JSON.stringify(body)}).then(function(r){clearTimeout(t);end(r.ok)}).catch(function(){clearTimeout(t);end(false)})}catch(x){clearTimeout(t);end(false)}}
})();"""

PIXEL_JS = r"""(function(){var C=__PX__,K="es-consent",d=document,bar=d.getElementById("es-cc");if(!bar)return;
function load(){if(window.fbq)return;!function(f,b,e,v,n,t,s){if(f.fbq)return;n=f.fbq=function(){n.callMethod?n.callMethod.apply(n,arguments):n.queue.push(arguments)};if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version="2.0";n.queue=[];t=b.createElement(e);t.async=!0;t.src=v;s=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s)}(window,d,"script","https://connect.facebook.net/en_US/fbevents.js");window.fbq("init",C);window.fbq("track","PageView")}
var v=null;try{v=JSON.parse(localStorage.getItem(K))}catch(x){}
if(v&&Date.now()-v.t<1.5e10){if(v.ok)load()}else bar.hidden=false;
[].forEach.call(bar.querySelectorAll("button"),function(b){b.addEventListener("click",function(){var ok=b.getAttribute("data-cc")==="1";try{localStorage.setItem(K,JSON.stringify({ok:ok,t:Date.now()}))}catch(x){}bar.hidden=true;if(ok)load();else if(window.fbq)location.reload()})});
[].forEach.call(d.querySelectorAll(".es-cc-open"),function(b){b.addEventListener("click",function(){bar.hidden=false})})})();"""


def page(key, cfg, logo_url):
    m = M[key]
    accent = cfg.get("accent", "#2D5BE3")
    ent = cfg["entreprise"]
    tel = cfg.get("telephone", "")
    telh = "+33" + re.sub(r"\D", "", tel)[1:] if tel else ""
    steps, n = steps_html(m, cfg, accent)
    logo = f'<img src="{logo_url}" alt="{a(ent)}" width="180" height="36">' if logo_url else f'<span class="es-name">{e(ent)}</span>'
    call = (f'<a class="es-call" href="tel:{telh}">{ico("phone")}<span class="es-num">{e(tel)}</span><span class="es-short">Appeler</span></a>' if tel else "")
    own = bool(cfg.get("tarifs", {}).get(key))
    facts = ["6 questions, 1 minute", f"Tarifs de {ent}" if own else "Prix publiés et sourcés", "Sans engagement"] + list(cfg.get("atouts", []))
    facts_html = "".join(f"<li>{ico('check')}{e(x)}</li>" for x in facts)
    kick = f'<p class="es-kick">{e(m["artisan"].capitalize())} · {e(cfg["zone"])}</p>' if cfg.get("zone") else ""
    lead = (f"Six questions, une minute. Le calculateur applique à votre projet les tarifs indicatifs de {ent}." if own
            else f"Six questions, une minute. Le calculateur applique à votre projet les prix publiés par {m['sources']}.")
    by = f'<img src="{logo_url}" alt="{a(ent)}" width="150" height="28">' if logo_url else f"<b>{e(ent)}</b>"
    cc = ('<div class="es-cc" id="es-cc" role="dialog" aria-label="Cookies" hidden><p>Acceptez-vous un cookie de Meta qui mesure l’efficacité de nos annonces ? '
          'Sans accord, rien n’est déposé.</p><div><button type="button" data-cc="0">Refuser</button><button type="button" data-cc="1">Accepter</button></div></div>') if cfg.get("meta_pixel") else ""
    cfg_json = json.dumps(cfg_js(key, m, cfg), ensure_ascii=False, separators=(",", ":"))
    ico_json = json.dumps({"phone": ico("phone"), "wa": ico("wa")}, ensure_ascii=False)
    js = JS.replace("__CFG__", cfg_json).replace("__ICO__", ico_json)
    scripts = [js] + ([PIXEL_JS.replace("__PX__", json.dumps(cfg["meta_pixel"]))] if cfg.get("meta_pixel") else [])
    hashes = " ".join("'sha256-" + base64.b64encode(hashlib.sha256(s.encode()).digest()).decode() + "'" for s in scripts)
    env_origin = ""
    if cfg.get("envoi"):
        u = urlparse(cfg["envoi"])
        env_origin = f" {u.scheme}://{u.netloc}" if u.netloc else ""
    fb = " https://connect.facebook.net" if cfg.get("meta_pixel") else ""
    csp = (f"default-src 'self'; script-src 'self' {hashes}{fb}; style-src 'self' 'unsafe-inline'; img-src 'self' data:{' https://www.facebook.com' if fb else ''}; "
           f"font-src 'self'; connect-src 'self'{env_origin}{' https://www.facebook.com' + fb if fb else ''}; form-action 'none'; base-uri 'self'; object-src 'none'")
    title = f"{m['title']} | {ent}"
    hero_art = icons.house(m["hero"], None, accent, s=16, title=f"Maison : {m['nom']} mise en évidence")
    return f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta http-equiv="Content-Security-Policy" content="{csp}">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{e(title)}</title>
<meta name="description" content="{a(fr(m['desc']))}">
<meta name="robots" content="noindex, nofollow">
<meta name="theme-color" content="#ffffff">
<meta property="og:type" content="website">
<meta property="og:locale" content="fr_FR">
<meta property="og:title" content="{a(fr(title))}">
<meta property="og:description" content="{a(fr(m['desc']))}">
<link rel="preload" href="/assets/fonts/host-grotesk-latin.woff2" as="font" type="font/woff2" crossorigin>
<style>{CSS.strip()}</style>
</head>
<body>
<header class="es-hdr"><span class="es-logo">{logo}</span>{call}</header>
<main>
<section class="es-hero" aria-labelledby="es-h">
  <div>
    {kick}<p class="es-pill">{ico('alert')}{e(m['pill'])}</p>
    <h1 class="es-h" id="es-h">{re.sub(r"<mark>(.*?)</mark>", lambda x: "<mark>" + x.group(1).replace(" ", "\u00a0") + "</mark>", fr(m['h1']))}</h1>
    <p class="es-lead">{e(lead)}</p>
    <button type="button" class="es-cta" data-start><b>Calculer le montant{ico('arrow')}</b><small>Gratuit et immédiat</small></button>
    <noscript><p class="es-note">Le calculateur a besoin de JavaScript. Vous pouvez aussi appeler le {e(tel)}.</p></noscript>
    <ul class="es-facts">{facts_html}</ul>
  </div>
  <div class="es-art">{hero_art}</div>
</section>
<section class="es-wrap" id="estimation" aria-label="Estimation">
<form class="es-card" id="es-form" novalidate>
  <div class="es-top"><span class="es-num-step">Étape 1 sur {n}</span><span class="es-pct">0 %</span></div>
  <div class="es-bar" aria-hidden="true"><i></i></div>
  {steps}
  <div class="es-res" hidden aria-live="polite"></div>
  <p class="es-err" role="alert" hidden></p>
  <div class="es-nav"><button type="button" class="es-prev" aria-label="Précédent">{ico('back')}<span>Précédent</span></button><button type="button" class="es-next"><span>Suivant</span>{ico('arrow')}</button></div>
</form>
</section>
</main>
<footer class="es-ftr">
  <p class="es-by">Proposé par {by}</p>
  <p>Estimations indicatives, sans valeur contractuelle.</p>
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
    keys = [k for k in ORDER if k in cfg.get("metiers", ORDER)]
    for k in keys:
        d = out / M[k]["slug"]
        d.mkdir(parents=True)
        (d / "index.html").write_text(page(k, cfg, logo_url), encoding="utf-8")
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
    for w in warn:
        print("  à compléter :", w)


if __name__ == "__main__":
    files = sys.argv[1:] or sorted(str(p) for p in (HERE / "clients").glob("*.json"))
    for p in files:
        build(p)

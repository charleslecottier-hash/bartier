#!/usr/bin/env python3
"""Diagnostic secteur de Bartier & Co : un PDF de 2 pages pour un artisan, puis 20 minutes au téléphone pour le commenter.

    python3 generer.py prospects/<fiche>.json          # complète ce qui manque (Insee, avis Google), puis fait le PDF
    python3 generer.py prospects/<fiche>.json --maj    # relève à nouveau l'Insee et les avis Google

La fiche JSON se remplit à la main pour le reste (voir README.md) :
  - recherches_google : à relever dans le Planificateur de mots clés de Google Ads ;
  - pubs : annonces actives dans la Bibliothèque publicitaire Meta (captures facultatives, dans captures/).
Tant que les recherches Google manquent, le PDF porte la mention « Brouillon ».
Aucun chiffre n'est inventé : chaque donnée affichée a sa source et sa date dans le PDF.
"""
import datetime
import html
import json
import os
import pathlib
import re
import subprocess
import sys
import time
import unicodedata
import urllib.parse
import urllib.request

ICI = pathlib.Path(__file__).resolve().parent
POLICES = ICI.parent / "v8b" / "assets" / "fonts"
NB, NNB = " ", " "  # espace insécable, espace fine insécable

METIERS = {  # libellé, mot tapé dans Google Maps, mots pour la Bibliothèque publicitaire Meta
    "couverture": ("Couverture et zinguerie", "couvreur", ["couvreur", "toiture"]),
    "facade": ("Façade et ravalement", "ravalement façade", ["ravalement", "façade"]),
    "menuiserie": ("Menuiserie extérieure", "menuiserie fenêtre", ["fenêtres", "menuiserie"]),
    "charpente": ("Charpente", "charpentier", ["charpente", "charpentier"]),
    "isolation": ("Isolation", "isolation maison", ["isolation", "isolation extérieure"]),
}

# Hypothèses : les mêmes que la section Tarifs de bartierandco.com (arrondis au plus proche à chaque étape).
COUT_DEMANDE = (20, 45)       # € de publicité par demande reçue
QUALIFIEES = (0.25, 0.40)     # part des demandes qui deviennent une visite fixée
HONOREES = 0.75               # 3 visites sur 4 honorées
SIGNEES = 1 / 3               # environ un chantier signé pour 3 visites
BUDGETS = (1000, 2000, 3000)

MOIS = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre", "décembre"]


# ——— Outils ———
def get_json(url, data=None, headers=None, essais=3):
    for i in range(essais):
        try:
            req = urllib.request.Request(url, data=json.dumps(data).encode() if data is not None else None,
                                         headers={"Content-Type": "application/json", **(headers or {})})
            with urllib.request.urlopen(req, timeout=30) as r:
                return json.load(r)
        except Exception as e:  # réseau capricieux : on réessaie
            err = e
            time.sleep(2 * (i + 1))
    raise SystemExit(f"Impossible de joindre {url.split('?')[0]} : {err}")


def nombre(n):
    return f"{round(n):,}".replace(",", NNB)


def euros(n):
    return nombre(n) + NB + "€"


def date_fr(iso):
    d = datetime.date.fromisoformat(iso)
    return f"{d.day}{'er' if d.day == 1 else ''} {MOIS[d.month - 1]} {d.year}"


def fr(t):
    """Typographie française : espace insécable avant : ; ? ! et dans les guillemets."""
    t = re.sub(r" ([:;?!])", NB + r"\1", t)
    return t.replace("« ", "«" + NB).replace(" »", NB + "»")


def e(t):
    return fr(html.escape(str(t), quote=False))


def simple(t):
    t = unicodedata.normalize("NFKD", t.lower())
    return re.sub(r"[^a-z0-9]+", " ", "".join(c for c in t if not unicodedata.combining(c))).strip()


def court(nom, n=46):
    if len(nom) <= n:
        return nom
    return nom[:n].rsplit(" ", 1)[0].rstrip(" -,·|") + "…"


# ——— Données publiques ———
def commune(fiche):
    if fiche.get("insee") and fiche.get("commune") and fiche.get("departement"):
        return
    cp = fiche["code_postal"]
    rows = get_json(f"https://geo.api.gouv.fr/communes?codePostal={cp}&fields=nom,code,codeDepartement,population")
    if not rows:
        raise SystemExit(f"Code postal inconnu : {cp}")
    c = max(rows, key=lambda r: r.get("population") or 0)  # plusieurs communes : la plus peuplée, à corriger dans la fiche si besoin
    dep = get_json(f"https://geo.api.gouv.fr/departements/{c['codeDepartement']}?fields=nom")
    fiche.update(commune=c["nom"], insee=c["code"], departement=c["codeDepartement"], departement_nom=dep["nom"])


def melodi(geo, annee, **dims):
    base = dict(GEO=geo, TIME_PERIOD=annee, RP_MEASURE="DWELLINGS", OCS="DW_MAIN", NRG_SRC="_T", CARS="_T", CARPARK="_T",
                NOR="_T", L_STAY="_T", TDW="_T", TSH="_T", BUILD_END="_T")
    base.update(dims)
    d = get_json("https://api.insee.fr/melodi/data/DS_RP_LOGEMENT_PRINC?" + urllib.parse.urlencode(base))
    obs = d.get("observations") or []
    return round(obs[0]["measures"]["OBS_VALUE_NIVEAU"]["value"]) if obs else None


def parc(fiche, maj):
    if fiche.get("parc") and not maj:
        return
    annee = next(a for a in ("2024", "2023", "2022", "2021") if melodi(f"COM-{fiche['insee']}", a) is not None)
    out = {"annee": annee, "source": "https://api.insee.fr/melodi/data/DS_RP_LOGEMENT_PRINC", "releve_le": fiche["date"]}
    for cle, geo in (("commune", f"COM-{fiche['insee']}"), ("departement", f"DEP-{fiche['departement']}")):
        anciennes = [melodi(geo, annee, TDW="1", BUILD_END=p) for p in ("Y_LT1919", "Y1919T1945", "Y1946T1970", "Y1971T1990")]
        out[cle] = {"maisons": melodi(geo, annee, TDW="1"), "maisons_avant_1991": sum(x or 0 for x in anciennes),
                    "residences": melodi(geo, annee), "proprietaires": melodi(geo, annee, TSH="100")}
    fiche["parc"] = out


def avis(fiche, maj):
    if fiche.get("avis") and not maj:
        return
    requete = fiche.get("recherche_maps") or f"{METIERS[fiche['metier']][1]} {fiche['commune']}"
    masque = "places.displayName,places.rating,places.userRatingCount,places.formattedAddress,places.googleMapsUri"
    url, h = "https://places.googleapis.com/v1/places:searchText", {"X-Goog-Api-Key": os.environ.get("GOOGLE_PLACES_KEY", "x"), "X-Goog-FieldMask": masque}  # dans une session Claude, la clé est ajoutée en route
    r = get_json(url, {"textQuery": requete, "languageCode": "fr", "regionCode": "FR", "pageSize": 20}, h)
    fiches = [{"rang": i + 1, "nom": p["displayName"]["text"], "note": p.get("rating"), "avis": p.get("userRatingCount") or 0,
               "adresse": p.get("formattedAddress", ""), "lien": p.get("googleMapsUri", "")} for i, p in enumerate(r.get("places", []))]
    cible = simple(fiche.get("fiche_google") or fiche["entreprise"])
    moi = next((f for f in fiches if cible and cible in simple(f["nom"])), None)
    if not moi:  # au-delà des 20 premières : on cherche sa fiche à part
        r2 = get_json(url, {"textQuery": f"{fiche.get('fiche_google') or fiche['entreprise']} {fiche['commune']}", "languageCode": "fr",
                            "regionCode": "FR", "pageSize": 1}, h)
        p = (r2.get("places") or [None])[0]
        moi = p and {"rang": None, "nom": p["displayName"]["text"], "note": p.get("rating"), "avis": p.get("userRatingCount") or 0,
                     "adresse": p.get("formattedAddress", ""), "lien": p.get("googleMapsUri", "")}
    fiche["avis"] = {"requete": requete, "releve_le": fiche["date"], "fiches": fiches, "moi": moi}


# ——— Calculs ———
def estimation(budget, chantier):
    d = (round(budget / COUT_DEMANDE[1]), round(budget / COUT_DEMANDE[0]))
    v = (round(d[0] * QUALIFIEES[0]), round(d[1] * QUALIFIEES[1]))
    h = (round(v[0] * HONOREES), round(v[1] * HONOREES))
    s = (round(h[0] * SIGNEES), round(h[1] * SIGNEES))
    return {"budget": budget, "demandes": d, "visites": v, "honorees": h, "signes": s, "ca": (s[0] * chantier, s[1] * chantier)}


def adresses_partagees(fiches):
    par = {}
    for f in fiches:
        cle = simple(f["adresse"].split(",")[0]) if f["adresse"] else ""
        if cle:
            par.setdefault(cle, []).append(f)
    return [(v[0]["adresse"].split(",")[0], len(v)) for v in par.values() if len(v) >= 2]


# ——— Mise en page ———
CSS = """
@font-face{font-family:"Host Grotesk";font-weight:300 700;src:url(@@POL@@/host-grotesk-latin.woff2) format("woff2")}
@font-face{font-family:"Host Grotesk";font-weight:300 700;src:url(@@POL@@/host-grotesk-latin-ext.woff2) format("woff2");unicode-range:U+0100-02BA,U+1E00-1EFF,U+2020,U+20A0-20C0}
@page{size:A4;margin:0}
:root{--ink:#0A1424;--muted:#5B6475;--line:#DCE1E8;--soft:#F3F5F8;--accent:#24489A;--tint:#E4E8F2;--bar:#8A93A3;--warn:#9A5B00;--warn-bg:#FFF6E5}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:"Host Grotesk",system-ui,sans-serif;color:var(--ink);font-size:9.6pt;line-height:1.45;-webkit-print-color-adjust:exact;print-color-adjust:exact}
.page{position:relative;width:210mm;height:297mm;padding:16mm 16mm 20mm;display:flex;flex-direction:column;gap:7mm;page-break-after:always;overflow:hidden}
.page:last-child{page-break-after:auto}
.top{display:flex;justify-content:space-between;align-items:baseline;padding-bottom:3mm;border-bottom:1px solid var(--line);font-size:8.6pt;color:var(--muted)}
.top b{font-size:11pt;font-weight:600;color:var(--ink);letter-spacing:-.01em}
.foot{position:absolute;left:16mm;right:16mm;bottom:9mm;display:flex;justify-content:space-between;font-size:7.6pt;color:var(--muted)}
.kick{font-size:9pt;color:var(--muted)}
h1{font-size:23pt;line-height:1.1;font-weight:500;letter-spacing:-.02em;margin:1.5mm 0 2.5mm}
.lead{font-size:10.4pt;color:var(--muted);max-width:150mm}
section{display:flex;flex-direction:column;gap:3mm}
h2{font-size:12.4pt;font-weight:500;letter-spacing:-.01em;display:flex;gap:3mm;align-items:baseline}
h2 i{font-style:normal;font-size:9pt;color:var(--accent);font-weight:600;min-width:5mm}
.src{font-size:7.6pt;color:var(--muted)}
.src a{color:var(--muted)}
.stats{display:grid;grid-template-columns:repeat(3,1fr);gap:3mm}
.stat{background:var(--soft);border-radius:8px;padding:4mm}
.stat b{display:block;font-size:19pt;font-weight:500;letter-spacing:-.02em;line-height:1.1;font-variant-numeric:tabular-nums}
.stat span{display:block;margin-top:1.5mm;color:var(--muted);font-size:8.8pt}
.gap{border:1.5px dashed var(--warn);background:var(--warn-bg);color:var(--warn);border-radius:8px;padding:4mm;font-size:9pt}
.gap b{display:block;margin-bottom:1mm}
table{width:100%;border-collapse:collapse;font-variant-numeric:tabular-nums}
th,td{text-align:left;padding:2.2mm 2.5mm;border-bottom:1px solid var(--line);vertical-align:top}
th{font-weight:500;color:var(--muted);font-size:8.4pt}
td.n,th.n{text-align:right;white-space:nowrap}
tr.hi td{background:var(--tint)}
.ads{display:grid;grid-template-columns:repeat(3,1fr);gap:3mm}
.ad{border:1px solid var(--line);border-radius:8px;padding:3.5mm;display:flex;flex-direction:column;gap:1.5mm;font-size:8.8pt}
.ad b{font-size:9.8pt;font-weight:600}
.ad q{color:var(--ink);quotes:"«\\00a0" "\\00a0»"}
.ad a{color:inherit;text-decoration:none}
.ad span{color:var(--muted)}
.ad img{width:100%;border-radius:4px;border:1px solid var(--line);margin-top:1mm}
.none{color:var(--muted)}
.bars{display:flex;flex-direction:column;gap:2.6mm}
.row{display:grid;grid-template-columns:62mm 1fr 30mm;gap:3mm;align-items:center;font-size:8.8pt}
.row .name{white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.row .name em{font-style:normal;color:var(--muted);margin-right:1.5mm;font-variant-numeric:tabular-nums}
.track{height:3.2mm;background:var(--soft);border-radius:2px;overflow:hidden}
.track i{display:block;height:100%;background:var(--bar);border-radius:2px}
.row.me .name{font-weight:600}
.row.me .track i{background:var(--accent)}
.row .val{text-align:right;font-variant-numeric:tabular-nums;color:var(--muted)}
.row.me .val{color:var(--ink)}
.note{background:var(--soft);border-radius:8px;padding:3.5mm 4mm;font-size:8.8pt}
.next{background:var(--ink);color:#fff;border-radius:10px;padding:5mm 6mm;display:grid;grid-template-columns:1fr auto;gap:6mm;align-items:center}
.next p{font-size:10.4pt}
.next b{font-weight:600}
.next .who{font-size:9pt;text-align:right;color:#C9D0DC;line-height:1.6}
.next .who strong{color:#fff;font-weight:600}
.draft{position:absolute;top:9mm;right:16mm;font-size:8pt;font-weight:600;color:var(--warn);border:1px solid var(--warn);border-radius:4px;padding:.6mm 2mm}
"""


def page(fiche, num, corps, brouillon):
    tete = (f'<div class="top"><b>Bartier &amp; Co</b><span>Diagnostic secteur · {e(date_fr(fiche["date"]))}</span></div>')
    pied = (f'<div class="foot"><span>Bartier &amp; Co · bartierandco.com · Diagnostic préparé pour {e(fiche["entreprise"])}</span>'
            f'<span>{num} / 2</span></div>')
    marque = '<div class="draft">Brouillon</div>' if brouillon else ""
    return f'<div class="page">{marque}{tete}{corps}{pied}</div>'


def construire(fiche):
    libelle, _, _ = METIERS[fiche["metier"]]
    ville, dep = fiche["commune"], fiche["departement_nom"]
    pc, pd = fiche["parc"]["commune"], fiche["parc"]["departement"]
    rg = fiche.get("recherches_google") or {}
    brouillon = not rg.get("total_mois")
    chantier = fiche["chantier_moyen"]
    chantier_txt = (f"votre chantier moyen de {euros(chantier)}" if fiche.get("chantier_moyen_source") == "déclaré"
                    else f"un chantier moyen de {euros(chantier)} (valeur par défaut, à remplacer par le vôtre)")

    # 1. Les maisons
    part = round(100 * pc["maisons_avant_1991"] / pc["maisons"]) if pc["maisons"] else 0
    s1 = f"""<section><h2><i>1</i>Les maisons autour de votre dépôt</h2>
<div class="stats">
<div class="stat"><b>{nombre(pc['maisons'])}</b><span>maisons habitées à l’année à {e(ville)}</span></div>
<div class="stat"><b>{part}{NB}%</b><span>de ces maisons construites avant 1991 : toitures, façades et menuiseries ont plus de 30 ans</span></div>
<div class="stat"><b>{nombre(pd['maisons'])}</b><span>maisons habitées à l’année dans le département ({e(dep)})</span></div>
</div>
<p class="src">Source : Insee, recensement de la population {fiche['parc']['annee']}, résidences principales (relevé le {e(date_fr(fiche['parc']['releve_le']))}).</p></section>"""

    # 2. Les recherches Google
    if brouillon:
        s2_corps = ('<div class="gap"><b>À relever avant l’envoi</b>Planificateur de mots clés de Google Ads, zone : '
                    f'{e(ville)} et {fiche.get("rayon_km", 30)}{NB}km autour. Reporter le total mensuel et les 5 recherches principales '
                    'dans la fiche (recherches_google).</div>')
    else:
        lignes = "".join(f"<tr><td>{e(k)}</td><td class=\"n\">{nombre(v)}</td></tr>" for k, v in rg.get("mots_cles", [])[:6])
        s2_corps = (f'<div class="stats" style="grid-template-columns:1fr 2fr"><div class="stat"><b>{nombre(rg["total_mois"])}</b>'
                    f'<span>recherches par mois liées à votre métier, autour de {e(ville)}</span></div>'
                    f'<table><thead><tr><th>Ce que les gens tapent</th><th class="n">Par mois</th></tr></thead><tbody>{lignes}</tbody></table></div>'
                    f'<p class="src">Source : Planificateur de mots clés Google Ads, {e(rg.get("zone", ""))}, moyenne mensuelle sur 12 mois '
                    f'(relevé le {e(date_fr(rg["releve_le"]))}).</p>')
    s2 = f'<section><h2><i>2</i>Ce que les propriétaires cherchent sur Google</h2>{s2_corps}</section>'

    # 3. Les concurrents qui font de la publicité
    pubs = fiche.get("pubs") or []
    if pubs:
        cartes = ""
        for p in pubs[:3]:
            img = f'<img src="{(ICI / "captures" / p["capture"]).as_uri()}" alt="">' if p.get("capture") else ""
            cartes += (f'<div class="ad"><b><a href="{html.escape(p.get("lien", ""))}">{e(p["page"])}</a></b><q>{e(court(p["titre"], 90))}</q>'
                       f'<span>En ligne depuis le {e(date_fr(p["depuis"]))}</span>{img}</div>')
        s3_corps = f'<div class="ads">{cartes}</div>'
        if len(pubs) > 3:
            s3_corps += f'<p class="src">Et {len(pubs) - 3} autre(s) annonceur(s) sur les mêmes recherches.</p>'
    else:
        s3_corps = f'<p class="none">Aucune annonce active trouvée pour votre métier à {e(ville)} : le terrain est libre sur Facebook et Instagram.</p>'
    mots = " et ".join(f"« {m} »" for m in fiche.get("pubs_recherche", []))
    s3 = (f'<section><h2><i>3</i>Qui fait déjà de la publicité près de chez vous</h2>{s3_corps}'
          f'<p class="src">Source : Bibliothèque publicitaire Meta (Facebook et Instagram), annonces actives en France pour {e(mots)}, '
          f'relevé le {e(date_fr(fiche.get("pubs_releve_le", fiche["date"])))}.</p></section>')

    # 4. Votre fiche Google face aux 3 premières
    av = fiche["avis"]
    top3, moi = av["fiches"][:3], av.get("moi")
    rangs = top3 + ([moi] if moi and moi not in top3 else [])
    mx = max([f["avis"] for f in rangs] + [1])
    barres = ""
    for f in rangs:
        est_moi = moi is not None and f == moi
        note = f'{str(f["note"]).replace(".", ",")}/5' if f.get("note") else "sans note"
        rang = f"{f['rang']}." if f.get("rang") else "—"
        barres += (f'<div class="row{" me" if est_moi else ""}"><span class="name"><em>{rang}</em>{e(court(f["nom"]))}'
                   f'{" (vous)" if est_moi else ""}</span><span class="track"><i style="width:{max(2, 100 * f["avis"] / mx):.1f}%"></i></span>'
                   f'<span class="val">{nombre(f["avis"])} avis · {note}</span></div>')
    if not moi:
        constat = "Nous n’avons pas trouvé votre fiche Google : c’est la première chose à régler, avant toute publicité."
    elif moi.get("rang") and moi["rang"] <= 3:
        constat = f"Vous êtes {moi['rang']}e sur « {av['requete']} ». La publicité sert alors à aller chercher ceux qui ne passent pas par Google Maps."
    else:
        place = f"{moi['rang']}e" if moi.get("rang") else "au-delà de la 20e place"
        devant = [f["rang"] for f in top3 if f["avis"] < moi["avis"]]
        if devant:
            qui = " et la ".join(f"{r}e" for r in devant)
            constat = (f"Vous apparaissez {place} sur « {av['requete']} », alors que vous avez plus d’avis que la {qui} fiche. "
                       "Google classe les fiches selon leur pertinence, la distance et la notoriété : le nombre d’avis ne suffit pas, "
                       "la fiche elle-même compte (catégories, services, photos, réponses aux avis).")
        else:
            ecart = top3[0]["avis"] - moi["avis"] if top3 else 0
            constat = (f"Vous apparaissez {place} sur « {av['requete']} ». Les propriétaires appellent surtout les premières fiches"
                       + (f" : la première compte {nombre(ecart)} avis de plus que vous." if ecart > 0 else "."))
    partagees = adresses_partagees(av["fiches"])
    if sum(n for _, n in partagees) >= 4:
        detail = ", ".join(f"{n} au {a}" for a, n in sorted(partagees, key=lambda x: -x[1]))
        constat += f" À savoir : sur les {len(av['fiches'])} premières fiches, {sum(n for _, n in partagees)} déclarent la même adresse qu’une autre ({detail})."
    s4 = (f'<section><h2><i>4</i>Votre fiche Google face aux 3 premières</h2><div class="bars">{barres}</div>'
          f'<p class="note">{e(constat)}</p>'
          f'<p class="src">Source : Google, classement des fiches pour « {e(av["requete"])} », note et nombre d’avis relevés le {e(date_fr(av["releve_le"]))}.</p></section>')

    # 5. Ce qu'un budget peut donner
    lignes = ""
    for b in BUDGETS:
        x = estimation(b, chantier)
        a_b = lambda t, u="": f"{nombre(t[0])} à {nombre(t[1])}{u}"
        lignes += (f'<tr{" class=hi" if b == 2000 else ""}><td>{euros(b)}</td><td class="n">{a_b(x["demandes"])}</td>'
                   f'<td class="n">{a_b(x["visites"])}</td><td class="n">{a_b(x["signes"])}</td>'
                   f'<td class="n">{nombre(x["ca"][0])} à {euros(x["ca"][1])}</td></tr>')
    s5 = f"""<section><h2><i>5</i>Ce qu’un budget publicitaire peut vous apporter chaque mois</h2>
<table><thead><tr><th>Publicité par mois</th><th class="n">Demandes</th><th class="n">Visites fixées</th><th class="n">Chantiers signés</th><th class="n">Chiffre d’affaires</th></tr></thead><tbody>{lignes}</tbody></table>
<p class="note">{e(f"Des estimations, pas des promesses. Elles reposent sur {COUT_DEMANDE[0]} à {COUT_DEMANDE[1]} € de publicité par demande, {round(QUALIFIEES[0]*100)} à {round(QUALIFIEES[1]*100)} % de demandes qui deviennent une visite, 3 visites sur 4 honorées, environ un chantier signé pour 3 visites, et {chantier_txt}. Le budget est payé directement à Meta ou à Google, sur des comptes à votre nom.")}</p></section>"""

    suite = (f'<div class="next"><p><b>La suite :</b> Martin vous appelle pour parcourir ce diagnostic avec vous, en 20{NB}minutes. '
             f'Ce qu’il faut viser dans votre secteur, le budget qui a du sens, et si votre secteur est encore libre.</p>'
             f'<p class="who"><strong>Martin Barthélémy</strong><br>07{NB}81{NB}01{NB}89{NB}36<br>contact@bartierandco.com</p></div>')

    intro = (f'<div><p class="kick">Diagnostic préparé pour {e(fiche["entreprise"])} · dépôt {e(fiche["code_postal"])} {e(ville)}</p>'
             f'<h1>{e(libelle)} autour de {e(ville)}</h1>'
             f'<p class="lead">{e("Combien de propriétaires vous entourent, ce qu’ils cherchent, qui fait déjà de la publicité, où vous en êtes sur Google, et ce qu’un budget peut vous rapporter. Chaque chiffre a sa source.")}</p></div>')
    p1 = page(fiche, 1, fr(intro + s1 + s2 + s3), brouillon)
    p2 = page(fiche, 2, fr(s4 + s5 + suite), brouillon)
    css = CSS.replace("@@POL@@", POLICES.as_uri())
    titre = f"Diagnostic secteur, {fiche['entreprise']}"
    return f'<!doctype html><html lang="fr"><head><meta charset="utf-8"><title>{e(titre)}</title><style>{css}</style></head><body>{p1}{p2}</body></html>', brouillon


def main():
    if len(sys.argv) < 2:
        raise SystemExit(__doc__)
    chemin = pathlib.Path(sys.argv[1])
    maj = "--maj" in sys.argv
    fiche = json.loads(chemin.read_text(encoding="utf-8"))
    if fiche.get("metier") not in METIERS:
        raise SystemExit("metier : " + ", ".join(METIERS))
    fiche.setdefault("date", datetime.date.today().isoformat())
    if maj:
        fiche["date"] = datetime.date.today().isoformat()
    fiche.setdefault("chantier_moyen", 5000)
    fiche.setdefault("pubs_recherche", [f"{m} {fiche.get('commune', '')}".strip() for m in METIERS[fiche["metier"]][2]])
    commune(fiche)
    parc(fiche, maj)
    avis(fiche, maj)
    chemin.write_text(json.dumps(fiche, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")  # les relevés restent dans la fiche

    doc, brouillon = construire(fiche)
    sortie = ICI / "sortie"
    sortie.mkdir(exist_ok=True)
    nom = f"Diagnostic secteur - {fiche['entreprise']}"
    src = sortie / f".{chemin.stem}.html"
    src.write_text(doc, encoding="utf-8")
    pdf = sortie / f"{nom}.pdf"
    subprocess.run(["node", str(ICI / "render.js"), str(src), str(pdf)], check=True, cwd=ICI)
    print("PDF :", pdf)
    if brouillon:
        print("Brouillon : relevez les recherches Google (recherches_google) avant de l'envoyer.")
    if fiche.get("chantier_moyen_source") != "déclaré":
        print(f"Chantier moyen par défaut ({fiche['chantier_moyen']} €) : remplacez-le par celui de l'artisan et mettez chantier_moyen_source à « déclaré ».")


if __name__ == "__main__":
    main()

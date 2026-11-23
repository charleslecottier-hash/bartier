"""Le Bâtimètre, l'observatoire Bartier & Co : index BT de l'Insee, pages par index, calculateur de révision de prix.

Données : _build/indices_bt.json (mis à jour par _build/indices_bt.py). Aucune donnée inventée :
chaque valeur vient de l'Insee, chaque règle citée a sa source.
"""
import html
import json
import math
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
D = json.loads((ROOT / "_build" / "indices_bt.json").read_text(encoding="utf-8"))
# Intitulés de l'Insee, sans les tirets ni les majuscules de la base de données
NOMS = {"BT45": "Vitrerie, miroiterie", "BT50": "Rénovation et entretien, tous corps d’état",
        "BT55": "Isolation thermique par l’extérieur, enduit sur isolant"}
for _x in D["index"]:
    _x["nom"] = NOMS.get(_x["code"], _x["nom"]).replace("'", "’")
IDX = {x["code"]: x for x in D["index"]}
BASE = "/chiffres-du-batiment/"
LIST = BASE + "indices-bt/"
CALC = BASE + "revision-de-prix/"
INSEE_SRC = ("Insee, index du bâtiment base 2010", "https://www.insee.fr/fr/metadonnees/source/indicateur/p1623/description")
CCH = ("Code de la construction et de l’habitation, art. L231-11", "https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000006896217")

MOIS = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre", "décembre"]
NB, NN = " ", " "


def mois(p):
    y, m = p.split("-")
    return f"{MOIS[int(m) - 1]} {y}"


MOIS_C = ["janv.", "févr.", "mars", "avr.", "mai", "juin", "juil.", "août", "sept.", "oct.", "nov.", "déc."]


def mois_court(p):
    y, m = p.split("-")
    return f"{MOIS_C[int(m) - 1]} {y}"


def num(v, d=1):
    return f"{v:,.{d}f}".replace(",", NN).replace(".", ",")


def pct(x):
    s = num(abs(x) * 100, 1)
    return ("+" if x > 0 else "−" if x < 0 else "") + s + NN + "%"


def date_fr(iso):
    y, m, d = iso.split("-")
    return f"{int(d)} {MOIS[int(m) - 1]} {y}"


def slug(code):
    return code.lower()


def path(code):
    return f"{LIST}{slug(code)}/"


def last(x):
    return x["valeurs"][-1]


def var(x, n):
    v = x["valeurs"]
    return (v[-1][1] / v[-1 - n][1] - 1) if len(v) > n else None


ACTIVE = [x for x in D["index"] if not x["arretee"]]
N_ACT = len(ACTIVE)
LAST_P = max(last(x)[0] for x in ACTIVE)
MAJ = max(x["maj"] for x in D["index"])

# Familles, pour lire 38 index d'un coup d'œil
FAMILLES = [
    ("Tous corps d’état et rénovation", ["BT01", "BT50"]),
    ("Couverture, charpente et étanchéité", ["BT16b", "BT30", "BT32", "BT33", "BT34", "BT35", "BT49", "BT53"]),
    ("Façade et isolation", ["BT52", "BT55", "BT46"]),
    ("Menuiseries et fermetures", ["BT19b", "BT18a", "BT26", "BT51", "BT27", "BT43", "BT28", "BT42", "BT45"]),
    ("Gros œuvre et structure", ["BT02", "BT03", "BT06", "BT07", "BT54", "BT08"]),
    ("Revêtements", ["BT09", "BT10", "BT11", "BT12", "BT14"]),
    ("Équipements techniques", ["BT38", "BT40", "BT41", "BT47", "BT48"]),
]
FAM_OF = {c: f for f, cs in FAMILLES for c in cs}
assert set(FAM_OF) == set(IDX), set(IDX) ^ set(FAM_OF)

# Quel index pour quels travaux : correspondance avec les intitulés officiels de l'Insee
TRAVAUX = [
    ("Toiture en tuiles de terre cuite", "BT32"), ("Toiture en tuiles béton", "BT33"), ("Toiture en ardoise", "BT30"),
    ("Toiture et bardage en zinc ou en métal", "BT34"), ("Toiture en bac acier", "BT49"), ("Charpente en bois", "BT16b"),
    ("Ravalement, imperméabilité de façade", "BT52"), ("Isolation par l’extérieur sous enduit", "BT55"), ("Peinture de façade", "BT46"),
    ("Fenêtres PVC", "BT26"), ("Fenêtres aluminium", "BT27"), ("Fenêtres en bois", "BT19b"), ("Étanchéité de toiture-terrasse", "BT53"),
    ("Rénovation et entretien, tous corps d’état", "BT50"), ("Construction neuve, tous corps d’état", "BT01"),
]
USAGE = {c: [t for t, k in TRAVAUX if k == c] for c in IDX}


def de(s):
    """« de » ou « d’ » devant un intitulé en minuscules."""
    s = s[0].lower() + s[1:]
    return ("d’" if s[0] in "aeiouyéèêàâîôûh" else "de ") + s


def label(code):
    return f"{code} · {IDX[code]['nom']}"


# ——— Courbe SVG (une série, une couleur, survol par JS) ———
def chart(code, since=None):
    """Courbe d'une série : tracé SVG étiré à la largeur, étiquettes en HTML pour rester lisibles sur téléphone."""
    x = IDX[code]
    pts = [(p, v) for p, v in x["valeurs"] if not since or p >= since]
    vs = [v for _, v in pts]
    lo, hi = min(vs), max(vs)
    step = 5 if hi - lo > 12 else 2 if hi - lo > 5 else 1
    y0, y1 = math.floor(lo / step) * step, math.ceil(hi / step) * step
    if y1 == y0:
        y1 = y0 + step
    n = len(pts)
    X = lambda i: 100 * (i / (n - 1) if n > 1 else 0.5)  # en % de la largeur du tracé
    Y = lambda v: 100 * (1 - (v - y0) / (y1 - y0))  # en % de la hauteur
    grid = "".join(f'<line x1="0" x2="1000" y1="{Y(g):.2f}" y2="{Y(g):.2f}" class="ob-g"/>' for g in range(int(y0), int(y1) + 1, step))
    ylab = "".join(f'<span class="ob-yl" style="top:{Y(g):.2f}%">{num(g, 0)}</span>' for g in range(int(y0), int(y1) + 1, step))
    if n > 14:
        years = [(i, p[:4]) for i, (p, _) in enumerate(pts) if p.endswith("-01")]
        cls = lambda k: (" o2" if k % 2 else "") + (" o3" if k % 3 else "")
    else:  # série courte : un repère par trimestre
        years = [(i, mois_court(p) if i == 0 else mois_court(p).split(" ")[0]) for i, (p, _) in enumerate(pts) if int(p[5:]) % 3 == 1]
        cls = lambda k: ""
    xlab = "".join(f'<span class="ob-xl{cls(k)}" style="left:{X(i):.2f}%">{y}</span>' for k, (i, y) in enumerate(years))
    d = "M" + " L".join(f"{X(i) * 10:.1f},{Y(v):.2f}" for i, (_, v) in enumerate(pts))
    data = json.dumps([[p, v] for p, v in pts], separators=(",", ":"))
    summary = (f"Courbe de l’index {code}, {x['nom'][0].lower() + x['nom'][1:]}, de {mois(pts[0][0])} à {mois(pts[-1][0])} : "
               f"de {num(pts[0][1])} à {num(pts[-1][1])}, plus bas {num(lo)}, plus haut {num(hi)}.")
    ex, ey = X(n - 1), Y(pts[-1][1])
    return (f'<figure class="ob-chart" data-pts="{html.escape(data)}" data-y0="{y0}" data-y1="{y1}"><div class="ob-plot">'
            f'<svg viewBox="0 0 1000 100" preserveAspectRatio="none" role="img" aria-label="{html.escape(summary)}">{grid}<path d="{d}" class="ob-line"/></svg>'
            f'<div aria-hidden="true">{ylab}{xlab}<i class="ob-end" style="left:{ex:.2f}%;top:{ey:.2f}%"></i>'
            f'<span class="ob-endl" style="top:{ey:.2f}%">{num(pts[-1][1])}</span><i class="ob-x" hidden></i><i class="ob-dot" hidden></i></div>'
            f'<div class="ob-tip" hidden></div></div></figure>')


def tiles(items):
    return '<ul class="ob-tiles">' + "".join(f'<li><p class="ob-tk">{k}</p><p class="ob-tv">{v}</p><p class="ob-ts">{s}</p></li>' for k, v, s in items) + "</ul>"


def ext(label_, url):
    return f'<a class="link" href="{url}" target="_blank" rel="noopener">{label_}</a>'


def table_family(codes, caption):
    rows = []
    for c in codes:
        x = IDX[c]
        p, v = last(x)
        v1, v12 = var(x, 1), var(x, 12)
        stop = ' <span class="ob-stop">série arrêtée</span>' if x["arretee"] else ""
        rows.append(f'<tr><th scope="row"><a class="link" href="{path(c)}">{c}</a></th><td class="ob-name">{x["nom"]}{stop}</td><td class="ob-n" data-label="{mois_court(p)}">{num(v)}<span class="ob-m"> {mois_court(p)}</span></td>'
                    f'<td class="ob-n" data-label="Sur 1 mois">{pct(v1) if v1 is not None else "–"}</td><td class="ob-n" data-label="Sur 1 an">{pct(v12) if v12 is not None else "–"}</td></tr>')
    return (f'<div class="ob-tw"><table class="ob-tab ob-tab-c"><caption>{caption}</caption><thead><tr><th scope="col">Index</th><th scope="col">Travaux</th>'
            f'<th scope="col">Dernière valeur</th><th scope="col">Sur 1 mois</th><th scope="col">Sur 1 an</th></tr></thead><tbody>{"".join(rows)}</tbody></table></div>')


def hero(crumb, kick, h1, lead, actions, aside=""):
    return f"""<section class="sheet pg-top ob-top" data-tone="light">
  <div class="grid pg-grid">
    <div class="pg-text">
      {crumb}
      <p class="kick">{kick}</p>
      <h1>{h1}</h1>
      <p class="lead">{lead}</p>
      <div class="actions">{actions}</div>
    </div>
    {aside}
  </div>
</section>"""


def chg(x, n):
    d = var(x, n)
    return pct(d) if d is not None else "–"


def panel_index(code):
    """Encadré du héros : la valeur du mois, lisible sans défiler."""
    x = IDX[code]
    p, v = last(x)
    first_p, first_v = x["valeurs"][0]
    since = (("depuis 2010", pct(v / 100 - 1)) if first_p < "2020" else (f"depuis {mois_court(first_p)}", pct(v / first_v - 1)))
    rows = [("sur 1 mois", chg(x, 1))] + ([("sur 1 an", chg(x, 12))] if var(x, 12) is not None else []) + [since]
    state = f"Série arrêtée par l’Insee après {mois(p)}" if x["arretee"] else f"Publié par l’Insee le {date_fr(x['maj'])}"
    return (f'<aside class="ob-aside" aria-label="Dernière valeur de l’index {code}"><div class="ob-panel">'
            f'<p class="ob-ph"><span>Index {code}</span><span>{mois(p)}</span></p>'
            f'<p class="ob-big">{num(v)}</p>'
            f'<dl class="ob-chg">' + "".join(f"<div><dt>{k}</dt><dd>{val}</dd></div>" for k, val in rows) + "</dl>"
            f'<p class="ob-live">{state} · base 100 en 2010</p></div></aside>')


BOARD = [("BT01", "Tous corps d’état"), ("BT50", "Rénovation et entretien"), ("BT32", "Couverture en tuiles de terre cuite"),
         ("BT16b", "Charpente bois"), ("BT52", "Imperméabilité de façades"), ("BT26", "Fenêtres et baies en PVC")]


def board():
    """Tableau d'affichage du héros de l'observatoire : six index très suivis, valeur et évolution sur un an."""
    rows = "".join(f'<li><a href="{path(c)}"><span class="ob-bn"><span class="ob-bc">{c}</span><span class="ob-bl">{t}</span></span>'
                   f'<span class="ob-bv">{num(last(IDX[c])[1])}</span><span class="ob-by">{chg(IDX[c], 12)}</span></a></li>' for c, t in BOARD)
    return (f'<aside class="ob-aside" aria-label="Index BT de {mois(LAST_P)}"><div class="ob-panel">'
            f'<p class="ob-ph"><span>Index BT de {mois(LAST_P)}</span><span>sur 1 an</span></p>'
            f'<ol class="ob-board">{rows}</ol>'
            f'<p class="ob-live">Publié par l’Insee le {date_fr(MAJ)} · base 100 en 2010</p></div></aside>')


def formula_panel():
    return ('<aside class="ob-aside" aria-label="La formule de révision"><div class="ob-panel">'
            '<p class="ob-ph"><span>La formule de révision</span></p>'
            '<p class="ob-fbig">P = P<sub>0</sub> × (a + (1 − a) × I<sub>n</sub> / I<sub>0</sub>)</p>'
            '<dl class="ob-legend"><div><dt>P<sub>0</sub></dt><dd>le prix initial, hors taxes</dd></div><div><dt>I<sub>0</sub></dt><dd>l’index du mois de référence</dd></div>'
            '<div><dt>I<sub>n</sub></dt><dd>l’index du mois de révision</dd></div><div><dt>a</dt><dd>la partie fixe, si le contrat en prévoit une</dd></div></dl>'
            f'<p class="ob-live">Index Insee à jour de {mois(LAST_P)}</p></div></aside>')


def btn(label_, href, tick):
    return f'<a class="btn" href="{href}"><span>{label_}</span>{tick}</a>'


def section(title, intro, inner, tone="light", sid=""):
    sid = f' id="{sid}"' if sid else ""
    intro = f"<p>{intro}</p>" if intro else ""
    return f"""<section class="sheet ob-sec"{sid} data-tone="{tone}">
  <div class="grid sp-head"><h2 data-split>{title}</h2>{intro}</div>
  <div class="ob-in">{inner}</div>
</section>"""


SRC_LINE = (f'<p class="ob-src">Source&nbsp;: {ext("Insee, index du bâtiment (base 2010)", INSEE_SRC[1])}, données mises à jour le {date_fr(MAJ)}. '
            f'Les données sont en accès libre&nbsp;: <a class="link" href="/assets/data/indices-bt.csv" download>CSV</a>, '
            f'<a class="link" href="/assets/data/indices-bt.json" download>JSON</a>.</p>')

FAQ_GEN = [
    ("Qu’est-ce qu’un index BT ?", "Un index publié chaque mois par l’Insee, qui mesure l’évolution du coût des travaux de bâtiment, corps d’état par corps d’état. Les index BT servent à réviser ou actualiser le prix d’un marché ou d’un devis, quand le contrat le prévoit."),
    ("Que veut dire « base 2010 » ?", "La moyenne de l’année 2010 vaut 100. Un index à 139,1 indique un coût supérieur de 39,1 % à celui de 2010."),
    ("Quel index BT pour un contrat de construction de maison individuelle ?", f"Le BT01, tous corps d’état : si le contrat prévoit une révision du prix, elle ne peut être calculée qu’avec cet index ({CCH[0]})."),
    ("Comment réviser un prix avec un index BT ?", "Avec la formule de votre contrat, en général P = P0 × (a + (1 − a) × In / I0) : P0 le prix initial, I0 l’index du mois de référence, In celui du mois de révision et a la partie fixe éventuelle. Notre calculateur fait le calcul."),
    ("Révision ou actualisation : quelle différence ?", "La révision fait suivre l’index au prix pendant l’exécution des travaux, selon la formule du contrat. L’actualisation ajuste une seule fois un prix ferme quand les travaux démarrent longtemps après la date du prix."),
]


def faq_html(items, title, phone, phone_txt):
    rows = "\n".join(f'      <details class="fq"><summary><span>{q}</span><i class="fq-icon" aria-hidden="true"></i></summary><div class="fq-a"><p>{a}</p></div></details>' for q, a in items)
    return f"""<section class="faq sheet" id="questions" data-kind="faq" data-tone="paper">
  <div class="grid fq-grid">
    <div class="fq-head"><h2 data-split>{title}</h2><p>Une autre question&nbsp;? <a class="link" href="tel:{phone}">{phone_txt}</a></p></div>
    <div class="fq-list">
{rows}
    </div>
  </div>
</section>"""


def links_band(title, links):
    items = "".join(f'<li><a class="link" href="{h}">{t}</a></li>' for t, h in links)
    return f"""<section class="sheet more" data-tone="light">
  <div class="grid sp-split">
    <div><h2 data-split>{title}</h2></div>
    <ul class="more-list">{items}</ul>
  </div>
</section>"""


# ——— Pages ———
def page_hub(crumbs, tick, phone, phone_txt):
    bt01 = IDX["BT01"]
    p, v = last(bt01)
    act = [x for x in ACTIVE if var(x, 12) is not None]
    up = max(act, key=lambda x: var(x, 12))
    down = min(act, key=lambda x: var(x, 12))
    n_up = sum(1 for x in act if var(x, 12) > 0)
    t = tiles([("BT01 sur un an", pct(var(bt01, 12)), f"tous corps d’état, {mois(p)} par rapport à {mois(bt01['valeurs'][-13][0])}"),
               ("Index en hausse sur un an", f"{n_up} sur {len(act)}", "index publiés depuis plus d’un an"),
               ("Plus forte hausse", pct(var(up, 12)), f"{up['code']}, {up['nom'][0].lower() + up['nom'][1:]}"),
               ("Plus faible hausse" if var(down, 12) > 0 else "Plus faible évolution", pct(var(down, 12)), f"{down['code']}, {down['nom'][0].lower() + down['nom'][1:]}")])
    h = hero(crumbs, "Observatoire Bartier &amp; Co", "Le Bâtimètre",
             f"Les {N_ACT} index BT publiés chaque mois par l’Insee, un calculateur de révision de prix et les données en accès libre. Dernier mois publié&nbsp;: {mois(LAST_P)}.",
             btn("Réviser un prix", CALC, tick) + f'<a class="link" href="{LIST}">Tous les index BT</a>', board())
    trows = "".join(f'<tr><th scope="row" class="ob-name">{t_}</th><td class="ob-code"><a class="link" href="{path(c)}">{c}</a></td><td class="ob-n" data-label="Valeur">{num(last(IDX[c])[1])}</td>'
                    f'<td class="ob-n" data-label="Sur 1 mois">{chg(IDX[c], 1)}</td><td class="ob-n" data-label="Sur 1 an">{chg(IDX[c], 12)}</td></tr>' for t_, c in TRAVAUX)
    trade = (f'<div class="ob-tw"><table class="ob-tab ob-tab-c ob-tab-t"><caption>Index BT par type de travaux, valeurs de {mois(LAST_P)}</caption><thead><tr><th scope="col">Travaux</th>'
             f'<th scope="col">Index</th><th scope="col">Valeur</th><th scope="col">Sur 1 mois</th><th scope="col">Sur 1 an</th></tr></thead><tbody>{trows}</tbody></table></div>')
    body = [h,
            section(f"Le bâtiment en {mois(LAST_P)}", "Le coût des travaux par rapport au même mois de l’année précédente, d’après les index de l’Insee", t + SRC_LINE, "light", "chiffres"),
            section("L’index BT01 depuis 2014", "Tous corps d’état, base 100 en 2010. Survolez ou touchez la courbe pour lire chaque mois", chart("BT01"), "paper", "bt01"),
            section("Quel index pour quels travaux&nbsp;?", "L’index le plus proche de chaque type de chantier, d’après les intitulés de l’Insee. Le bon index reste celui que fixe votre contrat",
                    trade, "light", "travaux"),
            section("Les outils", "", f"""<ul class="ob-tools">
  <li><h3><a class="link" href="{CALC}">Calculateur de révision de prix</a></h3><p>Choisissez l’index, les deux mois et le prix initial : le prix révisé et la formule détaillée, à copier dans votre facture.</p></li>
  <li><h3><a class="link" href="{LIST}">Tous les index BT</a></h3><p>Dernière valeur, évolution sur un mois et sur un an, et une page par index avec tout l’historique.</p></li>
  <li><h3><a class="link" href="/assets/data/indices-bt.csv" download>Les données en CSV</a></h3><p>Toutes les valeurs depuis octobre 2014, prêtes pour un tableur. Réutilisation libre en citant l’Insee.</p></li>
</ul>""", "paper", "outils"),
            section("Méthode", "", f"""<div class="ob-prose"><p>Les valeurs sont celles publiées par l’Insee dans sa base de données macroéconomiques (jeu « Index bâtiment, travaux publics et divers de la construction », base 2010). Nous les reprenons sans retouche, chaque mois, après la publication officielle.</p>
<p>Les variations sont calculées par nos soins&nbsp;: sur un mois, par rapport au mois précédent ; sur un an, par rapport au même mois de l’année précédente. Depuis janvier 2026, l’Insee publie un nouvel index, le BT55 (isolation thermique par l’extérieur), et a arrêté le BT12.</p>
<p>Le Bâtimètre est réalisé par <a class="link" href="/qui-sommes-nous/">Bartier &amp; Co</a>, l’agence qui trouve des clients aux artisans du bâtiment.</p></div>{SRC_LINE}""", "light", "methode"),
            faq_html(FAQ_GEN, "Index BT : vos questions", phone, phone_txt),
            links_band("Aller plus loin", [("Calculateur de révision de prix", CALC), ("Tous les index BT", LIST), ("Lexique des chantiers et des travaux", "/lexique/"), ("Trouver des chantiers", "/trouver-des-chantiers/")])]
    title = "Le Bâtimètre : index BT de l’Insee et révision de prix"
    desc = f"Le Bâtimètre : les {N_ACT} index BT de l’Insee mis à jour chaque mois ({mois(LAST_P)} : BT01 à {num(v)}), un calculateur de révision de prix et les données en accès libre."
    return title, desc, "\n\n".join(body) + OB_JS, FAQ_GEN


def page_list(crumbs, tick, phone, phone_txt):
    secs = []
    for i, (fam, codes) in enumerate(FAMILLES):
        secs.append(section(fam, "", table_family(codes, f"{fam}, {mois(LAST_P)}"), "light" if i % 2 == 0 else "paper", f"f{i + 1}"))
    bt01 = IDX["BT01"]
    h = hero(crumbs, "Le Bâtimètre", f"Indices BT&nbsp;: les valeurs de {mois(LAST_P)}",
             f"Les {N_ACT} index BT publiés chaque mois par l’Insee, base 100 en 2010, classés par famille de travaux, et le BT12, arrêté fin 2025.",
             btn("Réviser un prix", CALC, tick) + '<a class="link" href="/assets/data/indices-bt.csv" download>Télécharger les données (CSV)</a>', panel_index("BT01"))
    body = [h] + secs + [section("Source", "", SRC_LINE, "light"), faq_html(FAQ_GEN, "Index BT : vos questions", phone, phone_txt),
                         links_band("Aller plus loin", [("Calculateur de révision de prix", CALC), ("Le Bâtimètre, l’observatoire des index BT", BASE), ("Lexique", "/lexique/")])]
    title = f"Indices BT {mois(LAST_P)} : toutes les valeurs (Insee)"
    desc = f"Les {N_ACT} index BT du bâtiment de {mois(LAST_P)}, base 2010 : BT01 à {num(last(bt01)[1])}. Évolutions sur un mois et sur un an, historique et données en CSV. Source Insee."
    return title, desc, "\n\n".join(body), FAQ_GEN


def page_index(code, crumbs, tick, phone, phone_txt):
    x = IDX[code]
    p, v = last(x)
    v1, v12 = var(x, 1), var(x, 12)
    fam = FAM_OF[code]
    nom = x["nom"]
    first_p = x["valeurs"][0][0]
    stop = x["arretee"]
    lead = (f"L’index {code} de l’Insee mesure l’évolution du coût des travaux {de(nom)}. "
            + (f"Valeur de {mois(p)}&nbsp;: {num(v)}." if not stop else f"Cette série est arrêtée : dernière valeur, {num(v)} en {mois(p)}."))
    h = hero(crumbs, f"Le Bâtimètre · {fam}", f"Index {code}&nbsp;: {nom[0].lower() + nom[1:]}", lead,
             (btn(f"Réviser un prix avec le {code}", f"{CALC}?index={code}", tick) if not stop else "") + f'<a class="link" href="{LIST}">Tous les index BT</a>', panel_index(code))
    recent = list(reversed(x["valeurs"][-24:]))
    vals = dict(x["valeurs"])
    rows = "".join(f'<tr><th scope="row">{mois(pp)}</th><td class="ob-n">{num(vv)}</td><td class="ob-n">'
                   + (pct(vv / vals[f"{int(pp[:4]) - 1}{pp[4:]}"] - 1) if f"{int(pp[:4]) - 1}{pp[4:]}" in vals else "–") + "</td></tr>" for pp, vv in recent)
    tab = (f'<div class="ob-tw"><table class="ob-tab ob-tab-s"><caption>Index {code}, {len(recent)} derniers mois publiés</caption><thead><tr><th scope="col">Mois</th>'
           f'<th scope="col">Valeur</th><th scope="col">Sur 1 an</th></tr></thead><tbody>{rows}</tbody></table></div>')
    years = sorted({pp[:4] for pp, _ in x["valeurs"]})
    yrows = ""
    for y in years:
        ys = [vv for pp, vv in x["valeurs"] if pp.startswith(y)]
        if len(ys) == 12:
            yrows += f'<tr><th scope="row">{y}</th><td class="ob-n">{num(sum(ys) / 12)}</td><td class="ob-n">{num(min(ys))}</td><td class="ob-n">{num(max(ys))}</td></tr>'
    ytab = (f'<div class="ob-tw"><table class="ob-tab ob-tab-s"><caption>Moyenne annuelle de l’index {code}, années complètes</caption><thead><tr><th scope="col">Année</th>'
            f'<th scope="col">Moyenne</th><th scope="col">Plus bas</th><th scope="col">Plus haut</th></tr></thead><tbody>{yrows}</tbody></table></div>') if yrows else ""
    use = USAGE.get(code) or []
    use_html = (f"<p>D’après son intitulé, c’est l’index le plus proche pour&nbsp;: {', '.join(u[0].lower() + u[1:] for u in use)}.</p>" if use else "")
    sibs = [c for c in dict(FAMILLES)[fam] if c != code]
    formula = (f"<p>Avec la formule la plus courante, un prix P0 fixé au mois de référence devient P = P0 × (a + (1 − a) × In / I0), où I0 et In sont les valeurs de l’index {code} "
               f"aux deux mois prévus par le contrat et a la partie fixe éventuelle. Exemple sans partie fixe, entre {mois(x['valeurs'][-13][0]) if v12 is not None else mois(first_p)} et {mois(p)}&nbsp;: "
               f"10&nbsp;000&nbsp;€ deviennent {num(10000 * v / (x['valeurs'][-13][1] if v12 is not None else x['valeurs'][0][1]), 0)}&nbsp;€.</p>")
    extra = f"<p>{'Le BT01 est le seul index autorisé pour réviser le prix d’un contrat de construction de maison individuelle (' + ext(CCH[0], CCH[1]) + ').' if code == 'BT01' else ''}</p>" if code == "BT01" else ""
    body = [h,
            section(f"Courbe de l’index {code}", f"De {mois(first_p)} à {mois(p)}, base 100 en 2010. Survolez ou touchez la courbe pour lire chaque mois", chart(code) + SRC_LINE, "paper", "courbe"),
            section("Les derniers mois", "Valeurs publiées et évolution par rapport au même mois de l’année précédente", tab + ytab, "light", "valeurs"),
            section(f"À quoi sert l’index {code}&nbsp;?", "",
                    f'<div class="ob-prose"><p>Il sert à réviser ou actualiser le prix d’un marché ou d’un devis de travaux {de(nom)}, quand le contrat le prévoit.</p>{use_html}{extra}{formula}'
                    f'<p><a class="link" href="{CALC}?index={code}">Calculer une révision avec le {code}</a></p></div>', "paper", "usage"),
            faq_html([(f"Quelle est la valeur de l’index {code} en {mois(p)} ?", f"{num(v)}, en base 100 en 2010 (Insee, données mises à jour le {date_fr(x['maj'])})."
                       + (f" C’est {pct(v12)} par rapport à {mois(x['valeurs'][-13][0])}." if v12 is not None else "")),
                      (f"Quand l’Insee publie-t-il l’index {code} ?", f"Chaque mois, comme les autres index du bâtiment. La dernière mise à jour de la série date du {date_fr(x['maj'])}." if not stop
                       else f"Plus du tout : la série est arrêtée, sa dernière valeur est celle de {mois(p)}."),
                      FAQ_GEN[3], FAQ_GEN[1]], f"Index {code} : vos questions", phone, phone_txt),
            links_band("Index de la même famille", [(label(c), path(c)) for c in sibs] + [("Tous les index BT", LIST), ("Calculateur de révision de prix", CALC)])]
    title = f"Indice {code} {mois(p)} : {num(v)} (Insee)"
    desc = (f"Index {code} ({nom.lower()}) de {mois(p)} : {num(v)}" + (f", {pct(v12)} sur un an" if v12 is not None else "")
            + f". Courbe depuis {first_p[:4]}, valeurs mensuelles, moyennes annuelles et calculateur de révision. Source Insee.")
    faqs = [(f"Quelle est la valeur de l’index {code} en {mois(p)} ?", f"{num(v)}, en base 100 en 2010 (Insee).")]
    return title, desc, "\n\n".join(body) + OB_JS, faqs


def page_calc(crumbs, tick, phone, phone_txt):
    groups = "".join(f'<optgroup label="{fam}">' + "".join(f'<option value="{c}"{" selected" if c == "BT01" else ""}>{c} · {IDX[c]["nom"]}</option>' for c in codes if not IDX[c]["arretee"]) + "</optgroup>"
                     for fam, codes in FAMILLES)
    bt = IDX["BT01"]["valeurs"]
    opts = lambda sel: "".join(f'<option value="{pp}"{" selected" if pp == sel else ""}>{mois(pp)}</option>' for pp, _ in reversed(bt))
    m0, mn = bt[-13][0], bt[-1][0]
    i0, i_n = bt[-13][1], bt[-1][1]
    p0 = 10000
    res = p0 * i_n / i0
    form = f"""<form class="ob-calc" id="ob-calc" novalidate>
  <div class="ob-cin">
    <label class="ob-f"><span>Index</span><select id="ob-idx" name="index">{groups}</select></label>
    <label class="ob-f"><span>Prix initial, HT</span><span class="ob-eur"><input id="ob-p0" name="p" type="text" inputmode="decimal" value="10 000" autocomplete="off"><b>€</b></span></label>
    <div class="ob-row">
      <label class="ob-f"><span>Mois de l’index de référence (I0)</span><select id="ob-m0" name="m0">{opts(m0)}</select></label>
      <label class="ob-f"><span>Mois de l’index de révision (In)</span><select id="ob-mn" name="mn">{opts(mn)}</select></label>
    </div>
    <fieldset class="ob-f ob-fix"><legend>Partie fixe (a), selon votre contrat</legend>
      <label><input type="radio" name="a" value="0" checked><span>Aucune</span></label>
      <label><input type="radio" name="a" value="0.125"><span>12,5&nbsp;%</span></label>
      <label><input type="radio" name="a" value="0.15"><span>15&nbsp;%</span></label>
      <label class="ob-other"><input type="radio" name="a" value="autre"><span>Autre</span><input id="ob-ac" type="text" inputmode="decimal" aria-label="Partie fixe en pourcentage" placeholder="%"></label>
    </fieldset>
  </div>
  <div class="ob-cout" aria-live="polite">
    <p class="ob-tk">Prix révisé, HT</p>
    <p class="ob-res" id="ob-res">{num(res, 2)}&nbsp;€</p>
    <p class="ob-diff" id="ob-diff">{"+" if res >= p0 else "−"}{num(abs(res - p0), 2)}&nbsp;€, soit {pct(res / p0 - 1)}</p>
    <p class="ob-formula" id="ob-formula">P = 10&nbsp;000 × (0 + 1 × {num(i_n)} / {num(i0)})</p>
    <p class="ob-idxv" id="ob-idxv">BT01&nbsp;: {num(i0)} en {mois(m0)}, {num(i_n)} en {mois(mn)}</p>
    <button type="button" class="btn ob-copy" id="ob-copy"><span>Copier le calcul</span>{tick}</button>
    <p class="ob-note">Le calcul suit la formule P = P0 × (a + (1 − a) × In / I0). Vérifiez qu’elle correspond à celle de votre contrat.</p>
  </div>
</form>"""
    h = hero(crumbs, "Le Bâtimètre · outil gratuit", "Calculateur de révision de prix",
             "Révisez le prix d’un devis ou d’un marché avec l’index BT de votre choix, à partir des valeurs officielles de l’Insee. Le calcul est fait dans votre navigateur.",
             btn("Faire le calcul", "#calcul", tick) + f'<a class="link" href="{LIST}">Tous les index BT</a>', formula_panel())
    how = f"""<div class="ob-prose"><ol class="ob-steps">
<li><b>Choisissez l’index</b> prévu par votre contrat : BT01 pour un contrat de construction de maison individuelle ({ext(CCH[0], CCH[1])}), sinon l’index du corps d’état, par exemple BT32 pour une couverture en tuiles de terre cuite.</li>
<li><b>Choisissez les deux mois</b> : celui de l’index de référence, I0, et celui de l’index de révision, In, comme les fixe votre contrat.</li>
<li><b>Indiquez la partie fixe</b> si votre formule en prévoit une, par exemple 0,15 dans P = P0 × (0,15 + 0,85 × In / I0). Sans partie fixe, le prix suit entièrement l’index.</li>
<li><b>Copiez le calcul</b> : la formule avec les valeurs de l’Insee, à joindre à votre facture ou à votre situation de travaux.</li></ol></div>"""
    body = [h, section("Votre calcul", "Les valeurs de l’index s’affichent dès que vous choisissez les mois", form + SRC_LINE, "paper", "calcul"),
            section("Comment l’utiliser", "", how, "light", "mode-emploi"),
            faq_html([FAQ_GEN[3], FAQ_GEN[4], FAQ_GEN[2], ("Les valeurs sont-elles à jour ?", f"Oui : ce sont les index publiés par l’Insee, mis à jour chaque mois. Dernier mois disponible&nbsp;: {mois(LAST_P)}.")],
                     "Révision de prix : vos questions", phone, phone_txt),
            links_band("Aller plus loin", [("Tous les index BT", LIST), (label("BT01"), path("BT01")), (label("BT50"), path("BT50")), ("Le Bâtimètre, l’observatoire des index BT", BASE)])]
    title = "Révision de prix BT01 : calculateur gratuit (index BT)"
    desc = f"Calculez la révision de prix d’un devis ou d’un marché avec le BT01 ou l’un des {N_ACT} index BT de l’Insee, à jour de {mois(LAST_P)}. Formule détaillée, prête à copier."
    faqs = [FAQ_GEN[3], FAQ_GEN[4], FAQ_GEN[2]]
    return title, desc, "\n\n".join(body) + CALC_JS + OB_JS, faqs


OB_CSS = """<style id="ob-css">
.ob-top .lead{max-width:56ch}
.ob-top h1{font-size:clamp(2.3rem,4.4vw,4.4rem);text-wrap:balance}
.ob-aside{grid-column:3 / 5;align-self:center;min-width:0}
.ob-panel{--rule:color-mix(in oklab,var(--bg) 14%,transparent);--soft:color-mix(in oklab,var(--bg) 68%,var(--ink));display:grid;gap:16px;padding:clamp(22px,2.4vw,36px);background:var(--ink);color:var(--bg);border-radius:var(--r)}
.ob-ph{display:flex;justify-content:space-between;gap:12px;font-size:.88rem;color:var(--soft)}
.ob-big{margin:8px 0 4px;font:300 clamp(4.6rem,9vw,8.4rem)/.86 var(--f-display);letter-spacing:-.055em;font-variant-numeric:tabular-nums}
.ob-chg{display:grid;grid-auto-flow:column;grid-auto-columns:minmax(0,1fr);gap:12px;margin:0}
.ob-chg div{padding-top:12px;border-top:1px solid var(--rule)}
.ob-chg dt{font-size:.8rem;color:var(--soft)}
.ob-chg dd{margin:6px 0 0;font:400 1.35rem/1.1 var(--f-display);font-variant-numeric:tabular-nums}
.ob-live{display:flex;align-items:center;gap:10px;padding-top:14px;border-top:1px solid var(--rule);font-size:.8rem;line-height:1.4;color:var(--soft)}
.ob-live::before{content:"";width:7px;height:7px;border-radius:50%;background:var(--spark);flex:none}
.ob-board{margin:0;padding:0;list-style:none;border-top:1px solid var(--rule)}
.ob-board a{display:grid;grid-template-columns:minmax(0,1fr) auto 72px;align-items:baseline;gap:16px;min-height:52px;padding:14px 0;border-bottom:1px solid var(--rule);color:inherit;text-decoration:none;transition:background-color .2s}
.ob-bn{display:flex;align-items:baseline;gap:12px;min-width:0}
.ob-bc{flex:none;width:48px}
.ob-board a:hover{background:color-mix(in oklab,var(--bg) 6%,transparent)}
.ob-board a:focus-visible{outline:2px solid var(--spark);outline-offset:-2px}
.ob-bc{font-size:.85rem;color:var(--soft)}
.ob-bv,.ob-by,.ob-n,.ob-diff,.ob-formula,.ob-idxv,.ob-tv,.ob-yl,.ob-xl,.ob-endl,.ob-tip{font-family:var(--f-display)}
.ob-bl{overflow:hidden;text-overflow:ellipsis;white-space:nowrap;font-size:.92rem}
.ob-bv{font:400 1.5rem/1 var(--f-display);letter-spacing:-.02em}
.ob-by{text-align:right;font-size:.95rem;color:var(--soft);font-variant-numeric:tabular-nums}
.ob-bv{font-variant-numeric:tabular-nums}
.ob-fbig{margin:6px 0;font:300 clamp(1.7rem,2.6vw,2.4rem)/1.2 var(--f-display);letter-spacing:-.02em}
.ob-fbig sub,.ob-legend sub{font-size:.6em;vertical-align:-.25em;line-height:0}
.ob-legend{display:grid;gap:0;margin:0;border-top:1px solid var(--rule)}
.ob-legend div{display:grid;grid-template-columns:48px 1fr;gap:12px;padding:10px 0;border-bottom:1px solid var(--rule);font-size:.92rem}
.ob-legend dt{font-family:var(--f-display);font-size:1.05rem}
.ob-legend dd{margin:0;color:var(--soft)}
@media (max-width:760px){.ob-aside{grid-column:1 / -1}.ob-big{font-size:5rem}.ob-board a{grid-template-columns:minmax(0,1fr) auto 64px;gap:12px}.ob-bn{flex-direction:column;gap:2px}.ob-bc{width:auto}.ob-bl{white-space:normal}}
.ob-top .actions{display:flex;flex-wrap:wrap;align-items:center;gap:14px 24px}
.ob-in{padding:0 var(--cell)}
.ob-tiles{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:0;margin:0;padding:0;list-style:none;border-top:1px solid var(--rule)}
.ob-tiles li{padding:22px 20px 22px 0;border-right:1px solid var(--rule);margin-right:20px}
.ob-tiles li:last-child{border-right:0;margin-right:0}
.ob-tk{font-size:.85rem;color:var(--soft)}
.ob-tv{margin:10px 0 8px;font:300 clamp(2.4rem,4.2vw,3.6rem)/1 var(--f-display);letter-spacing:-.04em;font-variant-numeric:tabular-nums}
.ob-ts{font-size:.85rem;line-height:1.4;color:var(--soft)}
.ob-src{margin-top:20px;font-size:.8125rem;line-height:1.5;color:var(--soft);max-width:90ch}
.ob-chart{margin:0;padding:12px 64px 36px 44px}
.ob-plot{position:relative;height:clamp(220px,30vw,400px);touch-action:pan-y;cursor:crosshair}
.ob-plot svg{position:absolute;inset:0;width:100%;height:100%;overflow:visible}
.ob-g{stroke:var(--rule);stroke-width:1;vector-effect:non-scaling-stroke}
.ob-line{fill:none;stroke:var(--accent);stroke-width:2;stroke-linejoin:round;stroke-linecap:round;vector-effect:non-scaling-stroke}
.ob-yl,.ob-xl,.ob-endl{position:absolute;font-size:.75rem;line-height:1;color:var(--soft);font-variant-numeric:tabular-nums;white-space:nowrap}
.ob-yl{right:calc(100% + 10px);transform:translateY(-50%)}
.ob-xl{top:calc(100% + 12px);transform:translateX(-50%)}
.ob-endl{left:calc(100% + 12px);transform:translateY(-50%);font-size:.9rem;font-weight:500;color:var(--ink)}
.ob-end,.ob-dot{position:absolute;width:10px;height:10px;margin:-5px 0 0 -5px;border-radius:50%;background:var(--accent);box-shadow:0 0 0 2px var(--bg)}
.ob-x{position:absolute;top:0;bottom:0;width:0;border-left:1px dashed color-mix(in oklab,var(--ink) 45%,transparent)}
.ob-tip{position:absolute;top:0;transform:translate(-50%,calc(-100% - 12px));padding:8px 10px;border-radius:var(--r);background:var(--ink);color:var(--bg);font-size:.8rem;line-height:1.35;white-space:nowrap;pointer-events:none;font-variant-numeric:tabular-nums;z-index:2}
@media (max-width:1024px){.ob-xl.o2{display:none}}
@media (max-width:640px){.ob-chart{padding:12px 52px 32px 32px}.ob-xl.o2{display:block}.ob-xl.o3{display:none}.ob-yl{right:calc(100% + 6px)}}
.ob-tip b{display:block;font:400 1.05rem/1.1 var(--f-display)}
.ob-tw{overflow-x:auto;margin-top:8px}
.ob-tab{width:100%;border-collapse:collapse;font-size:.9rem}
.ob-tab .ob-n{font-variant-numeric:tabular-nums;font-size:.95rem}
.ob-tab caption{text-align:left;padding:0 0 10px;font-size:.8rem;color:var(--soft)}
.ob-tab th,.ob-tab td{padding:11px 12px 11px 0;text-align:left;border-bottom:1px solid var(--rule);vertical-align:baseline;font-weight:400}
.ob-tab thead th{font-size:.78rem;font-weight:500;color:var(--soft)}
.ob-tab tbody th{font-weight:500;white-space:nowrap}
.ob-tab .ob-n{text-align:right;white-space:nowrap}
.ob-tab thead th:nth-child(n+3){text-align:right}
.ob-m{color:var(--soft);font-size:.8rem}
.ob-stop{display:inline-block;margin-left:6px;font-size:.75rem;color:var(--soft)}
.ob-tab-s{max-width:560px}
.ob-tab-s+.ob-tw,.ob-tw+.ob-tw{margin-top:36px}
.ob-tools{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:28px;margin:0;padding:0;list-style:none}
.ob-tools li{padding-top:18px;border-top:1px solid var(--ink)}
.ob-tools h3{font:400 1.2rem/1.25 var(--f-display);margin:0 0 10px}
.ob-tools p{font-size:.92rem;line-height:1.5;color:var(--soft)}
.ob-prose{max-width:68ch}
.ob-prose .link,.ob-src .link,.ob-steps .link,.ob-tools .link,.ob-tab td .link{white-space:normal;display:inline;min-height:0}
.ob-cout .btn{--b:var(--bg);--f:var(--ink);--h:var(--accent);--hf:var(--bg)}
.ob-prose p{margin:0 0 1em;line-height:1.6}
.ob-steps{margin:0;padding-left:1.2em}
.ob-steps li{margin:0 0 1em;line-height:1.6}
.ob-calc{display:grid;grid-template-columns:1.1fr .9fr;background:var(--bg);border:1px solid var(--rule);border-radius:var(--r)}
.ob-cin{display:grid;gap:22px;padding:clamp(22px,3vw,40px);min-width:0}
.ob-f{display:grid;gap:8px;min-width:0;margin:0;padding:0;border:0}
.ob-f>span,.ob-f legend{font-size:.9rem;font-weight:500;padding:0}
.ob-f select,.ob-f input{width:100%;min-height:48px;padding:0 12px;border:1px solid color-mix(in oklab,var(--ink) 22%,transparent);border-radius:var(--r);background:var(--bg);color:var(--ink);font:400 1rem var(--f-text)}
.ob-f select:focus-visible,.ob-f input:focus-visible{outline:2px solid var(--accent);outline-offset:1px}
.ob-eur{position:relative;display:block}
.ob-eur input{padding-right:36px}
.ob-eur b{position:absolute;right:12px;top:50%;transform:translateY(-50%);font-weight:400;color:var(--soft)}
.ob-row{display:grid;grid-template-columns:1fr 1fr;gap:16px}
.ob-fix{display:flex;flex-wrap:wrap;gap:8px}
.ob-fix legend{margin-bottom:8px;width:100%}
.ob-fix label{position:relative;display:inline-flex;align-items:center;gap:8px;min-height:44px;padding:0 14px;border:1px solid color-mix(in oklab,var(--ink) 22%,transparent);border-radius:var(--r);cursor:pointer;font-size:.92rem}
.ob-fix label:has(input:checked){border-color:var(--ink);background:var(--ink);color:var(--bg)}
.ob-fix input[type=radio]{position:absolute;opacity:0;inset:0;margin:0;cursor:pointer}
.ob-fix label:has(input[type=radio]:focus-visible){outline:2px solid var(--accent);outline-offset:2px}
.ob-other input[type=text]{position:relative;z-index:1;width:64px;min-height:30px;padding:0 6px;border-radius:2px}
.ob-cout{display:flex;flex-direction:column;gap:10px;margin:10px;padding:clamp(20px,2.6vw,34px);background:var(--ink);color:var(--bg);border-radius:var(--r);min-width:0}
.ob-cout .ob-tk{color:color-mix(in oklab,var(--bg) 66%,var(--ink))}
.ob-res{font:300 clamp(2.6rem,4.6vw,4.2rem)/1 var(--f-display);letter-spacing:-.04em;font-variant-numeric:tabular-nums;overflow-wrap:anywhere}
.ob-diff{font-size:1rem;font-variant-numeric:tabular-nums}
.ob-formula,.ob-idxv{font-size:.88rem;line-height:1.45;color:color-mix(in oklab,var(--bg) 78%,var(--ink));font-variant-numeric:tabular-nums;overflow-wrap:anywhere}
.ob-formula{padding:12px 0;border-top:1px solid color-mix(in oklab,var(--bg) 16%,transparent);border-bottom:1px solid color-mix(in oklab,var(--bg) 16%,transparent)}
.ob-cout .btn{align-self:stretch;justify-content:center;margin-top:6px}
.ob-note{font-size:.78rem;line-height:1.45;color:color-mix(in oklab,var(--bg) 66%,var(--ink))}
.ob-res.is-bump{animation:bump .35s var(--ease)}
@media (max-width:1024px){.ob-tiles{grid-template-columns:repeat(2,minmax(0,1fr))}.ob-tiles li:nth-child(2){border-right:0;margin-right:0}.ob-tiles li:nth-child(n+3){border-top:1px solid var(--rule)}.ob-tools{grid-template-columns:1fr 1fr}}
@media (max-width:900px){.ob-calc{grid-template-columns:minmax(0,1fr)}}
@media (max-width:640px){
.ob-tab-c thead{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0)}
.ob-tab-c tr{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:10px 12px;padding:16px 0;border-bottom:1px solid var(--rule)}
.ob-tab-c th,.ob-tab-c td{display:block;padding:0;border:0;text-align:left!important;white-space:normal}
.ob-tab-c tbody th{grid-column:1}
.ob-tab-c .ob-name{grid-column:2 / 4}
.ob-tab-t .ob-name.ob-name{grid-column:1 / 3;white-space:normal;align-self:center}
.ob-tab-t .ob-code{grid-column:3;text-align:right!important}
.ob-tab-c .ob-n{font-size:1.05rem}
.ob-tab-c .ob-n::before{content:attr(data-label);display:block;margin-bottom:4px;font:400 .75rem var(--f-text);color:var(--soft)}
.ob-tab-c .ob-m{display:none}
.ob-tools,.ob-row{grid-template-columns:minmax(0,1fr)}.ob-tiles li{padding-right:12px;margin-right:12px}.ob-tv{font-size:2.2rem}.ob-tab{font-size:.85rem}.ob-cout{margin:0 8px 8px}}
@media (prefers-reduced-motion:reduce){.ob-res.is-bump{animation:none}}
</style>"""

OB_JS = r"""<script id="ob-js">
(function(){var M=["janvier","février","mars","avril","mai","juin","juillet","août","septembre","octobre","novembre","décembre"];
function mo(p){var a=p.split("-");return M[+a[1]-1]+" "+a[0]}
function nf(v){return v.toFixed(1).replace(".",",")}
[].forEach.call(document.querySelectorAll(".ob-chart"),function(fg){var pts=JSON.parse(fg.dataset.pts),y0=+fg.dataset.y0,y1=+fg.dataset.y1,pl=fg.querySelector(".ob-plot"),
  x=pl.querySelector(".ob-x"),d=pl.querySelector(".ob-dot"),tip=pl.querySelector(".ob-tip"),n=pts.length;
  function show(cx){var r=pl.getBoundingClientRect(),i=Math.round((cx-r.left)/r.width*(n-1));i=Math.max(0,Math.min(n-1,i));
    var px=n>1?i/(n-1)*100:50,py=(1-(pts[i][1]-y0)/(y1-y0))*100;x.style.left=px+"%";x.hidden=false;d.style.left=px+"%";d.style.top=py+"%";d.hidden=false;
    tip.innerHTML="<b>"+nf(pts[i][1])+"</b>"+mo(pts[i][0]);tip.hidden=false;var tw=tip.offsetWidth/2,lx=px/100*r.width;tip.style.left=Math.max(tw,Math.min(r.width-tw,lx))+"px";tip.style.top=(py/100*r.height)+"px"}
  function hide(){x.hidden=true;d.hidden=true;tip.hidden=true}
  pl.addEventListener("pointermove",function(e){show(e.clientX)});pl.addEventListener("pointerdown",function(e){show(e.clientX)});pl.addEventListener("pointerleave",hide)})})();
</script>"""

CALC_JS = r"""<script id="ob-calc-js">
(function(){var f=document.getElementById("ob-calc");if(!f)return;var M=["janvier","février","mars","avril","mai","juin","juillet","août","septembre","octobre","novembre","décembre"],D=null;
var $=function(i){return document.getElementById(i)},idx=$("ob-idx"),p0=$("ob-p0"),m0=$("ob-m0"),mn=$("ob-mn"),ac=$("ob-ac"),res=$("ob-res"),diff=$("ob-diff"),fo=$("ob-formula"),iv=$("ob-idxv"),cp=$("ob-copy");
function mo(p){var a=p.split("-");return M[+a[1]-1]+" "+a[0]}
function n(v,d){return v.toLocaleString("fr-FR",{minimumFractionDigits:d,maximumFractionDigits:d})}
function eur(v){return n(v,2)+" €"}
function parse(s){s=String(s||"").replace(/\s| | /g,"").replace(",",".");var v=parseFloat(s);return isFinite(v)?v:NaN}
function fixA(){var r=f.querySelector("input[name=a]:checked");if(!r)return 0;if(r.value==="autre"){var v=parse(ac.value);return isFinite(v)?Math.min(Math.max(v,0),100)/100:0}return +r.value}
function fill(sel,vals,keep){var cur=keep&&vals.some(function(x){return x[0]===keep})?keep:null;sel.innerHTML="";for(var i=vals.length-1;i>=0;i--){var o=document.createElement("option");o.value=vals[i][0];o.textContent=mo(vals[i][0]);sel.appendChild(o)}return cur}
function setIndex(code,k0,kn){var v=D.index[code].v,a=fill(m0,v,k0),b=fill(mn,v,kn);m0.value=a||v[Math.max(0,v.length-13)][0];mn.value=b||v[v.length-1][0]}
function calc(bump){if(!D)return;var code=idx.value,v=D.index[code].v,map={};v.forEach(function(x){map[x[0]]=x[1]});var I0=map[m0.value],In=map[mn.value],P0=parse(p0.value),a=fixA();
  if(!isFinite(P0)||!I0||!In){res.textContent="–";diff.textContent="Indiquez un prix initial.";return}
  var P=P0*(a+(1-a)*In/I0),dd=P-P0;res.textContent=eur(P);diff.textContent=(dd>=0?"+":"−")+eur(Math.abs(dd))+", soit "+(dd>=0?"+":"−")+n(Math.abs(dd/P0*100),1)+" %";
  fo.textContent="P = "+n(P0,P0%1?2:0)+" × ("+n(a,3).replace(/,?0+$/,"")+" + "+n(1-a,3).replace(/,?0+$/,"")+" × "+n(In,1)+" / "+n(I0,1)+")";
  iv.textContent=code+" : "+n(I0,1)+" en "+mo(m0.value)+", "+n(In,1)+" en "+mo(mn.value)+" (Insee)";
  if(bump){res.classList.remove("is-bump");void res.offsetWidth;res.classList.add("is-bump")}
  try{var q=new URLSearchParams({index:code,m0:m0.value,mn:mn.value,p:String(P0),a:String(a)});history.replaceState(null,"","?"+q.toString())}catch(e){}}
cp.addEventListener("click",function(){var t="Révision de prix, index "+idx.value+" (Insee)\n"+fo.textContent+"\n"+iv.textContent+"\nPrix révisé HT : "+res.textContent;
  (navigator.clipboard?navigator.clipboard.writeText(t):Promise.reject()).then(function(){cp.querySelector("span").textContent="Calcul copié"},function(){cp.querySelector("span").textContent="Copie impossible"});
  setTimeout(function(){cp.querySelector("span").textContent="Copier le calcul"},2200)});
f.addEventListener("submit",function(e){e.preventDefault()});
idx.addEventListener("change",function(){setIndex(idx.value,m0.value,mn.value);calc(true)});
[m0,mn].forEach(function(s){s.addEventListener("change",function(){calc(true)})});
p0.addEventListener("input",function(){calc(false)});ac.addEventListener("input",function(){var o=f.querySelector("input[name=a][value=autre]");o.checked=true;calc(false)});
[].forEach.call(f.querySelectorAll("input[name=a]"),function(r){r.addEventListener("change",function(){calc(true)})});
fetch("/assets/data/indices-bt.json").then(function(r){return r.json()}).then(function(d){D=d;var q=new URLSearchParams(location.search),c=q.get("index");
  if(c){c=c.toUpperCase().replace("B","b").replace(/^bT/,"BT");var k=Object.keys(D.index).filter(function(x){return x.toUpperCase()===q.get("index").toUpperCase()})[0];if(k)idx.value=k}
  setIndex(idx.value,q.get("m0"),q.get("mn"));if(q.get("p"))p0.value=String(q.get("p")).replace(".",",");
  var a=q.get("a");if(a!==null){var r=f.querySelector("input[name=a][value=\""+a+"\"]");if(r)r.checked=true;else if(isFinite(+a)){f.querySelector("input[name=a][value=autre]").checked=true;ac.value=n(+a*100,1)}}
  calc(false)}).catch(function(){diff.textContent="Les données n’ont pas pu être chargées. Réessayez dans un instant."})})();
</script>"""


def dataset_ld(SITE, url):
    return {"@type": "Dataset", "@id": SITE + url + "#donnees", "name": "Index du bâtiment BT, base 2010 : séries mensuelles", "alternateName": "Le Bâtimètre",
            "description": f"Les {len(IDX)} index BT de l’Insee (base 100 en 2010), dont {len(IDX) - N_ACT} série arrêtée, d’octobre 2014 à {mois(LAST_P)}, mis à jour chaque mois.",
            "url": SITE + url, "inLanguage": "fr-FR", "temporalCoverage": f"2014-10/{LAST_P}", "spatialCoverage": {"@type": "Country", "name": "France"},
            "dateModified": MAJ, "isBasedOn": "https://bdm.insee.fr/series/sdmx/data/INDEX-BT-TP-DIV-IM-2010", "creditText": "Source : Insee",
            "creator": {"@type": "Organization", "name": "Insee", "url": "https://www.insee.fr/"},
            "publisher": {"@id": SITE + "/#org"}, "keywords": ["index BT", "indice BT01", "révision de prix", "bâtiment", "Insee"],
            "distribution": [{"@type": "DataDownload", "encodingFormat": "text/csv", "contentUrl": SITE + "/assets/data/indices-bt.csv"},
                             {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": SITE + "/assets/data/indices-bt.json"}]}

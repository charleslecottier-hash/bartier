# Pages « Devis travaux à <ville> » pour les particuliers : une page par ville, les 5 métiers sur chaque page.
# Contenu local vérifié et sourcé (recherches du 20/11/2026), jamais une page copiée où seul le nom de la ville change :
# Google sanctionne les pages satellites. Aucune promesse de présence locale : la mise en relation dépend de la commune
# (« Hors zone, nous vous le disons à l'appel »), comme sur le reste du site.
import json as _json
import pathlib as _pl
import re as _re

import math as _math

from villes_data import CITIES as _BASE  # les six premières villes (données locales, une entrée par ville)

# Code Insee, département et région des six premières villes (les fiches de villes_new/ les portent elles-mêmes)
_META = {"lille": ("59350", 50.6292, 3.0573, "Nord", "59", "Hauts-de-France"), "rouen": ("76540", 49.4431, 1.0993, "Seine-Maritime", "76", "Normandie"),
         "paris": ("75056", 48.8566, 2.3522, "Paris", "75", "Île-de-France"), "lyon": ("69123", 45.7640, 4.8357, "Rhône", "69", "Auvergne-Rhône-Alpes"),
         "marseille": ("13055", 43.2965, 5.3698, "Bouches-du-Rhône", "13", "Provence-Alpes-Côte d’Azur"),
         "toulouse": ("31555", 43.6047, 1.4442, "Haute-Garonne", "31", "Occitanie")}
# Ordre d'affichage : des plus grandes communes aux plus petites (sert aussi de priorité aux étiquettes de la carte)
ORDER = ["paris", "marseille", "lyon", "toulouse", "nice", "nantes", "montpellier", "strasbourg", "bordeaux", "lille", "rennes", "toulon", "reims",
         "saint-etienne", "le-havre", "dijon", "grenoble", "angers", "nimes", "aix-en-provence", "clermont-ferrand", "le-mans", "brest", "tours",
         "amiens", "annecy", "limoges", "metz", "perpignan", "besancon", "orleans", "rouen", "caen", "mulhouse", "nancy", "avignon", "poitiers",
         "dunkerque", "versailles", "pau", "la-rochelle", "calais", "cannes", "beziers", "colmar", "bourges", "saint-nazaire", "ajaccio", "valence",
         "quimper", "troyes", "lorient", "niort", "chambery", "la-roche-sur-yon", "vannes", "bayonne", "cherbourg-en-cotentin", "chartres", "laval"]


def _new_cities():
    """Fiches de villes_new/ qui passent le contrôle qualité ; les autres restent des brouillons, non publiés."""
    import villes_check
    folder = _pl.Path(__file__).parent / "villes_new"
    if not folder.exists():
        return []
    pool = villes_check.others()
    out = []
    for p in sorted(folder.glob("*.py")):
        if villes_check.ok(p, pool):
            out.append(villes_check.load(p).CITY)
        else:
            print(f"  ville non publiée (contrôle qualité ou brouillon) : {p.stem}")
    return out


_rank = lambda c: (ORDER.index(c["slug"]) if c["slug"] in ORDER else len(ORDER), c["name"])
CITIES = sorted([dict(c, insee=m[0], lat=m[1], lon=m[2], dept=m[3], depcode=m[4], region=m[5]) for c in _BASE for m in [_META[c["slug"]]]]
                + _new_cities(), key=_rank)
_MOIS = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre", "décembre"]


def verified(c):
    """Date de vérification des sources : (ISO, en toutes lettres)."""
    iso = c.get("verified", "2026-11-20")
    y, m, d = (int(x) for x in iso.split("-"))
    return iso, f"{'1er' if d == 1 else d} {_MOIS[m - 1]} {y}"


def km(a, b):
    """Distance à vol d'oiseau entre deux villes, en kilomètres."""
    la1, lo1, la2, lo2 = map(_math.radians, (a["lat"], a["lon"], b["lat"], b["lon"]))
    h = _math.sin((la2 - la1) / 2) ** 2 + _math.cos(la1) * _math.cos(la2) * _math.sin((lo2 - lo1) / 2) ** 2
    return 12742 * _math.asin(_math.sqrt(h))


def voisines(c, n=6):
    return sorted((x for x in CITIES if x["slug"] != c["slug"]), key=lambda x: km(c, x))[:n]

TRADE_H3 = {"toiture": "Couvreur {a}", "facade": "Ravalement de façade {a}", "fenetres": "Fenêtres et portes {a}",
            "charpente": "Charpente {a}", "isolation": "Isolation {a}"}


def a_(c):
    """« à Lyon », mais « au Havre » : la fiche peut donner sa préposition (champ « a »)."""
    return c.get("a") or f"à {c['name']}"
TRADE_MORE = {"toiture": "Prix d’une toiture", "facade": "Prix d’un ravalement", "fenetres": "Prix d’une fenêtre",
              "charpente": "Prix d’une charpente", "isolation": "Prix de l’isolation"}
TRADE_PICK = {"toiture": "Devis toiture", "facade": "Devis façade", "fenetres": "Devis fenêtres", "charpente": "Devis charpente",
              "isolation": "Devis isolation"}

CSS = """<style id="vl-css">
.vl-wrap{padding:0 var(--cell)}
.vl-nw{white-space:nowrap}
.vl-others{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:36px 64px;padding:0 var(--cell)}
.vl-others .pf-olist{padding:0}
.vl-oh{margin-bottom:12px;font-size:.8rem;color:var(--muted)}
.vl-km{margin-left:6px;font-size:.8rem;color:var(--muted);white-space:nowrap}
.vl-trades li{scroll-margin-top:96px}
.vl-dl .link,.vl-trades .link,.vl-steps .link{display:inline;white-space:normal;min-height:0}
.vl-more{align-items:center}
.vl-more .link{align-self:center}
.vl-dl{grid-column:1 / -1}
.vl-trades{grid-template-columns:repeat(2,minmax(0,1fr))}
.vl-trades p+p{margin-top:8px}
.vl-more{display:flex;flex-wrap:wrap;gap:8px 16px;font-size:.92rem}
.vl-src{margin-top:24px;padding:0 var(--cell);font-size:.8rem;color:var(--muted)}
.vl-figs b small{font-size:.4em;letter-spacing:0}
.vl-figs .vl-fsrc{font-size:.78rem;color:rgba(255,255,255,.55)}
.vl-figs .vl-fsrc a{color:inherit}
.pf-howto.vl-steps li::before{color:var(--accent)}
.pf-howto.vl-steps p{color:inherit}
/* en-tête : pas de bande vide sous le formulaire */
.vl-hero{padding-bottom:clamp(48px,5vw,72px)}
/* fuite : bandeau sobre, l'accent reste sur le bouton */
.vl-leak{padding-block:clamp(40px,4vw,56px)}
.vl-leakbar{display:flex;align-items:center;justify-content:space-between;gap:16px 40px;margin:0 var(--cell);padding:24px 28px;border:1px solid var(--rule);background:#fff}
.vl-leakbar h2{margin-bottom:4px;font:400 clamp(1.3rem,2vw,1.6rem)/1.2 var(--f-display);letter-spacing:-.01em}
.vl-leakbar p{color:var(--muted)}
.vl-leakbar .btn{flex:none}
/* photo de la ville, fondue dans le bandeau sombre */
.vl-fig.has-scene{padding-top:0}
.vl-scene{position:relative;margin:0 0 clamp(40px,5vw,72px);height:clamp(280px,34vw,520px);overflow:hidden;background:var(--ink)}
.vl-scene img{width:100%;height:100%;object-fit:cover;display:block}
.vl-scene::after{content:"";position:absolute;inset:0;background:linear-gradient(to bottom,rgba(10,20,36,0) 45%,rgba(10,20,36,.55) 75%,var(--ink) 100%);pointer-events:none}
.vl-scene figcaption{position:absolute;left:var(--cell);right:var(--cell);bottom:16px;z-index:1;font-size:.75rem;color:rgba(255,255,255,.62)}
.vl-scene figcaption a{color:inherit}
/* sommaire */
.vl-toc{display:flex;flex-wrap:wrap;align-items:center;gap:8px;margin-top:32px;padding:0 var(--cell)}
.vl-toc span{flex:0 0 auto;margin-right:8px;font-size:.8rem;color:var(--muted);white-space:nowrap}
.vl-toc a{padding:8px 16px;border:1px solid var(--rule);font-size:.9rem;line-height:1.2;color:inherit;text-decoration:none;transition:border-color .2s,color .2s}
.vl-toc a:hover,.vl-toc a:focus-visible{border-color:var(--accent);color:var(--accent)}
#en-chiffres,#a-savoir,#travaux,#demarches,#aides,#questions{scroll-margin-top:72px}
/* chiffres et carte */
.vl-figgrid{display:grid;grid-template-columns:minmax(0,1.5fr) minmax(0,1fr);gap:40px 72px;align-items:center;padding:0 var(--cell)}
.vl-figgrid .pf-proms{grid-template-columns:repeat(2,minmax(0,1fr));gap:40px 32px;padding:0}
.vl-map-d{width:100%;max-width:440px;justify-self:end}
[data-tone="dark"] .vl-fr{fill:rgba(255,255,255,.04);stroke:#fff;stroke-opacity:.32}
[data-tone="dark"] .vl-dot{fill:rgba(255,255,255,.7)}
[data-tone="dark"] .vl-lab{fill:rgba(255,255,255,.72)}
[data-tone="dark"] .vl-dot.is-on{fill:#8fb0ff}
[data-tone="dark"] .vl-halo{fill:#8fb0ff;opacity:.22}
[data-tone="dark"] .vl-lab.is-on{fill:#fff}
[data-tone="dark"] .vl-svg a:hover .vl-lab,[data-tone="dark"] .vl-svg a:focus .vl-lab,[data-tone="dark"] .vl-svg a:hover .vl-dot,[data-tone="dark"] .vl-svg a:focus .vl-dot{fill:#fff}
/* règles locales en fiches */
.vl-dl{grid-template-columns:repeat(3,minmax(0,1fr));gap:16px}
.vl-dl div{padding:24px;border:1px solid var(--rule);background:#fff}
.vl-dl dt{margin-bottom:8px}
.vl-dl dd{font-size:1rem;line-height:1.5}
/* métiers avec photo */
.vl-tr{display:grid;grid-template-columns:128px minmax(0,1fr);gap:24px;align-items:start}
.vl-tr-ph{margin:0;aspect-ratio:1 / 1;overflow:hidden}
.vl-tr-ph img{width:100%;height:100%;object-fit:cover}
.vl-tr-b h3{margin-top:2px}
/* conseiller public mis en avant */
.vl-aides .vl-adv{grid-column:1 / -1;display:grid;grid-template-columns:minmax(0,1fr) auto;gap:16px 40px;align-items:center;padding:28px 32px;border-top:0;background:var(--ink);color:#fff}
.vl-adv .vl-adv-k{margin-bottom:6px;font-size:.8rem;color:rgba(255,255,255,.6)}
.vl-adv h3{font-size:1.5rem}
.vl-adv p{color:rgba(255,255,255,.82)}
.vl-adv .link{color:#fff}
.vl-adv .btn{white-space:nowrap}
@media (max-width:760px){.vl-trades{grid-template-columns:1fr}.vl-others{grid-template-columns:1fr}
.vl-leakbar{flex-direction:column;align-items:flex-start;padding:20px}
.vl-toc{flex-wrap:nowrap;overflow-x:auto;margin-top:20px;padding-bottom:4px;scrollbar-width:none}.vl-toc::-webkit-scrollbar{display:none}.vl-toc a{flex:0 0 auto}
.vl-figgrid{grid-template-columns:1fr}.vl-map-d{justify-self:center;max-width:320px}
.vl-dl{grid-template-columns:1fr}
.vl-tr{grid-template-columns:84px minmax(0,1fr);gap:16px}
.vl-aides .vl-adv{grid-template-columns:1fr;padding:24px 20px}}
@media (min-width:761px) and (max-width:1100px){.vl-dl{grid-template-columns:repeat(2,minmax(0,1fr))}}
</style>"""


_MAP = _json.loads((_pl.Path(__file__).parent / "france_map.json").read_text(encoding="utf-8"))  # Natural Earth, domaine public


def _xy(c):
    """Position sur la carte : projection de la carte (Natural Earth, équirectangulaire), ajustée sur les six premières villes."""
    if c["slug"] in _MAP["cities"]:
        return tuple(_MAP["cities"][c["slug"]])
    return (round(27.9265 * c["lon"] - 0.0069 * c["lat"] + 133.3579, 1), round(-0.0035 * c["lon"] - 40.5889 * c["lat"] + 2073.9614, 1))


def carte(current=None):
    """Carte de France des villes, cliquable ; la ville de la page est mise en avant. Toutes les villes ont leur point ;
    les noms s'affichent tant qu'ils ne se chevauchent pas (la ville de la page d'abord, puis les plus grandes)."""
    W, H = _MAP["w"] + 72, _MAP["h"] + 16
    fs = 14 if len(CITIES) > 20 else 17  # au-delà d'une vingtaine de villes, des noms plus petits pour qu'ils tiennent
    cw = .54 * fs
    rank = {c["slug"]: i for i, c in enumerate(sorted(CITIES, key=_rank))}
    dots = {c["slug"]: (lambda x, y: (x - 6, y - 6, x + 6, y + 6))(*_xy(c)) for c in CITIES}
    inter = lambda a, b: a[0] < b[2] and b[0] < a[2] and a[1] < b[3] and b[1] < a[3]
    out = lambda b: b[0] < -12 or b[2] > W or b[1] < -16 or b[3] > H
    placed, labels = [], {}
    for c in sorted(CITIES, key=lambda c: (c["slug"] != current, _rank(c))):
        x, y = _xy(c)
        w = cw * len(c["name"]) + 4
        # la ville de la page et les plus grandes villes passent avant les points des villes plus petites
        strong = c["slug"] == current or rank[c["slug"]] < 6
        every = [b for s2, b in dots.items() if s2 != c["slug"]]
        block = [b for s2, b in dots.items() if s2 != c["slug"] and (s2 == current or rank[s2] < rank[c["slug"]])]
        cands = []
        for lx, anchor, dy in ((x + 12, "start", 0), (x - 12, "end", 0), (x, "middle", -(fs - 1)), (x, "middle", fs + 5),
                               (x + 10, "start", fs - 2), (x - 10, "end", fs - 2), (x + 10, "start", -(fs - 4)), (x - 10, "end", -(fs - 4))):
            k = fs / 17
            b = ((lx, y + dy - 12 * k, lx + w, y + dy + 6 * k) if anchor == "start" else (lx - w, y + dy - 12 * k, lx, y + dy + 6 * k) if anchor == "end"
                 else (x - w / 2, y + dy - 16 * k, x + w / 2, y + dy + 2 * k))
            cands.append((b, (lx, anchor, dy)))
        pick = next((lab for b, lab in cands if not out(b) and not any(inter(b, o) for o in placed + every)), None)
        if pick is None and strong:  # sinon, une grande ville peut passer sur le point d'une ville plus petite
            pick = next((lab for b, lab in cands if not out(b) and not any(inter(b, o) for o in placed + block)), None)
        if pick is None and c["slug"] == current:  # la ville de la page a toujours son nom
            pick = next((lab for b, lab in cands if not out(b)), cands[0][1])
        if pick:
            placed.append(next(b for b, lab in cands if lab == pick))
            labels[c["slug"]] = pick
    pins = []
    for c in CITIES:
        x, y = _xy(c)
        on = c["slug"] == current
        dot = (f'<circle cx="{x}" cy="{y}" r="13" class="vl-halo"/><circle cx="{x}" cy="{y}" r="6.5" class="vl-dot is-on"/>' if on
               else f'<circle cx="{x}" cy="{y}" r="5" class="vl-dot"/>')
        lab = labels.get(c["slug"])
        ta = f' text-anchor="{lab[1]}"' if lab and lab[1] != "start" else ""
        fz = f' style="font-size:{fs}px"' if fs != 17 else ""
        label = (f'<text x="{lab[0]}" y="{y + 4.5 + lab[2]}" class="vl-lab{" is-on" if on else ""}"{ta}{fz}>{c["name"]}</text>'
                 if lab else f'<title>{c["name"]}</title>')
        pins.append(f'<g>{dot}{label}</g>' if on else f'<a href="{path(c)}" aria-label="Devis travaux {a_(c)}">{dot}{label}</a>')
    w, h = _MAP["w"], _MAP["h"]
    return (f'<svg class="vl-svg" viewBox="-12 -16 {w + 84} {h + 32}" role="img" aria-labelledby="vl-map-t"><title id="vl-map-t">Carte des villes : '
            + ", ".join(c["name"] for c in CITIES) + f'</title><path d="{_MAP["d"]}" class="vl-fr"/>' + "".join(pins) + '</svg>')


MAP_CSS = """.vl-map{margin:0}
.vl-svg{display:block;width:100%;height:auto;overflow:visible}
.vl-fr{fill:var(--paper,#EEF0F3);stroke:var(--ink,#0A1424);stroke-opacity:.18;stroke-width:1;stroke-linejoin:round}
.vl-dot{fill:var(--ink,#0A1424)}
.vl-dot.is-on{fill:var(--accent,#2D5BE3)}
.vl-halo{fill:var(--accent,#2D5BE3);opacity:.16}
.vl-lab{font-size:17px;fill:var(--ink,#0A1424)}
[data-tone="paper"] .vl-fr{fill:#fff}
.vl-lab.is-on{font-weight:500;fill:var(--accent,#2D5BE3)}
.vl-svg a:hover .vl-lab,.vl-svg a:focus .vl-lab{fill:var(--accent,#2D5BE3);text-decoration:underline}
.vl-svg a:hover .vl-dot,.vl-svg a:focus .vl-dot{fill:var(--accent,#2D5BE3)}"""
CSS = CSS.replace("</style>", MAP_CSS + "\n</style>", 1)


def path(c):
    return f"/devis-travaux/{c['slug']}/"


_TEL = _re.compile(r"(?<![\d+])0[1-9](?: \d{2}){4}(?!\d)")
_MAIL = _re.compile(r"(?<![\w.:/-])[\w.+-]+@[\w-]+(?:\.[\w-]+)+")


def _contact(s):
    """Numéros et adresses e-mail cliquables (un geste pour appeler la mairie ou le conseiller)."""
    s = _TEL.sub(lambda m: f'<a class="link" href="tel:+33{m.group(0)[1:].replace(" ", "")}">{m.group(0)}</a>', s)
    return _MAIL.sub(lambda m: f'<a class="link" href="mailto:{m.group(0)}">{m.group(0)}</a>', s)


def _ext(label, url):
    return f'<a class="link" href="{url}" target="_blank" rel="noopener">{label}</a>'


def build_city(PF, phone, phone_txt, crumbs, c, img=None):
    tick = PF.tick()
    v = c["name"]
    av = a_(c)
    one = lambda s: s[:-1] if s.endswith(".") and ". " not in s else s  # sous-titre d'une phrase : pas de point final
    c = dict(c, figures_intro=one(c["figures_intro"]), steps_intro=one(c["steps_intro"]), trades_intro=one(c["trades_intro"]))
    parts = PF.build(lambda a: ("", ""), phone, phone_txt, crumbs, parts=True)
    form = parts["form"]
    form = form.replace('placeholder="Ex. 80000"', f'placeholder="Ex. {c["cp"]}"', 1)
    hero = f"""<section class="sheet pf-hero vl-hero" id="haut" data-tone="light">
  <div class="grid pf-hero-grid">
    <div class="pf-intro">
      {crumbs}
      <div class="pf-h1"><h1 class="pf-kw">Devis travaux {av} : toiture, façade, fenêtres, isolation</h1> <p class="pf-big">Pas cinq <span class="pf-who">artisans</span>. <br>Un seul, près de chez vous.</p></div>
      <p class="lead">Décrivez vos travaux {av} en 1 minute.<br>Nous vous rappelons en moins de 5 minutes en semaine, et nous fixons la visite.</p>
      {PF.trust("d-only")}
      <p class="pf-call d-only">Pressé ? <a class="link" href="tel:{phone}">{phone_txt}</a></p>
    </div>
    {form}
    <div class="pf-mtrust m-only">{PF.trust()}</div>
  </div>
  <nav class="vl-toc" aria-label="Sur cette page"><span>Sur cette page</span><a href="#en-chiffres">Chiffres</a><a href="#a-savoir">À savoir</a><a href="#travaux">Par métier</a><a href="#demarches">Démarches</a><a href="#aides">Aides</a><a href="#questions">Questions</a></nav>
</section>"""

    figs = "".join(f'<li><b>{a}</b> <span>{b}</span> <span class="vl-fsrc">{src}</span></li>' for a, b, src in c["figures"])
    scene, scls = "", ""
    if c.get("photo"):
        ph = c["photo"]
        srcset = ", ".join(f'/assets/villes/{c["slug"]}-{w}.webp {w}w' for w in (800, 1200, 1600, 2400))
        scene = (f'<figure class="vl-scene"><img srcset="{srcset}" sizes="100vw" src="/assets/villes/{c["slug"]}-1600.webp" alt="{ph["alt"]}" '
                 f'width="2400" height="{ph["h"]}" loading="lazy" decoding="async" style="object-position:{ph.get("pos", "50% 50%")}">'
                 f'<figcaption>{ph["caption"]} · Photo : <a href="{ph["page"]}" target="_blank" rel="noopener">{ph["creator"]}</a>, '
                 f'<a href="{ph["license_url"]}" target="_blank" rel="noopener">{ph["license"]}</a>, recadrée</figcaption></figure>')
        scls = " has-scene"
    figures = f"""<section class="sheet vl-fig{scls}" id="en-chiffres" data-tone="dark">
  {scene}
  <div class="grid sp-head"><h2 data-split>{v} en quelques chiffres</h2><p>{c["tldr"]}</p></div>
  <div class="vl-figgrid"><ul class="pf-proms vl-figs">{figs}</ul><figure class="vl-map vl-map-d">{carte(c["slug"])}</figure></div>
</section>"""
    steps = "".join(f"<li><h3>{a}</h3><p>{_contact(b)}</p></li>" for a, b in c["steps"])
    steps = f"""<section class="sheet" id="demarches" data-tone="light">
  <div class="grid sp-head"><h2 data-split>Quelles démarches avant des travaux {av} ?</h2><p>{c["steps_intro"]}</p></div>
  <ol class="pf-howto vl-steps">{steps}</ol>
</section>"""

    facts = "".join(f"<div><dt>{a}</dt><dd>{_contact(b)}</dd></div>" for a, b in c["facts"])
    local = f"""<section class="sheet" id="a-savoir" data-tone="paper">
  <div class="grid sp-head"><h2 data-split>Que faut-il savoir avant des travaux {av} ?</h2><p>{c["answer"]}</p></div>
  <div class="grid"><dl class="pf-dl vl-dl">{facts}</dl></div>
  <p class="vl-src">Par <a class="link" href="/qui-sommes-nous/#charles">Charles Le Cottier</a>, cofondateur de Bartier &amp; Co. Sources officielles vérifiées le <time datetime="{verified(c)[0]}">{verified(c)[1]}</time>. Une règle a changé ? <a class="link" href="mailto:contact@bartierandco.com">Écrivez-nous</a>.</p>
</section>"""

    items = []
    photos = {x[0]: (x[3], x[7]) for x in PF.TRADES}
    for k in ("toiture", "facade", "fenetres", "charpente", "isolation"):
        paras = "".join(f"<p>{_contact(p)}</p>" for p in c["trades"][k])
        ph = ""
        if img:
            if k == "isolation":
                src = f'srcset="{PF.ISO_SRCSET}" sizes="(max-width: 760px) 84px, 128px" src="{PF.ISO_PHOTO}-480x360.webp"'
            else:
                src = f'src="{img(photos[k][0])[0]}" sizes="(max-width: 760px) 84px, 128px"'
            ph = f'<figure class="frame vl-tr-ph"><img {src} alt="{photos[k][1]}" width="400" height="400" loading="lazy"></figure>'
        items.append(f'<li id="t-{k}" class="vl-tr">{ph}<div class="vl-tr-b"><h3>{TRADE_H3[k].format(a=av)}</h3>{paras}<p class="vl-more"><a class="link pf-pick" href="#projet" data-v="{k}">{TRADE_PICK[k]}</a>'
                     f'<a class="link" href="/devis-travaux/{PF.SLUG[k]}/">{TRADE_MORE[k]}</a></p></div></li>')
    trades = f"""<section class="sheet" id="travaux" data-tone="light">
  <div class="grid sp-head"><h2 data-split>Vos travaux {av}, métier par métier</h2><p>{c["trades_intro"]}</p></div>
  <ul class="pf-checks vl-trades">{"".join(items)}</ul>
</section>"""

    a0, b0 = c["aides"][0]
    m = _TEL.search(b0)
    call = f'<a class="btn" href="tel:+33{m.group(0)[1:].replace(" ", "")}"><span>Appeler le {m.group(0)}</span>{tick}</a>' if m else ""
    adv = f'<li class="vl-adv"><div><p class="vl-adv-k">Conseil public, gratuit et neutre</p><h3>{a0}</h3><p>{_contact(b0)}</p></div>{call}</li>'
    aid = adv + "".join(f"<li><h3>{a}</h3><p>{_contact(b)}</p></li>" for a, b in c["aides"][1:])
    aides = f"""<section class="sheet" id="aides" data-tone="paper">
  <div class="grid sp-head"><h2 data-split>Quelles aides pour vos travaux {av} ?</h2><p>{c["aides_intro"]}</p></div>
  <ul class="pf-checks vl-trades vl-aides">{aid}</ul>
</section>"""

    leak = f"""<section class="sheet vl-leak" id="fuite-toiture" data-tone="light">
  <div class="vl-leakbar"><div><h2>Une fuite de toiture {av} ?</h2><p>Signalez-la : rappel prioritaire. En attendant, suivez <a class="link" href="/devis-travaux/toiture/#fuite-toiture">les 5 bons réflexes</a>.</p></div><a class="btn pf-pick" href="#projet" data-v="toiture" data-need="fuite"><span>Signaler une fuite</span>{tick}</a></div>
</section>"""

    brief = [("Le service", f"Bartier &amp; Co vous met gratuitement en relation avec l’artisan partenaire qui couvre votre commune, pour vos travaux de toiture, façade, fenêtres, charpente ou isolation {av} et alentours."),
             ("Pour qui", f"Les propriétaires {av}, occupants ou bailleurs, en maison ou en copropriété. Locataire ? Transmettez la page à votre propriétaire.")] + PF.BRIEF[1:]
    brief = "".join(f"<div><dt>{a}</dt><dd>{b}</dd></div>" for a, b in brief)
    brief = f"""<section class="sheet pf-brief" data-tone="light" aria-labelledby="pf-brief-h">
  <div class="grid pf-brief-grid">
    <h2 id="pf-brief-h">Devis travaux {av} : l’essentiel</h2>
    <dl class="pf-dl">{brief}</dl>
    <p class="pf-upd">Mis à jour le <time datetime="@@MAJ@@">@@MAJFR@@</time></p>
  </div>
</section>"""

    rows = "\n".join(f'      <details class="fq"><summary><span>{q}</span><i class="fq-icon" aria-hidden="true"></i></summary><div class="fq-a"><p>{_contact(a)}</p></div></details>' for q, a in faq(c))
    faqs = f"""<section class="faq sheet" id="questions" data-kind="faq" data-tone="paper">
  <div class="grid fq-grid">
    <div class="fq-head"><h2 data-split>Travaux {av} : vos questions</h2><p>Une autre question ? <a class="link" href="tel:{phone}">{phone_txt}</a></p><p><a class="link" href="/devis-travaux/#questions">Voir toutes les questions</a></p></div>
    <div class="fq-list">
{rows}
    </div>
  </div>
</section>"""

    cities = "".join(f'<li><a class="link" href="{path(x)}">Devis travaux {a_(x)}</a> <span class="vl-km">{round(km(c, x)):d} km</span></li>' for x in voisines(c))
    cities += '<li><a class="link" href="/devis-travaux/#villes">Toutes les villes</a></li>'
    metiers = "".join(f'<li><a class="link" href="/devis-travaux/{PF.SLUG[x[0]]}/">{x[5]}</a></li>' for x in PF.TRADES)
    others = f"""<section class="sheet pf-others" data-tone="light">
  <div class="grid sp-head"><h2 data-split>Ailleurs en France</h2><p><a class="link" href="/devis-travaux/">Tous les devis de travaux</a></p></div>
  <div class="vl-others"><div><p class="vl-oh">Villes les plus proches</p><ul class="pf-olist">{cities}</ul></div><div><p class="vl-oh">Par métier</p><ul class="pf-olist">{metiers}</ul></div></div>
</section>"""

    out = CSS + "\n" + "\n\n".join([hero, figures, local, trades, parts["promise"], steps, aides, leak, brief, faqs, others, parts["end"]])
    for w in ("PLUi-H", "PLU-H"):  # pas de coupure au trait d'union
        out = _re.sub(r"(?<![\w-])" + _re.escape(w) + r"(?![\w-])", f'<span class="vl-nw">{w}</span>', out)
    return out


PLACE = {"lille": (50.6292, 3.0573, "Nord"), "rouen": (49.4431, 1.0993, "Seine-Maritime"), "paris": (48.8566, 2.3522, "Paris"),
         "lyon": (45.7640, 4.8357, "Rhône"), "marseille": (43.2965, 5.3698, "Bouches-du-Rhône"), "toulouse": (43.6047, 1.4442, "Haute-Garonne")}


def faq(c):
    return c["faq"] + [(f"Intervenez-vous partout {a_(c)} ?",
                        "Nous vous mettons en relation avec l’artisan partenaire qui couvre votre commune et votre métier. "
                        "Si aucun ne la couvre, nous vous le disons dès l’appel et votre demande n’est transmise à personne.")]


def schema(SITE, faq_ld, bc_ld, PF, c):
    clean = lambda s: _re.sub("<[^>]+>", "", s).replace("&amp;", "&").replace("&nbsp;", " ")
    p = path(c)
    city = {"@type": "City", "name": c["name"], "sameAs": [c["wiki"], f"https://www.wikidata.org/wiki/{c['wikidata']}"],
            "identifier": {"@type": "PropertyValue", "propertyID": "Code officiel géographique (Insee)", "value": c["insee"]},
            "geo": {"@type": "GeoCoordinates", "latitude": c["lat"], "longitude": c["lon"]},
            "containedInPlace": {"@type": "AdministrativeArea", "name": c["dept"], "identifier": c["depcode"],
                                 "containedInPlace": {"@type": "AdministrativeArea", "name": c["region"]}}}
    graph = [
        {"@type": "WebPage", "@id": SITE + p, "url": SITE + p, "name": c["title"], "description": c["desc"], "inLanguage": "fr-FR",
         "dateModified": "@@MAJ@@", "lastReviewed": verified(c)[0], "isPartOf": {"@id": SITE + "/#website"}, "publisher": {"@id": SITE + "/#org"}, "about": city,
         "author": {"@type": "Person", "@id": SITE + "/qui-sommes-nous/#charles", "name": "Charles Le Cottier", "jobTitle": "Cofondateur", "url": SITE + "/qui-sommes-nous/#charles"}},
        {"@type": "Service", "name": f"Devis travaux {a_(c)}", "serviceType": "Mise en relation avec un artisan : toiture, façade, fenêtres, charpente, isolation",
         "description": clean(c["answer"]), "url": SITE + p, "areaServed": city,
         "audience": {"@type": "Audience", "audienceType": "Propriétaires"},
         "provider": {"@type": "Organization", "@id": SITE + "/#org", "name": "Bartier & Co", "url": SITE + "/"},
         "offers": {"@type": "Offer", "price": "0", "priceCurrency": "EUR", "description": "Gratuit pour le particulier : mise en relation, visite et devis de l'artisan"}},
        faq_ld([(q, clean(a)) for q, a in faq(c)]), bc_ld(("Devis travaux", "/devis-travaux/"), (c["name"], p))]
    return PF.link_graph(SITE, p, {"@context": "https://schema.org", "@graph": graph})

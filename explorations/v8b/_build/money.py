"""Pages « money » pour les particuliers : recherches d'achat (voir explorations/seo/MONEY-KEYWORDS.md).

- /devis-travaux/toiture/urgence/      couvreur en urgence, fuite de toiture
- /devis-travaux/toiture/demoussage/   démoussage et nettoyage de toiture
- /devis-travaux/<métier>/<ville>/     couvreur à <ville>, ravalement de façade à <ville>

Les faits locaux viennent des fiches ville déjà vérifiées (villes_data.py, villes_new/). Rien n'est inventé :
pas de « RGE », pas d'intervention « 24 h/24 » ni « dans l'heure ».
"""
import re

CLEAN = lambda s: re.sub("<[^>]+>", "", s).replace("&amp;", "&").replace("&nbsp;", " ").replace(" ", " ")
EXT = lambda label, url: f'<a class="link" href="{url}" target="_blank" rel="noopener">{label}</a>'

# Source unique du démoussage (lue le 22/11/2026)
SG_NET = ("La Maison Saint-Gobain, 03/2026", "https://www.lamaisonsaintgobain.fr/guides-travaux/toiture-charpente/prix-nettoyage-toiture-m2")

# Métiers qui ont une page par ville, et leurs libellés
CITY_TRADES = {
    "toiture": dict(h1="Couvreur {a} : devis toiture gratuit", title="Couvreur {a} : devis toiture gratuit",
                    desc="Un couvreur {a} vient chiffrer votre toiture : réfection, fuite, zinguerie, démoussage. Règles locales vérifiées, visite et devis gratuits.",
                    local_h2="Votre toiture {a} : ce qu’il faut savoir", link="Couvreur {a}", service="Couverture et zinguerie", who="couvreurs",
                    faq_kw=r"toit|toiture|couvreur|tuile|ardoise|zinc|charpente|termite|mérule|tempête|vent|neige|grêle|solaire|photovolta"),
    "facade": dict(h1="Ravalement de façade {a} : devis gratuit", title="Ravalement de façade {a} : devis gratuit",
                   desc="Une entreprise de ravalement {a} vient chiffrer votre façade : nettoyage, fissures, enduit, peinture, isolation. Règles locales vérifiées, devis gratuit.",
                   local_h2="Votre façade {a} : ce qu’il faut savoir", link="Ravalement de façade {a}", service="Ravalement de façade", who="façadiers",
                   faq_kw=r"façade|ravalement|enduit|peinture|couleur|échafaudage|nichoir|martinet|isolation|pierre|crépi"),
}
ROOF_ONLY = re.compile(r"ravalement|façade|nichoir|martinet", re.I)


def need_preset(form, need):
    """Le formulaire s'ouvre directement sur le bon besoin (« fuite » ou libellé exact d'une option)."""
    return form.replace('<form class="pf-form"', f'<form class="pf-form" data-need="{need}"', 1)


def _faq_block(rows_qa, title, phone, phone_txt):
    rows = "\n".join(f'      <details class="fq"><summary><span>{q}</span><i class="fq-icon" aria-hidden="true"></i></summary><div class="fq-a"><p>{a}</p></div></details>' for q, a in rows_qa)
    return f"""<section class="faq sheet" id="questions" data-kind="faq" data-tone="paper">
  <div class="grid fq-grid">
    <div class="fq-head"><h2 data-split>{title}</h2><p>Une autre question&nbsp;? <a class="link" href="tel:{phone}">{phone_txt}</a></p><p><a class="link" href="/devis-travaux/#questions">Voir toutes les questions</a></p></div>
    <div class="fq-list">
{rows}
    </div>
  </div>
</section>"""


def _hero(PF, crumbs, kw, big, lead, form, extra=""):
    return f"""<section class="sheet pf-hero" id="haut" data-tone="light">
  <div class="grid pf-hero-grid">
    <div class="pf-intro">
      {crumbs}
      <div class="pf-h1"><h1 class="pf-kw">{kw}</h1> <p class="pf-big">{big}</p></div>
      <p class="lead">{lead}</p>{extra}
      {PF.trust("d-only")}
    </div>
    {form}
    <div class="pf-mtrust m-only">{PF.trust()}</div>
  </div>
</section>"""


def _band(PF, text, sub, href="#projet", label="Obtenir mon devis gratuit"):
    return f'<div class="pf-band"><p>{text} <span class="pf-band-sub">{sub}</span></p><a class="btn" href="{href}"><span>{label}</span>{PF.tick()}</a></div>'


def _others(title, links, more=None):
    items = "".join(f'<li><a class="link" href="{h}">{t}</a></li>' for t, h in links)
    more = f'<p><a class="link" href="{more[1]}">{more[0]}</a></p>' if more else ""
    return f"""<section class="sheet pf-others" data-tone="light">
  <div class="grid sp-head"><h2 data-split>{title}</h2>{more}</div>
  <ul class="pf-olist">{items}</ul>
</section>"""


# ——— Toiture en urgence ———
URGENCE = dict(
    path="/devis-travaux/toiture/urgence/",
    title="Couvreur en urgence : fuite de toiture, rappel prioritaire",
    desc="Fuite de toiture ou dégât de tempête : décrivez-le en 1 minute. Rappel prioritaire, et le couvreur de votre secteur fixe le premier créneau possible. Gratuit.",
    crumb="Urgence",
)
URG_FAQ = [
    ("Rappelez-vous le soir et le week-end ?",
     "Nous rappelons du lundi au vendredi, de 8 h à 19 h, en moins de 5 minutes. Le soir et le week-end, votre demande est enregistrée et rappelée en premier dès la réouverture."),
    ("Le couvreur peut-il venir dans l’heure ?",
     "Nous ne le promettons pas : le délai dépend du planning de l’artisan et de la météo. Le couvreur de votre secteur fixe avec vous le premier créneau possible, et nous vous le disons pendant l’appel."),
    ("Faut-il bâcher le toit soi-même ?",
     "Non. Ne montez jamais sur le toit, encore moins s’il est mouillé ou par grand vent. Protégez l’intérieur (seaux, bâches au sol, mobilier à l’abri) et laissez le couvreur mettre la toiture hors d’eau."),
    ("Et en cas de danger immédiat ?",
     "Des tuiles ou des éléments qui menacent de tomber sur la voie publique, un plafond qui s’affaisse : éloignez-vous et appelez les pompiers, au 18 ou au 112."),
]


def build_urgence(PF, phone, phone_txt, crumbs):
    blocks = PF.build(lambda a: ("", ""), phone, phone_txt, crumbs, parts=True)
    form = need_preset(blocks["form"].replace('<form class="pf-form"', '<form class="pf-form" data-preset="toiture"', 1), "fuite")
    hero = _hero(PF, crumbs, "Couvreur en urgence : fuite de toiture", 'Une fuite&nbsp;? <br><span class="pf-acc">Rappel prioritaire.</span>',
                 "Décrivez la fuite en 1 minute. En semaine, de 8 h à 19 h, nous vous rappelons en priorité, en moins de 5 minutes. Le couvreur de votre secteur fixe ensuite le premier créneau possible.",
                 form)
    honest = [("Rappel prioritaire", "Une fuite passe avant les autres demandes : en semaine de 8 h à 19 h, en moins de 5 minutes. Le soir et le week-end, elle est rappelée en premier dès la réouverture."),
              ("Un seul couvreur", "Celui qui couvre votre commune. Il trouve l’origine de la fuite, protège la toiture si besoin et chiffre la réparation."),
              ("Pas de promesse intenable", "Nous ne promettons pas d’intervention dans l’heure : le délai dépend de l’artisan et de la météo. Nous vous le disons dès l’appel."),
              ("Gratuit pour vous", "La mise en relation, la visite et le devis sont gratuits. C’est l’artisan qui nous rémunère.")]
    honest = "".join(f"<li><h3>{a}</h3><p>{b}</p></li>" for a, b in honest)
    honest = f"""<section class="sheet" id="travaux" data-tone="light">
  <div class="grid sp-head"><h2 data-split>Ce que nous faisons pour une fuite</h2><p>Et ce que nous ne promettons pas</p></div>
  <ul class="pf-checks pf-needs">{honest}</ul>
  {_band(PF, "Une fuite en ce moment&nbsp;?", "Rappel prioritaire, sans engagement.", label="Signaler une fuite")}
  <p class="pf-upd" style="padding:0 var(--cell)">Mis à jour le <time datetime="@@MAJ@@">@@MAJFR@@</time></p>
</section>"""
    faq_rows = URG_FAQ + [qa for qa in PF.trade_faq("toiture") if qa[0].startswith("L’assurance")]
    faq = _faq_block(faq_rows, "Fuite de toiture : vos questions", phone, phone_txt)
    others = _others("Autres travaux de toiture", [("Devis toiture", "/devis-travaux/toiture/"), ("Démoussage de toiture", DEMOUSSAGE["path"]),
                                                    ("Devis charpente", "/devis-travaux/charpente/")], more=("Tous les devis de travaux", "/devis-travaux/"))
    return "\n\n".join([hero, blocks["leak"], honest, faq, others, blocks["end"]]), faq_rows


# ——— Démoussage de toiture ———
DEMOUSSAGE = dict(
    path="/devis-travaux/toiture/demoussage/",
    title="Démoussage de toiture : devis gratuit près de chez vous",
    desc="Démoussage et nettoyage de toiture : 25 à 35 €/m² (La Maison Saint-Gobain). Un couvreur de votre secteur vient chiffrer. Visite et devis gratuits.",
    crumb="Démoussage",
)
DEM_PRICES = [("Nettoyage simple", "20 à 30 €/m²"), ("Démoussage avec brossage manuel", "25 à 35 €/m²"),
              ("Nettoyage, démoussage et traitement hydrofuge", "35 à 45 €/m²"), ("Toiture en ardoise naturelle", "30 à 40 €/m² au minimum"),
              ("Toiture de 150 m², démoussage et hydrofuge", "5 250 à 6 750 €"), ("Toiture de 200 m², traitement complet", "8 000 à 10 000 €")]
DEM_STEPS = [("Inspection de la couverture", "Le couvreur vérifie l’état des tuiles ou des ardoises et choisit la méthode adaptée."),
             ("Retrait des débris et des mousses", "Feuilles, branches et mousses sont retirées, au balai ou à la brosse."),
             ("Produit antimousse, puis rinçage", "Le produit est pulvérisé, laissé agir, puis rincé à l’eau claire."),
             ("En option, un traitement hydrofuge", "Il protège la couverture de l’eau. Il ne s’applique pas sur l’ardoise naturelle.")]
DEM_FAQ = [
    ("Combien coûte un démoussage de toiture ?", "De 25 à 35 €/m² avec un brossage manuel, et de 35 à 45 €/m² avec un traitement hydrofuge (La Maison Saint-Gobain, 03/2026). Seule une visite permet un devis fiable."),
    ("Tous les combien faut-il démousser sa toiture ?", "Tous les 2 à 5 ans en général, selon les arbres autour de la maison, l’humidité et le matériau de la couverture (La Maison Saint-Gobain)."),
    ("Quand faire démousser sa toiture ?", "Au printemps ou à l’automne, par temps sec : le produit a besoin de temps pour agir, et la pluie gêne le chantier."),
    ("Faut-il un traitement hydrofuge ?", "C’est une option, utile pour protéger tuiles et béton de l’eau. Il ne s’applique pas sur l’ardoise naturelle, qui se nettoie avec des produits doux et à basse pression."),
    ("Ma toiture est en fibrociment : est-ce différent ?", "Si la couverture peut contenir de l’amiante, des précautions particulières s’imposent et seules des entreprises formées peuvent intervenir. Signalez-le dans votre demande."),
]


def build_demoussage(PF, phone, phone_txt, crumbs, img):
    t = next(x for x in PF.TRADES if x[0] == "toiture")
    blocks = PF.build(lambda a: ("", ""), phone, phone_txt, crumbs, parts=True)
    form = need_preset(blocks["form"].replace('<form class="pf-form"', '<form class="pf-form" data-preset="toiture"', 1), "Démoussage, nettoyage")
    hero = _hero(PF, crumbs, "Démoussage de toiture : devis gratuit", 'Pas cinq <span class="pf-who">couvreurs</span>. <br>Un seul, près de chez vous.',
                 "Décrivez votre toiture en 1 minute.<br>Nous vous rappelons en moins de 5 minutes en semaine, et nous fixons la visite.", form)
    url, alt = img(t[3])
    steps = "".join(f"<li><h3>{a}</h3><p>{b}</p></li>" for a, b in DEM_STEPS)
    steps = f"""<section class="sheet" id="travaux" data-tone="light">
  <div class="grid sp-head"><h2 data-split>Ce que comprend un démoussage</h2><p>Les étapes décrites par {EXT(SG_NET[0], SG_NET[1])}</p></div>
  <div class="pf-split"><figure class="frame pf-ph"><img src="{url}" alt="{t[7]}" width="1200" height="900" loading="lazy"></figure><ul class="pf-checks pf-needs">{steps}</ul></div>
  {_band(PF, "Devis démoussage en 1 minute", "Visite et devis offerts. Sans engagement.")}
</section>"""
    rows = "".join(f'<tr><td>{a}</td><td>{b}</td><td>{EXT("Saint-Gobain, 03/2026", SG_NET[1])}</td></tr>' for a, b in DEM_PRICES)
    price = f"""<section class="sheet" id="prix" data-tone="paper">
  <div class="grid sp-head"><h2 data-split>Prix d’un démoussage de toiture</h2><p>Prix TTC moyens, main-d’œuvre comprise</p></div>
  <div class="pf-refbox"><p class="pf-ref">Démoussage avec brossage manuel&nbsp;: de 25 à 35 €/m². Avec un traitement hydrofuge&nbsp;: de 35 à 45 €/m².</p><p class="pf-src">Source&nbsp;: {EXT(SG_NET[0], SG_NET[1])}</p>
  <table class="pf-tab"><caption>Prix indicatifs TTC, main-d’œuvre comprise</caption><thead><tr><th scope="col">Travaux</th><th scope="col">Prix</th><th scope="col">Source</th></tr></thead><tbody>{rows}</tbody></table>
  <p>Le prix dépend de la surface, du matériau, de l’état de la toiture et de son accès. Seule une visite permet un devis fiable.</p>
  <a class="btn" href="#projet"><span>Obtenir mon devis gratuit</span>{PF.tick()}</a></div>
</section>"""
    when = f"""<section class="sheet pf-ser-short" id="quand" data-tone="light">
  <div class="grid sp-head"><h2 data-split>Quand faire démousser sa toiture&nbsp;?</h2><p>Au printemps ou à l’automne, par temps sec, tous les 2 à 5 ans selon les arbres alentour, l’humidité et le matériau. Profitez-en pour faire vérifier tuiles, faîtage et gouttières.</p></div>
  <p class="pf-upd" style="padding:0 var(--cell)">Mis à jour le <time datetime="@@MAJ@@">@@MAJFR@@</time></p>
</section>"""
    faq = _faq_block(DEM_FAQ, "Démoussage : vos questions", phone, phone_txt)
    others = _others("Autres travaux de toiture", [("Devis toiture", "/devis-travaux/toiture/"), ("Fuite de toiture en urgence", URGENCE["path"]),
                                                    ("Devis charpente", "/devis-travaux/charpente/")], more=("Tous les devis de travaux", "/devis-travaux/"))
    return "\n\n".join([hero, steps, price, when, blocks["promise"], faq, others, blocks["end"]]), DEM_FAQ


def sub_schema(SITE, PF, faq_ld, bc_ld, page, faq_rows, service, crumb_items, howto=None):
    p = page["path"]
    graph = [
        {"@type": "WebPage", "@id": SITE + p, "url": SITE + p, "name": page["title"], "description": page["desc"], "inLanguage": "fr-FR",
         "dateModified": "@@MAJ@@", "isPartOf": {"@id": SITE + "/#website"}, "publisher": {"@id": SITE + "/#org"}},
        {"@type": "Service", "name": service, "serviceType": f"Mise en relation avec un couvreur : {service.lower()}", "url": SITE + p,
         "areaServed": {"@type": "Country", "name": "France"}, "audience": {"@type": "Audience", "audienceType": "Propriétaires"},
         "provider": {"@type": "Organization", "@id": SITE + "/#org", "name": "Bartier & Co", "url": SITE + "/"},
         "offers": {"@type": "Offer", "price": "0", "priceCurrency": "EUR", "description": "Gratuit pour le particulier : mise en relation, visite et devis de l'artisan"}},
        faq_ld([(q, CLEAN(a)) for q, a in faq_rows]), bc_ld(*crumb_items)]
    if howto:
        graph.append({"@type": "HowTo", "name": howto[0], "step": [{"@type": "HowToStep", "position": i, "name": a, "text": CLEAN(b)} for i, (a, b) in enumerate(howto[1], 1)]})
    return PF.link_graph(SITE, p, {"@context": "https://schema.org", "@graph": graph})


# ——— Métier à <ville> ———
def city_path(PF, key, c):
    return f"/devis-travaux/{PF.SLUG[key]}/{c['slug']}/"


def build_trade_city(PF, VL, phone, phone_txt, crumbs, key, c, img):
    T = CITY_TRADES[key]
    t = next(x for x in PF.TRADES if x[0] == key)
    av = VL.a_(c)
    blocks = PF.build(lambda a: ("", ""), phone, phone_txt, crumbs, parts=True)
    form = blocks["form"].replace('<form class="pf-form"', f'<form class="pf-form" data-preset="{key}"', 1).replace('placeholder="Ex. 80000"', f'placeholder="Ex. {c["cp"]}"', 1)
    hero = _hero(PF, crumbs, T["h1"].format(a=av), f'Pas cinq <span class="pf-who">{T["who"]}</span>. <br>Un seul, près de chez vous.',
                 "Décrivez vos travaux en 1 minute.<br>Nous vous rappelons en moins de 5 minutes en semaine, et nous fixons la visite.", form)
    # Les faits locaux vérifiés du métier
    paras = "".join(f"<p>{VL._contact(p)}</p>" for p in c["trades"][key])
    figs = "".join(f'<li><b>{a}</b> <span>{b}</span> <span class="vl-fsrc">{src}</span></li>' for a, b, src in c["figures"])
    ver = VL.verified(c)
    url, _ = img(t[3])
    ph = f'<img src="{url}" alt="{t[7]}" width="1200" height="900" loading="lazy">'
    if c.get("photo") and (__import__("pathlib").Path(__file__).resolve().parent.parent / "assets" / "villes" / f"{c['slug']}-1200.webp").exists():
        srcset = ", ".join(f"/assets/villes/{c['slug']}-{w}.webp {w}w" for w in (800, 1200, 1600))
        ph = f'<img srcset="{srcset}" sizes="(max-width: 760px) 100vw, 50vw" src="/assets/villes/{c["slug"]}-1200.webp" alt="{c["photo"]["alt"]}" width="1200" height="900" loading="lazy" style="object-fit:cover">'
    local = f"""<section class="sheet" id="local" data-tone="light">
  <div class="grid sp-head"><h2 data-split>{T["local_h2"].format(a=av)}</h2><p>Règles et repères vérifiés sur les sources officielles</p></div>
  <div class="pf-split"><figure class="frame pf-ph">{ph}</figure><div class="mc-local">{paras}
  <p class="vl-src">Sources officielles vérifiées le <time datetime="{ver[0]}">{ver[1]}</time>, par <a class="link" href="/qui-sommes-nous/#charles">Charles Le Cottier</a>.</p></div></div>
  <ul class="pf-proms vl-figs mc-figs">{figs}</ul>
</section>"""
    # Démarches locales : pour la toiture, on écarte celles qui ne concernent que la façade
    st = [(a, b) for a, b in c["steps"] if key != "toiture" or not ROOF_ONLY.search(a + " " + b)]
    steps = ""
    if st:
        items = "".join(f"<li><h3>{a}</h3><p>{VL._contact(b)}</p></li>" for a, b in st)
        steps = f"""<section class="sheet" id="demarches" data-tone="paper">
  <div class="grid sp-head"><h2 data-split>Les démarches {av}</h2><p>Avant de signer le devis</p></div>
  <ol class="pf-howto mc-steps">{items}</ol>
</section>"""
    P = PF.PAGES[key]
    needs = "".join(f"<li><h3>{a}</h3><p>{b}</p></li>" for a, b in P["needs"])
    needs = f"""<section class="sheet" id="travaux" data-tone="light">
  <div class="grid sp-head"><h2 data-split>{P["h2"]} {av}</h2><p>{t[6]}</p></div>
  <ul class="pf-checks pf-needs mc-needs">{needs}</ul>
  {_band(PF, T["link"].format(a=av) + " en 1 minute", "Visite et devis offerts. Sans engagement.")}
</section>"""
    price = f"""<section class="sheet" id="prix" data-tone="paper">
  <div class="grid sp-head"><h2 data-split>{P["price_h2"]}</h2><p>Moyennes en France, à affiner lors de la visite</p></div>
  <div class="pf-refbox"><p class="pf-ref">{PF.REF[key][0]}</p><p class="pf-src">Source&nbsp;: {PF.REF[key][1]}</p>{PF.detail_table(key)}<p>Seule une visite permet un devis fiable.</p>
  <a class="btn" href="#projet"><span>Obtenir mon devis gratuit</span>{PF.tick()}</a></div>
</section>"""
    faq_rows = [(q, VL._contact(a)) for q, a in c["faq"] if re.search(T["faq_kw"], q + " " + a, re.I)]
    faq_rows += [(f"Intervenez-vous partout {av} ?", "Nous vous mettons en relation avec l’artisan partenaire qui couvre votre commune. "
                  "Si aucun ne la couvre, nous vous le disons dès l’appel et votre demande n’est transmise à personne.")]
    faq_rows += [qa for qa in PF.trade_faq(key)[:2]]
    faq = _faq_block(faq_rows, f"{t[5]} {av} : vos questions", phone, phone_txt)
    near = [x for x in VL.voisines(c, 6)]
    links = [(T["link"].format(a=VL.a_(x)), city_path(PF, key, x)) for x in near]
    links += [(f"Tous les travaux {av}", VL.path(c)), (P["title"].split(" :")[0] if key != "toiture" else "Devis toiture", f"/devis-travaux/{PF.SLUG[key]}/")]
    others = _others("Ailleurs et autres travaux", links, more=("Tous les devis de travaux", "/devis-travaux/"))
    return "\n\n".join([hero, local, blocks["promise"], needs, steps, price, faq, others, blocks["end"]]), faq_rows


def trade_city_meta(PF, VL, key, c):
    T = CITY_TRADES[key]
    av = VL.a_(c)
    return T["title"].format(a=av), T["desc"].format(a=av)


def trade_city_schema(SITE, PF, VL, faq_ld, bc_ld, key, c, faq_rows):
    T = CITY_TRADES[key]
    p = city_path(PF, key, c)
    title, desc = trade_city_meta(PF, VL, key, c)
    t = next(x for x in PF.TRADES if x[0] == key)
    city = {"@type": "City", "name": c["name"], "sameAs": [c["wiki"], f"https://www.wikidata.org/wiki/{c['wikidata']}"],
            "geo": {"@type": "GeoCoordinates", "latitude": c["lat"], "longitude": c["lon"]},
            "containedInPlace": {"@type": "AdministrativeArea", "name": c["dept"], "identifier": c["depcode"]}}
    graph = [
        {"@type": "WebPage", "@id": SITE + p, "url": SITE + p, "name": title, "description": desc, "inLanguage": "fr-FR", "dateModified": "@@MAJ@@",
         "lastReviewed": VL.verified(c)[0], "isPartOf": {"@id": SITE + "/#website"}, "publisher": {"@id": SITE + "/#org"}, "about": city},
        {"@type": "Service", "name": T["link"].format(a=VL.a_(c)), "serviceType": f"Mise en relation avec un artisan : {T['service'].lower()}", "url": SITE + p,
         "description": CLEAN(" ".join(c["trades"][key]))[:300], "areaServed": city, "audience": {"@type": "Audience", "audienceType": "Propriétaires"},
         "provider": {"@type": "Organization", "@id": SITE + "/#org", "name": "Bartier & Co", "url": SITE + "/"},
         "offers": {"@type": "Offer", "price": "0", "priceCurrency": "EUR", "description": "Gratuit pour le particulier : mise en relation, visite et devis de l'artisan"}},
        faq_ld([(q, CLEAN(a)) for q, a in faq_rows]),
        bc_ld(("Devis travaux", "/devis-travaux/"), (t[1], f"/devis-travaux/{PF.SLUG[key]}/"), (c["name"], p))]
    return PF.link_graph(SITE, p, {"@context": "https://schema.org", "@graph": graph})


CSS = """<style id="mc-css">
.pf-big .pf-acc{color:var(--accent)}
.mc-local p{margin:0 0 1em;max-width:62ch;line-height:1.6}
.mc-local .vl-src{margin-top:1.2em;font-size:.85rem;color:var(--muted)}
.mc-figs{margin-top:clamp(28px,3vw,44px)}
.mc-figs li{border-top-color:var(--rule)}
.mc-figs b{color:var(--ink);font-size:clamp(2rem,3.4vw,3.2rem)}
.mc-figs span{color:var(--muted)}
.mc-figs .vl-fsrc{color:var(--muted)}
.mc-figs .vl-fsrc a{color:inherit;text-decoration:underline;text-underline-offset:3px}
.mc-steps{counter-reset:mc}
</style>"""

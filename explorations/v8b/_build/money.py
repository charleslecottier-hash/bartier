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
CITY_TRADES.update({
    "fenetres": dict(h1="Remplacement de fenêtres {a} : devis gratuit", title="Remplacement de fenêtres {a} : devis gratuit",
                     desc="Un menuisier {a} vient chiffrer vos fenêtres, porte d’entrée, baie vitrée ou volets. Règles locales vérifiées, visite et devis gratuits.",
                     local_h2="Vos fenêtres {a} : ce qu’il faut savoir", link="Fenêtres {a}", service="Menuiserie extérieure", who="menuisiers",
                     faq_kw=r"fenêtre|menuiser|pvc|volet|vitrage|porte|baie|huisserie"),
    "charpente": dict(h1="Charpentier {a} : devis charpente gratuit", title="Charpentier {a} : devis charpente gratuit",
                      desc="Un charpentier {a} vient chiffrer : réparation, renfort, traitement du bois, surélévation. Règles locales vérifiées, visite et devis gratuits.",
                      local_h2="Votre charpente {a} : ce qu’il faut savoir", link="Charpentier {a}", service="Charpente", who="charpentiers",
                      faq_kw=r"charpent|termite|mérule|capricorne|insecte|surélévation"),
    "isolation": dict(h1="Isolation {a} : combles et murs, devis gratuit", title="Isolation {a} : combles et murs, devis gratuit",
                      desc="Une entreprise d’isolation {a} vient chiffrer vos combles, vos murs ou votre toiture. Aides locales et règles vérifiées, visite et devis gratuits.",
                      local_h2="Isoler son logement {a} : ce qu’il faut savoir", link="Isolation {a}", service="Isolation", who="artisans",
                      faq_kw=r"isol|combles|thermique|chaleur|froid|dpe|énergétique|aide|rénov"),
})
HUB = {"toiture": "Devis toiture", "facade": "Devis ravalement de façade", "fenetres": "Devis fenêtres et portes", "charpente": "Devis charpente", "isolation": "Devis isolation"}
AIDES_FOR = ("isolation", "fenetres")  # métiers dont les aides locales sont utiles sur la page
FACADE_STEPS = ("facade", "isolation")  # les autres métiers n'affichent pas les démarches propres au ravalement
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
  <ul class="pf-checks pf-needs mc-list">{honest}</ul>
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


def sub_schema(SITE, PF, faq_ld, bc_ld, page, faq_rows, service, crumb_items, howto=None, pro="un couvreur"):
    p = page["path"]
    graph = [
        {"@type": "WebPage", "@id": SITE + p, "url": SITE + p, "name": page["title"], "description": page["desc"], "inLanguage": "fr-FR",
         "dateModified": "@@MAJ@@", "isPartOf": {"@id": SITE + "/#website"}, "publisher": {"@id": SITE + "/#org"}},
        {"@type": "Service", "name": service, "serviceType": f"Mise en relation avec {pro} : {service.lower()}", "url": SITE + p,
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
    st = [(a, b) for a, b in c["steps"] if key in FACADE_STEPS or not ROOF_ONLY.search(a + " " + b)]
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
    links += [(f"Tous les travaux {av}", VL.path(c)), (HUB[key], f"/devis-travaux/{PF.SLUG[key]}/")]
    others = _others("Ailleurs et autres travaux", links, more=("Tous les devis de travaux", "/devis-travaux/"))
    aides = ""
    if key in AIDES_FOR and c.get("aides"):
        a0, b0 = c["aides"][0]
        items = f'<li class="vl-adv"><div><p class="vl-adv-k">Conseil public, gratuit et neutre</p><h3>{a0}</h3><p>{VL._contact(b0)}</p></div></li>'
        items += "".join(f"<li><h3>{a}</h3><p>{VL._contact(b)}</p></li>" for a, b in c["aides"][1:])
        aides = f"""<section class="sheet" id="aides" data-tone="light">
  <div class="grid sp-head"><h2 data-split>Les aides {av}</h2><p>Les aides de l’État ne sont versées que si l’entreprise est RGE : demandez-le à l’artisan lors de la visite</p></div>
  <ul class="pf-checks vl-trades vl-aides">{items}</ul>
</section>"""
    return "\n\n".join([hero, local, blocks["promise"], needs, steps, aides, price, faq, others, blocks["end"]]), faq_rows


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
.mc-list,.mc-needs{padding-inline:var(--cell)}
</style>"""


# ——— Sous-services, sur un modèle commun ———
SG = lambda label, url, date: (f"La Maison Saint-Gobain, {date}", url)
SG_PORTE = SG("", "https://www.lamaisonsaintgobain.fr/guides-travaux/menuiseries-exterieures/prix-porte-d-entree", "12/2025")
SG_BAIE = SG("", "https://www.lamaisonsaintgobain.fr/guides-travaux/menuiseries-exterieures/comment-choisir-ma-baie-vitree", "05/2026")
SG_ITE = SG("", "https://www.lamaisonsaintgobain.fr/guides-travaux/isolation/prix-isolation-thermique-par-l-exterieur-ite-au-m2", "10/2026")
QE_ZING = ("QuelleEnergie", "https://www.quelleenergie.fr/economies-energie/corps-de-metier/trouver-couvreur-zingueur")

SUBS = [
    dict(key="toiture", path="/devis-travaux/toiture/gouttieres/", crumb="Gouttières", need="Réparation, tuiles, zinguerie", pro="un couvreur zingueur",
         title="Gouttières : remplacement et devis gratuit près de chez vous", kw="Gouttières : devis gratuit",
         desc="Changer ou réparer vos gouttières : un couvreur zingueur de votre secteur vient chiffrer. Zinc, acier ou cuivre, chéneaux et descentes. Visite et devis gratuits.",
         service="Pose et réparation de gouttières",
         what_h2="Ce que fait le couvreur zingueur", what_sub="Gouttières, chéneaux et descentes d’eau pluviale",
         what=[("Remplacement des gouttières", "Dépose de l’ancienne installation, pose des gouttières neuves, raccords et descentes."),
               ("Réparation", "Fuite à une jonction, gouttière qui déborde ou qui s’affaisse, crochet arraché."),
               ("Chéneaux et noues", "Les pièces qui recueillent l’eau entre deux pans de toit ou au pied d’un mur."),
               ("Descentes d’eau pluviale", "Les tuyaux qui conduisent l’eau au sol ou au réseau.")],
         price_h2="Prix d’une gouttière", price_ref="Gouttière seule, hors pose, au mètre linéaire&nbsp;: 10 à 15 € en zinc, 15 à 20 € en acier, 25 à 35 € en cuivre.",
         price_src=QE_ZING, price_cap="Prix indicatifs de la gouttière seule, hors pose", price_rows=[("Zinc", "10 à 15 €/m linéaire"), ("Acier", "15 à 20 €/m linéaire"), ("Cuivre", "25 à 35 €/m linéaire")],
         price_note="La pose, la dépose de l’ancienne installation et l’accès (nacelle ou échafaudage) s’ajoutent : le couvreur les chiffre lors de la visite.",
         local=True,
         faq=[("Combien coûte une gouttière ?", "Hors pose, comptez 10 à 15 € le mètre linéaire en zinc, 15 à 20 € en acier et 25 à 35 € en cuivre (QuelleEnergie). La pose et l’accès au toit sont chiffrés lors de la visite."),
              ("Couvreur ou zingueur : qui appeler ?", "Le couvreur zingueur pose et répare les gouttières, chéneaux et descentes. C’est lui que nous vous envoyons."),
              ("Faut-il une autorisation pour changer ses gouttières ?", "À l’identique, en général non. En secteur protégé, le matériau peut être imposé : zinc ou cuivre, et pas de PVC, dans plusieurs villes. Renseignez-vous en mairie avant de commander.")]),
    dict(key="isolation", path="/devis-travaux/isolation/exterieur/", crumb="Par l’extérieur", need="Murs par l’extérieur", pro="une entreprise d’isolation",
         title="Isolation par l’extérieur : devis gratuit près de chez vous", kw="Isolation par l’extérieur : devis gratuit",
         desc="Isolation thermique par l’extérieur : 130 à 215 €/m² posée (La Maison Saint-Gobain). Une entreprise de votre secteur vient chiffrer. Visite et devis gratuits.",
         service="Isolation thermique par l’extérieur",
         what_h2="Sous enduit ou sous bardage", what_sub="Les deux techniques d’isolation par l’extérieur",
         what=[("Sous enduit", "L’isolant est fixé sur le mur puis recouvert d’un enduit : 130 à 190 €/m², fourni et posé."),
               ("Sous bardage", "L’isolant est posé sur une ossature puis habillé de bois, de métal ou de composite : 140 à 215 €/m², fourni et posé."),
               ("Avec un ravalement", "C’est le bon moment : l’échafaudage sert aux deux chantiers. <a class=\"link\" href=\"/devis-travaux/ravalement-facade/\">Devis ravalement</a>"),
               ("Les démarches", "L’isolation par l’extérieur change l’aspect de la façade : une déclaration préalable en mairie est en général nécessaire.")],
         price_h2="Prix d’une isolation par l’extérieur", price_ref="Isolation thermique par l’extérieur&nbsp;: de 130 à 215 €/m², fourniture et pose comprises.",
         price_src=SG_ITE, price_cap="Prix indicatifs au m², fourniture et pose comprises",
         price_rows=[("Sous enduit", "130 à 190 €/m²"), ("Sous bardage", "140 à 215 €/m²"), ("Pour comparer : isolation par l’intérieur", "80 à 130 €/m²")],
         price_note="TVA à 5,5 % dans un logement achevé depuis plus de deux ans. Les aides (MaPrimeRénov’, primes CEE) ne sont versées que si l’entreprise est RGE : demandez-le à l’artisan lors de la visite.",
         faq=[("Combien coûte une isolation par l’extérieur ?", "De 130 à 215 €/m², fourniture et pose comprises : 130 à 190 €/m² sous enduit, 140 à 215 €/m² sous bardage (La Maison Saint-Gobain, 10/2026)."),
              ("Par l’extérieur ou par l’intérieur ?", "Par l’intérieur, c’est moins cher (80 à 130 €/m²) mais on perd de la surface habitable. Par l’extérieur, on garde ses pièces intactes et on supprime les ponts thermiques."),
              ("Faut-il une autorisation ?", "Oui, en général une déclaration préalable en mairie, car l’aspect de la façade change. En secteur protégé, l’architecte des Bâtiments de France donne son avis."),
              ("Quelles aides pour isoler par l’extérieur ?", "MaPrimeRénov’ et les primes CEE, si les travaux sont faits par une entreprise RGE. Un conseiller France Rénov’ vous dit gratuitement à quoi vous avez droit.")]),
    dict(key="fenetres", path="/devis-travaux/fenetres/porte-entree/", crumb="Porte d’entrée", need="Porte d’entrée", pro="un menuisier",
         title="Porte d’entrée posée : devis gratuit près de chez vous", kw="Porte d’entrée : devis gratuit",
         desc="Porte d’entrée posée : environ 1 500 € en PVC, 2 000 € en bois, 3 000 € en aluminium (La Maison Saint-Gobain). Un menuisier de votre secteur vient chiffrer.",
         service="Pose de porte d’entrée",
         what_h2="Quel matériau choisir ?", what_sub="Les prix moyens d’une porte simple, pose comprise",
         what=[("PVC, environ 1 500 €", "Le plus économique, une isolation correcte et aucun entretien."),
               ("Bois, environ 2 000 €", "Du cachet et une bonne durée de vie, avec un entretien tous les 5 à 10 ans."),
               ("Acier, environ 2 000 €", "Le même budget moyen que le bois, pose comprise."),
               ("Aluminium, environ 3 000 €", "Le plus cher des quatre, avec des profils fins.")],
         price_h2="Prix d’une porte d’entrée", price_ref="Porte d’entrée standard, pose comprise&nbsp;: de 1&nbsp;500 à 4&nbsp;000 € selon le matériau et les options.",
         price_src=SG_PORTE, price_cap="Prix moyens, pose comprise",
         price_rows=[("PVC", "1 500 € (2 000 € avec paroi fixe)"), ("Bois", "2 000 € (3 000 € avec paroi fixe)"), ("Acier", "2 000 € (3 000 € avec paroi fixe)"),
                     ("Aluminium", "3 000 € (4 000 € avec paroi fixe)"), ("Porte blindée", "1 400 à 4 100 €"), ("Porte haute isolation", "1 500 à 4 800 €"),
                     ("Dépose de l’ancienne porte", "80 à 150 €")],
         price_note="Sur mesure, comptez 15 à 25 % de plus pour un petit écart avec les dimensions standard (215 × 90 cm).",
         faq=[("Combien coûte une porte d’entrée posée ?", "Environ 1 500 € en PVC, 2 000 € en bois ou en acier et 3 000 € en aluminium pour une porte simple, pose comprise (La Maison Saint-Gobain, 12/2025)."),
              ("Combien de temps dure la pose ?", "4 à 6 heures pour une installation standard, selon La Maison Saint-Gobain."),
              ("Faut-il une autorisation pour changer sa porte d’entrée ?", "À l’identique, en général non. Changer l’aspect, le matériau ou la couleur demande une déclaration préalable en mairie, et davantage en secteur protégé.")]),
    dict(key="fenetres", path="/devis-travaux/fenetres/baie-vitree/", crumb="Baie vitrée", need="Baie vitrée", pro="un menuisier",
         title="Baie vitrée posée : devis gratuit près de chez vous", kw="Baie vitrée : devis gratuit",
         desc="Baie vitrée coulissante posée : 1 600 à 2 200 € en PVC, 2 400 à 3 300 € en aluminium (La Maison Saint-Gobain). Un menuisier de votre secteur vient chiffrer.",
         service="Pose de baie vitrée",
         what_h2="Coulissante, à galandage ou battante", what_sub="Trois façons d’ouvrir une baie vitrée",
         what=[("Coulissante", "Les vantaux glissent l’un devant l’autre : le modèle le plus courant."),
               ("À galandage", "Les vantaux disparaissent dans le mur : il faut prévoir l’épaisseur de cloison."),
               ("Battante", "Elle s’ouvre comme une porte-fenêtre."),
               ("Création d’ouverture", "Créer ou agrandir une ouverture touche souvent un mur porteur : il faut l’étude d’un professionnel et une déclaration préalable en mairie.")],
         price_h2="Prix d’une baie vitrée", price_ref="Baie vitrée coulissante de 215 × 240 cm, double vitrage, fournie et posée&nbsp;: de 1&nbsp;600 à 3&nbsp;600 € TTC selon le matériau.",
         price_src=SG_BAIE, price_cap="Prix TTC fourni et posé, baie coulissante 215 × 240 cm",
         price_rows=[("PVC", "1 600 à 2 200 €"), ("Aluminium", "2 400 à 3 300 €"), ("Bois", "2 600 à 3 600 €")],
         price_note="Une création d’ouverture dans un mur coûte davantage : le menuisier la chiffre lors de la visite.",
         faq=[("Combien coûte une baie vitrée posée ?", "Pour une baie coulissante de 215 × 240 cm en double vitrage : 1 600 à 2 200 € en PVC, 2 400 à 3 300 € en aluminium, 2 600 à 3 600 € en bois, TTC et posée (La Maison Saint-Gobain, 05/2026)."),
              ("PVC ou aluminium ?", "Le PVC est le plus économique. L’aluminium permet des profils fins et de grandes baies."),
              ("Faut-il une autorisation ?", "Remplacer à l’identique ne demande en général rien. Créer une ouverture ou changer l’aspect de la façade demande une déclaration préalable en mairie.")]),
]
PARENT = {"toiture": ("Toiture", "/devis-travaux/toiture/"), "isolation": ("Isolation", "/devis-travaux/isolation/"), "fenetres": ("Fenêtres et portes", "/devis-travaux/fenetres/")}


def gutter_local(PF, VL):
    """Règles des gouttières relevées dans les fiches ville vérifiées."""
    rows = []
    for c in VL.CITIES:
        for p in c["trades"]["toiture"]:
            s = re.sub(r"\s*\([^()]*<a [^)]*\)", "", p)  # la source reste sur la page de la ville
            if re.search(r"gouttières?[^.]*(zinc|cuivre|PVC|plastique)|descentes en PVC", CLEAN(s), re.I):
                rows.append((c, CLEAN(s).strip()))
    items = "".join(f'<li><h3><a class="link" href="{city_path(PF, "toiture", c)}">Couvreur {VL.a_(c)}</a></h3><p>{txt}</p></li>' for c, txt in rows)
    return f"""<section class="sheet" id="villes" data-tone="paper">
  <div class="grid sp-head"><h2 data-split>Ce que les villes imposent</h2><p>Dans les secteurs protégés, le matériau des gouttières est souvent fixé. Relevé dans nos fiches ville vérifiées</p></div>
  <ul class="pf-checks pf-needs mc-list">{items}</ul>
</section>""" if rows else ""


def build_sub(PF, VL, phone, phone_txt, crumbs, img, S):
    t = next(x for x in PF.TRADES if x[0] == S["key"])
    blocks = PF.build(lambda a: ("", ""), phone, phone_txt, crumbs, parts=True)
    form = need_preset(blocks["form"].replace('<form class="pf-form"', f'<form class="pf-form" data-preset="{S["key"]}"', 1), S["need"])
    hero = _hero(PF, crumbs, S["kw"], f'Pas cinq <span class="pf-who">{t[2]}</span>. <br>Un seul, près de chez vous.',
                 "Décrivez vos travaux en 1 minute.<br>Nous vous rappelons en moins de 5 minutes en semaine, et nous fixons la visite.", form)
    url, _ = img(t[3])
    ph = (f'srcset="{PF.ISO_SRCSET}" sizes="(max-width: 760px) 100vw, 50vw" src="{PF.ISO_PHOTO}-1400x1050.webp"' if S["key"] == "isolation" else f'src="{url}"')
    what = "".join(f"<li><h3>{a}</h3><p>{b}</p></li>" for a, b in S["what"])
    what = f"""<section class="sheet" id="travaux" data-tone="light">
  <div class="grid sp-head"><h2 data-split>{S["what_h2"]}</h2><p>{S["what_sub"]}</p></div>
  <div class="pf-split"><figure class="frame pf-ph"><img {ph} alt="{t[7]}" width="1200" height="900" loading="lazy"></figure><ul class="pf-checks pf-needs">{what}</ul></div>
  {_band(PF, S["kw"].split(" :")[0] + " : devis en 1 minute", "Visite et devis offerts. Sans engagement.")}
</section>"""
    n, u = S["price_src"]
    rows = "".join(f'<tr><td>{a}</td><td>{b}</td><td>{EXT(n.replace("La Maison ", ""), u)}</td></tr>' for a, b in S["price_rows"])
    price = f"""<section class="sheet" id="prix" data-tone="paper">
  <div class="grid sp-head"><h2 data-split>{S["price_h2"]}</h2><p>{S["price_cap"]}</p></div>
  <div class="pf-refbox"><p class="pf-ref">{S["price_ref"]}</p><p class="pf-src">Source&nbsp;: {EXT(n, u)}</p>
  <table class="pf-tab"><caption>{S["price_cap"]}</caption><thead><tr><th scope="col">Travaux</th><th scope="col">Prix</th><th scope="col">Source</th></tr></thead><tbody>{rows}</tbody></table>
  <p>{S["price_note"]} Seule une visite permet un devis fiable.</p>
  <a class="btn" href="#projet"><span>Obtenir mon devis gratuit</span>{PF.tick()}</a></div>
  <p class="pf-upd" style="padding:0 var(--cell)">Mis à jour le <time datetime="@@MAJ@@">@@MAJFR@@</time></p>
</section>"""
    local = gutter_local(PF, VL) if S.get("local") else ""
    faq = _faq_block(S["faq"], f'{S["crumb"]} : vos questions', phone, phone_txt)
    sibs = [(x["crumb"], x["path"]) for x in SUBS if x["key"] == S["key"] and x["path"] != S["path"]]
    links = [(HUB[S["key"]], f"/devis-travaux/{PF.SLUG[S['key']]}/")] + sibs + [(CITY_TRADES[S["key"]]["link"].format(a=VL.a_(c)), city_path(PF, S["key"], c)) for c in VL.CITIES[:6]]
    others = _others("Autres travaux", links, more=("Tous les devis de travaux", "/devis-travaux/"))
    return "\n\n".join([hero, what, price, local, blocks["promise"], faq, others, blocks["end"]]), S["faq"]

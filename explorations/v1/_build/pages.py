"""Génère les pages Google Ads, Meta Ads, Qui sommes-nous, le blog et les fichiers SEO/GEO.

En-tête, pied de page et formulaire sont repris de index.html.

    python3 _build/pages.py
"""
import html
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
HOME = (ROOT / "index.html").read_text(encoding="utf-8")
SITE = "https://bartierandco.com"
TODAY = "2026-11-17"
TODAY_FR = "17 novembre 2026"
NB = " "


def between(start, end):
    i = HOME.index(start)
    return HOME[i:HOME.index(end, i) + len(end)]


def absolutize(block):
    block = block.replace('href="#top"', 'href="/"')
    return re.sub(r'href="#(?!secteur|contenu)([\w-]+)"', r'href="/#\1"', block)


HEADER = absolutize(between('<a class="skip"', "</header>"))
FOOTER = absolutize(between('<footer class="site-footer">', "</footer>"))
FORM = between("<!-- Formulaire -->", "</section>").replace("<!-- Formulaire -->", "")
ENGAGEMENTS = between('<ul class="en">', "</ul>")
GUARANTEE = between('<div class="guarantee">', "</div>")
MOBILE_CTA = between('<a class="mobile-cta', "</a>")
HEAD_SCRIPT = between("<script>(function(d)", "</script>")


def fr(text):
    """Apostrophes typographiques et espaces insécables avant ; : ? !"""
    text = text.replace("'", "’")
    return re.sub(r" ([;:?!»])", NB + r"\1", text).replace("« ", "«" + NB)


def page(path, title, description, body, nav=None, schema=None):
    header = HEADER
    if nav:
        header = header.replace(f'<a href="{nav}">', f'<a href="{nav}" aria-current="page">', 1)
    ld = f'\n<script type="application/ld+json">{json.dumps(schema, ensure_ascii=False)}</script>' if schema else ""
    doc = f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(fr(title), quote=False)}</title>
<meta name="description" content="{html.escape(fr(description))}">
<meta name="robots" content="noindex">
<meta name="theme-color" content="#0B0D12">
<link rel="canonical" href="{SITE}{path}">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="preload" href="/fonts/general-sans-500.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/fonts/manrope-400.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/styles.css">
{HEAD_SCRIPT}{ld}
</head>
<body>
{header}

<main id="contenu">
{fr(body)}
</main>

{FOOTER}

{MOBILE_CTA}

<script src="/script.js" defer></script>
</body>
</html>
"""
    out = ROOT / path.strip("/") / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(doc, encoding="utf-8")
    return path


def crumbs(*items):
    parts = ['<a href="/">Accueil</a>']
    for label, href in items[:-1]:
        parts.append(f'<a href="{href}">{label}</a>')
    parts.append(f'<span aria-current="page">{items[-1][0]}</span>')
    return '<nav class="crumbs" aria-label="Fil d\'Ariane">' + '<span aria-hidden="true">/</span>'.join(parts) + "</nav>"


def breadcrumb_ld(*items):
    elems = [{"@type": "ListItem", "position": 1, "name": "Accueil", "item": SITE + "/"}]
    for i, (name, href) in enumerate(items, 2):
        elems.append({"@type": "ListItem", "position": i, "name": name, "item": SITE + href})
    return {"@type": "BreadcrumbList", "itemListElement": elems}


def faq_block(items, title="Questions fréquentes"):
    rows = "\n".join(f"      <details><summary>{q}</summary><p>{a}</p></details>" for q, a in items)
    return f"""<section class="section" aria-labelledby="fq-h">
  <div class="wrap faq-grid">
    <div class="head"><h2 id="fq-h">{title}</h2></div>
    <div class="faq">
{rows}
    </div>
  </div>
</section>"""


def faq_ld(items):
    clean = lambda t: re.sub("<[^>]+>", "", fr(t))
    return {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": clean(q), "acceptedAnswer": {"@type": "Answer", "text": clean(a)}} for q, a in items]}


def hero(kicker, h1, lead, crumb, cta2=None):
    second = f'<a class="btn btn-outline" href="{cta2[1]}">{cta2[0]}</a>' if cta2 else ""
    return f"""<section class="page-hero" aria-labelledby="h1">
  <div class="wrap">
    {crumb}
    <p class="kicker">{kicker}</p>
    <h1 id="h1">{h1}</h1>
    <p class="lead">{lead}</p>
    <div class="ctas">
      <a class="btn btn-white" href="#secteur">Vérifier mon secteur <span class="go" aria-hidden="true">→</span></a>
      {second}
    </div>
  </div>
</section>"""


def cols(items, kicker, title, grey=False, sub=""):
    lis = "\n".join(f'      <li><span class="n">{i:02d}</span><h3>{h}</h3><p>{p}</p></li>' for i, (h, p) in enumerate(items, 1))
    sub = f'<p class="sub">{sub}</p>' if sub else ""
    return f"""<section class="section{' section-grey' if grey else ''}">
  <div class="wrap">
    <div class="head"><p class="kicker">{kicker}</p><h2>{title}</h2>{sub}</div>
    <ul class="cols">
{lis}
    </ul>
  </div>
</section>"""


def split_list(kicker, title, sub, items, grey=False, no=False):
    lis = "\n".join(f"        <li>{x}</li>" for x in items)
    return f"""<section class="section{' section-grey' if grey else ''}">
  <div class="wrap split2">
    <div><p class="kicker">{kicker}</p><h2>{title}</h2><p class="sub">{sub}</p></div>
    <ul class="list-x{' is-no' if no else ''}">
{lis}
    </ul>
  </div>
</section>"""


ENG_SECTION = f"""<section class="section section-grey" aria-labelledby="en-h">
  <div class="wrap">
    <div class="head"><p class="kicker">Engagements</p><h2 id="en-h">Écrits dans le contrat.</h2></div>
    {ENGAGEMENTS}
    {GUARANTEE}
  </div>
</section>"""

COMPARE = """<section class="section">
  <div class="wrap">
    <div class="head"><p class="kicker">Google ou Meta</p><h2>Deux canaux, deux demandes différentes.</h2></div>
    <div class="table" role="table" aria-label="Google Ads et Meta Ads">
      <div class="t-row t-head" role="row"><span role="columnheader"></span><span role="columnheader">Google Ads</span><span role="columnheader">Meta Ads</span></div>
      <div class="t-row" role="row"><span role="rowheader">La demande</span><span role="cell">Le propriétaire cherche déjà</span><span role="cell">Le propriétaire n'a pas encore cherché</span></div>
      <div class="t-row" role="row"><span role="rowheader">Typiquement</span><span role="cell">Urgences, projets mûrs</span><span role="cell">Rénovation, entretien, projets à venir</span></div>
      <div class="t-row" role="row"><span role="rowheader">Le volume</span><span role="cell">Limité aux recherches locales</span><span role="cell">Tous les propriétaires du rayon</span></div>
      <div class="t-row" role="row"><span role="rowheader">Le point clé</span><span role="cell">Filtrer les recherches inutiles</span><span role="cell">Qualifier au téléphone</span></div>
    </div>
  </div>
</section>"""

# ——— Google Ads ———
GOOGLE_FAQ = [
    ("Google Ads ou Meta, lequel choisir ?", "Les deux se complètent. Google capte ceux qui cherchent déjà, Meta ceux qui y pensent. Nous recommandons l'un, l'autre ou les deux selon votre métier et votre secteur, pendant l'appel."),
    ("Quel budget prévoir ?", "Il dépend de votre métier et de la concurrence dans votre secteur. Nous l'estimons avec vous avant de démarrer. Vous le payez directement à Google."),
    ("Le compte Google Ads est-il à moi ?", "Oui. Le compte est à votre nom, vous gardez l'accès et l'historique, même si vous arrêtez."),
    ("Qui rappelle les demandes ?", "Notre équipe, en moins de 5 minutes, en semaine de 8 h à 19 h. Vous ne recevez que des visites vérifiées, directement dans votre agenda."),
    ("Sur quelles recherches apparaissez-vous ?", "Sur les recherches de votre métier dans vos communes, comme « couvreur » suivi du nom de la ville. Les recherches inutiles sont exclues : gratuit, pas cher, emploi, formation, bricolage."),
    ("Combien de temps avant les premières demandes ?", "L'intégration prend 24 à 48 heures après notre appel, puis 3 à 5 jours pour lancer vos annonces. Le rythme des demandes dépend ensuite des recherches dans votre secteur."),
]
page("/google-ads/", "Google Ads pour artisans du bâtiment | Bartier & Co",
     "Campagnes Google Ads locales pour couvreurs, façadiers et menuisiers : captez les propriétaires qui cherchent déjà, rappelés en moins de 5 minutes.",
     "\n\n".join([
         hero("Google Ads", "Captez les propriétaires qui cherchent déjà.",
              "Ils tapent « couvreur » et le nom de leur ville. Nous faisons en sorte qu'ils tombent sur vous, puis nous les rappelons en moins de 5 minutes.",
              crumbs(("Google Ads", "/google-ads/")), ("Comparer avec Meta", "/meta-ads/")),
         cols([("Les urgences", "Fuite, tuiles envolées, gouttière arrachée : la demande est immédiate."),
               ("Les projets mûrs", "Le propriétaire compare déjà des entreprises. Il faut être là, et rappeler vite."),
               ("Les secteurs denses", "Assez de recherches locales pour qu'une campagne tienne toute l'année.")],
              "Quand Google est le bon canal", "La demande existe déjà. Il faut la capter."),
         split_list("Ce que nous mettons en place", "Une campagne qui ne paie que les bonnes recherches.",
                    "Chaque clic coûte. Le travail consiste surtout à écarter ceux qui ne deviendront jamais des chantiers.",
                    ["Campagnes par métier et par commune de votre zone",
                     "Exclusion des recherches inutiles : gratuit, pas cher, emploi, formation, bricolage",
                     "Une page dédiée à votre entreprise, rapide sur mobile",
                     "Chaque appel et chaque formulaire suivi jusqu'au rendez-vous",
                     "Rappel en moins de 5 minutes, qualification, rendez-vous dans votre agenda"], grey=True),
         split_list("Ce qui reste à vous", "Votre compte, votre budget, vos chiffres.",
                    "Vous ne dépendez pas de nous pour garder ce qui a été construit.",
                    ["Le compte Google Ads est à votre nom",
                     "Le budget est payé directement à Google",
                     "Vous voyez chaque recherche, chaque clic, chaque euro"]),
         COMPARE,
         ENG_SECTION,
         faq_block(GOOGLE_FAQ),
         FORM,
     ]), nav="/google-ads/",
     schema={"@context": "https://schema.org", "@graph": [
         {"@type": "Service", "name": "Google Ads pour artisans du bâtiment", "serviceType": "Publicité Google Ads locale", "areaServed": ["FR"], "provider": {"@type": "Organization", "name": "Bartier & Co", "url": SITE + "/"}},
         breadcrumb_ld(("Google Ads", "/google-ads/")), faq_ld(GOOGLE_FAQ)]})

# ——— Meta Ads ———
META_FAQ = [
    ("Faut-il une page Facebook ?", "Oui, à votre nom. Si vous n'en avez pas, nous la créons avec vous pendant la mise en place."),
    ("Quel budget prévoir ?", "Il dépend de votre secteur et du nombre de visites que vous pouvez prendre en plus. Nous l'estimons ensemble. Vous le payez directement à Meta."),
    ("Est-ce légal de rappeler ces personnes ?", "Oui. Le formulaire demande leur accord explicite pour être recontactées par votre entreprise, et la preuve est conservée. Nous ne démarchons personne."),
    ("Les demandes Facebook sont-elles sérieuses ?", "Pas toutes. C'est pourquoi chaque demande est rappelée et vérifiée avant d'arriver dans votre agenda : propriétaire, projet, commune, délai."),
    ("Dans quel rayon les annonces sont-elles diffusées ?", "En général 25 à 40 km autour de votre dépôt, réglés commune par commune selon les chantiers que vous voulez."),
    ("Faut-il des photos de mes chantiers ?", "Oui. Vos photos de chantier et de votre équipe passent avant les images de banque."),
]
page("/meta-ads/", "Publicité Facebook et Instagram pour artisans | Bartier & Co",
     "Annonces Facebook et Instagram locales pour artisans du bâtiment : les propriétaires de votre secteur, rappelés en moins de 5 minutes et qualifiés.",
     "\n\n".join([
         hero("Meta Ads · Facebook et Instagram", "Touchez les propriétaires avant qu'ils ne cherchent.",
              "Des annonces à votre nom, à 25 à 40 km de votre dépôt. Chaque demande est rappelée en moins de 5 minutes, puis qualifiée.",
              crumbs(("Meta Ads", "/meta-ads/")), ("Comparer avec Google", "/google-ads/")),
         cols([("Un rayon autour du dépôt", "25 à 40 km, réglés commune par commune selon vos chantiers."),
               ("Vos vraies photos", "Vos chantiers, votre équipe. Rien de plus convaincant pour un voisin."),
               ("Des angles de saison", "Après les intempéries, avant l'hiver, au printemps pour la rénovation.")],
              "Comment nous diffusons", "Des annonces locales, au nom de votre entreprise."),
         split_list("Du clic au rendez-vous", "Rien ne part sans être vérifié.",
                    "Une demande Facebook n'est qu'un début. Le tri se fait au téléphone.",
                    ["Formulaire avec questions de tri et accord explicite pour être recontacté",
                     "Preuve du consentement conservée pour chaque demande",
                     "Rappel en moins de 5 minutes, en semaine de 8 h à 19 h",
                     "Propriétaire, projet, commune et délai vérifiés",
                     "Rendez-vous dans votre agenda, rappels au propriétaire la veille et deux heures avant",
                     "Flyers distribués dans les rues voisines de chaque chantier signé"], grey=True),
         split_list("Ce qui reste à vous", "Votre page, votre compte, vos chiffres.",
                    "Tout est créé à votre nom, et le reste si vous arrêtez.",
                    ["Page Facebook et compte publicitaire à votre nom",
                     "Budget payé directement à Meta",
                     "Accès à toutes les statistiques des annonces"]),
         COMPARE,
         ENG_SECTION,
         faq_block(META_FAQ),
         FORM,
     ]), nav="/meta-ads/",
     schema={"@context": "https://schema.org", "@graph": [
         {"@type": "Service", "name": "Publicité Facebook et Instagram pour artisans du bâtiment", "serviceType": "Publicité Meta Ads locale", "areaServed": ["FR"], "provider": {"@type": "Organization", "name": "Bartier & Co", "url": SITE + "/"}},
         breadcrumb_ld(("Meta Ads", "/meta-ads/")), faq_ld(META_FAQ)]})

# ——— Qui sommes-nous ———
page("/qui-sommes-nous/", "Qui sommes-nous | Bartier & Co",
     "Bartier & Co est une SAS française fondée par Charles Le Cottier et Martin Barthélémy. Des clients pour les artisans du bâtiment.",
     "\n\n".join([
         hero("Qui sommes-nous", "Deux fondateurs, joignables directement.",
              "Bartier & Co est une SAS française fondée par Charles Le Cottier et Martin Barthélémy. Nous remplissons l'agenda des artisans du bâtiment partout en France.",
              crumbs(("Qui sommes-nous", "/qui-sommes-nous/"))),
         """<section class="section">
  <div class="wrap split2">
    <div><p class="kicker">Pourquoi</p><h2>Un bon artisan ne devrait pas courir après les devis.</h2></div>
    <div class="prose">
      <p>Les artisans que nous rencontrons ont du métier et des clients satisfaits. Ce qui leur manque, c'est un flux régulier de projets sérieux.</p>
      <p>Les plateformes revendent la même demande à plusieurs entreprises. Le bouche-à-oreille ne se commande pas. Et personne n'a le temps de rappeler depuis un toit.</p>
      <p>Nous avons donc construit un système simple : des annonces locales, un rappel en moins de 5 minutes, et un rendez-vous réservé à un seul artisan.</p>
    </div>
  </div>
</section>""",
         cols([("Un interlocuteur, pas un standard", "Vous avez le numéro de Charles et de Martin. L'un de nous répond."),
               ("Des engagements écrits", "Exclusivité, un artisan par secteur, rappel en 5 minutes, sans engagement de durée."),
               ("Des chiffres vérifiables", "Le budget publicitaire est sur votre compte, et chaque rendez-vous est suivi jusqu'au chantier signé.")],
              "Comment nous travaillons", "Simple, joignable, honnête.", grey=True),
         """<section class="section">
  <div class="wrap tm">
    <div class="tm-text">
      <p class="kicker">Les fondateurs</p>
      <h2>Charles et Martin.</h2>
      <p class="sub">Charles, responsable des annonces, pilote les annonces, le rappel et les résultats. Martin, responsable commercial, est votre interlocuteur du premier appel au démarrage.</p>
    </div>
    <div class="tm-people">
      <figure><div class="ph" role="img" aria-label="Portrait de Charles Le Cottier, à venir"></div><figcaption><b>Charles Le Cottier</b><small>Cofondateur · Responsable des annonces</small></figcaption></figure>
      <figure><div class="ph" role="img" aria-label="Portrait de Martin Barthélémy, à venir"></div><figcaption><b>Martin Barthélémy</b><small>Cofondateur · Responsable commercial</small></figcaption></figure>
    </div>
  </div>
</section>""",
         ENG_SECTION,
         FORM,
     ]), nav="/qui-sommes-nous/",
     schema={"@context": "https://schema.org", "@graph": [
         {"@type": "AboutPage", "name": "Qui sommes-nous", "url": SITE + "/qui-sommes-nous/"},
         {"@type": "Organization", "name": "Bartier & Co", "legalName": "Bartier & Co SAS", "url": SITE + "/", "founder": [
             {"@type": "Person", "name": "Charles Le Cottier", "jobTitle": "Cofondateur, responsable des annonces"},
             {"@type": "Person", "name": "Martin Barthélémy", "jobTitle": "Cofondateur, responsable commercial"}]},
         breadcrumb_ld(("Qui sommes-nous", "/qui-sommes-nous/"))]})

# ——— Blog ———
ARTICLES = [
    {
        "slug": "lead-partage-lead-exclusif-rendez-vous-qualifie",
        "tag": "Comprendre",
        "title": "Demande partagée, demande exclusive, rendez-vous qualifié : les différences pour un artisan",
        "short": "Demande partagée, exclusive ou rendez-vous qualifié : ce qui change pour vous",
        "desc": "Trois offres qui se ressemblent sur le papier, mais pas sur le terrain. Ce que chacune vous livre vraiment, et les questions à poser avant de signer un contrat.",
        "minutes": 5,
        "body": """
<p class="answer">Une <b>demande partagée</b> est une demande de devis vendue à plusieurs entreprises. Une <b>demande exclusive</b> n'est vendue qu'à vous, mais c'est à vous de rappeler. Un <b>rendez-vous qualifié</b> est une visite déjà fixée, chez un propriétaire dont le projet a été vérifié.</p>

<h2>Quelle différence entre une demande de devis et un rendez-vous qualifié ?</h2>
<p>Le vocabulaire marketing mélange tout, et les plateformes parlent de « leads ». Pour un artisan, il n'y a que trois questions : combien d'entreprises reçoivent la même demande, qui rappelle le propriétaire, et ce qui a été vérifié avant que vous vous déplaciez.</p>

<h2>La demande partagée : la même demande vendue plusieurs fois</h2>
<p>Vous recevez un nom, un numéro et une description du projet. D'autres entreprises reçoivent la même demande, au même moment. Le propriétaire est appelé plusieurs fois, compare les prix, et retient souvent le premier qui rappelle ou le moins cher.</p>

<h2>La demande exclusive : exclusive jusqu'où ?</h2>
<p>La demande n'est vendue qu'à vous. C'est mieux, mais vérifiez ce que recouvre le mot. Exclusive pendant combien de temps ? Sur quelle zone ? Et surtout : qui rappelle ? Si c'est vous, le soir, la demande a souvent refroidi.</p>

<h2>Le rendez-vous qualifié : ce qui a été vérifié</h2>
<p>Quelqu'un a rappelé le propriétaire, vérifié qu'il est propriétaire occupant, compris son projet, confirmé la commune, puis fixé une date avec lui. Vous recevez directement une visite dans votre agenda, sans personne à rappeler.</p>

<h2>Demande partagée, demande exclusive, rendez-vous qualifié : le comparatif</h2>
<table>
<thead><tr><th><span class="vh">Critère</span></th><th>Demande partagée</th><th>Demande exclusive</th><th>Rendez-vous qualifié</th></tr></thead>
<tbody>
<tr><td>Entreprises sur la même demande</td><td>Plusieurs</td><td>Une</td><td>Une</td></tr>
<tr><td>Qui rappelle</td><td>Vous</td><td>Vous</td><td>Le prestataire</td></tr>
<tr><td>Projet vérifié</td><td>Rarement</td><td>Parfois</td><td>Oui</td></tr>
<tr><td>Ce que vous recevez</td><td>Un nom et un numéro</td><td>Un nom et un numéro</td><td>Une visite fixée</td></tr>
</tbody>
</table>

<h2>Les questions à poser avant de signer</h2>
<ol>
<li>À combien d'entreprises la même demande est-elle transmise ?</li>
<li>Qui rappelle le propriétaire, et en combien de temps ?</li>
<li>Qu'est-ce qui est vérifié avant de me transmettre la demande ?</li>
<li>Que se passe-t-il si le propriétaire n'est pas joignable ou n'est pas sérieux ?</li>
<li>Y a-t-il une durée d'engagement minimale ?</li>
</ol>
<p>Nos réponses sont dans nos <a href="/#principles">engagements</a>, sur la page d'accueil. Les définitions sont dans notre <a href="/lexique/#clients">lexique</a>.</p>
""",
    },
    {
        "slug": "google-ads-ou-meta-ads-artisan",
        "tag": "Publicité",
        "title": "Google Ads ou Meta Ads pour un artisan du bâtiment : qui capte quelle demande",
        "short": "Google Ads ou Meta Ads : qui capte quelle demande",
        "desc": "Google capte ceux qui cherchent déjà, Meta touche ceux qui n'ont pas encore cherché. Comment choisir selon votre métier, votre secteur et votre budget.",
        "minutes": 4,
        "body": """
<p class="answer"><b>Google Ads</b> capte une demande qui existe déjà : le propriétaire cherche un artisan. <b>Meta Ads</b> (Facebook et Instagram) suscite une demande chez des propriétaires qui n'ont pas encore cherché. Le premier convient aux urgences et aux projets mûrs, le second aux rénovations et à l'entretien.</p>

<h2>Demande exprimée ou demande suscitée</h2>
<p>Sur Google, le propriétaire tape « couvreur » et le nom de sa ville. Il a un besoin, souvent précis, parfois urgent. Sur Facebook ou Instagram, il ne cherche rien : il voit une annonce d'une entreprise de son secteur, et elle tombe au bon moment, ou non.</p>

<h2>Urgence ou projet de rénovation</h2>
<p>Une fuite après un coup de vent se cherche sur Google. Une toiture qui verdit, des fenêtres de vingt ans ou une façade fatiguée sont des projets que le propriétaire repousse : une annonce bien placée les fait avancer.</p>

<h2>Combien coûte une campagne : ce qui dépend de vous</h2>
<p>Sur Google, le prix du clic dépend du métier et de la concurrence locale. Sur Meta, le budget se règle librement, mais toutes les demandes ne sont pas sérieuses. Dans les deux cas, comptez ce que vous coûte un <a href="/lexique/#cout-par-chantier-signe">chantier signé</a>.</p>

<h2>Ce que chaque canal exige après le clic</h2>
<ul>
<li><b>Google</b> : écarter les recherches inutiles (gratuit, emploi, bricolage) et répondre vite, car le propriétaire appelle plusieurs entreprises.</li>
<li><b>Meta</b> : trier au téléphone, car une partie des demandes est encore au stade de l'idée.</li>
</ul>
<p>Dans les deux cas, la demande doit être rappelée en quelques minutes. C'est souvent là que se perdent les meilleurs projets.</p>

<h2>Google Ads ou Meta Ads : notre choix, et ses limites</h2>
<p>Nous commençons le plus souvent par Meta pour les métiers de rénovation (couverture, façade, menuiserie, isolation), parce que le volume se construit dans un rayon précis. Nous ajoutons Google quand votre secteur a assez de recherches locales. Ce n'est pas une règle : certains secteurs ruraux n'ont pas assez de recherches pour Google, et certains métiers vivent surtout de l'urgence.</p>
<p>Voir aussi : <a href="/google-ads/">Google Ads</a> et <a href="/meta-ads/">Meta Ads</a>.</p>
""",
    },
    {
        "slug": "relance-devis-artisan",
        "tag": "Méthode",
        "title": "Relance de devis : calendrier, SMS et script d'appel pour artisans",
        "short": "Relance de devis : le calendrier, les SMS et le script",
        "desc": "Un devis de rénovation se relance. Voici un calendrier simple, trois SMS prêts à copier, un script d'appel de deux minutes et le bon moment pour s'arrêter.",
        "minutes": 5,
        "body": """
<p class="answer">Relancez un devis de rénovation <b>par un appel</b>, quelques jours après l'envoi, puis <b>par SMS</b> si vous n'avez pas de réponse. Arrêtez après trois tentatives sans retour, en laissant la porte ouverte. Chaque relance sert à savoir où en est le projet.</p>

<h2>Quand relancer un devis ?</h2>
<table>
<thead><tr><th>Quand</th><th>Quoi</th><th>Pourquoi</th></tr></thead>
<tbody>
<tr><td>Le jour de l'envoi</td><td>SMS court</td><td>Confirmer que le devis est bien arrivé</td></tr>
<tr><td>Quelques jours après</td><td>Appel</td><td>Répondre aux questions avant que le client compare</td></tr>
<tr><td>Une semaine plus tard</td><td>SMS</td><td>Proposer de rappeler le client au moment qui l'arrange</td></tr>
<tr><td>Deux à trois semaines plus tard</td><td>Dernier SMS</td><td>Clore poliment et laisser la porte ouverte</td></tr>
</tbody>
</table>
<p>Adaptez le rythme au projet : une urgence se relance plus vite qu'une rénovation prévue pour le printemps.</p>

<h2>Trois SMS de relance prêts à copier</h2>
<blockquote>Bonjour Madame Durand, c'est Julien de l'entreprise Lemaire Couverture. Je vous ai envoyé le devis pour votre toiture par e-mail. Dites-moi s'il est bien arrivé. Bonne journée.</blockquote>
<blockquote>Bonjour Madame Durand, avez-vous pu regarder le devis pour la toiture ? Je peux vous rappeler pour en parler, à l'heure qui vous arrange.</blockquote>
<blockquote>Bonjour Madame Durand, je ne veux pas vous déranger davantage. Si le projet revient, je reste disponible. Bonne continuation.</blockquote>
<p>Les noms sont des exemples. Gardez le vôtre, celui de l'entreprise, et le projet précis.</p>

<h2>Un script d'appel de relance en deux minutes</h2>
<ol>
<li><b>Le contexte</b> : « Bonjour, c'est Julien, je suis passé jeudi pour votre toiture. Vous avez deux minutes ? »</li>
<li><b>La question ouverte</b> : « Qu'avez-vous pensé du devis ? »</li>
<li><b>L'écoute</b> : le prix, le délai, une question technique, un autre devis.</li>
<li><b>La prochaine étape</b> : « Je vous propose qu'on se rappelle vendredi, après que vous en aurez parlé ensemble. »</li>
</ol>

<h2>Quand arrêter de relancer un devis ?</h2>
<p>Après trois tentatives sans réponse, arrêtez. Un dernier message poli laisse une meilleure impression qu'un quatrième appel, et le propriétaire reviendra parfois quelques mois plus tard.</p>

<h2>Comment mesurer l'effet de vos relances ?</h2>
<p>Notez pour chaque devis : envoyé, relancé, signé ou perdu, et pourquoi. Au bout de quelques mois, vous saurez quels projets vous signez, et où partent les autres. Votre <a href="/lexique/#taux-de-signature">taux de signature</a> (devis signés ÷ devis envoyés × 100) dit si les relances paient.</p>
""",
    },
    {
        "slug": "dpe-2027",
        "tag": "Propriétaires",
        "date": "2026-11-20",
        "date_fr": "20 novembre 2026",
        "date_short": "20 nov. 2026",
        "minutes": 6,
        "title": "DPE 2027 : ce qui change pour les propriétaires",
        "short": "DPE 2027 : ce qui change pour les propriétaires",
        "desc": "Nouvelle étiquette gratuite, location des logements G, F et E, vote en cours au Parlement : ce qui change pour le DPE en 2027, sources officielles à l'appui.",
        "cta": ("Obtenir mon devis gratuit", "/devis-travaux/#projet"),
        "citation": {"@type": "Report", "name": "Le diagnostic de performance énergétique (DPE) des logements au 1er janvier 2027 : synthèse documentaire", "identifier": "https://doi.org/10.5281/zenodo.24396448", "url": "https://doi.org/10.5281/zenodo.24396448", "license": "https://creativecommons.org/licenses/by/4.0/", "inLanguage": "fr-FR"},
        "aside": '<h3>Des travaux pour gagner une classe ?</h3>\n      <p>Isolation, fenêtres, toiture, façade : un seul artisan près de chez vous. Visite et devis offerts.</p>\n      <a class="btn" href="/devis-travaux/#projet"><span>Obtenir mon devis gratuit</span></a>',
        "faq": [
            ("Le DPE 2027 peut-il faire baisser mon étiquette ?", "Non. Selon le ministère de la Transition écologique, le passage du coefficient de l'électricité à 1,7 ne dégrade aucune étiquette. Il peut seulement améliorer celle des logements chauffés à l'électricité."),
            ("Faut-il refaire son DPE en 2027 ?", "Non, s'il est encore valable. À partir du 1er janvier 2027, une attestation avec la nouvelle étiquette s'obtient gratuitement sur l'Observatoire DPE-Audit de l'ADEME, avec le numéro du DPE. Un nouveau diagnostic n'est utile que si vous avez fait des travaux depuis."),
            ("Peut-on encore louer un logement classé G ?", "Pas selon la loi en vigueur : depuis le 1er janvier 2025, un logement classé G n'est plus décent pour un nouveau bail, un renouvellement ou une reconduction. Un projet de loi en cours d'examen pourrait changer cette règle, qui s'applique tant qu'il n'est pas promulgué."),
            ("Quand un logement classé F ne pourra-t-il plus être loué ?", "Le 1er janvier 2028, selon la loi en vigueur, sous réserve du projet de loi sur le logement en cours d'examen au Parlement."),
            ("Le DPE est-il obligatoire pour louer ?", "Oui. Il fait partie du dossier remis au locataire avec le bail, et l'étiquette doit figurer dans l'annonce."),
            ("Quels travaux améliorent le plus le DPE ?", "Dans une maison non isolée, la toiture et les combles d'abord : 25 à 30 % des pertes de chaleur selon l'ADEME. Viennent ensuite les fuites d'air, les murs, puis les fenêtres."),
        ],
        "body": """
<p class="answer">Au <b>1er janvier 2027</b>, le DPE des logements chauffés à l'électricité est recalculé : le coefficient de l'électricité passe de 1,9 à 1,7. L'étiquette peut s'améliorer, jamais se dégrader, et la mise à jour est gratuite sur l'Observatoire DPE-Audit de l'ADEME. Pour la location, les règles en vigueur n'ont pas changé : logements G interdits depuis 2025, F à partir de 2028, E à partir de 2034. Un projet de loi en cours d'examen pourrait toutefois les modifier.</p>

<h2>Qu'est-ce qui change pour le DPE au 1er janvier 2027 ?</h2>
<p>Un <a href="https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000054747079" target="_blank" rel="noopener">arrêté du 19 août 2026</a> abaisse de 1,9 à 1,7 le coefficient qui convertit la consommation d'électricité en énergie primaire, la valeur qui sert à calculer l'étiquette. Ce coefficient avait déjà baissé de 2,3 à 1,9 au 1er janvier 2026.</p>
<ul>
<li>Le changement porte sur la part d'électricité dans la consommation : il profite surtout aux logements chauffés à l'électricité.</li>
<li>Selon le <a href="https://www.ecologie.gouv.fr/presse/dpe-audits-energetiques-publication-larrete-abaissant-facteur-conversion-lelectricite-17-1er" target="_blank" rel="noopener">ministère de la Transition écologique</a>, aucun logement ne verra son étiquette se dégrader.</li>
<li>Les DPE réalisés à partir du 1er janvier 2027 intègrent directement la nouvelle valeur. Les DPE déjà faits restent valables (<a href="https://www.service-public.gouv.fr/particuliers/actualites/A18446" target="_blank" rel="noopener">Service-Public</a>).</li>
</ul>

<h2>Comment obtenir la nouvelle étiquette de votre DPE ?</h2>
<p>Inutile de refaire le diagnostic. À partir du 1er janvier 2027, la mise à jour est gratuite et immédiate :</p>
<ol>
<li>Retrouvez le numéro de votre DPE : 13 caractères, en haut de la première page du rapport.</li>
<li>Saisissez-le sur l'<a href="https://observatoire-dpe-audit.ademe.fr/" target="_blank" rel="noopener">Observatoire DPE-Audit de l'ADEME</a>.</li>
<li>Téléchargez l'attestation qui indique la nouvelle étiquette, et gardez-la avec votre DPE.</li>
</ol>
<p>L'attestation recalcule l'étiquette à partir des mêmes données. Si vous avez fait des travaux depuis le diagnostic, seul un nouveau DPE les prendra en compte.</p>

<h2>Votre DPE est-il encore valable ?</h2>
<table>
<thead><tr><th>DPE réalisé</th><th>Validité</th></tr></thead>
<tbody>
<tr><td>Depuis le 1er juillet 2021</td><td>10 ans</td></tr>
<tr><td>Du 1er janvier 2018 au 30 juin 2021</td><td>Plus valable depuis le 1er janvier 2025</td></tr>
<tr><td>Avant le 1er janvier 2018</td><td>Plus valable depuis le 1er janvier 2023</td></tr>
</tbody>
</table>
<p>Le DPE est obligatoire pour vendre ou louer un logement, et son étiquette doit figurer dans l'annonce (<a href="https://www.service-public.gouv.fr/particuliers/vosdroits/F16096" target="_blank" rel="noopener">Service-Public, fiche F16096</a>).</p>

<h2>Louer un logement classé G, F ou E : les règles en vigueur</h2>
<p>La loi Climat et Résilience fixe un niveau minimal de performance pour qu'un logement soit décent, donc louable (<a href="https://www.service-public.gouv.fr/particuliers/actualites/A17975" target="_blank" rel="noopener">Service-Public</a>) :</p>
<table>
<thead><tr><th>Classe</th><th>Plus louable à partir du</th></tr></thead>
<tbody>
<tr><td>G</td><td>1er janvier 2025</td></tr>
<tr><td>F</td><td>1er janvier 2028</td></tr>
<tr><td>E</td><td>1er janvier 2034</td></tr>
</tbody>
</table>
<p>La règle s'applique à la signature d'un nouveau bail, à son renouvellement ou à sa reconduction tacite, pas en cours de bail. En Guadeloupe, en Martinique, en Guyane, à La Réunion et à Mayotte, le calendrier est décalé : 2028 pour les logements G, 2031 pour les F.</p>
<p>Avec le coefficient à 1,7, certains logements chauffés à l'électricité changent de classe sans travaux : vérifiez la nouvelle étiquette avant de conclure que votre logement ne peut plus être loué.</p>

<h2>Ce que le Parlement est en train de voter</h2>
<p>Le <a href="https://www.vie-publique.fr/loi/303813-relance-logement-projet-de-loi-jeanbrun" target="_blank" rel="noopener">projet de loi sur la relance et la décentralisation du logement</a> pourrait changer ce calendrier :</p>
<ul>
<li><b>Juillet 2026</b> : le Sénat adopte une version qui garde l'interdiction, avec des assouplissements.</li>
<li><b>17 novembre 2026</b> : l'Assemblée nationale adopte un amendement qui supprime les interdictions de louer liées au DPE, contre l'avis du gouvernement (<a href="https://www.batiweb.com/actualites/legislation/passoires-thermiques-deputes-amendement-interdiction-location-49635" target="_blank" rel="noopener">Batiweb</a>).</li>
<li><b>24 novembre 2026</b> : vote solennel de l'Assemblée sur l'ensemble du texte. Une commission mixte paritaire, sept députés et sept sénateurs, cherchera ensuite un texte commun.</li>
</ul>
<p><b>Rien n'est définitif</b> : tant que la loi n'est pas promulguée, les interdictions restent en vigueur. Cette page sera mise à jour à chaque étape.</p>

<h2>Classe E : ce qui vous attend, à la location comme à la vente</h2>
<ul>
<li><b>Location</b> : plus possible à partir du 1er janvier 2034, selon le calendrier en vigueur.</li>
<li><b>Vente</b> : depuis le 1er janvier 2025, vendre une maison ou un immeuble appartenant à un seul propriétaire classé E demande un audit énergétique, comme pour les classes F et G depuis avril 2023. L'obligation s'étendra à la classe D en 2034. Elle ne concerne pas un appartement en copropriété (<a href="https://www.ecologie.gouv.fr/politiques-publiques/audit-energetique-reglementaire" target="_blank" rel="noopener">ministère de la Transition écologique</a>).</li>
<li>L'audit propose des scénarios de travaux chiffrés, avec les aides possibles. Il est valable 5 ans.</li>
</ul>

<h2>Quels travaux font gagner une classe ?</h2>
<p>Dans une maison non isolée, la chaleur s'échappe d'abord par le toit (25 à 30 %), puis par l'air renouvelé et les fuites (20 à 25 %), par les murs (20 à 25 %) et par les fenêtres (10 à 15 %), selon le guide de l'ADEME <a href="https://www.ecologie.gouv.fr/sites/default/files/documents/guide-hiver-tout-confort.pdf" target="_blank" rel="noopener">« Un hiver tout confort »</a>. C'est pourquoi l'isolation des combles ou de la toiture est souvent le premier chantier.</p>
<table>
<thead><tr><th>Travaux</th><th>Prix moyen</th><th>Source</th></tr></thead>
<tbody>
<tr><td><a href="/devis-travaux/isolation/">Isolation des combles perdus</a></td><td>environ 40 €/m² TTC</td><td>La Maison Saint-Gobain, 07/2026</td></tr>
<tr><td><a href="/devis-travaux/isolation/">Combles aménagés, par l'intérieur</a></td><td>130 à 180 €/m² TTC</td><td>La Maison Saint-Gobain, 07/2026</td></tr>
<tr><td><a href="/devis-travaux/toiture/">Isolation de la toiture par l'extérieur (sarking)</a></td><td>120 à 250 €/m²</td><td>QuelleEnergie, 11/2026</td></tr>
<tr><td><a href="/devis-travaux/ravalement-facade/">Ravalement avec isolant</a></td><td>110 à 215 €/m²</td><td>La Maison Saint-Gobain, 08/2026</td></tr>
<tr><td><a href="/devis-travaux/fenetres/">Fenêtre PVC posée en remplacement</a></td><td>870 à 1 170 € TTC</td><td>La Maison Saint-Gobain, 02/2026</td></tr>
</tbody>
</table>
<p>Le gain réel dépend de votre logement. L'audit énergétique, obligatoire pour vendre une maison classée E, F ou G, chiffre justement l'étiquette visée par chaque scénario de travaux.</p>
<p>MaPrimeRénov' et les primes CEE demandent une entreprise certifiée RGE, et les travaux d'amélioration énergétique peuvent bénéficier d'une TVA à 5,5 %. Les conditions changent chaque année : vérifiez-les sur <a href="https://france-renov.gouv.fr/aides/maprimerenov" target="_blank" rel="noopener">france-renov.gouv.fr</a> et sur <a href="https://www.economie.gouv.fr/particuliers/impots-et-fiscalite/gerer-mes-autres-impots-et-taxes/tva-taux-reduit-pour-quels-travaux" target="_blank" rel="noopener">economie.gouv.fr</a>.</p>
<p>Une synthèse documentaire de 4 pages, avec toutes les sources de cet article, est archivée sur Zenodo, l'archive ouverte du CERN : <a href="https://doi.org/10.5281/zenodo.24396448" target="_blank" rel="noopener">DOI 10.5281/zenodo.24396448</a>.</p>
""",
    },
    {
        'slug': 'demarchage-arnaques-travaux',
        'tag': 'Propriétaires',
        'date': '2026-11-21',
        'date_fr': '21 novembre 2026',
        'date_short': '21 nov. 2026',
        'minutes': 5,
        'title': 'Démarchage pour des travaux : vos droits et les pièges à éviter',
        'short': 'Démarchage et arnaques aux travaux : vos droits',
        'desc': 'Démarchage à domicile ou par téléphone pour une toiture ou une isolation : ce que dit la loi en 2026, les signaux d’alerte et que faire si vous avez signé.',
        'cta': ('Obtenir mon devis gratuit', '/devis-travaux/#projet'),
        'aside': '<h3>Un artisan que vous avez choisi</h3>\n      <p>Décrivez vos travaux&nbsp;: un seul artisan de votre secteur vient chiffrer chez vous. Visite et devis offerts.</p>\n      <a class="btn" href="/devis-travaux/#projet"><span>Obtenir mon devis gratuit</span></a>',
        'faq': [('Un démarcheur peut-il demander un acompte le jour de la signature ?', 'Non. Après un contrat signé chez vous, il ne peut recevoir aucun paiement pendant 7 jours : ni acompte, ni chèque, ni autorisation de prélèvement. Seuls les travaux de réparation urgents que vous avez demandés échappent à cette règle.'), ('Combien de temps ai-je pour annuler un contrat signé à domicile ?', '14 jours, sans avoir à vous justifier. Utilisez le formulaire de rétractation remis avec le contrat, de préférence par lettre recommandée avec accusé de réception.'), ('Une entreprise d’isolation peut-elle m’appeler sans que je l’aie demandé ?', 'Non. Depuis le 11 août 2026, le démarchage téléphonique pour la rénovation énergétique est interdit, même si vous avez donné votre accord pour être démarché. Seule exception : un rappel que vous avez vous-même demandé, dans les 5 jours ouvrables.'), ('Bloctel existe-t-il encore ?', 'Non. Bloctel a cessé d’exister le 11 août 2026. Depuis, une entreprise ne peut plus vous démarcher par téléphone sans votre accord préalable.'), ('Comment signaler un démarchage abusif ?', 'Envoyez par SMS « spam vocal » suivi du numéro qui vous a appelé au 33700, ou faites le signalement sur 33700.fr. C’est gratuit. Un litige avec une entreprise peut aussi être signalé sur SignalConso.'), ('Bartier & Co fait-il du démarchage auprès des particuliers ?', 'Non. Nous rappelons uniquement les personnes qui ont décrit leurs travaux sur notre site et accepté d’être rappelées. Ensuite, un seul artisan de leur secteur vient chiffrer chez elles.')],
        'body': '\n<p class="answer">Chez vous, un démarcheur ne peut rien encaisser pendant <b>7 jours</b> après la signature, et vous avez <b>14 jours</b> pour annuler le contrat sans vous justifier. Par téléphone, depuis le <b>11 août 2026</b>, une entreprise ne peut plus vous démarcher sans votre accord préalable. Pour la rénovation énergétique, c’est interdit même avec votre accord, et un contrat obtenu par un démarchage téléphonique illégal est nul.</p>\n\n<h2>Un démarcheur sonne à votre porte&nbsp;: que dit la loi&nbsp;?</h2>\n<p>Un contrat signé chez vous après un démarchage ne peut donner lieu à <b>aucun paiement pendant 7 jours</b> à compter de la signature&nbsp;: ni acompte, ni chèque, ni autorisation de prélèvement. L’entreprise n’a pas non plus le droit de commencer les travaux avant la fin de ce délai. Si elle encaisse quand même, le contrat n’est pas valable (<a href="https://entreprendre.service-public.gouv.fr/vosdroits/F23224" target="_blank" rel="noopener">Service Public, vérifié le 11 août 2026</a>).</p>\n<p>Ce délai de 7 jours ne s’applique pas aux travaux de réparation à faire en urgence chez vous, à votre demande, comme une fuite que vous signalez vous-même.</p>\n<p>Vous disposez ensuite de <b>14 jours pour annuler le contrat</b>, sans avoir à vous justifier. Avant la signature, l’entreprise doit vous remettre un document qui indique son identité, son adresse postale et son téléphone, le prix, les délais, et les conditions de rétractation avec un formulaire type.</p>\n\n<h2>Démarchage par téléphone&nbsp;: qu’est-ce qui a changé le 11 août 2026&nbsp;?</h2>\n<p>Depuis le 11 août 2026, une entreprise ne peut plus vous démarcher par téléphone sans votre accord préalable. Le démarchage est interdit par défaut, et la liste Bloctel a cessé d’exister ce jour-là (<a href="https://www.service-public.gouv.fr/particuliers/actualites/A18384" target="_blank" rel="noopener">Service Public, 11 août 2026</a>). Ces règles viennent de la loi du 30 juin 2025 contre toutes les fraudes aux aides publiques.</p>\n<p>Pour les économies d’énergie, la rénovation énergétique et l’adaptation du logement au vieillissement ou au handicap, la règle est plus stricte&nbsp;: <b>le démarchage téléphonique est interdit même si vous avez donné votre accord</b>. Seule exception&nbsp;: vous avez vous-même demandé à être rappelé. L’appel doit alors avoir lieu dans les 5 jours ouvrables et porter uniquement sur ce que vous avez demandé (<a href="https://www.service-public.gouv.fr/particuliers/vosdroits/F33267" target="_blank" rel="noopener">Service Public, vérifié le 12 août 2026</a>).</p>\n<p>Un contrat conclu après un démarchage téléphonique illégal est nul. L’entreprise risque jusqu’à 75&nbsp;000&nbsp;€ d’amende pour une personne physique et 375&nbsp;000&nbsp;€ pour une société, par appel.</p>\n\n<h2>Quels signaux doivent vous alerter&nbsp;?</h2>\n<ul>\n<li><b>Une visite que vous n’avez pas demandée</b>, juste après un orage ou une tempête, pour «&nbsp;vérifier&nbsp;» ou démousser votre toit.</li>\n<li><b>Un prix valable «&nbsp;aujourd’hui seulement&nbsp;»</b>, ou une remise si vous signez tout de suite.</li>\n<li><b>Une demande d’argent le jour même</b>&nbsp;: acompte, chèque ou autorisation de prélèvement.</li>\n<li><b>Un appel que vous n’avez pas sollicité</b> pour de l’isolation ou des travaux d’économies d’énergie&nbsp;: il est interdit.</li>\n<li><b>Pas de devis écrit et détaillé</b>, ou un devis sans le nom de l’assureur décennal de l’entreprise.</li>\n</ul>\n<p>Service Public conseille de ne jamais signer lors d’une première visite et de prendre le temps de comparer plusieurs devis (<a href="https://www.service-public.gouv.fr/particuliers/actualites/A17228" target="_blank" rel="noopener">Service Public, 2024</a>).</p>\n\n<h2>Vous avez signé&nbsp;: que faire&nbsp;?</h2>\n<ol>\n<li><b>Vous êtes dans les 14 jours</b>&nbsp;: envoyez le formulaire de rétractation remis avec le contrat, de préférence par lettre recommandée avec accusé de réception, pour garder une preuve.</li>\n<li><b>Vous avez payé dans les 7 jours</b>&nbsp;: le contrat n’est pas valable. Faites-le savoir par écrit à l’entreprise.</li>\n<li><b>Signalez-le</b>&nbsp;: un démarchage téléphonique abusif se signale gratuitement en envoyant par SMS «&nbsp;spam vocal&nbsp;» suivi du numéro de l’appelant au 33700. Un litige avec une entreprise se signale sur SignalConso.</li>\n</ol>\n\n<h2>Le bon réflexe&nbsp;: choisir vous-même l’artisan</h2>\n<p>Le plus sûr est de faire vous-même la démarche&nbsp;: vous choisissez l’entreprise, vous lui demandez de venir voir le chantier, et vous prenez le temps de lire son devis. Avant de signer, vérifiez son immatriculation, son assurance décennale et, si vous visez des aides, sa certification RGE&nbsp;: <a class="link" href="/devis-travaux/#artisan-serieux">les 5 points à vérifier</a>.</p>\n<p>Sur Bartier &amp; Co, c’est vous qui décrivez vos travaux. Nous vous rappelons parce que vous l’avez demandé, puis un seul artisan de votre secteur vient chiffrer chez vous. Vous restez libre de refuser son devis.</p>\n',
    },
]


def article_page(a):
    path = f"/blog/{a['slug']}/"
    others = [o for o in ARTICLES if o is not a]
    more = "".join(f'<li><a href="/blog/{o["slug"]}/">{o["short"]}</a></li>' for o in others)
    body = f"""<section class="page-hero" aria-labelledby="h1">
  <div class="wrap">
    {crumbs(("Blog", "/blog/"), (a["short"], path))}
    <p class="kicker">{a["tag"]}</p>
    <h1 id="h1">{a["title"]}</h1>
    <p class="post-meta"><span>Par Charles Le Cottier, cofondateur</span><span>Publié le <time datetime="{TODAY}">{TODAY_FR}</time></span><span>{a["minutes"]} min de lecture</span></p>
  </div>
</section>

<section class="section">
  <div class="wrap article">
    <article class="prose">
{a["body"]}
    </article>
    <aside>
      <div class="aside-box">
        <h3>Votre secteur est-il libre&nbsp;?</h3>
        <p>Un seul artisan par métier et par secteur. Quatre questions, une minute.</p>
        <a class="btn btn-primary" href="#secteur">Vérifier mon secteur</a>
      </div>
      <div class="aside-box" style="position:static;margin-top:16px">
        <h3>À lire aussi</h3>
        <ul class="list-x">{more}</ul>
      </div>
    </aside>
  </div>
</section>

{FORM}"""
    schema = {"@context": "https://schema.org", "@graph": [
        {"@type": "BlogPosting", "headline": fr(a["title"]), "description": fr(a["desc"]), "datePublished": TODAY + "T09:00:00+01:00", "dateModified": TODAY + "T09:00:00+01:00",
         "inLanguage": "fr-FR", "mainEntityOfPage": SITE + path,
         "author": {"@type": "Person", "name": "Charles Le Cottier", "jobTitle": "Cofondateur", "url": SITE + "/qui-sommes-nous/"},
         "publisher": {"@type": "Organization", "name": "Bartier & Co", "url": SITE + "/"}},
        breadcrumb_ld(("Blog", "/blog/"), (fr(a["short"]), path))]}
    return page(path, f'{a["short"]} | Bartier & Co', a["desc"], body, nav="/blog/", schema=schema)


paths = ["/", "/metiers/"] + [f"/metiers/{s}/" for s in ["couverture", "menuiserie-exterieure", "facade", "charpente", "isolation"]]
paths += ["/google-ads/", "/meta-ads/", "/qui-sommes-nous/", "/blog/"]
for a in ARTICLES:
    paths.append(article_page(a))

cards = "\n".join(f"""      <li><a class="post-card" href="/blog/{a['slug']}/"><span class="tag">{a['tag']}</span><h3>{a['short']}</h3><p>{a['desc']}</p><span class="meta">{a['minutes']} min · {TODAY_FR}</span></a></li>""" for a in ARTICLES)
page("/blog/", "Blog : trouver des chantiers, publicité, relance de devis | Bartier & Co",
     "Conseils concrets pour les artisans du bâtiment : trouver des chantiers, publicité locale, relance de devis, plateformes et rendez-vous qualifiés.",
     f"""<section class="page-hero" aria-labelledby="h1">
  <div class="wrap">
    {crumbs(("Blog", "/blog/"))}
    <p class="kicker">Blog</p>
    <h1 id="h1">Trouver des chantiers, sans y passer vos soirées.</h1>
    <p class="lead">Des articles courts et concrets, écrits pour les artisans du bâtiment.</p>
  </div>
</section>
<section class="section">
  <div class="wrap">
    <ul class="posts">
{cards}
    </ul>
  </div>
</section>
{FORM}""", nav="/blog/",
     schema={"@context": "https://schema.org", "@graph": [{"@type": "Blog", "name": "Blog Bartier & Co", "url": SITE + "/blog/", "inLanguage": "fr-FR"}, breadcrumb_ld(("Blog", "/blog/"))]})

# ——— Fichiers SEO et GEO ———
(ROOT / "robots.txt").write_text("""# Bartier & Co
# Moteurs de recherche et moteurs de réponse IA : accès autorisé à tout le site.

User-agent: *
Allow: /

# Moteurs de réponse et assistants IA (GEO)
User-agent: GPTBot
Allow: /

User-agent: OAI-SearchBot
Allow: /

User-agent: ChatGPT-User
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: Claude-SearchBot
Allow: /

User-agent: Claude-User
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: Perplexity-User
Allow: /

User-agent: Google-Extended
Allow: /

User-agent: Applebot-Extended
Allow: /

User-agent: Applebot
Allow: /

User-agent: Bingbot
Allow: /

User-agent: Amazonbot
Allow: /

User-agent: meta-externalagent
Allow: /

User-agent: MistralAI-User
Allow: /

User-agent: MistralAI-Index
Allow: /

User-agent: Meta-WebIndexer
Allow: /

User-agent: meta-externalfetcher
Allow: /

User-agent: DuckAssistBot
Allow: /

User-agent: CCBot
Allow: /

Sitemap: https://bartierandco.com/sitemap.xml
""", encoding="utf-8")

urls = "\n".join(f"  <url><loc>{SITE}{p}</loc><lastmod>{TODAY}</lastmod></url>" for p in paths)
(ROOT / "sitemap.xml").write_text(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}\n</urlset>\n', encoding="utf-8")

art_lines = "\n".join(f"- [{fr(a['short'])}]({SITE}/blog/{a['slug']}/) : {fr(a['desc'])}" for a in ARTICLES)
(ROOT / "llms.txt").write_text(f"""# Bartier & Co

> Bartier & Co trouve des clients aux artisans du bâtiment à gros chantiers (couverture, façade, menuiserie extérieure, charpente, isolation) partout en France. Bartier & Co diffuse des annonces locales (Meta Ads, Google Ads), rappelle chaque demande en moins de 5 minutes en semaine de 8 h à 19 h, vérifie le projet et fixe la visite chez le propriétaire, directement dans l'agenda de l'artisan. Les rendez-vous ne sont proposés qu'à un seul artisan par métier et par secteur. Sans engagement de durée. Pour les propriétaires, la mise en relation avec un artisan de leur secteur est gratuite : {SITE}/devis-travaux/. Société : Bartier & Co, SAS française en cours d'immatriculation. Fondateurs : Charles Le Cottier et Martin Barthélémy.

## Pages principales
- [Accueil]({SITE}/) : la méthode, les engagements et le formulaire pour vérifier si un secteur est libre.
- [Métiers]({SITE}/metiers/) : couverture et zinguerie, façade et ravalement, menuiserie extérieure, charpente, isolation.
- [Google Ads]({SITE}/google-ads/) : campagnes locales pour capter les propriétaires qui cherchent déjà un artisan.
- [Meta Ads]({SITE}/meta-ads/) : annonces Facebook et Instagram dans un rayon de 25 à 40 km autour du dépôt.
- [Qui sommes-nous]({SITE}/qui-sommes-nous/) : les fondateurs et la façon de travailler.
- [Devis travaux, pour les particuliers]({SITE}/devis-travaux/) : un propriétaire décrit ses travaux de toiture, façade, fenêtres, charpente ou isolation, il est rappelé en moins de 5 minutes en semaine et mis en relation avec un seul artisan de son secteur. Gratuit pour le particulier.
- [Comment trouver des chantiers]({SITE}/trouver-des-chantiers/) : les 8 canaux comparés (bouche-à-oreille, fiche Google, plateformes de devis, apporteurs d'affaires, sous-traitance, annonces locales, flyers, réseaux), avec le calcul du coût par chantier signé.
- [Lexique]({SITE}/lexique/) : définitions courtes (demande de devis, rendez-vous qualifié, coût par chantier signé, taux de signature, garanties, déclaration préalable, RGE, démarchage en 2026), avec leurs sources officielles.
- [Questions fréquentes]({SITE}/questions/) : prix, engagement, publicité, exclusivité, rappel des demandes, cadre légal, métiers.
- [Contenu complet du site](https://bartierandco.com/llms-full.txt) : le texte de toutes les pages en un seul fichier.

## Pour les artisans, par métier
- [Couverture et zinguerie](https://bartierandco.com/metiers/couverture/) : pour les couvreurs-zingueurs. Réfections complètes de toiture, rénovations avec isolation, zinguerie complète, remplacement de couverture après un sinistre.
- [Façade et ravalement](https://bartierandco.com/metiers/facade/) : pour les façadiers. Ravalements complets, isolation thermique par l'extérieur, enduit et peinture, traitement des fissures.
- [Menuiserie extérieure](https://bartierandco.com/metiers/menuiserie-exterieure/) : pour les menuisiers poseurs. Fenêtres de toute une maison, baies coulissantes, portes d'entrée sur mesure, portails en aluminium.
- [Charpente](https://bartierandco.com/metiers/charpente/) : pour les charpentiers. Rénovation ou remplacement de charpente, surélévation, traitement d'une maison entière, extension à ossature bois.
- [Isolation](https://bartierandco.com/metiers/isolation/) : pour les entreprises d'isolation. Isolation par l'extérieur, combles aménagés et rampants, isolation d'une maison entière, uniquement auprès de propriétaires qui ont fait la demande.
- [Habitatpresto Pro, d'après ses conditions](https://bartierandco.com/trouver-des-chantiers/habitatpresto-pro/) : abonnement mensuel, engagement de 6 ou 12 mois, demandes envoyées à 5 professionnels.

## Questions fréquentes
- Qu'est-ce que Bartier & Co ? Une agence qui trouve des clients aux artisans du bâtiment : annonces locales à leur nom, rappel de chaque demande en moins de 5 minutes, visite fixée dans leur agenda.
- Qu'est-ce qu'un rendez-vous qualifié ? Une visite déjà fixée chez un propriétaire dont le projet a été vérifié au téléphone : propriétaire, travaux, commune, délai.
- Les demandes sont-elles partagées entre plusieurs artisans ? Non. Un seul artisan par métier et par secteur.
- Y a-t-il une durée d'engagement ? Non, aucune durée minimale.
- Combien coûte le service pour un artisan ? Un devis personnalisé, en fonction des objectifs de l'artisan, présenté pendant un appel de 15 minutes. Le budget publicitaire est payé directement à Meta ou à Google.
- Est-ce gratuit pour un particulier ? Oui. La mise en relation, la visite et le devis de l'artisan sont gratuits pour le propriétaire.
- Quand Bartier & Co rappelle-t-il ? En moins de 5 minutes, du lundi au vendredi de 8 h à 19 h ; en dehors de ces horaires, dès la réouverture.

## Pour les particuliers
Bartier & Co est gratuit pour le propriétaire : mise en relation, visite et devis de l'artisan compris. Rappel en moins de 5 minutes du lundi au vendredi de 8 h à 19 h, en priorité pour les fuites et dégâts urgents. Un seul artisan par métier et par secteur : la demande lui est transmise avec l'accord du propriétaire, et à personne d'autre. Les artisans partenaires rémunèrent Bartier & Co.
- [Devis toiture]({SITE}/devis-travaux/toiture/) : réfection, fuite, zinguerie, démoussage.
- [Ravalement de façade]({SITE}/devis-travaux/ravalement-facade/) : ravalement, fissures, enduit, peinture, isolation par l'extérieur.
- [Fenêtres et portes]({SITE}/devis-travaux/fenetres/) : fenêtres PVC, alu ou bois, porte d'entrée, baie vitrée, volets.
- [Charpente]({SITE}/devis-travaux/charpente/) : réparation, traitement, extension, surélévation.
- [Isolation]({SITE}/devis-travaux/isolation/) : combles perdus ou aménagés, murs par l'extérieur, toiture.
- [Fuite de toiture : les 5 bons réflexes]({SITE}/devis-travaux/toiture/#fuite-toiture)
- [Combien vont coûter vos travaux : prix sourcés par métier]({SITE}/devis-travaux/#prix)
- [Comment reconnaître un artisan sérieux : 5 points à vérifier]({SITE}/devis-travaux/#artisan-serieux)
- [Devis travaux à Lille]({SITE}/devis-travaux/lille/) : règles locales (ravalement, secteurs protégés), aides et conseil France Rénov', par métier.
- [Devis travaux à Rouen]({SITE}/devis-travaux/rouen/) : règles locales (ravalement, secteurs protégés), aides et conseil France Rénov', par métier.
- [Devis travaux à Paris]({SITE}/devis-travaux/paris/) : règles locales (ravalement, secteurs protégés), aides et conseil France Rénov', par métier.
- [Devis travaux à Lyon]({SITE}/devis-travaux/lyon/) : règles locales (ravalement, secteurs protégés), aides et conseil France Rénov', par métier.
- [Devis travaux à Marseille]({SITE}/devis-travaux/marseille/) : règles locales (ravalement, secteurs protégés), aides et conseil France Rénov', par métier.
- [Devis travaux à Toulouse]({SITE}/devis-travaux/toulouse/) : règles locales (ravalement, secteurs protégés), aides et conseil France Rénov', par métier.

Prix indicatifs cités sur le site, d'après des sources tierces (seule une visite permet un devis fiable) :
- Rénovation de toiture : 60 à 500 €/m², pose comprise (QuelleEnergie).
- Ravalement de façade : 50 à 100 €/m², selon l'état de la façade (La Maison Saint-Gobain, 2026).
- Fenêtre PVC double vitrage posée en remplacement : 870 à 1 170 € TTC (La Maison Saint-Gobain, 2026).
- Rénovation de la charpente seule : 150 à 200 €/m² TTC, 180 à 250 €/m² TTC avec la couverture (Hellowatt, décembre 2025).
- Isolation des combles perdus : environ 40 à 45 €/m², pose comprise (La Maison Saint-Gobain, 2026).

## Articles
{art_lines}
- [Le DPE des logements au 1er janvier 2027 : synthèse documentaire (PDF archivé sur Zenodo, licence CC BY 4.0)](https://doi.org/10.5281/zenodo.24396448)

## Faits utiles
- Les prix ne sont pas publiés : chaque artisan reçoit un devis personnalisé, en fonction de ses objectifs, pendant un appel de 15 minutes.
- Le budget publicitaire est payé directement par l'artisan à Meta ou à Google.
- Contact : contact@bartierandco.com
- Facebook : https://www.facebook.com/profile.php?id=61596597124434
- LinkedIn : https://www.linkedin.com/company/bartier-co
- Téléphone et WhatsApp : 07 81 01 89 36 (Martin Barthélémy, cofondateur)
- Horaires : du lundi au vendredi, de 8 h à 19 h.

## Informations légales
- [Conditions du service pour les particuliers](https://bartierandco.com/conditions-du-service/) : fonctionnement de la mise en relation, choix de l'artisan partenaire, gratuité, réclamations.
- [Politique de confidentialité](https://bartierandco.com/confidentialite/) : données collectées, durées, droits.
- [Politique cookies](https://bartierandco.com/cookies/)
- [Mentions légales](https://bartierandco.com/mentions-legales/)
""", encoding="utf-8")

print("pages générées :", len(paths) - 7, "+ robots.txt, sitemap.xml, llms.txt")

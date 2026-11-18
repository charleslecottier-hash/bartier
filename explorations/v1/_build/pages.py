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
      <div class="t-row" role="row"><span role="rowheader">La demande</span><span role="cell">Exprimée : le propriétaire cherche déjà</span><span role="cell">Suscitée : il n'a pas encore cherché</span></div>
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
    ("Qui rappelle les demandes ?", "Notre équipe, en moins de cinq minutes, en semaine de 8 h à 19 h. Vous ne recevez que des rendez-vous qualifiés."),
]
page("/google-ads/", "Google Ads pour artisans du bâtiment | Bartier & Co",
     "Campagnes Google Ads locales pour couvreurs, façadiers et menuisiers : captez les propriétaires qui cherchent déjà, rappelés en moins de cinq minutes.",
     "\n\n".join([
         hero("Google Ads", "Captez les propriétaires qui cherchent déjà.",
              "Ils tapent « couvreur » et le nom de leur ville. Nous faisons en sorte qu'ils tombent sur vous, puis nous les rappelons en moins de cinq minutes.",
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
                     "Chaque appel et chaque formulaire suivis jusqu'au rendez-vous",
                     "Rappel en moins de cinq minutes, qualification, rendez-vous dans votre agenda"], grey=True),
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
    ("Quel budget prévoir ?", "Il dépend de votre secteur et du nombre de rendez-vous que vous pouvez absorber. Nous l'estimons ensemble. Vous le payez directement à Meta."),
    ("Est-ce légal de rappeler ces personnes ?", "Oui. Le formulaire demande leur accord explicite pour être recontactées par votre entreprise, et la preuve est conservée. Nous ne démarchons personne."),
    ("Les demandes Facebook sont-elles sérieuses ?", "Pas toutes. C'est pourquoi chaque demande est rappelée et vérifiée avant d'arriver dans votre agenda : propriétaire, projet, commune, délai."),
]
page("/meta-ads/", "Publicité Facebook et Instagram pour artisans | Bartier & Co",
     "Annonces Facebook et Instagram locales pour artisans du bâtiment : les propriétaires de votre secteur, rappelés en moins de cinq minutes et qualifiés.",
     "\n\n".join([
         hero("Meta Ads · Facebook et Instagram", "Touchez les propriétaires avant qu'ils ne cherchent.",
              "Des annonces à votre nom, à 25 à 40 km de votre dépôt. Chaque demande est rappelée en moins de cinq minutes, puis qualifiée.",
              crumbs(("Meta Ads", "/meta-ads/")), ("Comparer avec Google", "/google-ads/")),
         cols([("Un rayon autour du dépôt", "25 à 40 km, réglés commune par commune selon vos chantiers."),
               ("Vos vraies photos", "Vos chantiers, votre équipe. Rien de plus convaincant pour un voisin."),
               ("Des angles de saison", "Après les intempéries, avant l'hiver, au printemps pour la rénovation.")],
              "Comment nous diffusons", "Des annonces locales, au nom de votre entreprise."),
         split_list("Du clic au rendez-vous", "Rien ne part sans être vérifié.",
                    "Une demande Facebook n'est qu'un début. Le tri se fait au téléphone.",
                    ["Formulaire avec questions de tri et accord explicite d'être recontacté",
                     "Preuve du consentement conservée pour chaque demande",
                     "Rappel en moins de cinq minutes, en semaine de 8 h à 19 h",
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
      <p>Nous avons donc construit un système simple : des annonces locales, un rappel en moins de cinq minutes, et un rendez-vous réservé à un seul artisan.</p>
    </div>
  </div>
</section>""",
         cols([("Un interlocuteur, pas un standard", "Vous avez le numéro de Charles et de Martin. L'un de nous répond."),
               ("Des engagements écrits", "Exclusivité, un artisan par secteur, rappel en cinq minutes, sans engagement de durée."),
               ("Des chiffres vérifiables", "Le budget publicitaire est sur votre compte, et chaque rendez-vous est suivi jusqu'au chantier signé.")],
              "Comment nous travaillons", "Simple, joignable, honnête.", grey=True),
         """<section class="section">
  <div class="wrap tm">
    <div class="tm-text">
      <p class="kicker">Les fondateurs</p>
      <h2>Charles et Martin.</h2>
      <p class="sub">Charles, Head of Performance, pilote les annonces, le rappel et les résultats. Martin, Head of Sales, est votre interlocuteur du premier appel au démarrage.</p>
    </div>
    <div class="tm-people">
      <figure><div class="ph" role="img" aria-label="Portrait de Charles Le Cottier, à venir"></div><figcaption><b>Charles Le Cottier</b><small>Cofondateur · Head of Performance</small></figcaption></figure>
      <figure><div class="ph" role="img" aria-label="Portrait de Martin Barthélémy, à venir"></div><figcaption><b>Martin Barthélémy</b><small>Cofondateur · Head of Sales</small></figcaption></figure>
    </div>
  </div>
</section>""",
         ENG_SECTION,
         FORM,
     ]), nav="/qui-sommes-nous/",
     schema={"@context": "https://schema.org", "@graph": [
         {"@type": "AboutPage", "name": "Qui sommes-nous", "url": SITE + "/qui-sommes-nous/"},
         {"@type": "Organization", "name": "Bartier & Co", "legalName": "Bartier & Co SAS", "url": SITE + "/", "founder": [
             {"@type": "Person", "name": "Charles Le Cottier", "jobTitle": "Cofondateur, Head of Performance"},
             {"@type": "Person", "name": "Martin Barthélémy", "jobTitle": "Cofondateur, Head of Sales"}]},
         breadcrumb_ld(("Qui sommes-nous", "/qui-sommes-nous/"))]})

# ——— Blog ———
ARTICLES = [
    {
        "slug": "lead-partage-lead-exclusif-rendez-vous-qualifie",
        "tag": "Comprendre",
        "title": "Lead partagé, lead exclusif, rendez-vous qualifié : les différences pour un artisan",
        "short": "Lead partagé, exclusif ou rendez-vous qualifié : ce qui change pour vous",
        "desc": "Trois offres qui se ressemblent sur le papier, mais pas sur le terrain. Ce que chacune vous livre vraiment, et les questions à poser avant de signer.",
        "minutes": 5,
        "body": """
<p class="answer">Un <b>lead partagé</b> est une demande de devis vendue à plusieurs entreprises. Un <b>lead exclusif</b> n'est vendu qu'à vous, mais c'est à vous de rappeler. Un <b>rendez-vous qualifié</b> est une visite déjà fixée, chez un propriétaire dont le projet a été vérifié.</p>

<h2>Trois choses différentes</h2>
<p>Le vocabulaire marketing mélange tout. Pour un artisan, il n'y a que trois questions : combien d'entreprises reçoivent la même demande, qui rappelle le propriétaire, et qu'est-ce qui a été vérifié avant que vous vous déplaciez.</p>

<h2>Le lead partagé : la même fiche vendue plusieurs fois</h2>
<p>Vous recevez un nom, un numéro et une description du projet. D'autres entreprises reçoivent la même fiche, au même moment. Le propriétaire est appelé plusieurs fois, compare les prix, et retient souvent le premier qui rappelle ou le moins cher.</p>

<h2>Le lead exclusif : exclusif jusqu'où ?</h2>
<p>La fiche n'est vendue qu'à vous. C'est mieux, mais vérifiez ce que recouvre le mot. Exclusif pendant combien de temps ? Sur quelle zone ? Et surtout : qui rappelle ? Si c'est vous, le soir, la demande a souvent refroidi.</p>

<h2>Le rendez-vous qualifié : ce qui a été vérifié</h2>
<p>Quelqu'un a rappelé le propriétaire, vérifié qu'il est propriétaire occupant, compris son projet, confirmé la commune, puis fixé une date avec lui. Vous recevez une visite dans votre agenda, pas une fiche à traiter.</p>

<h2>Le tableau</h2>
<table>
<thead><tr><th></th><th>Lead partagé</th><th>Lead exclusif</th><th>Rendez-vous qualifié</th></tr></thead>
<tbody>
<tr><td>Entreprises sur la même demande</td><td>Plusieurs</td><td>Une</td><td>Une</td></tr>
<tr><td>Qui rappelle</td><td>Vous</td><td>Vous</td><td>Le prestataire</td></tr>
<tr><td>Projet vérifié</td><td>Rarement</td><td>Parfois</td><td>Oui</td></tr>
<tr><td>Ce que vous recevez</td><td>Une fiche</td><td>Une fiche</td><td>Une visite fixée</td></tr>
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
<p>Nos réponses sont sur la page <a href="/#engagements">Engagements</a>.</p>
""",
    },
    {
        "slug": "google-ads-ou-meta-ads-artisan",
        "tag": "Publicité",
        "title": "Google Ads ou Meta Ads pour un artisan du bâtiment : qui capte quelle demande",
        "short": "Google Ads ou Meta Ads : qui capte quelle demande",
        "desc": "Google capte ceux qui cherchent déjà, Meta touche ceux qui n'ont pas encore cherché. Comment choisir selon votre métier et votre secteur.",
        "minutes": 4,
        "body": """
<p class="answer"><b>Google Ads</b> capte une demande qui existe déjà : le propriétaire cherche un artisan. <b>Meta Ads</b> (Facebook et Instagram) suscite une demande chez des propriétaires qui n'ont pas encore cherché. Le premier convient aux urgences et aux projets mûrs, le second aux rénovations et à l'entretien.</p>

<h2>Demande exprimée ou demande suscitée</h2>
<p>Sur Google, le propriétaire tape « couvreur » et le nom de sa ville. Il a un besoin, souvent précis, parfois urgent. Sur Facebook ou Instagram, il ne cherche rien : il voit une annonce d'une entreprise de son secteur, et elle tombe au bon moment, ou non.</p>

<h2>Urgence ou projet de rénovation</h2>
<p>Une fuite après un coup de vent se cherche sur Google. Une toiture qui verdit, des fenêtres de vingt ans ou une façade fatiguée sont des projets que le propriétaire repousse : une annonce bien placée les fait avancer.</p>

<h2>Le coût : ce qui dépend de vous</h2>
<p>Sur Google, le prix du clic dépend du métier et de la concurrence locale. Sur Meta, le budget se règle librement, mais toutes les demandes ne sont pas sérieuses. Dans les deux cas, le vrai coût est celui du chantier signé, pas celui du clic.</p>

<h2>Ce que chaque canal exige après le clic</h2>
<ul>
<li><b>Google</b> : écarter les recherches inutiles (gratuit, emploi, bricolage) et répondre vite, car le propriétaire appelle plusieurs entreprises.</li>
<li><b>Meta</b> : qualifier au téléphone, car une partie des demandes est encore au stade de l'idée.</li>
</ul>
<p>Dans les deux cas, la demande doit être rappelée en quelques minutes. C'est là que la plupart des campagnes perdent leurs meilleurs projets.</p>

<h2>Notre choix, et ses limites</h2>
<p>Nous commençons le plus souvent par Meta pour les métiers de rénovation (couverture, façade, menuiserie, isolation), parce que le volume se construit dans un rayon précis. Nous ajoutons Google quand votre secteur a assez de recherches locales. Ce n'est pas une règle : certains secteurs ruraux n'ont pas assez de recherches pour Google, et certains métiers vivent surtout de l'urgence.</p>
<p>Voir aussi : <a href="/google-ads/">Google Ads</a> et <a href="/meta-ads/">Meta Ads</a>.</p>
""",
    },
    {
        "slug": "relance-devis-artisan",
        "tag": "Méthode",
        "title": "Relance de devis : calendrier, SMS et script d'appel pour artisans",
        "short": "Relance de devis : le calendrier, les SMS et le script",
        "desc": "Un devis de plusieurs milliers d'euros se relance. Un calendrier simple, trois SMS prêts à copier et un script d'appel de deux minutes.",
        "minutes": 5,
        "body": """
<p class="answer">Relancez un devis de rénovation <b>par un appel</b>, quelques jours après l'envoi, puis <b>par SMS</b> si vous n'avez pas de réponse. Arrêtez après trois tentatives sans retour, en laissant la porte ouverte. Le but n'est pas d'insister : c'est de savoir où en est le projet.</p>

<h2>Le calendrier</h2>
<table>
<thead><tr><th>Quand</th><th>Quoi</th><th>Pourquoi</th></tr></thead>
<tbody>
<tr><td>Le jour de l'envoi</td><td>SMS court</td><td>Confirmer que le devis est bien arrivé</td></tr>
<tr><td>Quelques jours après</td><td>Appel</td><td>Répondre aux questions avant qu'il compare</td></tr>
<tr><td>Une semaine plus tard</td><td>SMS</td><td>Proposer un rappel au moment qui l'arrange</td></tr>
<tr><td>Deux à trois semaines plus tard</td><td>Dernier SMS</td><td>Clore poliment et laisser la porte ouverte</td></tr>
</tbody>
</table>
<p>Adaptez le rythme au projet : une urgence se relance plus vite qu'une rénovation prévue pour le printemps.</p>

<h2>Trois SMS prêts à copier</h2>
<blockquote>Bonjour Madame Durand, c'est Julien de l'entreprise Martin Couverture. Je vous ai envoyé le devis pour votre toiture par e-mail. Dites-moi s'il est bien arrivé. Bonne journée.</blockquote>
<blockquote>Bonjour Madame Durand, avez-vous pu regarder le devis pour la toiture ? Je peux vous rappeler pour en parler, à l'heure qui vous arrange.</blockquote>
<blockquote>Bonjour Madame Durand, je ne veux pas vous déranger davantage. Si le projet revient, je reste disponible. Bonne continuation.</blockquote>
<p>Les noms sont des exemples. Gardez le vôtre, celui de l'entreprise, et le projet précis.</p>

<h2>Un script d'appel de deux minutes</h2>
<ol>
<li><b>Le contexte</b> : « Bonjour, c'est Julien, je suis passé jeudi pour votre toiture. Vous avez deux minutes ? »</li>
<li><b>La question ouverte</b> : « Qu'avez-vous pensé du devis ? »</li>
<li><b>L'écoute</b> : le prix, le délai, une question technique, un autre devis.</li>
<li><b>La prochaine étape</b> : « Je vous propose qu'on se rappelle vendredi, après que vous en aurez parlé ensemble. »</li>
</ol>

<h2>Quand arrêter</h2>
<p>Après trois tentatives sans réponse, arrêtez. Un dernier message poli laisse une meilleure impression qu'un quatrième appel, et le propriétaire reviendra parfois quelques mois plus tard.</p>

<h2>Mesurez</h2>
<p>Notez pour chaque devis : envoyé, relancé, signé ou perdu, et pourquoi. Au bout de quelques mois, vous saurez quels projets vous signez, et où partent les autres.</p>
""",
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

User-agent: Bingbot
Allow: /

Sitemap: https://bartierandco.com/sitemap.xml
""", encoding="utf-8")

urls = "\n".join(f"  <url><loc>{SITE}{p}</loc><lastmod>{TODAY}</lastmod></url>" for p in paths)
(ROOT / "sitemap.xml").write_text(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}\n</urlset>\n', encoding="utf-8")

art_lines = "\n".join(f"- [{fr(a['short'])}]({SITE}/blog/{a['slug']}/) : {fr(a['desc'])}" for a in ARTICLES)
(ROOT / "llms.txt").write_text(f"""# Bartier & Co

> Bartier & Co trouve des clients aux artisans du bâtiment à gros chantiers (couverture, façade, menuiserie extérieure, charpente, isolation) partout en France. Bartier & Co diffuse des annonces locales (Meta Ads, Google Ads), rappelle chaque demande en moins de cinq minutes en semaine de 8 h à 19 h, vérifie le projet et fixe la visite chez le propriétaire, directement dans l'agenda de l'artisan. Les rendez-vous ne sont proposés qu'à un seul artisan par métier et par secteur. Sans engagement de durée. Société : Bartier & Co SAS (France). Fondateurs : Charles Le Cottier et Martin Barthélémy.

## Pages principales
- [Accueil]({SITE}/) : la méthode, les engagements et le formulaire pour vérifier si un secteur est libre.
- [Métiers]({SITE}/metiers/) : couverture et zinguerie, façade et ravalement, menuiserie extérieure, charpente, isolation.
- [Google Ads]({SITE}/google-ads/) : campagnes locales pour capter les propriétaires qui cherchent déjà un artisan.
- [Meta Ads]({SITE}/meta-ads/) : annonces Facebook et Instagram dans un rayon de 25 à 40 km autour du dépôt.
- [Qui sommes-nous]({SITE}/qui-sommes-nous/) : les fondateurs et la façon de travailler.
- [Devis travaux, pour les particuliers]({SITE}/devis-travaux/) : un propriétaire décrit ses travaux de toiture, façade, fenêtres, charpente ou isolation, il est rappelé en moins de cinq minutes en semaine et mis en relation avec un seul artisan de son secteur. Gratuit pour le particulier.

## Articles
{art_lines}

## Faits utiles
- Les prix ne sont pas publiés : ils dépendent du métier et du secteur, et sont donnés pendant un appel de 15 minutes.
- Le budget publicitaire est payé directement par l'artisan à Meta ou à Google.
- Contact : contact@bartierandco.com
- Facebook : https://www.facebook.com/profile.php?id=61596597124434
- Téléphone et WhatsApp : 07 81 01 89 36 (Martin Barthélémy, Head of Sales)
""", encoding="utf-8")

print("pages générées :", len(paths) - 7, "+ robots.txt, sitemap.xml, llms.txt")

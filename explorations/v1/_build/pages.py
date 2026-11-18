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
                     "Chaque appel et chaque formulaire suivis jusqu'au rendez-vous",
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
    ("Faut-il des photos de mes chantiers ?", "Oui, c'est ce qui convainc le mieux un voisin. Vos vraies photos de chantier et de votre équipe passent avant les images de banque."),
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
                    ["Formulaire avec questions de tri et accord explicite d'être recontacté",
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
        "desc": "Trois offres qui se ressemblent sur le papier, mais pas sur le terrain. Ce que chacune vous livre vraiment, et les questions à poser avant de signer.",
        "minutes": 5,
        "body": """
<p class="answer">Une <b>demande partagée</b> est une demande de devis vendue à plusieurs entreprises. Une <b>demande exclusive</b> n'est vendue qu'à vous, mais c'est à vous de rappeler. Un <b>rendez-vous qualifié</b> est une visite déjà fixée, chez un propriétaire dont le projet a été vérifié.</p>

<h2>Quelle différence entre une demande de devis et un rendez-vous qualifié ?</h2>
<p>Le vocabulaire marketing mélange tout, et les plateformes parlent de « leads ». Pour un artisan, il n'y a que trois questions : combien d'entreprises reçoivent la même demande, qui rappelle le propriétaire, et qu'est-ce qui a été vérifié avant que vous vous déplaciez.</p>

<h2>La demande partagée : la même demande vendue plusieurs fois</h2>
<p>Vous recevez un nom, un numéro et une description du projet. D'autres entreprises reçoivent la même demande, au même moment. Le propriétaire est appelé plusieurs fois, compare les prix, et retient souvent le premier qui rappelle ou le moins cher.</p>

<h2>La demande exclusive : exclusive jusqu'où ?</h2>
<p>La demande n'est vendue qu'à vous. C'est mieux, mais vérifiez ce que recouvre le mot. Exclusif pendant combien de temps ? Sur quelle zone ? Et surtout : qui rappelle ? Si c'est vous, le soir, la demande a souvent refroidi.</p>

<h2>Le rendez-vous qualifié : ce qui a été vérifié</h2>
<p>Quelqu'un a rappelé le propriétaire, vérifié qu'il est propriétaire occupant, compris son projet, confirmé la commune, puis fixé une date avec lui. Vous recevez directement une visite dans votre agenda, sans personne à rappeler.</p>

<h2>Demande partagée, demande exclusive, rendez-vous qualifié : le comparatif</h2>
<table>
<thead><tr><th></th><th>Demande partagée</th><th>Demande exclusive</th><th>Rendez-vous qualifié</th></tr></thead>
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
        "desc": "Google capte ceux qui cherchent déjà, Meta touche ceux qui n'ont pas encore cherché. Comment choisir selon votre métier et votre secteur.",
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
        "desc": "Un devis de rénovation se relance. Un calendrier simple, trois SMS prêts à copier et un script d'appel de deux minutes.",
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

> Bartier & Co trouve des clients aux artisans du bâtiment à gros chantiers (couverture, façade, menuiserie extérieure, charpente, isolation) partout en France. Bartier & Co diffuse des annonces locales (Meta Ads, Google Ads), rappelle chaque demande en moins de 5 minutes en semaine de 8 h à 19 h, vérifie le projet et fixe la visite chez le propriétaire, directement dans l'agenda de l'artisan. Les rendez-vous ne sont proposés qu'à un seul artisan par métier et par secteur. Sans engagement de durée. Société : Bartier & Co SAS, 6 rue Saint-Bon, 75004 Paris (France). Fondateurs : Charles Le Cottier et Martin Barthélémy.

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

## Articles
{art_lines}

## Faits utiles
- Les prix ne sont pas publiés : chaque artisan reçoit un devis personnalisé, en fonction de ses objectifs, pendant un appel de 15 minutes.
- Le budget publicitaire est payé directement par l'artisan à Meta ou à Google.
- Contact : contact@bartierandco.com
- Facebook : https://www.facebook.com/profile.php?id=61596597124434
- Téléphone et WhatsApp : 07 81 01 89 36 (Martin Barthélémy, responsable commercial)
- Horaires : du lundi au vendredi, de 8 h à 19 h.

## Informations légales
- [Conditions du service pour les particuliers](https://bartierandco.com/conditions-du-service/) : fonctionnement de la mise en relation, choix de l'artisan partenaire, gratuité, réclamations.
- [Politique de confidentialité](https://bartierandco.com/confidentialite/) : données collectées, durées, droits.
- [Politique cookies](https://bartierandco.com/cookies/)
- [Mentions légales](https://bartierandco.com/mentions-legales/)
""", encoding="utf-8")

print("pages générées :", len(paths) - 7, "+ robots.txt, sitemap.xml, llms.txt")

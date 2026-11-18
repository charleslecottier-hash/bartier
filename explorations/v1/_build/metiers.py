"""Génère les pages métiers (/metiers/<slug>/) et la page /metiers/ à partir de index.html.

L'en-tête, le pied de page et le formulaire sont repris de la page d'accueil :
une modification faite dans index.html se propage en relançant ce script.

    python3 _build/metiers.py
"""
import html
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
HOME = (ROOT / "index.html").read_text(encoding="utf-8")


def between(start, end):
    i = HOME.index(start)
    j = HOME.index(end, i) + len(end)
    return HOME[i:j]


def absolutize(block):
    """Liens d'ancre de la page d'accueil -> liens absolus depuis une sous-page."""
    block = block.replace('href="#top"', 'href="/"')
    block = re.sub(r'href="#(?!secteur|contenu)([\w-]+)"', r'href="/#\1"', block)
    block = block.replace('src="', 'src="/').replace('href="favicon', 'href="/favicon')
    return block


HEADER = absolutize(between('<a class="skip"', "</header>"))
FOOTER = absolutize(between('<footer class="site-footer">', "</footer>"))
FORM = between("<!-- Formulaire -->", "</section>")
HEAD_SCRIPT = between("<script>(function(d)", "</script>")
ENGAGEMENTS = between('<ul class="en">', "</ul>")
GUARANTEE = absolutize(between('<div class="guarantee">', "</div>"))
MOBILE_CTA = between('<a class="mobile-cta', "</a>")

T = "’"  # apostrophe typographique
NB = " "  # espace insécable


def fr(text):
    """Apostrophes typographiques et espaces insécables avant ; : ? !"""
    text = text.replace("'", T)
    return re.sub(r" ([;:?!])", NB + r"\1", text)


TRADES = [
    {
        "slug": "couverture",
        "radio": "couverture",
        "name": "Couverture et zinguerie",
        "who": "Couvreurs-zingueurs",
        "title": "Trouver des chantiers de couverture",
        "h1": "Couvreurs : des rendez-vous de réfection,",
        "h1_em": "pas des appels de dépannage.",
        "lede": "Nous allons chercher les propriétaires qui préparent une réfection, une rénovation ou une zinguerie complète près de votre dépôt. Nous les rappelons en moins de 5 minutes, nous vérifions le projet, puis nous posons la visite dans votre agenda.",
        "keep": ["Réfection complète de toiture", "Rénovation de toiture avec isolation", "Démoussage et hydrofuge d'une toiture entière", "Zinguerie complète : gouttières, chéneaux, noues", "Remplacement de couverture après un sinistre"],
        "drop": ["Une tuile à remettre en place", "Une petite fuite à dépanner", "Les locataires et les demandes hors de votre zone"],
        "problems": [
            ("Trop de dépannages, pas assez de chantiers.", "Une tuile déplacée, une gouttière bouchée : vous vous déplacez pour un devis de quelques centaines d'euros, pendant qu'une réfection part chez un autre."),
            ("Un planning qui suit la météo.", "Après un coup de vent, tout le monde appelle en même temps. Puis plus rien pendant des semaines. Difficile de prévoir le travail d'une équipe."),
            ("Une demande partagée entre plusieurs couvreurs.", "Sur les plateformes, le propriétaire reçoit plusieurs appels pour la même toiture. Il compare des prix, rarement la qualité du travail."),
        ],
        "questions": ["Êtes-vous propriétaire de la maison et l'occupez-vous ?", "Quels travaux envisagez-vous : réfection, rénovation, démoussage, zinguerie, fuite ?", "Quel est le matériau de la toiture et quel est son âge, à peu près ?", "Quelle est la taille de la maison ?", "Dans quelle commune se trouve-t-elle ?", "Quand souhaitez-vous faire les travaux ?"],
        "angles": [
            ("Après les intempéries", "Votre toiture a-t-elle souffert des derniers coups de vent ? Faites-la vérifier par un couvreur de votre secteur."),
            ("Toiture de plus de quinze ans", "Une toiture qui verdit devient poreuse au gel. Faites le point avant que l'eau n'atteigne l'isolation."),
            ("Rénovation complète", "Réfection de toiture par une entreprise locale, avec garantie décennale. Étude et chiffrage à domicile."),
        ],
        "faq": [
            ("Vous m'envoyez aussi des petits dépannages ?", "Non. Nos annonces et nos questions écartent les petits dépannages. Si un propriétaire signale une urgence, nous vous le précisons avant de proposer le créneau, et vous restez libre de refuser."),
            ("Les demandes arrivent-elles seulement après une tempête ?", "Non. Nous alternons les angles selon la saison : vérification après intempéries, entretien avant l'hiver, rénovation complète au printemps. L'objectif est un agenda régulier."),
        ],
    },
    {
        "slug": "menuiserie-exterieure",
        "radio": "menuiserie",
        "name": "Menuiserie extérieure",
        "who": "Menuisiers poseurs",
        "title": "Trouver des chantiers de menuiserie extérieure",
        "h1": "Menuisiers : des projets de maison entière,",
        "h1_em": "pas des prix à la fenêtre.",
        "lede": "Nous allons chercher les propriétaires qui veulent remplacer leurs fenêtres, leur baie ou leur porte d'entrée, près de votre atelier. Nous les rappelons en moins de 5 minutes, nous vérifions l'ampleur du projet, puis nous posons la visite dans votre agenda.",
        "keep": ["Remplacement de toutes les fenêtres d'une maison", "Baies coulissantes et galandages", "Portes d'entrée sur mesure", "Volets roulants posés avec les fenêtres", "Portails et clôtures en aluminium"],
        "drop": ["Une seule fenêtre à changer", "La pose de matériel acheté ailleurs", "Les locataires et les demandes hors de votre zone"],
        "problems": [
            ("Des propriétaires échaudés par les fausses promesses.", "Le secteur a connu les offres trop belles et les aides annoncées à tort. Beaucoup de propriétaires arrivent méfiants, ou avec des attentes impossibles."),
            ("Une mise en concurrence avec les grandes enseignes.", "Le propriétaire compare votre devis au prix d'une fenêtre en magasin. Sans échange avant la visite, il ne voit pas ce qui justifie l'écart."),
            ("Des projets qui s'endorment après le devis.", "Entre la visite et la décision, il peut s'écouler des semaines. Sans relance, le projet passe au second plan, ou chez un concurrent."),
        ],
        "questions": ["Êtes-vous propriétaire de la maison et l'occupez-vous ?", "Combien de menuiseries souhaitez-vous remplacer ?", "Quel matériau envisagez-vous : PVC, aluminium, bois ?", "S'agit-il de la maison entière ou de quelques ouvertures ?", "Dans quelle commune se trouve la maison ?", "Quand souhaitez-vous faire les travaux ?"],
        "angles": [
            ("Fenêtres de plus de vingt ans", "Courants d'air, condensation, bruit de la rue ? Faites étudier le remplacement de vos fenêtres par un menuisier de votre secteur."),
            ("La baie vitrée", "Une baie coulissante sur mesure, posée par un artisan local. Visite et chiffrage à domicile."),
            ("La porte d'entrée", "Une porte d'entrée isolante et sûre, fabriquée sur mesure. Choisissez-la avec un professionnel, chez vous."),
        ],
        "faq": [
            ("Les propriétaires savent-ils que vous ne vendez pas d'aides ?", "Oui. Nos annonces ne promettent ni aide ni prix d'appel. Le propriétaire sait qu'il rencontre une entreprise pour un devis, et notre équipe le lui confirme au téléphone."),
            ("Je travaille surtout l'aluminium. Pouvez-vous filtrer ?", "Oui. Nous adaptons les annonces et les questions à ce que vous posez : matériaux, gammes, types d'ouvertures. Les projets hors de votre offre sont écartés."),
        ],
    },
    {
        "slug": "facade",
        "radio": "facade",
        "name": "Façade et ravalement",
        "who": "Façadiers",
        "title": "Trouver des chantiers de façade",
        "h1": "Façadiers : des ravalements complets,",
        "h1_em": "pas des demandes de nettoyage.",
        "lede": "Nous allons chercher les propriétaires qui préparent un ravalement ou une isolation par l'extérieur près de votre dépôt. Nous les rappelons en moins de 5 minutes, nous vérifions le projet, puis nous posons la visite dans votre agenda, avec les deux décideurs.",
        "keep": ["Ravalement complet de maison", "Isolation thermique par l'extérieur", "Enduit, crépi et peinture de façade", "Traitement des fissures et imperméabilisation"],
        "drop": ["Un simple nettoyage haute pression", "Les petites retouches", "Les locataires et les demandes hors de votre zone"],
        "problems": [
            ("Une décision qui se prend à deux.", "Un ravalement se décide en couple, après plusieurs devis. Une visite faite sans les deux décideurs est souvent une visite à refaire."),
            ("Des chantiers qui se signent au printemps.", "Les propriétaires pensent à leur façade quand il fait beau. Pour travailler toute la belle saison, l'agenda doit se remplir dès l'hiver."),
            ("Une demande partagée entre plusieurs entreprises.", "Sur les plateformes, plusieurs façadiers reçoivent la même demande. Le propriétaire compare des prix au mètre carré, pas des méthodes."),
        ],
        "questions": ["Êtes-vous propriétaire de la maison et l'occupez-vous ?", "Quels travaux envisagez-vous : ravalement, isolation par l'extérieur, fissures, peinture ?", "Combien d'étages et quelle surface de façade, à peu près ?", "Les deux décideurs pourront-ils être présents à la visite ?", "Dans quelle commune se trouve la maison ?", "Quand souhaitez-vous faire les travaux ?"],
        "angles": [
            ("Façade fatiguée", "Fissures, traces noires, enduit qui se décolle ? Faites étudier le ravalement de votre façade par une entreprise locale."),
            ("Préparer le printemps", "Les plannings de ravalement se remplissent dès l'hiver. Faites chiffrer votre façade maintenant."),
            ("Isoler par l'extérieur", "Isolation et ravalement en un seul chantier. Étude et chiffrage à domicile par un professionnel de votre secteur."),
        ],
        "faq": [
            ("Travaillez-vous avec les copropriétés ?", "Notre méthode vise les maisons individuelles, où le propriétaire décide seul ou en couple. Pour les copropriétés, parlons-en pendant l'appel."),
            ("Pouvez-vous viser seulement l'isolation par l'extérieur ?", "Oui. Les annonces et les questions s'adaptent aux chantiers que vous voulez développer en priorité."),
        ],
    },
    {
        "slug": "charpente",
        "radio": "charpente",
        "name": "Charpente",
        "who": "Charpentiers",
        "title": "Trouver des chantiers de charpente",
        "h1": "Charpentiers : des projets prêts à démarrer,",
        "h1_em": "pas des idées pour dans trois ans.",
        "lede": "Nous allons chercher les propriétaires qui ont un projet de charpente concret près de votre atelier. Nous les rappelons en moins de 5 minutes, nous vérifions où en est le projet, puis nous posons la visite dans votre agenda.",
        "keep": ["Rénovation ou remplacement de charpente", "Surélévation de maison", "Traitement de charpente sur une maison entière", "Extension à ossature bois"],
        "drop": ["Les abris de jardin et petits ouvrages", "Les projets sans calendrier", "Les locataires et les demandes hors de votre zone"],
        "problems": [
            ("Des projets longs à mûrir.", "Une surélévation ou une extension passe par des plans et des démarches. Beaucoup de demandes arrivent bien trop tôt pour signer."),
            ("Des demandes mêlées à la couverture.", "Les propriétaires ne distinguent pas toujours charpente et couverture. Sans tri, vous recevez des demandes qui ne relèvent pas de votre métier."),
            ("Un savoir-faire difficile à montrer.", "Le propriétaire compare des devis sans voir la différence entre deux charpentes. La visite est le moment où tout se joue."),
        ],
        "questions": ["Êtes-vous propriétaire de la maison et l'occupez-vous ?", "Quel est votre projet : rénovation, remplacement, surélévation, extension, traitement ?", "Où en sont les plans et les démarches administratives ?", "Dans quelle commune se trouve la maison ?", "Quand souhaitez-vous commencer les travaux ?"],
        "angles": [
            ("Agrandir sans déménager", "Surélévation ou extension bois : faites étudier votre projet par un charpentier de votre secteur."),
            ("Charpente à vérifier", "Bois attaqué, déformation, tuiles qui ondulent ? Faites contrôler votre charpente par un professionnel."),
        ],
        "faq": [
            ("Mes chantiers ont des cycles longs. Est-ce adapté ?", "Oui, à condition de trier tôt. Nos questions portent sur l'avancement des plans et des démarches : vous ne rencontrez que des propriétaires dont le projet peut démarrer."),
            ("Pouvez-vous écarter les demandes de couverture ?", "Oui. Ou, si vous faites aussi la couverture, les garder. Nous réglons le tri selon ce que vous réalisez."),
        ],
    },
    {
        "slug": "isolation",
        "radio": "isolation",
        "name": "Isolation",
        "who": "Entreprises d'isolation",
        "title": "Trouver des chantiers d'isolation",
        "h1": "Isolation : des propriétaires qui ont fait la demande,",
        "h1_em": "jamais du démarchage.",
        "lede": "Le secteur a souffert du démarchage et des offres trop belles. Nous faisons l'inverse : seuls les propriétaires qui ont fait une demande et accepté d'être recontactés sont rappelés, en moins de 5 minutes, avant que la visite soit posée dans votre agenda.",
        "keep": ["Isolation thermique par l'extérieur", "Isolation des combles aménagés et des rampants", "Isolation des combles perdus avec d'autres travaux", "Isolation par l'intérieur d'une maison entière"],
        "drop": ["Les demandes d'offres à prix symbolique", "Les projets dont l'éligibilité aux aides est la seule motivation", "Les locataires et les demandes hors de votre zone"],
        "problems": [
            ("Un secteur abîmé par le démarchage.", "Après des années d'appels non sollicités, les propriétaires se méfient. Le démarchage téléphonique dans la rénovation énergétique est d'ailleurs interdit."),
            ("Des demandes motivées par les seules aides.", "Beaucoup de demandes ne portent que sur l'aide promise. Quand elle ne correspond pas à leur situation, le projet s'arrête."),
            ("Une demande partagée entre plusieurs entreprises.", "Sur les plateformes, la même demande part chez plusieurs entreprises. Le propriétaire choisit souvent le moins cher, pas le mieux réalisé."),
        ],
        "questions": ["Êtes-vous propriétaire de la maison et l'occupez-vous ?", "Quels travaux envisagez-vous : murs, combles, rampants, planchers ?", "De quelle année date la maison, à peu près ?", "Quelle est sa surface ?", "Dans quelle commune se trouve-t-elle ?", "Quand souhaitez-vous faire les travaux ?"],
        "angles": [
            ("Une maison froide l'hiver", "Murs froids, combles mal isolés ? Faites étudier l'isolation de votre maison par une entreprise de votre secteur."),
            ("Isoler et rénover", "Isolation par l'extérieur et ravalement en un seul chantier. Étude et chiffrage à domicile."),
        ],
        "faq": [
            ("Est-ce compatible avec l'interdiction du démarchage ?", "Oui. Nous ne démarchons personne. Nous rappelons uniquement des propriétaires qui ont rempli une demande et accepté d'être recontactés par votre entreprise. La preuve de leur accord est conservée."),
            ("Faut-il être certifié RGE ?", "Ce n'est pas obligatoire pour travailler avec nous. Si vous l'êtes, nous pouvons le mettre en avant dans vos annonces. Nous ne promettons jamais d'aide au propriétaire."),
        ],
    },
]


def esc(t):
    return html.escape(fr(t), quote=False)


def nw(t):
    """Empêche la coupure de « rendez-vous » en fin de ligne."""
    return t.replace("rendez-vous", '<span class="nw">rendez-vous</span>')


def li(items, cls=""):
    return "\n".join(f'          <li{cls}>{esc(x)}</li>' for x in items)


PROJECT = {
    "couverture": "une réfection ou une rénovation de toiture",
    "menuiserie-exterieure": "le remplacement de leurs fenêtres ou de leur porte",
    "facade": "un ravalement ou une isolation par l'extérieur",
    "charpente": "un projet de charpente prêt à démarrer",
    "isolation": "l'isolation complète de leur maison",
}


def trade_page(t):
    short = f"Nous trouvons les propriétaires qui préparent {PROJECT[t['slug']]}, nous les rappelons en moins de 5 minutes. Vous faites la visite."
    others = [o for o in TRADES if o["slug"] != t["slug"]]
    form = FORM.replace(f'value="{t["radio"]}"', f'value="{t["radio"]}" checked', 1)
    form = form.replace("<!-- Formulaire -->", "")
    problems = "\n".join(
        f"""      <li><span class="pb-n">{i}</span><h3>{esc(h)}</h3><p>{esc(p)}</p></li>""" for i, (h, p) in enumerate(t["problems"], 1))
    questions = "\n".join(f'      <li>{esc(q)}</li>' for q in t["questions"])
    angles = "\n".join(
        f"""      <article class="ad">
        <p class="ad-meta"><span class="ad-dot" aria-hidden="true"></span><span><b>Votre entreprise</b> · Sponsorisé</span></p>
        <p class="ad-angle">{esc(a)}</p>
        <p class="ad-text">{esc(b)}</p>
        <div class="ad-img">Vos vraies photos de chantier</div>
        <p class="ad-cta"><span>Demander une visite</span><b>En savoir plus</b></p>
      </article>""" for a, b in t["angles"])
    faq = "\n".join(
        f"""      <details><summary>{esc(q)}</summary><p>{esc(a)}</p></details>""" for q, a in t["faq"] + [
            ("Combien cela coûte-t-il ?", "Cela dépend de votre secteur et du nombre de rendez-vous que vous pouvez absorber. Nous vous donnons un prix précis pendant l'appel de 15 minutes, avant toute décision."),
            ("Y a-t-il un engagement ?", "Non. Aucune durée minimale."),
        ])
    other_links = "\n".join(f'      <li><a href="/metiers/{o["slug"]}/">{esc(o["name"])} <span aria-hidden="true">→</span></a></li>' for o in others)

    return f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(t["title"])} — Bartier &amp; Co</title>
<meta name="description" content="{html.escape(fr(short))}">
<meta name="robots" content="noindex">
<meta name="theme-color" content="#FFFFFF">
<link rel="canonical" href="https://bartierandco.com/metiers/{t["slug"]}/">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="preload" href="/fonts/general-sans-500.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/fonts/manrope-400.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/styles.css">
{HEAD_SCRIPT}
</head>
<body class="page-trade">
{HEADER}

<main id="contenu">

<section class="hero hero-trade" aria-labelledby="h1">
  <div class="wrap trade-hero">
    <div>
      <nav class="crumbs" aria-label="Fil d’Ariane"><a href="/">Accueil</a><span aria-hidden="true">/</span><a href="/metiers/">Métiers</a><span aria-hidden="true">/</span><span aria-current="page">{esc(t["name"])}</span></nav>
      <p class="kicker">{esc(t["who"])} · Partout en France</p>
      <h1 id="h1">{nw(esc(t["h1"]))} {nw(esc(t["h1_em"]))}</h1>
      <p class="lead">{esc(short)}</p>
      <div class="ctas">
        <a class="btn btn-primary" href="#secteur">Vérifier si mon secteur est libre <span class="go" aria-hidden="true">→</span></a>
        <a class="btn btn-ghost" href="#questions-tel">Ce que nous vérifions</a>
      </div>
      <p class="hero-note">Un artisan par secteur. Sans engagement.</p>
    </div>
    <aside class="sort" aria-label="Les chantiers que nous allons chercher">
      <p class="sort-head"><span>Le tri</span><span class="tag">{esc(t["name"])}</span></p>
      <p class="sort-label">Nous allons chercher</p>
      <ul class="sort-keep">
{li(t["keep"])}
      </ul>
      <p class="sort-label">Nous écartons</p>
      <ul class="sort-drop">
{li(t["drop"])}
      </ul>
    </aside>
  </div>
</section>

<section class="section section-soft" aria-labelledby="pb-h">
  <div class="wrap">
    <div class="head-c">
      <p class="kicker">Le constat</p>
      <h2 id="pb-h">Le métier est bon. Les demandes, beaucoup moins.</h2>
    </div>
    <ul class="pb">
{problems}
    </ul>
  </div>
</section>

<section class="section section-dark" id="questions-tel" aria-labelledby="tel-h">
  <div class="wrap calls-grid">
    <div>
      <p class="kicker hl-light">Au téléphone</p>
      <h2 id="tel-h">Ce que nous vérifions avant votre visite.</h2>
      <p class="sub">Rappel en moins de 5 minutes, en semaine de 8{NB}h à 19{NB}h. Pas de bonnes réponses, pas de rendez-vous.</p>
    </div>
    <ol class="calls">
{questions}
    </ol>
  </div>
</section>

<section class="section" aria-labelledby="ads-h">
  <div class="wrap">
    <div class="head-c">
      <p class="kicker">Les annonces</p>
      <h2 id="ads-h">À votre nom, autour de chez vous.</h2>
      <p class="sub">Facebook et Instagram, à 25 à 40{NB}km de votre dépôt, avec vos photos de chantier. Budget réglé par vous à Meta.</p>
    </div>
    <div class="ads">
{angles}
    </div>
    <p class="note">Exemples d’angles, écrits ensuite avec vous.</p>
  </div>
</section>

<section class="section section-soft" aria-labelledby="en-h">
  <div class="wrap">
    <div class="head-c">
      <p class="kicker">Engagements</p>
      <h2 id="en-h">Écrits dans le contrat.</h2>
    </div>
    {ENGAGEMENTS}
    {GUARANTEE}
  </div>
</section>

<section class="section" aria-labelledby="fq-h">
  <div class="wrap faq-grid">
    <div class="head"><h2 id="fq-h">Questions fréquentes</h2></div>
    <div class="faq">
{faq}
    </div>
  </div>
</section>
{form}

<section class="section section-grey" aria-labelledby="autres-h">
  <div class="wrap">
    <div class="head-c"><h2 id="autres-h">Les autres métiers</h2></div>
    <ul class="other-trades">
{other_links}
    </ul>
  </div>
</section>

</main>

{FOOTER}

{MOBILE_CTA}

<script src="/script.js" defer></script>
</body>
</html>
"""


def hub_page():
    cards = "\n".join(
        f"""      <li>
        <a class="trade-card" href="/metiers/{t["slug"]}/">
          <span class="trade-card-num">{i:02d}</span>
          <span class="trade-card-name">{esc(t["name"])}</span>
          <span class="trade-card-text">{esc(", ".join(t["keep"][:3]))}.</span>
          <span class="trade-card-go">Voir la page <span aria-hidden="true">→</span></span>
        </a>
      </li>""" for i, t in enumerate(TRADES, 1))
    return f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Métiers — Bartier &amp; Co</title>
<meta name="description" content="Rendez-vous de devis exclusifs pour les artisans du bâtiment à gros chantiers : couverture, menuiserie extérieure, façade, charpente, isolation.">
<meta name="robots" content="noindex">
<meta name="theme-color" content="#FFFFFF">
<link rel="canonical" href="https://bartierandco.com/metiers/">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="preload" href="/fonts/general-sans-500.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/styles.css">
{HEAD_SCRIPT}
</head>
<body>
{HEADER}
<main id="contenu">
<section class="hero" aria-labelledby="h1">
  <div class="wrap hero-inner">
    <nav class="crumbs" aria-label="Fil d’Ariane"><a href="/">Accueil</a><span aria-hidden="true">/</span><span aria-current="page">Métiers</span></nav>
    <p class="kicker">Métiers</p>
    <h1 id="h1">Uniquement les métiers où un chantier compte.</h1>
    <p class="lead">{esc("Des chantiers de plusieurs milliers d'euros. Pas de dépannage, pas de petits travaux.")}</p>
  </div>
</section>
<section class="section section-soft">
  <div class="wrap">
    <ol class="trade-cards">
{cards}
      <li>
        <a class="trade-card trade-card-other" href="/#secteur">
          <span class="trade-card-num">06</span>
          <span class="trade-card-name">Un autre métier du bâtiment ?</span>
          <span class="trade-card-text">{esc("Si vos chantiers dépassent plusieurs milliers d'euros, parlons-en.")}</span>
          <span class="trade-card-go">Vérifier mon secteur <span aria-hidden="true">→</span></span>
        </a>
      </li>
    </ol>
  </div>
</section>
</main>
{FOOTER}
{MOBILE_CTA}
<script src="/script.js" defer></script>
</body>
</html>
"""


for t in TRADES:
    out = ROOT / "metiers" / t["slug"] / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(trade_page(t), encoding="utf-8")
(ROOT / "metiers" / "index.html").write_text(hub_page(), encoding="utf-8")
print("pages générées :", len(TRADES) + 1)

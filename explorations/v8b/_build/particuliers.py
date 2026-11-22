# Page « particuliers » : capter la demande des propriétaires (toiture, façade, fenêtres, charpente, isolation)
# puis les mettre en relation avec un seul artisan de leur secteur.
# Contenu construit sur les recherches Google Trends (France, 5 ans) : « devis toiture », « prix toiture »,
# « réparation fuite toiture », « ravalement de façade » (personne ne cherche « façadier »), « prix fenêtre pvc »,
# « isolation des combles », « [métier] autour de moi », aides à l'isolation.
# SEO : mots-clés dans le titre, le H1, les H2 et H3. GEO : encadré « En bref » factuel, réponses courtes et directes,
# listes numérotées, date de mise à jour visible, sources officielles en lien, données structurées alignées sur le texte.

PATH = "/devis-travaux/"
CONSENT = "J’accepte d’être rappelé par Bartier &amp; Co au sujet de ce projet et mis en relation avec un artisan partenaire."
PRIVACY = "Votre numéro n’est transmis qu’à un seul artisan partenaire, à personne d’autre."
UPDATED = "2026-11-18"
UPDATED_TXT = "18 novembre 2026"
TITLE = "Devis travaux gratuit : toiture, façade, fenêtres, isolation"
DESC = ("Devis travaux gratuit : décrivez votre projet en 1 minute, rappel en moins de 5 min, un seul artisan local vient chiffrer. "
        "Toiture, façade, fenêtres, isolation.")

TRADES = [
    # clé, libellé, artisan (titre dynamique), photo, besoins (étape 2), titre SEO, texte, alt, titre prix, ce qui fait le prix
    ("toiture", "Toiture", "couvreurs", "Un couvreur pose",
     ["Fuite ou dégât urgent", "Réfection complète", "Réparation, tuiles, zinguerie", "Démoussage, nettoyage"],
     "Toiture et couverture",
     "Réfection, fuite, tuiles cassées, zinguerie, démoussage.",
     "Couvreur en train de réparer une toiture en tuiles",
     "Prix d’une réfection de toiture",
     "Surface, matériau (tuiles, ardoise, bac acier), état de la charpente, accès au toit."),
    ("facade", "Façade", "façadiers", "Une façade en rénovation",
     ["Ravalement complet", "Fissures, réparation", "Nettoyage, peinture", "Isolation par l’extérieur"],
     "Ravalement de façade",
     "Ravalement, fissures, enduit, peinture, isolation par l’extérieur.",
     "Façade de maison en cours de ravalement",
     "Prix d’un ravalement de façade",
     "Surface, état du support, finition, échafaudage."),
    ("fenetres", "Fenêtres et portes", "menuisiers", "Un menuisier pose",
     ["Remplacer des fenêtres", "Porte d’entrée", "Baie vitrée", "Volets"],
     "Fenêtres et portes",
     "PVC, alu ou bois, double vitrage, porte d’entrée, baie vitrée, volets.",
     "Menuisier posant une fenêtre",
     "Prix de fenêtres posées",
     "Nombre et taille des ouvertures, matériau, vitrage, type de pose."),
    ("charpente", "Charpente", "charpentiers", "Une charpente en bois",
     ["Réparation, renfort", "Traitement du bois", "Extension, surélévation", "Charpente neuve"],
     "Charpente",
     "Réparation, traitement du bois, extension, surélévation.",
     "Charpente en bois en cours de pose",
     "Prix de travaux de charpente",
     "État du bois, portée, traitement, accès au chantier."),
    ("isolation", "Isolation", "artisans", "Isolation d",
     ["Combles", "Murs par l’extérieur", "Toiture", "Je ne sais pas encore"],
     "Isolation des combles et des murs",
     "Combles perdus ou aménagés, murs par l’extérieur, toiture.",
     "Artisan posant de la laine isolante entre les montants d’un mur",
     "Prix de l’isolation des combles",
     "Surface, technique (combles perdus, rampants, murs), isolant."),
]

BRIEF = [
    ("Le service", "Bartier &amp; Co vous met gratuitement en relation avec l’artisan partenaire de votre secteur, pour vos travaux de toiture, façade, fenêtres, charpente ou isolation."),
    ("Le prix pour vous", "Gratuit, visite et devis compris. Les artisans nous rémunèrent."),
    ("Le délai", "Rappel en moins de 5 minutes, en semaine de 8 h à 19 h. Sinon, dès la réouverture."),
    ("Le rendez-vous", "Fixé pendant notre appel, rappelé par SMS avant la visite."),
    ("Combien d’artisans", "Un seul. Vos coordonnées ne vont à personne d’autre."),
    ("La zone", "Selon votre commune. Hors zone, nous vous le disons à l’appel."),
    ("La société", "Bartier &amp; Co, SAS en cours d’immatriculation. <a href=\"/mentions-legales/\">Mentions légales</a>."),
]

LEAK = [
    ("Mettez-vous en sécurité", "Éloignez l’eau des prises. Au moindre doute, coupez le courant de la pièce."),
    ("Limitez les dégâts", "Seaux, bâches, mobilier à l’abri. Ne montez jamais sur le toit."),
    ("Prenez des photos", "Plafond, murs, objets abîmés. Votre assureur vous les demandera."),
    ("Prévenez votre assureur", "Votre contrat vous laisse au moins cinq jours ouvrés pour déclarer le sinistre (Code des assurances, art. L113-2). Faites-le sans attendre."),
    ("Faites intervenir un couvreur", "Il trouve l’origine de la fuite, protège si besoin et chiffre la réparation."),
]

SERIOUS = [
    ("Une entreprise immatriculée", 'Son SIREN se vérifie en quelques secondes sur <a class="link" href="https://annuaire-entreprises.data.gouv.fr/" target="_blank" rel="noopener">annuaire-entreprises.data.gouv.fr</a>.'),
    ("Une assurance décennale", "Obligatoire. Demandez l’attestation&nbsp;: l’assureur figure aussi sur le devis."),
    ("Un devis écrit et détaillé", "Matériaux, main-d’œuvre, délais, paiement. Avant tout début de travaux."),
    ("RGE si vous visez des aides", 'Obligatoire pour les aides à la rénovation énergétique. Annuaire officiel&nbsp;: <a class="link" href="https://france-renov.gouv.fr/" target="_blank" rel="noopener">france-renov.gouv.fr</a>.'),
    ("Aucune pression", 'Méfiez-vous du démarchage « après la tempête » et des prix valables « aujourd’hui seulement ». <a class="link" href="/blog/demarchage-arnaques-travaux/">Vos droits face au démarchage</a>.'),
]

import html as _html, re as _re
SERIOUS_LD = {"@type": "ItemList", "name": "Comment reconnaître un artisan sérieux ? 5 points à vérifier avant de signer",
              "itemListElement": [{"@type": "ListItem", "position": i, "name": a, "description": _html.unescape(_re.sub("<[^>]+>", "", b)).replace("\xa0", " ")}
                                  for i, (a, b) in enumerate(SERIOUS, 1)]}

FAQ = [
    ("Est-ce vraiment gratuit ?",
     "Oui. Notre service est gratuit pour vous : ce sont les artisans partenaires qui nous rémunèrent. Vous ne payez que les travaux, et seulement si vous acceptez le devis."),
    ("La visite et le devis de l’artisan sont-ils payants ?",
     "Non. L’artisan vient voir le chantier et vous remet son devis sans frais pour vous. Vous restez libre de ne pas donner suite."),
    ("Combien d’entreprises vont m’appeler ?",
     "Une seule entreprise de travaux : l’artisan retenu. Avant lui, nous vous appelons pour vérifier votre projet. Vos coordonnées ne sont envoyées qu’à cet artisan, jamais à plusieurs entreprises."),
    ("Comment l’artisan est-il choisi ?",
     "C’est l’entreprise partenaire qui couvre votre métier et votre commune : nous n’en avons qu’une par secteur, et votre demande ne va qu’à elle. Elle nous confie sa publicité locale et nous rémunère, c’est pourquoi le service est gratuit pour vous. Avant de signer, vérifiez son immatriculation et son attestation décennale."),
    ("Et si le devis ne me convient pas ?",
     "Vous ne signez rien. Vous restez libre de refuser le devis ou de le comparer, sans frais et sans avoir à vous justifier."),
    ("Pourquoi passer par vous plutôt que chercher seul ?",
     "Pour gagner du temps et éviter les relances. Un seul appel, l’artisan de votre secteur, et la date de visite fixée pendant l’appel. Vous ne racontez votre projet qu’une fois."),
    ("Comment trouver un bon couvreur près de chez moi ?",
     "Cherchez un artisan local, immatriculé, assuré en décennale, qui se déplace pour voir le toit avant de chiffrer. Décrivez vos travaux ici : nous vous présentons le couvreur partenaire de votre secteur."),
    ("Combien coûte une réfection de toiture ?",
     "Comptez de 60 à 500 €/m², pose comprise, selon QuelleEnergie. L’écart vient de ce qui est refait : couverture seule, avec isolation ou avec la charpente. Le matériau (tuiles, ardoise, bac acier) et l’accès au toit comptent aussi. Seule une visite permet un devis fiable."),
    ("Combien coûte un ravalement de façade ?",
     "Comptez de 50 à 100 €/m², selon La Maison Saint-Gobain (2026). Le prix dépend de la surface, de l’état du support, de la finition et de l’échafaudage. Des fissures ou un enduit abîmé le font monter : l’artisan les évalue lors de la visite."),
    ("Combien coûte le remplacement d’une fenêtre ?",
     "Comptez de 870 à 1 170 € TTC pour une fenêtre PVC double vitrage posée en remplacement, selon La Maison Saint-Gobain (2026). Le prix change avec la taille, le matériau (PVC, alu, bois), le vitrage et le type de pose. Le devis détaille chaque fenêtre."),
    ("J’ai une fuite de toiture, que faire tout de suite ?",
     "Éloignez l’eau des prises, protégez le mobilier, photographiez les dégâts et prévenez votre assureur sans attendre : votre contrat vous laisse au moins cinq jours ouvrés (Code des assurances, art. L113-2). Dans le formulaire, choisissez « Fuite ou dégât urgent » : ces demandes sont rappelées en priorité."),
    ("Puis-je obtenir des aides pour mes travaux ?",
     "Pour la rénovation énergétique, comme l’isolation, oui dans certains cas : MaPrimeRénov’, primes CEE des fournisseurs d’énergie, éco-prêt à taux zéro. Toutes demandent une entreprise certifiée RGE, et leurs conditions changent souvent : vérifiez votre cas sur france-renov.gouv.fr. Dans un logement de plus de deux ans, la TVA est aussi réduite : 10 % pour la rénovation, 5,5 % pour les travaux d’économie d’énergie (Code général des impôts, art. 279-0 bis et 278-0 bis A)."),
    ("Où intervenez-vous ?",
     "Là où un artisan partenaire couvre votre commune. Sinon, nous vous le disons dès l’appel et votre demande n’est transmise à personne."),
    ("Prenez-vous aussi les petites réparations ?",
     "Dites-le-nous à l’appel. Si l’artisan partenaire de votre secteur ne prend pas ce type de chantier, nous vous le disons tout de suite, et votre demande n’est transmise à personne."),
    ("Comment savoir si un artisan est sérieux ?",
     "Vérifiez son immatriculation sur annuaire-entreprises.data.gouv.fr, demandez son attestation d’assurance décennale et un devis écrit et détaillé. Pour obtenir des aides, il doit être certifié RGE. Méfiez-vous des démarcheurs qui vous pressent ou annoncent un prix valable « aujourd’hui seulement »."),
    ("Qu’est-ce que l’assurance décennale ?",
     "C’est l’assurance qui couvre, pendant 10 ans après la réception des travaux, les dommages qui menacent la solidité du bâtiment ou le rendent impropre à son usage. Elle est obligatoire pour les artisans du bâtiment (Code des assurances, art. L241-1), et le nom de l’assureur doit figurer sur le devis."),
    ("Faut-il une autorisation de la mairie pour ses travaux ?",
     "Souvent, oui, dès que l’aspect extérieur change : matériau ou couleur de la toiture, façade, fenêtres. Il faut alors une déclaration préalable. Des travaux à l’identique n’en demandent en général pas, sauf en secteur protégé ou si votre commune l’impose : le service urbanisme de la mairie vous le confirme."),
    ("Le devis est-il obligatoire ?",
     "Oui pour un dépannage, une réparation ou un entretien à domicile de plus de 150 € TTC, ou si vous le demandez : l’artisan doit remettre un devis détaillé avant d’intervenir (arrêté du 24 janvier 2017). Pour les autres travaux, demandez-en toujours un : une fois accepté, il engage l’artisan au prix indiqué."),
    ("Combien de devis faut-il demander ?",
     "Aucune règle ne l’impose. Pour de gros travaux, comparer deux ou trois devis est courant. Avec nous, un artisan local vient chiffrer chez vous, et vous restez libre de demander d’autres devis."),
    ("Quand l’artisan vient-il chez moi ?",
     "La date de visite est fixée pendant notre appel, selon vos disponibilités et celles de l’artisan. Les fuites et dégâts urgents passent en priorité."),
    ("Pouvez-vous me rappeler le soir ou le week-end ?",
     "Nous rappelons du lundi au vendredi, de 8 h à 19 h. Une demande envoyée en dehors de ces horaires est traitée dès la réouverture, en priorité si c’est une urgence."),
    ("Que faites-vous de mes données ?",
     "Elles servent uniquement à traiter votre demande et à la transmettre à l’artisan retenu, à personne d’autre. Vous pouvez demander leur suppression à contact@bartierandco.com."),
]


FAQ_TOP = ["Est-ce vraiment gratuit ?", "La visite et le devis de l’artisan sont-ils payants ?", "Combien d’entreprises vont m’appeler ?",
           "Comment l’artisan est-il choisi ?", "Et si le devis ne me convient pas ?", "Quand l’artisan vient-il chez moi ?",
           "Où intervenez-vous ?", "Que faites-vous de mes données ?"]


def tick():
    return '<svg class="tick" viewBox="0 0 10 10" aria-hidden="true"><path d="M1 1h8v8" fill="none" stroke="currentColor" stroke-width="1.4"/></svg>'


def check():
    return '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="m5 12.5 4.5 4.5L19 7.5" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></svg>'


def trust(cls=""):
    return f"""<ul class="pf-trust {cls}">
        <li>{check()}Visite et devis offerts</li><li>{check()}Sans engagement</li><li>{check()}Un seul artisan</li>
      </ul>"""


def people(cls=""):
    """Visages et noms des fondateurs, près du formulaire : on sait à qui on confie son numéro."""
    av = "".join(f'<img src="/assets/photos/{n}-360x450-nb.webp" alt="" width="360" height="450" loading="lazy" decoding="async">'
                 for n in ("charles-le-cottier", "martin-barthelemy"))
    return (f'<p class="pf-people {cls}"><span class="pf-av" aria-hidden="true">{av}</span>'
            f'<span><b>Charles et Martin</b>, fondateurs de Bartier &amp; Co.<br>Martin répond au '
            f'<a href="tel:@@PHONE@@">@@PHONE_TXT@@</a>, en semaine de 8&nbsp;h à 19&nbsp;h.</span></p>')


STEPS = [
    ("Maintenant", "Vous décrivez vos travaux", "Cinq questions, une minute, sans créer de compte."),
    ("Moins de 5 minutes après", "Nous vous rappelons", "En semaine, de 8 h à 19 h. Nous vérifions votre projet avec vous."),
    ("Pendant l’appel", "La visite est fixée", "Avec l’artisan partenaire de votre secteur, selon vos disponibilités."),
    ("Avant la visite", "Un SMS vous la rappelle", "Vous n’avez rien à noter ni à relancer."),
    ("Le jour de la visite", "L’artisan chiffre chez vous", "Il voit le chantier et vous remet son devis, sans frais. Vous restez libre de refuser."),
]

ENGAGE = [
    ("Gratuit du début à la fin", "Notre service, la visite et le devis ne vous coûtent rien. Vous ne payez que vos travaux, si vous acceptez le devis."),
    ("Un seul artisan a votre numéro", "Vos coordonnées vont à l’artisan retenu, à personne d’autre. Vous pouvez demander leur suppression à tout moment."),
    ("Vous restez libre", "Vous ne signez rien avec nous. Refusez le devis ou comparez-le, sans avoir à vous justifier."),
    ("Hors zone, nous vous le disons", "Si aucun artisan partenaire ne couvre votre commune, vous le savez dès l’appel, et votre demande n’est transmise à personne."),
]

TEAM_IMG = "/assets/photos/fondateurs-bartier-co"
GALLERY = [  # photos Pexels déjà au site (voir stock/SOURCES.md), présentées comme illustrations
    ("couvreur-repare-toiture-ardoise", "Couverture", "Couvreur réparant une toiture en ardoise"),
    ("artisan-enduit-mur-pierre", "Façade", "Artisan appliquant un enduit sur un mur en pierre"),
    ("menuisier-dans-son-atelier", "Menuiserie", "Menuisier dans son atelier"),
    ("charpentier-sur-charpente-bois", "Charpente", "Charpentier sur une charpente en bois"),
]
WHY = '<li class="pf-why-free"><a class="link" href="#qui">Pourquoi c’est gratuit&nbsp;?</a></li></ul>'


def build(img, phone, phone_txt, crumbs, parts=False):
    tiles = "".join(f'<button type="button" class="pf-tile" data-v="{t[0]}">{t[1]}</button>' for t in TRADES) + \
        '<button type="button" class="pf-tile" data-v="autre">Autre projet</button>'
    form = f"""<div class="pf-card" id="projet">
      <p class="pf-live" aria-live="polite"><i></i><span class="pf-live-t">Rappel en moins de 5 minutes, en semaine</span></p>
      <form class="pf-form" method="post" action="/api/lead/" novalidate aria-label="Demande de devis de travaux">
        <div class="pf-top"><p class="pf-count" id="pf-count">Étape <b class="pf-n">1</b> sur 5 · 1 minute</p><button type="button" class="pf-back" hidden>← Retour</button></div>
        <p class="pf-bar"><i></i></p>
        <fieldset class="pf-step is-on" data-step="1"><legend>Quels travaux&nbsp;?</legend><div class="pf-grid">{tiles}</div><input type="hidden" name="travaux"></fieldset>
        <fieldset class="pf-step" data-step="2"><legend>Précisez votre besoin</legend><div class="pf-list pf-need"></div><input type="hidden" name="besoin"></fieldset>
        <fieldset class="pf-step" data-step="3"><legend>Quand souhaitez-vous démarrer&nbsp;?</legend><div class="pf-list">
          <button type="button" class="pf-opt" data-v="Dès que possible">Dès que possible</button><button type="button" class="pf-opt" data-v="Dans 1 à 3 mois">Dans 1 à 3 mois</button><button type="button" class="pf-opt" data-v="Dans plus de 3 mois">Dans plus de 3 mois</button><button type="button" class="pf-opt" data-v="Je compare des prix">Je compare des prix</button>
        </div><input type="hidden" name="delai"></fieldset>
        <fieldset class="pf-step" data-step="4"><legend>Vous êtes&nbsp;:</legend><div class="pf-list">
          <button type="button" class="pf-opt" data-v="Propriétaire occupant">Propriétaire, j’y habite</button><button type="button" class="pf-opt" data-v="Propriétaire bailleur">Propriétaire, je loue le logement</button><button type="button" class="pf-opt" data-v="Locataire">Locataire</button>
        </div><input type="hidden" name="statut">
          <p class="pf-note pf-tenant" hidden>Les travaux sur le toit, la façade ou les fenêtres se décident avec le propriétaire. Transmettez-lui cette page&nbsp;: la demande lui prend une minute.</p></fieldset>
        <fieldset class="pf-step" data-step="5"><legend>Dernière étape&nbsp;: où vous joindre&nbsp;?</legend>
          <div class="pf-fields">
            <label class="pf-f" for="pf-cp"><span>Code postal du chantier</span><input id="pf-cp" name="code_postal" aria-invalid="false" inputmode="numeric" autocomplete="postal-code" maxlength="5" placeholder="Ex. 80000" required></label>
            <label class="pf-f" for="pf-prenom"><span>Prénom</span><input id="pf-prenom" name="prenom" aria-invalid="false" autocomplete="given-name" placeholder="Votre prénom" required></label>
            <label class="pf-f is-wide" for="pf-tel"><span>Téléphone</span><input id="pf-tel" name="telephone" aria-invalid="false" type="tel" inputmode="tel" autocomplete="tel" placeholder="06 12 34 56 78" required></label>
          </div>
          <label class="pf-consent" for="pf-ok"><input id="pf-ok" type="checkbox" name="consentement" required aria-invalid="false"><span>{CONSENT}</span></label>
          <input class="pf-hp" name="site_web" tabindex="-1" autocomplete="off" aria-hidden="true">
          <p class="pf-err" id="pf-err" aria-live="polite" hidden></p>
          <button type="submit" class="btn pf-submit"><span>Être rappelé gratuitement</span>{tick()}</button>
          <p class="pf-small">Gratuit, sans engagement. {PRIVACY}</p>
        </fieldset>
        <div class="pf-done" hidden>
          <div class="pf-manual">
            <p class="pf-done-k">Dernière étape</p>
            <p class="pf-done-h"><span class="pf-name2">Envoyez</span> votre demande.</p>
            <p class="pf-when">Votre message est déjà rédigé. Nous vous répondons en moins de 5 minutes, du lundi au vendredi de 8 h à 19 h.</p>
            <a class="pf-wa pf-send" href="https://wa.me/33781018936" target="_blank" rel="noopener" data-wa="particulier-envoi">Envoyer ma demande sur WhatsApp</a>
            <a class="pf-ortel" href="tel:{phone}">ou appeler le {phone_txt}</a>
          </div>
          <div class="pf-sent">
          <span class="pf-ok">{check()}</span>
          <p class="pf-done-h">C’est noté<span class="pf-name"></span>.</p>
          <p class="pf-when pf-when-sent"></p>
          <p class="pf-keep">Gardez votre téléphone à portée de main.</p>
          <ol class="pf-next"><li>Nous vérifions votre projet avec vous.</li><li>Pendant l’appel, nous fixons la date de visite avec l’artisan de votre secteur.</li><li>Vous recevez un rappel par SMS avant la visite.</li><li>L’artisan chiffre chez vous, sans frais.</li></ol>
          <a class="pf-wa" href="https://wa.me/33781018936" target="_blank" rel="noopener" data-wa="particulier">Envoyer aussi ma demande sur WhatsApp</a>
          </div>
        </div>
      </form>
    </div>"""

    hero = f"""<section class="sheet pf-hero" id="haut" data-tone="light">
  <div class="grid pf-hero-grid">
    <div class="pf-intro">
      {crumbs}
      <div class="pf-h1"><h1 class="pf-kw">Devis travaux : toiture, façade, fenêtres, charpente, isolation</h1> <p class="pf-big pf-big-hub">Fini les <span class="pf-who">artisans</span> qui ne rappellent&nbsp;pas.</p></div>
      <p class="lead">Décrivez vos travaux en 1 minute. Nous vous rappelons en moins de 5 minutes en semaine, et la visite d’un artisan de votre secteur est fixée pendant l’appel.</p>
      {trust("d-only").replace("</ul>", WHY)}
      {people("d-only").replace("@@PHONE@@", phone).replace("@@PHONE_TXT@@", phone_txt)}
    </div>
    {form}
    <div class="pf-mtrust m-only">{trust().replace("</ul>", WHY)}{people().replace("@@PHONE@@", phone).replace("@@PHONE_TXT@@", phone_txt)}</div>
  </div>
</section>"""

    brief = "".join(f"<div><dt>{a}</dt><dd>{b}</dd></div>" for a, b in BRIEF)
    brief = f"""<section class="sheet pf-brief" data-tone="paper" aria-labelledby="pf-brief-h">
  <div class="grid pf-brief-grid">
    <h2 id="pf-brief-h">Bartier &amp; Co en bref</h2>
    <dl class="pf-dl">{brief}</dl>
    <p class="pf-upd">Mis à jour le <time datetime="@@MAJ@@">@@MAJFR@@</time></p>
  </div>
</section>"""

    promise = f"""<section class="sheet pf-promise" id="promesse" data-tone="accent">
  <div class="grid sp-head"><h2 data-split>Fini les artisans qui ne rappellent pas.</h2><p>Vous laissez un message, vous relancez, vous attendez. Ici, la visite est fixée pendant notre appel.</p></div>
  <ul class="pf-proms">
    <li><b>5 <small>min</small></b> <span>pour vous rappeler, en semaine de 8 h à 19 h</span></li>
    <li><b>1 <small>appel</small></b> <span>pour fixer la date de visite</span></li>
    <li><b>1 <small>SMS</small></b> <span>de rappel avant la visite</span></li>
    <li><b>0 <small>€</small></b> <span>pour vous&nbsp;: visite et devis offerts, sans engagement</span></li>
  </ul>
  <p class="pf-mid"><a class="btn pf-btn-inv" href="#projet"><span>Obtenir mon devis gratuit</span>{tick()}</a><a class="link pf-end-call" href="tel:{phone}">ou appelez le {phone_txt}</a></p>
</section>"""

    gal = "".join(f'<li><figure class="frame"><img srcset="/assets/photos/{n}-480x600.webp 480w, /assets/photos/{n}-640x800.webp 640w, /assets/photos/{n}-800x1000.webp 800w" '
                  f'sizes="(max-width: 760px) 46vw, 23vw" src="/assets/photos/{n}-480x600.webp" alt="{alt}" width="800" height="1000" loading="lazy" decoding="async"></figure>'
                  f'<p>{lab}</p></li>' for n, lab, alt in GALLERY)
    gallery = f"""<section class="sheet pf-gal" id="sur-place" data-tone="light">
  <div class="grid sp-head"><h2 data-split>Un artisan qui vient voir le chantier</h2><p>L’artisan partenaire de votre secteur se déplace chez vous avant de chiffrer. Son devis part de ce qu’il a vu.</p></div>
  <ul class="pf-gal-row">{gal}</ul>
  <p class="pf-gal-cap">Photos d’illustration</p>
</section>"""

    steps = "".join(f'<li><span class="pf-t">{t}</span><h3>{h}</h3><p>{p}</p></li>' for t, h, p in STEPS)
    process = f"""<section class="sheet pf-steps" id="promesse" data-tone="accent">
  <div class="grid sp-head"><h2 data-split>Ce qui se passe après votre demande</h2><p>Vous ne relancez personne&nbsp;: la visite est fixée dès notre premier appel.</p></div>
  <ol class="pf-howto">{steps}</ol>
  <p class="pf-mid"><a class="btn pf-btn-inv" href="#projet"><span>Obtenir mon devis gratuit</span>{tick()}</a><a class="link pf-end-call" href="tel:{phone}">ou appelez le {phone_txt}</a></p>
</section>"""

    eng = "".join(f'<li><span class="pf-eng-i">{check()}</span><h3>{a}</h3><p>{b}</p></li>' for a, b in ENGAGE)
    engage = f"""<section class="sheet pf-eng" id="engagements" data-tone="light">
  <div class="grid sp-head"><h2 data-split>Nos engagements envers vous</h2><p>Ce que vous pouvez attendre de nous, quels que soient vos travaux.</p></div>
  <ul class="pf-checks pf-eng-list">{eng}</ul>
  <p class="pf-mid"><a class="btn" href="#projet"><span>Obtenir mon devis gratuit</span>{tick()}</a><a class="link" href="tel:{phone}">ou appelez le {phone_txt}</a></p>
</section>"""

    team = f"""<section class="sheet pf-team" id="qui" data-tone="paper">
  <div class="grid pf-team-grid">
    <figure class="frame pf-team-img"><img srcset="{TEAM_IMG}-480x360-nb.webp 480w, {TEAM_IMG}-800x600-nb.webp 800w, {TEAM_IMG}-1200x900-nb.webp 1200w" sizes="(max-width: 760px) 100vw, 50vw" src="{TEAM_IMG}-800x600-nb.webp" alt="Charles Le Cottier et Martin Barthélémy, fondateurs de Bartier &amp; Co" width="1200" height="900" loading="lazy" decoding="async"></figure>
    <div class="pf-team-txt">
      <h2 data-split>Qui est derrière Bartier &amp; Co&nbsp;?</h2>
      <p class="pf-team-lead">Une société française fondée par Charles Le Cottier et Martin Barthélémy. Notre métier&nbsp;: trouver des clients aux artisans du bâtiment, avec un seul artisan par métier et par secteur.</p>
      <dl class="pf-team-dl">
        <div><dt>Pourquoi c’est gratuit pour vous</dt><dd>L’artisan partenaire nous confie sa publicité locale et nous rémunère. Vous ne payez que vos travaux, et seulement si vous acceptez son devis.</dd></div>
        <div><dt>Pourquoi un seul artisan</dt><dd>Dans chaque secteur, nous travaillons avec une seule entreprise par métier. Votre demande va directement chez elle, et votre téléphone ne sonne pas cinq fois.</dd></div>
      </dl>
      <p class="pf-team-c"><a class="link" href="tel:{phone}">{phone_txt}</a><a class="link" href="https://wa.me/33781018936" target="_blank" rel="noopener" data-wa="particulier-equipe">WhatsApp</a><a class="link" href="mailto:contact@bartierandco.com">contact@bartierandco.com</a><a class="link" href="/qui-sommes-nous/">Qui sommes-nous</a></p>
    </div>
  </div>
</section>"""

    def band(text, btn, sub=""):
        sub = f'<span class="pf-band-sub">{sub}</span>' if sub else ""
        return f'<div class="pf-band"><p>{text}{sub}</p><a class="btn" href="#projet"><span>{btn}</span>{tick()}</a></div>'

    cards = []
    for k, l, who, photo, needs, h3, words, alt, ph, pr in TRADES:
        url, _ = img(photo)
        src_attr = f'srcset="{ISO_SRCSET}" src="{ISO_PHOTO}-1400x1050.webp"' if k == "isolation" else f'src="{url}"'
        cards.append(f"""    <li class="pf-trade"><figure class="frame"><img {src_attr} alt="{alt}" width="900" height="676" loading="lazy" sizes="(max-width: 760px) 46vw, 18vw"></figure>
      <h3><a class="pf-tl" href="/devis-travaux/{SLUG[k]}/">{h3}</a></h3><p>{words}</p><a class="link pf-pick" href="#projet" data-v="{k}">Devis {l.lower()}</a></li>""")
    trades = f"""<section class="sheet" id="travaux" data-tone="light">
  <div class="grid sp-head"><h2 data-split>Toiture, façade, fenêtres, charpente, isolation</h2><p>Pour chaque chantier, un artisan de votre secteur, qui se déplace avant de chiffrer.</p></div>
  <ul class="pf-trades">
{chr(10).join(cards)}
  </ul>
  {band("Vos travaux ne sont pas dans la liste&nbsp;?", "Obtenir mon devis gratuit", "Décrivez-les quand même. Nous vous disons si un artisan partenaire peut s’en charger.")}
</section>"""


    compare = f"""<section class="sheet" data-tone="tint">
  <div class="grid sp-head"><h2 data-split>Pas cinq entreprises. Un seul artisan.</h2><p>Ailleurs, votre demande part chez plusieurs entreprises et le téléphone ne s’arrête plus. Ici, nous vous rappelons, puis un seul artisan s’occupe de votre projet.</p></div>
  <div class="sp-table" role="table" aria-label="Site de devis classique et Bartier &amp; Co">
    <div class="sp-row is-head" role="row"><span role="columnheader"><span class="vh">Critère</span></span><span role="columnheader">Site de devis classique</span><span role="columnheader">Bartier &amp; Co</span></div>
    <div class="sp-row" role="row"><span role="rowheader">Qui vous appelle</span><span role="cell">Souvent plusieurs entreprises</span><span role="cell">Nous, puis un seul artisan</span></div>
    <div class="sp-row" role="row"><span role="rowheader">Avant la visite</span><span role="cell">Vous répétez votre projet</span><span role="cell">Votre besoin est déjà vérifié</span></div>
    <div class="sp-row" role="row"><span role="rowheader">Le rendez-vous</span><span role="cell">Vous relancez les artisans</span><span role="cell">Fixé pendant notre appel</span></div>
    <div class="sp-row" role="row"><span role="rowheader">Avant le jour J</span><span role="cell">Rien</span><span role="cell">Rappel par SMS</span></div>
    <div class="sp-row" role="row"><span role="rowheader">Vos coordonnées</span><span role="cell">Partagées entre entreprises</span><span role="cell">Transmises à un seul artisan</span></div>
    <div class="sp-row" role="row"><span role="rowheader">Le prix pour vous</span><span role="cell">Gratuit</span><span role="cell">Gratuit</span></div>
  </div>
  {band("Un seul artisan, de votre secteur.", "Obtenir mon devis gratuit")}
</section>"""

    leak = "".join(f"<li><h3>{a}</h3><p>{b}</p></li>" for a, b in LEAK)
    leak = f"""<section class="sheet pf-leak" id="fuite-toiture" data-tone="accent">
  <div class="grid sp-head"><h2 data-split>Fuite de toiture&nbsp;: que faire&nbsp;? Les 5 bons réflexes</h2><p>Suivez-les dans l’ordre, puis signalez-nous la fuite&nbsp;: nous vous rappelons en priorité.</p></div>
  <ol class="pf-howto">{leak}</ol>
  <p class="pf-mid"><a class="btn pf-pick" href="#projet" data-v="toiture" data-need="fuite"><span>Signaler une fuite</span>{tick()}</a><span class="pf-prio">Rappel prioritaire</span></p>
</section>"""

    # le chiffre d'abord (repris tel quel de la source citée), puis ce qui le fait varier
    FIG = {"toiture": ("60 à 500\u00a0€/m²", "Rénovation, pose comprise"), "facade": ("50 à 100\u00a0€/m²", "Ravalement, selon l’état de la façade"),
           "fenetres": ("870 à 1\u00a0170\u00a0€", "Fenêtre PVC double vitrage posée, TTC"), "charpente": ("150 à 200\u00a0€/m²", "Rénovation de la charpente seule, TTC"),
           "isolation": ("40 à 45\u00a0€/m²", "Combles perdus, pose comprise, TTC")}
    prices = "".join(f'<li><h3>{t[8]}</h3><p class="pf-fig"><b>{FIG[t[0]][0]}</b><span>{FIG[t[0]][1]}</span></p><p class="pf-why">Varie selon&nbsp;: {t[9][0].lower() + t[9][1:]}</p><p class="pf-src">Source&nbsp;: {REF[t[0]][1]}</p><a class="link pf-more" href="/devis-travaux/{SLUG[t[0]]}/">Prix et devis {SHORT[t[0]]}</a></li>' for t in TRADES)
    price = f"""<section class="sheet" id="prix" data-tone="light">
  <div class="grid sp-head"><h2 data-split>Combien vont coûter vos travaux&nbsp;?</h2><p>Les prix en ligne sont des moyennes : seul l’artisan peut chiffrer votre chantier, après une visite gratuite.</p></div>
  <ul class="pf-prices">{prices}</ul>
  <p class="pf-mid"><a class="btn" href="#projet"><span>Obtenir mon devis gratuit</span>{tick()}</a><a class="link" href="tel:{phone}">ou appelez le {phone_txt}</a></p>
</section>"""

    serious = "".join(f"<li><h3>{a}</h3><p>{b}</p></li>" for a, b in SERIOUS)
    serious = f"""<section class="sheet" id="artisan-serieux" data-tone="light">
  <div class="grid pf-ser">
    <div class="pf-ser-head"><h2 data-split>Comment reconnaître un artisan sérieux&nbsp;?</h2><p>5 points à vérifier avant de signer. Avec nous ou sans nous.</p>
      <p class="pf-ser-cta"><span>Nos artisans partenaires sont locaux et se déplacent avant de chiffrer.</span><a class="btn" href="#projet"><span>Obtenir mon devis gratuit</span>{tick()}</a></p></div>
    <div class="pf-ser-card"><p class="pf-ser-k"><b>Avant de signer</b><span>5 points</span></p><ul class="pf-checks pf-checklist">{serious}</ul></div>
  </div>
</section>"""

    row = lambda q, a: f'      <details class="fq"><summary><span>{q}</span><i class="fq-icon" aria-hidden="true"></i></summary><div class="fq-a"><p>{a}</p></div></details>'
    top = [x for x in FAQ if x[0] in FAQ_TOP]
    top.sort(key=lambda x: FAQ_TOP.index(x[0]))
    more = [x for x in FAQ if x[0] not in FAQ_TOP]
    rows = "\n".join(row(q, a) for q, a in top) + (f'\n      <details class="fq-more"><summary>Voir les {len(more)} autres questions</summary>\n'
                                                      + "\n".join(row(q, a) for q, a in more) + "\n      </details>")
    faq = f"""<section class="faq sheet" id="questions" data-kind="faq" data-tone="light">
  <div class="grid fq-grid">
    <div class="fq-head"><h2 data-split>Vos questions sur les devis de travaux</h2><p>Une autre question&nbsp;? <a class="link" href="tel:{phone}">{phone_txt}</a></p></div>
    <div class="fq-list">
{rows}
    </div>
  </div>
</section>"""

    end = f"""<section class="sheet pf-end" data-tone="accent">
  <div class="grid pf-end-grid">
    <h2 data-split>Décrivez vos travaux. Nous fixons la visite.</h2>
    <div><p class="pf-season"></p><a class="btn pf-btn-inv" href="#projet"><span>Obtenir mon devis gratuit</span>{tick()}</a><a class="link pf-end-call" href="tel:{phone}">ou appelez le {phone_txt}</a>{people("pf-people-inv").replace("@@PHONE@@", phone).replace("@@PHONE_TXT@@", phone_txt)}</div>
  </div>
</section>
<a class="pf-sticky" href="#projet">Obtenir mon devis gratuit <span>1 min</span></a>"""

    leak_short = f"""<section class="sheet pf-leak is-short" id="fuite-toiture" data-tone="accent">
  <div class="grid sp-head"><h2 data-split>Une fuite de toiture&nbsp;?</h2><p>Signalez-la&nbsp;: nous vous rappelons en priorité. En attendant, suivez <a class="link" href="/devis-travaux/toiture/#fuite-toiture">les 5 bons réflexes</a>.</p></div>
  <p class="pf-mid"><a class="btn pf-pick" href="#projet" data-v="toiture" data-need="fuite"><span>Signaler une fuite</span>{tick()}</a><span class="pf-prio">Rappel prioritaire</span></p>
</section>"""
    if parts:
        return dict(form=form, promise=promise, compare=compare, leak=leak, serious=serious, end=end)
    return "\n\n".join([hero, gallery, process, trades, engage, leak_short, price, team, serious, faq, brief, end])  # tableau « Pas cinq entreprises » retiré


# Questions aussi posées sur une page métier : balisées là-bas seulement (Google : une FAQ répétée se balise une fois)
HUB_UNMARKED = {"Combien coûte une réfection de toiture ?", "Combien coûte un ravalement de façade ?",
                "Combien coûte le remplacement d’une fenêtre ?", "J’ai une fuite de toiture, que faire tout de suite ?"}


def link_graph(SITE, path, g):
    """Chaque nœud reçoit son identifiant ; la page pointe vers son service, son fil d'Ariane et sa FAQ."""
    url = SITE + path
    g = dict(g, **{"@graph": [dict(n) for n in g["@graph"]]})  # copie : SERIOUS_LD est partagé entre les pages
    ids = {"Service": "#service", "FAQPage": "#questions", "HowTo": "#fuite-toiture", "BreadcrumbList": "#breadcrumb", "ItemList": "#artisan-serieux"}
    for n in g["@graph"]:
        if n.get("@type") in ids and "@id" not in n:
            n["@id"] = url + ids[n["@type"]]
    page = g["@graph"][0]
    page["mainEntity"] = {"@id": url + "#service"}
    page["breadcrumb"] = {"@id": url + "#breadcrumb"}
    page["hasPart"] = [{"@id": n["@id"]} for n in g["@graph"][1:] if n.get("@type") in ("FAQPage", "HowTo", "ItemList")]
    page["speakable"] = {"@type": "SpeakableSpecification", "cssSelector": ["h1", ".pf-brief"]}
    for n in g["@graph"]:
        if n.get("@type") == "Service":
            n["termsOfService"] = SITE + "/conditions-du-service/"
            n["availableChannel"] = {"@type": "ServiceChannel", "serviceUrl": url + "#haut",
                                     "servicePhone": {"@type": "ContactPoint", "telephone": "+33781018936", "contactType": "customer service", "availableLanguage": "French"}}
            break
    return g


def schema(SITE, faq_ld, bc_ld):
    import re
    clean = lambda t: re.sub("<[^>]+>", "", t).replace("&amp;", "&").replace("&nbsp;", " ")
    g = {"@context": "https://schema.org", "@graph": [
        {"@type": "WebPage", "@id": SITE + PATH, "url": SITE + PATH, "name": TITLE, "description": DESC, "inLanguage": "fr-FR",
         "dateModified": "@@MAJ@@", "isPartOf": {"@id": SITE + "/#website"}, "publisher": {"@id": SITE + "/#org"},
         "about": [{"@type": "Thing", "name": n} for n in ["Devis toiture", "Ravalement de façade", "Fenêtres", "Charpente", "Isolation des combles"]]},
        {"@type": "Service", "name": "Mise en relation avec un artisan du bâtiment", "serviceType": "Devis de travaux : toiture, façade, fenêtres, charpente, isolation",
         "description": clean(BRIEF[0][1]), "areaServed": {"@type": "Country", "name": "France"},
         "audience": {"@type": "Audience", "audienceType": "Propriétaires de maison"}, "url": SITE + PATH,
         "provider": {"@type": "Organization", "@id": SITE + "/#org", "name": "Bartier & Co", "url": SITE + "/"},
         "hoursAvailable": {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], "opens": "08:00", "closes": "19:00"},
         "offers": {"@type": "Offer", "price": "0", "priceCurrency": "EUR", "description": "Gratuit pour le particulier, sans engagement"},
         "hasOfferCatalog": {"@type": "OfferCatalog", "name": "Travaux", "itemListElement": [{"@type": "Offer", "itemOffered": {"@type": "Service", "@id": f"{SITE}{PATH}{SLUG[t[0]]}/#service", "url": f"{SITE}{PATH}{SLUG[t[0]]}/", "name": t[5], "description": clean(t[6])}} for t in TRADES]}},
        SERIOUS_LD, faq_ld([qa for qa in FAQ if qa[0] not in HUB_UNMARKED]), bc_ld(("Devis travaux", PATH))]}
    return link_graph(SITE, PATH, g)


CSS = """<style id="pf-css">
.m-only{display:none}
.pf-hero{padding-top:calc(var(--hdr) + clamp(28px,4vw,64px))}
.pf-hero-grid{row-gap:28px;align-items:start}
.pf-intro{grid-column:1 / 3;display:flex;flex-direction:column;gap:1.3rem}
.pf-h1{display:flex;flex-direction:column;gap:.9rem;font-weight:300}
.pf-kw{font:500 clamp(.92rem,1.1vw,1.02rem)/1.35 var(--f-text);letter-spacing:0;color:var(--accent);max-width:40ch}
.pf-big{font:300 clamp(3rem,6.4vw,6.4rem)/.95 var(--f-display);letter-spacing:-.05em}
.pf-who{color:var(--accent)}
.pf-intro .lead{font:400 clamp(1.15rem,1.6vw,1.45rem)/1.35 var(--f-display);letter-spacing:-.01em}
.pf-trust{display:flex;flex-wrap:wrap;gap:.6rem 1.6rem;margin:0;padding:0;list-style:none;font-size:.95rem}
.pf-trust li{display:flex;align-items:center;gap:.5rem}
.pf-trust svg{width:18px;height:18px;flex:none;color:var(--accent)}
.pf-call{display:flex;flex-wrap:wrap;align-items:baseline;gap:.3rem .6rem;font-size:.95rem}
.pf-call span{flex-basis:100%;color:var(--muted);font-size:.82rem}
.pf-card{grid-column:3 / 5;scroll-margin-top:calc(var(--hdr) + 16px);padding:clamp(20px,2.4vw,32px);background:var(--bg);border:1px solid var(--rule);border-radius:var(--r);box-shadow:0 30px 70px -40px rgba(10,20,36,.45)}
.pf-top{display:flex;justify-content:space-between;align-items:center;font-size:.85rem;color:var(--muted)}
.pf-back{display:inline-flex;align-items:center;min-height:44px;margin:-8px 0;border:0;background:none;color:var(--ink);font:inherit;cursor:pointer;padding:0 0 0 12px}
.pf-back[hidden]{display:none}
.pf-bar{height:4px;margin:12px 0 22px;background:var(--paper);border-radius:2px;overflow:hidden}
.pf-bar i{display:block;height:100%;width:20%;background:var(--accent);transition:width .45s var(--ease)}
.pf-step{display:none;margin:0;padding:0;border:0;min-width:0}
.pf-step.is-on{display:block;animation:pfIn .35s var(--ease)}
@keyframes pfIn{from{opacity:0;transform:translateX(14px)}}
.pf-step legend{margin-bottom:16px;padding:0;font:400 clamp(1.4rem,2vw,1.8rem)/1.15 var(--f-display);letter-spacing:-.02em}
.pf-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:10px}
.pf-list{display:grid;gap:10px}
.pf-tile,.pf-opt{display:flex;align-items:center;min-height:56px;padding:0 16px;border:1px solid var(--rule);border-radius:var(--r);background:var(--bg);color:var(--ink);font:500 1rem/1.25 var(--f-text);text-align:left;cursor:pointer;transition:border-color .2s,background-color .2s}
.pf-tile:hover,.pf-opt:hover{border-color:var(--accent)}
.pf-tile.is-sel,.pf-opt.is-sel{border-color:var(--accent);background:var(--tint)}
.pf-note{margin-top:14px;padding:12px 14px;background:var(--paper);font-size:.92rem;line-height:1.45}
.pf-fields{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-bottom:16px}
.pf-f{display:flex;flex-direction:column;gap:6px;font-size:.85rem;color:var(--muted)}
.pf-f.is-wide{grid-column:1 / -1}
.pf-f input{height:52px;padding:0 14px;border:1px solid var(--rule);border-radius:var(--r);background:var(--bg);color:var(--ink);font:400 1.05rem var(--f-text)}
.pf-f input:focus{outline:2px solid var(--accent);outline-offset:-1px;border-color:transparent}
.pf-f input[aria-invalid="true"]{border-color:#d93025}
.pf-consent{display:flex;gap:10px;align-items:flex-start;margin-bottom:16px;font-size:.85rem;line-height:1.45;color:var(--muted);cursor:pointer}
.pf-consent input{width:18px;height:18px;margin-top:2px;flex:none;accent-color:var(--accent)}
.pf-hp{position:absolute;left:-9999px;width:1px;height:1px;opacity:0}
.pf-err{margin-bottom:12px;color:#d93025;font-size:.9rem}
.pf-submit{width:100%;justify-content:center;min-height:56px;font-size:1.02rem}
.pf-small{margin-top:12px;font-size:.76rem;line-height:1.5;color:var(--muted)}
.pf-small a{white-space:nowrap}
.pf-ok{display:inline-grid;place-items:center;width:52px;height:52px;border-radius:50%;background:var(--accent);color:#fff}
.pf-ok svg{width:26px;height:26px}
.pf-done-h{margin-top:14px;font:400 1.8rem/1.1 var(--f-display);letter-spacing:-.02em}
.pf-done[data-state="sent"] .pf-manual,.pf-done[data-state="manual"] .pf-sent{display:none}
.pf-done-k{font-size:.85rem;color:var(--accent)}
.pf-manual .pf-done-h{margin-top:6px}
.pf-manual .pf-when{margin-bottom:16px}
.pf-send{width:100%;justify-content:center;min-height:56px;font-size:1.02rem}
.pf-ortel{display:inline-flex;align-items:center;min-height:44px;margin-top:4px;color:inherit;font-size:.95rem;text-underline-offset:.25em}
.pf-submit[disabled]{opacity:.7;cursor:progress}
.pf-when{margin-top:8px;font-size:1rem;line-height:1.45}
.pf-next{margin:18px 0;padding-left:1.2rem;display:grid;gap:6px;font-size:.95rem}
.pf-wa{display:inline-flex;align-items:center;min-height:48px;padding:0 16px;border-radius:var(--r);background:#25D366;color:#0A1424;font-weight:500;text-decoration:none}
.pf-brief{padding-block:clamp(48px,6vw,88px)}
.pf-brief-grid{row-gap:20px}
.pf-brief h2{grid-column:1 / 2;font:400 clamp(1.4rem,2vw,1.9rem)/1.1 var(--f-display);letter-spacing:-.02em}
.pf-dl{grid-column:2 / 5;display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:20px 28px;margin:0}
.pf-dl div{padding-top:12px;border-top:1px solid var(--rule)}
.pf-dl dt{margin-bottom:6px;font-size:.8rem;color:var(--muted)}
.pf-dl dd{margin:0;font-size:.95rem;line-height:1.45}
.pf-upd{grid-column:2 / 5;font-size:.8rem;color:var(--muted)}
.pf-trades{display:grid;grid-template-columns:repeat(5,minmax(0,1fr));gap:clamp(12px,1.4vw,20px);margin:0;padding:0 var(--cell);list-style:none}
.pf-trade{display:flex;flex-direction:column;gap:.6rem;min-width:0}
.pf-trade figure{aspect-ratio:4 / 3;margin:0 0 .4rem}
.pf-trade img{width:100%;height:100%;object-fit:cover}
.pf-trade h3{font:400 1.35rem/1.15 var(--f-display);letter-spacing:-.02em}
.pf-trade p{font-size:.92rem;line-height:1.45;color:var(--muted);flex:1}
.pf-pick.link{align-self:flex-start;font-size:.92rem;white-space:normal}
.pf-howto,.pf-checks,.pf-prices{display:grid;grid-template-columns:repeat(5,minmax(0,1fr));gap:20px;margin:0;padding:0 var(--cell);list-style:none;counter-reset:pf}
.pf-howto li,.pf-checks li,.pf-prices li{min-width:0;padding-top:14px;border-top:2px solid currentColor}
.pf-howto li{counter-increment:pf}
.pf-howto li::before{content:counter(pf,decimal-leading-zero);display:block;margin-bottom:10px;font:300 2rem/1 var(--f-display);color:var(--accent)}
.pf-big-hub{text-wrap:balance}
.pf-gal-row{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:20px;margin:0;padding:0 var(--cell);list-style:none}
.pf-gal-row figure{margin:0;overflow:hidden}
.pf-gal-row img{display:block;width:100%;height:auto;aspect-ratio:4/5;object-fit:cover}
.pf-gal-row p{margin-top:10px;font-size:.92rem;color:var(--muted)}
.pf-gal-cap{margin-top:16px;padding:0 var(--cell);font-size:.8rem;color:var(--muted)}
@media (max-width:760px){.pf-gal-row{grid-template-columns:repeat(2,minmax(0,1fr));gap:16px 12px}}
.pf-people a{color:var(--ink);text-decoration:underline;text-underline-offset:3px;white-space:nowrap}
.pf-people{display:flex;align-items:center;gap:14px;margin:0;font-size:.92rem;line-height:1.45;color:var(--muted)}
.pf-people b{font-weight:500;color:var(--ink)}
.pf-av{display:flex;flex:none}
.pf-av img{width:48px;height:48px;border-radius:50%;object-fit:cover;object-position:50% 20%;border:2px solid var(--bg);background:var(--paper)}
.pf-av img+img{margin-left:-12px}
.pf-mtrust .pf-people{margin-top:20px}
.pf-steps .pf-howto li::before{color:#9fb6ff}
.pf-steps .pf-howto p{color:rgba(255,255,255,.75)}
.pf-t{display:block;margin-bottom:6px;font-size:.8rem;line-height:1.3;color:rgba(255,255,255,.7)}
.pf-eng-list{grid-template-columns:repeat(4,minmax(0,1fr))}
.pf-eng-list li{display:flex;flex-direction:column;gap:10px;padding:22px;border:1px solid var(--rule);border-radius:var(--r);background:var(--bg)}
.pf-eng-list h3{margin:0;font:400 clamp(1.2rem,1.5vw,1.4rem)/1.15 var(--f-display);letter-spacing:-.015em}
.pf-eng-i{display:grid;place-items:center;width:36px;height:36px;border-radius:50%;background:var(--tint,#DCE4FB);color:var(--accent)}
.pf-eng-i svg{width:18px;height:18px}
@media (max-width:760px){.pf-checks.pf-eng-list{gap:12px}.pf-eng-list li{display:grid;grid-template-columns:36px minmax(0,1fr);column-gap:14px;row-gap:6px;padding:18px}.pf-eng-i{grid-row:1 / span 2}.pf-eng-list h3{align-self:center}.pf-eng-list p{grid-column:2}}
.pf-trust .pf-why-free{font-size:.92rem}
.fq-more>summary{display:block;padding:1.2rem var(--cell);color:var(--accent);font-weight:500;cursor:pointer;list-style:none;text-decoration:underline;text-underline-offset:4px}
.fq-more>summary::-webkit-details-marker{display:none}
.fq-more[open]>summary{display:none}
.pf-people-inv{margin-top:8px;color:rgba(255,255,255,.75)}.pf-people-inv b,.pf-people-inv a{color:#fff}.pf-people-inv .pf-av img{border-color:var(--accent)}
.pf-team-grid{row-gap:28px;align-items:center}
.pf-team-img{grid-column:1 / 3;margin:0}
.pf-team-img img{display:block;width:100%;height:auto}
.pf-team-txt{grid-column:3 / 5;display:flex;flex-direction:column;gap:1.2rem}
.pf-team-txt h2{font:300 clamp(2rem,3.4vw,3.2rem)/1.02 var(--f-display);letter-spacing:-.04em}
.pf-team-lead{font:400 clamp(1.1rem,1.4vw,1.3rem)/1.4 var(--f-display);letter-spacing:-.01em}
.pf-team-dl{display:grid;gap:16px;margin:0}
.pf-team-dl div{padding-top:12px;border-top:1px solid var(--rule)}
.pf-team-dl dt{margin-bottom:6px;font-weight:500}
.pf-team-dl dd{margin:0;font-size:.95rem;line-height:1.5;color:var(--ink)}
.pf-team-c{display:flex;flex-wrap:wrap;gap:.6rem 1.4rem;font-size:.95rem}
@media (max-width:1024px){.pf-eng-list{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media (max-width:760px){.pf-eng-list{grid-template-columns:1fr}.pf-team-img,.pf-team-txt{grid-column:1 / -1}.pf-steps .pf-howto{gap:0}.pf-steps .pf-howto li{display:grid;grid-template-columns:44px minmax(0,1fr);column-gap:12px;padding:16px 0;border-top-width:1px}.pf-steps .pf-howto li::before{grid-row:1 / span 3;margin:0;font-size:1.5rem}.pf-steps .pf-howto li>*{grid-column:2}.pf-steps .pf-howto h3{margin-bottom:4px}}
.pf-leak .pf-howto li::before{color:#9fb6ff}
.pf-howto h3,.pf-checks h3,.pf-prices h3{margin-bottom:8px;font:400 1.2rem/1.15 var(--f-display);letter-spacing:-.01em}
.pf-howto p,.pf-checks p,.pf-prices p{font-size:.92rem;line-height:1.5}
.pf-leak .pf-howto p{color:rgba(255,255,255,.75)}
.pf-mid{display:flex;flex-wrap:wrap;align-items:center;gap:.6rem 1.2rem;margin-top:clamp(28px,4vw,48px);padding:0 var(--cell)}
.pf-prio{font-size:.9rem;color:#9fb6ff}
.pf-end-grid{row-gap:24px;align-items:end}
.pf-end h2{grid-column:1 / 3;font:300 clamp(2.2rem,4.4vw,4rem)/1 var(--f-display);letter-spacing:-.04em}
.pf-end-grid > div{grid-column:3 / 5;display:flex;flex-direction:column;align-items:flex-start;gap:1.2rem}
.pf-btn-inv{background:#fff;color:var(--accent)}
.pf-live{display:flex;align-items:center;gap:8px;margin:-4px 0 14px;font-size:.85rem;color:var(--muted)}
.pf-live i{width:9px;height:9px;border-radius:50%;background:#b8bec6;flex:none}
.pf-live.is-on{color:#137333}.pf-live.is-on i{background:#1e8e3e;box-shadow:0 0 0 0 rgba(30,142,62,.5);animation:pfPulse 2s 4}
@keyframes pfPulse{70%{box-shadow:0 0 0 7px rgba(30,142,62,0)}100%{box-shadow:0 0 0 0 rgba(30,142,62,0)}}
.pf-keep{margin-top:6px;font-weight:500}
.pf-proms{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:20px;margin:0;padding:0 var(--cell);list-style:none}
.pf-proms li{display:flex;flex-direction:column;gap:8px;padding-top:16px;border-top:1px solid rgba(255,255,255,.25)}
.pf-proms b{font:300 clamp(2.6rem,4.6vw,4.2rem)/1 var(--f-display);letter-spacing:-.04em;color:#fff}
.pf-proms span{font-size:.95rem;line-height:1.45;color:rgba(255,255,255,.75)}
.pf-promise .pf-mid .link{color:#fff}
.pf-time{display:grid;grid-template-columns:repeat(5,minmax(0,1fr));gap:20px;margin:0;padding:0 var(--cell);list-style:none}
.pf-time li{position:relative;padding-top:22px;border-top:2px solid var(--accent)}
.pf-time li::before{content:"";position:absolute;top:-7px;left:0;width:12px;height:12px;border-radius:50%;background:var(--accent);box-shadow:0 0 0 4px var(--paper)}
.pf-t{display:block;margin-bottom:8px;font-size:.8rem;font-weight:600;color:var(--accent);text-transform:uppercase;letter-spacing:.04em}
.pf-time h3{margin-bottom:6px;font:400 1.2rem/1.15 var(--f-display)}
.pf-time p{font-size:.92rem;line-height:1.45;color:var(--muted)}
.pf-season{font-weight:500}
.pf-season:empty{display:none}
.pf-end-call{color:#fff}
.pf-band{display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;gap:16px 28px;margin:clamp(32px,4vw,56px) var(--cell) 0;padding:clamp(18px,2vw,26px) clamp(18px,2.4vw,32px);border:1px solid var(--accent);border-radius:var(--r);background:color-mix(in oklab,var(--accent) 5%,var(--bg))}
.pf-band p{display:flex;flex-direction:column;gap:4px;font:400 clamp(1.2rem,1.8vw,1.55rem)/1.2 var(--f-display);letter-spacing:-.015em;color:var(--ink)}
.pf-band-sub{font:400 .92rem/1.4 var(--f-text);letter-spacing:0;color:var(--muted)}
.pf-call.d-only{font-size:.95rem}
.pf-sticky{position:fixed;left:14px;right:78px;bottom:14px;z-index:89;display:none;flex-direction:column;justify-content:center;min-height:52px;padding:6px 18px;border-radius:var(--r);background:var(--accent);color:#fff;font-weight:500;text-decoration:none;box-shadow:0 14px 30px -12px rgba(45,91,227,.6);transform:translateY(140%);transition:transform .35s var(--ease)}
.pf-sticky span{font-size:.75rem;font-weight:400;opacity:.85}
.pf-sticky.is-on{transform:none}
@media (max-width:1024px){.pf-trades,.pf-prices,.pf-howto,.pf-checks,.pf-proms{grid-template-columns:repeat(2,minmax(0,1fr))}.pf-time{grid-template-columns:repeat(3,minmax(0,1fr))}.pf-dl{grid-column:1 / -1}.pf-brief h2{grid-column:1 / -1}}
@media (max-width:760px){
  .m-only{display:block}.d-only{display:none}
  .pf-intro,.pf-card,.pf-mtrust,.pf-end h2,.pf-end-grid > div{grid-column:1 / -1}
  .pf-hero{padding-top:calc(var(--hdr) + 18px)}
  .pf-hero-grid{row-gap:18px}
  .pf-intro{gap:.8rem}
  .pf-h1{gap:.6rem}.pf-kw{font-size:.85rem}.pf-big{font-size:2.9rem}
  .pf-trust{gap:.5rem 1rem;font-size:.9rem}.pf-upd{grid-column:1 / -1}
  .pf-call{display:none}
  .pf-card{padding:18px 16px;margin-inline:calc(var(--cell) * -1)}
  .pf-grid{gap:8px}.pf-tile{min-height:54px;padding:0 12px;font-size:.95rem}
  .pf-fields{grid-template-columns:1fr}
  .pf-trades{grid-template-columns:repeat(2,minmax(0,1fr));gap:22px 12px}
  .pf-trade h3{font-size:1.1rem}.pf-trade p{display:none}
  .pf-prices,.pf-howto,.pf-checks{grid-template-columns:1fr}
  .pf-sticky{display:flex}
  .pf-band{flex-direction:column;align-items:stretch}.pf-band .btn{justify-content:center}
  .pf-proms{grid-template-columns:1fr 1fr;gap:22px 14px}.pf-proms b{font-size:2.6rem}
  .pf-time{grid-template-columns:1fr;gap:0;border-left:2px solid var(--accent);margin-left:calc(var(--cell) + 5px);padding-left:20px}
  .pf-time li{border-top:0;padding:0 0 22px}.pf-time li::before{left:-27px;top:3px}
}
</style>"""

JS = r"""<script>
(function(){
var NEEDS=__NEEDS__, WHO=__WHO__, LABEL=__LABEL__;
var f=document.querySelector(".pf-form");if(!f)return;
var steps=[].slice.call(f.querySelectorAll(".pf-step")),cur=0,n=f.querySelector(".pf-n"),bar=f.querySelector(".pf-bar i"),back=f.querySelector(".pf-back");
var dl=function(e,p){(window.dataLayer=window.dataLayer||[]).push(Object.assign({event:e},p||{}))};
function sel(x,on){x.classList.toggle("is-sel",on);x.setAttribute("aria-pressed",on?"true":"false")}
f.querySelectorAll(".pf-tile,.pf-opt").forEach(function(x){x.setAttribute("aria-pressed",x.classList.contains("is-sel")?"true":"false")});
function val(k){var e=f.querySelector("[name="+k+"]");return e?(e.value||"").trim():""}
function set(k,v){f.querySelector("[name="+k+"]").value=v}
function show(i,mv){steps.forEach(function(s,j){s.classList.toggle("is-on",j===i)});cur=i;n.textContent=i+1;bar.style.width=(100*(i+1)/steps.length)+"%";back.hidden=i===0;
  if(i===4){var c=f.querySelector("[name=code_postal]");if(c&&window.innerWidth>760){setTimeout(function(){c.focus()},200);return}}
  if(mv!==false){var lg=steps[i].querySelector("legend");if(lg){lg.setAttribute("tabindex","-1");lg.setAttribute("aria-describedby","pf-count");lg.focus({preventScroll:true})}}}
function fillNeeds(t){var box=f.querySelector(".pf-need"),list=NEEDS[t]||["Rénovation globale","Extension","Autre projet"];
  box.innerHTML=list.map(function(x){return "<button type=\"button\" class=\"pf-opt\" data-v=\""+x+"\" aria-pressed=\"false\">"+x+"</button>"}).join("")}
function pickTrade(t,jump){set("travaux",t);f.querySelectorAll(".pf-tile").forEach(function(b){sel(b,b.dataset.v===t)});fillNeeds(t);
  var w=document.querySelector(".pf-who");if(w)w.textContent=WHO[t]||"artisans";if(jump)show(1)}
function pickLeak(mv){var o=f.querySelector(".pf-need .pf-opt");if(o){sel(o,true);set("besoin",o.dataset.v);show(2,mv)}}
function pickNeed(v){var o=[].filter.call(f.querySelectorAll(".pf-need .pf-opt"),function(x){return x.dataset.v===v})[0];if(o){sel(o,true);set("besoin",v);show(2,false)}}
f.addEventListener("click",function(e){var b=e.target.closest(".pf-tile,.pf-opt");if(!b||!f.contains(b))return;
  var st=b.closest(".pf-step"),inp=st.querySelector("input[type=hidden]");
  st.querySelectorAll(".pf-tile,.pf-opt").forEach(function(x){sel(x,x===b)});
  if(b.classList.contains("pf-tile")){pickTrade(b.dataset.v,false);if(cur===0)dl("particulier_debut",{travaux:b.dataset.v})}else inp.value=b.dataset.v;
  if(inp.name==="statut"){var ten=b.dataset.v==="Locataire";st.querySelector(".pf-tenant").hidden=!ten;if(ten)return}
  setTimeout(function(){show(cur+1)},230)});
back.addEventListener("click",function(){if(cur>0)show(cur-1)});
document.querySelectorAll(".pf-pick").forEach(function(a){a.addEventListener("click",function(){pickTrade(a.dataset.v,true);if(a.dataset.need==="fuite")pickLeak()})});
var q=new URLSearchParams(location.search),t=q.get("travaux")||f.dataset.preset;
if(t&&(NEEDS[t]||t==="autre")){pickTrade(t,false);show(1,false);var nd=q.get("besoin")||f.dataset.need;if(nd==="fuite")pickLeak(false);else if(nd)pickNeed(nd)}
(function(){var l=document.querySelector(".pf-live"),t=l&&l.querySelector(".pf-live-t"),w=nextOpen();
  if(l){if(!w){l.classList.add("is-on");t.textContent="Disponibles maintenant · rappel en moins de 5 min"}else t.textContent="Rappel "+w+" · demandes enregistrées 24\u00a0h/24"}
  var m=new Date().getMonth(),se=document.querySelector(".pf-season"),S=["Hiver : les fuites et dégâts de tempête sont rappelés en priorité.","Hiver : les fuites et dégâts de tempête sont rappelés en priorité.","Printemps : la saison des rénovations.","Printemps : la saison des rénovations.","Printemps : la saison des rénovations.","Été : prévoyez votre visite avant la rentrée.","Été : prévoyez votre visite avant la rentrée.","Été : prévoyez votre visite avant la rentrée.","Automne : faites le point sur vos travaux avant l’hiver.","Automne : faites le point sur vos travaux avant l’hiver.","Automne : faites le point sur vos travaux avant l’hiver.","Hiver : les fuites et dégâts de tempête sont rappelés en priorité."];
  if(se)se.textContent=S[m]})();
function nextOpen(){var d=new Date(),day=d.getDay(),h=d.getHours()+d.getMinutes()/60;
  if(day>=1&&day<=5&&h>=8&&h<19)return "";
  if(day>=1&&day<=4&&h>=19)return "demain dès 8 h";if(day>=1&&day<=5&&h<8)return "ce matin dès 8 h";return "lundi dès 8 h"}
function check(){var err=f.querySelector(".pf-err"),bad=[];
  var cp=f.querySelector("[name=code_postal]"),pr=f.querySelector("[name=prenom]"),tel=f.querySelector("[name=telephone]"),ok=f.querySelector("[name=consentement]");
  [cp,pr,tel,ok].forEach(function(x){x.setAttribute("aria-invalid","false");x.removeAttribute("aria-describedby")});
  if(!/^\d{5}$/.test(cp.value.trim()))bad.push([cp,"un code postal à 5 chiffres"]);
  if(pr.value.trim().length<2)bad.push([pr,"votre prénom"]);
  if(tel.value.replace(/\D/g,"").length<10)bad.push([tel,"un numéro de téléphone à 10 chiffres"]);
  if(!ok.checked)bad.push([ok,"votre accord pour être rappelé"]);
  bad.forEach(function(b){b[0].setAttribute("aria-invalid","true");b[0].setAttribute("aria-describedby","pf-err")});
  if(bad.length){var tx="Il manque "+bad.map(function(b){return b[1]}).join(", ")+".";if(err.textContent!==tx)err.textContent=tx;err.hidden=false}else err.hidden=true;
  return bad}
/* une fois l'erreur affichée, elle se met à jour pendant la saisie et disparaît quand tout est bon */
f.addEventListener("input",function(e){if(!f.querySelector(".pf-err").hidden&&e.target.closest(".pf-step"))check()});
f.addEventListener("change",function(e){if(!f.querySelector(".pf-err").hidden&&e.target.closest(".pf-step"))check()});
f.addEventListener("submit",function(e){e.preventDefault();var err=f.querySelector(".pf-err"),bad=check();
  if(bad.length){if(window.innerWidth<=760){err.scrollIntoView({block:"center"});bad[0][0].focus({preventScroll:true})}else bad[0][0].focus();return}
  err.hidden=true;if(val("site_web"))return;
  var tr=LABEL[val("travaux")]||"Autre projet",msg="Bonjour, je souhaite être rappelé pour des travaux : "+tr+" ("+val("besoin")+"), "+val("delai").toLowerCase()+". "+val("statut")+", code postal "+val("code_postal")+". "+val("prenom")+", "+(function(t){var d=t.replace(/\D/g,"");return /^0\d{9}$/.test(d)?d.replace(/(\d{2})(?=\d)/g,"$1 "):t})(val("telephone"))+".";
  var done=f.querySelector(".pf-done"),btn=f.querySelector(".pf-submit"),lab=btn.querySelector("span"),old=lab.textContent;
  f.querySelector(".pf-name").textContent=", "+val("prenom");f.querySelector(".pf-name2").textContent=val("prenom")+", envoyez";
  var w=nextOpen();var telf=val("telephone").replace(/\D/g,"").length===10?val("telephone").replace(/\D/g,"").replace(/(\d{2})(?=\d)/g,"$1\u00a0"):val("telephone");
  f.querySelector(".pf-when-sent").textContent=w?"Nous vous rappelons "+w+" au "+telf+".":"Nous vous rappelons dans les 5 minutes au "+telf+".";
  f.querySelectorAll(".pf-wa").forEach(function(a){a.href="https://wa.me/33781018936?text="+encodeURIComponent(msg)});
  var fin=false,end=function(sent){if(fin)return;fin=true;btn.disabled=false;lab.textContent=old;
    dl("particulier_demande",{travaux:val("travaux"),besoin:val("besoin"),delai:val("delai"),statut:val("statut"),envoi:sent?"auto":"manuel"});
    done.setAttribute("data-state",sent?"sent":"manual");steps.forEach(function(s){s.classList.remove("is-on")});f.querySelector(".pf-top").style.display="none";f.querySelector(".pf-bar").style.display="none";done.hidden=false;done.setAttribute("tabindex","-1");done.focus({preventScroll:true});
    document.getElementById("projet").scrollIntoView({behavior:"smooth",block:"start"})};
  var body={type:"particulier",fields:{travaux:val("travaux"),besoin:val("besoin"),delai:val("delai"),statut:val("statut"),code_postal:val("code_postal"),prenom:val("prenom"),telephone:val("telephone")},consent:{text:f.querySelector(".pf-consent span").textContent,at:new Date().toISOString()},page:location.pathname,site_web:""};try{var uq=new URLSearchParams(location.search);["utm_source","utm_medium","utm_campaign","utm_content"].forEach(function(k){var v=uq.get(k);if(v)body[k]=v.slice(0,200)})}catch(x){}
  btn.disabled=true;lab.textContent="Envoi…";var t=setTimeout(function(){end(false)},10000);
  try{fetch("/api/lead/",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify(body)}).then(function(r){return r.ok?r.json():null}).then(function(j){clearTimeout(t);end(!!(j&&j.ok))}).catch(function(){clearTimeout(t);end(false)})}catch(x){clearTimeout(t);end(false)}});
var sticky=document.querySelector(".pf-sticky"),card=document.getElementById("projet"),endS=document.querySelector(".pf-end");
if(sticky&&"IntersectionObserver" in window){var vis=new Set();var io=new IntersectionObserver(function(es){es.forEach(function(x){x.isIntersecting?vis.add(x.target):vis.delete(x.target)});sticky.classList.toggle("is-on",vis.size===0&&scrollY>200)},{threshold:0});[card,endS,document.querySelector(".ftr")].forEach(function(x){x&&io.observe(x)});
  addEventListener("scroll",function(){if(scrollY<=200)sticky.classList.remove("is-on");else if(vis.size===0)sticky.classList.add("is-on")},{passive:true})}
})();
</script>"""


def js():
    import json
    needs = {t[0]: t[4] for t in TRADES}
    who = {t[0]: t[2] for t in TRADES}
    who["autre"] = "artisans"
    label = {t[0]: t[1] for t in TRADES}
    return JS.replace("__NEEDS__", json.dumps(needs, ensure_ascii=False)).replace("__WHO__", json.dumps(who, ensure_ascii=False)).replace("__LABEL__", json.dumps(label, ensure_ascii=False))


# ——— Repères de prix publiés (vérifiés sur les pages sources le 18/11/2026) ———
def _src(name, url, date):
    return f'<a class="link" href="{url}" target="_blank" rel="noopener">{name}</a>, {date}'


REF = {
    "toiture": ("Rénovation de toiture&nbsp;: de 60 à 500 €/m², pose comprise. L’écart dépend de ce qui est refait&nbsp;: couverture seule, isolation, charpente.",
                _src("QuelleEnergie", "https://www.quelleenergie.fr/prix-travaux/isolation/renovation-toiture", "consulté le 18/11/2026")),
    "facade": ("Ravalement de façade&nbsp;: de 50 à 100 €/m², selon l’état de la façade, les techniques et les matériaux.",
               _src("La Maison Saint-Gobain", "https://www.lamaisonsaintgobain.fr/facades/conseils/avant-de-vous-lancer-dans-les-travaux-de-facades/le-prix-d-un-ravalement-de-facade", "mis à jour le 25/08/2026")),
    "fenetres": ("Fenêtre PVC double vitrage, fournie et posée en remplacement&nbsp;: de 870 à 1&nbsp;170 € TTC, 1&nbsp;020 € en moyenne.",
                 _src("La Maison Saint-Gobain", "https://www.lamaisonsaintgobain.fr/guides-travaux/menuiseries-exterieures/prix-fenetre-pvc", "mis à jour le 13/02/2026")),
    "charpente": ("Rénovation de la charpente seule&nbsp;: de 150 à 200 €/m² TTC. Avec la couverture&nbsp;: de 180 à 250 €/m² TTC.",
                  _src("Hellowatt", "https://www.hellowatt.fr/prime-energie/renovation-energetique/prix-m2", "mis à jour le 22/12/2025")),
    "isolation": ("Isolation des combles perdus, pose comprise&nbsp;: 40 €/m² TTC si l’accès se fait par l’intérieur, 45 €/m² TTC par le toit.",
                  _src("La Maison Saint-Gobain", "https://www.lamaisonsaintgobain.fr/guides-travaux/isolation/prix-isolation-combles", "mis à jour le 06/07/2026")),
}

ISO_PHOTO = "/assets/photos/artisan-pose-laine-isolante-mur"  # Pexels 6124239, voir _build/stock/SOURCES.md
ISO_SRCSET = ", ".join(f"{ISO_PHOTO}-{w}x{w * 3 // 4}.webp {w}w" for w in (480, 800, 1200, 1400))
SHORT = {"toiture": "toiture", "facade": "façade", "fenetres": "fenêtres", "charpente": "charpente", "isolation": "isolation"}
SLUG = {"toiture": "toiture", "facade": "ravalement-facade", "fenetres": "fenetres", "charpente": "charpente", "isolation": "isolation"}

PAGES = {
    "toiture": dict(
        title="Devis toiture gratuit : un couvreur près de chez vous",
        desc="Un couvreur de votre secteur vient chiffrer : réfection, fuite, zinguerie, démoussage. Devis gratuit, rappel en moins de 5 minutes en semaine.",
        kw="Couvreur : devis toiture gratuit", h2="Vos travaux de toiture", price_h2="Prix d’une réfection de toiture",
        needs=[("Réfection complète", "Dépose de l’ancienne couverture, écran sous-toiture, tuiles ou ardoises neuves."),
               ("Fuite et réparation", "Tuiles cassées ou déplacées, faîtage, solins, recherche de l’origine d’une fuite. <a class=\"link\" href=\"/devis-travaux/toiture/urgence/\">Fuite en urgence</a>"),
               ("Zinguerie", "Gouttières, chéneaux, noues et descentes d’eau pluviale. <a class=\"link\" href=\"/devis-travaux/toiture/gouttieres/\">Devis gouttières</a>"),
               ("Démoussage et nettoyage", "Mousses et lichens retirés, état des tuiles vérifié au passage. <a class=\"link\" href=\"/devis-travaux/toiture/demoussage/\">Devis démoussage</a>")],
        faq=[("Que doit contenir un devis de toiture ?",
              "Le détail de chaque poste en quantité et en prix unitaire (dépose, écran sous-toiture, liteaux, tuiles ou ardoises, faîtage, zinguerie), la main-d’œuvre, la date et la durée de validité, "
              "les coordonnées et le numéro d’immatriculation de l’entreprise, et l’assurance souscrite avec les coordonnées de l’assureur (Service-Public, fiche F31144)."),
             ("Faut-il une autorisation pour refaire sa toiture ?", "À l’identique, en général non. Changer de matériau ou de couleur, ou créer une fenêtre de toit, demande une déclaration préalable en mairie, et davantage en secteur protégé."),
             ("Faut-il réparer ou refaire toute la toiture ?", "Quelques tuiles cassées ou une fuite localisée se réparent. Des fuites qui reviennent, une couverture poreuse ou une charpente abîmée imposent souvent une réfection. Le couvreur tranche lors de la visite."),
             ("Faut-il démousser sa toiture ?", "Les mousses retiennent l’humidité et abîment les tuiles avec le temps. Un démoussage est aussi l’occasion de faire vérifier l’état de la couverture."),
             ("Combien de temps dure une réfection de toiture ?", "Cela dépend de la surface, de la météo et de l’état de la charpente. Le couvreur vous donne un délai dans son devis."),
             ("L’assurance paie-t-elle la réparation du toit ?", "Cela dépend de la cause. Après une tempête, la garantie tempête de l’assurance habitation joue en général (Code des assurances, art. L122-7). Si la fuite vient de l’usure ou d’un manque d’entretien, la réparation du toit reste le plus souvent à votre charge, même quand les dégâts intérieurs sont couverts. C’est votre contrat qui tranche."),
             ("Des aides pour refaire sa toiture ?", "Refaire la couverture seule n’ouvre en général pas droit à MaPrimeRénov’ : les aides visent la rénovation énergétique, comme l’isolation de la toiture, réalisée par une entreprise RGE. La TVA est en revanche de 10 % dans un logement de plus de deux ans, et de 5,5 % si les travaux améliorent sa performance énergétique. Vérifiez votre cas sur france-renov.gouv.fr.")],
        brief="Bartier &amp; Co vous met gratuitement en relation avec le couvreur partenaire de votre secteur : réfection, fuite, zinguerie ou démoussage. Visite et devis offerts."),
    "facade": dict(
        title="Entreprise de ravalement de façade : devis gratuit",
        desc="Une entreprise de ravalement de votre secteur vient chiffrer : nettoyage, fissures, enduit, peinture, isolation par l’extérieur. Visite et devis gratuits.",
        kw="Ravalement de façade : devis gratuit", h2="Vos travaux de façade", price_h2="Prix d’un ravalement de façade",
        needs=[("Ravalement complet", "Nettoyage, reprise du support, enduit ou peinture de finition. <a class=\"link\" href=\"/devis-travaux/ravalement-facade/enduit-crepi/\">Crépi et enduit</a>"),
               ("Fissures", "Diagnostic de l’origine et reprise des fissures avant finition."),
               ("Nettoyage et peinture", "Façade rafraîchie quand le support est sain. <a class=\"link\" href=\"/devis-travaux/ravalement-facade/nettoyage/\">Devis nettoyage de façade</a>"),
               ("Isolation par l’extérieur", "Isolant posé sur les murs puis recouvert d’un enduit ou d’un bardage. <a class=\"link\" href=\"/devis-travaux/isolation/exterieur/\">Isolation par l’extérieur</a>")],
        faq=[("Que doit contenir un devis de ravalement ?",
              "Le détail de chaque poste en quantité et en prix unitaire (échafaudage, nettoyage, fissures, enduit, finition), la main-d’œuvre, la date et la durée de validité, les coordonnées et le numéro d’immatriculation de l’entreprise, et l’assurance souscrite avec les coordonnées de l’assureur (Service-Public, fiche F31144)."),
             ("Le ravalement est-il obligatoire ?", "À Paris et dans les communes inscrites sur une liste fixée par le préfet, la mairie peut imposer un ravalement au moins tous les dix ans. Ailleurs, la loi ne fixe pas de fréquence (Code de la construction et de l’habitation). Votre mairie vous dit si votre commune est concernée."),
             ("Faut-il une autorisation pour un ravalement ?", "Un ravalement qui modifie l’aspect extérieur demande en général une déclaration préalable en mairie. Vérifiez aussi le plan local d’urbanisme de votre commune."),
             ("Peut-on isoler en même temps que le ravalement ?", "Oui, c’est le bon moment pour une isolation par l’extérieur. Réalisée par une entreprise RGE, elle peut ouvrir droit à des aides : vérifiez-les sur france-renov.gouv.fr."),
             ("Quelle TVA pour un ravalement ?", "Dans un logement de plus de deux ans, la TVA est de 10 % sur un ravalement, et de 5,5 % s’il s’accompagne d’une isolation qui améliore la performance énergétique (Code général des impôts, art. 279-0 bis et 278-0 bis A).")],
        brief="Bartier &amp; Co vous met gratuitement en relation avec l’artisan façade partenaire de votre secteur : nettoyage, fissures, enduit, peinture ou isolation par l’extérieur. Visite et devis offerts."),
    "fenetres": dict(
        title="Remplacement de fenêtres : devis gratuit près de chez vous",
        desc="Un menuisier poseur de votre secteur chiffre vos fenêtres PVC, alu ou bois, porte d’entrée, baie vitrée ou volets. Visite et devis gratuits.",
        kw="Remplacement de fenêtres : devis gratuit", h2="Vos travaux de fenêtres et portes", price_h2="Prix d’une fenêtre PVC posée",
        needs=[("Remplacement de fenêtres", "PVC, aluminium ou bois, double vitrage, sur mesure."),
               ("Porte d’entrée", "Isolation, sécurité et style de la façade. <a class=\"link\" href=\"/devis-travaux/fenetres/porte-entree/\">Devis porte d’entrée</a>"),
               ("Baie vitrée", "Coulissante ou à galandage, création ou remplacement. <a class=\"link\" href=\"/devis-travaux/fenetres/baie-vitree/\">Devis baie vitrée</a>"),
               ("Volets", "Roulants, battants ou persiennes, motorisés ou non. <a class=\"link\" href=\"/devis-travaux/fenetres/volets/\">Devis volets roulants</a>")],
        faq=[("Que doit contenir un devis de fenêtres ?",
              "Pour chaque fenêtre : le type de pose, le matériau, les dimensions, le vitrage et la performance, avec la quantité et le prix unitaire. S’y ajoutent la main-d’œuvre, la date et la durée de validité, les coordonnées et le numéro d’immatriculation de l’entreprise, et l’assurance souscrite (Service-Public, fiche F31144)."),
             ("Pose en rénovation ou dépose totale ?", "En rénovation, la fenêtre neuve se pose sur l’ancien cadre : c’est plus rapide, mais la surface vitrée diminue un peu. En dépose totale, tout est retiré : c’est plus cher, avec un meilleur résultat. Le menuisier vous conseille lors de la visite."),
             ("PVC, aluminium ou bois ?", "Le PVC est le plus économique, l’aluminium permet des profils fins et de grandes baies, le bois apporte du cachet et demande plus d’entretien."),
             ("Faut-il une autorisation pour changer ses fenêtres ?", "Remplacer à l’identique ne demande en général rien. Changer l’aspect, le matériau, la couleur ou le découpage demande une déclaration préalable en mairie."),
             ("Des aides pour changer ses fenêtres ?", "Remplacer du simple vitrage par des fenêtres performantes peut ouvrir droit à des aides à la rénovation énergétique, avec une entreprise RGE : vérifiez votre cas sur france-renov.gouv.fr. Dans un logement de plus de deux ans, la TVA est de 5,5 % pour des fenêtres qui améliorent la performance énergétique, et de 10 % sinon.")],
        brief="Bartier &amp; Co vous met gratuitement en relation avec le menuisier partenaire de votre secteur, pour vos fenêtres, portes, baies vitrées ou volets. Visite et devis offerts."),
    "charpente": dict(
        title="Charpentier près de chez vous : devis charpente gratuit",
        desc="Un charpentier de votre secteur vient chiffrer : réparation, renfort, traitement du bois, surélévation. Visite et devis gratuits, un seul artisan.",
        kw="Charpentier : devis charpente gratuit", h2="Vos travaux de charpente", price_h2="Prix de travaux de charpente",
        needs=[("Réparation et renfort", "Pièces de bois abîmées remplacées ou doublées."),
               ("Traitement du bois", "Contre les insectes et les champignons, en curatif ou en préventif. <a class=\"link\" href=\"/devis-travaux/charpente/traitement/\">Devis traitement de charpente</a>"),
               ("Extension et surélévation", "Nouvelle charpente pour agrandir ou créer un étage."),
               ("Charpente neuve", "Traditionnelle ou en fermettes, souvent avec la couverture.")],
        faq=[("Que doit contenir un devis de charpente ?",
              "Les pièces remplacées ou renforcées, l’essence et la section du bois, le traitement prévu, chaque poste en quantité et en prix unitaire, la main-d’œuvre, la date et la durée de validité, les coordonnées de l’entreprise et l’assurance souscrite (Service-Public, fiche F31144)."),
             ("Faut-il un permis pour une surélévation ?", "Une surélévation crée de la surface : selon la surface ajoutée et le plan local d’urbanisme, il faut une déclaration préalable ou un permis de construire. Renseignez-vous en mairie avant de signer le devis."),
             ("Quels signes montrent qu’une charpente est abîmée ?", "Du bois qui s’effrite, de la sciure ou de petits trous, des traces d’humidité, une toiture qui se déforme. Au moindre doute, faites-la inspecter."),
             ("Quand faut-il traiter une charpente ?", "En présence d’insectes ou de champignons, et en prévention lors d’une réfection de toiture, quand le bois est accessible."),
             ("Faut-il refaire la couverture en même temps ?", "Souvent, oui : la charpente est alors à nu et les deux chantiers se coordonnent. Le charpentier et le couvreur peuvent travailler ensemble.")],
        brief="Bartier &amp; Co vous met gratuitement en relation avec le charpentier partenaire de votre secteur, pour réparer, traiter ou créer votre charpente. Visite et devis offerts."),
    "isolation": dict(
        title="Entreprise d’isolation des combles et murs : devis gratuit",
        desc="Une entreprise d’isolation de votre secteur chiffre vos combles perdus ou aménagés, vos murs ou votre toiture. Visite et devis gratuits.",
        kw="Isolation des combles et des murs : devis gratuit", h2="Vos travaux d’isolation", price_h2="Prix de l’isolation des combles",
        needs=[("Combles perdus", "Isolant soufflé ou déroulé sur le plancher des combles."),
               ("Combles aménagés", "Isolation sous les rampants, par l’intérieur."),
               ("Murs par l’extérieur", "Isolant posé sur la façade puis recouvert. <a class=\"link\" href=\"/devis-travaux/isolation/exterieur/\">Devis isolation par l’extérieur</a>"),
               ("Toiture par l’extérieur", "Isolant posé sur la charpente lors d’une réfection, technique dite du sarking.")],
        faq=[("Que doit contenir un devis d’isolation ?",
              "Le type d’isolant, son épaisseur et sa résistance thermique, la surface traitée et le prix au m², la main-d’œuvre, la date et la durée de validité, les coordonnées de l’entreprise et l’assurance souscrite (Service-Public, fiche F31144). Pour les aides, l’entreprise doit être certifiée RGE."),
             ("Faut-il une autorisation pour isoler par l’extérieur ?", "En général oui : l’isolation par l’extérieur change l’aspect de la façade et demande une déclaration préalable en mairie."),
             ("Quelles aides pour isoler ses combles ?", "Les plus courantes sont MaPrimeRénov’ et les primes CEE des fournisseurs d’énergie. Leur montant dépend des travaux et de vos revenus, et toutes demandent une entreprise certifiée RGE. Les règles changent souvent : vérifiez votre cas sur france-renov.gouv.fr avant de signer."),
             ("Combles perdus ou aménagés : quelle différence ?", "Des combles perdus ne sont pas habitables : l’isolant se pose sur le plancher, c’est le chantier le plus simple. Des combles aménagés sont habitables : l’isolant se pose sous la toiture."),
             ("Faut-il une entreprise RGE ?", "Pour obtenir des aides publiques, oui. Dites-le lors de notre appel : nous vous disons si l’artisan de votre secteur est certifié RGE.")],
        brief="Bartier &amp; Co vous met gratuitement en relation avec l’artisan partenaire de votre secteur, pour isoler vos combles, vos murs ou votre toiture. Visite et devis offerts."),
}


_QE = ("QuelleEnergie", "https://www.quelleenergie.fr/prix-travaux/isolation/renovation-toiture")
_SG_TOIT = ("Saint-Gobain, 03/2026", "https://www.lamaisonsaintgobain.fr/guides-travaux/toiture-charpente/prix-nettoyage-toiture-m2")
_SG_FAC = ("Saint-Gobain, 08/2026", "https://www.lamaisonsaintgobain.fr/facades/conseils/avant-de-vous-lancer-dans-les-travaux-de-facades/le-prix-d-un-ravalement-de-facade")
_SG_FEN = ("Saint-Gobain, 02/2026", "https://www.lamaisonsaintgobain.fr/guides-travaux/menuiseries-exterieures/prix-fenetre-pvc")
_OB_CH = ("Obat, 10/2024", "https://travaux.obat.fr/guides/tarif-charpentier/")
_HW_CH = ("Hellowatt, 12/2025", "https://www.hellowatt.fr/prime-energie/renovation-energetique/prix-m2")
_SG_ISO = ("Saint-Gobain, 07/2026", "https://www.lamaisonsaintgobain.fr/guides-travaux/isolation/prix-isolation-combles")
DETAIL = {
    "toiture": [("Entretien avec quelques réparations", "10 à 80 €/m²", _QE), ("Nettoyage et démoussage", "25 à 35 €/m²", _SG_TOIT),
                ("Démoussage et traitement hydrofuge", "35 à 45 €/m²", _SG_TOIT), ("Remplacement de la couverture", "60 à 300 €/m²", _QE),
                ("Remplacement de toute la toiture", "180 à 500 €/m²", _QE), ("Isolation par l’extérieur (sarking)", "120 à 250 €/m²", _QE)],
    "facade": [("Mise en peinture", "50 à 75 €/m²", _SG_FAC), ("Projection d’enduit", "50 à 70 €/m²", _SG_FAC), ("Ravalement avec isolant", "110 à 215 €/m²", _SG_FAC)],
    "fenetres": [("Fenêtre PVC en remplacement", "870 à 1\u00a0170 € TTC", _SG_FEN), ("Fenêtre PVC en création d’ouverture", "environ 2\u00a0400 € TTC", _SG_FEN)],
    "charpente": [("Rénovation de la charpente seule", "150 à 200 € TTC/m²", _HW_CH), ("Charpente et couverture", "180 à 250 € TTC/m²", _HW_CH),
                  ("Traitement préventif ou curatif du bois", "40 à 180 €/m²", _OB_CH)],
    "isolation": [("Combles perdus, accès par l’intérieur", "40 €/m² TTC", _SG_ISO), ("Combles perdus, accès par le toit", "45 €/m² TTC", _SG_ISO),
                  ("Combles aménagés, par l’intérieur", "130 à 180 €/m² TTC", _SG_ISO), ("Combles aménagés, par le toit", "240 €/m² TTC", _SG_ISO)],
}


def detail_table(key):
    rows = "".join(f'<tr><td>{a}</td><td>{b}</td><td><a class="link" href="{u}" target="_blank" rel="noopener">{n}</a></td></tr>' for a, b, (n, u) in DETAIL[key])
    return f'<table class="pf-tab"><caption>Prix indicatifs, pose comprise</caption><thead><tr><th scope="col">Travaux</th><th scope="col">Prix</th><th scope="col">Source</th></tr></thead><tbody>{rows}</tbody></table>'


def build_trade(img, phone, phone_txt, crumbs, key):
    t = next(x for x in TRADES if x[0] == key)
    P = PAGES[key]
    blocks = build(img, phone, phone_txt, crumbs, parts=True)
    form = blocks["form"].replace('<form class="pf-form"', f'<form class="pf-form" data-preset="{key}"', 1)
    url, _ = img(t[3])
    ph_attr = (f'srcset="{ISO_SRCSET}" sizes="(max-width: 760px) 100vw, 50vw" src="{ISO_PHOTO}-1400x1050.webp"' if key == "isolation" else f'src="{url}"')
    hero = f"""<section class="sheet pf-hero" id="haut" data-tone="light">
  <div class="grid pf-hero-grid">
    <div class="pf-intro">
      {crumbs}
      <div class="pf-h1"><h1 class="pf-kw">{P["kw"]}</h1> <p class="pf-big">Pas cinq <span class="pf-who">{t[2]}</span>. <br>Un seul, près de chez vous.</p></div>
      <p class="lead">Décrivez vos travaux en 1 minute.<br>Nous vous rappelons en moins de 5 minutes en semaine, et nous fixons la visite.</p>
      {trust("d-only")}
    </div>
    {form}
    <div class="pf-mtrust m-only">{trust()}</div>
  </div>
</section>"""
    needs = "".join(f"<li><h3>{a}</h3><p>{b}</p></li>" for a, b in P["needs"])
    needs = f"""<section class="sheet" id="travaux" data-tone="light">
  <div class="grid sp-head"><h2 data-split>{P["h2"]}</h2><p>{t[6]}</p></div>
  <div class="pf-split"><figure class="frame pf-ph"><img {ph_attr} alt="{t[7]}" width="1200" height="900" loading="lazy"></figure><ul class="pf-checks pf-needs">{needs}</ul></div>
  <div class="pf-band"><p>Devis {t[1].lower()} en 1 minute <span class="pf-band-sub">Visite et devis offerts. Sans engagement.</span></p><a class="btn" href="#projet"><span>Obtenir mon devis gratuit</span>{tick()}</a></div>
</section>"""
    price = f"""<section class="sheet" id="prix" data-tone="paper">
  <div class="grid sp-head"><h2 data-split>{P["price_h2"]}</h2><p>{t[9]}</p></div>
  <div class="pf-refbox"><p class="pf-ref">{REF[key][0]}</p><p class="pf-src">Source&nbsp;: {REF[key][1]}</p>{detail_table(key)}<p>Ce sont des moyennes : seule une visite permet un devis fiable.</p>
  <a class="btn" href="#projet"><span>Obtenir mon devis gratuit</span>{tick()}</a></div>
</section>"""
    brief = [("Le service", P["brief"])] + BRIEF[1:]
    brief = "".join(f"<div><dt>{a}</dt><dd>{b}</dd></div>" for a, b in brief)
    brief = f"""<section class="sheet pf-brief" data-tone="light" aria-labelledby="pf-brief-h">
  <div class="grid pf-brief-grid">
    <h2 id="pf-brief-h">Devis {t[1].lower()} : l’essentiel</h2>
    <dl class="pf-dl">{brief}</dl>
    <p class="pf-upd">Mis à jour le <time datetime="@@MAJ@@">@@MAJFR@@</time></p>
  </div>
</section>"""
    faq_items = trade_faq(key)
    rows = "\n".join(f'      <details class="fq"><summary><span>{q}</span><i class="fq-icon" aria-hidden="true"></i></summary><div class="fq-a"><p>{a}</p></div></details>' for q, a in faq_items)
    faq = f"""<section class="faq sheet" id="questions" data-kind="faq" data-tone="paper">
  <div class="grid fq-grid">
    <div class="fq-head"><h2 data-split>Devis {t[1].lower()} : vos questions</h2><p>Une autre question&nbsp;? <a class="link" href="tel:{phone}">{phone_txt}</a></p><p><a class="link" href="/devis-travaux/#questions">Voir toutes les questions</a></p></div>
    <div class="fq-list">
{rows}
    </div>
  </div>
</section>"""
    others = "".join(f'<li><a class="link" href="/devis-travaux/{SLUG[x[0]]}/">{x[5]}</a></li>' for x in TRADES if x[0] != key)
    others = f"""<section class="sheet pf-others" data-tone="light">
  <div class="grid sp-head"><h2 data-split>Autres travaux</h2><p><a class="link" href="/devis-travaux/">Tous les devis de travaux</a></p></div>
  <ul class="pf-olist">{others}</ul>
</section>"""
    ser_h = {"toiture": "Avant de signer avec un couvreur", "facade": "Avant de signer un devis de ravalement", "fenetres": "Avant de signer avec un menuisier",
             "charpente": "Avant de signer avec un charpentier", "isolation": "Avant de signer un devis d’isolation"}[key]
    serious = f"""<section class="sheet pf-ser-short" id="artisan-serieux" data-tone="light">
  <div class="grid sp-head"><h2 data-split>{ser_h}</h2><p>Vérifiez cinq points&nbsp;: son immatriculation (<a class="link" href="https://annuaire-entreprises.data.gouv.fr/" target="_blank" rel="noopener">annuaire-entreprises.data.gouv.fr</a>), son assurance décennale, un devis écrit et détaillé, la certification RGE si vous visez des aides (<a class="link" href="https://france-renov.gouv.fr/" target="_blank" rel="noopener">france-renov.gouv.fr</a>), et l’absence de pression pour signer. <a class="link" href="/devis-travaux/#artisan-serieux">Le détail des 5 points</a></p></div>
</section>"""
    seq = [hero, blocks["promise"], needs, price] + [example(key)] + ([blocks["leak"]] if key == "toiture" else []) + [serious, brief, faq, others, blocks["end"]]
    return "\n\n".join(seq)


SP_DEVIS = "https://www.service-public.gouv.fr/particuliers/vosdroits/F31144"
DEVIS = {  # postes courants d'un devis, sans prix : les prix sourcés sont dans le tableau « prix » de chaque page
    "toiture": [
        ("Installation de chantier, échafaudage, protections", "forfait", "La durée de location et la protection des abords"),
        ("Dépose de l’ancienne couverture", "m²", "L’évacuation et le tri des déchets : compris ou non"),
        ("Écran sous-toiture", "m²", "Le type de membrane, respirante ou non"),
        ("Liteaux et contre-liteaux", "m²", "Un remplacement complet ou partiel"),
        ("Tuiles ou ardoises neuves", "m²", "La marque, le modèle, le coloris et le nombre au m²"),
        ("Faîtage, rives, arêtiers", "mètre linéaire", "La pose : scellée au mortier ou à sec"),
        ("Zinguerie : gouttières, descentes, solins", "mètre linéaire", "Le matériau : zinc, cuivre ou aluminium"),
        ("Main-d’œuvre", "heure ou forfait", "Le nombre de couvreurs et la durée du chantier"),
        ("TVA", "taux", "10 % pour l’entretien d’un logement de plus de deux ans, 5,5 % avec une isolation qui améliore la performance énergétique")],
    "facade": [
        ("Installation de chantier, échafaudage, protections", "forfait ou m²", "La protection des fenêtres et des abords, et l’autorisation de voirie si l’échafaudage est sur le trottoir"),
        ("Nettoyage du support", "m²", "La technique, adaptée au matériau de la façade"),
        ("Traitement des fissures", "mètre linéaire", "L’origine des fissures et la façon de les reprendre"),
        ("Reprise de l’enduit ou des joints", "m²", "Un enduit adapté au support, à la chaux sur un mur ancien par exemple"),
        ("Finition : peinture, enduit ou crépi", "m²", "Le produit, le nombre de couches et la référence de la teinte"),
        ("Isolation par l’extérieur, si prévue", "m²", "L’isolant, son épaisseur et sa résistance thermique"),
        ("Main-d’œuvre", "heure ou forfait", "Le nombre de personnes et la durée du chantier"),
        ("TVA", "taux", "10 % pour un ravalement dans un logement de plus de deux ans, 5,5 % s’il s’accompagne d’une isolation qui améliore la performance énergétique")],
    "fenetres": [
        ("Type de pose", "par fenêtre", "Rénovation sur l’ancien cadre ou dépose totale : la surface vitrée n’est pas la même"),
        ("Fenêtre fournie", "par fenêtre", "Le matériau, les dimensions, le vitrage et le coefficient Uw : plus il est bas, mieux la fenêtre isole"),
        ("Pose et étanchéité", "par fenêtre", "Les joints, le calfeutrement et les finitions intérieures"),
        ("Volets et coffres", "par fenêtre", "Le type de volet et la motorisation, si elle est prévue"),
        ("Habillages et appuis", "mètre linéaire", "Les matériaux et la teinte"),
        ("Évacuation des anciennes menuiseries", "forfait", "Comprise ou non"),
        ("TVA", "taux", "5,5 % pour des fenêtres qui améliorent la performance énergétique d’un logement de plus de deux ans, sinon 10 %")],
    "charpente": [
        ("Accès et sécurité : échafaudage, étaiement", "forfait", "La durée et ce qui est protégé"),
        ("Dépose des pièces abîmées", "mètre linéaire", "Quelles pièces, et pourquoi elles sont déposées"),
        ("Remplacement ou renfort des pièces", "mètre linéaire", "L’essence du bois, la section des pièces et leur traitement"),
        ("Traitement du bois", "m²", "Préventif ou curatif, contre les insectes ou les champignons, et le produit utilisé"),
        ("Dépose et repose de la couverture, si nécessaire", "m²", "Ce qui est réutilisé et ce qui est remplacé"),
        ("Main-d’œuvre", "heure ou forfait", "Le nombre de charpentiers et la durée du chantier"),
        ("TVA", "taux", "10 % dans un logement de plus de deux ans")],
    "isolation": [
        ("Préparation des combles", "forfait", "La protection des gaines et des spots, et l’accès aux combles"),
        ("Isolant fourni et posé", "m²", "Le type d’isolant, soufflé ou déroulé, son épaisseur et sa résistance thermique R"),
        ("Pare-vapeur", "m²", "Sa présence et sa continuité"),
        ("Écarts au feu autour des conduits", "par conduit", "La distance laissée autour des conduits de cheminée"),
        ("Trappe d’accès", "par trappe", "Son isolation et son étanchéité"),
        ("Main-d’œuvre", "heure ou forfait", "La durée du chantier"),
        ("TVA", "taux", "5,5 % pour des travaux qui améliorent la performance énergétique d’un logement de plus de deux ans")],
}
DEVIS_HEAD = {
    "toiture": ("Exemple de devis de toiture : les lignes à vérifier", "Un devis de réfection se lit poste par poste, et chaque ligne a son point à vérifier avant de signer.", "Postes d’un devis de réfection de toiture"),
    "facade": ("Exemple de devis de ravalement : les lignes à vérifier", "Un devis de ravalement se lit de l’échafaudage à la finition, poste par poste.", "Postes d’un devis de ravalement de façade"),
    "fenetres": ("Exemple de devis de fenêtres : les lignes à vérifier", "Chaque fenêtre a sa ligne : le devis doit dire ce qui est posé, et comment.", "Postes d’un devis de remplacement de fenêtres"),
    "charpente": ("Exemple de devis de charpente : les lignes à vérifier", "Le prix dépend de l’état du bois : le devis doit dire quelles pièces sont remplacées ou renforcées.", "Postes d’un devis de travaux de charpente"),
    "isolation": ("Exemple de devis d’isolation des combles : les lignes à vérifier", "Un devis d’isolation se juge sur l’isolant posé : son épaisseur et sa résistance thermique doivent y figurer.", "Postes d’un devis d’isolation des combles"),
}
DEVIS_MENTIONS = ["La date du devis et sa durée de validité", "Le nom, l’adresse et la forme juridique de l’entreprise",
                  "Son numéro d’immatriculation (Siren et répertoire des métiers pour un artisan) et son numéro de TVA",
                  "Votre nom et l’adresse du chantier", "La date de début et la durée estimée des travaux",
                  "Le détail de chaque prestation, en quantité et en prix unitaire, et le prix de la main-d’œuvre",
                  "Les frais de déplacement, s’il y en a, et les modalités de paiement",
                  "L’assurance souscrite, les coordonnées de l’assureur et la zone couverte"]


def example(key):
    h2, intro, cap = DEVIS_HEAD[key]
    rows = "".join(f'<tr><td>{a}</td><td>{b}</td><td>{c}</td></tr>' for a, b, c in DEVIS[key])
    lis = "".join(f"<li>{m}</li>" for m in DEVIS_MENTIONS)
    note = ("Ces mentions sont obligatoires pour une réparation ou un entretien de toiture ; exigez-les aussi pour une réfection." if key == "toiture"
            else "Ces mentions sont obligatoires pour une réparation ou un entretien ; exigez-les aussi pour des travaux de rénovation.")
    return f"""<section class="sheet" id="exemple-devis" data-tone="light">
  <div class="grid sp-head"><h2 data-split>{h2}</h2><p>{intro}</p></div>
  <div class="pf-refbox" style="max-width:none">
    <table class="pf-tab"><caption>{cap}</caption><thead><tr><th scope="col">Poste</th><th scope="col">Unité</th><th scope="col">À vérifier</th></tr></thead><tbody>{rows}</tbody></table>
    <h3 style="margin-top:24px">Les mentions que le devis doit porter</h3>
    <ul style="margin:12px 0 0;padding-left:20px;list-style:disc;line-height:1.6">{lis}</ul>
    <p class="pf-src">Source : <a class="link" href="{SP_DEVIS}" target="_blank" rel="noopener">Service-Public, fiche F31144</a>. {note}</p>
    <a class="btn" href="#projet"><span>Obtenir mon devis gratuit</span>{tick()}</a>
  </div>
</section>"""


def trade_faq(key):
    P = PAGES[key]
    t = next(x for x in TRADES if x[0] == key)
    general = {q: a for q, a in FAQ}
    price_q = {"toiture": "Combien coûte une réfection de toiture ?", "facade": "Combien coûte un ravalement de façade ?",
               "fenetres": "Combien coûte le remplacement d’une fenêtre ?"}
    out = []
    if key in price_q:
        out.append((price_q[key], general[price_q[key]]))
    else:
        out.append({"charpente": ("Combien coûtent des travaux de charpente ?", "Comptez de 150 à 200 €/m² TTC pour rénover la charpente seule, et de 180 à 250 €/m² TTC avec la couverture, selon Hellowatt (2025). Tout dépend de l’état du bois : remplacer quelques pièces coûte bien moins que refaire la charpente. Le charpentier le voit lors d’une visite gratuite."),
                    "isolation": ("Combien coûtent des travaux d’isolation ?", "Pour des combles perdus, comptez environ 40 €/m² TTC pose comprise si l’accès se fait par l’intérieur, 45 €/m² par le toit, selon La Maison Saint-Gobain (2026). Sous les rampants ou par l’extérieur, c’est plus cher. Seule une visite permet un devis fiable, et elle est gratuite.")}[key])
    out += P["faq"]
    if key in ("toiture", "fenetres"):  # chantiers où l'on demande souvent une petite intervention
        out.append(("Prenez-vous aussi les petites réparations ?", general["Prenez-vous aussi les petites réparations ?"]))
    if key == "toiture":
        out.append(("J’ai une fuite de toiture, que faire tout de suite ?", general["J’ai une fuite de toiture, que faire tout de suite ?"]))
    return out


def trade_schema(SITE, faq_ld, bc_ld, key):
    import re
    clean = lambda s: re.sub("<[^>]+>", "", s).replace("&amp;", "&").replace("&nbsp;", " ")
    t = next(x for x in TRADES if x[0] == key)
    P = PAGES[key]
    path = f"{PATH}{SLUG[key]}/"
    graph = [
        {"@type": "WebPage", "@id": SITE + path, "url": SITE + path, "name": P["title"], "description": P["desc"], "inLanguage": "fr-FR",
         "dateModified": "@@MAJ@@", "isPartOf": {"@id": SITE + "/#website"}, "publisher": {"@id": SITE + "/#org"}},
        {"@type": "Service", "name": f"Devis {t[5].lower()}", "serviceType": f"Mise en relation avec un artisan : {t[5].lower()}", "description": clean(P["brief"]), "url": SITE + path,
         "areaServed": {"@type": "Country", "name": "France"}, "audience": {"@type": "Audience", "audienceType": "Propriétaires de maison"},
         "provider": {"@type": "Organization", "@id": SITE + "/#org", "name": "Bartier & Co", "url": SITE + "/"},
         "offers": {"@type": "Offer", "price": "0", "priceCurrency": "EUR", "description": "Gratuit pour le particulier : mise en relation, visite et devis de l'artisan"}},
        faq_ld([qa for qa in trade_faq(key) if qa[0] != "Prenez-vous aussi les petites réparations ?"]), bc_ld(("Devis travaux", PATH), (t[1], path))]
    if key == "toiture":
        graph.append({"@type": "HowTo", "name": "Fuite de toiture ? Les 5 bons réflexes", "step": [{"@type": "HowToStep", "position": i, "name": a, "text": clean(b)} for i, (a, b) in enumerate(LEAK, 1)]})
    return link_graph(SITE, path, {"@context": "https://schema.org", "@graph": graph})


CSS_TRADE = """<style id="pf-css-2">
.pf-tl{color:inherit;text-decoration:none}.pf-tl:hover{color:var(--accent)}
.pf-ref{margin-top:10px;font-weight:500}
.pf-src{font-size:.8rem;color:var(--muted)}
.pf-src a{font-size:inherit}
.pf-more{margin-top:8px;display:inline-block;font-size:.88rem}
.pf-prices li{display:flex;flex-direction:column;gap:4px}
.pf-split{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:clamp(20px,3vw,48px);padding:0 var(--cell);align-items:start}
.pf-ph{aspect-ratio:4 / 3;margin:0}.pf-ph img{width:100%;height:100%;object-fit:cover}
.pf-needs{grid-template-columns:1fr 1fr;padding:0}
.pf-refbox{display:flex;flex-direction:column;align-items:flex-start;gap:10px;max-width:56ch;padding:0 var(--cell)}
.pf-refbox .pf-ref{font:400 clamp(1.3rem,2vw,1.7rem)/1.25 var(--f-display);letter-spacing:-.01em}
.pf-olist{display:flex;flex-wrap:wrap;gap:12px 28px;margin:0;padding:0 var(--cell);list-style:none;font-size:1.05rem}
@media (max-width:760px){.pf-split{grid-template-columns:1fr}.pf-needs{grid-template-columns:1fr}}
/* Aération mobile */
@media (max-width:760px){
  :root{--sp:76px}
  .pf-hero{padding-top:calc(var(--hdr) + 24px);padding-bottom:60px}
  .pf-hero-grid{row-gap:24px}
  .pf-intro{gap:16px}
  .pf-h1{gap:12px}
  .pf-card{padding:24px 20px}
  .pf-live{margin:0 0 16px}
  .pf-bar{margin:16px 0 24px}
  .pf-step legend{margin-bottom:16px}
  .pf-grid,.pf-list{gap:12px}
  .pf-tile,.pf-opt{min-height:56px}
  .pf-fields{gap:16px;margin-bottom:20px}
  .pf-trust{gap:12px 16px}
  .sp-head{row-gap:24px;margin-bottom:40px}
  .sp-head p{line-height:1.55}
  .pf-proms{gap:32px 16px}
  .pf-proms li{padding-top:16px;gap:12px}
  .pf-trades{gap:32px 16px}
  .pf-trade{gap:12px}
  .pf-howto,.pf-checks,.pf-prices{gap:32px}
  .pf-howto li,.pf-checks li,.pf-prices li{padding-top:16px}
  .pf-howto h3,.pf-checks h3,.pf-prices h3{margin-bottom:12px}
  .pf-howto p,.pf-checks p,.pf-prices p,.pf-time p,.pf-trade p{font-size:.95rem;line-height:1.55}
  .pf-time li{padding-bottom:32px}
  .pf-time h3{margin-bottom:8px}
  .sp-row > *{padding-top:16px;padding-bottom:16px}
  .pf-band{margin-top:40px;padding:24px 20px;gap:16px}
  .pf-mid{margin-top:40px;gap:16px 20px}
  .pf-dl{gap:24px}
  .pf-end-grid{row-gap:28px}
  .pf-end-grid > div{gap:24px}
  .fq summary{padding-top:1.5rem;padding-bottom:1.5rem}
}
</style>"""

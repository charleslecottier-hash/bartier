# Page « particuliers » : capter la demande des propriétaires (toiture, façade, fenêtres, charpente, isolation)
# puis les mettre en relation avec un seul artisan de leur secteur.
# Contenu construit sur les recherches Google Trends (France, 5 ans) : « devis toiture », « prix toiture »,
# « réparation fuite toiture », « ravalement de façade » (personne ne cherche « façadier »), « prix fenêtre pvc »,
# « isolation des combles », « [métier] autour de moi », aides à l'isolation.
# SEO : mots-clés dans le titre, le H1, les H2 et H3. GEO : encadré « En bref » factuel, réponses courtes et directes,
# listes numérotées, date de mise à jour visible, sources officielles en lien, données structurées alignées sur le texte.

PATH = "/devis-travaux/"
UPDATED = "2026-11-18"
UPDATED_TXT = "18 novembre 2026"
TITLE = "Devis toiture, façade, fenêtres, isolation : un artisan local | Bartier & Co"
DESC = ("Décrivez vos travaux en 1 minute : rappel en moins de 5 min et un seul artisan local vient chiffrer. "
        "Toiture, façade, fenêtres, charpente, isolation. Gratuit.")

TRADES = [
    # clé, libellé, artisan (titre dynamique), photo, besoins (étape 2), titre SEO, texte, alt, titre prix, ce qui fait le prix
    ("toiture", "Toiture", "couvreurs", "Un couvreur pose",
     ["Fuite ou dégât urgent", "Réfection complète", "Réparation, tuiles, zinguerie", "Démoussage, nettoyage"],
     "Toiture et couverture",
     "Réfection de toiture, réparation de fuite, tuiles cassées, zinguerie et gouttières, démoussage.",
     "Couvreur en train de réparer une toiture en tuiles",
     "Prix d’une réfection de toiture",
     "La surface, le matériau (tuiles, ardoise, bac acier), l’état de la charpente et l’accès au toit."),
    ("facade", "Façade", "façadiers", "Une façade en rénovation",
     ["Ravalement complet", "Fissures, réparation", "Nettoyage, peinture", "Isolation par l’extérieur"],
     "Ravalement de façade",
     "Ravalement, reprise de fissures, enduit, nettoyage et peinture, isolation par l’extérieur.",
     "Façade de maison en cours de ravalement",
     "Prix d’un ravalement de façade",
     "La surface, l’état du support, la finition choisie et l’échafaudage."),
    ("fenetres", "Fenêtres et portes", "menuisiers", "Un menuisier pose",
     ["Remplacer des fenêtres", "Porte d’entrée", "Baie vitrée", "Volets"],
     "Fenêtres et portes",
     "Fenêtres PVC, alu ou bois, double vitrage, porte d’entrée, baie vitrée, volets roulants.",
     "Menuisier posant une fenêtre",
     "Prix de fenêtres posées",
     "Le nombre et la taille des ouvertures, le matériau, le vitrage et le type de pose, en rénovation ou en dépose totale."),
    ("charpente", "Charpente", "charpentiers", "Une charpente en bois",
     ["Réparation, renfort", "Traitement du bois", "Extension, surélévation", "Charpente neuve"],
     "Charpente",
     "Réparation et renfort, traitement du bois, extension, surélévation, charpente neuve.",
     "Charpente en bois en cours de pose",
     "Prix de travaux de charpente",
     "L’état du bois, la portée, le traitement nécessaire et l’accès au chantier."),
    ("isolation", "Isolation", "artisans", "Isolation d",
     ["Combles", "Murs par l’extérieur", "Toiture", "Je ne sais pas encore"],
     "Isolation des combles et des murs",
     "Isolation des combles perdus ou aménagés, des murs par l’extérieur, de la toiture.",
     "Isolation de combles en laine minérale",
     "Prix de l’isolation des combles",
     "La surface, la technique, l’isolant choisi et les aides auxquelles vous avez droit."),
]

BRIEF = [
    ("Le service", "Bartier &amp; Co met en relation les propriétaires avec un artisan du bâtiment de leur secteur pour des travaux de toiture, façade, fenêtres, charpente ou isolation."),
    ("Le prix pour vous", "Gratuit et sans engagement, visite et devis de l’artisan compris. Les artisans partenaires rémunèrent Bartier &amp; Co."),
    ("Le délai", "Rappel en moins de 5 minutes, du lundi au vendredi de 8 h à 19 h, en priorité pour les fuites et dégâts urgents. Hors de ces horaires, dès l’ouverture suivante."),
    ("Combien d’artisans", "Un seul par métier et par secteur. Vos coordonnées ne sont jamais revendues."),
    ("La zone", "Partout en France, avec des artisans locaux."),
]

LEAK = [
    ("Mettez-vous en sécurité", "Éloignez l’eau des prises et des appareils électriques. En cas de doute, coupez le courant de la pièce."),
    ("Limitez les dégâts", "Placez des récipients, protégez le mobilier et épongez. Ne montez pas sur le toit, surtout par temps de pluie ou de vent."),
    ("Prenez des photos", "Plafond, murs, objets abîmés et, si vous la voyez sans risque, la partie du toit touchée."),
    ("Prévenez votre assureur", "Déclarez le dégât des eaux dans le délai prévu par votre contrat d’assurance habitation, souvent cinq jours ouvrés."),
    ("Faites intervenir un couvreur", "Il trouve l’origine de la fuite, pose une protection provisoire si besoin, puis chiffre la réparation."),
]

SERIOUS = [
    ("Une entreprise immatriculée", 'Son numéro SIREN se vérifie gratuitement sur <a class="link" href="https://annuaire-entreprises.data.gouv.fr/" target="_blank" rel="noopener">annuaire-entreprises.data.gouv.fr</a>.'),
    ("Une assurance décennale", "Elle est obligatoire pour les travaux de construction. Demandez l’attestation : l’assureur doit aussi figurer sur le devis."),
    ("Un devis écrit et détaillé", "Matériaux, quantités, main-d’œuvre, délais et conditions de paiement, avant tout début de travaux."),
    ("La mention RGE si vous visez des aides", 'Pour l’isolation, les aides publiques demandent une entreprise RGE. L’annuaire officiel est sur <a class="link" href="https://france-renov.gouv.fr/" target="_blank" rel="noopener">france-renov.gouv.fr</a>.'),
    ("Pas de pression", "Méfiez-vous du démarchage « après la tempête » et des réductions valables seulement aujourd’hui. Un artisan sérieux vous laisse le temps de comparer."),
]

FAQ = [
    ("Est-ce vraiment gratuit ?",
     "Oui. Notre service est gratuit pour vous : ce sont les artisans partenaires qui nous rémunèrent. Vous ne payez que les travaux, et seulement si vous acceptez le devis."),
    ("La visite et le devis de l’artisan sont-ils payants ?",
     "Non. L’artisan vient voir le chantier et vous remet son devis sans frais pour vous. Vous restez libre de ne pas donner suite."),
    ("Combien d’entreprises vont m’appeler ?",
     "Une seule : nous d’abord, pour vérifier votre projet, puis l’artisan retenu. Vos coordonnées ne sont ni revendues ni envoyées à plusieurs entreprises."),
    ("Comment trouver un bon couvreur près de chez moi ?",
     "Cherchez un artisan local, immatriculé, assuré en décennale, qui se déplace pour voir le toit avant de chiffrer. Décrivez vos travaux ici : nous vous présentons le couvreur partenaire de votre secteur."),
    ("Combien coûte une réfection de toiture ?",
     "Le prix dépend de la surface, du matériau (tuiles, ardoise, bac acier), de l’état de la charpente et de l’accès au toit. Un prix au mètre carré trouvé en ligne reste une moyenne : seule une visite permet un devis fiable."),
    ("Combien coûte un ravalement de façade ?",
     "Il dépend de la surface, de l’état du support, de la finition et de l’échafaudage. Des fissures ou un enduit abîmé changent fortement le prix : l’artisan les évalue lors de la visite."),
    ("Combien coûte le remplacement d’une fenêtre ?",
     "Il dépend de la taille, du matériau (PVC, alu, bois), du vitrage et du type de pose : en rénovation sur l’ancien cadre, ou en dépose totale. Le devis détaille chaque fenêtre."),
    ("J’ai une fuite de toiture, que faire tout de suite ?",
     "Éloignez l’eau des prises, protégez le mobilier, photographiez les dégâts et prévenez votre assureur dans le délai de votre contrat, souvent cinq jours ouvrés. Dans le formulaire, choisissez « Fuite ou dégât urgent » : ces demandes sont rappelées en priorité."),
    ("Puis-je obtenir des aides pour mes travaux ?",
     "Certains travaux de rénovation énergétique, comme l’isolation, peuvent ouvrir droit à des aides publiques s’ils sont réalisés par une entreprise certifiée RGE. Les conditions changent chaque année : vérifiez-les sur france-renov.gouv.fr et parlez-en lors de notre appel."),
    ("Où intervenez-vous ?",
     "Partout en France, avec des artisans locaux. Si aucun artisan partenaire ne couvre encore votre commune, nous vous le disons dès l’appel."),
    ("Que faites-vous de mes données ?",
     "Elles servent uniquement à traiter votre demande et à la transmettre à l’artisan retenu. Elles ne sont jamais revendues. Vous pouvez demander leur suppression à contact@bartierandco.com."),
]


def tick():
    return '<svg class="tick" viewBox="0 0 10 10" aria-hidden="true"><path d="M1 1h8v8" fill="none" stroke="currentColor" stroke-width="1.4"/></svg>'


def check():
    return '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="m5 12.5 4.5 4.5L19 7.5" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></svg>'


def trust(cls=""):
    return f"""<ul class="pf-trust {cls}">
        <li>{check()}Visite et devis offerts</li><li>{check()}Sans engagement</li><li>{check()}Jamais revendu</li>
      </ul>"""


def build(img, phone, phone_txt, crumbs):
    tiles = "".join(f'<button type="button" class="pf-tile" data-v="{t[0]}">{t[1]}</button>' for t in TRADES) + \
        '<button type="button" class="pf-tile" data-v="autre">Autre projet</button>'
    form = f"""<div class="pf-card" id="projet">
      <form class="pf-form" novalidate aria-label="Demande de devis de travaux">
        <div class="pf-top"><p class="pf-count">Étape <b class="pf-n">1</b> sur 5</p><button type="button" class="pf-back" hidden>← Retour</button></div>
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
        <fieldset class="pf-step" data-step="5"><legend>Où et comment vous joindre&nbsp;?</legend>
          <div class="pf-fields">
            <label class="pf-f"><span>Code postal du chantier</span><input name="code_postal" inputmode="numeric" autocomplete="postal-code" maxlength="5" placeholder="Ex. 80000" required></label>
            <label class="pf-f"><span>Prénom</span><input name="prenom" autocomplete="given-name" placeholder="Votre prénom" required></label>
            <label class="pf-f is-wide"><span>Téléphone</span><input name="telephone" type="tel" inputmode="tel" autocomplete="tel" placeholder="06 12 34 56 78" required></label>
          </div>
          <label class="pf-consent"><input type="checkbox" name="consentement" required><span>J’accepte d’être rappelé par Bartier &amp; Co au sujet de ce projet et mis en relation avec un artisan partenaire.</span></label>
          <input class="pf-hp" name="site_web" tabindex="-1" autocomplete="off" aria-hidden="true">
          <p class="pf-err" role="alert" hidden></p>
          <button type="submit" class="btn pf-submit"><span>Être rappelé gratuitement</span>{tick()}</button>
          <p class="pf-small">Gratuit, sans engagement. Vos coordonnées ne sont jamais revendues.</p>
        </fieldset>
        <div class="pf-done" hidden>
          <span class="pf-ok">{check()}</span>
          <p class="pf-done-h">C’est noté<span class="pf-name"></span>.</p>
          <p class="pf-when"></p>
          <ol class="pf-next"><li>Nous vérifions votre projet avec vous au téléphone.</li><li>Nous vous présentons l’artisan de votre secteur.</li><li>Il vient voir le chantier et vous remet son devis.</li></ol>
          <a class="pf-wa" target="_blank" rel="noopener" data-wa="particulier">Envoyer aussi ma demande sur WhatsApp</a>
        </div>
      </form>
    </div>"""

    hero = f"""<section class="sheet pf-hero" id="haut" data-tone="light">
  <div class="grid pf-hero-grid">
    <div class="pf-intro">
      {crumbs}
      <h1 class="pf-h1"><span class="pf-kw">Devis toiture, façade, fenêtres, isolation</span><span class="pf-big">Pas cinq <span class="pf-who">artisans</span>.<br>Un seul. Le bon.</span></h1>
      <p class="lead">Décrivez vos travaux en 1 minute.<br>On vous rappelle en 5.</p>
      {trust("d-only")}
    </div>
    {form}
    <div class="pf-mtrust m-only">{trust()}</div>
  </div>
</section>"""

    brief = "".join(f"<div><dt>{a}</dt><dd>{b}</dd></div>" for a, b in BRIEF)
    brief = f"""<section class="sheet pf-brief" data-tone="paper" aria-labelledby="pf-brief-h">
  <div class="grid pf-brief-grid">
    <h2 id="pf-brief-h">Bartier &amp; Co en bref</h2>
    <dl class="pf-dl">{brief}</dl>
    <p class="pf-upd">Mis à jour le <time datetime="{UPDATED}">{UPDATED_TXT}</time></p>
  </div>
</section>"""

    cards = []
    for k, l, who, photo, needs, h3, words, alt, ph, pr in TRADES:
        url, _ = img(photo)
        cards.append(f"""    <li class="pf-trade"><figure class="frame"><img src="{url}" alt="{alt}" width="900" height="676" loading="lazy"></figure>
      <h3>{h3}</h3><p>{words}</p><a class="link pf-pick" href="#projet" data-v="{k}">Devis {l.lower()}</a></li>""")
    trades = f"""<section class="sheet" id="travaux" data-tone="light">
  <div class="grid sp-head"><h2 data-split>Toiture, façade, fenêtres, charpente, isolation</h2><p>Les gros travaux de la maison. Un artisan local pour chacun.</p></div>
  <ul class="pf-trades">
{chr(10).join(cards)}
  </ul>
</section>"""

    steps = """<section class="sheet" data-tone="paper">
  <div class="grid sp-head"><h2 data-split>Votre devis en 3 étapes</h2><p>Une minute de votre temps. Le reste, on s’en occupe.</p></div>
  <ol class="sp-cols">
    <li><span class="sp-n">01</span><h3>Vous décrivez vos travaux</h3><p>Cinq questions, une minute. Pas de compte à créer.</p></li>
    <li><span class="sp-n">02</span><h3>Nous vous rappelons</h3><p>En moins de cinq minutes, du lundi au vendredi de 8 h à 19 h. Nous vérifions votre besoin et vos disponibilités.</p></li>
    <li><span class="sp-n">03</span><h3>Un artisan vient chiffrer</h3><p>L’artisan de votre secteur visite le chantier et vous remet son devis, sans frais. Vous décidez ensuite, sans engagement.</p></li>
  </ol>
</section>"""

    compare = """<section class="sheet" data-tone="tint">
  <div class="grid sp-head"><h2 data-split>Pas cinq appels. Un seul.</h2><p>Sur beaucoup de sites de devis, votre demande part chez plusieurs entreprises. Le téléphone sonne, et vous racontez cinq fois le même projet.</p></div>
  <div class="sp-table" role="table" aria-label="Site de devis classique et Bartier &amp; Co">
    <div class="sp-row is-head" role="row"><span role="columnheader"></span><span role="columnheader">Site de devis classique</span><span role="columnheader">Bartier &amp; Co</span></div>
    <div class="sp-row" role="row"><span role="rowheader">Qui vous appelle</span><span role="cell">Souvent plusieurs entreprises</span><span role="cell">Nous, puis un seul artisan</span></div>
    <div class="sp-row" role="row"><span role="rowheader">Avant la visite</span><span role="cell">Vous répétez votre projet</span><span role="cell">Votre besoin est déjà vérifié</span></div>
    <div class="sp-row" role="row"><span role="rowheader">Vos coordonnées</span><span role="cell">Partagées entre entreprises</span><span role="cell">Jamais revendues</span></div>
    <div class="sp-row" role="row"><span role="rowheader">Le prix pour vous</span><span role="cell">Gratuit</span><span role="cell">Gratuit</span></div>
  </div>
</section>"""

    leak = "".join(f"<li><h3>{a}</h3><p>{b}</p></li>" for a, b in LEAK)
    leak = f"""<section class="sheet pf-leak" id="fuite-toiture" data-tone="dark">
  <div class="grid sp-head"><h2 data-split>Fuite de toiture&nbsp;? Les 5 bons réflexes</h2><p>Dans l’ordre. Ensuite, signalez-nous la fuite&nbsp;: les urgences sont rappelées en priorité.</p></div>
  <ol class="pf-howto">{leak}</ol>
  <p class="pf-mid"><a class="btn pf-pick" href="#projet" data-v="toiture" data-need="fuite"><span>Signaler une fuite</span>{tick()}</a><span class="pf-prio">Rappel prioritaire</span></p>
</section>"""

    prices = "".join(f'<li><h3>{t[8]}</h3><p>{t[9]}</p></li>' for t in TRADES)
    price = f"""<section class="sheet" id="prix" data-tone="light">
  <div class="grid sp-head"><h2 data-split>Combien vont coûter vos travaux&nbsp;?</h2><p>Un prix au mètre carré trouvé en ligne reste une moyenne. Voici ce qui fait vraiment le prix. La visite, elle, est gratuite.</p></div>
  <ul class="pf-prices">{prices}</ul>
  <p class="pf-mid"><a class="btn" href="#projet"><span>Obtenir mon devis</span>{tick()}</a></p>
</section>"""

    serious = "".join(f"<li><h3>{a}</h3><p>{b}</p></li>" for a, b in SERIOUS)
    serious = f"""<section class="sheet" id="artisan-serieux" data-tone="light">
  <div class="grid sp-head"><h2 data-split>Reconnaître un artisan sérieux</h2><p>Cinq points à vérifier avant de signer. Avec nous ou sans nous.</p></div>
  <ul class="pf-checks">{serious}</ul>
</section>"""

    rows = "\n".join(f'      <details class="fq"><summary><span>{q}</span><i class="fq-icon" aria-hidden="true"></i></summary><div class="fq-a"><p>{a}</p></div></details>' for q, a in FAQ)
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
    <h2 data-split>Votre maison mérite le bon artisan.</h2>
    <div><p>Une minute pour décrire vos travaux. Un appel pour tout vérifier. Un artisan de votre secteur.</p><a class="btn pf-btn-inv" href="#projet"><span>Décrire mes travaux</span>{tick()}</a></div>
  </div>
</section>
<a class="pf-sticky" href="#projet">Décrire mes travaux<span>1 min · gratuit</span></a>"""

    return "\n\n".join([hero, trades, steps, compare, leak, price, serious, brief, faq, end])


def schema(SITE, faq_ld, bc_ld):
    import re
    clean = lambda t: re.sub("<[^>]+>", "", t).replace("&amp;", "&")
    return {"@context": "https://schema.org", "@graph": [
        {"@type": "WebPage", "@id": SITE + PATH, "url": SITE + PATH, "name": TITLE, "description": DESC, "inLanguage": "fr-FR",
         "dateModified": UPDATED + "T09:00:00+01:00", "isPartOf": {"@id": SITE + "/#website"}, "publisher": {"@id": SITE + "/#org"},
         "about": [{"@type": "Thing", "name": n} for n in ["Devis toiture", "Ravalement de façade", "Fenêtres", "Charpente", "Isolation des combles"]]},
        {"@type": "Service", "name": "Mise en relation avec un artisan du bâtiment", "serviceType": "Devis de travaux : toiture, façade, fenêtres, charpente, isolation",
         "description": clean(BRIEF[0][1]), "areaServed": {"@type": "Country", "name": "France"},
         "audience": {"@type": "Audience", "audienceType": "Propriétaires de maison"}, "url": SITE + PATH,
         "provider": {"@type": "Organization", "@id": SITE + "/#org", "name": "Bartier & Co", "url": SITE + "/"},
         "hoursAvailable": {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], "opens": "08:00", "closes": "19:00"},
         "offers": {"@type": "Offer", "price": "0", "priceCurrency": "EUR", "description": "Gratuit pour le particulier, sans engagement"},
         "hasOfferCatalog": {"@type": "OfferCatalog", "name": "Travaux", "itemListElement": [{"@type": "Offer", "itemOffered": {"@type": "Service", "name": t[5], "description": clean(t[6])}} for t in TRADES]}},
        {"@type": "HowTo", "name": "Fuite de toiture : que faire en urgence", "step": [{"@type": "HowToStep", "position": i, "name": a, "text": clean(b)} for i, (a, b) in enumerate(LEAK, 1)]},
        faq_ld(FAQ), bc_ld(("Devis travaux", PATH))]}


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
.pf-back{border:0;background:none;color:var(--ink);font:inherit;cursor:pointer;padding:.3rem 0}
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
.pf-small{margin-top:10px;text-align:center;font-size:.8rem;color:var(--muted)}
.pf-ok{display:inline-grid;place-items:center;width:52px;height:52px;border-radius:50%;background:var(--accent);color:#fff}
.pf-ok svg{width:26px;height:26px}
.pf-done-h{margin-top:14px;font:400 1.8rem/1.1 var(--f-display);letter-spacing:-.02em}
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
.pf-trade img{width:100%;height:100%;object-fit:cover;filter:grayscale(1) contrast(1.05)}
.pf-trade h3{font:400 1.35rem/1.15 var(--f-display);letter-spacing:-.02em}
.pf-trade p{font-size:.92rem;line-height:1.45;color:var(--muted);flex:1}
.pf-pick.link{align-self:flex-start;font-size:.92rem;white-space:normal}
.pf-howto,.pf-checks,.pf-prices{display:grid;grid-template-columns:repeat(5,minmax(0,1fr));gap:20px;margin:0;padding:0 var(--cell);list-style:none;counter-reset:pf}
.pf-howto li,.pf-checks li,.pf-prices li{min-width:0;padding-top:14px;border-top:2px solid currentColor}
.pf-howto li{counter-increment:pf}
.pf-howto li::before{content:counter(pf,decimal-leading-zero);display:block;margin-bottom:10px;font:300 2rem/1 var(--f-display);color:var(--accent)}
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
.pf-sticky{position:fixed;left:14px;right:78px;bottom:14px;z-index:89;display:none;flex-direction:column;justify-content:center;min-height:52px;padding:6px 18px;border-radius:var(--r);background:var(--accent);color:#fff;font-weight:500;text-decoration:none;box-shadow:0 14px 30px -12px rgba(45,91,227,.6);transform:translateY(140%);transition:transform .35s var(--ease)}
.pf-sticky span{font-size:.75rem;font-weight:400;opacity:.85}
.pf-sticky.is-on{transform:none}
@media (max-width:1024px){.pf-trades,.pf-prices,.pf-howto,.pf-checks{grid-template-columns:repeat(2,minmax(0,1fr))}.pf-dl{grid-column:1 / -1}.pf-brief h2{grid-column:1 / -1}}
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
}
</style>"""

JS = r"""<script>
(function(){
var NEEDS=__NEEDS__, WHO=__WHO__, LABEL=__LABEL__;
var f=document.querySelector(".pf-form");if(!f)return;
var steps=[].slice.call(f.querySelectorAll(".pf-step")),cur=0,n=f.querySelector(".pf-n"),bar=f.querySelector(".pf-bar i"),back=f.querySelector(".pf-back");
var dl=function(e,p){(window.dataLayer=window.dataLayer||[]).push(Object.assign({event:e},p||{}))};
function val(k){var e=f.querySelector("[name="+k+"]");return e?(e.value||"").trim():""}
function set(k,v){f.querySelector("[name="+k+"]").value=v}
function show(i){steps.forEach(function(s,j){s.classList.toggle("is-on",j===i)});cur=i;n.textContent=i+1;bar.style.width=(100*(i+1)/steps.length)+"%";back.hidden=i===0;
  if(i===4){var c=f.querySelector("[name=code_postal]");if(c&&window.innerWidth>760)setTimeout(function(){c.focus()},200)}}
function fillNeeds(t){var box=f.querySelector(".pf-need"),list=NEEDS[t]||["Rénovation globale","Extension","Autre projet"];
  box.innerHTML=list.map(function(x){return "<button type=\"button\" class=\"pf-opt\" data-v=\""+x+"\">"+x+"</button>"}).join("")}
function pickTrade(t,jump){set("travaux",t);f.querySelectorAll(".pf-tile").forEach(function(b){b.classList.toggle("is-sel",b.dataset.v===t)});fillNeeds(t);
  var w=document.querySelector(".pf-who");if(w)w.textContent=WHO[t]||"artisans";if(jump)show(1)}
function pickLeak(){var o=f.querySelector(".pf-need .pf-opt");if(o){o.classList.add("is-sel");set("besoin",o.dataset.v);show(2)}}
f.addEventListener("click",function(e){var b=e.target.closest(".pf-tile,.pf-opt");if(!b||!f.contains(b))return;
  var st=b.closest(".pf-step"),inp=st.querySelector("input[type=hidden]");
  st.querySelectorAll(".pf-tile,.pf-opt").forEach(function(x){x.classList.toggle("is-sel",x===b)});
  if(b.classList.contains("pf-tile")){pickTrade(b.dataset.v,false);if(cur===0)dl("particulier_debut",{travaux:b.dataset.v})}else inp.value=b.dataset.v;
  if(inp.name==="statut"){var ten=b.dataset.v==="Locataire";st.querySelector(".pf-tenant").hidden=!ten;if(ten)return}
  setTimeout(function(){show(cur+1)},230)});
back.addEventListener("click",function(){if(cur>0)show(cur-1)});
document.querySelectorAll(".pf-pick").forEach(function(a){a.addEventListener("click",function(){pickTrade(a.dataset.v,true);if(a.dataset.need==="fuite")pickLeak()})});
var q=new URLSearchParams(location.search),t=q.get("travaux");
if(t&&(NEEDS[t]||t==="autre")){pickTrade(t,true);if(q.get("besoin")==="fuite")pickLeak()}
function nextOpen(){var d=new Date(),day=d.getDay(),h=d.getHours()+d.getMinutes()/60;
  if(day>=1&&day<=5&&h>=8&&h<19)return "";
  if(day>=1&&day<=4&&h>=19)return "demain dès 8 h";if(day>=1&&day<=5&&h<8)return "ce matin dès 8 h";return "lundi dès 8 h"}
f.addEventListener("submit",function(e){e.preventDefault();var err=f.querySelector(".pf-err"),bad=[];
  var cp=f.querySelector("[name=code_postal]"),pr=f.querySelector("[name=prenom]"),tel=f.querySelector("[name=telephone]"),ok=f.querySelector("[name=consentement]");
  [cp,pr,tel].forEach(function(x){x.removeAttribute("aria-invalid")});
  if(!/^\d{5}$/.test(cp.value.trim()))bad.push([cp,"un code postal à 5 chiffres"]);
  if(pr.value.trim().length<2)bad.push([pr,"votre prénom"]);
  if(tel.value.replace(/\D/g,"").length<10)bad.push([tel,"un numéro de téléphone"]);
  if(!ok.checked)bad.push([ok,"votre accord pour être rappelé"]);
  if(bad.length){bad.forEach(function(b){b[0].setAttribute("aria-invalid","true")});err.textContent="Il manque "+bad.map(function(b){return b[1]}).join(", ")+".";err.hidden=false;bad[0][0].focus();return}
  err.hidden=true;if(val("site_web"))return;
  var tr=LABEL[val("travaux")]||"Autre projet",msg="Bonjour, je souhaite être rappelé pour des travaux : "+tr+" ("+val("besoin")+"), "+val("delai").toLowerCase()+". "+val("statut")+", code postal "+val("code_postal")+". "+val("prenom")+", "+val("telephone")+".";
  dl("particulier_demande",{travaux:val("travaux"),besoin:val("besoin"),delai:val("delai"),statut:val("statut")});
  var done=f.querySelector(".pf-done");f.querySelector(".pf-name").textContent=", "+val("prenom");
  var w=nextOpen();f.querySelector(".pf-when").textContent=w?"Nous vous rappelons "+w+" au "+val("telephone")+".":"Nous vous rappelons dans les 5 minutes au "+val("telephone")+".";
  f.querySelector(".pf-wa").href="https://wa.me/33781018936?text="+encodeURIComponent(msg);
  steps.forEach(function(s){s.classList.remove("is-on")});f.querySelector(".pf-top").style.display="none";f.querySelector(".pf-bar").style.display="none";done.hidden=false;
  document.getElementById("projet").scrollIntoView({behavior:"smooth",block:"start"})});
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

"""Contenus de fond pour les moteurs de réponse (passe AEO du 18/11/2026).

- PILLAR : page « Comment trouver des chantiers » (requête la plus cherchée par les artisans).
- HP : fiche factuelle Habitatpresto Pro, tirée uniquement des documents publiés par Habitatpresto (consultés le 18/11/2026).
- PLUS : ajouts aux trois articles (sections, tableaux, questions-réponses visibles).

Règles : les mots des clients (pas de « lead » sauf pour citer le jargon), réponse d'abord, phrases courtes,
sources officielles, aucun chiffre présenté comme une moyenne s'il n'est qu'un exemple de calcul.
"""

SRC = {
    "gbp": ("Google, aide de la fiche d'établissement", "https://support.google.com/business/answer/7091?hl=fr"),
    "gads": ("Google Ads, mots clés à exclure", "https://support.google.com/google-ads/answer/2453972?hl=fr"),
    "meta": ("Meta, publicités à formulaire", "https://www.facebook.com/business/ads/lead-ads"),
    "cnil": ("CNIL, prospection par téléphone", "https://www.cnil.fr/fr/prospection-commerciale-par-telephone-hors-automate-dappel-quelles-sont-les-regles"),
    "l223": ("Code de la consommation, L223-1 et suivants", "https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069565/LEGISCTA000032221441/2026-08-11"),
    "devis": ("Service-Public, devis obligatoire", "https://www.service-public.fr/particuliers/vosdroits/F31144"),
    "decennale": ("Service-Public, garantie décennale", "https://www.service-public.fr/particuliers/vosdroits/F2034"),
    "hp_cgv": ("Habitatpresto Pro, conditions générales de vente", "https://www.habitatpresto.com/pro/conditions-generales-vente"),
    "hp_tarifs": ("Habitatpresto Pro, page Tarifs", "https://www.habitatpresto.com/pro/tarifs"),
    "hp_inscr": ("Habitatpresto Pro, page Inscription", "https://www.habitatpresto.com/pro/inscription"),
}


def src(*keys):
    return "Source : " + ", ".join(f'<a href="{SRC[k][1]}" target="_blank" rel="noopener">{SRC[k][0]}</a>' for k in keys) + "."


def qa_html(items):
    """Questions-réponses visibles dans un article (pas de menu dépliant)."""
    return "<h2>Questions fréquentes</h2>\n" + "\n".join(f"<h3>{q}</h3>\n<p>{a}</p>" for q, a in items)


# ——— Page de fond : comment trouver des chantiers ———
PILLAR = dict(
    path="/trouver-des-chantiers/",
    title="Comment trouver des chantiers : 8 canaux comparés",
    desc="Les 8 canaux pour trouver des chantiers quand on est artisan, comparés par coût du chantier signé : bouche-à-oreille, fiche Google, plateformes, annonces.",
    h1="Comment trouver des chantiers quand on est artisan",
    lead="Un artisan du bâtiment trouve ses chantiers par 8 canaux : le bouche-à-oreille, la fiche Google, les plateformes de devis, les apporteurs d'affaires, la sous-traitance, les annonces locales, les flyers et panneaux de chantier, et les réseaux professionnels. Le bon canal n'est pas le moins cher par demande : c'est celui dont le coût par chantier signé est le plus bas.",
    body=f"""
<h2>Les 8 canaux pour trouver des chantiers</h2>
<p>Pour comparer deux canaux, trois questions suffisent : ce que vous payez, à combien d'entreprises la même demande est proposée, et qui rappelle le propriétaire.</p>
<table>
<thead><tr><th>Canal</th><th>Ce que vous payez</th><th>Demande partagée ?</th><th>Qui rappelle</th><th>Ce qu'il faut pour que ça marche</th></tr></thead>
<tbody>
<tr><td>Bouche-à-oreille</td><td>Rien, sinon du temps</td><td>Non</td><td>Le client vous appelle</td><td>Des chantiers récents et des clients contents</td></tr>
<tr><td>Fiche Google</td><td>Rien</td><td>Non, mais le propriétaire compare plusieurs fiches</td><td>Le client vous appelle</td><td>Une fiche complète, des photos, des avis</td></tr>
<tr><td>Plateformes de devis</td><td>Un abonnement ou un prix par demande</td><td>Souvent, selon la plateforme</td><td>Vous</td><td>Rappeler très vite et relancer chaque devis</td></tr>
<tr><td>Apporteur d'affaires</td><td>Une commission sur le chantier signé</td><td>Selon le contrat</td><td>Vous, ou l'apporteur</td><td>Un contrat écrit : commission, zone, durée</td></tr>
<tr><td>Sous-traitance</td><td>Une marge plus faible</td><td>Non</td><td>L'entreprise principale</td><td>Un réseau d'entreprises générales ou d'architectes</td></tr>
<tr><td>Annonces locales (Google, Facebook, Instagram)</td><td>Le budget publicitaire et la gestion des campagnes</td><td>Non</td><td>Vous, ou votre prestataire</td><td>Une zone bien réglée, un tri au téléphone, un rappel rapide</td></tr>
<tr><td>Flyers et panneaux de chantier</td><td>L'impression et la distribution</td><td>Non</td><td>Le client vous appelle</td><td>Des chantiers en cours dans le quartier</td></tr>
<tr><td>Réseaux professionnels</td><td>Une cotisation, du temps</td><td>Non</td><td>Le client ou le prescripteur vous appelle</td><td>Une présence régulière et des recommandations</td></tr>
</tbody>
</table>
<p>Les plateformes de devis ne fonctionnent pas toutes de la même façon : lisez leurs conditions avant de signer. Exemple : <a href="/trouver-des-chantiers/habitatpresto-pro/">ce que disent les conditions d'Habitatpresto Pro</a>.</p>

<h2>Comment calculer le coût par chantier signé ?</h2>
<p>Additionnez tout ce qu'un canal vous a coûté sur une période : abonnement, publicité, commissions, impression. Divisez par le nombre de chantiers signés grâce à ce canal sur la même période.</p>
<p class="answer">Coût par chantier signé = dépenses du canal ÷ chantiers signés grâce à ce canal</p>
<p>Exemple, avec des chiffres choisis pour le calcul (ce ne sont pas des moyennes) :</p>
<table>
<thead><tr><th></th><th>Canal A</th><th>Canal B</th></tr></thead>
<tbody>
<tr><td>Dépenses du mois</td><td>400 €</td><td>900 €</td></tr>
<tr><td>Demandes reçues</td><td>40, soit 10 € la demande</td><td>12, soit 75 € la demande</td></tr>
<tr><td>Chantiers signés</td><td>2</td><td>6</td></tr>
<tr><td>Coût par chantier signé</td><td>200 €</td><td>150 €</td></tr>
</tbody>
</table>
<p>La demande la moins chère ne donne pas le chantier le moins cher. Comptez aussi votre temps : les appels, les visites qui ne donnent rien, les devis jamais signés. Le <a href="/lexique/#taux-de-signature">taux de signature</a> de vos devis complète le calcul.</p>

<h2>Quels canaux sont gratuits ?</h2>
<p>Le bouche-à-oreille, la fiche Google, le panneau de chantier et les prescripteurs ne coûtent presque rien en argent. Ils coûtent du temps, et ils mettent des mois à donner un flux régulier.</p>
<ul>
<li><b>Fiche Google</b> : renseignez votre métier, votre zone, vos horaires et des photos, puis demandez un avis après chaque chantier. Google classe les fiches locales selon trois critères : la pertinence, la distance et la notoriété.</li>
<li><b>Panneau de chantier</b> : votre nom, votre métier et votre numéro, lisibles depuis la rue.</li>
<li><b>Voisinage</b> : un mot dans les boîtes aux lettres des rues voisines, avant et pendant le chantier.</li>
<li><b>Prescripteurs</b> : architectes, maîtres d'œuvre, autres corps de métier, fournisseurs.</li>
</ul>
<p class="src">{src("gbp")}</p>

<h2>Quel canal choisir selon votre métier ?</h2>
<table>
<thead><tr><th>Métier</th><th>Ce que cherchent les propriétaires</th><th>Canaux qui conviennent</th></tr></thead>
<tbody>
<tr><td><a href="/metiers/couverture/">Couverture</a></td><td>Urgences (fuite, tuiles) et réfections</td><td>Google pour les urgences, Facebook et Instagram pour la réfection, panneau de chantier</td></tr>
<tr><td><a href="/metiers/facade/">Façade</a></td><td>Ravalements, souvent repoussés</td><td>Facebook et Instagram, flyers dans les rues voisines</td></tr>
<tr><td><a href="/metiers/menuiserie-exterieure/">Menuiserie extérieure</a></td><td>Remplacement de fenêtres et de portes</td><td>Facebook et Instagram, fiche Google, fournisseurs</td></tr>
<tr><td><a href="/metiers/charpente/">Charpente</a></td><td>Projets liés à la toiture ou à une extension</td><td>Prescripteurs (couvreurs, architectes), Google</td></tr>
<tr><td><a href="/metiers/isolation/">Isolation</a></td><td>Projets souvent liés aux aides</td><td>Annonces locales, en respectant les règles propres à la rénovation énergétique</td></tr>
</tbody>
</table>
<p>Pour aller plus loin : <a href="/blog/google-ads-ou-meta-ads-artisan/">Google Ads ou Meta Ads : qui capte quelle demande</a>.</p>

<h2>Où se perdent les chantiers après la demande ?</h2>
<ol>
<li><b>Le rappel tardif</b> : une demande rappelée le soir a pu parler entre-temps à un concurrent.</li>
<li><b>La visite inutile</b> : un locataire, un projet pour dans trois ans, une commune hors zone. Quelques questions au téléphone l'évitent.</li>
<li><b>Le devis envoyé tard</b> : plus il arrive tard, plus le propriétaire a reçu d'autres devis.</li>
<li><b>Le devis jamais relancé</b> : un appel et un SMS suffisent souvent. Voir <a href="/blog/relance-devis-artisan/">la relance de devis</a>.</li>
</ol>

<h2>Ce que la loi interdit depuis 2026</h2>
<p>Depuis le 11 août 2026, appeler un particulier pour lui proposer des travaux demande son accord préalable, sauf contrat en cours. Pour la rénovation énergétique, la prospection par téléphone est interdite. Rappeler un propriétaire qui vous a lui-même demandé d'être contacté reste possible, si vous gardez la preuve de sa demande.</p>
<p class="src">{src("cnil", "l223")} Définition dans notre <a href="/lexique/#demarchage-telephonique">lexique</a>.</p>

<h2>Notre approche, et ses limites</h2>
<p>Bartier & Co combine deux canaux de cette liste, les annonces locales sur Google et sur Facebook et Instagram, avec l'étape où se perdent le plus de chantiers : le rappel. Chaque demande est rappelée en moins de 5 minutes en semaine, vérifiée, puis la visite est fixée dans votre agenda. Un seul artisan par métier et par secteur.</p>
<p>Ce n'est pas un remplacement du bouche-à-oreille : c'est un flux en plus, sans durée d'engagement. <a href="/#process">Voir comment ça marche</a>.</p>
""",
    faq=[
        ("Quel est le meilleur site pour trouver des chantiers ?", "Aucun site n'est le meilleur pour tous les artisans. Comparez trois points : à combien d'entreprises la même demande est proposée, qui rappelle le propriétaire, et combien vous coûte un chantier signé."),
        ("Comment trouver des chantiers gratuitement ?", "Par le bouche-à-oreille, une fiche Google complète avec des avis, un panneau sur chaque chantier et des prescripteurs comme les architectes. C'est gratuit en argent, mais cela demande du temps et plusieurs mois."),
        ("Comment trouver des chantiers chez les particuliers ?", "Visez les propriétaires de votre secteur : la fiche Google et les annonces Google pour ceux qui cherchent déjà, les annonces Facebook et Instagram et les flyers pour ceux qui y pensent. Depuis août 2026, ne les appelez que s'ils l'ont demandé."),
        ("Faut-il payer pour avoir des chantiers ?", "Non, mais les canaux gratuits sont lents. Payer a du sens quand le coût par chantier signé reste nettement inférieur à votre marge sur le chantier."),
        ("Combien de temps faut-il pour remplir son agenda ?", "Cela dépend du canal, du métier et de la saison. Le bouche-à-oreille et la fiche Google demandent des mois. Des annonces locales donnent des demandes dès qu'elles tournent, à condition de les rappeler vite."),
        ("Les plateformes de devis valent-elles le coup ?", "Cela dépend de leurs conditions. Avant de signer, demandez à combien d'artisans chaque demande est envoyée, la durée d'engagement, le prix réel et ce qui se passe pour une demande non valable."),
    ],
)


# ——— Fiche factuelle : Habitatpresto Pro ———
HP = dict(
    path="/trouver-des-chantiers/habitatpresto-pro/",
    title="Habitatpresto Pro : abonnement, engagement et demandes",
    desc="Habitatpresto Pro côté artisan, d'après ses conditions publiées : abonnement mensuel, engagement de 6 ou 12 mois, demandes envoyées à 5 professionnels.",
    h1="Habitatpresto Pro : ce que disent ses conditions, côté artisan",
    lead="Habitatpresto Pro fonctionne par abonnement mensuel, avec des frais de mise en service. Le prix n'est pas publié : il dépend des départements et des catégories choisis. L'engagement initial est de 6 ou 12 mois, et chaque demande de devis est d'abord envoyée à 5 professionnels, puis à 5 autres.",
    body=f"""
<p>Cette fiche résume les documents publiés par Habitatpresto, consultés le 18 novembre 2026. Elle ne donne pas d'avis. Si une information a changé, <a href="mailto:contact@bartierandco.com">écrivez-nous</a> : nous corrigeons.</p>

<h2>Comment fonctionne Habitatpresto Pro ?</h2>
<table>
<thead><tr><th>Point</th><th>Ce qu'indique Habitatpresto</th><th>Où</th></tr></thead>
<tbody>
<tr><td>Modèle</td><td>« une cotisation mensuelle et des frais de mise en service lors de la souscription »</td><td>Conditions générales de vente</td></tr>
<tr><td>Coût par chantier</td><td>« Aucun coût par chantier, vous ne payez rien de plus que votre abonnement. »</td><td>Page Inscription</td></tr>
<tr><td>Prix</td><td>Non publié : « Le prix dépend des départements et des catégories souhaitées »</td><td>Page Tarifs</td></tr>
<tr><td>Durée d'engagement</td><td>« 6 (six) ou 12 (douze) Périodes Mensuelles », puis renouvellement pour une durée indéterminée</td><td>Conditions générales, article 5</td></tr>
<tr><td>Arrêt avant la fin</td><td>Pas de résiliation avant la fin de l'engagement initial. Habitatpresto peut l'accepter contre des frais de gestion de 50 % de l'abonnement restant à payer, et au moins 100 €</td><td>Conditions générales, article 6</td></tr>
<tr><td>Prix après l'engagement</td><td>« HABITATPRESTO est libre de modifier ses tarifs »</td><td>Conditions générales, article 6</td></tr>
<tr><td>Professionnels par demande</td><td>Chaque demande est envoyée « dans un premier temps à cinq Membres, puis dans un second temps à cinq autres Membres » ; les coordonnées sont communiquées à cinq membres</td><td>Conditions générales, article 9</td></tr>
<tr><td>Vérification des projets</td><td>« Seuls les projets validés par nos équipes vous parviennent ». La méthode n'est pas décrite</td><td>Page Tarifs</td></tr>
<tr><td>Horaires d'envoi</td><td>Les demandes sont envoyées entre 8 h et 20 h</td><td>Conditions générales, article 9</td></tr>
<tr><td>Délai de contact</td><td>Les membres s'engagent à contacter le demandeur dans les 48 heures suivant l'acceptation de la demande</td><td>Conditions générales, article 9</td></tr>
</tbody>
</table>
<p class="src">{src("hp_cgv", "hp_tarifs", "hp_inscr")}</p>

<h2>Ce qui n'est pas publié</h2>
<ul>
<li>Le montant de l'abonnement et des frais de mise en service : il faut demander une estimation.</li>
<li>La méthode de vérification des projets.</li>
<li>Une règle de remboursement des demandes non valables : nous n'en avons pas trouvé dans les pages consultées.</li>
</ul>

<h2>Comment calculer votre coût par chantier signé avec un abonnement ?</h2>
<p>Avec un abonnement fixe, le coût par chantier signé dépend surtout du nombre de chantiers que vous signez chaque mois.</p>
<p class="answer">Coût par chantier signé = (abonnement mensuel + part des frais de mise en service) ÷ chantiers signés dans le mois</p>
<p>Comme une même demande peut être proposée à plusieurs professionnels, la rapidité de votre rappel et la qualité de votre devis comptent beaucoup. Notez vos chiffres réels pendant les premiers mois : demandes reçues, visites, devis envoyés, chantiers signés.</p>

<h2>Les questions à poser avant de signer</h2>
<ol>
<li>Quel est le prix exact pour mes métiers et mes départements, frais de mise en service compris ?</li>
<li>Combien de professionnels recevront la même demande, dans mon secteur ?</li>
<li>Combien de demandes ont été reçues ces derniers mois, dans ma zone et pour mon métier ?</li>
<li>Que se passe-t-il pour une demande non valable : faux numéro, locataire, hors zone ?</li>
<li>Quelle durée d'engagement est inscrite sur le bon de commande, et à quelle date dois-je résilier ?</li>
</ol>

<h2>Une autre approche</h2>
<p>Si vous préférez recevoir des visites déjà fixées, réservées à un seul artisan par métier et par secteur, sans durée d'engagement, voyez <a href="/#process">comment travaille Bartier & Co</a>. Pour comparer tous les canaux : <a href="/trouver-des-chantiers/">comment trouver des chantiers</a>.</p>
""",
    faq=[
        ("Combien coûte Habitatpresto Pro ?", "Le prix n'est pas publié. Selon Habitatpresto, il dépend des départements et des catégories choisis, et des frais de mise en service s'ajoutent à l'abonnement mensuel."),
        ("Peut-on résilier Habitatpresto Pro à tout moment ?", "Pas pendant l'engagement initial de 6 ou 12 mois, selon les conditions générales. Habitatpresto peut accepter un arrêt anticipé contre des frais de 50 % de l'abonnement restant, au moins 100 €."),
        ("Combien d'artisans reçoivent la même demande sur Habitatpresto ?", "Selon les conditions générales, chaque demande est d'abord envoyée à 5 professionnels, puis à 5 autres, et les coordonnées du particulier sont communiquées à 5 professionnels."),
    ],
)


# ——— Ajouts aux articles : (texte inséré avant ce marqueur, texte ajouté à la fin, questions-réponses) ———
PLUS = {
    "lead-partage-lead-exclusif-rendez-vous-qualifie": dict(
        before="<h2>Les questions à poser avant de signer</h2>",
        insert=f"""<h2>Combien coûte vraiment une demande ?</h2>
<p>Le prix affiché d'une demande ne dit pas grand-chose. Ce qui compte, c'est le <a href="/lexique/#cout-par-chantier-signe">coût par chantier signé</a> : le prix des demandes divisé par le nombre de chantiers qu'elles vous ont fait signer.</p>
<p>Exemple, avec des chiffres choisis pour le calcul (ce ne sont pas des moyennes) :</p>
<table>
<thead><tr><th></th><th>Demandes partagées</th><th>Demandes exclusives</th></tr></thead>
<tbody>
<tr><td>Prix d'une demande</td><td>25 €</td><td>60 €</td></tr>
<tr><td>Demandes achetées</td><td>20, soit 500 €</td><td>10, soit 600 €</td></tr>
<tr><td>Chantiers signés</td><td>1</td><td>2</td></tr>
<tr><td>Coût par chantier signé</td><td>500 €</td><td>300 €</td></tr>
</tbody>
</table>
<p>Ajoutez votre temps : chaque demande se rappelle, et chaque visite inutile coûte une demi-journée.</p>

<h2>Que vérifier dans le contrat ?</h2>
<ul>
<li>La durée d'engagement, et les frais si vous arrêtez avant la fin.</li>
<li>La zone couverte, et la durée de l'exclusivité si elle est promise.</li>
<li>Ce qui se passe pour une demande non valable : faux numéro, locataire, hors zone.</li>
<li>Le prix après la première période.</li>
<li>La preuve que le particulier a demandé à être rappelé au sujet de son projet.</li>
</ul>

<h2>Depuis 2026, l'accord du particulier compte</h2>
<p>Depuis le 11 août 2026, appeler un particulier pour lui proposer des travaux demande son accord préalable. Avant d'acheter des demandes, vérifiez que chaque particulier a bien demandé à être rappelé au sujet de son projet, et que le vendeur peut le prouver. Sans cet accord, l'appel peut être considéré comme du démarchage interdit.</p>
<p class="src">{src("cnil", "l223")}</p>

""",
        append="",
        faq=[
            ("Qu'est-ce qu'un lead dans le bâtiment ?", "C'est le mot des plateformes pour une demande de devis : les coordonnées d'un particulier qui envisage des travaux. Il reste à le rappeler, à vérifier son projet et à fixer une visite."),
            ("Une demande exclusive coûte-t-elle plus cher ?", "Elle coûte en général plus cher à l'achat, mais elle peut revenir moins cher par chantier signé, puisque vous n'êtes pas en concurrence sur le même appel. Faites le calcul avec vos propres chiffres."),
            ("Comment savoir si une demande est sérieuse ?", "Posez cinq questions au premier appel : êtes-vous propriétaire, quels travaux, quelle commune, pour quand, avez-vous déjà des devis ? Les réponses suffisent à trier."),
        ],
    ),
    "google-ads-ou-meta-ads-artisan": dict(
        before="<h2>Google Ads ou Meta Ads : notre choix, et ses limites</h2>",
        insert=f"""<h2>Google Ads ou Meta Ads : le tableau</h2>
<table>
<thead><tr><th></th><th>Google Ads</th><th>Meta Ads (Facebook, Instagram)</th></tr></thead>
<tbody>
<tr><td>La demande</td><td>Exprimée : le propriétaire cherche</td><td>Suscitée : il n'a pas encore cherché</td></tr>
<tr><td>Typiquement</td><td>Urgences, projets mûrs</td><td>Rénovation, entretien, projets à venir</td></tr>
<tr><td>Le ciblage</td><td>Les recherches, dans vos communes</td><td>Un rayon autour de votre dépôt</td></tr>
<tr><td>Le point clé</td><td>Écarter les recherches inutiles</td><td>Trier les demandes au téléphone</td></tr>
<tr><td>Ce qui convainc</td><td>Répondre vite</td><td>Vos vraies photos de chantier</td></tr>
</tbody>
</table>

<h2>Combien de budget prévoir pour commencer ?</h2>
<p>Il n'existe pas de bon chiffre pour tous : le prix d'un clic dépend du métier, de la ville et de la saison. Partez de votre objectif : combien de chantiers voulez-vous signer par mois, et combien êtes-vous prêt à payer pour chacun ?</p>
<p class="answer">Budget de départ ≈ chantiers visés par mois × coût acceptable par chantier signé</p>
<p>Exemple pour le calcul : pour 2 chantiers par mois, à 400 € au plus chacun, le budget de départ est d'environ 800 € par mois. Ajustez-le après quelques semaines, selon les demandes réelles.</p>

<h2>Les erreurs qui coûtent le plus cher</h2>
<ul>
<li><b>Aucun mot exclu sur Google</b> : sans liste de mots à exclure (gratuit, emploi, formation, bricolage), vous payez des clics qui ne deviendront jamais des chantiers.</li>
<li><b>Un rayon trop large</b> : des demandes à une heure de route, que vous refuserez.</li>
<li><b>Un formulaire sans question</b> : sur Facebook et Instagram, ajoutez des questions de tri (propriétaire, travaux, commune).</li>
<li><b>Un rappel le lendemain</b> : la demande a refroidi, ou un concurrent a rappelé avant vous.</li>
<li><b>Des comptes au nom du prestataire</b> : si vous arrêtez, vous perdez l'historique. Exigez des comptes à votre nom.</li>
</ul>
<p class="src">{src("gads", "meta")}</p>

""",
        append="",
        faq=[
            ("Google Ads ou Meta Ads pour un couvreur ?", "Souvent les deux : Google pour les urgences comme une fuite, Facebook et Instagram pour la réfection, que le propriétaire repousse. Commencez par celui qui correspond aux chantiers que vous voulez."),
            ("Faut-il un site internet pour faire de la publicité ?", "Pas forcément un site complet. Pour Google, une page rapide sur mobile, à votre nom, suffit. Sur Facebook et Instagram, le formulaire peut rester dans l'application."),
            ("Qui doit posséder les comptes publicitaires ?", "Vous. Les comptes Google Ads et Meta doivent être à votre nom, payés directement par votre entreprise, pour garder l'historique si vous changez de prestataire."),
        ],
    ),
    "relance-devis-artisan": dict(
        before="<h2>Quand arrêter de relancer un devis ?</h2>",
        insert=f"""<h2>Que répondre quand le devis est jugé trop cher ?</h2>
<ol>
<li><b>Demandez à quoi il est comparé</b> : un autre devis, un budget, un prix vu en ligne.</li>
<li><b>Comparez poste par poste</b> : matériaux, surface, échafaudage, évacuation des déchets, garanties.</li>
<li><b>Proposez une option, pas une remise</b> : un autre matériau, une partie des travaux plus tard.</li>
<li><b>Rappelez ce qui est inclus</b> : la visite, la garantie décennale, le délai.</li>
</ol>

<h2>Un devis qui aide à signer</h2>
<p>Un devis clair se relance plus facilement. Il détaille les travaux poste par poste, les matériaux, le prix hors taxes et toutes taxes comprises, la durée de validité, le délai d'exécution, et le nom de votre assurance décennale.</p>
<p class="src">{src("devis", "decennale")}</p>

<h2>Un modèle de relance par e-mail</h2>
<blockquote>Objet : votre devis de toiture<br>Bonjour Madame Durand, je reviens vers vous au sujet du devis envoyé le 4 mars pour la réfection de votre toiture. Avez-vous des questions sur les matériaux ou le délai ? Je peux vous rappeler à l'heure qui vous arrange. Bien cordialement, Julien, Martin Couverture.</blockquote>
<p>Comme pour les SMS, les noms sont des exemples.</p>

""",
        append="""
<h2>Le tableau de suivi des devis</h2>
<table>
<thead><tr><th>Client</th><th>Devis envoyé le</th><th>Montant</th><th>Relances</th><th>Statut</th><th>Si perdu, pourquoi</th></tr></thead>
<tbody>
<tr><td>Exemple : M. et Mme Durand</td><td>4 mars</td><td>14 800 €</td><td>SMS, appel, SMS</td><td>Signé</td><td></td></tr>
<tr><td>Exemple : M. Petit</td><td>11 mars</td><td>6 200 €</td><td>SMS, appel</td><td>Perdu</td><td>Prix, autre devis</td></tr>
</tbody>
</table>
<p>Au bout de quelques mois, la dernière colonne vous dit où partent vos chantiers.</p>
""",
        faq=[
            ("Combien de fois faut-il relancer un devis ?", "Trois fois au plus : un SMS le jour de l'envoi, un appel quelques jours après, puis un dernier message deux à trois semaines plus tard."),
            ("Faut-il relancer par téléphone ou par SMS ?", "Les deux. L'appel sert à répondre aux questions, le SMS à ne pas déranger. Commencez par confirmer la réception du devis par SMS le jour même."),
            ("Comment savoir si mes relances fonctionnent ?", "Suivez votre taux de signature (devis signés ÷ devis envoyés × 100) avant et après avoir mis en place les relances, sur plusieurs mois."),
        ],
    ),
}

# Reverse engineering de callead.fr

Analyse réalisée le 17 novembre 2026 à partir des pages publiques du site (accueil, page sectorielle « menuiseries extérieures », page « isolation », étude de cas Isol'R, prise de rendez-vous, « qui sommes-nous », formulaire de contact, sitemaps). Objectif : reprendre ce qui fonctionne, l'adapter aux seuls artisans du bâtiment à gros chantiers, et ne pas reprendre ce que nous ne pouvons pas assumer.

## 1. Positionnement

- Agence de génération de leads multi-secteurs, active depuis 2020 : Google Ads, Meta Ads, TikTok, création de landing pages.
- Elle se présente comme le mélange « d'une agence sur mesure et d'un fournisseur de leads ».
- Elle couvre dix secteurs très différents : courtage immobilier, PER, SCPI, formation CPF, B2B, menuiseries extérieures, traitement de l'humidité, photovoltaïque, pompe à chaleur, isolation.
- Promesse d'accueil : « Boostez votre croissance avec des leads hautement qualifiés ». C'est le lexique marketing classique (booster, propulser, leads).
- Ce qu'elle vend : des leads, c'est-à-dire des formulaires remplis. Le rappel du prospect reste à la charge du client.

**Ce que cela nous laisse** : une agence généraliste parle à tout le monde. Nous ne parlons qu'aux artisans à gros chantiers, et nous vendons des rendez-vous, pas des leads.

## 2. Architecture du site

| Type de page | Exemples | Rôle |
|---|---|---|
| Accueil | `/` | Promesse, logos, choix du secteur, méthode, chiffres, témoignages |
| Pages secteur (10) | `/secteur-activite/menuiseries-exterieures/` | Pages d'atterrissage par métier, pour le référencement et les campagnes |
| Hub des secteurs | `/tous-les-secteurs-dactivites/` | Index des secteurs |
| Expertises (3) | `/domaines-expertise/google/`, `facebook-instagram/`, `site-internet/` | Pages par canal |
| Études de cas (11) | `/succes-clients/isolr-menuiserie-exterieure/` | Un témoignage et trois indicateurs chiffrés |
| Prise de rendez-vous | `/prendre-rendez-vous/` | Agenda Calendly en pleine page (30 minutes) |
| Contact | `/contact/` | Formulaire long |
| À propos | `/qui-sommes-nous/` | Équipe par pôle, avec prénoms et rôles |
| Recrutement, pages légales | `/on-recrute/`, mentions, confidentialité | |

Le menu principal met « Votre secteur d'activité » en premier, avec un menu déroulant. Le visiteur se range lui-même dans un secteur dès le premier clic.

## 3. Le gabarit des pages secteur (le cœur du site)

Les pages secteur suivent toutes le même ordre :

1. **Titre avec le mot-clé métier** : « Leads menuiserie extérieure : … ». Deux boutons, « Obtenir plus de clients » (contact) et « Prendre rdv » (Calendly).
2. **Les problèmes du secteur**, en trois cartes : qualité des leads, volume, transparence (leads mutualisés entre concurrents). C'est la section la plus convaincante : le visiteur se reconnaît.
3. **Pourquoi nous**, en cinq arguments : qualité, maîtrise du secteur, exclusivité, volume, sans engagement.
4. **Chiffres du secteur** : nombre de clients, leads générés, coût du lead, taux de transformation.
5. **Méthodologie en quatre étapes**, identique sur toutes les pages.
6. **Expertises** : trois cartes (Meta, Google, site).
7. **Un témoignage du secteur**, avec trois indicateurs et un lien vers l'étude de cas.
8. Bandeau d'appel à l'action, puis pied de page avec la photo et le téléphone d'un dirigeant.

Les textes des sections 5 et 6 sont identiques d'une page à l'autre ; seules les sections 1 à 4 et 7 changent. C'est un gabarit industrialisé : une nouvelle page secteur coûte peu à produire.

## 4. Parcours de conversion

- **Deux portes d'entrée sur chaque écran** : « Prendre RDV » (agenda Calendly intégré, 30 minutes avec le dirigeant) et « Nous contacter » (formulaire). Les deux boutons sont dans l'en-tête fixe.
- **Formulaire de contact** : prénom, nom, société, e-mail, téléphone, domaine, objectif, date, plus quatre champs libres. Il contient des **champs cachés** qui enregistrent `utm_source`, `utm_medium`, `utm_campaign`, `utm_content` et `gclid`. Chaque demande est donc rattachée à la campagne qui l'a produite.
- **Preuves** : « + de 300 clients », bandeau de 21 logos, « +10 M€ d'investissements publicitaires », « +1 M de leads générés », « +32 % de chiffre d'affaires en moyenne après 3 mois », témoignages avec prénom, initiale et cinq étoiles.
- **Réassurance** : « Sans engagement » répété sur chaque page, et des visages : la page équipe et la photo du dirigeant dans le pied de page.

## 5. Technique

- **Socle** : WordPress 6.9, Elementor 4.0, Yoast SEO (sitemaps par type de contenu), WP Rocket (cache, JavaScript différé, polices hébergées localement).
- **Mesure** : Google Tag Manager et gtag (Google Ads, Analytics).
- **Agenda** : Calendly en intégration inline, couleur de marque passée en paramètre.
- **Identité** : bleu nuit `#081732` et vert `#6BE88D`, linéale géométrique, illustrations en icônes 3D, fond pointillé.
- **Poids** : 470 Ko de HTML pour l'accueil, et plus de 3 000 occurrences de classes Elementor. C'est lourd et générique, mais rapide à éditer sans développeur.

## 6. Ce que nous reprenons

1. **Une page par métier**, sur un gabarit commun, avec le mot-clé métier dans le titre et l'adresse. C'est fait pour la couverture, la menuiserie extérieure, la façade, la charpente et l'isolation, plus une page d'index `/metiers/`.
2. **La section « problèmes du secteur »**, réécrite métier par métier avec ses vrais irritants : dépannages et météo pour le couvreur, mise en concurrence avec les grandes enseignes pour le menuisier, décision en couple pour le façadier, démarchage pour l'isolation.
3. **Le menu orienté métier** : « Métiers » mène à l'index ; chaque métier de l'accueil mène à sa page.
4. **L'enregistrement de la source de chaque demande** : champs cachés UTM, `gclid`, `fbclid` et page d'origine, conservés pendant la visite.
5. **Le métier présélectionné** dans le formulaire quand on arrive depuis une page métier : le formulaire démarre à la question 2.
6. **Les visages et le « sans engagement »**, déjà présents chez nous.

## 7. Ce que nous faisons mieux ou autrement

1. **Uniquement les gros chantiers.** Pas de CPF, de SCPI ni de crédit. Chaque page métier affiche aussi ce que nous **écartons** (dépannages, petits travaux, locataires) : c'est la preuve concrète du « haut de gamme ».
2. **Nous vendons des rendez-vous, pas des leads.** Chaque page métier montre les questions posées au téléphone avant de déplacer l'artisan. Callead n'en dit rien.
3. **Les annonces sont montrées** : des exemples d'angles publicitaires par métier, présentés comme tels. Cela démontre la maîtrise du métier mieux qu'un paragraphe.
4. **Aucune preuve inventée.** Callead affiche chiffres, logos et témoignages. Nous n'en avons pas encore, donc nous le disons, et chaque page réserve la place des futures études de cas avec des chiffres réels. Nous ne reprenons pas les formulations de type « +32 % de chiffre d'affaires en moyenne » sans preuve publiable.
5. **Une garantie écrite**, absente chez Callead.
6. **Un formulaire court et progressif** (4 questions, puis les coordonnées), plutôt qu'un formulaire de dix champs.
7. **Un site léger et rapide** : HTML et CSS faits main, polices auto-hébergées, aucune dépendance externe.
8. **Une identité distincte** : écru, bleu de travail et typographie éditoriale, à l'opposé du bleu nuit et vert « startup » utilisé par la plupart des agences.

## 8. Reste à faire, d'après cette analyse

- **Études de cas** : un gabarit `/resultats/<entreprise>/` (témoignage réel, trois indicateurs, métier, zone), à publier dès le premier client.
- **Prise de rendez-vous directe** : un agenda (Cal.com ou Calendly) en plus du formulaire, comme second bouton, quand vous serez prêts à l'ouvrir.
- **Pages par canal** (« Publicité Facebook pour couvreurs », etc.) et articles de blog reliés aux pages métiers, d'après la recherche de mots-clés.
- **Téléphone et photo d'un fondateur** dans le pied de page, dès que les portraits seront disponibles.

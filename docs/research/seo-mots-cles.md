# Mots-clés de la cible et architecture SEO

Recherche du 17 novembre 2026. Cible : gérants d'entreprises artisanales du bâtiment (couverture-zinguerie et façade d'abord), France et Belgique francophone. Le français fait référence, l'anglais est un miroir. Le corps du rapport tient dans les sections 1 à 9 ; l'annexe détaille les 20 briefs.

Fichiers : `seo-requetes.csv` (1 475 requêtes réelles dédoublonnées : 959 en France, 136 en Belgique, 238 communes aux deux, 142 en anglais) et `seo-briefs-articles.csv` (les briefs au format tableur, avec requêtes secondaires).

## 1. Ce qu'il faut retenir

1. **L'artisan cherche « des chantiers », pas des « leads ».** Le préfixe « trouver des chantiers » suivi de chaque lettre donne 95 complétions, en France comme en Belgique ; « rendez-vous qualifiés » en donne 4. Par gabarit : « rendez-vous qualifiés + activité » 0 réponse sur 24 essais, « agence marketing + métier » 1 sur 24, « trouver des chantiers + activité » 12 sur 25.
2. **Les deux métiers de lancement ont peu de requêtes propres** : 10 pour couverture et toiture, 1 pour façade, aucune pour zinguerie, ravalement ou charpente. La demande porte sur le générique et sur les marques de plateformes.
3. **Marques** : 208 requêtes sur les plateformes françaises, dont 44 sur Habitatpresto (« pro avis », « pro tarif », « arnaque », « supprimer compte ») et 27 requêtes d'évaluation sur Travaux.com (« tarif artisan », « prix du contact », « resiliation ») ; 56 sur les belges. Les résultats y sont tenus par des sites d'avis et des forums.
4. **« Gratuit »** revient dans 16 requêtes du cœur de cible.
5. **Sur « trouver des chantiers »**, les résultats appartiennent à des néobanques, des éditeurs de logiciels et aux plateformes, sous forme de listes mises à jour en 2025-2026. Aucune agence n'y figure.
6. **Réglementation** : depuis le 11 août 2026, le démarchage téléphonique des consommateurs est interdit sauf consentement préalable ou contrat en cours, et Bloctel a cessé d'exister. Sujet de recherche actif, et point de conformité pour le formulaire et le rappel en moins de 5 minutes.
7. **Google Trends est resté bloqué** : aucune donnée de saisonnalité.

## 2. Univers de requêtes

Collecte : 1 833 appels d'autocomplétion, espacés d'au moins 320 ms par file avec trois files au plus en parallèle (Google Suggest France 1 263, Belgique 340, Royaume-Uni 29 ; YouTube 40 ; DuckDuckGo 161). 7 123 suggestions brutes, 4 637 écartées par règles (hors bâtiment, villes, néerlandais, homonymes), 1 475 requêtes uniques retenues. Bing Suggest n'a rien renvoyé.

| Groupe | Nb | Exemples réels | Intention | Potentiel | Difficulté | Proximité vente | Priorité |
|---|---|---|---|---|---|---|---|
| Trouver des chantiers | 148 | trouver des chantiers btp ; recherche chantier toiture | solution | très fort | très forte | moyenne | 1 |
| Plateformes France (marques) | 208 | habitatpresto pro avis ; travaux com tarif artisan | évaluation | fort | moyenne | forte | 1 |
| Sites et applications génériques | 43 | site pour trouver des chantiers | comparaison | fort | forte | forte | 1 |
| Leads, rendez-vous qualifiés | 96 | achat leads travaux ; lead exclusif ; achat de rdv qualifiés | transaction | faible | faible | très forte | 1 |
| Plateformes Belgique (marques) | 56 | trustup pro avis ; bobex prix ; solvari avis | évaluation | moyen | faible | forte | 2 |
| Apporteur d'affaires, sous-traitance | 86 | apporteur d'affaires btp | information | fort | moyenne | moyenne | 2 |
| Démarchage : règles | 281 | démarchage téléphonique aout 2026 ; interdit b2b ; liste ne m'appelez plus | réglementaire | fort | forte en tête | moyenne | 2 |
| Conversion du devis | 80 | relance devis artisan ; taux de transformation devis | information | fort | moyenne | moyenne | 2 |
| Agence et publicité | 71 | publicité facebook prix ; google ads couvreur | mixte | moyen | moyenne | forte | 2 |
| Visibilité locale, supports | 84 | flyer couvreur ; panneau de chantier | information | moyen | faible | moyenne | 3 |
| Trouver des clients (métier) | 28 | comment trouver des clients dans le btp | information | moyen | forte | moyenne | 3 |
| Gestion de l'entreprise | 61 | carnet de commande btp ; couvreur à son compte | information | moyen | moyenne | faible | 3 |
| Particuliers (hors cible) | 91 | couvreur autour de moi ; toiturier | B2C | — | — | nulle | exclure |
| Anglais (miroir) | 142 | buy exclusive roofing leads | transaction | hors marché | — | faible | miroir |

En Belgique le vocabulaire change : « toiturier », « entrepreneur », « ne m'appelez plus ».

## 3. Google Trends

Tentative 1 (Chromium piloté par Playwright, configuration par défaut) : la page d'accueil se charge, la page « Explorer » répond 429 dès la première comparaison. Tentative 2 (passage par le champ de recherche de l'accueil) : non aboutie, puis relance refusée par la politique d'autorisation de la session. Pas de troisième tentative. **Aucun indice ni saisonnalité n'a été obtenu, et rien n'est extrapolé.** Rappel : Trends fournit un indice relatif de 0 à 100, jamais un volume.

## 4. Pages de résultats (approximation)

Seul l'outil WebSearch (index américain) a répondu. DuckDuckGo HTML (captcha), Bing en ligne de commande (résultats sans rapport), Brave (429), Mojeek (403), Qwant (403) et Startpage (défi JavaScript) étaient inutilisables. Le tableau approche Google France et Belgique sans le reproduire.

| Requête testée | Qui se positionne | Type et angle | Lecture |
|---|---|---|---|
| trouver des chantiers artisan | Shine, Pro by Crédit Agricole, Qonto, Legalnest, Effy, Habitatpresto Pro | listes « N sites, N méthodes », 2025-2026 | très concurrentiel, aucune agence |
| meilleur site pour trouver des chantiers | Qonto, Shine, Obat, Keobiz, Legalnest | comparatifs de banques et de logiciels | angle libre : le partage de la demande |
| trouver des clients couvreur | Habitatpresto Pro (« 17 astuces », 20/05/2026), puis pages pour particuliers | un seul guide dédié | peu de concurrence B2B |
| trouver des chantiers de façade | Ootravaux, Travaux.com, PagesJaunes | annuaires | aucun guide façadier |
| leads couvreur toiture exclusifs | Effy, puis sites américains | presque rien en français | créneau vide, demande mince |
| acheter des leads travaux BTP | Obat, Habitatpresto Pro, Effy, publi-rédactionnels helloLeads sur Batiweb | pages vendeuses | concurrence commerciale directe |
| rendez-vous qualifiés artisan BTP | FFB, CAPEB, Batirama | hors sujet | pas de page de résultats établie |
| agence marketing BTP artisans | La Fabrique du Net, podcast BTP Engagé, Habitatpresto Pro | annuaire, podcast | pas d'agence spécialisée en tête |
| publicité Facebook artisan bâtiment | artisanatpaysdelaloire.fr et CAPEB (formations), Obat, FFB, Shopify | formations, guides génériques | angle libre : l'après-clic |
| habitatpresto pro avis ; travaux.com avis artisan | Custplace, Signal-Arnaques, forum Que Choisir, Gowork, Trustpilot | avis, forums | fiche factuelle possible |
| apporteur d'affaires BTP | LegalVision, Captain Contrat, Effy, Obat | guides juridiques | moyenne |
| démarchage téléphonique interdit août 2026 | economie.gouv.fr, Service Public, Selectra | sources officielles, juillet-août 2026 | tête imprenable, viser « artisan » |
| relance devis artisan | Effy, Abby, Sellsy, ComeUp | éditeurs de logiciels | moyenne |
| trouver des chantiers Belgique ; leads toiture Belgique | Bobex, blog TrustUp, Buildwise et Embuild (PDF) | plateformes, peu de guides | faible à moyenne |

« Solvari avis entrepreneur » n'a renvoyé aucun résultat pertinent. TrustUp publie aussi un guide belge « 30 méthodes » (mis à jour le 22/06/2026). Pages ouvertes : Pro by Crédit Agricole (05/11/2025, mise à jour le 22/12/2025, boutons « résumer avec ChatGPT, Claude, Perplexity, Mistral ») ; Shine (29/06/2023, auteur et relecteur nommés) ; Obat (02/12/2019, mise à jour le 09/06/2026) ; Legalnest (page mère, tableau de prix, une fiche par plateforme). Obat écrit que « les demandes de devis sont diffusées à un large nombre d'entreprises simultanément » ; la page Bobex ne dit pas combien de fournisseurs reçoivent une demande.

## 5. Architecture recommandée

| Type | Page | Slug français | Slug anglais | Requête principale |
|---|---|---|---|---|
| Socle | Accueil | `/` | `/en/` | marque |
| Socle | Méthode, par étapes | `/methode/` | `/en/how-it-works/` | — |
| Socle | Engagements | `/engagements/` | `/en/commitments/` | lead exclusif |
| Socle | À propos, fondateurs | `/a-propos/` | `/en/about/` | marque |
| Conversion | Demande de rappel | `/demande-de-rappel/` | `/en/request-a-call/` | — |
| Pilier | Trouver des chantiers | `/trouver-des-chantiers/` | `/en/find-building-work/` | comment trouver des chantiers |
| Métier | Couverture-zinguerie | `/trouver-des-chantiers/couverture/` | `/en/find-building-work/roofing/` | trouver des chantiers de couverture |
| Métier | Façade | `/trouver-des-chantiers/facade/` | `/en/find-building-work/facade/` | trouver chantier facade |
| Métier, phase 2 | Isolation, menuiserie extérieure, charpente | `/trouver-des-chantiers/{activite}/` | `/en/find-building-work/{trade}/` | trouver chantier isolation |
| Comparatif | Page thèse | `/comparatif/plateformes-de-devis-ou-rendez-vous-exclusifs/` | `/en/compare/quote-platforms-vs-exclusive-appointments/` | plateforme devis artisan |
| Comparatif | Fiches | `/comparatif/habitatpresto-pro/`, `/travaux-com/`, `/plateformes-de-devis-belgique/`, `/apporteur-d-affaires-btp/` | `/en/compare/…` | habitatpresto pro avis |
| Blog | Articles | `/blog/{slug}/` | `/en/blog/{slug}/` | voir annexe |
| Glossaire | 12 à 20 termes | `/glossaire/{terme}/` | `/en/glossary/{term}/` | leads qualifiés définition |
| Auteurs | Deux fiches | `/auteurs/{prenom-nom}/` | `/en/authors/{name}/` | — |

Deux pages métier suffisent au lancement : elles servent d'abord à convaincre un gérant déjà appelé. Le glossaire répond aux requêtes de définition relevées (« lead qualifié définition », « apporteur d'affaires définition », « carnet de commandes définition »).

**Modèles** (title d'environ 60 caractères, description de 140 à 155 ; jamais de prix ni de nombre de rendez-vous) :

- Métier : `Trouver des chantiers de {activité} | Rendez-vous exclusifs – {Marque}` · `Des rendez-vous de devis en {activité} fixés dans votre agenda, jamais revendus. Un seul {métier} par secteur, sans engagement de durée.`
- Fiche comparative : `{Plateforme} : avis, tarifs et fonctionnement côté artisan ({année})` · `Ce que {Plateforme} publie sur ses prix, son engagement et le partage des demandes, sources à l'appui. Mis à jour le {date}.`
- Article : `{Requête cible} : {bénéfice concret} ({année})` · `{Réponse en une phrase}. {Méthode ou preuve}. Pour les {métier}.`
- Glossaire : `{Terme} : définition pour les artisans du bâtiment` · `{Terme} expliqué en une phrase, avec un exemple sur un chantier de {activité}.`
- Anglais : `{Trade} work in France and Belgium | Exclusive quote appointments – {Brand}`.

## 6. Vingt briefs priorisés

Ils sont classés par proximité de la vente, puis potentiel, puis difficulté. Chacun figure en annexe avec titre, requête cible, intention, angle, plan et maillage.

## 7. Calendrier éditorial sur 12 semaines

| Semaine | Mises en ligne |
|---|---|
| 1 | Pages socles, deux pages métier, glossaire (8 termes), article 4 |
| 2 | Page thèse du comparatif, article 1 |
| 3 | Fiche 2 (Habitatpresto Pro), article 7 (démarchage 2026) |
| 4 | Fiche 3 (Travaux.com), article 8 (publicité Facebook) |
| 5 | Pilier 5, glossaire (6 termes de plus) |
| 6 | Articles 6 et 11 |
| 7 | Articles 9 et 10 |
| 8 | Articles 12 (Belgique) et 13 |
| 9 | Articles 14 et 15 |
| 10 | Articles 16 et 17 |
| 11 | Articles 18 et 19 |
| 12 | Article 20, mise à jour datée des fiches, bilan Search Console |

## 8. Règles on-page

- **Titres** : un H1 (requête et bénéfice) ; des H2 repris des sous-questions du CSV ; 40 à 60 mots de réponse directe sous chaque H2 ; un tableau dès qu'il y a comparaison.
- **Maillage** : chaque article pointe vers une page métier, un comparatif, un terme du glossaire et la demande de rappel.
- **Auteur réel** : signature d'un fondateur, fiche auteur (photo, parcours, lien LinkedIn), relecture par le second.
- **Dates** : « Publié le » et « Mis à jour le » visibles ; `datePublished` et `dateModified` en ISO 8601 avec fuseau ; prix de tiers datés et revérifiés chaque trimestre.
- **Données structurées** : `Organization`, `WebSite`, `BreadcrumbList`, `BlogPosting` avec `author` de type `Person` et son `url`, `Service` sur les pages métier, `DefinedTerm` au glossaire, `FAQPage` seulement si la FAQ est visible. Aucun avis ni note sans client. Le balisage reprend le texte visible.
- **hreflang** : `fr` et `en` réciproques, auto-référents, en URL absolues, `x-default` vers le français. Pas d'arbre `fr-BE` dupliqué : des pages belges dédiées dans l'arbre français.
- **Moteurs génératifs** : Google indique qu'aucune optimisation, balise ni fichier particulier n'est requis pour AI Overviews et AI Mode. Il faut des pages indexables, du texte et des liens internes, donc des définitions nettes et des faits datés et sourcés.
- **Liens entrants** repérés dans les résultats : annuaires d'agences (La Fabrique du Net), publi-rédactionnels de la presse du bâtiment (Batiweb, utilisés par helloLeads), podcasts (BTP Engagé), pages partenaires d'organisations professionnelles (CAPEB Bas-Rhin).
- **Mesure** : Search Console dès la mise en ligne ; GA4 et Pixel Meta chargés après consentement.

## 9. Limites

- **Pas de volumes** : sans Keyword Planner ni Ahrefs, l'autocomplétion prouve qu'une requête existe, pas sa fréquence. Les potentiels sont estimés d'après la profondeur des complétions.
- **Pas de Trends**, donc pas de saisonnalité.
- **Positions non vérifiées** sur google.fr et google.be ; la difficulté est estimée d'après le type de domaines.
- **Classement par règles** : il reste du bruit (noms d'entreprises, fautes de frappe) ; le néerlandais est exclu.
- **Prix de tiers divergents** : pour Travaux.com, 15 à 40 € par devis selon Obat, jusqu'à 90 € HT par lead selon Pro by Crédit Agricole.
- **Droit** : seules la page Service Public et l'accueil de Do Not Call Me ont été lus ici. Le cadre complet (prospection entre entreprises, Belgique, rénovation énergétique) figure dans le rapport juridique de la session (`legal.md`), à suivre pour les articles 7 et 20.

## Sources (ouvertes le 17/11/2026)

- Autocomplétion : https://suggestqueries.google.com/complete/search?client=firefox&hl=fr&gl=fr&q=trouver%20des%20chantiers (aussi avec `gl=be`, `gl=gb`, `ds=yt`) ; https://duckduckgo.com/ac/?q=trouver%20des%20chantiers&kl=fr-fr
- Trends : https://trends.google.com/trends/explore?date=today%205-y&geo=FR (429)
- https://entreprendre.service-public.gouv.fr/actualites/A18384?lang=fr (21/07/2026, mis à jour le 11/08/2026)
- https://www.donotcallme.be/fr/ (non daté)
- https://pro.credit-agricole.fr/artisan/trouver-chantiers (05/11/2025, mis à jour le 22/12/2025)
- https://www.shine.fr/blog/meilleurs-sites-trouver-chantiers-artisan/ (29/06/2023, mis à jour « le 3 avril »)
- https://www.legalnest.fr/trouver-chantiers (non daté)
- https://www.obat.fr/blog/acheter-devis-travaux/ (02/12/2019, mis à jour le 09/06/2026)
- https://www.habitatpresto.com/pro/conseils/pratiques/chantiers-couverture (20/05/2026)
- https://www.effy.fr/pro/boite-a-outils/lead-travaux (09/06/2026, mis à jour le 02/11/2026)
- https://www.bobex.be/fr-be/leads/construction/ (non daté)
- https://pro.trustup.be/fr/trouver-chantiers-batiment-belgique/ (mis à jour le 22/06/2026 ; texte lu dans le dossier de travail de la session)
- https://developers.google.com/search/docs/appearance/ai-features ; https://developers.google.com/search/docs/specialty/international/localized-versions ; https://developers.google.com/search/docs/appearance/structured-data/article (dates de mise à jour non visibles)
- Non ouverte : la fiche DGCCRF sur economie.gouv.fr (403).

## Annexe. Détail des 20 briefs

Requêtes secondaires et sources à citer : voir `seo-briefs-articles.csv`.

### 1. Sites pour trouver des chantiers : le comparatif côté artisan (2026)

- `/blog/sites-pour-trouver-des-chantiers-comparatif/` · `/en/blog/websites-to-find-building-jobs-compared/` · semaine 2
- **Requête cible** : site pour trouver des chantiers (FR+BE) · commerciale (comparaison) · potentiel fort, difficulté forte, proximité de la vente forte
- **Angle** : Comparer par modèle économique et par partage de la demande (combien d'artisans reçoivent la même fiche), avec prix publics sourcés et datés, au lieu d'un « top 10 ».
- **Plan** : 1. Les 4 modèles : abonnement, paiement au contact, commission, rendez-vous exclusif ; 2. Tableau : prix publics, engagement, partage de la demande ; 3. Ce que « gratuit » veut dire ; 4. Les questions à poser avant de s'inscrire ; 5. Quand une plateforme reste pertinente ; 6. L'alternative : des rendez-vous jamais revendus ; 7. FAQ
- **Maillage** : Comparatif thèse ; fiches Habitatpresto Pro et Travaux.com ; glossaire « lead partagé » ; demande de rappel

### 2. Habitatpresto Pro : avis, tarifs et fonctionnement côté artisan (2026)

- `/comparatif/habitatpresto-pro/` · `/en/compare/habitatpresto-pro/` · semaine 3
- **Requête cible** : habitatpresto pro avis (FR) · commerciale (évaluation) · potentiel fort, difficulté moyenne, proximité de la vente forte
- **Angle** : Fiche factuelle et datée, sans dénigrement : ce que la plateforme publie, ce que disent les sources tierces, ce qui n'est pas public ; méthode de calcul du coût par chantier signé.
- **Plan** : 1. Ce que vend Habitatpresto Pro, selon ses propres pages ; 2. Tarifs et engagement : ce qui est public, ce qui ne l'est pas ; 3. Une demande est-elle partagée ? Ce que disent les sources ; 4. Calculer votre coût par chantier signé ; 5. Résilier : ce qu'il faut relire dans votre contrat ; 6. Pour quel artisan c'est adapté, pour lequel non ; 7. FAQ
- **Maillage** : Comparatif thèse ; article 1 ; fiche Travaux.com ; glossaire « coût par chantier signé »

### 3. Travaux.com côté artisan : prix du contact, avis et alternatives (2026)

- `/comparatif/travaux-com/` · `/en/compare/travaux-com/` · semaine 4
- **Requête cible** : travaux.com avis artisan (FR) · commerciale (évaluation) · potentiel fort, difficulté moyenne, proximité de la vente forte
- **Angle** : Même grille que la fiche Habitatpresto : faits publics datés, écarts entre sources signalés, calcul du coût par chantier signé.
- **Plan** : 1. Comment fonctionne Travaux.com pour un professionnel ; 2. Prix du contact : les fourchettes publiées et leurs écarts ; 3. Combien d'artisans reçoivent la même demande ? ; 4. Ce que disent les avis d'artisans, et leurs limites ; 5. Calculer votre coût par chantier signé ; 6. Alternatives ; 7. FAQ
- **Maillage** : Comparatif thèse ; article 18 ; fiche Habitatpresto Pro

### 4. Lead partagé, lead exclusif, rendez-vous qualifié : les différences pour un artisan

- `/blog/lead-partage-lead-exclusif-rendez-vous-qualifie/` · `/en/blog/shared-leads-exclusive-leads-qualified-appointments/` · semaine 1
- **Requête cible** : lead exclusif (FR+BE) · informationnelle · potentiel faible à moyen, difficulté faible, proximité de la vente très forte
- **Angle** : Traduire le jargon marketing dans les mots de l'artisan (fiche, demande, visite de devis) et montrer ce qui change sur le terrain : le nombre de concurrents sur la même demande.
- **Plan** : 1. Une demande, un lead, un rendez-vous : trois choses différentes ; 2. Lead partagé : la même fiche vendue plusieurs fois ; 3. Lead exclusif : exclusif jusqu'où ? ; 4. Rendez-vous qualifié : ce qui a été vérifié avant la visite ; 5. Tableau comparatif ; 6. Les questions à poser à tout fournisseur ; 7. FAQ
- **Maillage** : Glossaire (4 termes) ; page Engagements ; page Méthode ; article 11

### 5. Comment trouver des chantiers en 2026 : 9 canaux classés par coût du chantier signé

- `/trouver-des-chantiers/` · `/en/find-building-work/` · semaine 5
- **Requête cible** : comment trouver des chantiers (FR+BE) · informationnelle puis commerciale · potentiel très fort, difficulté très forte, proximité de la vente moyenne
- **Angle** : Page pilier : classement par coût et par exclusivité plutôt qu'une liste ; chaque canal renvoie vers une page métier ou un article ; données de terrain de l'agence ajoutées dès qu'elles existent.
- **Plan** : 1. Réponse courte : les canaux qui remplissent un planning ; 2. Bouche-à-oreille et voisinage des chantiers ; 3. Fiche Google et avis ; 4. Plateformes de devis ; 5. Publicité locale Meta et Google ; 6. Sous-traitance, apporteurs d'affaires, réseau ; 7. Tableau coût, délai, exclusivité et FAQ
- **Maillage** : Pages métier couverture et façade ; comparatif thèse ; articles 1, 6, 8, 10

### 6. Trouver des chantiers gratuitement : ce qui est vraiment gratuit, et ce que cela coûte en temps

- `/blog/trouver-des-chantiers-gratuitement/` · `/en/blog/find-building-jobs-for-free/` · semaine 6
- **Requête cible** : trouver des chantiers gratuitement (FR+BE) · informationnelle · potentiel fort, difficulté forte, proximité de la vente moyenne
- **Angle** : Honnêteté : lister ce qui est réellement gratuit, chiffrer le temps passé, dire à partir de quand payer a du sens. Sert aussi à écarter les demandes hors cible.
- **Plan** : 1. Les sources réellement gratuites ; 2. Le coût caché : les heures de devis non signés ; 3. Les « gratuits » qui deviennent payants ; 4. Calculer ce que vous coûte un chantier « gratuit » ; 5. Quand passer au payant ; 6. FAQ
- **Maillage** : Pilier ; article 1 ; article 15 ; demande de rappel

### 7. Démarchage téléphonique interdit depuis le 11 août 2026 : ce qu'un artisan peut encore faire

- `/blog/demarchage-telephonique-artisan-regles-2026/` · `/en/blog/cold-calling-rules-france-2026-tradespeople/` · semaine 3
- **Requête cible** : démarchage téléphonique interdit professionnel (FR) · informationnelle (réglementaire) · potentiel fort, difficulté forte en tête, faible en longue traîne, proximité de la vente moyenne
- **Angle** : Lecture côté artisan : rappeler une demande reçue, consentement, horaires, preuve. Sources officielles citées et datées, relecture par un juriste.
- **Plan** : 1. La règle en trois phrases ; 2. Rappeler un particulier qui a demandé un devis : ce qui est permis ; 3. Le consentement : forme, durée d'un an, preuve ; 4. Jours et horaires autorisés ; 5. Rénovation énergétique : le régime le plus strict ; 6. Sanctions et nullité du contrat ; 7. Check-list de conformité et FAQ
- **Maillage** : Page Méthode (rappel en moins de 5 minutes) ; article 20 ; glossaire « consentement » ; politique de confidentialité

### 8. Publicité Facebook pour un artisan du bâtiment : budget, rayon, formulaire

- `/blog/publicite-facebook-artisan-batiment/` · `/en/blog/facebook-ads-for-tradespeople/` · semaine 4
- **Requête cible** : publicité facebook prix (FR) · informationnelle · potentiel moyen, difficulté moyenne à forte, proximité de la vente forte
- **Angle** : Le budget est payé directement à Meta par l'artisan ; ce qui fait la différence n'est pas l'annonce mais le rappel dans les minutes qui suivent.
- **Plan** : 1. Ce que Facebook sait faire pour un couvreur, et ce qu'il ne sait pas faire ; 2. Un rayon de 25 à 40 km autour du dépôt : pourquoi ; 3. Budget : qui paie quoi, à qui ; 4. L'annonce : des photos réelles de chantier ; 5. Le formulaire : quatre questions qui filtrent ; 6. Après le clic : rappel, vérification, visite ; 7. FAQ
- **Maillage** : Page Méthode ; article 17 ; glossaire « formulaire instantané » ; demande de rappel

### 9. Relance de devis : calendrier, modèles de SMS et script d'appel pour artisans

- `/blog/relance-devis-artisan/` · `/en/blog/quote-follow-up-for-tradespeople/` · semaine 7
- **Requête cible** : relance devis artisan (FR) · informationnelle · potentiel fort, difficulté moyenne, proximité de la vente moyenne
- **Angle** : Relance pensée pour un chantier de plusieurs milliers d'euros après une visite, pas pour un devis envoyé à froid ; modèles prêts à copier.
- **Plan** : 1. Quand relancer : les repères publiés et leurs limites ; 2. Appel, SMS, e-mail : dans quel ordre ; 3. Trois modèles de SMS ; 4. Un script d'appel de deux minutes ; 5. Quand arrêter ; 6. Mesurer : le taux de transformation ; 7. FAQ
- **Maillage** : Article 15 ; page Méthode (rappels SMS) ; glossaire « taux de transformation »

### 10. Apporteur d'affaires BTP : commission, contrat, et quand préférer une agence

- `/comparatif/apporteur-d-affaires-btp/` · `/en/compare/business-introducers-construction/` · semaine 7
- **Requête cible** : apporteur d'affaires btp (FR+BE) · informationnelle puis commerciale · potentiel fort, difficulté moyenne, proximité de la vente moyenne à forte
- **Angle** : Comparer trois façons de déléguer l'apport de chantiers (commission au chantier signé, plateforme, agence) avec la même grille de critères.
- **Plan** : 1. Ce que fait un apporteur d'affaires ; 2. Commission : les fourchettes publiées et leurs sources ; 3. Le contrat : les clauses à exiger ; 4. Apporteur, plateforme, agence : tableau comparatif ; 5. Les signaux d'alerte ; 6. FAQ
- **Maillage** : Comparatif thèse ; article 11 ; glossaire « apporteur d'affaires »

### 11. Achat de leads travaux : sept questions à poser avant de signer

- `/blog/achat-leads-travaux-questions/` · `/en/blog/buying-home-improvement-leads-questions/` · semaine 6
- **Requête cible** : achat leads travaux (FR+BE) · transactionnelle · potentiel faible à moyen, difficulté faible à moyenne, proximité de la vente très forte
- **Angle** : Grille d'audit neutre, que l'agence s'applique à elle-même : ses réponses sont publiées sur la page Engagements.
- **Plan** : 1. D'où vient la demande ? ; 2. À combien d'artisans est-elle vendue ? ; 3. Qui l'a rappelée, et en combien de temps ? ; 4. Qu'est-ce qui a été vérifié ? ; 5. Durée d'engagement et sortie ; 6. Qui paie la publicité ? ; 7. Que se passe-t-il si le rendez-vous n'a pas lieu ?
- **Maillage** : Page Engagements ; article 4 ; comparatif thèse ; demande de rappel

### 12. Solvari, Bobex, TrustUp : les plateformes de devis en Belgique vues par un entrepreneur

- `/comparatif/plateformes-de-devis-belgique/` · `/en/compare/quote-platforms-belgium/` · semaine 8
- **Requête cible** : trustup pro avis (BE) · commerciale (évaluation) · potentiel moyen, difficulté faible, proximité de la vente forte
- **Angle** : Vocabulaire belge (entrepreneur, toiturier), prix et conditions publics sourcés, question du partage des demandes posée à chaque plateforme.
- **Plan** : 1. Trois modèles belges ; 2. Ce que chaque plateforme publie : prix, engagement, vérification ; 3. Partage de la demande : ce qui est dit, ce qui ne l'est pas ; 4. Calculer le coût par chantier signé ; 5. Alternatives ; 6. FAQ
- **Maillage** : Comparatif thèse ; page métier couverture ; article 4

### 13. Trouver des chantiers chez les particuliers : viser les propriétaires occupants de votre secteur

- `/blog/trouver-des-chantiers-chez-les-particuliers/` · `/en/blog/find-residential-jobs-homeowners/` · semaine 8
- **Requête cible** : trouver des chantiers particuliers (FR+BE) · commerciale (recherche de solution) · potentiel moyen, difficulté moyenne, proximité de la vente forte
- **Angle** : Expliquer la qualification (propriétaire occupant, besoin, zone) comme tri avant déplacement.
- **Plan** : 1. Pourquoi le particulier propriétaire occupant ; 2. Où il se trouve : le rayon autour du dépôt ; 3. Ce qu'il faut vérifier avant de se déplacer ; 4. Le voisinage d'un chantier en cours ; 5. Du premier appel à la visite ; 6. FAQ
- **Maillage** : Page Méthode ; article 14 ; glossaire « propriétaire occupant »

### 14. Flyer de couvreur : le modèle « voisinage de chantier » (texte, format, distribution)

- `/blog/flyer-couvreur-voisinage-chantier/` · `/en/blog/roofer-flyer-neighbourhood-template/` · semaine 9
- **Requête cible** : flyer couvreur (FR) · informationnelle · potentiel moyen, difficulté faible, proximité de la vente moyenne
- **Angle** : Le flyer distribué autour d'un chantier signé, pas le boîtage de masse ; modèle à télécharger.
- **Plan** : 1. Pourquoi les voisins d'un chantier ; 2. Le texte du flyer en soixante mots ; 3. Format, photo, preuve ; 4. Combien de boîtes, et quand ; 5. Distribution : les règles à vérifier ; 6. Le panneau de chantier en complément ; 7. FAQ
- **Maillage** : Page Méthode (étape flyers) ; article 13 ; page métier couverture

### 15. Taux de transformation des devis : le calculer et l'améliorer

- `/blog/taux-de-transformation-devis/` · `/en/blog/quote-conversion-rate/` · semaine 9
- **Requête cible** : taux de transformation devis (FR) · informationnelle · potentiel moyen, difficulté moyenne, proximité de la vente moyenne
- **Angle** : Suivre le taux par source de demande : c'est là que l'écart entre demande partagée et rendez-vous exclusif se mesure.
- **Plan** : 1. La formule ; 2. Le calculer par source de demande ; 3. Ce qui fait baisser le taux : demandes partagées, délais de rappel ; 4. Trois leviers ; 5. Un tableau de suivi à copier ; 6. FAQ
- **Maillage** : Article 9 ; article 4 ; glossaire

### 16. Devis gratuit ou payant : filtrer les curieux sans perdre les vrais projets

- `/blog/devis-gratuit-ou-payant-artisan/` · `/en/blog/free-or-paid-quotes/` · semaine 10
- **Requête cible** : faire payer un devis (FR) · informationnelle · potentiel moyen à fort, difficulté moyenne, proximité de la vente faible à moyenne
- **Angle** : La qualification avant la visite comme alternative au devis payant.
- **Plan** : 1. Ce que dit la règle ; 2. Pourquoi les artisans y pensent ; 3. L'alternative : qualifier avant de se déplacer ; 4. Les quatre questions ; 5. Quand facturer le déplacement ; 6. FAQ
- **Maillage** : Page Méthode ; article 13

### 17. Google Ads ou Meta Ads pour un couvreur : qui capte quelle demande

- `/blog/google-ads-ou-meta-ads-couvreur/` · `/en/blog/google-ads-vs-meta-ads-roofers/` · semaine 10
- **Requête cible** : google ads couvreur (FR) · commerciale (recherche de solution) · potentiel faible à moyen, difficulté faible, proximité de la vente forte
- **Angle** : Demande exprimée contre demande suscitée ; dire aussi les limites du choix de l'agence.
- **Plan** : 1. Demande exprimée ou demande suscitée ; 2. Urgence ou projet de rénovation ; 3. Coûts : ce qui est public, ce qui dépend du secteur ; 4. Ce que chaque canal exige après le clic ; 5. Notre choix et ses limites ; 6. FAQ
- **Maillage** : Article 8 ; page Méthode

### 18. Alternatives aux plateformes de devis : cinq façons d'obtenir des demandes non partagées

- `/blog/alternatives-plateformes-de-devis/` · `/en/blog/alternatives-to-quote-platforms/` · semaine 11
- **Requête cible** : alternative travaux com (FR) · commerciale (comparaison) · potentiel faible, difficulté faible, proximité de la vente très forte
- **Angle** : Répondre à la recherche d'alternative sans dénigrer : cinq voies, dont celle de l'agence, avec leurs limites.
- **Plan** : 1. Ce que l'on cherche à éviter ; 2. Fiche Google et avis ; 3. Voisinage de chantier ; 4. Publicité locale à son nom ; 5. Réseau de prescripteurs ; 6. Rendez-vous exclusifs par une agence : fonctionnement et limites ; 7. FAQ
- **Maillage** : Fiches 2 et 3 ; comparatif thèse ; demande de rappel

### 19. Carnet de commandes : lisser les creux d'activité d'une entreprise de couverture

- `/blog/carnet-de-commandes-entreprise-de-couverture/` · `/en/blog/order-book-roofing-company/` · semaine 11
- **Requête cible** : carnet de commande btp (FR+BE) · informationnelle · potentiel moyen, difficulté faible à moyenne, proximité de la vente moyenne
- **Angle** : Mesurer le carnet en semaines de travail et raisonner en délai entre demande et chantier ; saisonnalité à documenter avec les données de l'agence (Google Trends indisponible).
- **Plan** : 1. Définition, et mesure en semaines de travail ; 2. Les creux : d'où ils viennent ; 3. Anticiper : le délai entre la demande et le chantier ; 4. Trois sources régulières ; 5. Un tableau de bord mensuel ; 6. FAQ
- **Maillage** : Pilier ; article 15

### 20. Démarchage à domicile et faux couvreurs : comment un vrai couvreur rassure dès le premier contact

- `/blog/demarchage-a-domicile-faux-couvreurs/` · `/en/blog/door-to-door-sales-rogue-roofers/` · semaine 12
- **Requête cible** : démarchage à domicile règles (FR) · informationnelle (réglementaire) · potentiel moyen, difficulté moyenne, proximité de la vente faible à moyenne
- **Angle** : Article de confiance : ce que craint le particulier, et les preuves qu'un artisan sérieux montre.
- **Plan** : 1. Ce que craint le particulier ; 2. Les règles du démarchage à domicile ; 3. Les preuves à montrer : assurance, références locales ; 4. Pourquoi le flyer de voisinage n'est pas du porte-à-porte ; 5. Check-list du premier contact ; 6. FAQ
- **Maillage** : Article 7 ; article 14 ; page Engagements


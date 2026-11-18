# Audit SEO, GEO et design du site Bartier & Co

Date : 18 novembre 2026. Site audité : https://bartier-8b.vercel.app (futur domaine bartierandco.com), 24 pages.
Méthode : audit SEO (mots-clés, pages, contenu, technique, concurrence), critique design, audit « unslop ». Contre-vérification sur les documentations officielles de Google, OpenAI, Anthropic, Perplexity, Mistral, Apple et Meta, consultées le 18/11/2026.

## 1. Réponse courte

**Le site est prêt techniquement. Il n'est pas « prêt à 100 % » pour ressortir dans Google ou dans les réponses des IA, et cela ne dépend plus du code.**

| Volet | État | Ce qui manque |
|---|---|---|
| Technique (vitesse, balises, données structurées, liens, robots, plan du site) | Prêt | Rien à corriger |
| GEO (accès des robots IA, fichiers llms, faits cohérents, questions-réponses) | Prêt | Rien à corriger |
| Indexation | **Bloquée volontairement** | Brancher le domaine, puis lever le blocage |
| Contenu | Partiel | 3 articles sur 20 prévus, courts ; page « Qui sommes-nous » mince |
| Autorité (liens, avis, fiche Google) | À zéro | Fiche Google, premiers liens, mentions |
| Mentions légales | Incomplètes | SIREN, capital, greffe, TVA, directeur de publication, médiateur |

Les trois priorités, dans l'ordre : brancher le domaine et ouvrir l'indexation ; fournir les informations légales et les photos des fondateurs ; publier les articles à plus fort potentiel.

## 2. Ce qui a été mesuré

| Mesure | Résultat |
|---|---|
| Pages au plan du site | 24, toutes datées |
| Liens internes et ancres vérifiés | 661, aucun défaut |
| Titre principal (h1) | 1 par page |
| Titres de page | 30 à 62 caractères, tous différents |
| Descriptions | 129 à 159 caractères, toutes différentes |
| Données structurées | Présentes et valides sur chaque page ; fichiers cités tous existants |
| Images | Texte alternatif et dimensions réelles sur toutes |
| Lighthouse, téléphone, site en ligne | Performance 97 à 99, accessibilité 100, bonnes pratiques 100 |
| Affichage principal (LCP) | 1,4 à 2,3 s ; décalage de mise en page 0 à 0,003 |
| Audit d'affichage | 25 pages en 2 formats, aucun débordement, aucune erreur |

La note SEO de Lighthouse est à 69 pour une seule raison : la balise `noindex`, posée exprès tant que le domaine n'est pas branché. Sans elle, la note est de 100.

Non vérifié : Safari et Firefox réels (seul Chromium est disponible ici) ; l'outil « Résultats enrichis » de Google (les données structurées ont été contrôlées par programme, pas par l'outil de Google).

## 3. Corrigé pendant cet audit

| Défaut trouvé | Gravité | Correction |
|---|---|---|
| Articles : l'image citée dans les données structurées pointait vers un dossier qui n'existe plus | Élevée | Adresse corrigée, vérifiée en ligne |
| Pages métiers : 3 liens internes entrants seulement | Élevée | Liens dans le pied de page de toutes les pages et bande « Autres métiers » : 24 liens entrants |
| Articles : 2 liens internes entrants | Moyenne | Bande « À lire aussi » sur les articles et sur les pages Google Ads et Meta Ads : 4 à 6 liens |
| Accueil : le titre principal était le seul mot « Complet. » | Moyenne | Le titre principal est maintenant la phrase d'accroche, qui nomme la cible. L'affichage ne change pas |
| 16 photos déclaraient des proportions fausses | Moyenne | Dimensions réelles du fichier servi |
| Robots d'indexation de Mistral et de Meta AI non nommés | Moyenne | Ajoutés (21 groupes dans robots.txt) |
| Bloc « fuite de toiture » : nom différent du titre visible | Faible | Aligné sur le titre visible |
| Accueil : questions-réponses absentes des données structurées | Faible | Ajoutées, identiques au texte visible |
| Espaces et apostrophes non typographiques (18 cas sur l'accueil) | Faible | Corrigé sur tout le site, à la construction |
| Durées écrites tantôt en chiffres, tantôt en lettres | Faible | Chiffres partout (« 5 minutes », « 15 minutes ») |
| Photos larges lourdes | Faible | Environ 13 % de poids en moins sur l'ensemble des photos, sans différence visible |

Un changement de texte est à valider : l'accroche de l'accueil commence maintenant par « Artisans du bâtiment : ».

## 4. Mots-clés : où le site se place

Source : la recherche du 17/11/2026 (`docs/research/seo-mots-cles.md`, 1 475 requêtes réelles). Les volumes exacts ne sont pas connus : seuls le potentiel et la difficulté relatifs sont donnés.

| Requête | Intention | Potentiel | Difficulté | Page sur le site |
|---|---|---|---|---|
| comment trouver des chantiers | information puis solution | très fort | très forte | Non |
| site pour trouver des chantiers | comparaison | fort | forte | Non |
| habitatpresto pro avis | évaluation | fort | moyenne | Non |
| travaux.com avis artisan | évaluation | fort | moyenne | Non |
| trouver des chantiers gratuitement | information | fort | forte | Non |
| démarchage téléphonique interdit (artisan) | réglementaire | fort | forte en tête | Non |
| relance devis artisan | information | fort | moyenne | Oui, article court |
| apporteur d'affaires btp | information | fort | moyenne | Non |
| publicité facebook artisan | information | moyen | moyenne | Page Meta Ads |
| google ads couvreur | solution | faible à moyen | faible | Page Google Ads et article |
| lead exclusif | information | faible à moyen | faible | Oui, article court |
| achat leads travaux | transaction | faible à moyen | faible | Non |
| alternative travaux com | comparaison | faible | faible | Non |
| trouver des chantiers de couverture, façade, menuiserie, charpente, isolation | solution | faible à moyen | faible | Oui, 5 pages métiers |
| flyer couvreur | information | moyen | faible | Non |
| taux de transformation devis | information | moyen | moyenne | Non |
| devis toiture, ravalement, fenêtres, charpente, isolation (particuliers) | transaction | fort | très forte | Oui, 6 pages |

Lecture : les pages de service existent. Les requêtes qui amènent du monde (« trouver des chantiers », les comparatifs de plateformes) n'ont pas encore de page.

## 5. Contenu : ce qui manque

| Sujet | Pourquoi | Format | Priorité | Effort |
|---|---|---|---|---|
| Comment trouver des chantiers : les canaux classés par coût | La requête la plus cherchée de la cible | Page de fond | Haute | Plusieurs jours |
| Sites pour trouver des chantiers : comparatif côté artisan | Aucune agence dans les résultats, angle libre (le partage de la demande) | Article comparatif | Haute | Une journée |
| Habitatpresto Pro et Travaux.com côté artisan | 208 requêtes de marque, résultats tenus par des forums | Fiches factuelles et datées | Haute | Une journée chacune |
| Démarchage téléphonique : ce qu'un artisan peut encore faire | Sujet actif depuis le 11/08/2026 | Article | Moyenne | Une demi-journée |
| Les 3 articles existants (environ 420 mots) | Trop courts face aux guides concurrents | Les étoffer : exemples, modèles, tableaux | Moyenne | Deux heures chacun |
| Qui sommes-nous | Pas de photo ni de parcours des fondateurs | Photos, deux parcours courts, liens LinkedIn | Haute | Une heure, avec vos éléments |

Les 20 sujets sont déjà cadrés dans `docs/research/seo-briefs-articles.csv`.

## 6. Technique

| Contrôle | État | Détail |
|---|---|---|
| Vitesse sur téléphone | Conforme | 97 à 99, LCP sous 2,5 s |
| Adaptation au téléphone | Conforme | Aucun débordement ; boutons, liens de navigation et champs à 44 px ou plus (un lien placé dans une phrase garde la hauteur du texte) |
| HTTPS, en-têtes de sécurité | Conforme | Fourni par l'hébergeur, en-têtes ajoutés |
| Une seule adresse par page | Conforme | Redirections 308 vers l'adresse avec barre finale |
| Adresse canonique | Conforme | Vers bartierandco.com |
| Plan du site, robots.txt | Conforme | 24 adresses, dates réelles |
| Page 404 | Conforme | Vrai code 404 |
| Données structurées | Conforme | Organisation, site, service, fil d'Ariane, article, questions-réponses, page « à propos », personnes |
| Indexation | **Bloquée** | `noindex` volontaire jusqu'au branchement du domaine |
| Domaine | **À faire** | bartierandco.com affiche encore une page d'attente |
| Formulaires | **À faire** | Sans service d'envoi, ils finissent sur WhatsApp, e-mail ou téléphone préremplis |

Deux précisions honnêtes sur les données structurées :
- Google n'affiche plus les questions-réponses enrichies depuis le 7 mai 2026. Le balisage reste utile aux autres moteurs et aux IA, mais n'apportera pas d'affichage particulier dans Google.
- Les pas-à-pas enrichis ne sont plus affichés non plus. Même remarque.

## 7. GEO : être cité par les IA

| Point | État |
|---|---|
| Robots de ChatGPT, Claude, Perplexity, Mistral, Gemini, Apple, Meta AI, Copilot | Autorisés et nommés |
| llms.txt et llms-full.txt (tout le texte du site, 91 Ko) | En place |
| Faits identiques partout (5 minutes, 8 h à 19 h, un seul artisan par secteur, sans engagement) | Vérifié |
| Réponses courtes et directes, questions-réponses sur chaque page de service | En place |
| Entité « Bartier & Co » décrite (adresse, téléphone, fondateurs, activité) | En place |

Trois limites à connaître :
1. Google précise qu'aucun fichier spécial n'est nécessaire pour apparaître dans ses réponses IA. Les fichiers llms sont un plus sans effet prouvé.
2. Une IA ne cite qu'un site indexé. Tant que le `noindex` est là, rien ne remontera.
3. Les IA citent surtout les marques dont d'autres sites parlent. C'est le volet « autorité », encore à zéro.

## 8. Concurrence

Comparaison qualitative, tirée des pages de résultats relevées le 17/11/2026. Aucun chiffre de liens ou de trafic n'a pu être mesuré sans outil payant.

| Critère | Bartier & Co | Plateformes (Habitatpresto Pro, Travaux.com) | Banques et logiciels (Qonto, Shine, Obat) |
|---|---|---|---|
| Pages de service par métier | Oui | Oui | Non |
| Guides longs sur « trouver des chantiers » | Non | Oui | Oui, mis à jour en 2025-2026 |
| Rythme de publication | 3 articles | Régulier | Régulier |
| Ancienneté et liens | Domaine neuf | Forts | Très forts |
| Angle distinctif | Demande non partagée, rappel en 5 minutes | Volume | Généraliste |
| Vitesse et qualité technique | Très bonnes | Non mesuré | Non mesuré |

Aucune agence spécialisée n'apparaît en tête sur ces requêtes : la place est libre, mais elle se gagne par le contenu et les liens.

## 9. Plan d'action

### Cette semaine

| Action | Effet | Effort | Dépend de |
|---|---|---|---|
| Brancher bartierandco.com, puis ouvrir l'indexation (un réglage, `LIVE = True`) | Décisif | 30 minutes | Accès au domaine |
| Déclarer le site dans Google Search Console et Bing Webmaster, envoyer le plan du site | Fort | 30 minutes | Domaine branché |
| Compléter les mentions légales | Fort (confiance, obligation légale) | 10 minutes | SIREN, capital, greffe, TVA, directeur de publication, médiateur |
| Créer la fiche Google Business Profile | Fort | 1 heure | Adresse et téléphone confirmés |
| Photos et parcours des deux fondateurs | Moyen | 1 heure | Vos éléments |
| Choisir le service d'envoi des formulaires | Fort (conversion) | 1 heure | Votre choix |

### Ce trimestre

| Action | Effet | Effort |
|---|---|---|
| Publier les 5 premiers sujets du plan éditorial | Fort | 1 à 2 jours par sujet |
| Étoffer les 3 articles existants | Moyen | 2 heures chacun |
| Premiers liens : annuaires professionnels, organisations du bâtiment, presse locale, partenaires | Fort | Continu |
| Collecter de vrais avis d'artisans dès les premiers clients | Fort | Continu |
| Tester le site sur un iPhone et un Android réels | Moyen | 30 minutes |

## 10. Espacement et design

Constat de départ : marges de section et alignements réguliers, mais l'écart entre un titre, son introduction et le contenu changeait d'une section à l'autre (8 règles différentes sur l'accueil, 3 gabarits différents sur les pages intérieures).

| Avant | Après |
|---|---|
| Titre vers introduction : 16, 19, 20 ou 24 px selon la section | 24 px partout |
| Introduction vers contenu : de 16 à 64 px sur téléphone | 40 px partout sur téléphone, 72 px sur ordinateur (mesuré section par section) |
| Marges de composants hors grille (15,2 ; 19,76 ; 14 ; 18 ; 22 ; 30 px) | Grille de 4 px : boutons, étiquettes, tuiles, listes, cartes |
| Avis en 4 + 2 sur ordinateur | 3 colonnes |
| Zones tactiles trop petites : logo d'en-tête (19 px), bouton « Retour » du formulaire (30 px), curseurs du calcul (30 px) | 44 px |
| Bouton répété dans le pied de page, juste sous le formulaire | Retiré quand le formulaire est au-dessus |
| Accroche de l'accueil avec un mot seul en bout de ligne | Lignes équilibrées |
| Longs titres d'articles coupés sur téléphone dans les liens | Retour à la ligne |

Reste à faire, avec vos éléments : les photos des fondateurs (deux monogrammes en attendant) et de vraies photos de chantier.

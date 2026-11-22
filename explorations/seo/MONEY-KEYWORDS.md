# Particuliers : les recherches d'achat (money terms)

Mis à jour le 22/11/2026. Objectif : ne viser que les recherches de quelqu'un qui veut faire faire ses travaux maintenant, pas celles de quelqu'un qui se renseigne.

## Méthode et limites

- Source : les suggestions de recherche Google (France, en français). 720 requêtes : 60 mots de départ sur les 5 métiers, croisés avec 12 signaux d'achat (devis, prix, entreprise, artisan, urgent, autour de moi, près de chez moi, RGE…).
- Résultat : 2 144 suggestions uniques, dont **1 057 recherches d'achat** une fois retirés les recherches d'information, les emplois et salaires, les magasins et les pays étrangers. La liste complète est dans `money-keywords.csv`.
- Limite : aucun volume de recherche. Aucun outil SEO n'est branché, et une suggestion prouve que la recherche existe sans dire combien de fois elle est faite. Pour les volumes : le Planificateur de mots-clés de Google Ads, gratuit avec un compte.
- Concurrence : vérifiée sur trois recherches types (« couvreur Lyon devis gratuit », « entreprise ravalement de façade Bordeaux devis », « couvreur urgence fuite toiture »).

## Ce qu'on garde, ce qu'on écarte

**On garde** : métier + ville, métier + « autour de moi / près de chez moi », devis (gratuit, en ligne), entreprise ou artisan, urgence, RGE.

**On écarte** : comment, pourquoi, quand, normes, aides, faire soi-même, salaires et formations, magasins, « pas cher », pays étrangers. Les recherches de prix seules (« refaire toiture prix m2 ») ne sont pas des cibles : les prix restent dans les pages, en appui.

## Les 5 formes d'une recherche d'achat

1. **Métier + ville** : « couvreur paris », « couvreur bordeaux », « ravalement façade toulouse ». Les villes les plus suggérées sont Paris, Bordeaux, Toulouse, Lille, Marseille, Nantes, Lyon, Rouen, Dijon et Le Havre.
2. **Métier + autour de moi ou près de chez moi**, souvent avec « les mieux notés » ou « ouvert actuellement ». C'est la forme la plus fréquente pour tous les métiers : 70 suggestions en toiture, 65 en fenêtres. Google y répond avec la carte et des pages ville. On la gagne avec des pages métier × ville et la fiche Google, pas avec un article.
3. **Métier + devis** : « couvreur devis gratuit », « charpentier devis en ligne », « devis ravalement façade en ligne », « isolation combles devis ».
4. **Urgence** : « couvreur urgence », « couvreur urgence fuite », « pose bâche toiture urgence », « charpentier urgence ».
5. **RGE** : surtout en isolation (45 suggestions) et en façade (24), par exemple « entreprise isolation combles rge » ou « isolation extérieure rge ». À viser uniquement si les artisans partenaires sont vraiment RGE.

## Qui occupe ces recherches aujourd'hui

Des annuaires et des plateformes qui ont une page par métier et par ville :
- Obat, avec par exemple « Les 20 meilleurs couvreurs à Lyon » ;
- Ootravaux, avec « Couvreur à Lyon » ;
- Pages Jaunes ;
- Habitatpresto, avec un article « couvreur autour de moi ».

Ce ne sont pas des guides, ce sont des pages d'action.

## Carte : recherche visée → page

| Recherches visées | Page | Statut |
|---|---|---|
| couvreur, couvreur près de chez moi, couvreur devis gratuit, devis toiture | /devis-travaux/toiture/ | titre et H1 réorientés le 22/11 |
| entreprise de ravalement, façadier, devis ravalement façade | /devis-travaux/ravalement-facade/ | titre réorienté le 22/11 |
| remplacement fenêtre, changer fenêtres devis, poseur et menuisier fenêtre | /devis-travaux/fenetres/ | titre et H1 réorientés le 22/11 |
| charpentier, charpentier devis gratuit, charpentier près de chez moi | /devis-travaux/charpente/ | titre et H1 réorientés le 22/11 |
| entreprise isolation combles, isolation combles devis | /devis-travaux/isolation/ | titre réorienté le 22/11 |
| couvreur + ville, ravalement façade + ville | /devis-travaux/toiture/<ville>/ et /devis-travaux/ravalement-facade/<ville>/ | 36 pages en ligne le 22/11 (18 villes × 2 métiers) |
| fenêtres, charpente, isolation + ville | /devis-travaux/<métier>/<ville>/ | à créer |
| couvreur urgence, fuite toiture urgence, bâche de toit | /devis-travaux/toiture/urgence/ | en ligne le 22/11 |
| démoussage toiture devis, artisan, autour de moi | /devis-travaux/toiture/demoussage/ | en ligne le 22/11 |
| changer gouttière, artisan zinguerie | /devis-travaux/toiture/gouttieres/ | à créer |
| entreprise isolation extérieure (autour de moi, RGE) | /devis-travaux/isolation/exterieur/ | à créer |
| traitement charpente devis, artisan | /devis-travaux/charpente/traitement/ | à créer |
| porte d'entrée, baie vitrée : devis, artisan | /devis-travaux/fenetres/porte-entree/ et /baie-vitree/ | à créer |

## Ordre conseillé

1. Fait : titres, descriptions et H1 des 5 pages métier.
2. Fait le 22/11 : toiture en urgence et démoussage.
3. Fait le 22/11 : couvreur et ravalement dans les 18 villes déjà vérifiées (l'entreprise couvre toute la France). Chaque page doit avoir ses propres faits locaux (règles d'urbanisme, aides, climat), tirés des fiches ville déjà vérifiées. Sans cela, Google traite ces pages comme des pages satellites et les écarte.
4. Les autres métiers dans ces villes, puis les sous-services.
5. Plus d'articles informatifs pour les particuliers.

## Garde-fous

- Ne pas écrire « RGE », « 24 h/24 » ou « intervention dans l'heure » sans que ce soit vrai.
- Ne créer une page ville que là où un artisan partenaire peut répondre, ou dire clairement « hors zone, nous vous le disons à l'appel ».
- Suivi dans la Search Console : filtrer les requêtes qui contiennent devis, couvreur, entreprise, autour de moi ou un nom de ville.

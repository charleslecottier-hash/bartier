# data.gouv.fr : déclarer l'observatoire comme réutilisation

But : un lien depuis data.gouv.fr vers https://bartierandco.com/chiffres-du-batiment/, sur la page d'un jeu de données de l'Insee.
À faire depuis votre navigateur : data.gouv.fr refuse les connexions depuis notre environnement de travail.

## 1. Le jeu de données à lier

Candidat principal, trouvé par recherche (à vérifier avant de lier) :
- « Activité productrice des entreprises » (Insee, séries de la Banque de données macroéconomiques) : https://www.data.gouv.fr/datasets/activite-productrice-des-entreprises
- Vérifier que sa description ou ses fichiers citent bien les index du bâtiment (BT, ou « Index bâtiment, travaux publics et divers de la construction »).

Solution de repli si ce n'est pas le cas :
- « Prix et indices de prix » (Insee) : https://www.data.gouv.fr/datasets/prix-et-indices-de-prix

Ne lier qu'un jeu qui contient vraiment les index BT.

## 2. Les champs du formulaire

**Titre**
Observatoire des index BT : valeurs mensuelles, courbes et calculateur de révision de prix

**Lien**
https://bartierandco.com/chiffres-du-batiment/

**Type**
Application (à défaut : Visualisation)

**Thématique**
La plus proche du logement, de l'urbanisme ou de l'économie, selon la liste proposée.

**Description**

Les 37 index BT publiés chaque mois par l'Insee (index bâtiment, base 100 en 2010), présentés pour les artisans, les entreprises du bâtiment et leurs clients :

- une page par index, avec la valeur du dernier mois, l'évolution sur un mois et sur un an, la courbe depuis octobre 2014, les 24 derniers mois et les moyennes annuelles ;
- un tableau de tous les index, classés par famille de travaux ;
- un calculateur gratuit de révision de prix selon la formule P = P0 × (a + (1 − a) × In / I0), qui donne le prix révisé et le détail du calcul ;
- les séries complètes en CSV et en JSON, réutilisables.

Les valeurs sont celles de la Banque de données macroéconomiques de l'Insee, reprises sans modification et mises à jour chaque mois après la publication officielle. Seules les variations sur un mois et sur un an sont calculées par l'éditeur.

Édité par Bartier & Co, agence qui trouve des clients aux artisans du bâtiment. Source : Insee.

**Mots-clés**
index-bt, bt01, batiment, construction, revision-de-prix, indices-de-prix, insee

**Image**
datagouv-observatoire.png (1600 × 640, capture de la page). Si le formulaire demande un format carré, recadrer sur le tableau sombre.

## 3. Après la publication

- Noter l'adresse de la réutilisation dans PLAN.md (section Suivi).
- La citer dans la section « Méthode » de l'observatoire, si elle est publiée.

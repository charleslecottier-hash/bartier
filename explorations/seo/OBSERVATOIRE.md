# Le Bâtimètre, l'observatoire Bartier & Co

Nom choisi le 23/11/2026 (avant : « Les chiffres du bâtiment »). L'adresse /chiffres-du-batiment/ ne change pas. Nom non trouvé sur le web au 23/11 ; à vérifier à l'INPI avant tout dépôt de marque.

En ligne le 22/11/2026 sur bartierandco.com. Objectif : une source de référence pour toute la profession, éditée par Bartier & Co, qui attire des liens et des citations (presse, moteurs de réponse IA) et des artisans qui cherchent l'indice BT01 chaque mois.

## Pages

| Page | Recherches visées |
|---|---|
| /chiffres-du-batiment/ | Bâtimètre, index BT, indices BT, chiffres du bâtiment |
| /chiffres-du-batiment/indices-bt/ | indices BT + mois, index BT Insee, tableau des index BT |
| /chiffres-du-batiment/indices-bt/btXX/ (38 pages) | indice BT01, indice BT01 + mois, index BT32, BT50, BT52… |
| /chiffres-du-batiment/revision-de-prix/ | révision de prix BT01, calcul révision de prix, formule de révision |

Chaque page d'index affiche la valeur du mois dès le haut de page, la courbe depuis octobre 2014, les 24 derniers mois, les moyennes annuelles, l'usage de l'index et une FAQ. Le calculateur garde le calcul dans l'adresse (lien partageable) et le copie prêt à coller dans une facture.

## Données

- Source : Insee, base de données macroéconomiques, jeu INDEX-BT-TP-DIV-IM-2010 (accès libre, sans clé).
- Script : `explorations/v8b/_build/indices_bt.py`. Il écrit le cache `_build/indices_bt.json` et les fichiers publics `assets/data/indices-bt.json` et `assets/data/indices-bt.csv`.
- Aucune valeur n'est retouchée. Les variations sur 1 mois et 1 an sont calculées par nos soins.
- Règle citée : BT01 seul index pour réviser un contrat de construction de maison individuelle (CCH, art. L231-11).

## Mise à jour mensuelle

L'Insee publie les index BT vers le milieu du mois (valeurs de septembre 2026 publiées le 13/11/2026).

1. `python3 _build/indices_bt.py` (ou `--essai` pour voir le dernier mois sans rien écrire).
2. `python3 _build/site.py` : titres, valeurs, tableaux et données structurées se mettent à jour seuls.
3. Mise en ligne, puis `python3 _build/indexnow.py`.

## Maillage

Menu « Comment ça marche », pied de page (Révision de prix BT01, Le Bâtimètre), chaque page métier vers l'index de son corps d'état, deux définitions dans le lexique (index BT, révision de prix), llms.txt.

## Suite prévue

1. Pages métier : nombre d'entreprises, taux horaire, chiffre d'affaires, par métier.
2. Baromètre des créations et défaillances d'entreprises du bâtiment (il faut un accès aux données BODACC, bloqué depuis cet environnement).

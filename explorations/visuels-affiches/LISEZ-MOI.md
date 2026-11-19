# Affiches Bartier & Co en situation

Trois montages : nos affiches posées dans des maquettes de panneaux (rue, mur noir à trois caissons, grand panneau sur béton).
Export JPG 1920 px de large, sans métadonnées.

| Fichier | Affiche |
|---|---|
| affiche-rue-particuliers.jpg | Propriétaires : « Pas cinq artisans. Un seul, près de chez vous. » |
| affiches-nos-engagements.jpg | Les engagements en chiffres : 1 artisan par secteur, 5 min, 0 mois |
| panneau-plus-de-chantiers.jpg | Artisans : « Plus de chantiers. Moins de téléphone. » |

À utiliser sur LinkedIn, Instagram, dans la présentation ou les e-mails de prospection.
Ce sont des montages : ils ne montrent pas une vraie campagne d'affichage. À éviter sur la fiche Google,
qui demande des photos réelles et retire les images retouchées.

Vérifier que la licence des trois maquettes d'origine (_build/maquettes) autorise un usage commercial.

## Refaire les montages
```bash
node _build/mock_posters.js /tmp/affiches        # dessine les affiches (polices et logo du site)
python3 -I _build/mock_compose.py _build/maquettes /tmp/affiches _build/mock_quads.json .
```
Les noms de maquettes attendus par les scripts sont m1, m2, m3 : copier rue.jpg, mur-noir.jpg et panneau-beton.jpg sous ces noms dans un dossier à part.

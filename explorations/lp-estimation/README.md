# Pages d'estimation pour les clients artisans

Pages d'atterrissage pour les publicités Instagram et Facebook des clients de Bartier & Co. Il y en a une par métier : toiture, ravalement de façade, fenêtres, charpente et isolation.

Le visiteur répond à six questions et laisse son prénom et son numéro. Il voit alors une fourchette de prix, calculée à partir de prix publiés et sourcés. La demande part chez l'artisan.

Ces pages sont au nom du client, sur son domaine. Elles ne sont reliées ni au site bartierandco.com ni à son plan du site. Elles sont exclues des moteurs de recherche (`noindex`), car le même texte sert à plusieurs clients.

## Créer les pages d'un client

1. Copiez `clients/exemple.json` en `clients/<slug-du-client>.json`, puis remplissez-le (voir le tableau plus bas).
2. Lancez la génération :

```bash
python3 build.py clients/<slug-du-client>.json
```

3. Le dossier `dist/<slug-du-client>/` contient tout ce qu'il faut :
   - une page par métier (`/toiture/`, `/ravalement-facade/`, `/fenetres/`, `/charpente/`, `/isolation/`) ;
   - les polices et le logo ;
   - un `vercel.json` qui ajoute les en-têtes de sécurité et le `noindex`, et redirige `/` vers la première page.
4. Déployez ce dossier seul : un projet Vercel par client, sur son domaine ou un sous-domaine (par exemple `devis.entreprise-dupont.fr`).
   Vercel protège un nouveau projet par une connexion à son compte : retirez cette protection (Settings, Deployment Protection) pour que la page soit publique.

La fiche d'exemple est en ligne pour les tests : https://estimation-artisans-exemple-in-reach1.vercel.app/toiture/ (les numéros de téléphone et de WhatsApp sont fictifs).

Dans les annonces, utilisez l'adresse de la page avec ses paramètres de suivi, par exemple `https://devis.entreprise-dupont.fr/toiture/?utm_source=instagram&utm_campaign=toiture-hiver`. Les paramètres `utm_*`, `fbclid` et `gclid` sont transmis avec chaque demande.

## La fiche du client

| Champ | Rôle |
|---|---|
| `slug` | Nom du dossier de sortie (minuscules, chiffres, tirets) |
| `entreprise` | Nom affiché dans l'en-tête, les textes et les mentions |
| `logo` | Chemin du logo (SVG ou PNG), relatif à la fiche. Vide : le nom s'affiche en texte |
| `telephone` | Numéro affiché dans le bouton vert et à la fin |
| `whatsapp` | Numéro WhatsApp au format international sans `+` (ex. `33612345678`). Vide : pas de bouton WhatsApp |
| `envoi` | Adresse qui reçoit chaque demande en JSON (voir plus bas). Fortement conseillé |
| `zone` | Zone d'intervention affichée en haut de page (ex. « Lille et 30 km autour ») |
| `departements` | Départements couverts (ex. `["59", "62"]`). Hors zone, le visiteur est prévenu, sans être bloqué |
| `horaires` | Moment du rappel, repris après l'envoi (ex. « du lundi au vendredi ») |
| `contact` | La personne qui rappelle : `prenom`, `role` (ex. « gérant »), `photo` (chemin relatif à la fiche). Affichée sous le bouton et à l'étape du numéro. Sans photo, ses initiales s'affichent |
| `rappel` | Engagement de rappel affiché sous la personne (ex. « Rappel sous 24 h ouvrées »). Uniquement si l'artisan le tient |
| `avis` | Note et nombre d'avis Google, avec le lien vers la fiche (`note`, `nombre`, `lien`). Vide : rien ne s'affiche. Jamais d'avis inventés |
| `metiers` | Métiers à générer, parmi `toiture`, `facade`, `fenetres`, `charpente`, `isolation` |
| `accent` | Couleur de la partie mise en évidence dans les illustrations (couleur du client) |
| `atouts` | Arguments ajoutés sous le bouton. Seulement des faits vérifiables : « Assurance décennale », « Certifié RGE », etc. |
| `tarifs` | Tarifs propres à l'artisan, à la place des prix publiés (voir plus bas) |
| `meta_pixel` | Identifiant du pixel Meta. Rempli, il ajoute un bandeau de consentement et l'événement `Lead` |
| `legal` | Mentions légales de l'artisan : raison sociale, forme, capital, siège, SIRET, RCS, TVA, directeur de la publication, e-mail, assurance décennale, médiateur, hébergeur |

La génération liste les champs obligatoires manquants (« à compléter »). Une page ne doit pas être mise en ligne avec `[à compléter]` dans ses mentions légales.

## Recevoir les demandes

Avec `envoi`, la page envoie la demande en JSON (`POST`) à cette adresse dès la dernière étape. L'adresse peut être un service de formulaires qui transfère par e-mail, ou un webhook (Make, Zapier, Google Sheets…). Le JSON contient `type`, `metier`, `entreprise`, `fields` (travaux, quantité, estimation, détails, délai, statut, code postal, commune, prénom, téléphone), `consent`, `page` et `tracking`. Si l'envoi échoue, le visiteur voit le bouton WhatsApp, avec son message déjà rédigé.

Sans `envoi`, seul le bouton WhatsApp (ou l'appel) transmet la demande. Le visiteur doit appuyer sur « Envoyer » dans WhatsApp, et une partie des demandes se perd à ce moment-là.

## Le parcours

Sur téléphone, le titre et le bouton vert viennent en premier, le questionnaire juste en dessous. Une fois lancé, il occupe tout l'écran : la progression reste en haut et le bouton « Suivant » en bas, à portée du pouce. Sur ordinateur, le titre est à gauche et le questionnaire à droite, sans clic de plus.

Les tuiles illustrées passent à la question suivante dès qu'on les touche. Les surfaces et les quantités se règlent avec un curseur et des boutons − et +. Le code postal affiche le nom de la commune grâce à l'API publique de l'État (geo.api.gouv.fr) ; hors des départements du client, la page prévient le visiteur sans le bloquer. Vers la fin, le compteur laisse place à « Plus que 3 étapes », « Avant-dernière étape », puis « Dernière étape ».

À la dernière étape, l'estimation reste floutée jusqu'au numéro, qui se met en forme pendant la saisie. Il n'y a pas de case à cocher : une phrase d'information la remplace (« En validant, vous acceptez d'être rappelé… »), ce qui fait un champ obligatoire de moins. La demande vient du visiteur lui-même, et cela suffit pour le rappeler. L'estimation s'affiche ensuite comme un devis au nom de l'artisan, puis le visiteur est invité à envoyer des photos du chantier par WhatsApp.

## Les prix

Les prix viennent de `metiers.py`. Ce sont des prix moyens publiés, pose comprise, avec leur source et leur date : QuelleEnergie, La Maison Saint-Gobain, Hellowatt et Obat, relevés le 18/11/2026.

Un poste sans prix publié est quand même demandé, pour qualifier le projet, puis noté « chiffré à la visite ». C'est le cas des réparations, des fenêtres de toit, des gouttières, des baies, des portes et des volets. Aucun prix n'est inventé.

Pour utiliser les tarifs de l'artisan, ajoutez une fourchette par option, dans l'unité de la page :

```json
"tarifs": {"toiture": {"Nettoyage et démoussage": [20, 30], "Remplacement de la couverture": [90, 160]}}
```

La page cite alors les tarifs de l'artisan au lieu des sources.

## Vérifier avant de livrer

- Faire le parcours complet sur un téléphone, pour chaque métier livré.
- Tester l'envoi : une vraie demande doit arriver chez l'artisan.
- Relire les mentions légales et la confidentialité avec les informations du client.

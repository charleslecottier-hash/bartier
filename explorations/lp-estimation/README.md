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

Pour qu'une annonce mène directement au bon projet, ajoutez `projet=` à l'adresse : `/toiture/?projet=reparation-ou-fuite` coche « Réparation ou fuite » et ouvre la question suivante. La génération affiche les identifiants de chaque métier.

## La fiche du client

| Champ | Rôle |
|---|---|
| `slug` | Nom du dossier de sortie (minuscules, chiffres, tirets) |
| `entreprise` | Nom affiché dans l'en-tête, les textes et les mentions |
| `domaine` | Adresse du site du client (ex. `https://devis.entreprise-dupont.fr`). Sert à l'image d'aperçu des liens partagés |
| `logo` | Chemin du logo (SVG ou PNG), relatif à la fiche. Vide : le nom s'affiche en texte |
| `realisations` | Photos des vrais chantiers de l'artisan, par métier (ex. `{"toiture": [{"photo": "photos/toit-dupont.jpg", "legende": "Réfection d'une toiture à Roubaix"}]}`, chemins relatifs à la fiche). Elles remplacent les photos libres de droits sous le formulaire, sous le titre « Les chantiers de [entreprise] » |
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

Avec `envoi`, la page envoie la demande en JSON (`POST`) à cette adresse dès la dernière étape. Le plus simple est un service de formulaire comme Formspree ou FormSubmit, qui transfère chaque demande par e-mail à l'artisan : l'adresse du formulaire se met dans `envoi`. Un webhook (Make, Zapier, Google Sheets…) marche aussi. Le champ `message` contient la demande en clair, et `_subject` l'objet de l'e-mail. Le JSON contient aussi `type`, `metier`, `entreprise`, `fields` (travaux, quantité, estimation, détails, délai, statut, code postal, commune, prénom, téléphone), `consent`, `page` et `tracking`. Si l'envoi échoue, le visiteur voit le bouton WhatsApp, avec son message déjà rédigé.

Sans `envoi`, seul le bouton WhatsApp (ou l'appel) transmet la demande. Le visiteur doit appuyer sur « Envoyer » dans WhatsApp, et une partie des demandes se perd à ce moment-là.

## Le parcours

Sur téléphone, le titre et le bouton vert viennent en premier, puis un exemple d'estimation (la première option, à la quantité proposée) et le questionnaire juste en dessous. Une fois lancé, il occupe tout l'écran : la progression reste en haut et le bouton « Suivant » en bas, à portée du pouce. Sur ordinateur, le titre est à gauche et le questionnaire à droite, sans clic de plus.

Chaque option a sa propre illustration du chantier (mousse sur le toit, tuile manquante, façade à moitié repeinte, panneaux d'isolant…), et la tuile passe à la question suivante dès qu'on la touche. Les surfaces et les quantités se règlent avec un curseur et des boutons − et +. Le code postal affiche le nom de la commune grâce à l'API publique de l'État (geo.api.gouv.fr) ; hors des départements du client, la page prévient le visiteur sans le bloquer. Vers la fin, le compteur laisse place à « Plus que 3 étapes », « Avant-dernière étape », puis « Dernière étape ».

À la dernière étape, l'estimation reste floutée jusqu'au numéro, qui se met en forme pendant la saisie. Il n'y a pas de case à cocher : une phrase d'information la remplace (« En validant, vous acceptez d'être rappelé… »), ce qui fait un champ obligatoire de moins. La demande vient du visiteur lui-même, et cela suffit pour le rappeler. L'estimation s'affiche ensuite comme un devis au nom de l'artisan, puis le visiteur est invité à envoyer des photos du chantier par WhatsApp. Si la page se recharge (fréquent dans le navigateur d'Instagram après un passage par WhatsApp), le visiteur retrouve ses réponses et son estimation ; elles s'effacent quand il ferme l'onglet. Il peut aussi partager l'estimation (au conjoint, au propriétaire) depuis son téléphone. Sous le questionnaire, une foire aux questions répond aux hésitations : gratuité, origine des prix, prix final, qui rappelle, locataires, et une question propre au métier.

## Les photos

Sous le formulaire, une section montre le métier en photos : deux ou trois par page, à faire défiler du doigt sur téléphone. Par défaut, ce sont des photos libres de droits (voir `photos/SOURCES.md` : licences Unsplash et Pexels, usage commercial gratuit), titrées « [Le métier], en images » avec la mention « Photos d'illustration du métier ». Elles ne montrent pas les chantiers de l'artisan et ne doivent jamais être présentées comme tels.

Dès que l'artisan fournit ses propres photos de chantier, mettez-les dans sa fiche (`realisations`). La section devient « Les chantiers de [entreprise] ». Les légendes ne s'affichent pas : elles servent de texte de remplacement aux lecteurs d'écran. De vraies photos inspirent bien plus confiance. Retirez-en d'abord les métadonnées (lieu, date, appareil).

En haut de page, sur téléphone, un encadré compact donne l'exemple d'estimation, pour que le formulaire arrive vite. Sur ordinateur, la grande maison dessinée du métier porte cet exemple.

## L'image d'aperçu

Quand Node et Playwright sont installés, la génération crée pour chaque métier une image `og.png` (1200 × 630) : le titre, la première photo de la section (celle de l'artisan s'il en a fourni), l'exemple d'estimation et le nom de l'artisan. Elle s'affiche quand le lien est partagé sur WhatsApp, Facebook ou par SMS, à condition que `domaine` soit rempli.

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

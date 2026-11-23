# Pages d'estimation pour les clients artisans

Pages d'atterrissage pour les publicités Instagram et Facebook des clients de Bartier & Co. Il y en a une par métier : toiture, ravalement de façade, fenêtres, charpente et isolation.

Le visiteur répond à six questions et laisse son prénom et son numéro. Il voit alors une fourchette de prix, calculée à partir de prix publiés et sourcés. La demande s'inscrit en une ligne dans le Google Sheet des demandes, dans l'onglet du client. Par défaut, la page n'a ni bouton d'appel ni bouton WhatsApp : toutes les demandes passent par le formulaire.

Ces pages sont au nom du client, sur son domaine. Elles ne sont reliées ni au site bartierandco.com ni à son plan du site. Elles sont exclues des moteurs de recherche (`noindex`), car le même texte sert à plusieurs clients.

## Créer les pages d'un client

1. Copiez `clients/exemple.json` en `clients/<slug-du-client>.json`, puis remplissez-le (voir le tableau plus bas).
2. La première fois seulement, installez l'outil qui dessine la carte de la zone d'intervention :

```bash
npm install
```

3. Lancez la génération :

```bash
python3 build.py clients/<slug-du-client>.json
```

4. Le dossier `dist/<slug-du-client>/` contient tout ce qu'il faut :
   - une page par métier (`/toiture/`, `/ravalement-facade/`, `/fenetres/`, `/charpente/`, `/isolation/`) ;
   - les polices, le logo, les photos et la carte ;
   - un `vercel.json` qui ajoute les en-têtes de sécurité et le `noindex`, et redirige `/` vers la première page.
5. Déployez ce dossier seul : un projet Vercel par client, sur son domaine ou un sous-domaine (par exemple `devis.entreprise-dupont.fr`).
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
| `telephone` | Numéro de l'artisan, repris dans les mentions légales. Il n'apparaît dans des boutons que si `boutons_appel` vaut `true` |
| `boutons_appel` | `false` par défaut : aucun bouton d'appel ni WhatsApp, toutes les demandes passent par le formulaire. `true` : boutons d'appel (en-tête, zone, fin de page, résultat) et WhatsApp si `whatsapp` est rempli |
| `whatsapp` | Numéro WhatsApp au format international sans `+` (ex. `33612345678`). Utilisé seulement avec `boutons_appel` |
| `envoi` | `"tableau"` : chaque demande devient une ligne du Google Sheet (voir plus bas). C'est le réglage à utiliser. Une adresse https (Formspree, webhook) marche aussi |
| `zone` | Zone d'intervention affichée en haut de page (ex. « Lille et 30 km autour »). Vide, elle se déduit de `ville` et `rayon_km` |
| `ville` | Commune d'où part l'artisan (ex. « Lille »). Centre de la carte de la zone d'intervention |
| `rayon_km` | Rayon d'intervention en kilomètres (ex. `30`). Avec `ville`, il dessine la carte et sert au contrôle de zone |
| `code_postal` | Facultatif : à remplir seulement si plusieurs communes portent le même nom que `ville` |
| `departements` | Départements couverts (ex. `["59", "62"]`). Sert au contrôle de zone quand `ville` et `rayon_km` sont vides. Hors zone, le visiteur est prévenu, sans être bloqué |
| `horaires` | Moment du rappel, repris après l'envoi et sous la personne qui intervient (ex. « du lundi au vendredi » ou « du lundi au samedi, 8 h à 19 h ») |
| `contact` | La personne qui rappelle : `prenom`, `nom` (facultatif), `role` (ex. « gérant »), `photo` (chemin relatif à la fiche). Affichée sous le bouton, à l'étape du numéro et dans « Ce que nous faisons ». Sans photo, ses initiales s'affichent |
| `rappel` | Engagement de rappel affiché sous la personne (ex. « Rappel sous 24 h ouvrées »). Uniquement si l'artisan le tient |
| `avis` | Note et nombre d'avis Google, avec le lien vers la fiche (`note`, `nombre`, `lien`). Vide : rien ne s'affiche. Jamais d'avis inventés |
| `metiers` | Métiers à générer, parmi `toiture`, `facade`, `fenetres`, `charpente`, `isolation`. Ils forment aussi la liste cochée de « Ce que nous faisons » |
| `prestations` | Facultatif : lignes ajoutées à cette liste cochée (ex. `["Zinguerie et gouttières", "Étanchéité de toit-terrasse"]`) |
| `accent` | Couleur de la partie mise en évidence dans les illustrations (couleur du client) |
| `atouts` | Arguments ajoutés sous le bouton. Seulement des faits vérifiables : « Assurance décennale », « Certifié RGE », etc. |
| `tarifs` | Tarifs propres à l'artisan, à la place des prix publiés (voir plus bas) |
| `meta_pixel` | Identifiant du pixel (ensemble de données) Meta du client. Rempli, il ajoute le bandeau cookies, la case facultative et l'événement `Lead` (voir « Mesure des annonces ») |
| `google_ads` | Conversion Google Ads du client : `{"id": "AW-123456789", "label": "AbCdEf12"}`, lus dans Objectifs, Conversions, Configurer la balise. Rempli, la conversion part quand la demande est enregistrée, si le visiteur a accepté les cookies |
| `legal` | Mentions légales de l'artisan : raison sociale, forme, capital, siège, SIRET, RCS, TVA, directeur de la publication, e-mail, assurance décennale, médiateur, hébergeur |

La génération liste les champs obligatoires manquants (« à compléter »). Une page ne doit pas être mise en ligne avec `[à compléter]` dans ses mentions légales.

## Recevoir les demandes

Avec `"envoi": "tableau"`, la génération ajoute au dossier du client une fonction `api/lead.js` (source : `api_lead.js`). La page lui envoie la demande ; la fonction vérifie les champs et l'écrit en une ligne, en haut de l'onglet du client, dans le Google Sheet « Bartier & Co, demandes clients ». L'onglet se crée tout seul à la première demande. La colonne « Suivi » propose : À rappeler, Rappelé, Qualifié, Visite fixée, Devis remis, Signé, Sans suite, Hors zone.

Chaque ligne garde aussi la source de la visite : les paramètres `utm_*`, l'identifiant de clic Google (`gclid`, `gbraid`, `wbraid`) et Meta (`fbclid`), l'accord donné pour la mesure des annonces, et un identifiant de demande. Une même demande renvoyée après une coupure n'est écrite qu'une fois.

Si l'envoi échoue (connexion coupée), le visiteur voit « Votre demande n'est pas partie » et un bouton « Réessayer l'envoi ».

### Le tableau, une seule fois

1. Créez le Google Sheet « Bartier & Co, demandes clients » avec le compte Google de Bartier & Co.
2. Extensions, Apps Script : collez `sheets/apps-script.gs` à la place du code présent.
3. Remplacez `@@CLE@@` par une clé longue (au moins 16 caractères, lettres et chiffres). Ne la publiez nulle part et ne la mettez jamais dans le dépôt.
4. Déployer, Nouveau déploiement, type Application Web : exécuter en tant que « Moi », accès « Tout le monde ». Notez l'adresse qui finit par `/exec`.

### Pour chaque client, sur son projet Vercel

Dans Settings, Environment Variables :

| Variable | Valeur |
|---|---|
| `LEAD_SHEET_URL` | L'adresse `/exec` de l'application Web |
| `LEAD_SHEET_KEY` | La clé choisie à l'étape 3 |
| `META_ACCESS_TOKEN` | Facultatif : jeton de l'API Conversions du pixel du client (Gestionnaire d'événements, Paramètres, API Conversions, Générer un jeton d'accès) |
| `META_TEST_EVENT_CODE` | Facultatif, pendant les essais seulement : le code de l'onglet « Tester les événements ». À retirer avant le lancement |

Redéployez après avoir ajouté les variables. Sans `LEAD_SHEET_URL` et `LEAD_SHEET_KEY`, la fonction répond « non réglée » et le visiteur voit le bouton « Réessayer l'envoi » : testez toujours une vraie demande avant de lancer les annonces.

## Mesure des annonces

- **Avant l'accord du visiteur, rien ne se charge.** Ni le pixel Meta (PageView compris) ni la balise Google : c'est une obligation de la CNIL pour les traceurs publicitaires.
- **L'identifiant de clic est lu dans l'adresse de la page**, sans cookie, et part avec la demande. C'est lui qui relie la demande à l'annonce.
- **À l'envoi du formulaire, la fonction envoie l'événement `Lead` à l'API Conversions de Meta**, si le visiteur a accepté les cookies ou coché la case facultative de la dernière étape. La case n'apparaît qu'au visiteur venu d'une annonce qui n'a pas accepté les cookies. Meta reçoit l'identifiant du clic, l'heure, l'adresse de la page, l'adresse IP et le navigateur : jamais le prénom ni le téléphone.
- **Si le visiteur a accepté les cookies**, le pixel envoie aussi `PageView` et `Lead`, avec le même identifiant que l'API : Meta ne compte la demande qu'une fois. La balise Google envoie la conversion au même moment.
- **Les demandes qualifiées** (colonne « Suivi ») pourront être déclarées ensuite à Google (Data Manager, avec le `gclid`) et à Meta, seulement pour les lignes dont l'accord vaut « Oui ».
- Dans le Gestionnaire d'événements de Meta, désactivez la « correspondance avancée automatique » du pixel du client : la page promet que ni le nom ni le numéro ne sont transmis.

## Tests

```bash
node --test tests/*.test.js
```

Ils vérifient la fonction `/api/lead/` : ligne écrite, `Lead` envoyé à Meta seulement avec accord et sans données personnelles, refus d'un autre site, champ piège, champs invalides, panne du tableau ou de Meta.

## Le parcours

Sur téléphone, le haut de page est centré : la zone, une accroche en surligné jaune posée comme une question (« Tuiles cassées, fuite, mousse sur le toit ? »), le titre, une phrase et le bouton vert. Le questionnaire suit directement, et sa première réponse est visible sans faire défiler. Les réponses s'affichent en liste, un dessin à gauche, le libellé à droite. L'exemple d'estimation, la carte de la personne qui rappelle et la source des prix passent sous le questionnaire. Une fois lancé, il occupe tout l'écran : la progression reste en haut et le bouton « Suivant » en bas, à portée du pouce. Sur ordinateur, le titre est à gauche et le questionnaire à droite, sans clic de plus.

Chaque option a sa propre illustration du chantier (mousse sur le toit, tuile manquante, façade à moitié repeinte, panneaux d'isolant…), et la tuile passe à la question suivante dès qu'on la touche. Les surfaces et les quantités se règlent avec un curseur et des boutons − et +. Le code postal affiche le nom de la commune grâce à l'API publique de l'État (geo.api.gouv.fr) ; hors des départements du client, la page prévient le visiteur sans le bloquer. Vers la fin, le compteur laisse place à « Plus que 3 étapes », « Avant-dernière étape », puis « Dernière étape ».

À la dernière étape, l'estimation reste floutée jusqu'au numéro, qui se met en forme pendant la saisie. Il n'y a pas de case à cocher : une phrase d'information la remplace (« En validant, vous acceptez d'être rappelé… »), ce qui fait un champ obligatoire de moins. La demande vient du visiteur lui-même, et cela suffit pour le rappeler. L'estimation s'affiche ensuite comme un devis au nom de l'artisan, puis, avec `boutons_appel` et `whatsapp`, le visiteur est invité à envoyer des photos du chantier par WhatsApp. Si la page se recharge (fréquent dans le navigateur d'Instagram après un passage par WhatsApp), le visiteur retrouve ses réponses et son estimation ; elles s'effacent quand il ferme l'onglet. Il peut aussi partager l'estimation (au conjoint, au propriétaire) depuis son téléphone. Sous le questionnaire, une foire aux questions répond aux hésitations : gratuité, origine des prix, prix final, qui rappelle, locataires, et une question propre au métier. Tout en bas, un dernier encadré relance l'estimation (le bouton remonte au formulaire) et, avec `boutons_appel`, propose d'appeler l'artisan, pour le visiteur qui a tout lu sans se décider.

## Ce que nous faisons, nos spécialités

Sous le questionnaire, deux sections présentent l'artisan, comme sur une page de couvreur classique.

« Ce que nous faisons » liste ses métiers avec une coche verte (plus les lignes du champ `prestations`), puis la personne qui intervient : photo ou initiales, prénom, rôle, entreprise et horaires.

« Nos spécialités » montre une carte par type de travaux du questionnaire : une photo, une phrase, trois points qui décrivent le travail, puis le prix. Le prix est le tarif du client s'il l'a donné (`tarifs`), sinon le prix moyen publié, sinon « se chiffre sur place ». Le lien « Estimer ce projet » coche ce projet dans le questionnaire et y descend directement.

Les textes des cartes sont dans `prestations.py`. Ils décrivent le travail sans rien promettre (délai, garantie, qualification) : relisez-les avec l'artisan et ajustez-les à sa façon de travailler avant de publier sa page.

## Les photos

Chaque carte de « Nos spécialités » a sa photo. Par défaut, ce sont des photos libres de droits (voir `photos/SOURCES.md` : licences Unsplash et Pexels, usage commercial gratuit), avec la mention « Photos d'illustration du métier » sous le titre de la section. Elles ne montrent pas les chantiers de l'artisan et ne doivent jamais être présentées comme tels. Le choix des photos par carte est dans `prestations.py` (`PHOTOS`) ; une carte sans photo garde le dessin du projet.

Dès que l'artisan fournit une photo de ses chantiers pour un type de travaux, mettez-la dans sa fiche, champ `photos_prestations`, rangée par métier puis par projet : `{"toiture": {"Nettoyage et démoussage": "photos/demoussage.jpg"}}`. Elle remplace la photo d'illustration de cette carte. Quand toutes les cartes ont leur vraie photo, la mention « Photos d'illustration » disparaît.

Pour une galerie de ses chantiers, utilisez le champ `realisations` : une section « Les chantiers de [entreprise] » s'ajoute sous les cartes, à faire défiler du doigt sur téléphone. Les légendes ne s'affichent pas : elles servent de texte de remplacement aux lecteurs d'écran. Sans `realisations`, cette section n'apparaît pas. Dans tous les cas, retirez d'abord les métadonnées des photos (lieu, date, appareil).

Sur téléphone, un encadré compact donne l'exemple d'estimation, sous le questionnaire. Sur ordinateur, la grande maison dessinée du métier porte cet exemple, sous le titre.

## La zone d'intervention

Sous les cartes, une section reprend la promesse de rappel (champ `rappel`), le rayon (« Nous intervenons dans un rayon de 30 km autour de Lille (59) »), les horaires et un bouton « Parler à un couvreur » (menuisier, façadier, charpentier ou artisan selon la page) qui appelle l'artisan (sans `boutons_appel`, ce bouton relance l'estimation). En dessous, une carte montre la zone : un cercle du rayon indiqué autour de la commune.

La carte est le Plan IGN (données publiques, Licence Ouverte 2.0 : usage commercial libre en citant « © IGN », ce que font la carte et les mentions légales). Elle est dessinée une fois, à la génération, et publiée comme une simple image de 60 Ko environ : le navigateur du visiteur n'appelle aucun service de cartes, il n'y a donc ni cookie ni consentement à demander. La génération a besoin d'internet la première fois pour une commune donnée ; la carte est ensuite gardée dans `.cache/`.

Le contrôle de zone du questionnaire utilise la même distance : à partir du code postal, la page calcule la distance entre la commune du visiteur et celle de l'artisan. Au-delà du rayon (plus 5 km de marge), le visiteur est prévenu que son chantier semble hors zone, sans être bloqué.

Sur téléphone, un bouton « Calculer mon prix » reste en bas de l'écran quand le visiteur fait défiler les photos, la carte ou les questions. Il disparaît dès que le questionnaire, le haut ou le bas de la page sont à l'écran, et pour de bon une fois l'estimation affichée.

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
- Tester l'envoi : une vraie demande doit arriver en ligne dans l'onglet du client.
- Avec Meta : ouvrir la page avec `?fbclid=test` et `META_TEST_EVENT_CODE` réglé, envoyer une demande en cochant la case, vérifier le `Lead` dans « Tester les événements », puis retirer le code.
- Relire les mentions légales et la confidentialité avec les informations du client.

# Formulaire de démarrage des clients

Un formulaire Google Forms à envoyer au client avant l'appel de lancement. Il recueille tout ce qu'il faut pour fabriquer sa page d'estimation (`lp-estimation`) et préparer ses annonces. L'appel sert ensuite à parler de ses objectifs.

20 questions, dont 11 obligatoires, en 3 parties. Comptez cinq minutes pour le client. Il peut revenir modifier ses réponses avec le lien qu'il reçoit après l'envoi.

Les mentions légales ne sont pas demandées : raison sociale, forme juridique, capital, siège, immatriculation, numéro de TVA et dirigeant se retrouvent à partir du SIRET dans l'annuaire officiel des entreprises ([annuaire-entreprises.data.gouv.fr](https://annuaire-entreprises.data.gouv.fr)). Les objectifs, les prestations à mettre en avant, les chantiers refusés, les tarifs et la façon de recevoir les demandes se voient à l'appel.

## Le formulaire en ligne

Créé le 23/11/2026 avec le compte adminbartier@gmail.com.

- **Lien à envoyer aux clients :** https://docs.google.com/forms/d/e/1FAIpQLSeGF6tEZCbA7OYP6rGWO_vq22b_bZcUwqyhfMkvVGXXdne1_g/viewform
- Modifier le formulaire (compte Bartier & Co) : https://docs.google.com/forms/d/1p7cqQ4Z9y547aWU6j1aVfuDXidrq5mIVxqMn7BMPMU0/edit
- Tableau des réponses (compte Bartier & Co) : https://docs.google.com/spreadsheets/d/1dif9ll05_BAjlnS4QFcyh_pecmD6ixpg5ZQoMMeXUxQ/edit

## Le créer (une seule fois, environ 2 minutes)

Avec le compte Google de Bartier & Co (adminbartier@gmail.com) :

1. Ouvrez [script.google.com](https://script.google.com), puis **Nouveau projet**.
2. Collez le contenu de `formulaire-demarrage.gs` à la place du code présent, puis enregistrez.
3. En haut, choisissez la fonction `creerFormulaire`, puis **Exécuter**. Google demande l'autorisation de créer un formulaire et un tableau : acceptez.
4. En bas, le **journal d'exécution** affiche trois adresses :
   - le lien à envoyer aux clients ;
   - l'adresse pour modifier le formulaire ;
   - le tableau des réponses, « Bartier & Co, formulaires de démarrage (réponses) ».

Si le lien client affiche « Ce formulaire n'accepte plus de réponses », ouvrez l'adresse de modification et cliquez sur **Publier**.

Ne relancez pas le script : chaque exécution crée un nouveau formulaire. Pour changer une question, modifiez directement le formulaire dans Google Forms.

## Ce que demande le formulaire

| Partie | Questions |
|---|---|
| Vous et votre entreprise | Prénom et nom, téléphone, e-mail (aussi affiché dans les mentions légales), nom affiché, SIRET (14 chiffres vérifiés), décennale, médiateur de la consommation, qualifications |
| Votre activité | Métiers, ville de départ, rayon en km, qui rappelle, délai de rappel tenu, jours et heures de rappel |
| Vos photos et vos liens | Lien des photos, fiche Google, site, page Facebook, numéro Google Ads, remarques (tout est facultatif) |

Le logo et les photos arrivent à part, par WhatsApp (07 81 01 89 36), par e-mail (contact@bartierandco.com) ou par un lien de partage. Un formulaire Google ne peut recevoir des fichiers que si le client se connecte à un compte Google : c'est une friction qu'on évite.

## De la réponse à la fiche client

| Question du formulaire | Champ de `lp-estimation/clients/<client>.json` |
|---|---|
| Nom de l'entreprise affiché | `entreprise` (et `slug`, en minuscules avec des tirets) |
| Numéro SIRET | `legal.siret`, puis dans l'annuaire des entreprises : `legal.raison_sociale`, `legal.forme`, `legal.capital`, `legal.siege`, `legal.rcs`, `legal.tva`, `legal.directeur_publication` (le dirigeant, à confirmer à l'appel) |
| Votre e-mail | `legal.email` |
| Votre téléphone | `telephone` (mentions légales seulement) |
| Assurance décennale | `legal.assurance_decennale` |
| Médiateur de la consommation | `legal.mediateur` |
| Qualifications et labels | `atouts` (seulement ce qui est prouvé) |
| Vos métiers | `metiers` : `toiture`, `facade`, `fenetres`, `charpente`, `isolation` |
| Ville d'où vous partez, rayon | `ville`, `rayon_km` (les départements se déduisent de la carte) |
| Qui rappelle | `contact.prenom`, `contact.role` (photo : `contact.photo`) |
| Délai de rappel | `rappel` (ex. « Rappel sous 24 h ouvrées ») |
| Jours et heures de rappel | `horaires` |
| Lien de la fiche Google | `avis.lien`, puis `avis.note` et `avis.nombre` relevés sur la fiche |
| Logo, photos de chantiers | `logo`, `realisations`, `photos_prestations` |

Restent à remplir par vous : `domaine` (le domaine acheté au nom du client), `meta_pixel`, `google_ads`, `accent` (la couleur, prise sur le logo) et `"envoi": "tableau"`.

# Formulaire de démarrage des clients

Un formulaire Google Forms à envoyer au client avant l'appel de lancement. Il recueille tout ce qu'il faut pour fabriquer sa page d'estimation (`lp-estimation`) et préparer ses annonces. L'appel sert ensuite à parler de ses objectifs.

40 questions, dont 24 obligatoires, en 9 parties (la dernière est la confirmation). Comptez une dizaine de minutes pour le client. Il peut revenir modifier ses réponses avec le lien qu'il reçoit après l'envoi.

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
| Vous | Prénom et nom, téléphone, e-mail |
| Votre entreprise | Nom affiché, raison sociale, forme juridique, capital, siège, SIRET (14 chiffres vérifiés), immatriculation, TVA, responsable de la publication, e-mail des mentions légales |
| Assurance et qualifications | Décennale (assureur et numéro), médiateur de la consommation, qualifications (RGE, Qualibat…) |
| Votre activité | Métiers, autres prestations, ville de départ, rayon en km, départements, chantiers refusés, tarifs indicatifs |
| Le rappel des demandes | Qui rappelle, délai tenu, jours et heures, comment recevoir les demandes |
| Vos photos et vos avis | Mode d'envoi du logo et des photos, lien de partage, lien de la fiche Google |
| Votre présence en ligne | Site, page Facebook, compte Google Ads et son numéro |
| Vos objectifs | Chantiers en plus par mois, périodes complètes, remarques |

Le logo et les photos arrivent à part, par WhatsApp (07 81 01 89 36), par e-mail (contact@bartierandco.com) ou par un lien de partage. Un formulaire Google ne peut recevoir des fichiers que si le client se connecte à un compte Google : c'est une friction qu'on évite.

## De la réponse à la fiche client

| Question du formulaire | Champ de `lp-estimation/clients/<client>.json` |
|---|---|
| Nom de l'entreprise affiché | `entreprise` (et `slug`, en minuscules avec des tirets) |
| Raison sociale, forme, capital, siège, SIRET, immatriculation, TVA | `legal.raison_sociale`, `legal.forme`, `legal.capital`, `legal.siege`, `legal.siret`, `legal.rcs`, `legal.tva` |
| Responsable de la publication | `legal.directeur_publication` |
| E-mail des mentions légales | `legal.email` |
| Assurance décennale | `legal.assurance_decennale` |
| Médiateur de la consommation | `legal.mediateur` |
| Qualifications et labels | `atouts` (seulement ce qui est prouvé) |
| Vos métiers | `metiers` : `toiture`, `facade`, `fenetres`, `charpente`, `isolation` |
| Autres prestations | `prestations` |
| Ville d'où vous partez, rayon, départements | `ville`, `rayon_km`, `departements` |
| Tarifs indicatifs | `tarifs` (fourchette par option, dans l'unité de la page) |
| Qui rappelle | `contact.prenom`, `contact.role` (photo : `contact.photo`) |
| Délai de rappel | `rappel` (ex. « Rappel sous 24 h ouvrées ») |
| Jours et heures de rappel | `horaires` |
| Lien de la fiche Google | `avis.lien`, puis `avis.note` et `avis.nombre` relevés sur la fiche |
| Téléphone de l'entreprise | `telephone` (mentions légales seulement) |
| Logo, photos de chantiers | `logo`, `realisations`, `photos_prestations` |

Restent à remplir par vous : `domaine` (le domaine acheté au nom du client), `meta_pixel`, `google_ads`, `accent` (la couleur, prise sur le logo) et `"envoi": "tableau"`.

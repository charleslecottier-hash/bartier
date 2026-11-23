/**
 * Bartier & Co : crée le formulaire Google Forms « démarrage de votre campagne », à envoyer au client
 * avant l'appel de lancement, et le tableau de ses réponses.
 *
 * À lancer UNE SEULE FOIS, avec le compte Google de Bartier & Co (adminbartier@gmail.com) :
 *   1. Ouvrez script.google.com, Nouveau projet.
 *   2. Collez ce fichier à la place du code présent, puis Enregistrer.
 *   3. Choisissez la fonction creerFormulaire, puis Exécuter. Autorisez l'accès demandé (Forms et Sheets).
 *   4. Le journal d'exécution affiche trois adresses : le lien à envoyer aux clients, l'édition du formulaire
 *      et le tableau des réponses.
 *
 * Chaque question reprend un champ de la fiche client des pages d'estimation (lp-estimation/clients/<client>.json) :
 * la correspondance est dans onboarding/README.md.
 */

var CONTACT_TEL = '07 81 01 89 36';
var CONTACT_MAIL = 'contact@bartierandco.com';

function creerFormulaire() {
  var form = FormApp.create('Bartier & Co : démarrage de votre campagne');
  form.setDescription(
    'Ce formulaire prend environ 10 minutes. Vos réponses nous servent à préparer votre page et vos annonces avant notre appel de lancement : ' +
    'nous gagnons du temps, et l’appel sert à parler de vos objectifs.\n\n' +
    'Gardez sous la main votre Kbis ou votre avis de situation au répertoire SIRENE, et votre attestation d’assurance décennale.\n\n' +
    'Vous pouvez revenir modifier vos réponses avec le lien reçu après l’envoi. Une question ? ' + CONTACT_TEL + ' ou ' + CONTACT_MAIL + '.');
  form.setProgressBar(true);
  try { form.setCollectEmail(false); } catch (e) { /* réglage retiré par Google : sans effet */ }
  form.setAllowResponseEdits(true);
  form.setShowLinkToRespondAgain(false);
  form.setConfirmationMessage(
    'Merci, c’est bien reçu. Nous préparons votre page et revenons vers vous pour l’appel de lancement. ' +
    'Si ce n’est pas déjà fait, envoyez-nous votre logo et vos photos de chantiers par WhatsApp au ' + CONTACT_TEL + ' ou par e-mail à ' + CONTACT_MAIL + '.');

  /* ——— 1. Vous ——— */
  texte(form, 'Votre prénom et votre nom', '', true);
  texte(form, 'Votre téléphone', 'Pour vous joindre pendant la mise en place.', true, telephone());
  texte(form, 'Votre e-mail', '', true, FormApp.createTextValidation().requireTextIsEmail().setHelpText('Indiquez une adresse e-mail valide.').build());

  /* ——— 2. Votre entreprise ——— */
  section(form, 'Votre entreprise', 'Ces informations figurent dans les mentions légales de votre page. Recopiez-les exactement comme sur votre Kbis ou votre avis de situation.');
  texte(form, 'Nom de l’entreprise affiché sur la page et dans les annonces', 'Le nom que vos clients connaissent. Par exemple : Dupont Toiture.', true);
  texte(form, 'Raison sociale', 'Le nom officiel, s’il est différent. Par exemple : SARL Dupont et Fils.', true);
  liste(form, 'Forme juridique', ['Entreprise individuelle (dont micro-entreprise)', 'EURL', 'SARL', 'SASU', 'SAS', 'Autre'], true);
  texte(form, 'Capital social', 'Pour une société seulement. Par exemple : 10 000 €.', false);
  texte(form, 'Adresse du siège', 'Numéro, rue, code postal et ville.', true);
  texte(form, 'Numéro SIRET', '14 chiffres.', true, FormApp.createTextValidation()
    .requireTextMatchesPattern('^\\s*([0-9]\\s*){14}$').setHelpText('Le SIRET compte 14 chiffres.').build());
  texte(form, 'Immatriculation', 'Si vous êtes inscrit : RCS ou Répertoire des métiers, avec la ville. Par exemple : RCS Lille Métropole, ou RM 59.', false);
  texte(form, 'Numéro de TVA intracommunautaire', 'Si vous en avez un.', false);
  texte(form, 'Responsable de la publication du site', 'La personne responsable du contenu de la page, en général le gérant. Prénom et nom.', true);
  texte(form, 'E-mail de contact affiché dans les mentions légales', 'Les visiteurs peuvent vous écrire à cette adresse (par exemple pour leurs données personnelles).', true,
    FormApp.createTextValidation().requireTextIsEmail().setHelpText('Indiquez une adresse e-mail valide.').build());

  /* ——— 3. Assurance, médiation, qualifications ——— */
  section(form, 'Assurance et qualifications', 'Nous n’affichons que ce que vous pouvez prouver.');
  texte(form, 'Assurance décennale : assureur et numéro de contrat', 'Par exemple : MAAF, contrat n° 123456789.', true);
  texte(form, 'Médiateur de la consommation', 'Le nom de votre médiateur, obligatoire pour travailler avec des particuliers. Si vous n’en avez pas, laissez vide : nous en parlerons à l’appel.', false);
  cases(form, 'Qualifications et labels', 'Cochez seulement ceux qui sont valides aujourd’hui.', ['RGE', 'Qualibat', 'Artisan (Chambre de métiers)', 'Aucun pour l’instant'], false, true);

  /* ——— 4. Votre activité ——— */
  section(form, 'Votre activité', '');
  cases(form, 'Vos métiers', 'Une page est préparée pour chaque métier coché.',
    ['Toiture et couverture', 'Façade et ravalement', 'Fenêtres et portes', 'Charpente', 'Isolation'], true, true);
  paragraphe(form, 'Autres prestations à mettre en avant', 'Une par ligne. Par exemple : zinguerie et gouttières, étanchéité de toit-terrasse.', false);
  texte(form, 'Ville d’où vous partez', 'Le centre de votre zone d’intervention.', true);
  texte(form, 'Rayon d’intervention, en kilomètres', 'Par exemple : 30.', true, FormApp.createTextValidation()
    .requireNumberBetween(1, 200).setHelpText('Indiquez un nombre de kilomètres, entre 1 et 200.').build());
  texte(form, 'Départements couverts', 'Par exemple : 59, 62.', false);
  paragraphe(form, 'Les chantiers que vous ne voulez pas', 'Trop petits, trop loin, certains travaux : nous filtrerons les annonces et les questions en conséquence.', false);
  paragraphe(form, 'Vos tarifs indicatifs (facultatif)',
    'Si vous voulez que l’estimation de la page utilise vos prix : une fourchette par type de travaux, pose comprise. Par exemple : démoussage 20 à 30 €/m², réfection de toiture 90 à 160 €/m². Sinon, la page utilise des prix moyens publiés, avec leur source.', false);

  /* ——— 5. Le rappel des prospects ——— */
  section(form, 'Le rappel des demandes', 'Ces informations sont affichées sur la page. Indiquez ce que vous tenez vraiment.');
  texte(form, 'Qui rappelle les demandes ?', 'Prénom et rôle. Par exemple : Julien, gérant.', true);
  liste(form, 'Délai de rappel que vous tenez', ['Dans l’heure', 'Dans la journée', 'Sous 24 h ouvrées', 'Sous 48 h ouvrées'], true);
  texte(form, 'Jours et heures de rappel', 'Par exemple : du lundi au vendredi, 8 h à 18 h.', true);
  cases(form, 'Comment voulez-vous recevoir les nouvelles demandes ?', '', ['SMS', 'WhatsApp', 'E-mail', 'Appel'], true, false);

  /* ——— 6. Vos photos et vos avis ——— */
  section(form, 'Vos photos et vos avis',
    'Ce sont eux qui donnent confiance aux visiteurs. Envoyez-nous :\n' +
    '• votre logo, si vous en avez un ;\n' +
    '• 10 à 20 photos de vos vrais chantiers, avant et après si possible (pas de photos trouvées sur internet) ;\n' +
    '• une photo de la personne qui rappelle (facultatif, mais elle rassure).\n\n' +
    'Par WhatsApp au ' + CONTACT_TEL + ', par e-mail à ' + CONTACT_MAIL + ', ou avec un lien de partage ci-dessous.');
  choix(form, 'Comment nous envoyez-vous votre logo et vos photos ?', ['WhatsApp', 'E-mail', 'Lien de partage (ci-dessous)', 'Je n’en ai pas encore'], true);
  texte(form, 'Lien de partage de vos photos', 'Google Drive, WeTransfer ou autre. Facultatif.', false);
  texte(form, 'Lien de votre fiche Google (Google Maps)', 'Pour afficher votre note et vos avis. Facultatif.', false);

  /* ——— 7. Votre présence en ligne ——— */
  section(form, 'Votre présence en ligne', '');
  choix(form, 'Avez-vous un site internet ?', ['Oui', 'Non'], true);
  texte(form, 'Adresse de votre site', 'Si vous en avez un.', false);
  choix(form, 'Avez-vous une page Facebook pour votre entreprise ?', ['Oui', 'Non', 'Je ne sais pas'], true);
  texte(form, 'Lien de votre page Facebook ou Instagram', 'Si vous en avez une.', false);
  choix(form, 'Avez-vous déjà un compte Google Ads ?', ['Oui', 'Non', 'Je ne sais pas'], true);
  texte(form, 'Numéro de votre compte Google Ads', '10 chiffres, en haut à droite de Google Ads (par exemple 123-456-7890). Si vous en avez un.', false,
    FormApp.createTextValidation().requireTextMatchesPattern('^\\s*[0-9]{3}[-\\s]?[0-9]{3}[-\\s]?[0-9]{4}\\s*$').setHelpText('Le numéro compte 10 chiffres, par exemple 123-456-7890.').build());

  /* ——— 8. Vos objectifs ——— */
  section(form, 'Vos objectifs', '');
  liste(form, 'Combien de chantiers en plus pouvez-vous prendre par mois ?', ['1 à 2', '3 à 5', '6 à 10', 'Plus de 10'], true);
  paragraphe(form, 'Vos périodes complètes ou de congés', 'Pour mettre les annonces en pause au bon moment. Par exemple : août, ou carnet plein jusqu’en mars.', false);
  paragraphe(form, 'Autre chose à nous dire ?', '', false);

  /* ——— 9. Envoi ——— */
  section(form, 'Envoi',
    'Vos informations. Bartier & Co (SAS en cours d’immatriculation, 6 rue Saint-Bon, 75004 Paris) utilise vos réponses pour préparer et gérer votre campagne : ' +
    'votre page, vos annonces et le suivi des demandes. Elles ne sont ni vendues ni cédées. Elles sont gardées pendant notre collaboration, puis trois ans. ' +
    'Vous pouvez y accéder, les corriger ou les faire effacer en écrivant à ' + CONTACT_MAIL + '. En cas de difficulté, vous pouvez saisir la CNIL (cnil.fr).');
  cases(form, 'Confirmation', '', ['Je confirme que ces informations sont exactes'], true, false);

  /* ——— Tableau des réponses ——— */
  var ss = SpreadsheetApp.create('Bartier & Co, formulaires de démarrage (réponses)');
  form.setDestination(FormApp.DestinationType.SPREADSHEET, ss.getId());
  try { form.setPublished(true); } catch (e) { /* ancienne version de Forms : déjà publié */ }

  Logger.log('Lien à envoyer aux clients : ' + form.getPublishedUrl());
  Logger.log('Modifier le formulaire : ' + form.getEditUrl());
  Logger.log('Tableau des réponses : ' + ss.getUrl());
}

/* ——— Outils ——— */

function section(form, titre, aide) {
  var p = form.addPageBreakItem().setTitle(titre);
  if (aide) p.setHelpText(aide);
  return p;
}

function texte(form, titre, aide, obligatoire, validation) {
  var i = form.addTextItem().setTitle(titre).setRequired(obligatoire);
  if (aide) i.setHelpText(aide);
  if (validation) i.setValidation(validation);
  return i;
}

function paragraphe(form, titre, aide, obligatoire) {
  var i = form.addParagraphTextItem().setTitle(titre).setRequired(obligatoire);
  if (aide) i.setHelpText(aide);
  return i;
}

function liste(form, titre, valeurs, obligatoire) {
  return form.addListItem().setTitle(titre).setChoiceValues(valeurs).setRequired(obligatoire);
}

function choix(form, titre, valeurs, obligatoire) {
  return form.addMultipleChoiceItem().setTitle(titre).setChoiceValues(valeurs).setRequired(obligatoire);
}

function cases(form, titre, aide, valeurs, obligatoire, autre) {
  var i = form.addCheckboxItem().setTitle(titre).setChoiceValues(valeurs).setRequired(obligatoire);
  if (aide) i.setHelpText(aide);
  if (autre) i.showOtherOption(true);
  return i;
}

// Téléphone français : 06 12 34 56 78, +33 6 12 34 56 78, avec espaces, points ou tirets.
function telephone() {
  return FormApp.createTextValidation()
    .requireTextMatchesPattern('^\\s*(\\+33|0033|0)\\s*[1-9]([\\s.-]*[0-9]){8}\\s*$')
    .setHelpText('Indiquez un numéro français, par exemple 06 12 34 56 78.').build();
}

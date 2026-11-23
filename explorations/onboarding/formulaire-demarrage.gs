/**
 * Bartier & Co : crée le formulaire Google Forms « démarrage de votre campagne », à envoyer au client
 * avant l'appel de lancement, et le tableau de ses réponses.
 *
 * À lancer UNE SEULE FOIS, avec le compte Google de Bartier & Co (adminbartier@gmail.com) :
 *   1. Ouvrez script.google.com, Nouveau projet.
 *   2. Effacez tout le code présent, collez ce fichier, puis Enregistrer.
 *   3. Choisissez la fonction creerFormulaire, puis Exécuter. Autorisez l'accès demandé (Forms et Sheets).
 *   4. Le journal d'exécution affiche trois adresses : le lien à envoyer aux clients, l'édition du formulaire
 *      et le tableau des réponses.
 *
 * Version courte : 20 questions, dont 11 obligatoires. Les mentions légales (raison sociale, forme, capital,
 * siège, immatriculation, TVA, dirigeant) se retrouvent à partir du SIRET dans l'annuaire officiel des entreprises.
 * Correspondance avec la fiche client : onboarding/README.md.
 */

var CONTACT_TEL = '07 81 01 89 36';
var CONTACT_MAIL = 'contact@bartierandco.com';

function creerFormulaire() {
  var form = FormApp.create('Bartier & Co : démarrage de votre campagne');
  form.setDescription(
    'Cinq minutes pour préparer votre page et vos annonces avant notre appel de lancement.\n\n' +
    'Une question ? ' + CONTACT_TEL + ' ou ' + CONTACT_MAIL + '.');
  form.setProgressBar(true);
  try { form.setCollectEmail(false); } catch (e) { /* réglage retiré par Google : sans effet */ }
  form.setAllowResponseEdits(true);
  form.setShowLinkToRespondAgain(false);
  form.setConfirmationMessage(
    'Merci, c’est bien reçu. Nous préparons votre page et revenons vers vous pour l’appel de lancement. ' +
    'Si ce n’est pas déjà fait, envoyez-nous votre logo et vos photos de chantiers par WhatsApp au ' + CONTACT_TEL + ' ou par e-mail à ' + CONTACT_MAIL + '.');

  /* ——— 1. Vous et votre entreprise ——— */
  texte(form, 'Votre prénom et votre nom', '', true);
  texte(form, 'Votre téléphone', '', true, telephone());
  texte(form, 'Votre e-mail', 'Il sera aussi affiché dans les mentions légales de votre page.', true,
    FormApp.createTextValidation().requireTextIsEmail().setHelpText('Indiquez une adresse e-mail valide.').build());
  texte(form, 'Nom de l’entreprise affiché sur la page et dans les annonces', 'Le nom que vos clients connaissent. Par exemple : Dupont Toiture.', true);
  texte(form, 'Numéro SIRET', '14 chiffres. Nous retrouvons le reste (raison sociale, siège, forme juridique) dans l’annuaire officiel des entreprises.', true,
    FormApp.createTextValidation().requireTextMatchesPattern('^\\s*([0-9]\\s*){14}$').setHelpText('Le SIRET compte 14 chiffres.').build());
  texte(form, 'Assurance décennale : assureur et numéro de contrat', 'Facultatif. Par exemple : MAAF, contrat n° 123456789.', false);
  texte(form, 'Médiateur de la consommation', 'Facultatif. Si vous n’en avez pas, nous en parlerons à l’appel.', false);
  cases(form, 'Qualifications et labels', 'Facultatif. Cochez seulement ceux qui sont valides aujourd’hui.', ['RGE', 'Qualibat'], false, true);

  /* ——— 2. Votre activité et le rappel des demandes ——— */
  section(form, 'Votre activité', 'Ces informations sont affichées sur la page. Indiquez ce que vous tenez vraiment.');
  cases(form, 'Vos métiers', 'Une page est préparée pour chaque métier coché.',
    ['Toiture et couverture', 'Façade et ravalement', 'Fenêtres et portes', 'Charpente', 'Isolation'], true, true);
  texte(form, 'Ville d’où vous partez', '', true);
  texte(form, 'Rayon d’intervention, en kilomètres', 'Par exemple : 30.', true, FormApp.createTextValidation()
    .requireNumberBetween(1, 200).setHelpText('Indiquez un nombre de kilomètres, entre 1 et 200.').build());
  texte(form, 'Qui rappelle les demandes ?', 'Prénom et rôle. Par exemple : Julien, gérant.', true);
  liste(form, 'Délai de rappel que vous tenez', ['Dans l’heure', 'Dans la journée', 'Sous 24 h ouvrées', 'Sous 48 h ouvrées'], true);
  texte(form, 'Jours et heures de rappel', 'Par exemple : du lundi au vendredi, 8 h à 18 h.', true);

  /* ——— 3. Photos et présence en ligne ——— */
  section(form, 'Vos photos et vos liens',
    'Envoyez-nous votre logo et 10 à 20 photos de vos vrais chantiers (avant et après si possible), par WhatsApp au ' + CONTACT_TEL +
    ', par e-mail à ' + CONTACT_MAIL + ', ou avec un lien ci-dessous. Tout le reste de cette partie est facultatif.');
  texte(form, 'Lien de partage de vos photos', 'Google Drive, WeTransfer ou autre.', false);
  texte(form, 'Lien de votre fiche Google (Google Maps)', 'Pour afficher votre note et vos avis.', false);
  texte(form, 'Adresse de votre site internet', 'Si vous en avez un.', false);
  texte(form, 'Lien de votre page Facebook', 'Si vous en avez une.', false);
  texte(form, 'Numéro de votre compte Google Ads', 'Si vous en avez un : 10 chiffres, en haut à droite de Google Ads (par exemple 123-456-7890).', false,
    FormApp.createTextValidation().requireTextMatchesPattern('^\\s*[0-9]{3}[-\\s]?[0-9]{3}[-\\s]?[0-9]{4}\\s*$').setHelpText('Le numéro compte 10 chiffres, par exemple 123-456-7890.').build());
  paragraphe(form, 'Autre chose à nous dire ?',
    'Vos informations : Bartier & Co (SAS en cours d’immatriculation, 6 rue Saint-Bon, 75004 Paris) utilise vos réponses pour préparer et gérer votre campagne. ' +
    'Elles ne sont ni vendues ni cédées, et sont gardées pendant notre collaboration puis trois ans. Pour y accéder, les corriger ou les effacer : ' +
    CONTACT_MAIL + '. En cas de difficulté, vous pouvez saisir la CNIL (cnil.fr).', false);

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

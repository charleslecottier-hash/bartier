/** @OnlyCurrentDoc */

/**
 * Bartier & Co : reçoit les demandes des formulaires du site (via la fonction /api/lead) et les ajoute
 * en haut des onglets « Particuliers » et « Artisans » du tableau « Bartier & Co, demandes du site ».
 *
 * À coller dans le tableau : Extensions > Apps Script.
 * Déploiement : Déployer > Nouveau déploiement > Application Web, exécuter en tant que « Moi »,
 * accès « Tout le monde ». L'adresse /exec obtenue va dans LEAD_SHEET_URL sur Vercel.
 * La clé ci-dessous doit être identique à LEAD_SHEET_KEY sur Vercel. Ne la publiez nulle part.
 * À chaque demande, un e-mail part vers ALERTE (envoyé par le compte qui a déployé le script).
 * Après avoir collé une nouvelle version : lancez une fois testerAlerte (autorisation d'envoyer des e-mails),
 * puis Déployer > Gérer les déploiements > Modifier > Nouvelle version.
 */
var CLE = '@@CLE@@';

// Adresse(s) qui reçoivent une alerte à chaque demande, séparées par des virgules.
var ALERTE = 'adminbartier@gmail.com';

var METIERS = { couverture: 'Couverture et zinguerie', facade: 'Façade et ravalement', menuiserie: 'Menuiserie extérieure', charpente: 'Charpente', isolation: 'Isolation', autre: 'Autre métier' };
var TRAVAUX = { toiture: 'Toiture', facade: 'Façade', fenetres: 'Fenêtres et portes', charpente: 'Charpente', isolation: 'Isolation', autre: 'Autre projet' };
var CAPACITE = { oui: 'Oui, sans problème', bientot: 'Bientôt, ils recrutent', 'ne-sait-pas': 'Ne sait pas encore' };
var SUIVI = {
  Particuliers: ['À rappeler', 'Rappelé', 'Visite fixée', 'Devis remis', 'Travaux signés', 'Sans suite', 'Hors zone'],
  Artisans: ['À rappeler', 'Rappelé', 'Rendez-vous fixé', 'Client', 'Secteur déjà pris', 'Sans suite'],
};

function doPost(e) {
  try {
    var data = JSON.parse(e && e.postData ? e.postData.contents : '');
    if (!data || typeof data.cle !== 'string' || data.cle !== CLE) return reponse({ ok: false, error: 'cle' });
    var lead = data.lead || {};
    var f = lead.fields || {};
    var c = lead.consent || {};
    var artisan = lead.type === 'artisan';
    if (!artisan && lead.type !== 'particulier') return reponse({ ok: false, error: 'type' });

    var fin = [texte(lead.page), texte(lead.utm_source), texte(lead.utm_medium), texte(lead.utm_campaign), texte(lead.utm_content),
      texte(lead.gclid), texte(lead.fbclid), date(c.at), texte(c.text)];
    var ligne = artisan
      ? [date(lead.received_at), 'À rappeler', texte(f.entreprise), texte(f.prenom), tel(f.telephone), texte(f.email),
        texte(METIERS[f.metier] || f.metier), texte(f.code_postal), texte(f.chantier_moyen),
        texte(CAPACITE[f.capacite] || f.capacite), ''].concat(fin)
      : [date(lead.received_at), 'À rappeler', texte(f.prenom), tel(f.telephone), texte(f.code_postal),
        texte(TRAVAUX[f.travaux] || f.travaux), texte(f.besoin), texte(f.delai), texte(f.statut), ''].concat(fin);

    var nom = artisan ? 'Artisans' : 'Particuliers';
    var verrou = LockService.getScriptLock();
    verrou.waitLock(20000);
    try {
      var feuille = SpreadsheetApp.getActiveSpreadsheet().getSheetByName(nom);
      feuille.insertRowBefore(2);
      var r = feuille.getRange(2, 1, 1, ligne.length);
      r.setBackground(null).setFontWeight('normal').setFontColor('#000000').setVerticalAlignment('middle')
        .setWrapStrategy(SpreadsheetApp.WrapStrategy.CLIP).setNumberFormat('@');
      feuille.getRange(2, 1).setNumberFormat('dd/mm/yyyy hh:mm');
      feuille.getRange(2, ligne.length - 1).setNumberFormat('dd/mm/yyyy hh:mm:ss');
      r.setValues([ligne]);
      feuille.getRange(2, 2).setDataValidation(SpreadsheetApp.newDataValidation()
        .requireValueInList(SUIVI[nom], true).setAllowInvalid(true).build());
    } finally {
      verrou.releaseLock();
    }
    try { alerter(lead, artisan, feuille); } catch (err) { console.error('alerte non envoyée : ' + (err && err.message)); }
    return reponse({ ok: true });
  } catch (err) {
    console.error('demande non enregistrée : ' + (err && err.message));
    return reponse({ ok: false, error: 'script' });
  }
}

// E-mail d'alerte : la demande en clair, le numéro cliquable, le lien vers l'onglet.
function alerter(lead, artisan, feuille) {
  var a = String(ALERTE || '').split(',').map(function (x) { return x.trim(); })
    .filter(function (x) { return /^[^\s@<>,;]+@[^\s@<>,;]+\.[A-Za-z]{2,}$/.test(x); });
  if (!a.length) return;
  var f = lead.fields || {};
  var lignes, sujet, titre, consigne;
  if (artisan) {
    lignes = [['Entreprise', f.entreprise], ['Métier', METIERS[f.metier] || f.metier], ['Code postal du dépôt', f.code_postal],
      ['Chantier moyen', f.chantier_moyen], ['Chantiers en plus', CAPACITE[f.capacite] || f.capacite], ['E-mail', f.email]];
    sujet = 'Demande artisan : ' + [f.entreprise, METIERS[f.metier] || f.metier, f.code_postal].filter(Boolean).join(', ');
    titre = 'Nouvelle demande artisan (diagnostic secteur)';
    consigne = 'Rappel promis sous un jour ouvré, puis diagnostic secteur à préparer.';
  } else {
    lignes = [['Travaux', [TRAVAUX[f.travaux] || f.travaux, f.besoin].filter(Boolean).join(', ')], ['Délai', f.delai],
      ['Statut', f.statut], ['Code postal', f.code_postal]];
    sujet = 'Demande particulier : ' + [f.prenom, TRAVAUX[f.travaux] || f.travaux, f.code_postal].filter(Boolean).join(', ');
    titre = 'Nouvelle demande de travaux';
    consigne = 'Rappel promis en moins de 5 minutes, en semaine de 8 h à 19 h.';
  }
  lignes = lignes.concat([['Page', lead.page], ['Source', [lead.utm_source, lead.utm_campaign].filter(Boolean).join(' / ')]])
    .filter(function (l) { return l[1]; });
  var telF = tel(f.telephone);
  var lien = SpreadsheetApp.getActiveSpreadsheet().getUrl() + '#gid=' + feuille.getSheetId();
  var brut = titre + '\n\n' + f.prenom + '\n' + telF + '\n\n' +
    lignes.map(function (l) { return l[0] + ' : ' + l[1]; }).join('\n') + '\n\n' + consigne + '\n\nTableau : ' + lien;
  var html = '<div style="font-family:Arial,sans-serif;font-size:15px;line-height:1.5;color:#0A1424;max-width:560px">' +
    '<p style="margin:0 0 16px">' + h(titre) + ' sur bartierandco.com.</p>' +
    '<div style="padding:16px;border:1px solid #DCE1E8;border-radius:12px;margin:0 0 16px">' +
    '<p style="margin:0;font-size:18px"><b>' + h(f.prenom) + '</b></p>' +
    '<p style="margin:4px 0 0"><a href="tel:' + h(f.telephone) + '" style="color:#24489A;font-size:18px;text-decoration:none"><b>' + h(telF) + '</b></a></p></div>' +
    '<table style="border-collapse:collapse;width:100%">' + lignes.map(function (l) {
      return '<tr><td style="padding:6px 12px 6px 0;color:#5B6475;vertical-align:top;white-space:nowrap">' + h(l[0]) + '</td><td style="padding:6px 0">' + h(l[1]) + '</td></tr>';
    }).join('') + '</table>' +
    '<p style="margin:16px 0 0"><b>' + h(consigne) + '</b></p>' +
    '<p style="margin:16px 0 0"><a href="' + h(lien) + '" style="color:#24489A">Ouvrir le tableau des demandes</a></p></div>';
  var opts = { to: a.join(','), subject: sujet.slice(0, 200), body: brut, htmlBody: html, name: 'Bartier & Co, site' };
  if (artisan && /^[^\s@<>,;]+@[^\s@<>,;]+\.[A-Za-z]{2,}$/.test(String(f.email || ''))) opts.replyTo = String(f.email);
  MailApp.sendEmail(opts);
}

// À lancer une fois depuis l'éditeur (menu des fonctions, puis Exécuter) : autorise l'envoi d'e-mails et envoie un exemple.
function testerAlerte() {
  var feuille = SpreadsheetApp.getActiveSpreadsheet().getSheetByName('Artisans');
  alerter({ type: 'artisan', page: '/', utm_source: 'test', fields: { entreprise: 'TEST, exemple d’alerte', prenom: 'Jean', telephone: '+33612345678',
    email: '', metier: 'couverture', code_postal: '80000', chantier_moyen: '5 000 €', capacite: 'oui' } }, true, feuille);
}

function h(v) {
  return String(v == null ? '' : v).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
}

function doGet() {
  return reponse({ ok: true, service: 'Bartier & Co, demandes du site' });
}

function reponse(o) {
  return ContentService.createTextOutput(JSON.stringify(o)).setMimeType(ContentService.MimeType.JSON);
}

// Texte brut : rien n'est interprété comme une formule, un nombre ou une date (codes postaux à zéro initial compris).
function texte(v) {
  v = v == null ? '' : String(v).replace(/[\u0000-\u001F\u007F]/g, ' ').slice(0, 1000);
  return /^[=+\-@]/.test(v) ? "'" + v : v;
}

function date(v) {
  var d = v ? new Date(v) : null;
  return d && !isNaN(d.getTime()) ? d : '';
}

function tel(v) {
  var m = /^\+33([1-9])(\d{8})$/.exec(String(v || ''));
  return m ? '0' + m[1] + ' ' + m[2].replace(/(\d{2})(?=\d)/g, '$1 ').trim() : texte(v);
}

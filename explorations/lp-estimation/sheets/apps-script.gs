/** @OnlyCurrentDoc */

/**
 * Bartier & Co : reçoit les demandes des pages d'estimation des clients (via leur fonction /api/lead/)
 * et ajoute chaque demande en haut de l'onglet du client, dans le tableau « Bartier & Co, demandes clients ».
 * L'onglet est créé tout seul à la première demande d'un client. L'artisan reçoit aussitôt un e-mail avec la demande
 * (adresses du champ alerte_email de sa fiche), envoyé depuis le compte Google qui a déployé ce script.
 *
 * Mise en place (une seule fois, voir le README) :
 *   1. Dans le tableau : Extensions > Apps Script, collez ce fichier à la place du code présent.
 *   2. Remplacez @@CLE@@ par une clé longue (au moins 16 caractères, lettres et chiffres). Ne la publiez nulle part.
 *   3. Déployer > Nouveau déploiement > Application Web, exécuter en tant que « Moi », accès « Tout le monde ».
 *   4. L'adresse /exec obtenue va dans LEAD_SHEET_URL, et la clé dans LEAD_SHEET_KEY, sur le projet Vercel de chaque client.
 */
var CLE = '@@CLE@@';

// Facultatif : une adresse de Bartier & Co qui reçoit aussi une copie de chaque alerte (laisser vide sinon).
var COPIE = '';

var ENTETES = ['Reçue le', 'Suivi', 'Prénom', 'Téléphone', 'Code postal', 'Commune', 'Métier', 'Travaux', 'Quantité',
  'Estimation affichée', 'Détails', 'Délai', 'Statut', 'Accord mesure des annonces', 'Page',
  'utm_source', 'utm_medium', 'utm_campaign', 'utm_content', 'utm_term', 'gclid', 'gbraid', 'wbraid', 'fbclid',
  'ID de la demande', 'Phrase affichée', 'Envoyée le'];
var SUIVI = ['À rappeler', 'Rappelé', 'Qualifié', 'Visite fixée', 'Devis remis', 'Signé', 'Sans suite', 'Hors zone'];
var ACCORD = { cookies: 'Oui (cookies)', question: 'Oui (question)', non: 'Non', 'sans objet': 'Sans objet' };

function doPost(e) {
  try {
    var data = JSON.parse(e && e.postData ? e.postData.contents : '');
    if (!data || typeof data.cle !== 'string' || CLE.length < 16 || data.cle !== CLE) return reponse({ ok: false, error: 'cle' });
    var lead = data.lead || {};
    var f = lead.fields || {};
    var t = lead.tracking || {};
    var c = lead.consent || {};
    var nom = onglet(data.client);
    if (!nom) return reponse({ ok: false, error: 'client' });

    // Une même demande renvoyée (nouvel essai après une coupure) n'est écrite qu'une fois.
    var cache = CacheService.getScriptCache();
    var id = texte(lead.eid);
    if (id && cache.get('eid:' + id)) return reponse({ ok: true, doublon: true });

    var ligne = [date(lead.received_at), 'À rappeler', texte(f.prenom), tel(f.telephone), texte(f.code_postal), texte(f.commune),
      texte(lead.metier), texte(f.travaux), texte(f.quantite), texte(f.estimation), texte(f.details), texte(f.delai), texte(f.statut),
      texte(ACCORD[lead.accord] || 'Non'), texte(lead.page),
      texte(t.utm_source), texte(t.utm_medium), texte(t.utm_campaign), texte(t.utm_content), texte(t.utm_term),
      texte(t.gclid), texte(t.gbraid), texte(t.wbraid), texte(t.fbclid), id, texte(c.text), date(c.at)];

    var verrou = LockService.getScriptLock();
    verrou.waitLock(20000);
    try {
      var feuille = feuilleDe(nom);
      feuille.insertRowBefore(2);
      var r = feuille.getRange(2, 1, 1, ligne.length);
      r.setBackground(null).setFontWeight('normal').setFontColor('#000000').setVerticalAlignment('middle')
        .setWrapStrategy(SpreadsheetApp.WrapStrategy.CLIP).setNumberFormat('@');
      feuille.getRange(2, 1).setNumberFormat('dd/mm/yyyy hh:mm');
      feuille.getRange(2, ligne.length).setNumberFormat('dd/mm/yyyy hh:mm:ss');
      r.setValues([ligne]);
      feuille.getRange(2, 2).setDataValidation(SpreadsheetApp.newDataValidation()
        .requireValueInList(SUIVI, true).setAllowInvalid(true).build());
    } finally {
      verrou.releaseLock();
    }
    if (id) cache.put('eid:' + id, '1', 21600);
    try { alerter(data.alerte, nom, lead); } catch (err) { console.error('alerte non envoyée : ' + (err && err.message)); }
    return reponse({ ok: true });
  } catch (err) {
    console.error('demande non enregistrée : ' + (err && err.message));
    return reponse({ ok: false, error: 'script' });
  }
}

// E-mail à l'artisan : la demande en clair, le numéro cliquable. Une erreur d'envoi n'empêche jamais la ligne d'être écrite.
function alerter(adresses, client, lead) {
  var a = (Array.isArray(adresses) ? adresses : []).concat(COPIE ? [COPIE] : [])
    .map(function (x) { return String(x).trim(); })
    .filter(function (x) { return /^[^\s@<>,;]+@[^\s@<>,;]+\.[A-Za-z]{2,}$/.test(x); }).slice(0, 4);
  if (!a.length) return;
  var f = lead.fields || {};
  var lieu = [f.code_postal, f.commune].filter(Boolean).join(' ');
  var lignes = [['Travaux', lead.metier + (f.travaux ? ', ' + f.travaux : '')], ['Quantité', f.quantite], ['Estimation affichée', f.estimation],
    ['Détails', f.details], ['Délai', f.delai], ['Statut', f.statut]].filter(function (l) { return l[1]; });
  var telF = tel(f.telephone);
  var sujet = 'Nouvelle demande : ' + [f.prenom, lead.metier, lieu].filter(Boolean).join(', ');
  var texteBrut = 'Nouvelle demande d’estimation sur votre page ' + client + '.\n\n' + f.prenom + '\n' + telF + '\n' + lieu + '\n\n' +
    lignes.map(function (l) { return l[0] + ' : ' + l[1]; }).join('\n') + '\n\nRappelez dès que possible.\n\nEnvoyé automatiquement par Bartier & Co.';
  var html = '<div style="font-family:Arial,sans-serif;font-size:15px;line-height:1.5;color:#0A1424;max-width:560px">' +
    '<p style="margin:0 0 16px">Nouvelle demande d’estimation sur votre page <b>' + h(client) + '</b>.</p>' +
    '<div style="padding:16px;border:1px solid #DCE1E8;border-radius:12px;margin:0 0 16px">' +
    '<p style="margin:0;font-size:18px"><b>' + h(f.prenom) + '</b></p>' +
    '<p style="margin:4px 0"><a href="tel:' + h(f.telephone) + '" style="color:#2D5BE3;font-size:18px;text-decoration:none"><b>' + h(telF) + '</b></a></p>' +
    '<p style="margin:0;color:#5B6475">' + h(lieu) + '</p></div>' +
    '<table style="border-collapse:collapse;width:100%">' + lignes.map(function (l) {
      return '<tr><td style="padding:6px 12px 6px 0;color:#5B6475;vertical-align:top;white-space:nowrap">' + h(l[0]) + '</td><td style="padding:6px 0">' + h(l[1]) + '</td></tr>';
    }).join('') + '</table>' +
    '<p style="margin:16px 0 0"><b>Rappelez dès que possible.</b></p>' +
    '<p style="margin:24px 0 0;font-size:13px;color:#5B6475">Envoyé automatiquement par Bartier & Co.</p></div>';
  MailApp.sendEmail({ to: a.join(','), subject: sujet.slice(0, 200), body: texteBrut, htmlBody: html, name: 'Bartier & Co' });
}

function h(v) {
  return String(v == null ? '' : v).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
}

function doGet() {
  return reponse({ ok: true, service: 'Bartier & Co, demandes clients' });
}

// L'onglet du client : créé à la première demande, avec la ligne d'en-tête figée.
function feuilleDe(nom) {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var feuille = ss.getSheetByName(nom);
  if (feuille) return feuille;
  feuille = ss.insertSheet(nom);
  feuille.getRange(1, 1, 1, ENTETES.length).setValues([ENTETES]).setFontWeight('bold').setBackground('#F1F3F6');
  feuille.setFrozenRows(1);
  feuille.setColumnWidth(1, 130);
  feuille.setColumnWidth(2, 120);
  return feuille;
}

// Nom d'onglet : sans les caractères refusés par Sheets, 90 caractères au plus.
function onglet(v) {
  v = String(v == null ? '' : v).replace(/[\[\]:*?\/\\]/g, ' ').replace(/\s+/g, ' ').trim().slice(0, 90);
  return v;
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

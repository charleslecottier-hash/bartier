/** @OnlyCurrentDoc */

/**
 * Bartier & Co : reçoit les demandes des pages d'estimation des clients (via leur fonction /api/lead/)
 * et ajoute chaque demande en haut de l'onglet du client, dans le tableau « Bartier & Co, demandes clients ».
 * L'onglet est créé tout seul à la première demande d'un client.
 *
 * Mise en place (une seule fois, voir le README) :
 *   1. Dans le tableau : Extensions > Apps Script, collez ce fichier à la place du code présent.
 *   2. Remplacez @@CLE@@ par une clé longue (au moins 16 caractères, lettres et chiffres). Ne la publiez nulle part.
 *   3. Déployer > Nouveau déploiement > Application Web, exécuter en tant que « Moi », accès « Tout le monde ».
 *   4. L'adresse /exec obtenue va dans LEAD_SHEET_URL, et la clé dans LEAD_SHEET_KEY, sur le projet Vercel de chaque client.
 */
var CLE = '@@CLE@@';

var ENTETES = ['Reçue le', 'Suivi', 'Prénom', 'Téléphone', 'Code postal', 'Commune', 'Métier', 'Travaux', 'Quantité',
  'Estimation affichée', 'Détails', 'Délai', 'Statut', 'Accord mesure des annonces', 'Page',
  'utm_source', 'utm_medium', 'utm_campaign', 'utm_content', 'utm_term', 'gclid', 'gbraid', 'wbraid', 'fbclid',
  'ID de la demande', 'Phrase affichée', 'Envoyée le'];
var SUIVI = ['À rappeler', 'Rappelé', 'Qualifié', 'Visite fixée', 'Devis remis', 'Signé', 'Sans suite', 'Hors zone'];
var ACCORD = { cookies: 'Oui (cookies)', 'case': 'Oui (case cochée)', non: 'Non', 'sans objet': 'Sans objet' };

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
    return reponse({ ok: true });
  } catch (err) {
    console.error('demande non enregistrée : ' + (err && err.message));
    return reponse({ ok: false, error: 'script' });
  }
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

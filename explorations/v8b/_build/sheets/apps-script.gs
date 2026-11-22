/** @OnlyCurrentDoc */

/**
 * Bartier & Co : reçoit les demandes des formulaires du site (via la fonction /api/lead) et les ajoute
 * en haut des onglets « Particuliers » et « Artisans » du tableau « Bartier & Co, demandes du site ».
 *
 * À coller dans le tableau : Extensions > Apps Script.
 * Déploiement : Déployer > Nouveau déploiement > Application Web, exécuter en tant que « Moi »,
 * accès « Tout le monde ». L'adresse /exec obtenue va dans LEAD_SHEET_URL sur Vercel.
 * La clé ci-dessous doit être identique à LEAD_SHEET_KEY sur Vercel. Ne la publiez nulle part.
 */
var CLE = '@@CLE@@';

var METIERS = { couverture: 'Couverture et zinguerie', facade: 'Façade et ravalement', menuiserie: 'Menuiserie extérieure', charpente: 'Charpente', isolation: 'Isolation', autre: 'Autre métier' };
var TRAVAUX = { toiture: 'Toiture', facade: 'Façade', fenetres: 'Fenêtres et portes', charpente: 'Charpente', isolation: 'Isolation', autre: 'Autre projet' };
var EQUIPES = { '1': 'Une', '2': 'Deux', '3+': 'Trois ou plus' };
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
        texte(METIERS[f.metier] || f.metier), texte(f.code_postal), texte(EQUIPES[f.equipes] || f.equipes),
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
    return reponse({ ok: true });
  } catch (err) {
    console.error('demande non enregistrée : ' + (err && err.message));
    return reponse({ ok: false, error: 'script' });
  }
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

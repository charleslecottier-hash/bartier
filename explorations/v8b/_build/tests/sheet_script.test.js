'use strict';
// node --test _build/tests/ : script du tableau des demandes du site (_build/sheets/apps-script.gs), avec de faux services Google.
const fs = require('fs'), vm = require('vm'), assert = require('assert'), path = require('path');
const { test } = require('node:test');
const src = fs.readFileSync(path.join(__dirname, '..', 'sheets', 'apps-script.gs'), 'utf8').replace("'@@CLE@@'", "'cle-de-test-0123456789abcdef'");
function run(failMail) {
  const mails = [], rows = {};
  const sheet = (n) => ({ insertRowBefore() {}, getSheetId: () => (n === 'Artisans' ? 1 : 0),
    getRange: (r, c, nr, nc) => { const o = { setBackground: () => o, setFontWeight: () => o, setFontColor: () => o, setVerticalAlignment: () => o, setWrapStrategy: () => o, setNumberFormat: () => o, setValues: (v) => { rows[n] = v[0]; return o; }, setDataValidation: () => o }; return o; } });
  const ctx = { console, Utilities: {}, MailApp: { sendEmail: (o) => { if (failMail) throw new Error('quota'); mails.push(o); } },
    LockService: { getScriptLock: () => ({ waitLock() {}, releaseLock() {} }) },
    SpreadsheetApp: { WrapStrategy: { CLIP: 1 }, getActiveSpreadsheet: () => ({ getSheetByName: sheet, getUrl: () => 'https://docs.google.com/spreadsheets/d/X/edit' }), newDataValidation: () => { const b = { requireValueInList: () => b, setAllowInvalid: () => b, build: () => ({}) }; return b; } },
    ContentService: { MimeType: { JSON: 1 }, createTextOutput: (t) => ({ setMimeType: () => JSON.parse(t) }) } };
  vm.createContext(ctx); vm.runInContext(src, ctx);
  return { ctx, mails, rows };
}
test('alerte e-mail : artisan, particulier, mauvaise clé, panne d’envoi, exemple', () => {
const post = (ctx, o) => ctx.doPost({ postData: { contents: JSON.stringify(o) } });
let t = run(false);
let r = post(t.ctx, { cle: 'cle-de-test-0123456789abcdef', lead: { type: 'artisan', received_at: '2026-11-26T21:00:00Z', page: '/', utm_source: 'google', fields: { entreprise: 'Toitures <Durand>', prenom: 'Jean', telephone: '+33612345678', email: 'jean@durand.fr', metier: 'couverture', code_postal: '80000', chantier_moyen: '7 500 €', capacite: 'oui' } } });
assert.deepStrictEqual(r, { ok: true }); assert.strictEqual(t.mails.length, 1);
const m = t.mails[0];
assert.strictEqual(m.to, 'adminbartier@gmail.com'); assert.strictEqual(m.replyTo, 'jean@durand.fr');
assert.ok(m.subject.startsWith('Demande artisan : Toitures <Durand>, Couverture et zinguerie, 80000'));
assert.ok(m.htmlBody.includes('Toitures &lt;Durand&gt;') && m.htmlBody.includes('06 12 34 56 78') && m.htmlBody.includes('#gid=1') && m.htmlBody.includes('7 500 €'));
assert.strictEqual(t.rows.Artisans[2], 'Toitures <Durand>');
r = post(t.ctx, { cle: 'cle-de-test-0123456789abcdef', lead: { type: 'particulier', received_at: '2026-11-26T21:00:00Z', page: '/devis-travaux/', fields: { prenom: 'Anne', telephone: '+33611111111', code_postal: '59000', travaux: 'toiture', besoin: 'Fuite ou dégât urgent', delai: 'Dès que possible', statut: 'Propriétaire occupant' }, consent: { text: 'ok', at: '2026-11-26T21:00:00Z' } } });
assert.deepStrictEqual(r, { ok: true }); assert.strictEqual(t.mails.length, 2);
assert.ok(t.mails[1].subject === 'Demande particulier : Anne, Toiture, 59000' && !t.mails[1].replyTo && t.mails[1].body.includes('moins de 5 minutes'));
assert.deepStrictEqual(post(t.ctx, { cle: 'mauvaise', lead: {} }), { ok: false, error: 'cle' }); assert.strictEqual(t.mails.length, 2);
// Une panne d'envoi ne bloque pas l'enregistrement
console.error = () => {};
t = run(true);
r = post(t.ctx, { cle: 'cle-de-test-0123456789abcdef', lead: { type: 'artisan', fields: { entreprise: 'X', prenom: 'Y', telephone: '+33612345678', metier: 'facade', code_postal: '75001' } } });
assert.deepStrictEqual(r, { ok: true }); assert.ok(t.rows.Artisans);
// testerAlerte envoie un exemple
t = run(false); t.ctx.testerAlerte(); assert.strictEqual(t.mails.length, 1); assert.ok(t.mails[0].subject.includes('TEST'));

});

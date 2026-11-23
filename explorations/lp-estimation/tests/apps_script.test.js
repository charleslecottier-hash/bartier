'use strict';
// Tests du script du Google Sheet (sheets/apps-script.gs), avec de faux services Google : node --test tests/*.test.js
const test = require('node:test');
const assert = require('node:assert');
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');

function charger() {
  const rows = {}, mails = [], cache = {};
  const feuille = (nom) => {
    rows[nom] = rows[nom] || [];
    const range = (ligne) => { const r = { setBackground() { return r; }, setFontWeight() { return r; }, setFontColor() { return r; }, setVerticalAlignment() { return r; },
      setWrapStrategy() { return r; }, setNumberFormat() { return r; }, setValues(v) { if (ligne === 2) rows[nom].unshift(v[0]); return r; }, setDataValidation() { return r; } }; return r; };
    return { insertRowBefore() {}, getRange(l) { return range(l); }, setFrozenRows() {}, setColumnWidth() {} };
  };
  const ctx = {
    console,
    SpreadsheetApp: { getActiveSpreadsheet: () => ({ getSheetByName: (n) => (rows[n] ? feuille(n) : null), insertSheet: (n) => feuille(n) }),
      WrapStrategy: { CLIP: 'CLIP' }, newDataValidation: () => ({ requireValueInList() { return this; }, setAllowInvalid() { return this; }, build() { return {}; } }) },
    CacheService: { getScriptCache: () => ({ get: (k) => cache[k] || null, put: (k, v) => { cache[k] = v; } }) },
    LockService: { getScriptLock: () => ({ waitLock() {}, releaseLock() {} }) },
    MailApp: { sendEmail: (o) => mails.push(o) },
    ContentService: { createTextOutput: (t) => ({ setMimeType() { return JSON.parse(t); } }), MimeType: { JSON: 'json' } },
  };
  const src = fs.readFileSync(path.join(__dirname, '..', 'sheets', 'apps-script.gs'), 'utf8').replace("'@@CLE@@'", "'cle-de-test-0123456789'");
  vm.createContext(ctx); vm.runInContext(src, ctx);
  return { ctx, rows, mails };
}

const lead = {
  received_at: new Date().toISOString(), eid: 'abcdef12-3456', metier: 'Toiture', accord: 'question', page: '/toiture/',
  fields: { prenom: 'Jeanne', telephone: '+33612345678', code_postal: '59000', commune: 'Lille', travaux: 'Réfection', quantite: '100 m²', estimation: '9 000 € à 16 000 €', details: '=HYPERLINK("x")', delai: 'Dès que possible', statut: 'Propriétaire occupant' },
  tracking: { gclid: 'Cj0K', fbclid: 'IwAR' }, consent: { text: 'En validant…', at: new Date().toISOString() },
};
const post = (ctx, body) => ctx.doPost({ postData: { contents: JSON.stringify(body) } });

test('une demande : une ligne dans l’onglet du client et un e-mail à l’artisan', () => {
  const { ctx, rows, mails } = charger();
  const r = post(ctx, { cle: 'cle-de-test-0123456789', client: 'Toitures Test', alerte: ['artisan@exemple.fr'], lead });
  assert.strictEqual(r.ok, true);
  const l = rows['Toitures Test'][0];
  assert.strictEqual(l[1], 'À rappeler');
  assert.strictEqual(l[3], '06 12 34 56 78');
  assert.strictEqual(l[13], 'Oui (question)');
  assert.ok(String(l[10]).startsWith("'="), 'une formule est neutralisée');
  assert.strictEqual(mails.length, 1);
  assert.strictEqual(mails[0].to, 'artisan@exemple.fr');
  assert.match(mails[0].subject, /^Nouvelle demande : Jeanne, Toiture, 59000 Lille/);
  assert.match(mails[0].htmlBody, /href="tel:\+33612345678"/);
  assert.ok(!mails[0].htmlBody.includes('<script'), 'HTML échappé');
});

test('même demande renvoyée : ni deuxième ligne ni deuxième e-mail', () => {
  const { ctx, rows, mails } = charger();
  const b = { cle: 'cle-de-test-0123456789', client: 'Toitures Test', alerte: ['artisan@exemple.fr'], lead };
  post(ctx, b); const r = post(ctx, b);
  assert.strictEqual(r.ok, true); assert.strictEqual(r.doublon, true);
  assert.strictEqual(rows['Toitures Test'].length, 1); assert.strictEqual(mails.length, 1);
});

test('mauvaise clé : rien n’est écrit ni envoyé', () => {
  const { ctx, rows, mails } = charger();
  const r = post(ctx, { cle: 'mauvaise', client: 'Toitures Test', alerte: ['artisan@exemple.fr'], lead });
  assert.strictEqual(r.ok, false); assert.deepStrictEqual(rows, {}); assert.strictEqual(mails.length, 0);
});

test('adresse invalide ou absente : la ligne est écrite, pas d’e-mail', () => {
  const { ctx, rows, mails } = charger();
  post(ctx, { cle: 'cle-de-test-0123456789', client: 'Toitures Test', alerte: ['pas-une-adresse'], lead: Object.assign({}, lead, { eid: 'x1234567' }) });
  post(ctx, { cle: 'cle-de-test-0123456789', client: 'Toitures Test', lead: Object.assign({}, lead, { eid: 'x7654321' }) });
  assert.strictEqual(rows['Toitures Test'].length, 2); assert.strictEqual(mails.length, 0);
});

test('envoi d’e-mail en panne : la demande est quand même enregistrée', () => {
  const { ctx, rows } = charger();
  ctx.MailApp.sendEmail = () => { throw new Error('quota'); };
  const r = post(ctx, { cle: 'cle-de-test-0123456789', client: 'Toitures Test', alerte: ['artisan@exemple.fr'], lead });
  assert.strictEqual(r.ok, true); assert.strictEqual(rows['Toitures Test'].length, 1);
});

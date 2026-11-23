'use strict';
// Tests de la fonction /api/lead/ des pages clients : node --test tests/
const test = require('node:test');
const assert = require('node:assert');
const fs = require('node:fs');
const os = require('node:os');
const path = require('node:path');
const { Readable } = require('node:stream');

// Charge api_lead.js comme build.py le génère, pour un client fictif.
function load(pixel) {
  const src = fs.readFileSync(path.join(__dirname, '..', 'api_lead.js'), 'utf8')
    .replace('__CLIENT__', JSON.stringify('Toitures Test'))
    .replace('__METIERS__', JSON.stringify({ toiture: 'Toiture' }))
    .replace('__PIXEL__', JSON.stringify(pixel));
  const f = path.join(fs.mkdtempSync(path.join(os.tmpdir(), 'lead-')), 'lead.js');
  fs.writeFileSync(f, src);
  return require(f);
}

const SHEET = 'https://script.google.com/macros/s/AKfycbTEST_abcdefghij-0123456789/exec';
const ENV = { LEAD_SHEET_URL: SHEET, LEAD_SHEET_KEY: 'cle-de-test-0123456789', META_ACCESS_TOKEN: 'jeton-test' };

function payload(extra) {
  return Object.assign({
    type: 'estimation', metier: 'toiture', eid: 'abcdef12-3456-7890-abcd-ef1234567890', accord: 'case', clic_at: Date.now() - 60000,
    fields: { prenom: 'Jeanne', telephone: '06 12 34 56 78', code_postal: '59000', commune: 'Lille', travaux: 'Réfection', details: ['Tuiles'] },
    tracking: { fbclid: 'IwAR0abc_DEF-123', gclid: 'Cj0KCQ_test', utm_source: 'facebook' },
    consent: { text: 'En validant…', at: new Date().toISOString() }, page: '/toiture/', site_web: '',
  }, extra || {});
}

function call(handler, body, headers, env) {
  const req = Readable.from([Buffer.from(JSON.stringify(body))]);
  req.method = 'POST';
  req.headers = Object.assign({ origin: 'https://devis.toitures-test.fr', host: 'devis.toitures-test.fr', 'x-forwarded-for': '203.0.113.' + Math.floor(Math.random() * 250), 'user-agent': 'Mozilla/5.0 test' }, headers || {});
  return new Promise((resolve) => {
    const res = { statusCode: 0, headers: {}, setHeader(k, v) { this.headers[k] = v; }, end(b) { resolve({ status: this.statusCode, body: JSON.parse(b) }); } };
    handler(req, res, env || ENV);
  });
}

// Faux Google Sheet (avec la redirection d'Apps Script) et fausse API Meta.
function mockFetch(calls, opts) {
  opts = opts || {};
  global.fetch = async (url, init) => {
    calls.push({ url: String(url), init });
    if (String(url).startsWith(SHEET)) return { status: 302, headers: { get: () => 'https://script.googleusercontent.com/macros/echo?x=1' } };
    if (String(url).startsWith('https://script.googleusercontent.com/')) return { status: 200, ok: true, text: async () => JSON.stringify({ ok: !opts.sheetFails }) };
    if (String(url).startsWith('https://graph.facebook.com/')) return { status: opts.metaStatus || 200, ok: !opts.metaStatus };
    throw new Error('hôte inattendu ' + url);
  };
}

test('demande valide : une ligne dans le tableau et un Lead Meta avec l’identifiant de clic', async () => {
  const h = load('123456789012345'); const calls = []; mockFetch(calls);
  const r = await call(h, payload());
  assert.strictEqual(r.status, 200); assert.strictEqual(r.body.ok, true);
  const sheet = JSON.parse(calls.find((c) => c.url === SHEET).init.body);
  assert.strictEqual(sheet.client, 'Toitures Test');
  assert.strictEqual(sheet.lead.fields.telephone, '+33612345678');
  assert.strictEqual(sheet.lead.metier, 'Toiture');
  assert.strictEqual(sheet.lead.accord, 'case');
  assert.strictEqual(sheet.lead.tracking.gclid, 'Cj0KCQ_test');
  const meta = calls.find((c) => c.url.startsWith('https://graph.facebook.com/'));
  assert.match(meta.url, /\/v23\.0\/123456789012345\/events$/);
  const ev = JSON.parse(meta.init.body);
  assert.strictEqual(ev.data[0].event_name, 'Lead');
  assert.strictEqual(ev.data[0].event_id, 'abcdef12-3456-7890-abcd-ef1234567890');
  assert.strictEqual(ev.data[0].event_source_url, 'https://devis.toitures-test.fr/toiture/');
  assert.match(ev.data[0].user_data.fbc, /^fb\.1\.\d{13}\.IwAR0abc_DEF-123$/);
  assert.ok(!('ph' in ev.data[0].user_data) && !('fn' in ev.data[0].user_data), 'ni téléphone ni prénom chez Meta');
  assert.ok(!JSON.stringify(ev).includes('Jeanne') && !JSON.stringify(ev).includes('612345678'));
});

test('sans accord : la ligne est écrite, rien ne part chez Meta', async () => {
  const h = load('123456789012345'); const calls = []; mockFetch(calls);
  const r = await call(h, payload({ accord: 'non' }));
  assert.strictEqual(r.status, 200);
  assert.ok(calls.some((c) => c.url === SHEET));
  assert.ok(!calls.some((c) => c.url.startsWith('https://graph.facebook.com/')));
});

test('accord inconnu : traité comme un refus', async () => {
  const h = load('123456789012345'); const calls = []; mockFetch(calls);
  await call(h, payload({ accord: 'oui' }));
  assert.ok(!calls.some((c) => c.url.startsWith('https://graph.facebook.com/')));
});

test('sans pixel ni jeton : pas d’appel à Meta', async () => {
  const calls = []; mockFetch(calls);
  await call(load(''), payload());
  await call(load('123456789012345'), payload(), null, { LEAD_SHEET_URL: SHEET, LEAD_SHEET_KEY: ENV.LEAD_SHEET_KEY });
  assert.ok(!calls.some((c) => c.url.startsWith('https://graph.facebook.com/')));
});

test('Meta en panne : la demande reste enregistrée et la page reçoit ok', async () => {
  const h = load('123456789012345'); const calls = []; mockFetch(calls, { metaStatus: 500 });
  const r = await call(h, payload());
  assert.strictEqual(r.status, 200); assert.strictEqual(r.body.ok, true);
});

test('tableau en panne : la page reçoit une erreur (et propose de réessayer)', async () => {
  const h = load('123456789012345'); const calls = []; mockFetch(calls, { sheetFails: true });
  const r = await call(h, payload());
  assert.strictEqual(r.status, 502);
});

test('tableau non réglé : 503', async () => {
  const h = load('123456789012345'); const calls = []; mockFetch(calls);
  const r = await call(h, payload(), null, {});
  assert.strictEqual(r.status, 503);
  assert.strictEqual(calls.length, 0);
});

test('autre site : refusé', async () => {
  const h = load('123456789012345'); const calls = []; mockFetch(calls);
  const r = await call(h, payload(), { origin: 'https://autre-site.fr' });
  assert.strictEqual(r.status, 403);
  assert.strictEqual(calls.length, 0);
});

test('champ piège rempli : répond ok sans rien enregistrer', async () => {
  const h = load('123456789012345'); const calls = []; mockFetch(calls);
  const r = await call(h, payload({ site_web: 'http://spam.example' }));
  assert.strictEqual(r.status, 200);
  assert.strictEqual(calls.length, 0);
});

test('téléphone, métier ou identifiant invalides : 422', async () => {
  const h = load('123456789012345'); const calls = []; mockFetch(calls);
  for (const p of [payload({ fields: Object.assign(payload().fields, { telephone: '12' }) }), payload({ metier: 'piscine' }), payload({ eid: 'x' })]) {
    const r = await call(h, p);
    assert.strictEqual(r.status, 422);
  }
  assert.strictEqual(calls.length, 0);
});

test('identifiant de clic douteux : ignoré', async () => {
  const h = load('123456789012345'); const calls = []; mockFetch(calls);
  await call(h, payload({ tracking: { fbclid: 'abc<script>' } }));
  const sheet = JSON.parse(calls.find((c) => c.url === SHEET).init.body);
  assert.ok(!('fbclid' in sheet.lead.tracking));
});

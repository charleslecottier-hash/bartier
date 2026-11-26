'use strict';
// node --test /home/user/bartier/explorations/v8b/_build/tests/
const { test, beforeEach, afterEach } = require('node:test');
const assert = require('node:assert');
const crypto = require('node:crypto');
const { Readable } = require('node:stream');
const path = require('node:path');

const handler = require(path.join(__dirname, '..', '..', 'api', 'lead.js'));
const { normalisePhone, validate, buildEmail } = handler;

const ENV_KEYS = ['RESEND_API_KEY', 'LEAD_TO', 'LEAD_FROM', 'LEAD_WEBHOOK_URL', 'LEAD_WEBHOOK_SECRET', 'LEAD_SHEET_URL', 'LEAD_SHEET_KEY'];
const realFetch = global.fetch;
const realLog = console.log;
let logs = [];
let calls = [];

beforeEach(() => {
  for (const k of ENV_KEYS) delete process.env[k];
  handler._resetRateLimit();
  logs = [];
  calls = [];
  console.log = (...a) => { logs.push(a.join(' ')); };
  global.fetch = async () => { throw new Error('fetch non simulé'); };
});
afterEach(() => {
  global.fetch = realFetch;
  console.log = realLog;
});

function mockFetch(fn) {
  global.fetch = async (url, init) => {
    calls.push({ url: String(url), init });
    return fn(String(url), init);
  };
}
const okRes = { ok: true, status: 200 };

const ORIGIN = 'https://bartierandco.com';
const artisan = (over = {}, top = {}) => ({
  type: 'artisan',
  fields: Object.assign({
    metier: 'couverture', code_postal: '80000', chantier_moyen: '5 000', capacite: 'oui',
    prenom: 'Jean', telephone: '06 12 34 56 78', entreprise: 'Toitures Durand', email: 'jean@durand.fr',
  }, over),
  page: '/', utm_source: 'google', utm_medium: 'cpc', utm_campaign: 'couvreurs', utm_content: 'a1',
  gclid: 'G123', fbclid: '', site_web: '', ...top,
});
const particulier = (over = {}, top = {}) => ({
  type: 'particulier',
  fields: Object.assign({
    travaux: 'toiture', besoin: 'Fuite ou dégât urgent', delai: 'Dès que possible',
    statut: 'Propriétaire occupant', code_postal: '75004', prenom: 'Marie', telephone: '+33 7 12 34 56 78',
  }, over),
  page: '/devis-travaux/toiture/', utm_source: 'meta', utm_medium: '', utm_campaign: '', utm_content: '',
  gclid: '', fbclid: 'F1',
  consent: { text: 'J’accepte d’être rappelé par Bartier & Co au sujet de ce projet.', at: '2026-11-18T10:00:00.000Z' },
  site_web: '', ...top,
});

function call(body, opts = {}) {
  const headers = Object.assign({ 'content-type': 'application/json', origin: ORIGIN, 'x-forwarded-for': '203.0.113.7, 10.0.0.1' }, opts.headers || {});
  for (const k of Object.keys(headers)) if (headers[k] === undefined) delete headers[k];
  let req;
  if (opts.stream !== undefined) {
    req = Readable.from([Buffer.from(opts.stream)]);
    req.headers = headers;
    req.method = opts.method || 'POST';
  } else {
    req = { method: opts.method || 'POST', headers, body };
  }
  return new Promise((resolve, reject) => {
    const out = { status: 0, headers: {}, json: null };
    const res = {
      set statusCode(v) { out.status = v; },
      get statusCode() { return out.status; },
      setHeader(k, v) { out.headers[k.toLowerCase()] = v; },
      end(s) { try { out.json = JSON.parse(s); } catch (e) { out.json = s; } resolve(out); },
    };
    Promise.resolve(handler(req, res)).catch(reject);
  });
}

function useResend() {
  process.env.RESEND_API_KEY = 're_test_key';
  process.env.LEAD_TO = 'leads@example.test, second@example.test';
  process.env.LEAD_FROM = 'Site <site@example.test>';
}

/* ---------- Méthode, type de contenu, taille ---------- */

test('méthodes autres que POST : 405 avec Allow', async () => {
  for (const method of ['GET', 'PUT', 'DELETE', 'OPTIONS', 'HEAD']) {
    const r = await call(undefined, { method });
    assert.strictEqual(r.status, 405);
    assert.strictEqual(r.headers.allow, 'POST');
    assert.strictEqual(r.headers['cache-control'], 'no-store');
    assert.match(r.headers['content-type'], /application\/json/);
    assert.deepStrictEqual(r.json, { ok: false, error: 'method_not_allowed' });
  }
});

test('Content-Type autre que application/json : 415', async () => {
  const r = await call('type=artisan', { headers: { 'content-type': 'application/x-www-form-urlencoded' } });
  assert.strictEqual(r.status, 415);
  const r2 = await call(artisan(), { headers: { 'content-type': 'application/json; charset=utf-8' } });
  assert.strictEqual(r2.status, 503); // accepté, mais aucun canal configuré
});

test('corps trop gros : 413 (objet, chaîne, flux, content-length)', async () => {
  const big = 'x'.repeat(11 * 1024);
  assert.strictEqual((await call(artisan({}, { page: big }))).status, 413);
  assert.strictEqual((await call(JSON.stringify(artisan({}, { page: big })))).status, 413);
  assert.strictEqual((await call(undefined, { stream: JSON.stringify(artisan({}, { page: big })) })).status, 413);
  assert.strictEqual((await call(artisan(), { headers: { 'content-length': '20000' } })).status, 413);
});

test('corps : objet, chaîne, Buffer, flux, JSON invalide', async () => {
  useResend();
  mockFetch(() => okRes);
  assert.strictEqual((await call(artisan())).status, 200);
  assert.strictEqual((await call(JSON.stringify(artisan()), { headers: { 'x-forwarded-for': '198.51.100.1' } })).status, 200);
  assert.strictEqual((await call(Buffer.from(JSON.stringify(artisan())), { headers: { 'x-forwarded-for': '198.51.100.2' } })).status, 200);
  assert.strictEqual((await call(undefined, { stream: JSON.stringify(artisan()), headers: { 'x-forwarded-for': '198.51.100.3' } })).status, 200);
  const bad = await call('{nope', { headers: { 'x-forwarded-for': '198.51.100.4' } });
  assert.strictEqual(bad.status, 400);
  assert.deepStrictEqual(bad.json, { ok: false, error: 'bad_json' });
  assert.strictEqual((await call(undefined, { stream: '', headers: { 'x-forwarded-for': '198.51.100.5' } })).status, 400);
  assert.strictEqual((await call('[1,2]', { headers: { 'x-forwarded-for': '198.51.100.6' } })).status, 400);
});

/* ---------- Origine ---------- */

test('origines acceptées', async () => {
  const good = ['https://bartierandco.com', 'https://www.bartierandco.com', 'https://bartier-8b.vercel.app',
    'https://bartier-8b-git-main-equipe.vercel.app', 'https://bartier-8b-abc123.vercel.app',
    'http://localhost:8766', 'http://127.0.0.1:3000'];
  let i = 0;
  for (const origin of good) {
    const r = await call(artisan(), { headers: { origin, 'x-forwarded-for': '192.0.2.' + (i += 1) } });
    assert.strictEqual(r.status, 503, origin);
  }
});

test('origines refusées : 403', async () => {
  const badOrigins = ['https://evil.example', 'https://bartierandco.com.evil.example', 'https://bartier-8b.evil.example',
    'https://xbartier-8b.vercel.app', 'https://evilbartierandco.com', 'null', 'not a url', 'ftp://bartierandco.com'];
  for (const origin of badOrigins) {
    const r = await call(artisan(), { headers: { origin } });
    assert.strictEqual(r.status, 403, origin);
    assert.deepStrictEqual(r.json, { ok: false, error: 'forbidden' });
  }
  const none = await call(artisan(), { headers: { origin: undefined } });
  assert.strictEqual(none.status, 403);
});

test('Referer utilisé quand Origin est absent', async () => {
  const ok = await call(artisan(), { headers: { origin: undefined, referer: 'https://www.bartierandco.com/devis-travaux/' } });
  assert.strictEqual(ok.status, 503);
  const ko = await call(artisan(), { headers: { origin: undefined, referer: 'https://evil.example/?u=https://bartierandco.com' } });
  assert.strictEqual(ko.status, 403);
});

/* ---------- Pot de miel ---------- */

test('pot de miel : 200 {ok:true} et aucun envoi', async () => {
  useResend();
  mockFetch(() => okRes);
  const r = await call(artisan({ telephone: 'nimporte' }, { site_web: 'https://spam.example' }));
  assert.strictEqual(r.status, 200);
  assert.deepStrictEqual(r.json, { ok: true });
  assert.strictEqual(calls.length, 0);
});

/* ---------- Téléphone ---------- */

test('normalisation du téléphone', () => {
  const ok = {
    '06 12 34 56 78': '+33612345678',
    '0612345678': '+33612345678',
    '06.12.34.56.78': '+33612345678',
    '06-12-34-56-78': '+33612345678',
    ' 01 23 45 67 89 ': '+33123456789',
    '+33 6 12 34 56 78': '+33612345678',
    '+33612345678': '+33612345678',
    '+33 (0)6 12 34 56 78': '+33612345678',
    '+33 06 12 34 56 78': '+33612345678',
    '0033 6 12 34 56 78': '+33612345678',
    '0033612345678': '+33612345678',
    '07 81 01 89 36': '+33781018936',
    '09.70.12.34.56': '+33970123456',
  };
  for (const [input, want] of Object.entries(ok)) assert.strictEqual(normalisePhone(input), want, input);
  const ko = ['', '   ', '06 12 34 56', '06 12 34 56 78 9', '00 12 34 56 78', '+32 470 12 34 56', '+44 20 7946 0958',
    '+33 0 0 12 34 56 78', '+330012345678', '6 12 34 56 78', '612345678', '06 12 34 56 7a', 'abcdefghij',
    '06/12/34/56/78', '06 12 34 56 78\r\nBcc: x@y.z', '+33+612345678', '0033 0033 612345678', null, undefined, {}, 612345678];
  for (const input of ko) assert.strictEqual(normalisePhone(input), null, String(input));
});

/* ---------- Validation ---------- */

test('artisan valide : lead normalisé, rien d’autre repris', () => {
  const v = validate(artisan({ prenom: '  Jean\u0007 ', email: 'jean@durand.fr', inconnu: 'x' }, { ip: '1.2.3.4', autre: 'y' }), Date.UTC(2026, 10, 18, 9, 0, 0));
  assert.strictEqual(v.ok, true);
  assert.deepStrictEqual(v.lead, {
    type: 'artisan',
    received_at: '2026-11-18T09:00:00.000Z',
    fields: { metier: 'couverture', code_postal: '80000', chantier_moyen: '5 000 €', capacite: 'oui', prenom: 'Jean',
      telephone: '+33612345678', entreprise: 'Toitures Durand', email: 'jean@durand.fr' },
    page: '/', utm_source: 'google', utm_medium: 'cpc', utm_campaign: 'couvreurs', utm_content: 'a1', gclid: 'G123', fbclid: '',
  });
});

test('artisan : chaque champ requis et chaque valeur autorisée', () => {
  const cases = [
    ['metier', undefined], ['metier', 'plomberie'], ['metier', ''],
    ['code_postal', undefined], ['code_postal', '7500'], ['code_postal', '750044'], ['code_postal', '75 004'], ['code_postal', 'ABCDE'],
    ['chantier_moyen', undefined], ['chantier_moyen', ''], ['chantier_moyen', '0'], ['chantier_moyen', '200'], ['chantier_moyen', '5000,50'],
    ['chantier_moyen', '-5000'], ['chantier_moyen', '2000000'], ['chantier_moyen', 'cinq mille'],
    ['capacite', undefined], ['capacite', 'non'],
    ['prenom', undefined], ['prenom', ' '], ['prenom', 'J'], ['prenom', { a: 1 }],
    ['telephone', undefined], ['telephone', '123'], ['telephone', '+32 470 12 34 56'],
    ['entreprise', undefined], ['entreprise', ''],
    ['email', undefined], ['email', ''], ['email', 'pas-un-email'], ['email', 'a@b'], ['email', 'a b@c.fr'], ['email', 'a@b.fr\nBcc: x@y.fr'],
  ];
  for (const [field, value] of cases) {
    const v = validate(artisan({ [field]: value }));
    assert.deepStrictEqual(v, { ok: false, error: 'invalid', field }, `${field}=${JSON.stringify(value)}`);
  }
  for (const m of ['couverture', 'facade', 'menuiserie', 'charpente', 'isolation', 'autre']) assert.strictEqual(validate(artisan({ metier: m })).ok, true, m);
  for (const [v, attendu] of [['5000', '5 000 €'], ['12 500 €', '12 500 €'], [8000, '8 000 €'], ['300', '300 €'], ['1000000', '1 000 000 €'], ['15\u202f000', '15 000 €']]) {
    assert.strictEqual(validate(artisan({ chantier_moyen: v })).lead.fields.chantier_moyen, attendu, String(v));
  }
  for (const c of ['oui', 'bientot', 'ne-sait-pas']) assert.strictEqual(validate(artisan({ capacite: c })).ok, true, c);
  assert.strictEqual(validate(artisan({ code_postal: 80000 })).lead.fields.code_postal, '80000');
});

test('type et structure', () => {
  assert.deepStrictEqual(validate(artisan({}, { type: 'autre' })), { ok: false, error: 'invalid', field: 'type' });
  assert.deepStrictEqual(validate({ type: 'artisan' }), { ok: false, error: 'invalid', field: 'fields' });
  assert.deepStrictEqual(validate({ type: 'artisan', fields: [] }), { ok: false, error: 'invalid', field: 'fields' });
  assert.deepStrictEqual(validate(null), { ok: false, error: 'invalid', field: 'payload' });
});

test('particulier valide : consentement conservé comme preuve', () => {
  const v = validate(particulier(), Date.UTC(2026, 10, 18, 10, 0, 5));
  assert.strictEqual(v.ok, true);
  assert.deepStrictEqual(v.lead.fields, { travaux: 'toiture', besoin: 'Fuite ou dégât urgent', delai: 'Dès que possible',
    statut: 'Propriétaire occupant', code_postal: '75004', prenom: 'Marie', telephone: '+33712345678' });
  assert.deepStrictEqual(v.lead.consent, { text: 'J’accepte d’être rappelé par Bartier & Co au sujet de ce projet.', at: '2026-11-18T10:00:00.000Z' });
  assert.strictEqual(v.lead.received_at, '2026-11-18T10:00:05.000Z');
  assert.strictEqual(v.lead.page, '/devis-travaux/toiture/');
  assert.strictEqual(v.lead.fbclid, 'F1');
});

test('particulier : champs requis, valeurs du formulaire, consentement', () => {
  const cases = [
    ['travaux', undefined], ['travaux', 'piscine'],
    ['besoin', undefined], ['besoin', 'Combles'], // besoin d'un autre métier
    ['delai', undefined], ['delai', 'Jamais'],
    ['statut', undefined], ['statut', 'Locataire'],
    ['code_postal', '7500'], ['prenom', ''], ['telephone', '06 12'],
    ['email', 'x@'],
  ];
  for (const [field, value] of cases) {
    assert.deepStrictEqual(validate(particulier({ [field]: value })), { ok: false, error: 'invalid', field }, `${field}=${value}`);
  }
  const noConsent = [undefined, null, {}, { text: '', at: '2026-11-18T10:00:00Z' }, { text: 'ok', at: '' },
    { text: 'ok', at: 'hier' }, { text: 'ok', at: '2026-11-18' }, { text: 'ok', at: '2026-13-45T10:00:00Z' }, { text: '  ', at: '2026-11-18T10:00:00Z' }];
  for (const consent of noConsent) {
    assert.deepStrictEqual(validate(particulier({}, { consent })), { ok: false, error: 'invalid', field: 'consent' }, JSON.stringify(consent));
  }
  assert.strictEqual(validate(particulier({}, { consent: { text: 'ok', at: '2026-11-18T11:00:00+01:00' } })).lead.consent.at, '2026-11-18T10:00:00.000Z');
  // toutes les combinaisons du formulaire
  const combos = { toiture: 'Démoussage, nettoyage', facade: 'Isolation par l’extérieur', fenetres: 'Porte d’entrée',
    charpente: 'Charpente neuve', isolation: 'Je ne sais pas encore', autre: 'Rénovation globale' };
  for (const [travaux, besoin] of Object.entries(combos)) assert.strictEqual(validate(particulier({ travaux, besoin })).ok, true, travaux);
  // apostrophe droite tolérée, valeur canonique restituée
  assert.strictEqual(validate(particulier({ travaux: 'fenetres', besoin: "Porte d'entrée" })).lead.fields.besoin, 'Porte d’entrée');
  for (const d of ['Dès que possible', 'Dans 1 à 3 mois', 'Dans plus de 3 mois', 'Je compare des prix']) assert.strictEqual(validate(particulier({ delai: d })).ok, true, d);
  assert.strictEqual(validate(particulier({ statut: 'Propriétaire bailleur' })).ok, true);
  // l'artisan n'a pas besoin de consentement
  assert.strictEqual(validate(artisan()).ok, true);
});

test('nettoyage : espaces, caractères de contrôle, plafonds', () => {
  const v = validate(artisan({ prenom: '  Jean\r\n\tPaul\u0000  ', entreprise: 'E'.repeat(200) },
    { page: 'https://bartierandco.com/' + 'p'.repeat(500), utm_campaign: 'c\u0001amp\n', gclid: 42, fbclid: { a: 1 } }));
  assert.strictEqual(v.ok, true);
  assert.strictEqual(v.lead.fields.prenom, 'Jean Paul');
  assert.strictEqual(v.lead.fields.entreprise.length, 80);
  assert.strictEqual(v.lead.page.length, 300);
  assert.strictEqual(v.lead.utm_campaign, 'c amp');
  assert.strictEqual(v.lead.gclid, '42');
  assert.strictEqual(v.lead.fbclid, '');
  const c = validate(particulier({}, { consent: { text: 'x'.repeat(3000), at: '2026-11-18T10:00:00Z' } }));
  assert.strictEqual(c.lead.consent.text.length, 1000);
});

test('422 avec le champ en erreur via le gestionnaire', async () => {
  const r = await call(artisan({ telephone: '12' }));
  assert.strictEqual(r.status, 422);
  assert.deepStrictEqual(r.json, { ok: false, error: 'invalid', field: 'telephone' });
  assert.strictEqual(r.headers['cache-control'], 'no-store');
});

/* ---------- E-mail ---------- */

test('buildEmail : sujets, texte, réponse', () => {
  const a = buildEmail(validate(artisan({ email: 'jean@durand.fr' })).lead);
  assert.strictEqual(a.subject, 'Nouveau artisan : Toitures Durand (80000)');
  assert.strictEqual(a.reply_to, 'jean@durand.fr');
  assert.match(a.text, /Téléphone : \+33612345678/);
  assert.match(a.text, /utm_source : google/);
  const p = buildEmail(validate(particulier()).lead);
  assert.strictEqual(p.subject, 'Nouveau particulier : toiture (75004)');
  assert.strictEqual('reply_to' in p, false);
  assert.match(p.text, /Consentement : J’accepte/);
  assert.match(p.text, /Consentement donné le : 2026-11-18T10:00:00.000Z/);
  assert.match(p.html, /Besoin<\/th>/);
});

test('buildEmail : toutes les valeurs sont échappées en HTML', () => {
  const v = validate(artisan({ entreprise: '<script>alert("x")</script> & Fils', prenom: "D'Artagnan <b>" },
    { page: '/?a=<img src=x onerror=1>', utm_source: '"><svg/onload=1>' }));
  const m = buildEmail(v.lead);
  assert.ok(!/<script|<img|<svg|<b>/i.test(m.html));
  assert.ok(m.html.includes('&lt;script&gt;alert(&quot;x&quot;)&lt;/script&gt; &amp; Fils'));
  assert.ok(m.html.includes('D&#39;Artagnan &lt;b&gt;'));
  assert.ok(m.html.includes('&quot;&gt;&lt;svg/onload=1&gt;'));
  assert.ok(m.text.includes('<script>alert("x")</script> & Fils')); // le texte brut reste tel quel
});

test('injection d’en-têtes : pas de CR/LF dans le sujet ni reply_to', () => {
  const v = validate(artisan({ entreprise: 'Durand\r\nBcc: victime@example.test\r\n\r\nCorps', email: 'jean@durand.fr' }));
  const m = buildEmail(v.lead);
  assert.ok(!/[\r\n]/.test(m.subject));
  assert.strictEqual(m.subject, 'Nouveau artisan : Durand Bcc: victime@example.test Corps (80000)');
  // un lead construit à la main (sans passer par validate) reste sûr
  const forged = { type: 'artisan', received_at: 'x', fields: { entreprise: 'A\nB\u2028C', code_postal: '75004\r\nX: y', email: 'a@b.fr\r\nBcc: c@d.fr' } };
  const f = buildEmail(forged);
  assert.ok(!/[\r\n\u2028]/.test(f.subject));
  assert.strictEqual('reply_to' in f, false);
  assert.deepStrictEqual(validate(artisan({ email: 'jean@durand.fr\r\nBcc: x@y.fr' })), { ok: false, error: 'invalid', field: 'email' });
});

/* ---------- Livraison ---------- */

test('aucun canal configuré : 503 not_configured', async () => {
  const r = await call(artisan());
  assert.strictEqual(r.status, 503);
  assert.deepStrictEqual(r.json, { ok: false, error: 'not_configured' });
  process.env.RESEND_API_KEY = 'k'; // configuration partielle
  process.env.LEAD_TO = 'a@example.test';
  assert.strictEqual((await call(artisan())).status, 503);
  delete process.env.RESEND_API_KEY;
  process.env.LEAD_WEBHOOK_URL = 'http://hooks.example.test/x'; // http refusé
  mockFetch(() => okRes);
  assert.strictEqual((await call(artisan())).status, 503);
  assert.strictEqual(calls.length, 0);
});

test('Resend : succès', async () => {
  useResend();
  mockFetch(() => okRes);
  const r = await call(artisan({ email: 'jean@durand.fr' }));
  assert.strictEqual(r.status, 200);
  assert.deepStrictEqual(r.json, { ok: true });
  assert.strictEqual(calls.length, 1);
  const c = calls[0];
  assert.strictEqual(c.url, 'https://api.resend.com/emails');
  assert.strictEqual(c.init.method, 'POST');
  assert.strictEqual(c.init.headers.Authorization, 'Bearer re_test_key');
  assert.strictEqual(c.init.headers['Content-Type'], 'application/json');
  assert.ok(c.init.signal instanceof AbortSignal);
  const body = JSON.parse(c.init.body);
  assert.strictEqual(body.from, 'Site <site@example.test>');
  assert.deepStrictEqual(body.to, ['leads@example.test', 'second@example.test']);
  assert.strictEqual(body.subject, 'Nouveau artisan : Toitures Durand (80000)');
  assert.strictEqual(body.reply_to, 'jean@durand.fr');
  assert.ok(body.text.length > 0 && body.html.length > 0);
  assert.ok(!c.init.body.includes('203.0.113.7')); // l'IP n'est pas transmise
});

test('Resend : échec HTTP, erreur réseau, délai dépassé : 502', async () => {
  useResend();
  mockFetch(() => ({ ok: false, status: 422 }));
  let r = await call(artisan());
  assert.strictEqual(r.status, 502);
  assert.deepStrictEqual(r.json, { ok: false, error: 'delivery_failed' });
  mockFetch(() => { throw new TypeError('fetch failed'); });
  r = await call(artisan());
  assert.strictEqual(r.status, 502);
  mockFetch(() => { throw Object.assign(new Error('aborted'), { name: 'AbortError' }); });
  r = await call(artisan());
  assert.strictEqual(r.status, 502);
  assert.ok(logs.some((l) => l.includes('resend:timeout')));
  assert.ok(logs.some((l) => l.includes('resend:http_422')));
});

test('webhook : corps = lead normalisé, signature HMAC-SHA256', async () => {
  process.env.LEAD_WEBHOOK_URL = 'https://hooks.example.test/lead';
  process.env.LEAD_WEBHOOK_SECRET = 's3cret';
  mockFetch(() => okRes);
  const r = await call(particulier());
  assert.strictEqual(r.status, 200);
  assert.strictEqual(calls.length, 1);
  const c = calls[0];
  assert.strictEqual(c.url, 'https://hooks.example.test/lead');
  const want = crypto.createHmac('sha256', 's3cret').update(c.init.body).digest('hex');
  assert.strictEqual(c.init.headers['X-Bartier-Signature'], want);
  assert.match(want, /^[0-9a-f]{64}$/);
  const lead = JSON.parse(c.init.body);
  assert.deepStrictEqual(Object.keys(lead).sort(), ['consent', 'fbclid', 'fields', 'gclid', 'page', 'received_at', 'type',
    'utm_campaign', 'utm_content', 'utm_medium', 'utm_source'].sort());
  assert.strictEqual(lead.fields.telephone, '+33712345678');
  assert.ok(!Number.isNaN(Date.parse(lead.received_at)));
  assert.ok(!('site_web' in lead));
  assert.ok(!c.init.body.includes('203.0.113.7'));
});

test('webhook sans secret : pas de signature', async () => {
  process.env.LEAD_WEBHOOK_URL = 'https://hooks.example.test/lead';
  mockFetch(() => okRes);
  assert.strictEqual((await call(artisan())).status, 200);
  assert.strictEqual('X-Bartier-Signature' in calls[0].init.headers, false);
});

test('deux canaux : succès si au moins un accepte, 502 si tous échouent', async () => {
  useResend();
  process.env.LEAD_WEBHOOK_URL = 'https://hooks.example.test/lead';
  mockFetch((url) => (url.includes('resend') ? { ok: false, status: 500 } : okRes));
  let r = await call(artisan());
  assert.strictEqual(r.status, 200);
  assert.strictEqual(calls.length, 2);
  mockFetch((url) => (url.includes('resend') ? okRes : { ok: false, status: 500 }));
  assert.strictEqual((await call(artisan())).status, 200);
  mockFetch(() => ({ ok: false, status: 500 }));
  r = await call(artisan());
  assert.strictEqual(r.status, 502);
});

/* ---------- Limite de débit ---------- */

test('limite de débit : 5 par minute et par IP, 429 avec Retry-After', async () => {
  for (let i = 0; i < 5; i += 1) assert.strictEqual((await call(artisan())).status, 503, 'requête ' + (i + 1));
  const r = await call(artisan());
  assert.strictEqual(r.status, 429);
  assert.deepStrictEqual(r.json, { ok: false, error: 'rate_limited' });
  const retry = Number(r.headers['retry-after']);
  assert.ok(retry >= 1 && retry <= 60);
  // une autre IP (premier saut de x-forwarded-for) n'est pas touchée
  assert.strictEqual((await call(artisan(), { headers: { 'x-forwarded-for': '198.51.100.9, 203.0.113.7' } })).status, 503);
});

/* ---------- Journal ---------- */

test('aucune donnée personnelle dans les journaux', async () => {
  useResend();
  process.env.LEAD_WEBHOOK_URL = 'https://hooks.example.test/lead';
  mockFetch(() => okRes);
  await call(artisan({ email: 'jean@durand.fr' }));
  await call(particulier());
  await call(artisan({ telephone: '12' }));
  mockFetch(() => ({ ok: false, status: 500 }));
  await call(artisan());
  const all = logs.join('\n');
  assert.ok(logs.length >= 4);
  for (const secret of ['Jean', 'Marie', 'Durand', '612345678', '712345678', '80000', '75004', 'jean@', '203.0.113.7', 're_test_key', 'example.test']) {
    assert.ok(!all.includes(secret), secret);
  }
  assert.ok(all.includes('"type":"artisan"') && all.includes('"type":"particulier"'));
  assert.ok(all.includes('"outcome":"delivered"') && all.includes('"outcome":"invalid"') && all.includes('"outcome":"delivery_failed"'));
});

/* ---------- Google Sheets (Apps Script) ---------- */

const SHEET_URL = 'https://script.google.com/macros/s/AKfycbTEST_abcdefghij-0123456789/exec';
const SHEET_KEY = 'k'.repeat(48);
const ECHO = 'https://script.googleusercontent.com/macros/echo?user_content_key=abc&lib=x';
function useSheet() { process.env.LEAD_SHEET_URL = SHEET_URL; process.env.LEAD_SHEET_KEY = SHEET_KEY; }
const res302 = (loc) => ({ ok: false, status: 302, headers: { get: (h) => (h.toLowerCase() === 'location' ? loc : null) } });
const resJson = (o, status = 200) => ({ ok: status < 300, status, headers: { get: () => null }, text: async () => JSON.stringify(o) });

test('tableau : POST sans suivre la redirection, puis GET de la réponse Apps Script', async () => {
  useSheet();
  mockFetch((url, init) => (url === SHEET_URL ? res302(ECHO) : resJson({ ok: true })));
  const r = await call(particulier());
  assert.strictEqual(r.status, 200);
  assert.deepStrictEqual(r.json, { ok: true });
  assert.strictEqual(calls.length, 2);
  assert.strictEqual(calls[0].init.method, 'POST');
  assert.strictEqual(calls[0].init.redirect, 'manual');
  const sent = JSON.parse(calls[0].init.body);
  assert.strictEqual(sent.cle, SHEET_KEY);
  assert.strictEqual(sent.lead.type, 'particulier');
  assert.strictEqual(sent.lead.fields.telephone, '+33712345678');
  assert.ok(sent.lead.consent && sent.lead.consent.at);
  assert.strictEqual(calls[1].url, ECHO);
  assert.strictEqual(calls[1].init.method, 'GET');
  assert.strictEqual(calls[1].init.redirect, 'error');
});

test('tableau : réponse directe sans redirection acceptée', async () => {
  useSheet();
  mockFetch(() => resJson({ ok: true }));
  const r = await call(artisan());
  assert.strictEqual(r.status, 200);
  assert.strictEqual(calls.length, 1);
});

test('tableau : redirection vers un autre hôte refusée', async () => {
  useSheet();
  for (const loc of ['https://evil.example/x', 'http://script.googleusercontent.com/macros/echo', 'pas une adresse']) {
    calls = [];
    mockFetch((url) => (url === SHEET_URL ? res302(loc) : resJson({ ok: true })));
    const r = await call(artisan());
    assert.strictEqual(r.status, 502, loc);
    assert.strictEqual(calls.length, 1, loc);
  }
});

test('tableau : clé refusée ou réponse illisible = échec, sans détail au visiteur', async () => {
  useSheet();
  for (const reply of [resJson({ ok: false, error: 'cle' }), { ok: true, status: 200, headers: { get: () => null }, text: async () => '<html>' }, resJson({ ok: true }, 500)]) {
    mockFetch((url) => (url === SHEET_URL ? res302(ECHO) : reply));
    const r = await call(particulier());
    assert.strictEqual(r.status, 502);
    assert.deepStrictEqual(r.json, { ok: false, error: 'delivery_failed' });
  }
  assert.ok(!logs.join('\n').includes('Marie'), 'aucune donnée personnelle dans les journaux');
});

test('tableau : adresse ou clé non conformes = non configuré, aucun appel', async () => {
  for (const [url, key] of [['https://example.com/macros/s/AKfycbTEST_abcdefghij/exec', SHEET_KEY], ['http://script.google.com/macros/s/AKfycbTEST_abcdefghij/exec', SHEET_KEY],
    ['https://script.google.com/macros/s/AKfycbTEST_abcdefghij/exec?x=1', SHEET_KEY], [SHEET_URL, 'court'], [SHEET_URL, '']]) {
    process.env.LEAD_SHEET_URL = url; process.env.LEAD_SHEET_KEY = key; calls = [];
    mockFetch(() => resJson({ ok: true }));
    const r = await call(artisan());
    assert.strictEqual(r.status, 503, url + ' ' + key);
    assert.strictEqual(calls.length, 0);
  }
});

test('tableau et e-mail ensemble : un seul canal qui réussit suffit', async () => {
  useSheet(); useResend();
  mockFetch((url) => (url === 'https://api.resend.com/emails' ? { ok: false, status: 500 } : url === SHEET_URL ? res302(ECHO) : resJson({ ok: true })));
  const r = await call(particulier());
  assert.strictEqual(r.status, 200);
});

'use strict';
/**
 * POST /api/lead : réception des deux formulaires du site Bartier & Co
 * (artisans et particuliers). Fonction Vercel Node.js, CommonJS, sans dépendance.
 *
 * Variables d'environnement (toutes facultatives, aucune adresse ni clé dans le code) :
 *   RESEND_API_KEY       clé API Resend
 *   LEAD_TO              destinataire(s) des demandes, séparés par des virgules
 *   LEAD_FROM            expéditeur vérifié chez Resend ("Nom <adresse>")
 *   LEAD_WEBHOOK_URL     webhook générique (https uniquement), reçoit la demande en JSON
 *   LEAD_WEBHOOK_SECRET  si présent : en-tête X-Bartier-Signature = HMAC-SHA256 hex du corps
 *   LEAD_SHEET_URL       adresse /exec de l'application Web Apps Script liée au Google Sheet des demandes
 *   LEAD_SHEET_KEY       clé partagée avec ce script (constante CLE de _build/sheets/apps-script.gs)
 *
 * Aucune donnée personnelle n'est journalisée : seuls le type, l'issue et des codes d'erreur.
 * L'adresse IP sert uniquement à la limite de débit en mémoire : elle n'est ni stockée ni transmise.
 */
const crypto = require('node:crypto');

const MAX_BODY = 10 * 1024;
const TIMEOUT_MS = 8000;
const RATE_MAX = 5;
const RATE_WINDOW_MS = 60 * 1000;

const CAP_NAME = 80;
const CAP_TEXT = 1000;
const CAP_URL = 300;
const CAP_PARAM = 200;
const CAP_EMAIL = 254;

const ALLOWED_HOSTS = ['bartierandco.com', 'www.bartierandco.com', 'bartier-8b.vercel.app', 'localhost', '127.0.0.1'];

const METIERS = ['couverture', 'facade', 'menuiserie', 'charpente', 'isolation', 'autre'];
const EQUIPES = ['1', '2', '3+'];
const CAPACITES = ['oui', 'bientot', 'ne-sait-pas'];

// Valeurs du formulaire particulier (_build/particuliers.py : TRADES, build() et js()).
const BESOINS = {
  toiture: ['Fuite ou dégât urgent', 'Réfection complète', 'Réparation, tuiles, zinguerie', 'Démoussage, nettoyage'],
  facade: ['Ravalement complet', 'Fissures, réparation', 'Nettoyage, peinture', 'Isolation par l’extérieur'],
  fenetres: ['Remplacer des fenêtres', 'Porte d’entrée', 'Baie vitrée', 'Volets'],
  charpente: ['Réparation, renfort', 'Traitement du bois', 'Extension, surélévation', 'Charpente neuve'],
  isolation: ['Combles', 'Murs par l’extérieur', 'Toiture', 'Je ne sais pas encore'],
  autre: ['Rénovation globale', 'Extension', 'Autre projet'],
};
const DELAIS = ['Dès que possible', 'Dans 1 à 3 mois', 'Dans plus de 3 mois', 'Je compare des prix'];
// "Locataire" existe dans le formulaire mais bloque l'envoi : seuls les propriétaires peuvent soumettre.
const STATUTS = ['Propriétaire occupant', 'Propriétaire bailleur'];

const LABELS = {
  metier: 'Métier', equipes: 'Équipes', capacite: 'Capacité à prendre des chantiers', entreprise: 'Entreprise',
  travaux: 'Travaux', besoin: 'Besoin', delai: 'Délai', statut: 'Statut',
  code_postal: 'Code postal', prenom: 'Prénom', telephone: 'Téléphone', email: 'E-mail',
};
const FIELD_ORDER = ['entreprise', 'metier', 'equipes', 'capacite', 'travaux', 'besoin', 'delai', 'statut',
  'code_postal', 'prenom', 'telephone', 'email'];
const TRACKING = ['utm_source', 'utm_medium', 'utm_campaign', 'utm_content', 'gclid', 'fbclid'];

/* ---------- Nettoyage ---------- */

// Retire les caractères de contrôle (dont CR, LF, tabulation) et les séparateurs de ligne Unicode.
function clean(value, max) {
  if (typeof value === 'number' && Number.isFinite(value)) value = String(value);
  if (typeof value !== 'string') return '';
  const s = value.replace(/[\u0000-\u001F\u007F-\u009F\u2028\u2029]+/g, ' ').replace(/\s+/g, ' ').trim();
  return s.slice(0, max);
}

// Pour tout ce qui part dans un en-tête de message (sujet, reply_to).
function oneLine(value) {
  return String(value == null ? '' : value).replace(/[\r\n\u0085\u2028\u2029]+/g, ' ').replace(/[\u0000-\u001F\u007F]/g, '').trim();
}

function escapeHtml(value) {
  return String(value == null ? '' : value)
    .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;').replace(/'/g, '&#39;');
}

// Comparaison tolérante : apostrophe droite ou courbe, espaces insécables, casse.
function loose(s) {
  return String(s).replace(/[’‘ʼ]/g, "'").replace(/[\u00A0\u202F]/g, ' ').replace(/\s+/g, ' ').trim().toLowerCase();
}
function pick(value, allowed) {
  const v = loose(value);
  if (!v) return null;
  for (const a of allowed) if (loose(a) === v) return a;
  return null;
}

/**
 * Téléphone français : 0X XX XX XX XX, +33 X XX XX XX XX, 0033 X..., avec espaces, points ou tirets.
 * Le (0) ou 0 après l'indicatif (+33 (0)6..., +3306...) est toléré. Retourne "+33XXXXXXXXX" ou null.
 */
function normalisePhone(input) {
  if (typeof input === 'number' && Number.isFinite(input)) input = String(input);
  if (typeof input !== 'string') return null;
  let s = input.trim();
  if (!s || s.length > 30) return null;
  if (!/^[+\d][\d\s.\-()\u00A0\u202F]*$/.test(s)) return null;
  s = s.replace(/[\s.\-\u00A0\u202F]/g, '');
  let m = /^(?:\+33|0033)(?:\(0\)|0)?([1-9]\d{8})$/.exec(s);
  if (!m) m = /^0([1-9]\d{8})$/.exec(s);
  return m ? '+33' + m[1] : null;
}

function validEmail(s) {
  return s.length <= CAP_EMAIL && /^[^\s@<>(),;:"\\]+@[^\s@<>(),;:"\\]+\.[A-Za-z]{2,}$/.test(s) && !/\.\./.test(s);
}

function isoDate(value) {
  if (typeof value !== 'string') return null;
  const s = value.trim();
  if (!/^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}(:\d{2}(\.\d{1,9})?)?(Z|[+-]\d{2}:?\d{2})$/.test(s)) return null;
  const t = Date.parse(s);
  return Number.isNaN(t) ? null : new Date(t).toISOString();
}

/* ---------- Validation ---------- */

/**
 * Valide et normalise la charge utile. Retourne { ok:true, lead } ou { ok:false, error:"invalid", field }.
 * Le lead ne contient que des champs connus : rien d'autre de la requête n'est repris.
 */
function validate(payload, now) {
  const bad = (field) => ({ ok: false, error: 'invalid', field });
  if (!payload || typeof payload !== 'object' || Array.isArray(payload)) return bad('payload');
  const type = payload.type;
  if (type !== 'artisan' && type !== 'particulier') return bad('type');
  const src = payload.fields;
  if (!src || typeof src !== 'object' || Array.isArray(src)) return bad('fields');

  const fields = {};

  if (type === 'artisan') {
    const metier = pick(clean(src.metier, CAP_NAME), METIERS);
    if (!metier) return bad('metier');
    fields.metier = metier;
  } else {
    const travaux = pick(clean(src.travaux, CAP_NAME), Object.keys(BESOINS));
    if (!travaux) return bad('travaux');
    fields.travaux = travaux;
    const besoin = pick(clean(src.besoin, CAP_NAME), BESOINS[travaux]);
    if (!besoin) return bad('besoin');
    fields.besoin = besoin;
    const delai = pick(clean(src.delai, CAP_NAME), DELAIS);
    if (!delai) return bad('delai');
    fields.delai = delai;
    const statut = pick(clean(src.statut, CAP_NAME), STATUTS);
    if (!statut) return bad('statut');
    fields.statut = statut;
  }

  const cp = clean(src.code_postal, 20);
  if (!/^\d{5}$/.test(cp)) return bad('code_postal');
  fields.code_postal = cp;

  if (type === 'artisan') {
    const equipes = pick(clean(src.equipes, CAP_NAME), EQUIPES);
    if (!equipes) return bad('equipes');
    fields.equipes = equipes;
    const capacite = pick(clean(src.capacite, CAP_NAME), CAPACITES);
    if (!capacite) return bad('capacite');
    fields.capacite = capacite;
  }

  const prenom = clean(src.prenom, CAP_NAME);
  if (prenom.length < 2) return bad('prenom');
  fields.prenom = prenom;

  const telephone = normalisePhone(typeof src.telephone === 'string' ? clean(src.telephone, 40) : src.telephone);
  if (!telephone) return bad('telephone');
  fields.telephone = telephone;

  if (type === 'artisan') {
    const entreprise = clean(src.entreprise, CAP_NAME);
    if (entreprise.length < 2) return bad('entreprise');
    fields.entreprise = entreprise;
  }

  if (src.email != null && src.email !== '') {
    const email = clean(src.email, CAP_EMAIL + 1);
    if (!validEmail(email)) return bad('email');
    fields.email = email;
  }

  const lead = {
    type,
    received_at: new Date(now == null ? Date.now() : now).toISOString(),
    fields,
    page: clean(payload.page, CAP_URL),
  };
  for (const k of TRACKING) lead[k] = clean(payload[k], CAP_PARAM);

  // Preuve de consentement : obligatoire pour les particuliers, reprise si fournie pour les artisans.
  const c = payload.consent;
  const text = c && typeof c === 'object' ? clean(c.text, CAP_TEXT) : '';
  const at = c && typeof c === 'object' ? isoDate(c.at) : null;
  if (type === 'particulier') {
    if (!text) return bad('consent');
    if (!at) return bad('consent');
    lead.consent = { text, at };
  } else if (text && at) {
    lead.consent = { text, at };
  }

  return { ok: true, lead };
}

/* ---------- E-mail ---------- */

function buildEmail(lead) {
  const f = lead.fields || {};
  const subject = oneLine(lead.type === 'artisan'
    ? `Nouveau artisan : ${f.entreprise} (${f.code_postal})`
    : `Nouveau particulier : ${f.travaux} (${f.code_postal})`).slice(0, 200);

  const rows = [];
  for (const k of FIELD_ORDER) if (f[k]) rows.push([LABELS[k], f[k]]);
  rows.push(['Reçu le', lead.received_at]);
  if (lead.page) rows.push(['Page', lead.page]);
  for (const k of TRACKING) if (lead[k]) rows.push([k, lead[k]]);
  if (lead.consent) {
    rows.push(['Consentement', lead.consent.text]);
    rows.push(['Consentement donné le', lead.consent.at]);
  }

  const title = lead.type === 'artisan' ? 'Nouvelle demande artisan' : 'Nouvelle demande particulier';
  const text = title + '\n\n' + rows.map(([l, v]) => `${l} : ${v}`).join('\n') + '\n';
  const html = '<!doctype html><html lang="fr"><body style="font-family:Arial,Helvetica,sans-serif;font-size:15px;color:#111">'
    + `<h1 style="font-size:18px;margin:0 0 12px">${escapeHtml(title)}</h1>`
    + '<table cellpadding="6" cellspacing="0" style="border-collapse:collapse">'
    + rows.map(([l, v]) => '<tr><th align="left" valign="top" style="border-bottom:1px solid #ddd;font-weight:600">'
      + `${escapeHtml(l)}</th><td style="border-bottom:1px solid #ddd">${escapeHtml(v)}</td></tr>`).join('')
    + '</table></body></html>';

  const email = { subject, text, html };
  const reply = oneLine(f.email || '');
  if (reply && validEmail(reply)) email.reply_to = reply;
  return email;
}

/* ---------- Livraison ---------- */

async function post(url, headers, body) {
  const ctrl = new AbortController();
  const timer = setTimeout(() => ctrl.abort(), TIMEOUT_MS);
  try {
    const r = await fetch(url, { method: 'POST', headers, body, signal: ctrl.signal, redirect: 'error' });
    return r && r.ok ? null : 'http_' + (r ? r.status : 0);
  } catch (e) {
    return e && e.name === 'AbortError' ? 'timeout' : 'network';
  } finally {
    clearTimeout(timer);
  }
}

function sendResend(lead, env) {
  const mail = buildEmail(lead);
  const to = String(env.LEAD_TO).split(',').map((s) => s.trim()).filter(Boolean);
  const body = { from: oneLine(env.LEAD_FROM), to, subject: mail.subject, text: mail.text, html: mail.html };
  if (mail.reply_to) body.reply_to = mail.reply_to;
  return post('https://api.resend.com/emails',
    { Authorization: 'Bearer ' + String(env.RESEND_API_KEY).trim(), 'Content-Type': 'application/json' },
    JSON.stringify(body));
}

function sendWebhook(lead, env) {
  const body = JSON.stringify(lead);
  const headers = { 'Content-Type': 'application/json' };
  if (env.LEAD_WEBHOOK_SECRET) {
    headers['X-Bartier-Signature'] = crypto.createHmac('sha256', env.LEAD_WEBHOOK_SECRET).update(body).digest('hex');
  }
  return post(env.LEAD_WEBHOOK_URL.trim(), headers, body);
}

// Google Sheets, par une application Web Apps Script (_build/sheets/apps-script.gs).
// Apps Script exécute doPost puis répond par une redirection vers sa réponse, servie par
// script.googleusercontent.com : on suit cette seule redirection, vers ce seul hôte, en GET.
function sheetUrl(value) {
  try {
    const u = new URL(String(value).trim());
    return u.protocol === 'https:' && u.hostname === 'script.google.com' && /^\/macros\/s\/[\w-]{10,}\/exec$/.test(u.pathname) && !u.search && !u.hash;
  } catch (e) { return false; }
}

async function sendSheet(lead, env) {
  const ctrl = new AbortController();
  const timer = setTimeout(() => ctrl.abort(), TIMEOUT_MS);
  try {
    const body = JSON.stringify({ cle: String(env.LEAD_SHEET_KEY).trim(), lead });
    let r = await fetch(String(env.LEAD_SHEET_URL).trim(), { method: 'POST', headers: { 'Content-Type': 'application/json' }, body, signal: ctrl.signal, redirect: 'manual' });
    if (r.status === 301 || r.status === 302 || r.status === 303) {
      let loc;
      try { loc = new URL(r.headers.get('location') || ''); } catch (e) { return 'bad_redirect'; }
      if (loc.protocol !== 'https:' || loc.hostname !== 'script.googleusercontent.com') return 'bad_redirect';
      r = await fetch(loc.href, { method: 'GET', signal: ctrl.signal, redirect: 'error' });
    }
    if (!r.ok) return 'http_' + r.status;
    let j = null;
    try { j = JSON.parse(await r.text()); } catch (e) { j = null; }
    return j && j.ok === true ? null : 'sheet_' + (j && typeof j.error === 'string' ? j.error.slice(0, 20).replace(/[^a-z_]/g, '') : 'bad_response');
  } catch (e) {
    return e && e.name === 'AbortError' ? 'timeout' : 'network';
  } finally {
    clearTimeout(timer);
  }
}

function httpsUrl(value) {
  try { return new URL(String(value).trim()).protocol === 'https:'; } catch (e) { return false; }
}

/* ---------- Origine, débit, corps ---------- */

function allowedOrigin(headers) {
  const raw = headers.origin || headers.referer || headers.referrer;
  if (!raw || typeof raw !== 'string') return false;
  let host;
  try {
    const u = new URL(raw);
    if (u.protocol !== 'https:' && u.protocol !== 'http:') return false;
    host = u.hostname.toLowerCase();
  } catch (e) { return false; }
  if (ALLOWED_HOSTS.includes(host)) return true;
  // Aperçus Vercel du projet : bartier-8b-<suffixe>.vercel.app
  return host.startsWith('bartier-8b') && host.endsWith('.vercel.app');
}

// Limite de débit au mieux : en mémoire, donc PAR INSTANCE de la fonction. Chaque instance
// (et chaque démarrage à froid) a son propre compteur : ce n'est pas une limite globale.
const hits = new Map();
function rateLimited(ip, now) {
  if (hits.size > 5000) {
    for (const [k, v] of hits) if (now - v[v.length - 1] >= RATE_WINDOW_MS) hits.delete(k);
    if (hits.size > 5000) hits.clear();
  }
  const list = (hits.get(ip) || []).filter((t) => now - t < RATE_WINDOW_MS);
  if (list.length >= RATE_MAX) {
    hits.set(ip, list);
    return Math.max(1, Math.ceil((RATE_WINDOW_MS - (now - list[0])) / 1000));
  }
  list.push(now);
  hits.set(ip, list);
  return 0;
}
function clientIp(req) {
  const xff = req.headers['x-forwarded-for'];
  const first = (Array.isArray(xff) ? xff[0] : String(xff || '')).split(',')[0].trim();
  return first || (req.socket && req.socket.remoteAddress) || 'unknown';
}

function readStream(req) {
  return new Promise((resolve, reject) => {
    if (!req || typeof req.on !== 'function' || req.readableEnded || req.complete === true && req.readable === false) {
      return resolve('');
    }
    const chunks = [];
    let size = 0;
    let done = false;
    const finish = (fn, v) => { if (!done) { done = true; fn(v); } };
    req.on('data', (c) => {
      size += c.length;
      if (size > MAX_BODY) { finish(reject, Object.assign(new Error('too_large'), { code: 'too_large' })); return; }
      chunks.push(typeof c === 'string' ? Buffer.from(c) : c);
    });
    req.on('end', () => finish(resolve, Buffer.concat(chunks).toString('utf8')));
    req.on('error', () => finish(reject, Object.assign(new Error('bad_json'), { code: 'bad_json' })));
  });
}

// req.body peut être un objet (déjà analysé par Vercel), une chaîne, un Buffer, ou absent.
async function readBody(req) {
  const fail = (code) => { throw Object.assign(new Error(code), { code }); };
  if (Number(req.headers['content-length']) > MAX_BODY) fail('too_large');
  let body;
  try { body = req.body; } catch (e) { fail('bad_json'); } // l'accesseur de Vercel lève sur un JSON invalide
  if (Buffer.isBuffer(body)) body = body.toString('utf8');
  if (body == null) body = await readStream(req);
  if (typeof body === 'string') {
    if (Buffer.byteLength(body) > MAX_BODY) fail('too_large');
    try { body = JSON.parse(body); } catch (e) { fail('bad_json'); }
  } else if (typeof body === 'object') {
    let n = 0;
    try { n = Buffer.byteLength(JSON.stringify(body)); } catch (e) { fail('bad_json'); }
    if (n > MAX_BODY) fail('too_large');
  }
  if (!body || typeof body !== 'object' || Array.isArray(body)) fail('bad_json');
  return body;
}

/* ---------- Réponse et journal ---------- */

function send(res, status, data, extra) {
  res.statusCode = status;
  res.setHeader('Content-Type', 'application/json; charset=utf-8');
  res.setHeader('Cache-Control', 'no-store');
  if (extra) for (const k of Object.keys(extra)) res.setHeader(k, extra[k]);
  res.end(JSON.stringify(data));
}

// Jamais de donnée personnelle ici : type, issue et codes d'erreur uniquement.
function log(type, outcome, errors) {
  const t = type === 'artisan' || type === 'particulier' ? type : 'unknown';
  console.log(JSON.stringify({ evt: 'lead', type: t, outcome, errors: errors || [] }));
}

/* ---------- Gestionnaire ---------- */

async function handler(req, res) {
  const headers = req.headers || {};
  if (req.method !== 'POST') {
    log(null, 'method_not_allowed');
    return send(res, 405, { ok: false, error: 'method_not_allowed' }, { Allow: 'POST' });
  }
  if (!allowedOrigin(headers)) {
    log(null, 'forbidden_origin');
    return send(res, 403, { ok: false, error: 'forbidden' });
  }
  const retry = rateLimited(clientIp(req), Date.now());
  if (retry) {
    log(null, 'rate_limited');
    return send(res, 429, { ok: false, error: 'rate_limited' }, { 'Retry-After': String(retry) });
  }
  if (!/^application\/json\s*(;|$)/i.test(String(headers['content-type'] || '').trim())) {
    log(null, 'unsupported_media_type');
    return send(res, 415, { ok: false, error: 'unsupported_media_type' });
  }

  let payload;
  try {
    payload = await readBody(req);
  } catch (e) {
    const tooLarge = e && e.code === 'too_large';
    log(null, tooLarge ? 'too_large' : 'bad_json');
    return send(res, tooLarge ? 413 : 400, { ok: false, error: tooLarge ? 'too_large' : 'bad_json' });
  }

  // Pot de miel : un robot a rempli le champ caché. On répond comme si tout allait bien, sans rien faire.
  if (payload.site_web != null && String(payload.site_web).trim() !== '') {
    log(payload.type, 'honeypot');
    return send(res, 200, { ok: true });
  }

  const v = validate(payload);
  if (!v.ok) {
    log(payload.type, 'invalid', [v.field]);
    return send(res, 422, v);
  }
  const lead = v.lead;

  const env = process.env;
  const errors = [];
  const jobs = [];
  if (env.RESEND_API_KEY && env.LEAD_TO && env.LEAD_FROM) jobs.push(['resend', sendResend(lead, env)]);
  if (env.LEAD_SHEET_URL) {
    if (sheetUrl(env.LEAD_SHEET_URL) && env.LEAD_SHEET_KEY && String(env.LEAD_SHEET_KEY).trim().length >= 24) jobs.push(['sheet', sendSheet(lead, env)]);
    else errors.push('sheet:bad_config');
  }
  if (env.LEAD_WEBHOOK_URL) {
    if (httpsUrl(env.LEAD_WEBHOOK_URL)) jobs.push(['webhook', sendWebhook(lead, env)]);
    else errors.push('webhook:not_https');
  }
  if (!jobs.length) {
    log(lead.type, 'not_configured', errors);
    return send(res, 503, { ok: false, error: 'not_configured' });
  }

  const results = await Promise.all(jobs.map((j) => j[1].catch(() => 'error')));
  let delivered = 0;
  results.forEach((err, i) => { if (err) errors.push(jobs[i][0] + ':' + err); else delivered += 1; });
  if (!delivered) {
    log(lead.type, 'delivery_failed', errors);
    return send(res, 502, { ok: false, error: 'delivery_failed' });
  }
  log(lead.type, 'delivered', errors);
  return send(res, 200, { ok: true });
}

module.exports = async (req, res) => {
  try {
    return await handler(req, res);
  } catch (e) {
    log(null, 'server_error');
    return send(res, 500, { ok: false, error: 'server_error' });
  }
};
module.exports.normalisePhone = normalisePhone;
module.exports.validate = validate;
module.exports.buildEmail = buildEmail;
module.exports.escapeHtml = escapeHtml;
module.exports._resetRateLimit = () => hits.clear();

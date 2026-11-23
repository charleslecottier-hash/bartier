'use strict';
/**
 * POST /api/lead/ : reçoit la demande d'une page d'estimation client et
 *   1. crée ou met à jour le contact dans GoHighLevel (étiquette « demande-estimation » et note détaillée),
 *      ce qui déclenche l'automatisation de prise de rendez-vous ; et/ou l'écrit en une ligne dans le Google Sheet
 *      des demandes (application Web Apps Script, sheets/apps-script.gs). Il faut au moins l'un des deux ;
 *   2. si le visiteur a donné son accord (cookies acceptés, ou « oui » à la question de la dernière étape), envoie l'événement « Lead »
 *      à l'API Conversions de Meta, avec l'identifiant de clic lu dans l'adresse de la page.
 *
 * Fichier source : lp-estimation/api_lead.js. build.py le copie dans dist/<client>/api/lead.js
 * en remplissant les constantes CLIENT, METIERS, PIXEL et ALERTE. Fonction Vercel Node.js, CommonJS, sans dépendance.
 *
 * Variables d'environnement du projet Vercel du client (aucune adresse ni clé dans le code) :
 *   GHL_TOKEN              jeton d'intégration privée du sous-compte GoHighLevel du client (droit contacts.write)
 *   GHL_LOCATION_ID        identifiant du sous-compte (Location ID)
 *   LEAD_SHEET_URL         facultatif avec GoHighLevel : adresse /exec de l'application Web Apps Script
 *   LEAD_SHEET_KEY         clé partagée avec ce script (constante CLE de sheets/apps-script.gs)
 *   META_ACCESS_TOKEN      facultatif : jeton d'accès de l'API Conversions (Gestionnaire d'événements)
 *   META_TEST_EVENT_CODE   facultatif : code de test du Gestionnaire d'événements, à retirer après les essais
 *   META_API_VERSION       facultatif : version de l'API Graph (par défaut v23.0)
 *
 * Aucune donnée personnelle n'est journalisée : seulement l'issue et des codes d'erreur.
 */

const CLIENT = __CLIENT__;
const METIERS = __METIERS__;
const PIXEL = __PIXEL__;
const ALERTE = __ALERTE__; // adresses de l'artisan prévenues à chaque demande (fiche client : alerte_email)

const MAX_BODY = 10 * 1024;
const TIMEOUT_MS = 8000;
const RATE_MAX = 5;
const RATE_WINDOW_MS = 60 * 1000;
const TRACKING = ['utm_source', 'utm_medium', 'utm_campaign', 'utm_content', 'utm_term', 'gclid', 'gbraid', 'wbraid', 'fbclid'];
const ACCORDS = ['cookies', 'question', 'non', 'sans objet'];

/* ---------- Nettoyage ---------- */

function clean(value, max) {
  if (typeof value === 'number' && Number.isFinite(value)) value = String(value);
  if (typeof value !== 'string') return '';
  return value.replace(/[\u0000-\u001F\u007F-\u009F\u2028\u2029]+/g, ' ').replace(/\s+/g, ' ').trim().slice(0, max);
}

// Téléphone français : 0X XX XX XX XX, +33 X..., 0033 X..., avec espaces, points ou tirets. Retourne "+33XXXXXXXXX" ou null.
function normalisePhone(input) {
  if (typeof input !== 'string') return null;
  let s = input.trim();
  if (!s || s.length > 30 || !/^[+\d][\d\s.\-()  ]*$/.test(s)) return null;
  s = s.replace(/[\s.\-  ]/g, '');
  const m = /^(?:\+33|0033)(?:\(0\)|0)?([1-9]\d{8})$/.exec(s) || /^0([1-9]\d{8})$/.exec(s);
  return m ? '+33' + m[1] : null;
}

function isoDate(value) {
  if (typeof value !== 'string' || !/^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}/.test(value)) return '';
  const t = Date.parse(value);
  return Number.isNaN(t) ? '' : new Date(t).toISOString();
}

/* ---------- Validation ---------- */

function validate(p, now) {
  const bad = (field) => ({ ok: false, field });
  if (!p || typeof p !== 'object' || Array.isArray(p)) return bad('payload');
  if (p.type !== 'estimation') return bad('type');
  if (!Object.prototype.hasOwnProperty.call(METIERS, p.metier)) return bad('metier');
  const src = p.fields;
  if (!src || typeof src !== 'object' || Array.isArray(src)) return bad('fields');
  const prenom = clean(src.prenom, 60);
  if (prenom.length < 2) return bad('prenom');
  const telephone = normalisePhone(src.telephone);
  if (!telephone) return bad('telephone');
  const cp = clean(src.code_postal, 5);
  if (cp && !/^\d{5}$/.test(cp)) return bad('code_postal');
  const details = Array.isArray(src.details) ? src.details.slice(0, 12).map((x) => clean(x, 200)).filter(Boolean) : [];
  const tracking = {};
  const t = p.tracking && typeof p.tracking === 'object' && !Array.isArray(p.tracking) ? p.tracking : {};
  for (const k of TRACKING) {
    const v = clean(t[k], 200);
    if (v && /^[\w.~%+\-=/:]+$/.test(v)) tracking[k] = v;
  }
  const eid = clean(p.eid, 64);
  if (!/^[A-Za-z0-9-]{8,64}$/.test(eid)) return bad('eid');
  const accord = ACCORDS.includes(p.accord) ? p.accord : 'non';
  const clicAt = Number(p.clic_at);
  const page = clean(p.page, 200);
  const c = p.consent && typeof p.consent === 'object' ? p.consent : {};
  return {
    ok: true,
    lead: {
      received_at: new Date(now).toISOString(),
      eid,
      metier: METIERS[p.metier],
      fields: {
        prenom, telephone, code_postal: cp, commune: clean(src.commune, 80),
        travaux: clean(src.travaux, 120), quantite: clean(src.quantite, 120), estimation: clean(src.estimation, 120),
        details: details.join(' · '), delai: clean(src.delai, 80), statut: clean(src.statut, 80),
      },
      accord,
      page: /^\/[\w\-/]*$/.test(page) ? page : '',
      tracking,
      clic_at: Number.isFinite(clicAt) && clicAt > now - 7 * 864e5 && clicAt <= now + 6e4 ? Math.floor(clicAt) : now,
      fbp: /^fb\.\d\.\d{10,13}\.\d{5,25}$/.test(clean(p.fbp, 60)) ? clean(p.fbp, 60) : '',
      consent: { text: clean(c.text, 300), at: isoDate(c.at) },
    },
  };
}

/* ---------- Google Sheet (Apps Script) ---------- */

function sheetUrl(value) {
  try {
    const u = new URL(String(value).trim());
    return u.protocol === 'https:' && u.hostname === 'script.google.com' && /^\/macros\/s\/[\w-]{10,}\/exec$/.test(u.pathname) && !u.search && !u.hash;
  } catch (e) { return false; }
}

// Apps Script exécute doPost puis répond par une redirection vers sa réponse (script.googleusercontent.com) :
// on suit cette seule redirection, vers ce seul hôte, en GET.
async function sendSheet(lead, env) {
  const ctrl = new AbortController();
  const timer = setTimeout(() => ctrl.abort(), TIMEOUT_MS);
  try {
    const body = JSON.stringify({ cle: String(env.LEAD_SHEET_KEY).trim(), client: CLIENT, alerte: ALERTE, lead });
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

/* ---------- GoHighLevel ---------- */

const GHL = 'https://services.leadconnectorhq.com';

function ghlOn(env) {
  return !!(env.GHL_TOKEN && String(env.GHL_TOKEN).trim().length >= 20 && /^[A-Za-z0-9]{10,40}$/.test(String(env.GHL_LOCATION_ID || '').trim()));
}

function slugTag(v) {
  return String(v).normalize('NFD').replace(/[̀-ͯ]/g, '').toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '');
}

// La note lue par le téléprospecteur : la demande complète, en clair.
function noteGhl(lead) {
  const f = lead.fields, t = lead.tracking;
  const l = [
    'Demande d’estimation : ' + lead.metier + (lead.page ? ' (page ' + lead.page + ')' : ''),
    'Travaux : ' + (f.travaux || '?'), f.quantite && 'Quantité : ' + f.quantite, f.estimation && 'Estimation affichée : ' + f.estimation,
    f.details && 'Détails : ' + f.details, f.delai && 'Délai : ' + f.delai, f.statut && 'Statut : ' + f.statut,
    'Lieu : ' + [f.code_postal, f.commune].filter(Boolean).join(' '),
    'Accord mesure des annonces : ' + lead.accord,
    Object.keys(t).length ? 'Source : ' + Object.keys(t).map((k) => k + '=' + t[k]).join(', ') : 'Source : accès direct',
    'ID de la demande : ' + lead.eid,
  ];
  return l.filter(Boolean).join('\n');
}

async function sendGhl(lead, env) {
  const ctrl = new AbortController();
  const timer = setTimeout(() => ctrl.abort(), TIMEOUT_MS);
  const headers = { Authorization: 'Bearer ' + String(env.GHL_TOKEN).trim(), Version: '2021-07-28', 'Content-Type': 'application/json', Accept: 'application/json' };
  try {
    const contact = {
      locationId: String(env.GHL_LOCATION_ID).trim(), firstName: lead.fields.prenom, phone: lead.fields.telephone,
      postalCode: lead.fields.code_postal || undefined, city: lead.fields.commune || undefined,
      source: 'Page d’estimation ' + CLIENT, tags: ['demande-estimation', 'metier-' + slugTag(lead.metier)],
    };
    const r = await fetch(GHL + '/contacts/upsert', { method: 'POST', headers, body: JSON.stringify(contact), signal: ctrl.signal });
    if (!r.ok) return 'ghl_http_' + r.status;
    let j = null;
    try { j = await r.json(); } catch (e) { j = null; }
    const id = j && j.contact && j.contact.id;
    if (!id || !/^[A-Za-z0-9]{6,64}$/.test(String(id))) return 'ghl_no_id';
    const n = await fetch(GHL + '/contacts/' + encodeURIComponent(id) + '/notes', { method: 'POST', headers, body: JSON.stringify({ body: noteGhl(lead) }), signal: ctrl.signal });
    return n.ok ? null : 'ghl_note_' + n.status; // le contact existe déjà : la demande n'est pas perdue
  } catch (e) {
    return e && e.name === 'AbortError' ? 'ghl_timeout' : 'ghl_network';
  } finally {
    clearTimeout(timer);
  }
}

/* ---------- API Conversions de Meta ---------- */

// Seulement avec l'accord du visiteur. Ni nom ni téléphone : identifiant de clic (fbc), cookie _fbp s'il existe,
// adresse IP et navigateur (demandés par Meta pour un événement de site).
async function sendMeta(lead, req, env) {
  if (!PIXEL || !env.META_ACCESS_TOKEN) return 'off';
  if (lead.accord !== 'cookies' && lead.accord !== 'question') return 'no_consent';
  const h = req.headers || {};
  const user = {};
  if (lead.tracking.fbclid) user.fbc = 'fb.1.' + lead.clic_at + '.' + lead.tracking.fbclid;
  if (lead.fbp && lead.accord === 'cookies') user.fbp = lead.fbp;
  const ip = String(h['x-forwarded-for'] || '').split(',')[0].trim();
  if (ip) user.client_ip_address = ip;
  if (h['user-agent']) user.client_user_agent = String(h['user-agent']).slice(0, 400);
  const host = String(h['x-forwarded-host'] || h.host || '').split(',')[0].trim();
  const payload = {
    data: [{
      event_name: 'Lead', event_time: Math.floor(Date.now() / 1000), event_id: lead.eid, action_source: 'website',
      event_source_url: 'https://' + host + (lead.page || '/'), user_data: user,
    }],
    access_token: String(env.META_ACCESS_TOKEN).trim(),
  };
  if (env.META_TEST_EVENT_CODE) payload.test_event_code = String(env.META_TEST_EVENT_CODE).trim();
  const ver = /^v\d{2}\.\d$/.test(String(env.META_API_VERSION || '')) ? env.META_API_VERSION : 'v23.0';
  const ctrl = new AbortController();
  const timer = setTimeout(() => ctrl.abort(), 5000);
  try {
    const r = await fetch(`https://graph.facebook.com/${ver}/${encodeURIComponent(PIXEL)}/events`, {
      method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(payload), signal: ctrl.signal,
    });
    return r.ok ? null : 'meta_http_' + r.status;
  } catch (e) {
    return e && e.name === 'AbortError' ? 'meta_timeout' : 'meta_network';
  } finally {
    clearTimeout(timer);
  }
}

/* ---------- Origine, débit, corps ---------- */

// La page et la fonction sont sur le même domaine : l'origine de la requête doit être ce domaine.
function sameOrigin(h) {
  const raw = h.origin || h.referer;
  const host = String(h['x-forwarded-host'] || h.host || '').split(',')[0].trim().toLowerCase().replace(/:\d+$/, '');
  if (!raw || !host) return false;
  try { return new URL(raw).hostname.toLowerCase() === host; } catch (e) { return false; }
}

const hits = new Map(); // limite par instance de la fonction, au mieux
function rateLimited(ip, now) {
  if (hits.size > 5000) hits.clear();
  const list = (hits.get(ip) || []).filter((t) => now - t < RATE_WINDOW_MS);
  if (list.length >= RATE_MAX) { hits.set(ip, list); return true; }
  list.push(now);
  hits.set(ip, list);
  return false;
}

async function readBody(req) {
  let body = req.body;
  if (Buffer.isBuffer(body)) body = body.toString('utf8');
  if (body == null) {
    body = await new Promise((resolve, reject) => {
      const chunks = [];
      let size = 0;
      req.on('data', (c) => { size += c.length; if (size > MAX_BODY) reject(new Error('too_large')); else chunks.push(c); });
      req.on('end', () => resolve(Buffer.concat(chunks).toString('utf8')));
      req.on('error', () => reject(new Error('bad_json')));
    });
  }
  if (typeof body === 'string') {
    if (Buffer.byteLength(body) > MAX_BODY) throw new Error('too_large');
    body = JSON.parse(body);
  }
  if (!body || typeof body !== 'object' || Array.isArray(body)) throw new Error('bad_json');
  if (Buffer.byteLength(JSON.stringify(body)) > MAX_BODY) throw new Error('too_large');
  return body;
}

function send(res, status, data) {
  res.statusCode = status;
  res.setHeader('Content-Type', 'application/json; charset=utf-8');
  res.setHeader('Cache-Control', 'no-store');
  res.end(JSON.stringify(data));
}

function log(outcome, errors) {
  console.log(JSON.stringify({ evt: 'lead', outcome, errors: errors || [] }));
}

/* ---------- Gestionnaire ---------- */

async function handler(req, res, env = process.env) {
  const h = req.headers || {};
  if (req.method !== 'POST') { res.setHeader('Allow', 'POST'); return send(res, 405, { ok: false, error: 'method_not_allowed' }); }
  if (!sameOrigin(h)) { log('forbidden_origin'); return send(res, 403, { ok: false, error: 'forbidden' }); }
  const ip = String(h['x-forwarded-for'] || '').split(',')[0].trim() || 'unknown';
  if (rateLimited(ip, Date.now())) { log('rate_limited'); return send(res, 429, { ok: false, error: 'rate_limited' }); }
  let payload;
  try { payload = await readBody(req); } catch (e) {
    const code = e && e.message === 'too_large' ? 'too_large' : 'bad_json';
    log(code);
    return send(res, code === 'too_large' ? 413 : 400, { ok: false, error: code });
  }
  // Champ piège invisible : un robot le remplit. On répond « reçu » sans rien enregistrer.
  if (clean(payload.site_web, 200)) { log('honeypot'); return send(res, 200, { ok: true }); }
  const v = validate(payload, Date.now());
  if (!v.ok) { log('invalid', [v.field]); return send(res, 422, { ok: false, error: 'invalid', field: v.field }); }
  const sheetOn = sheetUrl(env.LEAD_SHEET_URL) && env.LEAD_SHEET_KEY && String(env.LEAD_SHEET_KEY).trim().length >= 16;
  const crmOn = ghlOn(env);
  if (!sheetOn && !crmOn) {
    log('not_configured');
    return send(res, 503, { ok: false, error: 'not_configured' });
  }
  const [sheetErr, ghlErr, metaErr] = await Promise.all([
    sheetOn ? sendSheet(v.lead, env) : 'off', crmOn ? sendGhl(v.lead, env) : 'off', sendMeta(v.lead, req, env)]);
  const meta = metaErr === null ? 'meta_ok' : 'meta_' + String(metaErr).replace(/^meta_/, '');
  const codes = [crmOn ? (ghlErr === null ? 'ghl_ok' : ghlErr) : 'ghl_off', sheetOn ? (sheetErr === null ? 'sheet_ok' : sheetErr) : 'sheet_off', meta];
  // Enregistrée si au moins une destination réglée l'a reçue (GoHighLevel ou le tableau).
  if (!((crmOn && ghlErr === null) || (sheetOn && sheetErr === null))) { log('failed', codes); return send(res, 502, { ok: false, error: 'not_saved' }); }
  log('saved', codes);
  return send(res, 200, { ok: true });
}

module.exports = handler;
module.exports._test = { validate, normalisePhone, sameOrigin, sendMeta, sendSheet, sendGhl, noteGhl };

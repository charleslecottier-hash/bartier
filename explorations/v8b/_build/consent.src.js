/* Bartier & Co : gestion du consentement aux cookies (recommandation CNIL).
   - rien n'est chargé avant le choix ; refuser est aussi simple qu'accepter ;
   - le choix est gardé 6 mois dans localStorage ("bc-consent") ; modifiable par [data-cookies] ou un lien #cookies ;
   - les balises (GA4, Google Ads, Pixel Meta) ne partent que si leur identifiant est configuré ET que la finalité est acceptée.
   Fichier généré par _build/site.py à partir de _build/consent.src.js. */
(function () {
  var T = __TEXTS__, TAGS = __TAGS__, KEY = "bc-consent", MAX = 183 * 864e5, d = document, root = d.documentElement;
  var state = null, ui = null, panel = null, lastFocus = null, loaded = {};
  function read() {
    try { var c = JSON.parse(localStorage.getItem(KEY) || "null"); if (c && c.v === 1 && Date.now() - c.t < MAX) return c; } catch (e) {}
    return null;
  }
  function write(a, p) {
    state = { v: 1, t: Date.now(), a: a ? 1 : 0, p: p ? 1 : 0 };
    try { localStorage.setItem(KEY, JSON.stringify(state)); } catch (e) {}
    apply(); close();
    try { d.dispatchEvent(new CustomEvent("bc:consent", { detail: state })); } catch (e) {}
  }
  function script(src) { var s = d.createElement("script"); s.async = true; s.src = src; d.head.appendChild(s); }
  function gtagBase() {
    if (loaded.gtag) return; loaded.gtag = 1;
    window.dataLayer = window.dataLayer || [];
    window.gtag = window.gtag || function () { window.dataLayer.push(arguments); };
    gtag("consent", "default", { ad_storage: "denied", ad_user_data: "denied", ad_personalization: "denied", analytics_storage: "denied" });
    gtag("js", new Date());
    script("https://www.googletagmanager.com/gtag/js?id=" + encodeURIComponent(TAGS.ga4 || TAGS.gads));
  }
  function dropCookies(names) {
    var host = location.hostname, parts = host.split("."), domains = [host];
    if (parts.length > 2) domains.push("." + parts.slice(-2).join("."));
    d.cookie.split(";").forEach(function (c) {
      var n = c.split("=")[0].trim();
      if (!names.some(function (p) { return n.indexOf(p) === 0; })) return;
      domains.concat([""]).forEach(function (dm) { d.cookie = n + "=; Max-Age=0; path=/" + (dm ? "; domain=" + dm : ""); });
    });
  }
  function apply() {
    if (!state) return;
    var a = !!state.a, p = !!state.p;
    if ((TAGS.ga4 && a) || (TAGS.gads && p)) {
      gtagBase();
      gtag("consent", "update", { analytics_storage: a ? "granted" : "denied", ad_storage: p ? "granted" : "denied", ad_user_data: p ? "granted" : "denied", ad_personalization: p ? "granted" : "denied" });
      if (TAGS.ga4 && a && !loaded.ga4) { loaded.ga4 = 1; gtag("config", TAGS.ga4, { cookie_expires: 34128000, cookie_flags: "SameSite=Lax;Secure" }); }
      if (TAGS.gads && p && !loaded.gads) { loaded.gads = 1; gtag("config", TAGS.gads); }
    } else if (loaded.gtag) {
      gtag("consent", "update", { analytics_storage: "denied", ad_storage: "denied", ad_user_data: "denied", ad_personalization: "denied" });
    }
    if (TAGS.meta && p && !loaded.meta) {
      loaded.meta = 1;
      (function (f, b, e, v, n, t, s) { if (f.fbq) return; n = f.fbq = function () { n.callMethod ? n.callMethod.apply(n, arguments) : n.queue.push(arguments); }; if (!f._fbq) f._fbq = n; n.push = n; n.loaded = true; n.version = "2.0"; n.queue = []; t = b.createElement(e); t.async = true; t.src = v; s = b.getElementsByTagName(e)[0]; s.parentNode.insertBefore(t, s); })(window, d, "script", "https://connect.facebook.net/en_US/fbevents.js");
      fbq("consent", "grant"); fbq("init", TAGS.meta); fbq("track", "PageView");
    } else if (loaded.meta && !p) { try { fbq("consent", "revoke"); } catch (e) {} }
    if (!a) dropCookies(["_ga"]);
    if (!p) dropCookies(["_gcl", "_fbp", "_fbc"]);
  }
  var CSS = ".cc,.cc-panel{font:400 .92rem/1.45 var(--f-text,system-ui,sans-serif);color:var(--ink,#0A1424)}" +
    ".cc{position:fixed;z-index:120;left:max(16px,env(safe-area-inset-left));bottom:max(16px,env(safe-area-inset-bottom));width:min(430px,calc(100vw - 32px));padding:20px 20px 16px;background:var(--bg,#fff);border:1px solid color-mix(in oklab,var(--ink,#0A1424) 16%,transparent);border-radius:2px;box-shadow:0 18px 50px -18px rgba(10,20,36,.45)}" +
    ".cc h2,.cc-panel h2{margin:0 0 .4rem;font:400 1.15rem/1.2 var(--f-display,system-ui,sans-serif);letter-spacing:-.02em}" +
    ".cc p,.cc-panel p{margin:0}.cc a,.cc-panel a{color:inherit;text-underline-offset:.2em}" +
    ".cc-row{display:grid;grid-template-columns:1fr 1fr;gap:8px;margin-top:14px}" +
    ".cc-b{min-height:46px;padding:0 14px;border:1px solid var(--ink,#0A1424);border-radius:2px;background:var(--ink,#0A1424);color:var(--bg,#fff);font:500 .92rem/1 var(--f-text,system-ui,sans-serif);cursor:pointer}" +
    ".cc-b:hover,.cc-b:focus-visible{background:var(--accent,#2D5BE3);border-color:var(--accent,#2D5BE3)}" +
    ".cc-l{display:block;width:100%;min-height:40px;margin-top:6px;padding:0;border:0;background:none;color:inherit;font:inherit;text-decoration:underline;text-underline-offset:.25em;cursor:pointer}" +
    ".cc-b:focus-visible,.cc-l:focus-visible,.cc-sw:focus-visible{outline:2px solid var(--accent,#2D5BE3);outline-offset:2px}" +
    ".cc-veil{position:fixed;inset:0;z-index:130;display:grid;place-items:center;padding:16px;background:rgba(10,20,36,.55);overflow:auto}" +
    ".cc-panel{width:min(520px,100%);max-height:calc(100dvh - 32px);overflow:auto;padding:24px;background:var(--bg,#fff);border-radius:2px}" +
    ".cc-item{display:grid;grid-template-columns:1fr auto;gap:4px 16px;align-items:center;padding:14px 0;border-top:1px solid color-mix(in oklab,var(--ink,#0A1424) 12%,transparent)}" +
    ".cc-item:first-of-type{margin-top:14px}.cc-item b{font-weight:500}.cc-item p{grid-column:1;color:color-mix(in oklab,var(--ink,#0A1424) 70%,transparent);font-size:.86rem}" +
    ".cc-on{grid-row:1 / span 2;grid-column:2;font-size:.8rem;color:color-mix(in oklab,var(--ink,#0A1424) 60%,transparent)}" +
    ".cc-sw{grid-row:1 / span 2;grid-column:2;position:relative;width:48px;height:28px;padding:0;border:0;border-radius:14px;background:color-mix(in oklab,var(--ink,#0A1424) 28%,transparent);cursor:pointer;transition:background .2s}" +
    ".cc-sw::after{content:'';position:absolute;top:3px;left:3px;width:22px;height:22px;border-radius:50%;background:#fff;transition:transform .2s}" +
    ".cc-sw[aria-checked=true]{background:var(--accent,#2D5BE3)}.cc-sw[aria-checked=true]::after{transform:translateX(20px)}" +
    ".cc-panel .cc-row{margin-top:18px}.cc-save{grid-column:1 / -1}" +
    "html.cc-open .wa,html.cc-open .pf-sticky{display:none!important}" +
    "@media (max-width:760px){.cc{left:0;right:0;bottom:0;width:auto;padding:16px 16px calc(12px + env(safe-area-inset-bottom));border-width:1px 0 0;box-shadow:0 -12px 40px -16px rgba(10,20,36,.4)}.cc h2{font-size:1.05rem}.cc p{font-size:.88rem}.cc-panel{padding:20px 18px}}" +
    "@media (prefers-reduced-motion:no-preference){.cc{animation:cc-in .45s cubic-bezier(.2,.7,.2,1) both}@keyframes cc-in{from{transform:translateY(16px);opacity:0}}}";
  function style() { if (d.getElementById("cc-css")) return; var s = d.createElement("style"); s.id = "cc-css"; s.textContent = CSS; d.head.appendChild(s); }
  function el(tag, cls, html) { var e = d.createElement(tag); if (cls) e.className = cls; if (html != null) e.innerHTML = html; return e; }
  function btn(cls, label, fn) { var b = el("button", cls); b.type = "button"; b.textContent = label; b.addEventListener("click", fn); return b; }
  function banner() {
    if (ui) return; style();
    ui = el("section", "cc"); ui.setAttribute("role", "region"); ui.setAttribute("aria-label", T.banner_title);
    ui.appendChild(el("h2", "", T.banner_title));
    ui.appendChild(el("p", "", T.banner_text));
    var row = el("div", "cc-row");
    row.appendChild(btn("cc-b", T.banner_refuse, function () { write(0, 0); }));
    row.appendChild(btn("cc-b", T.banner_accept, function () { write(1, 1); }));
    ui.appendChild(row);
    ui.appendChild(btn("cc-l", T.banner_customize, prefs));
    d.body.appendChild(ui); root.classList.add("cc-open");
  }
  function sw(on) { var b = el("button", "cc-sw"); b.type = "button"; b.setAttribute("role", "switch"); b.setAttribute("aria-checked", on ? "true" : "false"); b.addEventListener("click", function () { b.setAttribute("aria-checked", b.getAttribute("aria-checked") === "true" ? "false" : "true"); }); return b; }
  function item(title, text, control, id) { var it = el("div", "cc-item"); var b = el("b", "", title); b.id = id; it.appendChild(b); if (control.setAttribute) control.setAttribute("aria-labelledby", id); it.appendChild(control); it.appendChild(el("p", "", text)); return it; }
  function prefs() {
    if (panel) return; style(); lastFocus = d.activeElement;
    var veil = el("div", "cc-veil"), box = el("div", "cc-panel"), cur = state || { a: 0, p: 0 };
    box.setAttribute("role", "dialog"); box.setAttribute("aria-modal", "true"); box.setAttribute("aria-labelledby", "cc-t"); box.tabIndex = -1;
    var h = el("h2", "", T.prefs_title); h.id = "cc-t"; box.appendChild(h); box.appendChild(el("p", "", T.prefs_intro));
    var sa = sw(cur.a), sp = sw(cur.p), on = el("span", "cc-on", T.prefs_always);
    box.appendChild(item(T.prefs_necessary_title, T.prefs_necessary_text, on, "cc-n"));
    box.appendChild(item(T.prefs_audience_title, T.prefs_audience_text, sa, "cc-a"));
    box.appendChild(item(T.prefs_ads_title, T.prefs_ads_text, sp, "cc-p"));
    var row = el("div", "cc-row");
    row.appendChild(btn("cc-b", T.banner_refuse, function () { write(0, 0); }));
    row.appendChild(btn("cc-b", T.banner_accept, function () { write(1, 1); }));
    row.appendChild(btn("cc-b cc-save", T.prefs_save, function () { write(sa.getAttribute("aria-checked") === "true", sp.getAttribute("aria-checked") === "true"); }));
    box.appendChild(row); veil.appendChild(box); d.body.appendChild(veil); panel = veil; root.classList.add("cc-open");
    veil.addEventListener("mousedown", function (e) { if (e.target === veil) closePanel(); });
    veil.addEventListener("keydown", function (e) {
      if (e.key === "Escape") { closePanel(); return; }
      if (e.key !== "Tab") return;
      var f = box.querySelectorAll("button,a[href]"), first = f[0], last = f[f.length - 1];
      if (e.shiftKey && (d.activeElement === first || d.activeElement === box)) { e.preventDefault(); last.focus(); }
      else if (!e.shiftKey && d.activeElement === last) { e.preventDefault(); first.focus(); }
    });
    box.focus();
  }
  function closePanel() { if (!panel) return; panel.remove(); panel = null; if (!ui) root.classList.remove("cc-open"); if (lastFocus && lastFocus.focus) lastFocus.focus(); }
  function close() { if (ui) { ui.remove(); ui = null; } if (panel) { panel.remove(); panel = null; if (lastFocus && lastFocus.focus) lastFocus.focus(); } root.classList.remove("cc-open"); }
  d.addEventListener("click", function (e) {
    var t = e.target.closest && e.target.closest('[data-cookies],a[href="#cookies"],a[href$="/#cookies"]');
    if (!t) return; e.preventDefault(); prefs();
  });
  window.bcConsent = { get: function () { return state; }, open: prefs, reset: function () { try { localStorage.removeItem(KEY); } catch (e) {} state = null; banner(); } };
  state = read();
  if (state) apply(); else if (d.body) banner(); else d.addEventListener("DOMContentLoaded", banner);
})();

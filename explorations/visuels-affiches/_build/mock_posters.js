// Affiches Bartier & Co à poser dans les maquettes (style du site : grille fine, très grands chiffres, peu de texte).
const { chromium } = require('playwright');
const fs = require('fs');
const V8B = '/home/user/bartier/explorations/v8b';
const OUT = process.argv[2];
fs.mkdirSync(OUT, { recursive: true });
const font = f => 'data:font/woff2;base64,' + fs.readFileSync(`${V8B}/assets/fonts/${f}`).toString('base64');
const logoSvg = fs.readFileSync(`${V8B}/assets/logo-bartier.svg`, 'utf8');
const logo = (w, color) => logoSvg.replace('<svg ', `<svg style="display:block;width:${w}px;height:auto;color:${color}" `);
const CSS = `
@font-face{font-family:HG;src:url(${font('host-grotesk-latin.woff2')}) format('woff2');font-weight:300 800}
@font-face{font-family:HG;src:url(${font('host-grotesk-latin-ext.woff2')}) format('woff2');font-weight:300 800;unicode-range:U+0100-024F}
@font-face{font-family:SG;src:url(${font('schibsted-grotesk-latin.woff2')}) format('woff2');font-weight:400 900}
@font-face{font-family:SG;src:url(${font('schibsted-grotesk-latin-ext.woff2')}) format('woff2');font-weight:400 900;unicode-range:U+0100-024F}
*{box-sizing:border-box;margin:0;padding:0}
:root{--ink:#0A1424;--accent:#2D5BE3;--paper:#EEF0F3}
body{font-family:SG,sans-serif;-webkit-font-smoothing:antialiased}
.p{position:relative;overflow:hidden;display:flex;flex-direction:column}
.grid::before{content:"";position:absolute;inset:0;pointer-events:none;
  background-image:linear-gradient(to right,var(--g) 1px,transparent 1px),linear-gradient(to bottom,var(--g) 1px,transparent 1px);
  background-size:100px 100px;background-position:-1px -1px}
.d{font-family:HG,sans-serif;font-weight:300;letter-spacing:-.045em;line-height:.92}
.foot{margin-top:auto;display:flex;justify-content:space-between;align-items:flex-end;position:relative}
.url{font-size:30px;letter-spacing:-.01em}
.rule{height:3px;background:currentColor;position:relative}
`;
// Affiche verticale 600 x 1000 (rendu x2)
const V = (bg, fg, g, inner) => [600, 1000, `<div class="p grid" style="width:600px;height:1000px;background:${bg};color:${fg};--g:${g};padding:56px 52px 48px">${inner}</div>`];
const foot = (fg) => `<div class="foot"><div>${logo(230, fg)}</div><p class="url" style="font-size:24px;opacity:.8;padding-bottom:6px">bartierandco.com</p></div>`;
const num = (n, u, line, numColor, fg) => `
  <div style="position:relative">${logo(230, fg)}</div>
  <div class="rule" style="color:${fg};opacity:.9;margin-top:auto"></div>
  <p class="d" style="position:relative;margin-top:44px;font-size:360px;color:${numColor};white-space:nowrap">${n}<span style="font-size:96px;letter-spacing:-.03em;margin-left:14px;color:${fg}">${u}</span></p>
  <p class="d" style="position:relative;margin-top:36px;font-size:58px;letter-spacing:-.03em;line-height:1.02;min-height:2.04em">${line}</p>
  <p class="url" style="position:relative;margin-top:48px;font-size:24px;opacity:.8">bartierandco.com</p>`;
const posters = {
  // Rue : affiche pour les propriétaires
  'rue-particuliers': V('var(--accent)', '#fff', 'rgba(255,255,255,.09)', `
    <p style="position:relative;font-size:30px;opacity:.85">Vous êtes propriétaire&nbsp;?</p>
    <p class="d" style="position:relative;margin-top:34px;font-size:112px;line-height:.95">Pas cinq artisans.<br>Un seul, près de chez vous.</p>
    <p style="position:relative;margin-top:40px;font-size:30px;line-height:1.35;opacity:.92">Toiture, façade, fenêtres, charpente, isolation. Visite et devis offerts.</p>
    <p class="url" style="position:relative;margin-top:auto;font-size:26px;opacity:.9">bartierandco.com/devis-travaux</p>
    <div style="position:relative;margin-top:22px">${logo(230, '#fff')}</div>`),
  // Mur noir : les trois engagements en chiffres
  'mur-1-artisan': V('var(--ink)', '#fff', 'rgba(255,255,255,.07)', `${num('1', 'artisan', 'par secteur&nbsp;:<br>vous.', '#7da0ff', '#fff')}`),
  'mur-2-5-min': V('var(--accent)', '#fff', 'rgba(255,255,255,.10)', `${num('5', 'min', 'pour rappeler<br>chaque demande.', '#fff', '#fff')}`),
  'mur-3-0-mois': V('#fff', 'var(--ink)', 'rgba(10,20,36,.06)', `${num('0', 'mois', 'd’engagement.', 'var(--accent)', 'var(--ink)')}`),
  // Grand panneau : la promesse aux artisans
  'panneau-couverture': [1000, 520, `<div class="p grid" style="width:1000px;height:520px;background:var(--ink);color:#fff;--g:rgba(255,255,255,.07);padding:52px 60px 44px">
     <div style="position:relative">${logo(330, '#fff')}</div>
     <p class="d" style="position:relative;margin-top:52px;font-size:104px;line-height:.95">Plus de chantiers.<br><span style="color:#7da0ff">Moins de téléphone.</span></p>
     <div class="foot"><p style="font-size:24px;opacity:.8">Faire équipe. Faire la différence.</p><p class="url" style="font-size:24px;opacity:.8">bartierandco.com</p></div></div>`],
};
(async () => {
  const b = await chromium.launch();
  for (const [name, [w, h, body]] of Object.entries(posters)) {
    const p = await b.newPage({ viewport: { width: w, height: h }, deviceScaleFactor: 2 });
    await p.setContent(`<!doctype html><html lang="fr"><head><meta charset="utf-8"><style>${CSS}</style></head><body>${body}</body></html>`);
    await p.evaluate(() => document.fonts.ready);
    await p.waitForTimeout(150);
    await p.screenshot({ path: `${OUT}/${name}.png`, clip: { x: 0, y: 0, width: w, height: h } });
    await p.close();
  }
  await b.close();
  console.log('ok');
})();

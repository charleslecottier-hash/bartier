// Couverture de la fiche Google : plan d'élévation d'une maison au trait, ses cinq métiers annotés, promesse aux artisans.
// Rendu 1080 x 608 en CSS, x2 => 2160 x 1216. Contenu important dans le centre pour survivre aux recadrages de Google.
const { chromium } = require('playwright');
const fs = require('fs');
const V8B = '/home/user/bartier/explorations/v8b';
const OUT = process.argv[2];
const font = f => 'data:font/woff2;base64,' + fs.readFileSync(`${V8B}/assets/fonts/${f}`).toString('base64');
const logo = fs.readFileSync(`${V8B}/assets/logo-bartier.svg`, 'utf8').replace('<svg ', '<svg style="display:block;width:220px;height:auto;color:#fff" ');

// --- maison (pignon), coordonnées de la page ---
const L = 'stroke="rgba(255,255,255,.82)" stroke-width="1.4" fill="none" stroke-linecap="round" stroke-linejoin="round"';
const A = 'stroke="#8fb0ff" stroke-width="1.6" fill="none" stroke-linecap="round" stroke-linejoin="round"';
const H = 'stroke="#8fb0ff" stroke-width="1.1" fill="none" stroke-dasharray="4 4" stroke-linecap="round"';
const slopeL = x => 175 + (680 - x) * (125 / 120);
const zig = (() => { let p = []; for (let x = 598, i = 0; x <= 762; x += 6, i++) p.push(`${x},${i % 2 ? 282 : 291}`); return p.join(' '); })();
const tiles = (() => { // rangs de tuiles le long des rampants (traits courts perpendiculaires)
  let s = '';
  for (let t = 0.08; t < 0.98; t += 0.075) {
    for (const side of [-1, 1]) {
      const x0 = 680 + side * 120 * t, y0 = 175 + 125 * t;
      const nx = side * 125 / 173, ny = -120 / 173;
      s += `<line x1="${x0.toFixed(1)}" y1="${y0.toFixed(1)}" x2="${(x0 + nx * 7).toFixed(1)}" y2="${(y0 + ny * 7).toFixed(1)}" ${A} stroke-width="1.1"/>`;
    }
  }
  return s;
})();
const ground = (() => { let s = ''; for (let x = 524; x <= 836; x += 9) s += `<line x1="${x}" y1="471" x2="${x - 7}" y2="479" stroke="rgba(255,255,255,.28)" stroke-width="1"/>`; return s; })();
const house = `
  <!-- sol -->
  <line x1="516" y1="470" x2="844" y2="470" ${L}/>${ground}
  <!-- mur pignon et soubassement -->
  <rect x="580" y="300" width="200" height="170" ${L}/>
  <line x1="580" y1="452" x2="780" y2="452" stroke="rgba(255,255,255,.4)" stroke-width="1"/>
  <!-- toiture : rampants, épaisseur de couverture, rangs de tuiles -->
  <polyline points="556,302 680,173 804,302" ${A} stroke-width="2"/>
  <polyline points="570,300 680,187 790,300" ${A}/>
  ${tiles}
  <!-- cheminée sur le rampant gauche -->
  <polyline points="610,${slopeL(610).toFixed(1)} 610,196 632,196 632,${slopeL(632).toFixed(1)}" ${L}/>
  <line x1="606" y1="196" x2="636" y2="196" ${L}/>
  <!-- charpente (traits cachés) : entrait, poinçon, contrefiches -->
  <line x1="592" y1="296" x2="768" y2="296" ${H}/>
  <line x1="680" y1="193" x2="680" y2="296" ${H}/>
  <line x1="680" y1="296" x2="625" y2="244" ${H}/>
  <line x1="680" y1="296" x2="735" y2="244" ${H}/>
  <!-- isolation des combles -->
  <polyline points="${zig}" stroke="rgba(143,176,255,.75)" stroke-width="1.1" fill="none" stroke-linejoin="round"/>
  <!-- fenêtres à deux vantaux et porte -->
  <rect x="600" y="340" width="42" height="60" ${L}/><line x1="621" y1="340" x2="621" y2="400" ${L}/><line x1="600" y1="360" x2="642" y2="360" stroke="rgba(255,255,255,.5)" stroke-width="1"/><line x1="596" y1="404" x2="646" y2="404" ${L}/>
  <rect x="718" y="340" width="42" height="60" ${L}/><line x1="739" y1="340" x2="739" y2="400" ${L}/><line x1="718" y1="360" x2="760" y2="360" stroke="rgba(255,255,255,.5)" stroke-width="1"/><line x1="714" y1="404" x2="764" y2="404" ${L}/>
  <rect x="662" y="372" width="36" height="98" ${L}/><circle cx="691" cy="424" r="1.8" fill="rgba(255,255,255,.82)"/>
  <!-- cote -->
  <line x1="580" y1="474" x2="580" y2="504" stroke="rgba(255,255,255,.3)" stroke-width="1"/>
  <line x1="780" y1="474" x2="780" y2="504" stroke="rgba(255,255,255,.3)" stroke-width="1"/>
  <line x1="580" y1="498" x2="780" y2="498" stroke="rgba(255,255,255,.45)" stroke-width="1"/>
  <line x1="575" y1="503" x2="585" y2="493" stroke="rgba(255,255,255,.6)" stroke-width="1.2"/>
  <line x1="775" y1="503" x2="785" y2="493" stroke="rgba(255,255,255,.6)" stroke-width="1.2"/>`;
// annotations : cible -> coude -> étiquette
const notes = [['Charpente', 680, 215, 215], ['Toiture', 765, 263.5, 263], ['Isolation', 752, 286, 311], ['Fenêtres', 760, 372, 370], ['Façade', 780, 430, 428]];
const ann = notes.map(([t, x, y, ly]) => `
  <circle cx="${x}" cy="${y}" r="2.6" fill="#8fb0ff"/>
  <polyline points="${x},${y} ${ly === y ? 836 : 818},${ly} 840,${ly}" stroke="rgba(143,176,255,.7)" stroke-width="1" fill="none"/>
  <text x="850" y="${ly + 5}" font-family="SG" font-size="15.5" fill="rgba(255,255,255,.86)">${t}</text>`).join('');

const html = `<!doctype html><html lang="fr"><head><meta charset="utf-8"><style>
@font-face{font-family:HG;src:url(${font('host-grotesk-latin.woff2')}) format('woff2');font-weight:300 800}
@font-face{font-family:HG;src:url(${font('host-grotesk-latin-ext.woff2')}) format('woff2');font-weight:300 800;unicode-range:U+0100-024F}
@font-face{font-family:SG;src:url(${font('schibsted-grotesk-latin.woff2')}) format('woff2');font-weight:400 900}
@font-face{font-family:SG;src:url(${font('schibsted-grotesk-latin-ext.woff2')}) format('woff2');font-weight:400 900;unicode-range:U+0100-024F}
*{box-sizing:border-box;margin:0;padding:0}
body{width:1080px;height:608px;overflow:hidden;-webkit-font-smoothing:antialiased}
.c{position:relative;width:1080px;height:608px;color:#fff;
  background:
    radial-gradient(ellipse 70% 80% at 62% 52%, rgba(45,91,227,.12), rgba(10,20,36,0) 70%),
    linear-gradient(to right, rgba(255,255,255,.075) 1px, transparent 1px) -1px -1px / 120px 120px,
    linear-gradient(to bottom, rgba(255,255,255,.075) 1px, transparent 1px) -1px -1px / 120px 120px,
    linear-gradient(to right, rgba(255,255,255,.03) 1px, transparent 1px) -1px -1px / 24px 24px,
    linear-gradient(to bottom, rgba(255,255,255,.03) 1px, transparent 1px) -1px -1px / 24px 24px,
    #0A1424}
.txt{position:absolute;left:150px;top:0;bottom:0;width:380px;display:flex;flex-direction:column;justify-content:center}
.k{font-family:SG;font-size:16px;color:#a9bcff;margin-top:44px}
.h{font-family:HG;font-weight:300;font-size:58px;line-height:.98;letter-spacing:-.04em;margin-top:14px}
.h span{color:#8fb0ff}
.u{font-family:SG;font-size:15px;color:rgba(255,255,255,.62);margin-top:30px}
svg.art{position:absolute;inset:0}
</style></head><body><div class="c">
  <div class="txt">${logo}<p class="k">Artisans du bâtiment</p><p class="h">Plus de chantiers.<br><span>Moins de téléphone.</span></p><p class="u">bartierandco.com</p></div>
  <svg class="art" width="1080" height="608" viewBox="0 0 1080 608">${house}${ann}</svg>
</div></body></html>`;
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1080, height: 608 }, deviceScaleFactor: 2 });
  await p.setContent(html);
  await p.evaluate(() => document.fonts.ready);
  await p.waitForTimeout(200);
  await p.screenshot({ path: OUT });
  await b.close();
  console.log('ok');
})();

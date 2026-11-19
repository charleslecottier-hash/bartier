// Couverture de la fiche Google, version artisans : leurs métiers, la promesse, trois chiffres. Lisible même en vignette.
// Rendu 1080 x 608 en CSS, x2 => 2160 x 1216. Tout le contenu tient entre x 150 et 930 (recadrage 4:3 de Google).
const { chromium } = require('playwright');
const fs = require('fs');
const V8B = '/home/user/bartier/explorations/v8b';
const OUT = process.argv[2];
const font = f => 'data:font/woff2;base64,' + fs.readFileSync(`${V8B}/assets/fonts/${f}`).toString('base64');
const logo = fs.readFileSync(`${V8B}/assets/logo-bartier.svg`, 'utf8').replace('<svg ', '<svg style="display:block;width:190px;height:auto;color:#fff" ');
const facts = [['1', 'artisan', 'par métier et par secteur'], ['5', 'min', 'pour rappeler chaque demande'], ['0', 'mois', 'd’engagement']];
const html = `<!doctype html><html lang="fr"><head><meta charset="utf-8"><style>
@font-face{font-family:HG;src:url(${font('host-grotesk-latin.woff2')}) format('woff2');font-weight:300 800}
@font-face{font-family:HG;src:url(${font('host-grotesk-latin-ext.woff2')}) format('woff2');font-weight:300 800;unicode-range:U+0100-024F}
@font-face{font-family:SG;src:url(${font('schibsted-grotesk-latin.woff2')}) format('woff2');font-weight:400 900}
@font-face{font-family:SG;src:url(${font('schibsted-grotesk-latin-ext.woff2')}) format('woff2');font-weight:400 900;unicode-range:U+0100-024F}
*{box-sizing:border-box;margin:0;padding:0}
body{width:1080px;height:608px;overflow:hidden;-webkit-font-smoothing:antialiased}
.c{position:relative;width:1080px;height:608px;color:#fff;padding:0 150px;display:flex;flex-direction:column;justify-content:center;
  background:
    linear-gradient(to right, rgba(255,255,255,.07) 1px, transparent 1px) -1px -1px / 120px 120px,
    linear-gradient(to bottom, rgba(255,255,255,.07) 1px, transparent 1px) -1px -1px / 120px 120px,
    #0A1424}
.top{display:flex;align-items:flex-end;justify-content:space-between}
.k{font-family:SG;font-size:16.5px;color:#a9bcff;padding-bottom:4px}
.h{font-family:HG;font-weight:300;font-size:84px;line-height:.98;letter-spacing:-.045em;margin-top:42px}
.h span{color:#8fb0ff}
.f{display:grid;grid-template-columns:repeat(3,1fr);gap:20px;margin-top:46px}
.f div{border-top:1.5px solid rgba(255,255,255,.85);padding-top:16px}
.n{font-family:HG;font-weight:300;font-size:60px;line-height:1;letter-spacing:-.04em}
.n small{font-size:23px;letter-spacing:-.01em;margin-left:6px;color:rgba(255,255,255,.85)}
.l{font-family:SG;font-size:16px;white-space:nowrap;color:rgba(255,255,255,.76);margin-top:8px}
</style></head><body><div class="c">
  <div class="top">${logo}<p class="k">Couverture · Façade · Menuiserie · Charpente · Isolation</p></div>
  <p class="h">Plus de chantiers.<br><span>Moins de téléphone.</span></p>
  <div class="f">${facts.map(([n, u, l]) => `<div><p class="n">${n}<small>${u}</small></p><p class="l">${l}</p></div>`).join('')}</div>
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

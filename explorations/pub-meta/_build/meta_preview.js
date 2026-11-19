// Aperçu de la pub telle qu'elle apparaît dans un fil d'actu sur téléphone (maquette neutre, sans logos de Meta ni fausses réactions).
const { chromium } = require('playwright');
const fs = require('fs');
const V8B = '/home/user/bartier/explorations/v8b';
const [img, out] = process.argv.slice(2);
const b64 = f => fs.readFileSync(f).toString('base64');
const font = f => `data:font/woff2;base64,${b64(`${V8B}/assets/fonts/${f}`)}`;
const logo = fs.readFileSync(`${V8B}/assets/logo-bartier.svg`, 'utf8').replace('<svg ', '<svg style="display:block;width:36px;height:auto;color:#0A1424" ');
const html = `<!doctype html><html lang="fr"><head><meta charset="utf-8"><style>
@font-face{font-family:SG;src:url(${font('schibsted-grotesk-latin.woff2')}) format('woff2');font-weight:400 900}
@font-face{font-family:SG;src:url(${font('schibsted-grotesk-latin-ext.woff2')}) format('woff2');font-weight:400 900;unicode-range:U+0100-024F}
*{box-sizing:border-box;margin:0;padding:0}
body{background:#e9ebee;font-family:SG,sans-serif;color:#1c1e21;-webkit-font-smoothing:antialiased;width:390px;padding-bottom:12px}
.post{background:#fff;margin:12px 0}
.hd{display:flex;align-items:center;gap:10px;padding:12px 14px 8px}
.av{width:42px;height:42px;border-radius:50%;background:#fff;border:1px solid #dadde1;display:grid;place-items:center;overflow:hidden}
.nm{font-weight:600;font-size:15px}
.sp{font-size:12.5px;color:#65676b;margin-top:1px}
.txt{padding:2px 14px 10px;font-size:15px;line-height:1.38}
.txt b{font-weight:600;color:#65676b}
img{display:block;width:390px;height:487.5px;object-fit:cover}
.bar{display:flex;align-items:center;justify-content:space-between;gap:12px;background:#f0f2f5;padding:10px 14px 12px}
.dom{font-size:12px;color:#65676b;text-transform:uppercase;letter-spacing:.02em}
.hl{font-size:15.5px;font-weight:600;margin-top:2px;line-height:1.25}
.ds{font-size:13px;color:#65676b;margin-top:2px}
.cta{flex:none;background:#e4e6eb;border-radius:6px;font-size:14.5px;font-weight:600;padding:9px 12px}
</style></head><body>
<div class="post">
  <div class="hd"><div class="av">${logo}</div><div><p class="nm">Bartier &amp; Co</p><p class="sp">Sponsorisé</p></div></div>
  <p class="txt">Artisans du bâtiment&nbsp;: nous trouvons vos clients, vous faites les chantiers.<br><br>Nous lançons vos annonces à votre nom sur Facebook, Instagram et Google. Chaque demande est rappelée… <b>Voir plus</b></p>
  <img src="data:image/jpeg;base64,${b64(img)}" alt="">
  <div class="bar"><div><p class="dom">bartierandco.com</p><p class="hl">Des visites de devis dans votre agenda</p><p class="ds">Sans engagement</p></div><p class="cta">En savoir plus</p></div>
</div></body></html>`;
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 390, height: 800 }, deviceScaleFactor: 2 });
  await p.setContent(html);
  await p.evaluate(() => document.fonts.ready);
  await p.waitForTimeout(200);
  const h = await p.evaluate(() => document.body.scrollHeight);
  await p.screenshot({ path: out, clip: { x: 0, y: 0, width: 390, height: h } });
  await b.close();
  console.log('ok', h);
})();

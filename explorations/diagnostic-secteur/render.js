// Rend un fichier HTML en PDF A4 : node render.js entree.html sortie.pdf
const path = require('path');
const { chromium } = require('playwright');
(async () => {
  const [src, out] = process.argv.slice(2).map((p) => path.resolve(p));
  const b = await chromium.launch();
  const p = await b.newPage();
  await p.goto('file://' + src, { waitUntil: 'networkidle' });
  await p.evaluate(() => document.fonts.ready);
  await p.pdf({ path: out, format: 'A4', printBackground: true, preferCSSPageSize: true });
  if (process.env.APERCU) await p.screenshot({ path: process.env.APERCU, fullPage: true });
  await b.close();
})();

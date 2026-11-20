// Images d'aperçu (Open Graph) : une par page, 1200 × 630, rendues avec les polices du site.
// Entrée : _build/og_jobs.json [{file, kicker, title, map}] ; sortie : assets/og/<file>.png
const { chromium } = require('playwright');
const fs = require('fs'), path = require('path');
(async () => {
  const root = path.resolve(__dirname, '..');
  const jobs = JSON.parse(fs.readFileSync(path.join(__dirname, 'og_jobs.json'), 'utf8'));
  const logo = fs.readFileSync(path.join(root, 'assets/logo-bartier-wordmark.svg'), 'utf8');
  const font = f => 'data:font/woff2;base64,' + fs.readFileSync(path.join(root, 'assets/fonts', f)).toString('base64');  // intégrées : une page about:blank ne charge pas file://
  const css = `@font-face{font-family:HG;font-weight:300 600;src:url(${font('host-grotesk-latin.woff2')}) format('woff2');unicode-range:U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+0304,U+0308,U+0329,U+2000-206F,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD}
@font-face{font-family:HG;font-weight:300 600;src:url(${font('host-grotesk-latin-ext.woff2')}) format('woff2');unicode-range:U+0100-02BA,U+02BD-02C5,U+02C7-02CC,U+02CE-02D7,U+02DD-02FF,U+0304,U+0308,U+0329,U+1D00-1DBF,U+1E00-1E9F,U+1EF2-1EFF,U+2020,U+20A0-20AB,U+20AD-20C0,U+2113,U+2C60-2C7F,U+A720-A7FF}
html,body{margin:0}body{width:1200px;height:630px;position:relative;overflow:hidden;background:#0A1424;color:#fff;font-family:HG,sans-serif}
.k{position:absolute;left:80px;top:76px;font-size:26px;letter-spacing:.01em;color:#8fb0ff}
.t{position:absolute;left:80px;top:128px;font-size:64px;line-height:1.08;letter-spacing:-.02em;font-weight:300}
.f{position:absolute;left:80px;right:80px;bottom:64px;display:flex;align-items:center;justify-content:space-between;padding-top:28px;border-top:1px solid rgba(255,255,255,.16)}
.f svg{height:40px;width:auto;color:#fff}.u{font-size:22px;color:rgba(255,255,255,.6)}
.map{position:absolute;right:64px;top:64px;width:380px}
.vl-fr{fill:rgba(255,255,255,.05);stroke:#fff;stroke-opacity:.32;stroke-width:1.2}.vl-dot{fill:rgba(255,255,255,.55)}.vl-lab{font:17px HG;fill:rgba(255,255,255,.6)}
.vl-dot.is-on{fill:#8fb0ff}.vl-halo{fill:#8fb0ff;opacity:.25}.vl-lab.is-on{fill:#fff;font-weight:500}`;
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1200, height: 630 }, deviceScaleFactor: 1 });
  for (const j of jobs) {
    const w = j.map ? 600 : 1000;
    const html = `<!doctype html><html lang="fr"><head><meta charset="utf-8"><style>${css}</style></head><body>
<p class="k">${j.kicker}</p><p class="t" style="width:${w}px">${j.title}</p>${j.map ? `<div class="map">${j.map}</div>` : ''}
<div class="f">${logo}<span class="u">bartierandco.com</span></div></body></html>`;
    await p.setContent(html, { waitUntil: 'load' });
    await p.evaluate(() => document.fonts.ready);
    // le titre ne doit jamais toucher le pied : on réduit la taille si besoin
    await p.evaluate(() => { const t = document.querySelector('.t'), f = document.querySelector('.f'); let s = 64;
      while (t.getBoundingClientRect().bottom > f.getBoundingClientRect().top - 32 && s > 40) { s -= 2; t.style.fontSize = s + 'px'; } });
    await p.screenshot({ path: path.join(root, 'assets/og', j.file + '.png') });
  }
  await b.close();
  console.log(jobs.length + ' images');
})();

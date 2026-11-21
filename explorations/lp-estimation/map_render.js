// Carte de la zone d'intervention : rendu du plan IGN (style gris, données ouvertes) dans Chromium, à la génération.
// La page publiée n'appelle aucun service de cartes : elle affiche l'image produite ici.
//   node map_render.js <jobs.json>   jobs = [{out, lon, lat, zoom, w, h, style}]
const { chromium } = require('playwright');
const fs = require('fs'), path = require('path');

(async () => {
  const jobs = JSON.parse(fs.readFileSync(process.argv[2], 'utf8'));
  const lib = path.dirname(require.resolve('maplibre-gl/dist/maplibre-gl.js'));
  const b = await chromium.launch({ args: ['--use-angle=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist'] });
  for (const j of jobs) {
    const p = await b.newPage({ viewport: { width: j.w, height: j.h }, deviceScaleFactor: 2 });
    const errs = [];
    p.on('pageerror', e => errs.push(e.message));
    p.on('console', m => { if (m.type() === 'error') errs.push(m.text().slice(0, 200)); });
    await p.setContent('<!doctype html><html><head><style>html,body,#m{margin:0;width:100%;height:100%;background:#F2F3F5}</style></head><body><div id="m"></div></body></html>');
    await p.addStyleTag({ path: path.join(lib, 'maplibre-gl.css') });
    await p.addScriptTag({ path: path.join(lib, 'maplibre-gl.js') });
    const ok = await p.evaluate(j => new Promise(res => {
      const map = new maplibregl.Map({ container: 'm', style: j.style, center: [j.lon, j.lat], zoom: j.zoom, interactive: false,
        attributionControl: false, fadeDuration: 0, canvasContextAttributes: { preserveDrawingBuffer: true } });
      map.on('error', e => console.error('carte : ' + (e.error && e.error.message)));
      const t = setTimeout(() => res(false), 45000);
      map.once('idle', () => { clearTimeout(t); res(true); });
    }), j);
    if (!ok || errs.length) { console.error('carte', j.out, ok ? '' : 'délai dépassé', [...new Set(errs)].slice(0, 5).join(' | ')); process.exitCode = 1; }
    await p.screenshot({ path: j.out, type: 'png' });
    await p.close();
  }
  await b.close();
})();

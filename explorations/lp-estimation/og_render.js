// Images d'aperçu (1200 × 630) des pages d'estimation, pour les partages de lien (WhatsApp, Facebook, SMS).
// Appelé par build.py : node og_render.js <fichier de tâches JSON>. Nécessite Playwright.
const fs = require('fs');
const { chromium } = require('playwright');

(async () => {
  const jobs = JSON.parse(fs.readFileSync(process.argv[2], 'utf8'));
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1200, height: 630 } });
  for (const job of jobs) {
    await page.setContent(job.html, { waitUntil: 'load' });
    await page.evaluate(() => document.fonts.ready);
    await page.screenshot({ path: job.out, type: 'png' });
  }
  await browser.close();
})();

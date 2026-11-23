// Génère « Lancer un client - Bartier & Co.pdf » depuis process-client.html : node render_pdf.js
// L'aperçu de l'e-mail à l'artisan est produit par le vrai script du tableau (lp-estimation/sheets/apps-script.gs).
const fs = require('fs'), path = require('path'), vm = require('vm');
const { chromium } = require('playwright');
const HERE = __dirname;

function apercuEmail() {
  let html = '';
  const ctx = { console, MailApp: { sendEmail: (o) => { html = o.htmlBody; } } };
  vm.createContext(ctx);
  vm.runInContext(fs.readFileSync(path.join(HERE, '..', 'lp-estimation', 'sheets', 'apps-script.gs'), 'utf8'), ctx);
  ctx.alerter(['artisan@exemple.fr'], 'Toitures Dupont', {
    metier: 'Toiture',
    fields: { prenom: 'Jeanne', telephone: '+33612345678', code_postal: '59000', commune: 'Lille', travaux: 'Réfection de la couverture',
      quantite: '100 m²', estimation: '9 000 € à 16 000 €', details: 'Tuiles mécaniques · Gouttières à changer', delai: 'Dans 1 à 3 mois', statut: 'Propriétaire occupant' },
  });
  return html;
}

(async () => {
  const src = fs.readFileSync(path.join(HERE, 'process-client.html'), 'utf8').replace('<!--EMAIL-->', apercuEmail());
  const tmp = path.join(HERE, '.process-client.rendu.html');
  fs.writeFileSync(tmp, src);
  const b = await chromium.launch();
  const p = await b.newPage();
  await p.goto('file://' + tmp, { waitUntil: 'networkidle' });
  await p.evaluate(() => document.fonts.ready);
  const out = path.join(HERE, 'Lancer un client - Bartier & Co.pdf');
  await p.pdf({ path: out, format: 'A4', printBackground: true, preferCSSPageSize: true });
  await b.close();
  fs.unlinkSync(tmp);
  console.log('PDF :', out);
})();

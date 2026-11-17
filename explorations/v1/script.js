(() => {
    /* En-tête : filet sous la barre une fois la page défilée */
  const header = document.querySelector('.site-header');
  if (header) {
    const onScroll = () => header.classList.toggle('is-scrolled', window.scrollY > 8);
    onScroll();
    window.addEventListener('scroll', onScroll, { passive: true });
  }

  /* Bouton mobile : masqué sur le héros et sur le formulaire */
  const cta = document.querySelector('.mobile-cta');
  const hideOn = [document.querySelector('.hero'), document.querySelector('#secteur'), document.querySelector('.site-footer')].filter(Boolean);
  if (cta && 'IntersectionObserver' in window) {
    const visible = new Set();
    const io = new IntersectionObserver((entries) => {
      entries.forEach((e) => (e.isIntersecting ? visible.add(e.target) : visible.delete(e.target)));
      cta.classList.toggle('is-hidden', visible.size > 0);
    }, { threshold: 0.15 });
    hideOn.forEach((el) => io.observe(el));
  }

  /* Formulaire en étapes */
  const form = document.getElementById('qform');
  if (!form) return;
  const stepsEls = [...form.querySelectorAll('.qstep')];
  const count = form.querySelector('.qform-count');
  const bar = form.querySelector('.qform-bar span');
  const back = form.querySelector('.btn-back');
  const next = form.querySelector('.btn-next');
  const error = form.querySelector('.qform-error');
  const done = form.querySelector('.qform-done');
  let current = 0;

  const show = (i, focus) => {
    current = i;
    stepsEls.forEach((s, k) => s.classList.toggle('is-current', k === i));
    const last = i === stepsEls.length - 1;
    form.classList.toggle('is-last', last);
    back.hidden = i === 0;
    count.textContent = i < 4 ? `Question ${i + 1} sur 4` : 'Vos coordonnées';
    bar.style.transform = `scaleX(${(i + 1) / stepsEls.length})`;
    error.hidden = true;
    if (focus) {
      const first = stepsEls[i].querySelector('input, select');
      if (first) first.focus({ preventScroll: true });
    }
  };

  const valid = (i) => {
    const fields = [...stepsEls[i].querySelectorAll('input, select')];
    let ok = true;
    const radios = fields.filter((f) => f.type === 'radio');
    if (radios.length && !radios.some((r) => r.checked)) ok = false;
    fields.filter((f) => f.type !== 'radio').forEach((f) => {
      const good = f.checkValidity() && (!f.required || f.value.trim() !== '');
      f.setAttribute('aria-invalid', good ? 'false' : 'true');
      if (!good) ok = false;
    });
    if (!ok) {
      error.textContent = radios.length ? 'Choisissez une réponse pour continuer.' : 'Merci de compléter les champs indiqués.';
      error.hidden = false;
    }
    return ok;
  };

  next.addEventListener('click', () => { if (valid(current)) show(current + 1, true); });
  back.addEventListener('click', () => show(current - 1, true));

  /* Un choix fait avance automatiquement à la question suivante */
  form.addEventListener('change', (e) => {
    if (e.target.type === 'radio' && current < 4) setTimeout(() => show(current + 1, false), 220);
  });

  form.addEventListener('submit', (e) => {
    e.preventDefault();
    if (!valid(current)) return;
    /* Prototype : rien n'est envoyé. L'envoi par e-mail sera branché sur la version finale. */
    form.classList.add('is-done');
    done.hidden = false;
    done.focus();
  });

  /* Sur une page métier, le métier est déjà choisi : on commence à la question 2 */
  show(form.querySelector('input[name="metier"]:checked') ? 1 : 0, false);
})();

/* Source de la demande : page, UTM et identifiants de clic, conservés pendant la visite */
(() => {
  const form = document.getElementById('qform');
  if (!form) return;
  const keys = ['utm_source', 'utm_medium', 'utm_campaign', 'utm_content', 'utm_term', 'gclid', 'fbclid'];
  const params = new URLSearchParams(location.search);
  let stored = {};
  try { stored = JSON.parse(sessionStorage.getItem('bc_src') || '{}'); } catch (e) {}
  keys.forEach((k) => { if (params.get(k)) stored[k] = params.get(k); });
  try { sessionStorage.setItem('bc_src', JSON.stringify(stored)); } catch (e) {}
  keys.forEach((k) => { const f = form.elements[k]; if (f && stored[k]) f.value = stored[k]; });
  if (form.elements.page) form.elements.page.value = location.pathname;
})();

/* Simulateur : chiffre d'affaires en plus, calculé avec les chiffres de l'artisan */
(() => {
  const rdv = document.getElementById('s-rdv');
  if (!rdv) return;
  const panier = document.getElementById('s-panier');
  const taux = document.getElementById('s-taux');
  const eur = (n) => new Intl.NumberFormat('fr-FR', { maximumFractionDigits: 0 }).format(Math.round(n)) + '\u00a0€';
  const fill = (el) => el.style.setProperty('--p', ((el.value - el.min) / (el.max - el.min) * 100) + '%');
  const set = (id, v) => { document.getElementById(id).textContent = v; };
  const update = () => {
    [rdv, panier, taux].forEach(fill);
    const chantiers = rdv.value * taux.value / 100;
    const mois = chantiers * panier.value;
    set('o-rdv', rdv.value);
    set('o-panier', eur(panier.value));
    set('o-taux', taux.value + '\u00a0%');
    set('r-chantiers', chantiers.toLocaleString('fr-FR', { maximumFractionDigits: 1 }));
    set('r-mois', eur(mois));
    set('r-an', eur(mois * 12));
  };
  [rdv, panier, taux].forEach((el) => el.addEventListener('input', update));
  update();
})();

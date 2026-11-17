(() => {
  const reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* Le cordeau de la méthode se tend au fil du défilement */
  const steps = document.querySelector('.steps');
  if (steps && !reduce) {
    const update = () => {
      const r = steps.getBoundingClientRect();
      const vh = window.innerHeight;
      const p = Math.min(1, Math.max(0, (vh * 0.7 - r.top) / r.height));
      steps.style.setProperty('--progress', p.toFixed(3));
    };
    update();
    window.addEventListener('scroll', update, { passive: true });
    window.addEventListener('resize', update);
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

/* Sélecteur de palette : aperçu uniquement, à retirer une fois la palette choisie */
(() => {
  const root = document.documentElement;
  const names = { a: 'Cobalt', b: 'Outremer', c: 'Ardoise' };
  const box = document.createElement('div');
  box.className = 'palette-picker';
  box.setAttribute('role', 'group');
  box.setAttribute('aria-label', 'Choisir le bleu');
  box.innerHTML = '<span>Bleu</span>' + Object.keys(names).map((k) => `<button type="button" data-p="${k}" title="${names[k]}" aria-label="Palette ${names[k]}">${k.toUpperCase()}</button>`).join('');
  const sync = () => box.querySelectorAll('button').forEach((b) => b.setAttribute('aria-pressed', String((root.dataset.palette || 'a') === b.dataset.p)));
  box.addEventListener('click', (e) => {
    const b = e.target.closest('button'); if (!b) return;
    const p = b.dataset.p;
    if (p === 'a') delete root.dataset.palette; else root.dataset.palette = p;
    try { localStorage.setItem('bc_palette', p); } catch (err) {}
    sync();
  });
  sync();
  document.body.appendChild(box);
})();

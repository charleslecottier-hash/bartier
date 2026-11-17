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

  show(0, false);
})();

# Animations « téléphone » des pages Google Ads et Meta Ads :
# l'annonce, le clic, la page, le formulaire qualifiant, puis le rappel.

SIG = '<svg viewBox="0 0 64 14" aria-hidden="true"><g fill="currentColor"><rect x="0" y="9" width="3" height="5" rx="1"/><rect x="5" y="6" width="3" height="8" rx="1"/><rect x="10" y="3" width="3" height="11" rx="1"/><rect x="15" y="0" width="3" height="14" rx="1"/><path d="M30 4.2a9 9 0 0 1 12 0l-1.4 1.5a7 7 0 0 0-9.2 0zM32.6 7a5.2 5.2 0 0 1 6.8 0L38 8.5a3.2 3.2 0 0 0-4 0zM36 10.2l1.6 1.6L36 13.4l-1.6-1.6z"/><rect x="46" y="2" width="15" height="10" rx="3" fill="none" stroke="currentColor" stroke-width="1.2"/><rect x="47.8" y="3.8" width="10" height="6.4" rx="1.6"/><rect x="62" y="5.5" width="1.5" height="3" rx=".7"/></g></svg>'
LOCK = '<svg viewBox="0 0 10 12" aria-hidden="true"><path fill="currentColor" d="M2 5V3.5a3 3 0 0 1 6 0V5h.5A1.5 1.5 0 0 1 10 6.5v4A1.5 1.5 0 0 1 8.5 12h-7A1.5 1.5 0 0 1 0 10.5v-4A1.5 1.5 0 0 1 1.5 5zm1.4 0h3.2V3.5a1.6 1.6 0 0 0-3.2 0z"/></svg>'
MAG = '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="10.5" cy="10.5" r="6.5" fill="none" stroke="currentColor" stroke-width="2.2"/><path d="m15.5 15.5 5 5" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/></svg>'
PHONE = '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2a1 1 0 0 1 1-.25 11.4 11.4 0 0 0 3.6.57 1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1c0 1.25.2 2.45.57 3.57a1 1 0 0 1-.25 1z"/></svg>'


def _browser():
    return f'<div class="br"><span class="br-x">✕</span><span class="br-url">{LOCK}toitures-martin.fr</span><span class="br-x">⋯</span></div>'


def _lp(roof, kick, title):
    return f"""<div class="sc sc-lp">{_browser()}
      <div class="lp-body">
        <div class="lp-hero"><img src="{roof}" alt="" loading="lazy"><span class="lp-logo">Toitures Martin</span></div>
        <div class="lp-in">
          <p class="lp-kick">{kick}</p>
          <p class="lp-h">{title}</p>
          <ul class="lp-ok"><li>Visite et devis offerts</li><li>Garantie décennale</li><li>Rappel en moins de 5 minutes</li></ul>
          <span class="lp-btn">Vérifier mon projet en 30 s</span>
          <p class="lp-note">Sans engagement · Réponse aujourd’hui</p>
          <div class="lp-ghost"><i></i><i></i><i></i></div>
        </div>
      </div>
    </div>"""


def _form(qs):
    n = len(qs)
    blocks = []
    for i, q in enumerate(qs, 1):
        if q[0] == "opt":
            opts = "".join(f'<span class="o o{j}">{o}</span>' for j, o in enumerate(q[2], 1))
            blocks.append(f'<div class="q q{i}"><p class="q-t">{q[1]}</p>{opts}</div>')
        else:
            _, label, ph, btn, hint = q
            blocks.append(f'<div class="q q{i}"><p class="q-t">{label}</p><p class="in"><span class="in-v" data-ph="{ph}">{ph}</span><i></i></p><span class="nx">{btn}</span><p class="q-hint">{hint}</p></div>')
    return f"""<div class="sc sc-form">{_browser()}
      <div class="fm">
        <p class="fm-h">Votre visite gratuite</p>
        <p class="fm-step">Étape <b class="fm-n">1</b> sur {n}</p>
        <p class="fm-bar"><i style="width:{100 / n:.0f}%"></i></p>
        <div class="fm-qs" data-n="{n}">{"".join(blocks)}</div>
      </div>
    </div>"""


def _done(summary):
    return f"""<div class="sc sc-done">{_browser()}
      <div class="dn">
        <span class="dn-ok"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="m5 12.5 4.5 4.5L19 7.5" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
        <p class="dn-h">Demande envoyée</p>
        <p class="dn-p">Un conseiller vous rappelle dans les 5 minutes pour fixer la visite.</p>
        <ul class="dn-sum">{"".join(f"<li><span>{a}</span><b>{b}</b></li>" for a, b in summary)}</ul>
      </div>
    </div>"""


CALL = f"""<div class="sc sc-call" data-dark>
      <div class="cl-top"><p class="cl-sub">Appel mobile…</p><p class="cl-name">Toitures Martin</p><p class="cl-sub">Amiens</p><p class="cl-chip">Demande envoyée il y a 3 min</p></div>
      <p class="cl-live">Rendez-vous de visite<br><b>jeudi 10 h, à votre domicile</b></p>
      <div class="cl-btns"><span class="cl-b is-no">{PHONE}<small>Refuser</small></span><span class="cl-b is-ok">{PHONE}<small>Accepter</small></span></div>
    </div>"""


def _phone(flow, label, scenes, chapters):
    steps = "".join(f"<li>{c}</li>" for c in chapters)
    return f"""<figure class="pg-photo mk mk-anim" aria-label="{label}">
  <div class="ph" data-flow="{flow}">
    <div class="ph-screen">
      <div class="ph-status"><b>9:41</b>{SIG}</div>
      {scenes}
      <span class="ph-tap" aria-hidden="true"></span>
    </div>
  </div>
  <ol class="ph-steps" aria-hidden="true">{steps}</ol>
  <figcaption class="mk-tag">Exemple</figcaption>
</figure>"""


def meta_anim(roof):
    feed = f"""<div class="sc sc-feed is-on">
      <div class="fd-bar"><b>Accueil</b><span><i></i><i></i><i></i></span></div>
      <div class="fd-list">
        <div class="fd-ghost"><p class="fd-who"><i></i><span><b></b><small></small></span></p><p class="fd-l"></p><p class="fd-l is-s"></p><div class="fd-pic"></div></div>
        <div class="ad">
          <p class="fd-who"><span class="av">TM</span><span><b>Toitures Martin</b><small>Sponsorisé · Amiens</small></span></p>
          <p class="ad-t">Votre toiture a plus de 15 ans&nbsp;? Avant l’hiver, faites-la vérifier par un couvreur de votre secteur. Visite et chiffrage offerts.</p>
          <div class="ad-img"><img src="{roof}" alt="" loading="lazy"></div>
          <div class="ad-link"><span><small>TOITURES-MARTIN.FR</small><b>Visite gratuite à domicile</b></span><em class="ad-cta">Demander une visite</em></div>
          <p class="ad-re"><span>👍❤️ 48</span><span>12 commentaires · 3 partages</span></p>
          <p class="ad-act"><span>J’aime</span><span>Commenter</span><span>Partager</span></p>
        </div>
      </div>
    </div>"""
    qs = [("opt", "Votre toiture a quel âge&nbsp;?", ["Moins de 10 ans", "10 à 20 ans", "Plus de 20 ans"]),
          ("opt", "Qu’avez-vous remarqué&nbsp;?", ["Mousse, salissures", "Tuiles abîmées, infiltrations", "Rien, un simple contrôle"]),
          ("opt", "Vous êtes propriétaire&nbsp;?", ["Oui", "Non, locataire"]),
          ("in", "Votre code postal", "", "Continuer", "Nous intervenons à 40 km autour d’Amiens"),
          ("in", "Votre téléphone", "", "Être rappelé", "Rappel en moins de 5 minutes, du lundi au vendredi")]
    scenes = feed + _lp(roof, "Couvreur à Amiens et alentours", "Votre toiture vérifiée avant les premières pluies.") + _form(qs) + \
        _done([("Toiture", "Plus de 20 ans"), ("Constat", "Infiltrations"), ("Secteur", "80090 Amiens")]) + CALL
    return _phone("meta", "Exemple animé : une annonce Facebook, la page de l’artisan, le formulaire, puis le rappel", scenes,
                  ["L’annonce", "La page", "Le formulaire", "Le rappel"])


def google_anim(roof):
    sugg = ["couvreur amiens <b>devis réfection toiture</b>", "couvreur amiens <b>prix au m2</b>", "couvreur amiens <b>urgence fuite</b>", "couvreur amiens <b>avis</b>"]
    search = f"""<div class="sc sc-search is-on">
      <div class="gs-field">{MAG}<span class="gs-q" data-t=""></span><i class="caret"></i></div>
      <ul class="gs-sug">{"".join(f"<li>{MAG}<span>{s}</span></li>" for s in sugg)}</ul>
      <div class="gs-empty"><p>Recherches récentes</p><span></span><span></span></div>
    </div>"""
    serp = f"""<div class="sc sc-serp">
      <div class="gs-field is-top">{MAG}<span>couvreur amiens devis réfection toiture</span></div>
      <p class="gs-tabs"><b>Tous</b><span>Maps</span><span>Images</span><span>Actualités</span></p>
      <div class="gs-ad">
        <p class="gs-spon">Sponsorisé</p>
        <p class="gs-site"><span class="av">TM</span><span><b>Toitures Martin</b><small>toitures-martin.fr › devis</small></span></p>
        <p class="gs-title">Réfection de toiture à Amiens · Devis gratuit sous 48 h</p>
        <p class="gs-desc">Couvreur local, garantie décennale. Visite et chiffrage offerts, rappel en 5 minutes.</p>
        <p class="gs-links"><span>Prix d’une réfection</span><span>Nos chantiers</span></p>
        <p class="gs-call">{PHONE}Appeler</p>
      </div>
      <div class="gs-map"><i></i><span><b></b><small></small><small></small></span></div>
      <div class="gs-org"><i></i><i></i><i></i></div>
    </div>"""
    qs = [("opt", "Quel est votre projet&nbsp;?", ["Réfection complète", "Réparation, fuite", "Démoussage, entretien"]),
          ("opt", "Quand souhaitez-vous démarrer&nbsp;?", ["Dès que possible", "Dans 1 à 3 mois", "Je me renseigne"]),
          ("opt", "Vous êtes propriétaire&nbsp;?", ["Oui", "Non, locataire"]),
          ("in", "Votre code postal", "", "Continuer", "Nous intervenons à 40 km autour d’Amiens"),
          ("in", "Votre téléphone", "", "Recevoir mon devis", "Rappel en moins de 5 minutes, du lundi au vendredi")]
    scenes = search + serp + _lp(roof, "Réfection de toiture · Amiens", "Votre devis de toiture sous 48 h, après visite.") + _form(qs) + \
        _done([("Projet", "Réfection complète"), ("Démarrage", "Dès que possible"), ("Secteur", "80090 Amiens")]) + CALL
    return _phone("google", "Exemple animé : une recherche Google, l’annonce, la page de l’artisan, le formulaire, puis le rappel", scenes,
                  ["La recherche", "Le clic", "Le formulaire", "Le rappel"])


ANIM_CSS = """
.pg-photo.mk-anim{grid-template-rows:auto auto;gap:18px;padding:clamp(24px,3vw,40px) 12px}
.ph{position:relative;width:286px;height:590px;padding:9px;background:#0b0f17;border-radius:46px;box-shadow:inset 0 0 0 1.5px #2b3242,0 40px 80px -34px rgba(10,20,36,.65);flex:none}
.ph-screen{position:relative;height:100%;border-radius:38px;overflow:hidden;background:#fff;color:#0b0f17;font:13px/1.35 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;letter-spacing:0;isolation:isolate}
.ph-screen::before{content:"";position:absolute;top:9px;left:50%;width:82px;height:24px;margin-left:-41px;border-radius:14px;background:#000;z-index:30}
.ph-status{position:absolute;inset:0 0 auto;height:42px;display:flex;align-items:center;justify-content:space-between;padding:0 24px 0 30px;font-size:13.5px;z-index:25;transition:color .4s}
.ph-status svg{width:58px;height:13px}
.ph.is-dark .ph-status{color:#fff}
.pg-photo .ph img{filter:none}
.sc{position:absolute;inset:0;padding-top:42px;background:#fff;overflow:hidden;transform:translateX(100%);transition:transform .6s cubic-bezier(.2,.8,.2,1),opacity .6s}
.sc.is-on{transform:none;z-index:2}
.sc.is-off{transform:translateX(-30%);opacity:0}
.ph-tap{position:absolute;left:50%;top:60%;width:38px;height:38px;margin:-19px 0 0 -19px;border-radius:50%;background:rgba(10,20,36,.22);box-shadow:0 0 0 2px rgba(255,255,255,.7);opacity:0;z-index:40;pointer-events:none;transition:left .55s cubic-bezier(.4,0,.2,1),top .55s cubic-bezier(.4,0,.2,1),opacity .3s,transform .18s}
.ph-tap.is-vis{opacity:1}
.ph-tap.is-tap{transform:scale(.72);background:rgba(10,20,36,.36)}
.is-press{transform:scale(.96);filter:brightness(.92)}
.ph-steps{display:flex;flex-wrap:wrap;justify-content:center;gap:6px;margin:0;padding:0;list-style:none;font-size:.78rem;color:var(--muted)}
.ph-steps li{padding:.35em .7em;border-radius:99px;background:var(--bg);transition:background-color .3s,color .3s}
.ph-steps li.is-on{background:var(--accent);color:#fff}
.ph-steps li.is-done{color:var(--ink)}
/* Fil d'actualité */
.fd-bar{display:flex;align-items:center;justify-content:space-between;padding:4px 14px 9px;border-bottom:1px solid #e4e6eb}
.fd-bar b{font-size:19px;letter-spacing:-.02em}
.fd-bar span{display:flex;gap:7px}.fd-bar i{width:28px;height:28px;border-radius:50%;background:#e4e6eb}
.fd-list{background:#c9ccd1;transition:transform 1.4s cubic-bezier(.4,0,.2,1)}
.fd-ghost,.ad{background:#fff;margin-bottom:7px;padding-top:10px}
.fd-who{display:flex;align-items:center;gap:8px;padding:0 12px 8px}
.fd-who i,.av{display:grid;place-items:center;width:34px;height:34px;border-radius:50%;background:#d8dadf;flex:none}
.av{background:#7c2d12;color:#fff;font-size:11px;font-weight:700}
.fd-who b{display:block;font-size:13.5px}.fd-who small{display:block;color:#65676b;font-size:11.5px}
.fd-ghost .fd-who b{width:90px;height:9px;border-radius:5px;background:#d8dadf}.fd-ghost .fd-who small{width:60px;height:7px;margin-top:5px;border-radius:4px;background:#e4e6eb}
.fd-l{height:8px;margin:4px 12px;border-radius:4px;background:#e4e6eb}.fd-l.is-s{width:55%}
.fd-pic{height:150px;margin-top:9px;background:linear-gradient(135deg,#dfe5ec,#c8d3df)}
.ad-t{padding:0 12px 9px;font-size:13px}
.ad-img{height:172px;background:#ddd}.ad-img img{width:100%;height:100%;object-fit:cover}
.ad-link{display:flex;align-items:center;justify-content:space-between;gap:8px;padding:9px 12px;background:#f0f2f5}
.ad-link span{min-width:0}.ad-link small{display:block;color:#65676b;font-size:10.5px}.ad-link b{display:block;font-size:13px}
.ad-cta{flex:none;padding:7px 10px;border-radius:6px;background:#e2e5e9;font-style:normal;font-weight:600;font-size:12.5px;transition:transform .15s,filter .15s}
.ad-re{display:flex;justify-content:space-between;padding:8px 12px;color:#65676b;font-size:11.5px;border-bottom:1px solid #e4e6eb;margin:0 0}
.ad-act{display:flex;justify-content:space-around;padding:8px 0 10px;color:#65676b;font-weight:600;font-size:12px}
/* Recherche */
.gs-field{display:flex;align-items:center;gap:9px;height:44px;margin:10px 12px;padding:0 14px;border-radius:22px;background:#f1f3f4;font-size:14.5px;color:#202124}
.gs-field svg{width:17px;height:17px;flex:none;color:#5f6368}
.gs-field.is-top{margin-top:6px;background:#fff;box-shadow:0 1px 6px rgba(32,33,36,.28)}
.gs-field.is-top span{white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.caret{width:1.5px;height:18px;margin-left:-6px;background:#1a73e8;animation:phblink 1s steps(1) infinite}
@keyframes phblink{50%{opacity:0}}
.gs-sug{margin:0;padding:0;list-style:none;opacity:0;transform:translateY(-4px);transition:opacity .25s,transform .25s}
.gs-sug.is-show{opacity:1;transform:none}
.gs-sug li{display:flex;align-items:center;gap:12px;padding:11px 18px;font-size:14px;color:#202124;transition:background-color .15s}
.gs-sug li svg{width:15px;height:15px;color:#9aa0a6;flex:none}
.gs-sug li.is-press{background:#e8eaed;transform:none}
.gs-empty{padding:16px 18px;color:#5f6368;font-size:12px}.gs-empty span{display:block;height:9px;margin-top:12px;border-radius:5px;background:#f1f3f4;width:70%}
.gs-sug.is-show + .gs-empty{display:none}
.gs-tabs{display:flex;gap:16px;padding:0 16px 8px;border-bottom:1px solid #ebebeb;font-size:12.5px;color:#5f6368}.gs-tabs b{color:#1a73e8;font-weight:500;box-shadow:0 9px 0 -6px #1a73e8}
.gs-ad{padding:12px 16px;border-bottom:7px solid #f1f3f4}
.gs-spon{font-weight:700;font-size:12px;margin-bottom:6px}
.gs-site{display:flex;align-items:center;gap:9px;font-size:12px}.gs-site .av{width:26px;height:26px;font-size:9.5px}.gs-site small{display:block;color:#4d5156;font-size:11px}
.gs-title{margin:7px 0 4px;color:#1a0dab;font-size:17px;line-height:1.28;transition:transform .15s,filter .15s}
.gs-desc{color:#4d5156;font-size:12.5px;line-height:1.45}
.gs-links{display:flex;gap:6px;margin-top:9px}.gs-links span{padding:5px 10px;border:1px solid #dadce0;border-radius:16px;color:#1a0dab;font-size:11.5px}
.gs-call{display:inline-flex;align-items:center;gap:5px;margin-top:9px;padding:6px 12px;border-radius:16px;background:#e8f0fe;color:#1967d2;font-size:12px;font-weight:500}.gs-call svg{width:13px;height:13px}
.gs-map{display:flex;gap:10px;padding:12px 16px;border-bottom:7px solid #f1f3f4}.gs-map i{width:70px;height:56px;border-radius:8px;background:linear-gradient(135deg,#e6efe3,#d5e3ee)}.gs-map b,.gs-map small{display:block;height:8px;margin:5px 0;border-radius:4px;background:#e8eaed;width:120px}.gs-map small{width:90px}
.gs-org{padding:12px 16px}.gs-org i{display:block;height:8px;margin:7px 0;border-radius:4px;background:#eef0f2}.gs-org i:first-child{width:50%;height:11px;background:#e3e6f5}.gs-org i:nth-child(3){width:75%}
/* Page de l'artisan */
.br{position:relative;z-index:3;display:flex;align-items:center;justify-content:space-between;height:36px;padding:0 14px;border-bottom:1px solid #e9e9ec;background:#f6f6f8;font-size:12px;color:#3c3c43}
.br-url{display:flex;align-items:center;gap:5px;font-weight:500}.br-url svg{width:9px;height:11px;color:#6b6b70}
.br-x{width:16px;text-align:center;color:#6b6b70}
.lp-body{transition:transform 1.1s cubic-bezier(.4,0,.2,1)}
.lp-hero{position:relative;height:150px;background:#ccc}.lp-hero img{width:100%;height:100%;object-fit:cover}
.lp-logo{position:absolute;left:12px;top:10px;padding:4px 8px;border-radius:4px;background:#fff;font-weight:800;font-size:11px;letter-spacing:-.01em;color:#7c2d12}
.lp-in{padding:14px 16px}
.lp-kick{color:#c2410c;font-weight:700;font-size:11px;text-transform:uppercase;letter-spacing:.04em}
.lp-h{margin:6px 0 10px;font-size:21px;line-height:1.15;font-weight:800;letter-spacing:-.02em}
.lp-ok{margin:0 0 14px;padding:0;list-style:none;font-size:12.5px}.lp-ok li{padding-left:20px;margin:5px 0;background:no-repeat 0 50%/13px url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Cpath d='m5 12.5 4.5 4.5L19 7.5' fill='none' stroke='%23c2410c' stroke-width='3' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E")}
.lp-btn{display:block;padding:13px;border-radius:10px;background:#c2410c;color:#fff;text-align:center;font-weight:700;font-size:14px;box-shadow:0 8px 18px -10px #c2410c;transition:transform .15s,filter .15s}
.lp-note{margin-top:7px;text-align:center;color:#6b6b70;font-size:11px}
.lp-ghost{margin-top:18px}.lp-ghost i{display:block;height:8px;margin:7px 0;border-radius:4px;background:#efefef}.lp-ghost i:nth-child(2){width:80%}
/* Formulaire */
.fm{padding:16px}
.fm-h{font-weight:800;font-size:17px;letter-spacing:-.01em}
.fm-step{margin-top:3px;color:#6b6b70;font-size:11.5px}
.fm-bar{height:5px;margin:8px 0 16px;border-radius:3px;background:#f0e4dc}.fm-bar i{display:block;height:100%;border-radius:3px;background:#c2410c;transition:width .45s cubic-bezier(.4,0,.2,1)}
.fm-qs{position:relative;height:340px}
.q{position:absolute;inset:0;opacity:0;transform:translateX(24px);transition:opacity .35s,transform .35s;pointer-events:none}
.q.is-on{opacity:1;transform:none}
.q.is-off{opacity:0;transform:translateX(-24px)}
.q-t{margin-bottom:12px;font-weight:700;font-size:15px}
.o{display:flex;align-items:center;gap:10px;margin-bottom:9px;padding:12px;border:1.5px solid #e2e2e6;border-radius:10px;font-size:13.5px;transition:border-color .2s,background-color .2s,transform .15s}
.o::before{content:"";width:16px;height:16px;border-radius:50%;border:1.5px solid #b8b8bf;flex:none;transition:border .2s,background .2s}
.o.is-sel{border-color:#c2410c;background:#fff4ed}
.o.is-sel::before{border:5px solid #c2410c}
.in{display:flex;align-items:center;height:46px;padding:0 13px;border:1.5px solid #c2410c;border-radius:10px;font-size:16px;letter-spacing:.02em;box-shadow:0 0 0 4px #fde6d8}
.in i{width:1.5px;height:20px;margin-left:1px;background:#c2410c;animation:phblink 1s steps(1) infinite}
.nx{display:block;margin-top:12px;padding:13px;border-radius:10px;background:#c2410c;color:#fff;text-align:center;font-weight:700;font-size:14px;transition:transform .15s,filter .15s}
.q-hint{margin-top:9px;color:#6b6b70;font-size:11px;text-align:center}
/* Confirmation */
.dn{padding:40px 18px 0;text-align:center}
.dn-ok{display:inline-grid;place-items:center;width:62px;height:62px;border-radius:50%;background:#16a34a;color:#fff;transform:scale(.4);opacity:0;transition:transform .5s cubic-bezier(.3,1.6,.5,1),opacity .3s}
.dn-ok svg{width:30px;height:30px}
.sc-done.is-on .dn-ok{transform:none;opacity:1;transition-delay:.35s}
.dn-h{margin-top:14px;font-weight:800;font-size:19px}
.dn-p{margin:6px auto 18px;max-width:22ch;color:#3c3c43;font-size:13px}
.dn-sum{margin:0;padding:4px 14px;list-style:none;text-align:left;border-radius:12px;background:#f6f6f8}
.dn-sum li{display:flex;justify-content:space-between;gap:10px;padding:9px 0;font-size:12.5px}.dn-sum li + li{border-top:1px solid #e9e9ec}.dn-sum span{color:#6b6b70}
/* Appel */
.sc-call{display:flex;flex-direction:column;justify-content:space-between;padding:84px 0 46px;background:linear-gradient(180deg,#3a4a5f,#1b2431 55%,#10161f);color:#fff;transform:translateY(-100%);text-align:center}
.sc-call.is-on{transform:none}
.cl-name{margin:6px 0 4px;font-size:27px;font-weight:400;letter-spacing:-.01em}
.cl-sub{color:rgba(255,255,255,.7);font-size:13px}
.cl-chip{display:inline-block;margin-top:14px;padding:5px 10px;border-radius:99px;background:rgba(255,255,255,.14);font-size:11.5px}
.cl-live{margin:0 24px;padding:12px;border-radius:14px;background:rgba(255,255,255,.12);font-size:12.5px;opacity:0;transform:translateY(8px);transition:opacity .4s,transform .4s}
.cl-live b{font-size:14px}
.sc-call.is-live .cl-live{opacity:1;transform:none}
.cl-btns{display:flex;justify-content:space-around;padding:0 30px}
.cl-b{display:flex;flex-direction:column;align-items:center;gap:7px;font-size:11.5px;transition:transform .15s,opacity .3s}
.cl-b svg{width:62px;height:62px;padding:18px;border-radius:50%;background:#ef4444}
.cl-b.is-no svg{transform:rotate(135deg)}
.cl-b.is-ok svg{background:#22c55e;animation:phring 1.2s ease-in-out infinite}
@keyframes phring{0%,100%{transform:rotate(0)}10%,30%{transform:rotate(-14deg)}20%,40%{transform:rotate(14deg)}50%{transform:rotate(0)}}
.sc-call.is-live .cl-b.is-ok{display:none}
.sc-call.is-live .cl-b.is-no small{visibility:hidden}
.sc-call.is-live .cl-sub:first-child{color:#fff}
@media (max-width:760px){.ph{width:270px;height:556px}.fm-qs{height:300px}}
@media (prefers-reduced-motion:reduce){.ph *{transition:none!important;animation:none!important}}
"""

ANIM_JS = r"""<script>
(function(){
var FLOWS={
 meta:[['chap',0],['w',900],['scroll','.fd-list',236],['w',1700],['tap','.ad-cta'],['chap',1],['scene','.sc-lp'],['w',1300],['scroll','.lp-body',96],['w',900],['tap','.lp-btn'],['chap',2],['scene','.sc-form'],['w',800],
   ['pick','.q1 .o3'],['next'],['pick','.q2 .o2'],['next'],['pick','.q3 .o1'],['next'],['type','.q4 .in-v','80090'],['w',350],['tap','.q4 .nx'],['next'],['type','.q5 .in-v','06 12 34 56 78'],['w',350],['tap','.q5 .nx'],
   ['scene','.sc-done'],['w',2300],['chap',3],['scene','.sc-call'],['w',2000],['tap','.cl-b.is-ok'],['live'],['w',3200]],
 google:[['chap',0],['w',700],['type','.gs-q','couvreur ami'],['show','.gs-sug'],['type','.gs-q','ens devis'],['w',600],['tap','.gs-sug li'],['scene','.sc-serp'],['chap',1],['w',2000],['tap','.gs-title'],['scene','.sc-lp'],['w',1200],['scroll','.lp-body',96],['w',800],['tap','.lp-btn'],['chap',2],['scene','.sc-form'],['w',800],
   ['pick','.q1 .o1'],['next'],['pick','.q2 .o1'],['next'],['pick','.q3 .o1'],['next'],['type','.q4 .in-v','80090'],['w',350],['tap','.q4 .nx'],['next'],['type','.q5 .in-v','06 12 34 56 78'],['w',350],['tap','.q5 .nx'],
   ['scene','.sc-done'],['w',2300],['chap',3],['scene','.sc-call'],['w',2000],['tap','.cl-b.is-ok'],['live'],['w',3200]]};
var reduce=window.matchMedia&&matchMedia('(prefers-reduced-motion: reduce)').matches;
function sleep(ms){return new Promise(function(r){setTimeout(r,ms)})}
document.querySelectorAll('.ph[data-flow]').forEach(function(ph){
 if(ph.dataset.run)return;ph.dataset.run=1;
 var scr=ph.querySelector('.ph-screen'),fig=ph.closest('figure'),chips=fig.querySelectorAll('.ph-steps li'),init=scr.innerHTML,vis=false,waiters=[];
 if(reduce){if(chips[0])chips[0].classList.add('is-on');return;}
 new IntersectionObserver(function(e){vis=e[0].isIntersecting;if(vis){waiters.forEach(function(f){f()});waiters=[];}},{threshold:.25}).observe(ph);
 function whenVisible(){return vis?Promise.resolve():new Promise(function(r){waiters.push(r)})}
 var q=1;
 function $(s){return scr.querySelector(s)}
 function tapAt(el){var t=$('.ph-tap'),a=el.getBoundingClientRect(),b=scr.getBoundingClientRect(),k=b.width/scr.offsetWidth||1;
  t.style.left=((a.left-b.left+a.width/2)/k)+'px';t.style.top=((a.top-b.top+a.height/2)/k)+'px';t.classList.add('is-vis');
  return sleep(600).then(function(){t.classList.add('is-tap');el.classList.add('is-press');return sleep(200)}).then(function(){t.classList.remove('is-tap');el.classList.remove('is-press');return sleep(160)}).then(function(){t.classList.remove('is-vis')})}
 var acts={
  w:function(ms){return sleep(ms)},
  chap:function(n){chips.forEach(function(c,i){c.classList.toggle('is-on',i===n);c.classList.toggle('is-done',i<n)});},
  scroll:function(s,px){$(s).style.transform='translateY(-'+px+'px)'},
  tap:function(s){return tapAt($(s))},
  scene:function(s){var c=scr.querySelector('.sc.is-on'),n=$(s);if(c){c.classList.remove('is-on');c.classList.add('is-off')}n.classList.add('is-on');ph.classList.toggle('is-dark',n.hasAttribute('data-dark'));return sleep(650)},
  show:function(s){$(s).classList.add('is-show')},
  type:function(s,txt){var el=$(s),i=0;return (function step(){if(i>=txt.length)return Promise.resolve();el.textContent+=txt[i++];return sleep(70+Math.random()*90).then(step)})()},
  pick:function(s){var el=$(s);return tapAt(el).then(function(){el.classList.add('is-sel');return sleep(450)})},
  next:function(){var qs=scr.querySelectorAll('.q'),n=qs.length;if(qs[q-1]){qs[q-1].classList.remove('is-on');qs[q-1].classList.add('is-off')}q++;if(qs[q-1])qs[q-1].classList.add('is-on');$('.fm-n').textContent=q;$('.fm-bar i').style.width=(100*q/n)+'%';return sleep(450)},
  live:function(){var c=$('.sc-call'),s=c.querySelector('.cl-sub'),t=0;c.classList.add('is-live');s.textContent='00:00';var id=setInterval(function(){t++;s.textContent='00:0'+t},1000);return sleep(3100).then(function(){clearInterval(id)})}
 };
 (async function loop(){
  for(;;){await whenVisible();scr.innerHTML=init;ph.classList.remove('is-dark');q=1;var f=scr.querySelector('.q1');if(f)f.classList.add('is-on');
   await sleep(60);
   for(var i=0;i<FLOWS[ph.dataset.flow].length;i++){var st=FLOWS[ph.dataset.flow][i];await acts[st[0]].apply(null,st.slice(1));}
   await sleep(800);}
 })();
});
})();
</script>"""

# Le générateur remplace les apostrophes droites par des typographiques : le script n'utilise que des guillemets doubles.
ANIM_JS = ANIM_JS.replace("'", '"')

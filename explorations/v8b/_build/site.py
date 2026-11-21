"""Construit le site multi-pages Bartier & Co dans le design 8B.

Source : index.html (page d'accueil 8B, retouchée à la main).
Contenus des pages métiers, Google Ads, Meta Ads, Qui sommes-nous et blog : repris de ../v1/_build.

    python3 _build/site.py
"""
import html
import json
import pathlib
import re
import runpy

ROOT = pathlib.Path(__file__).resolve().parent.parent
V1 = ROOT.parent / "v1" / "_build"
SITE = "https://bartierandco.com"
TODAY = "2026-11-17"  # date de publication des trois premiers articles
BUILD = __import__("datetime").date.today().isoformat()
# Mise en ligne : passer LIVE à True le jour où bartierandco.com pointe vers ce site.
# Tant que LIVE est False, toutes les pages portent « noindex » (la préversion ne doit pas être référencée).
LIVE = True
INDEXNOW_KEY = "9e243e36d5aa224c04b988c6e4c145d3"  # clé publique IndexNow (Bing, et donc ChatGPT), servie à /<clé>.txt
NB = " "

M = runpy.run_path(str(V1 / "metiers.py"))
P = runpy.run_path(str(V1 / "pages.py"))
TRADES, PROJECT, ARTICLES = M["TRADES"], M["PROJECT"], P["ARTICLES"]
GOOGLE_FAQ, META_FAQ = P["GOOGLE_FAQ"], P["META_FAQ"]


DD_JS = '<script id="dd-js">(function(){document.querySelectorAll(".hdr-dd").forEach(function(dd){var t=dd.querySelector(".hdr-dd-t"),m=dd.querySelector(".hdr-dd-menu");if(!t||!m)return;var set=function(o){dd.classList.toggle("is-open",o);t.setAttribute("aria-expanded",String(o))};t.addEventListener("keydown",function(e){if(e.key==="ArrowDown"||e.key===" "){e.preventDefault();set(true);var a=m.querySelector("a");if(a)a.focus()}});dd.addEventListener("keydown",function(e){if(e.key==="Escape"&&dd.classList.contains("is-open")){set(false);t.focus()}});dd.addEventListener("focusout",function(e){if(!dd.contains(e.relatedTarget))set(false)})});var h=document.querySelector(".hdr"),y0=scrollY;if(h)addEventListener("scroll",function(){var y=scrollY,d=y-y0;if(Math.abs(d)<8)return;h.classList.toggle("is-up",d>0&&y>160&&!document.documentElement.classList.contains("menu-open"));y0=y},{passive:true})})();</script>'
ANIM_OPEN = '(function(){var run=function(){'
ANIM_CLOSE = '},go=function(){document.readyState==="loading"?document.addEventListener("DOMContentLoaded",run):run()};if(!(window.matchMedia&&matchMedia(__MQ__).matches)){go();return}var l=["gsap.min.js","ScrollTrigger.min.js","SplitText.min.js"],n=0;l.forEach(function(s){var e=document.createElement("script");e.src="/assets/js/"+s;e.async=false;e.onload=e.onerror=function(){if(++n===l.length)go()};document.head.appendChild(e)})})();'

def fr(text):
    text = text.replace("'", "’")
    return re.sub(r" ([;:?!»])", NB + r"\1", text).replace("« ", "«" + NB)


def esc(t):
    return html.escape(fr(t), quote=False)


# ——— Page d'accueil : navigation, héros, liens vers les pages ———
# La source de l'accueil est _build/home.src.html ; index.html est le fichier généré.
home = (ROOT / "_build" / "home.src.html").read_text(encoding="utf-8")

# Menu : le Blog est dans le pied de page
NAV = [("Comment ça marche", "#services"), ("Métiers", "/metiers/"), ("Google Ads", "/google-ads/"), ("Meta Ads", "/meta-ads/"),
       ("Qui sommes-nous", "/qui-sommes-nous/"), ("Questions", "/questions/"), ("Particuliers", "/devis-travaux/")]
# « Comment ça marche » ouvre une petite liste : l'accueil, le guide, les questions, puis la méthode sous un filet (comme « Métiers »)
NAV_SUB = {"#services": [("Accueil", "", "/"),
                         ("Comment trouver des chantiers", "", "/trouver-des-chantiers/"),
                         ("Questions fréquentes", "", "/questions/"),
                         ("Notre méthode", "", "#services")],
           # « Métiers » ouvre la liste des cinq métiers
           "/metiers/": [("Couverture et zinguerie", "", "/metiers/couverture/"),
                         ("Façade et ravalement", "", "/metiers/facade/"),
                         ("Menuiserie extérieure", "", "/metiers/menuiserie-exterieure/"),
                         ("Charpente", "", "/metiers/charpente/"),
                         ("Isolation", "", "/metiers/isolation/"),
                         ("Tous les métiers", "", "/metiers/")]}
NAV_CHEV = '<svg class="dd-chev" viewBox="0 0 10 6" aria-hidden="true"><path d="M1 1l4 4 4-4" fill="none" stroke="currentColor" stroke-width="1.4"/></svg>'
def _dd_link(st, sd, sh, parent):
    cls = ' class="is-all"' if sh == parent else ""
    return f'<a href="{sh}"{cls}><b>{st}</b>' + (f"<small>{sd}</small>" if sd else "") + "</a>"
def _nav_item(t, h):
    if h in NAV_SUB:
        sub = "".join(_dd_link(st, sd, sh, h) for st, sd, sh in NAV_SUB[h])
        return f'      <div class="hdr-dd"><a class="link hdr-dd-t" href="{h}" aria-expanded="false">{t}{NAV_CHEV}</a><div class="hdr-dd-menu">{sub}</div></div>'
    return f'      <a class="link" href="{h}">{t}</a>'
nav_html = "\n".join(_nav_item(t, h) for t, h in NAV)
def _menu_item(t, h):  # sur téléphone : « Comment ça marche » et « Métiers » s'ouvrent comme des listes
    if h in NAV_SUB:
        sub = "".join(_dd_link(st, sd, sh, h) for st, sd, sh in NAV_SUB[h])
        return f'    <details class="menu-dd"><summary>{t}{NAV_CHEV}</summary><div class="menu-dd-list">{sub}</div></details>'
    return f'    <a href="{h}">{t}</a>'
menu_html = "\n".join(_menu_item(t, h) for t, h in NAV) + '\n    <a href="#contact">Contact</a>'
home = re.sub(r'(<nav class="hdr-nav" aria-label="Menu">)[\s\S]*?(</nav>)', r"\1\n" + nav_html + r"\n    \2", home, count=1)
home = re.sub(r'(<div class="menu" id="menu">\s*<nav aria-label="Menu">)[\s\S]*?(</nav>)', r"\1\n" + menu_html + r"\n  \2", home, count=1)

# Héros : écrit dans _build/home.src.html. Le mot géant est décoratif (<p class="giant">), le titre principal est la phrase d'accroche (<h1 class="lead">).

# Métiers : chaque nom mène à sa page
SLUG = {"Couverture": "couverture", "Menuiserie": "menuiserie-exterieure", "Isolation": "isolation", "Charpente": "charpente", "Façade": "facade"}
for name, slug in SLUG.items():
    home = home.replace(f'<h3 class="sector-name">{name}</h3>', f'<h3 class="sector-name"><a href="/metiers/{slug}/">{name}</a></h3>', 1)
home = home.replace('<h3 class="sector-name">Autres</h3>', '<h3 class="sector-name"><a href="/metiers/">Autres</a></h3>', 1)

# Blog : liens vers les articles
for a in ARTICLES:
    pass
links = iter(f"/blog/{a['slug']}/" for a in ARTICLES)
home = re.sub(r'<a class="post-link" href="#journal">', lambda m: f'<a class="post-link" href="{next(links)}">', home)
home = home.replace('<a class="link" href="#journal">Tout lire</a>', '<a class="link" href="/blog/">Tout lire</a>', 1)

# Pied de page
FOOT = {
    '<a class="link" href="#about">À propos</a>': '<a class="link" href="/qui-sommes-nous/">Qui sommes-nous</a>',
    '<a class="link" href="#journal">Blog</a>': '<a class="link" href="/blog/">Blog</a>',
    '<a class="link" href="#services">Annonces Meta locales</a>': '<a class="link" href="/meta-ads/">Meta Ads</a>',
    '<a class="link" href="#services">Google Ads locales</a>': '<a class="link" href="/google-ads/">Google Ads</a>',
    '<a class="link" href="#services">Rendez-vous agenda</a>': '<a class="link" href="/metiers/">Métiers</a>',
}
for a, b in FOOT.items():
    home = home.replace(a, b, 1)

# Téléphone et WhatsApp de Martin
PHONE, PHONE_TXT, WA = "+33781018936", "07 81 01 89 36", "https://wa.me/33781018936"
home = home.replace('<a class="link" href="#">Numéro à venir</a>', f'<a class="link" href="tel:{PHONE}">{PHONE_TXT}</a>')
home = home.replace('<a class="hdr-login" href="#contact"><span>Nous appeler</span>', f'<a class="hdr-login" href="tel:{PHONE}"><span>Appeler Martin</span>')
home = home.replace('"telephone": "Numéro à venir"', f'"telephone": "{PHONE}"')

WA_CSS = """<style id="wa-css">
.wa{position:fixed;right:clamp(14px,2vw,24px);bottom:clamp(14px,2vw,24px);z-index:90;font-family:var(--f-text)}
.wa-fab{display:flex;align-items:center;gap:.65rem;padding:.55rem 1.1rem .55rem .55rem;border:0;border-radius:999px;background:var(--ink);color:var(--bg);font-size:.95rem;cursor:pointer;box-shadow:0 14px 34px -14px rgba(10,20,36,.55);transition:transform .3s var(--ease)}
.wa-fab:hover{transform:translateY(-2px)}
.wa-ico{display:grid;place-items:center;width:40px;height:40px;border-radius:50%;background:#25D366;flex:none}
.wa-ico svg{width:22px;height:22px;fill:#fff}
.wa-fab b{font-weight:500}
.wa-dot{width:8px;height:8px;border-radius:50%;background:#25D366;box-shadow:0 0 0 3px color-mix(in oklab,#25D366 30%,transparent)}
.wa-panel{position:absolute;right:0;bottom:calc(100% + 12px);width:min(360px,calc(100vw - 28px));background:var(--bg);color:var(--ink);border-radius:var(--r);box-shadow:0 30px 60px -20px rgba(10,20,36,.45);overflow:hidden;transform-origin:100% 100%;transform:translateY(8px) scale(.98);opacity:0;visibility:hidden;transition:opacity .25s var(--ease),transform .3s var(--ease),visibility 0s .3s}
.wa.is-open .wa-panel{opacity:1;visibility:visible;transform:none;transition:opacity .25s var(--ease),transform .3s var(--ease)}
.wa-head{display:flex;align-items:center;gap:.8rem;padding:1.1rem 1.2rem;background:var(--ink);color:var(--bg)}
.wa-av{display:grid;place-items:center;width:44px;height:44px;border-radius:50%;background:color-mix(in oklab,var(--bg) 14%,var(--ink));font:300 1.05rem/1 var(--f-display);flex:none;position:relative}
.wa-av::after{content:"";position:absolute;right:1px;bottom:1px;width:10px;height:10px;border-radius:50%;background:#25D366;border:2px solid var(--ink)}
.wa-head p{line-height:1.3}
.wa-head small{display:block;font-size:.8rem;color:color-mix(in oklab,var(--bg) 66%,var(--ink))}
.wa-x{margin-left:auto;width:36px;height:36px;border:0;background:transparent;color:var(--bg);font-size:1.4rem;cursor:pointer}
.wa-body{padding:1.1rem 1.2rem 1.2rem;display:flex;flex-direction:column;gap:.75rem}
.wa-bubble{padding:.8rem .95rem;background:var(--paper);border-radius:2px 12px 12px 12px;font-size:.95rem;line-height:1.45}
.wa-k{font-size:.78rem;color:var(--muted);margin-top:.2rem}
.wa-q{display:flex;align-items:center;justify-content:space-between;gap:.6rem;min-height:44px;padding:.6rem .9rem;border:1px solid color-mix(in oklab,var(--ink) 14%,transparent);border-radius:var(--r);color:var(--ink);text-decoration:none;font-size:.93rem;transition:border-color .2s,background .2s}
.wa-q:hover{border-color:var(--accent);background:var(--tint)}
.wa-q::after{content:"→";color:var(--accent)}
.wa-actions{display:grid;grid-template-columns:1fr 1fr;gap:.5rem;margin-top:.3rem}
.wa-btn{display:flex;align-items:center;justify-content:center;gap:.5rem;min-height:46px;border-radius:var(--r);font-size:.93rem;text-decoration:none}
.wa-btn.is-wa{background:#25D366;color:#0A1424;font-weight:500}
.wa-btn.is-call{background:var(--ink);color:var(--bg)}
.wa-btn svg{width:18px;height:18px;fill:currentColor}
.wa-foot{font-size:.78rem;color:var(--muted);text-align:center}
@media (max-width:760px){.wa{right:14px;bottom:14px}.wa-fab{padding:0;background:none}.wa-fab .wa-ico{box-shadow:0 10px 24px -8px rgba(10,20,36,.5)}.wa-fab b,.wa-fab .wa-dot{display:none}.wa-fab .wa-ico{width:50px;height:50px}
:root{--sp:64px}
.sheet::before,.ruled::before,.ftr::before{background:linear-gradient(var(--rule),var(--rule)) 0 0/1px 100% no-repeat,linear-gradient(var(--rule),var(--rule)) 100% 0/1px 100% no-repeat}
.ftr-base{flex-direction:column;align-items:flex-start;gap:.7rem}.ftr-base span:first-child{margin-right:0}
.pg-top{padding-top:calc(var(--hdr) + 32px)}.sector-name{transform:none!important}}
.wa-tip{position:absolute;right:0;bottom:calc(100% + 10px);display:none;align-items:flex-start;gap:4px;width:max-content;max-width:min(270px,calc(100vw - 28px));padding:4px 4px 4px 0;border-radius:14px 14px 4px 14px;background:var(--bg);color:var(--ink);box-shadow:0 14px 34px -12px rgba(10,20,36,.45),0 0 0 1px var(--rule);animation:waTip .45s cubic-bezier(.2,.8,.2,1)}
.wa.is-tip .wa-tip{display:flex}
.wa-tip-go{flex:1;padding:10px 4px 10px 14px;border:0;background:none;color:inherit;font:inherit;font-size:.9rem;line-height:1.35;text-align:left;cursor:pointer}
.wa-tip-go b{font-weight:600}
.wa-tip-x{width:30px;height:30px;border:0;background:none;color:var(--muted);font-size:1.2rem;cursor:pointer;flex:none}
@keyframes waTip{from{opacity:0;transform:translateY(8px) scale(.96)}}
@media (prefers-reduced-motion:reduce){.wa-panel,.wa-fab{transition:none}.wa-tip{animation:none}}
</style>
"""
WA_SVG = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2Zm0 18.2a8.2 8.2 0 0 1-4.2-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2Zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8-.2-.1-.4-.1-.6.1l-.8 1c-.1.2-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.2-.4.2-.4.7-1.3.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.1 5.1 0 0 0 1.1 2.7 11.6 11.6 0 0 0 4.5 3.9c1.7.7 2.3.8 3.2.7a2.7 2.7 0 0 0 1.8-1.3 2.2 2.2 0 0 0 .1-1.3c0-.1-.2-.2-.5-.3Z"/></svg>'
TEL_SVG = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2a1 1 0 0 1 1-.2 11.4 11.4 0 0 0 3.6.6 1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1 11.4 11.4 0 0 0 .6 3.6 1 1 0 0 1-.2 1Z"/></svg>'
import urllib.parse as _u
def wa(msg): return WA + "?text=" + _u.quote(msg)
QUESTIONS = [
    ("Mon secteur est-il encore libre ?", "Bonjour Martin, je suis artisan à [ville] ([métier]). Mon secteur est-il encore libre ?"),
    ("Comment se passent les rendez-vous ?", "Bonjour Martin, j'aimerais comprendre comment vous trouvez et vérifiez les rendez-vous."),
    ("Combien cela me coûterait-il ?", "Bonjour Martin, je voudrais connaître le prix pour mon entreprise ([métier], [ville])."),
]
qs = "\n".join(f'      <a class="wa-q" href="{html.escape(wa(m))}" target="_blank" rel="noopener" data-wa="question">{q.replace(" ?", "&nbsp;?")}</a>' for q, m in QUESTIONS)
WA_HTML = f"""<div class="wa" id="wa">
  <div class="wa-panel" id="wa-panel" role="dialog" aria-modal="false" aria-labelledby="wa-title">
    <div class="wa-head">
      <span class="wa-av" aria-hidden="true">MB</span>
      <p id="wa-title"><b>Martin Barthélémy</b><small>Cofondateur</small></p>
      <button class="wa-x" type="button" aria-label="Fermer" data-wa-close>×</button>
    </div>
    <div class="wa-body">
      <p class="wa-bubble">Bonjour. Une question sur votre secteur ou sur notre méthode&nbsp;? Écrivez-moi, je vous réponds personnellement.</p>
      <p class="wa-k">Choisissez une question, ou écrivez la vôtre&nbsp;:</p>
{qs}
      <div class="wa-actions">
        <a class="wa-btn is-wa" href="{WA}" target="_blank" rel="noopener" data-wa="chat">{WA_SVG}WhatsApp</a>
        <a class="wa-btn is-call" href="tel:{PHONE}" data-wa="call">{TEL_SVG}Appeler</a>
      </div>
      <p class="wa-foot">Lundi au vendredi, 8 h à 19 h · {PHONE_TXT}</p>
    </div>
  </div>
  <div class="wa-tip" role="status"><button class="wa-tip-go" type="button"><b>Une question&nbsp;?</b> Martin vous répond sur WhatsApp.</button><button class="wa-tip-x" type="button" aria-label="Fermer">×</button></div>
  <button class="wa-fab" type="button" aria-expanded="false" aria-controls="wa-panel" aria-label="Écrire à Martin sur WhatsApp ou l’appeler"><span class="wa-ico">{WA_SVG}</span><span class="wa-dot" aria-hidden="true"></span><b>Parler à Martin<span>, cofondateur</span></b></button>
</div>
<script>
(function(){{var w=document.getElementById('wa');if(!w)return;var b=w.querySelector('.wa-fab');
function set(o){{w.classList.remove('is-tip');w.classList.toggle('is-open',o);b.setAttribute('aria-expanded',String(o));}}
b.addEventListener('click',function(){{var o=!w.classList.contains('is-open');set(o);if(o){{var pn=w.querySelector('.wa-panel');pn.setAttribute('tabindex','-1');pn.focus({{preventScroll:true}})}}}});
w.querySelector('.wa-tip-go').addEventListener('click',function(){{set(true)}});
w.querySelector('.wa-tip-x').addEventListener('click',function(){{w.classList.remove('is-tip')}});
w.querySelector('[data-wa-close]').addEventListener('click',function(){{set(false);b.focus()}});
document.addEventListener('keydown',function(e){{if(e.key==='Escape'&&w.classList.contains('is-open')){{set(false);b.focus()}}}});
document.addEventListener('click',function(e){{if(!w.contains(e.target))set(false)}});
w.querySelectorAll('[data-wa]').forEach(function(a){{a.addEventListener('click',function(){{(window.dataLayer=window.dataLayer||[]).push({{event:'contact_martin',canal:a.dataset.wa}})}})}});
}})();
</script>
"""
home = re.sub(r'<style id="wa-css">[\s\S]*?</style>\n', "", home)
home = re.sub(r'<div class="wa" id="wa">[\s\S]*?</script>\n', "", home)
home = home.replace("</head>", WA_CSS + "</head>", 1)
home = home.replace("</body>", WA_HTML + "</body>", 1)

LD_HEAD = """<style id="ld-css">
.ld{position:fixed;inset:0;z-index:200;display:flex;flex-direction:column;justify-content:space-between;padding:clamp(20px,3vw,40px);background:#0A1424;color:#fff;transition:transform .7s cubic-bezier(.7,0,.2,1)}
.ld.is-out{transform:translateY(-100%)}
.ld-skip .ld{display:none}
.ld-logo{width:min(46vw,220px);aspect-ratio:6314 / 918;background:currentColor;-webkit-mask:url(/assets/logo-bartier-wordmark.svg) left center / contain no-repeat;mask:url(/assets/logo-bartier-wordmark.svg) left center / contain no-repeat}
.ld-row{display:flex;align-items:flex-end;justify-content:space-between;gap:20px}
.ld-row p{max-width:22ch;color:rgba(255,255,255,.6);font:400 .9rem/1.4 var(--f-text)}
.ld-n{font:300 clamp(4.5rem,14vw,11rem)/.8 var(--f-display);letter-spacing:-.05em;font-variant-numeric:tabular-nums}
.ld-bar{position:absolute;left:0;bottom:0;height:3px;width:100%;background:#2D5BE3;transform:scaleX(0);transform-origin:0 50%}
html.ld-on{overflow:hidden}
</style>
<script>try{if(sessionStorage.getItem('bc-ld'))document.documentElement.classList.add('ld-skip');else document.documentElement.classList.add('ld-on')}catch(e){}</script>
"""
LD_BODY = """<div class="ld" id="ld" aria-hidden="true"><span class="ld-logo"></span><div class="ld-row"><p>Des clients pour les artisans du bâtiment</p><span class="ld-n"><span id="ld-n">0</span>%</span></div><i class="ld-bar" id="ld-bar"></i></div>
<script>(function(){var l=document.getElementById('ld'),h=document.documentElement;if(!l||h.classList.contains('ld-skip')){if(l)l.remove();return}
var n=document.getElementById('ld-n'),b=document.getElementById('ld-bar'),t0=performance.now(),D=matchMedia('(prefers-reduced-motion: reduce)').matches?200:(innerWidth<761?900:1300);
function f(t){var k=Math.max(0,Math.min(1,(t-t0)/D)),e=1-Math.pow(1-k,3);n.textContent=Math.round(e*100);b.style.transform='scaleX('+e+')';if(k<1)requestAnimationFrame(f);else done()}
function done(){try{sessionStorage.setItem('bc-ld','1')}catch(e){}setTimeout(function(){l.classList.add('is-out');h.classList.remove('ld-on');setTimeout(function(){l.remove()},800)},180)}
requestAnimationFrame(f);setTimeout(function(){if(document.body.contains(l)){l.remove();h.classList.remove('ld-on')}},4000)})();</script>
"""
home = re.sub(r'<style id="ld-css">[\s\S]*?</script>\n', "", home)
home = re.sub(r'<div class="ld" id="ld"[\s\S]*?</script>\n', "", home)
# Écran de chargement : remis le 19/11/2026 à la demande de Charles (il avait été retiré le 18/11). Une fois par visite.
home = home.replace("</head>", LD_HEAD + "</head>", 1)
home = re.sub(r"(<body[^>]*>\n?)", lambda m: m.group(1) + LD_BODY, home, count=1)

# Données structurées, adresse canonique et balises de partage de l'accueil (toujours régénérées)
FOUNDERS = [("charles", "Charles Le Cottier", "Cofondateur"), ("martin", "Martin Barthélémy", "Cofondateur")]
PORTRAIT = {"charles": "charles-le-cottier", "martin": "martin-barthelemy"}
def portrait(k):
    return SITE + f"/assets/photos/{PORTRAIT[k]}-700x875-nb.webp"
ORG_REF = {"@type": "Organization", "@id": SITE + "/#org", "name": "Bartier & Co", "url": SITE + "/"}
WEBSITE = {"@type": "WebSite", "@id": SITE + "/#website", "url": SITE + "/", "name": "Bartier & Co", "inLanguage": "fr-FR", "publisher": {"@id": SITE + "/#org"}}
ORG = {"@type": "Organization", "@id": SITE + "/#org", "name": "Bartier & Co", "legalName": "Bartier & Co SAS", "alternateName": "Bartier and Co",
       "slogan": "Faire équipe. Faire la différence.", "url": SITE + "/", "logo": SITE + "/assets/logo-bartier.png", "image": SITE + "/assets/og.png",
       "email": "contact@bartierandco.com", "telephone": PHONE,
       "address": {"@type": "PostalAddress", "addressCountry": "FR"},
       "contactPoint": {"@type": "ContactPoint", "telephone": PHONE, "email": "contact@bartierandco.com", "contactType": "customer service", "areaServed": "FR", "availableLanguage": "French",
                        "hoursAvailable": {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], "opens": "08:00", "closes": "19:00"}},
       "areaServed": {"@type": "Country", "name": "France"},
       "knowsAbout": ["Google Ads", "Meta Ads", "Publicité locale", "Couverture", "Ravalement de façade", "Menuiserie extérieure", "Charpente", "Isolation"],
       "sameAs": ["https://www.facebook.com/profile.php?id=61596597124434", "https://www.linkedin.com/company/bartier-co"],
       "description": "Agence qui trouve des clients aux artisans du bâtiment : annonces locales, rappel des demandes en moins de 5 minutes, visites de devis fixées directement dans leur agenda. Pour les propriétaires, mise en relation gratuite avec un artisan de leur secteur.",
       "makesOffer": [{"@type": "Offer", "itemOffered": {"@id": SITE + u + "#service"}} for u in ("/devis-travaux/", "/google-ads/", "/meta-ads/")],
       "founder": [{"@type": "Person", "@id": f"{SITE}/qui-sommes-nous/#{k}", "name": n, "jobTitle": j, "image": portrait(k)} for k, n, j in FOUNDERS]}
ORG_PAGE = {k: ORG[k] for k in ("@type", "@id", "name", "legalName", "url", "logo", "email", "telephone", "address", "description", "sameAs", "areaServed")}
home = re.sub(r'<link rel="canonical"[^>]*>\n?', "", home)
home = re.sub(r'<script type="application/ld\+json">[\s\S]*?</script>\n?', "", home)
home = re.sub(r'<meta (?:property="og:|name="twitter:)[^>]*>\n?', "", home)
# (en ligne, la balise robots de l'accueil est remplacée par la passe finale, comme partout : extraits longs autorisés)
_ht = html.unescape(re.search(r"<title>(.*?)</title>", home).group(1))
_hd = html.unescape(re.search(r'<meta name="description" content="([^"]*)"', home).group(1))
_ld = {"@context": "https://schema.org", "@graph": [ORG, {"@type": "WebSite", "@id": SITE + "/#website", "url": SITE + "/", "name": "Bartier & Co", "inLanguage": "fr-FR", "publisher": {"@id": SITE + "/#org"}}]}
# Questions-réponses visibles de l'accueil, reprises telles quelles
_txt = lambda s: re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", "", s))).replace("'", "’").strip()
_qa = re.findall(r'<details class="fq"><summary><span>(.*?)</span>.*?<div class="fq-a">(.*?)</div>\s*</details>', home, flags=re.S)
# Les questions de l'accueil sont aussi sur /questions/ : le balisage FAQPage n'y figure qu'une fois, sur cette page-là.
_m = re.search(r'<meta name="description" content="[^"]*">\n?', home)
home = home[:_m.end()] + (
    f'<link rel="canonical" href="{SITE}/">\n'
    f'<meta property="og:type" content="website">\n<meta property="og:locale" content="fr_FR">\n<meta property="og:site_name" content="Bartier &amp; Co">\n'
    f'<meta property="og:title" content="{html.escape(_ht)}">\n<meta property="og:description" content="{html.escape(_hd)}">\n'
    f'<meta property="og:url" content="{SITE}/">\n<meta property="og:image" content="{SITE}/assets/og.png">\n<meta property="og:image:width" content="1200">\n<meta property="og:image:height" content="630">\n'
    f'<meta property="og:image:alt" content="Logo Bartier &amp; Co et slogan : Faire équipe. Faire la différence.">\n<meta name="twitter:card" content="summary_large_image">\n') + home[_m.end():]
home = home.replace("</head>", f'<script type="application/ld+json">{json.dumps(_ld, ensure_ascii=False, separators=(",", ":"))}</script>\n</head>', 1)
(ROOT / "index.html").write_text(home, encoding="utf-8")

# Feuille complémentaire (_build/extra.css), injectée dans toutes les pages
def mincss(c):
    c = re.sub(r"/\*[\s\S]*?\*/", "", c)
    c = re.sub(r"\s+", " ", c)
    return re.sub(r"\s*([{};,>])\s*", r"\1", c).replace(";}", "}").strip()
XCSS = mincss((ROOT / "_build" / "extra.css").read_text(encoding="utf-8"))
home = re.sub(r'<style id="bc-css">[\s\S]*?</style>\n', "", home)
home = home.replace("</head>", f'<style id="bc-css">{XCSS}</style>\n</head>', 1)
(ROOT / "index.html").write_text(home, encoding="utf-8")

# ——— Cookies : gestionnaire de consentement (assets/js/consent.js), textes dans _build/legal/notices.json s'il existe ———
# Identifiants des balises : laisser vide tant qu'ils n'existent pas. Rien n'est chargé sans identifiant ET sans accord.
TAGS = {"ga4": "", "gads": "", "meta": ""}
CC_TEXTS = {
    "banner_title": "Cookies : à vous de choisir",
    "banner_text": "Avec votre accord, nous mesurons l'audience du site et l'efficacité de nos publicités (Google, Meta). Sans accord, rien n'est déposé. <a href=\"/cookies/\">En savoir plus</a>",
    "banner_accept": "Tout accepter", "banner_refuse": "Tout refuser", "banner_customize": "Personnaliser mes choix",
    "prefs_title": "Vos choix de cookies",
    "prefs_intro": "Choisissez ce que vous acceptez. Le site fonctionne dans tous les cas.",
    "prefs_always": "Toujours actifs",
    "prefs_necessary_title": "Nécessaires", "prefs_necessary_text": "Ils retiennent votre choix et l'affichage du site. Aucun suivi.",
    "prefs_audience_title": "Mesure d'audience", "prefs_audience_text": "Google Analytics : pages vues et parcours, pour améliorer le site.",
    "prefs_ads_title": "Publicité", "prefs_ads_text": "Google Ads et Meta : savoir quelles annonces amènent des demandes.",
    "prefs_save": "Enregistrer mes choix",
}
_notices = ROOT / "_build" / "legal" / "notices.json"
NOTICES = json.loads(_notices.read_text(encoding="utf-8")) if _notices.exists() else {}
CC_TEXTS.update({k: v for k, v in NOTICES.items() if k in CC_TEXTS and isinstance(v, str) and v.strip()})
LEGAL_SLUGS = ["mentions-legales", "confidentialite", "cookies", "conditions-du-service"]
LEGAL_READY = [s for s in LEGAL_SLUGS if (ROOT / "_build" / "legal" / f"{s}.html").exists()]
if "cookies" not in LEGAL_READY:
    CC_TEXTS["banner_text"] = re.sub(r"\s*<a [^>]*>[^<]*</a>", "", CC_TEXTS["banner_text"])
_cc = (ROOT / "_build" / "consent.src.js").read_text(encoding="utf-8")
_cc = re.sub(r"^/\*[\s\S]*?\*/\n", "", _cc)
_cc = _cc.replace("__TEXTS__", json.dumps({k: fr(v) for k, v in CC_TEXTS.items()}, ensure_ascii=False)).replace("__TAGS__", json.dumps(TAGS))
_cc = "\n".join(l.strip() for l in _cc.splitlines() if l.strip())
(ROOT / "assets" / "js" / "consent.js").write_text(_cc, encoding="utf-8")
if NOTICES.get("artisan_form_notice") and "confidentialite" in LEGAL_READY:
    home = re.sub(r'<p class="dq-legal">.*?</p>', lambda m: f'<p class="dq-legal">{fr(NOTICES["artisan_form_notice"])}</p>', home, count=1, flags=re.S)
import hashlib
CC_TAG = f'<script src="/assets/js/consent.js?v={hashlib.sha1(_cc.encode()).hexdigest()[:8]}" defer></script>'
home = re.sub(r'<script src="/assets/js/consent\.js[^"]*" defer></script>\n?', "", home)
home = home.replace("</body>", CC_TAG + "\n</body>", 1)
(ROOT / "index.html").write_text(home, encoding="utf-8")

# ——— Gabarit des pages intérieures ———
HEAD = home[:home.index("</head>")]
HEAD = re.sub(r'<link rel="canonical"[^>]*>\n?', "", HEAD)
HEAD = re.sub(r'<script type="application/ld\+json">[\s\S]*?</script>\n?', "", HEAD)
HEAD = re.sub(r'<meta (?:property="og:|name="twitter:)[^>]*>\n?', "", HEAD)
BODY_OPEN = home[home.index("</head>"):home.index("<main>") + len("<main>")]
CONTACT = home[home.rindex('<section', 0, home.index('id="contact"')):]
CONTACT = CONTACT[:CONTACT.index("</section>") + len("</section>")]
TAIL = home[home.index("</main>"):]
_eq = (ROOT / "_build" / "equipe.html").read_text(encoding="utf-8")  # section équipe : sur Qui sommes-nous seulement
TEAM = _eq[_eq.index('<section class="team sheet"'):]
TEAM = TEAM[:TEAM.index("</section>") + len("</section>")]
# catalogue des photos : celles de l'accueil et celles des sections déplacées sur la page Métiers
IMGS = {html.unescape(a): u for u, a in re.findall(r'<img [^>]*?src="([^"]+)" alt="([^"]+)"', home + (ROOT / "_build" / "metiers_blocs.html").read_text(encoding="utf-8") + (ROOT / "_build" / "photos_catalogue.html").read_text(encoding="utf-8") + (ROOT / "_build" / "accueil_retire.html").read_text(encoding="utf-8") + _eq)}


def img(alt_start):
    for alt, url in IMGS.items():
        if alt.startswith(alt_start):
            return url, alt
    raise KeyError(alt_start)


def absolutize(block):
    block = block.replace('href="#hero"', 'href="/"')
    return re.sub(r'href="#(?!contact\b|menu\b|contenu\b)([\w-]+)"', r'href="/#\1"', block)


EXTRA_CSS = """<style>
/* Pages intérieures */
.pg-photo.mk{position:relative;display:grid;place-items:center;aspect-ratio:auto;height:auto;min-height:440px;padding:clamp(20px,3vw,40px);background:var(--paper);border-radius:var(--r);overflow:hidden}
.mk::before{content:"";position:absolute;inset:0;background:radial-gradient(60% 60% at 70% 20%,color-mix(in oklab,var(--accent) 16%,transparent),transparent 70%)}
.mk-tag{position:absolute;top:14px;right:14px;padding:.3em .6em;font-size:.72rem;background:var(--bg);color:var(--muted);border-radius:var(--r)}
.mk-g{position:relative;width:min(100%,460px);background:var(--bg);border-radius:12px;padding:18px;box-shadow:0 24px 50px -24px rgba(10,20,36,.35);font-family:Arial,Helvetica,sans-serif}
.mk-search{display:flex;align-items:center;gap:.6rem;height:44px;padding:0 14px;border:1px solid #dfe1e5;border-radius:22px;color:#5f6368;font-size:.95rem;margin-bottom:16px}
.mk-search svg{width:18px;height:18px;flex:none}
.mk-search span{color:#202124}
.mk-search i{margin-left:-2px;width:1px;height:18px;background:#202124;animation:blink 1s steps(1) infinite}
@keyframes blink{50%{opacity:0}}
.mk-res{padding:12px 4px;border-top:1px solid #f1f3f4}
.mk-res.is-ad{border-top:0;border-radius:8px;padding:12px;background:color-mix(in oklab,var(--accent) 5%,#fff);box-shadow:inset 0 0 0 1px color-mix(in oklab,var(--accent) 25%,transparent)}
.mk-spon{font-size:.72rem;font-weight:700;color:#202124;margin-bottom:6px}
.mk-site{display:flex;align-items:center;gap:.55rem;font-size:.8rem;color:#202124}
.mk-site small{display:block;color:#4d5156;font-size:.75rem}
.mk-fav{display:grid;place-items:center;width:28px;height:28px;border-radius:50%;background:var(--ink);color:#fff;font-size:.7rem;font-weight:700;flex:none}
.mk-title{margin:6px 0 4px;font-size:1.12rem;line-height:1.3;color:#1a0dab}
.mk-desc{font-size:.84rem;line-height:1.45;color:#4d5156}
.mk-links{display:flex;flex-wrap:wrap;gap:6px;margin-top:10px}
.mk-links span{padding:.35em .7em;border:1px solid #dadce0;border-radius:16px;font-size:.75rem;color:#1a0dab;background:#fff}
.mk-call{display:inline-flex;align-items:center;gap:.4rem;margin-top:10px;padding:.45em .85em;border-radius:16px;background:var(--accent);color:#fff;font-size:.8rem}
.mk-res.is-ghost i{display:block;height:9px;margin:7px 0;border-radius:5px;background:#eef0f3}
.mk-res.is-ghost i:first-child{width:45%}.mk-res.is-ghost i:nth-child(2){width:85%}.mk-res.is-ghost i:nth-child(3){width:70%}
.mk-phone{position:relative;width:min(100%,300px);padding:14px 10px 18px;background:#0A1424;border-radius:36px;box-shadow:0 30px 60px -24px rgba(10,20,36,.55)}
.mk-notch{width:90px;height:18px;margin:0 auto 10px;border-radius:12px;background:#000}
.mk-post{background:#fff;border-radius:22px;overflow:hidden;font-family:Arial,Helvetica,sans-serif;color:#050505}
.mk-post .mk-site{padding:12px 12px 0}
.mk-post .mk-site small{color:#65676b}
.mk-text{padding:8px 12px 10px;font-size:.82rem;line-height:1.4}
.mk-img{aspect-ratio:4/3;background:#e4e6eb}
.pg-photo .mk-img img{width:100%;height:100%;object-fit:cover;filter:none}
.mk-cta{display:flex;align-items:center;justify-content:space-between;gap:8px;padding:10px 12px;background:#f0f2f5}
.mk-cta small{display:block;color:#65676b;font-size:.72rem;text-transform:uppercase}
.mk-cta b{font-size:.8rem}.mk-cta > span{min-width:0}.mk-cta small{white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.mk-cta em{font-style:normal;flex:none;padding:.5em .8em;border-radius:6px;background:#e4e6eb;font-size:.76rem;font-weight:700}
.mk-react{display:flex;justify-content:space-between;padding:9px 12px;font-size:.72rem;color:#65676b}
@media (max-width:760px){.pg-photo.mk{min-height:0;padding:28px 16px;order:0}.mk-g{padding:14px}.mk-title{font-size:1rem}}
@media (prefers-reduced-motion:reduce){.mk-search i{animation:none}}

.pg-top{padding-top:calc(var(--hdr) + clamp(48px,7vw,104px))}
.pg-grid{row-gap:40px;align-items:end}
.pg-text{grid-column:1 / 3;display:flex;flex-direction:column;gap:1.4rem}
.pg-text h1{font:300 clamp(2.6rem,5.2vw,5rem)/1.02 var(--f-display);letter-spacing:-.045em;text-wrap:balance}
.pg-text .lead{font-size:clamp(1.05rem,1.3vw,1.2rem);line-height:1.5;max-width:36ch}
.pg-text .actions{display:flex;flex-wrap:wrap;align-items:center;gap:1rem 1.6rem}
.pg-photo{grid-column:3 / 5;aspect-ratio:4 / 3}
.crumbs{display:flex;flex-wrap:wrap;gap:.5rem;font-size:.85rem;color:var(--soft)}
.crumbs a{color:inherit}
.kick{font-size:.88rem;color:var(--accent)}
[data-tone="dark"] .kick,[data-tone="accent"] .kick{color:var(--soft)}
.sp-head{row-gap:24px;margin-bottom:var(--gap-head)}
.sp-head h2{grid-column:1 / 3}
.sp-head p{grid-column:3 / 5;align-self:end;max-width:44ch}
.sp-cols{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));border-top:1px solid var(--rule)}
.sp-cols > li{padding:clamp(18px,2vw,28px) var(--cell);display:flex;flex-direction:column;gap:.7rem}
.sp-cols > li + li{border-left:1px solid var(--rule)}
.sp-n{font:300 2.2rem/1 var(--f-display);color:var(--accent);letter-spacing:-.04em}
[data-tone="dark"] .sp-n{color:var(--soft)}
.sp-cols h3{font:300 clamp(1.35rem,1.8vw,1.7rem)/1.15 var(--f-display);letter-spacing:-.03em}
.sp-cols p{font-size:.95rem;color:var(--soft);max-width:40ch}
.sp-split{row-gap:var(--gap-head);align-items:start}
.sp-split > div:first-child{grid-column:1 / 3;display:flex;flex-direction:column;gap:24px}
.sp-split > div:first-child p{max-width:38ch;color:var(--soft)}
.sp-split > .sp-list,.sp-split > .prose,.sp-split > .sp-two{grid-column:3 / 5}
.sp-list{border-top:1px solid var(--rule)}
.sp-list li{display:grid;grid-template-columns:1.6em minmax(0,1fr);gap:.6rem;padding:1rem 0;border-bottom:1px solid var(--rule);font-size:1rem}
.sp-list li::before{content:"";width:.75em;height:.42em;margin-top:.45em;border-left:1.5px solid var(--accent);border-bottom:1.5px solid var(--accent);transform:rotate(-45deg)}
.sp-list.is-no li{color:var(--soft);text-decoration:line-through;text-decoration-color:color-mix(in oklab,currentColor 45%,transparent)}
.sp-list.is-no li::before{content:"×";width:auto;height:auto;margin:0;border:0;transform:none;color:var(--soft)}
[data-tone="dark"] .sp-list li::before{border-color:var(--bg)}
.sp-list.is-num{counter-reset:q}
.sp-list.is-num li{counter-increment:q;grid-template-columns:2.4em minmax(0,1fr)}
.sp-list.is-num li::before{content:counter(q,decimal-leading-zero);width:auto;height:auto;margin:0;border:0;transform:none;font:300 1.1rem/1.4 var(--f-display);color:var(--soft)}
.sp-table{border-top:1px solid var(--rule)}
.sp-row{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));border-bottom:1px solid var(--rule)}
.sp-row > *{padding:1rem var(--cell);font-size:.95rem}
.sp-row > :first-child{font-weight:500}
.sp-row.is-head > *{font:300 1.3rem/1.2 var(--f-display);letter-spacing:-.02em}
.sp-row > :last-child{background:var(--tint)}
.ad-card{display:flex;flex-direction:column;gap:.8rem;padding:var(--cell);background:var(--bg);border-radius:var(--r);height:100%}
.ad-meta{font-size:.82rem;color:var(--soft)}
.ad-angle{font-size:.82rem;color:var(--accent);text-transform:uppercase;letter-spacing:.06em}
.ad-text{font-size:1rem;flex:1}
.ad-cta{align-self:flex-start;padding:.55em .8em;background:var(--paper);font-size:.85rem}
.sp-cols.is-cards{border:0;gap:12px}
.sp-cols.is-cards > li{padding:0;border:0}
.prose{font-size:1.06rem;line-height:1.7;max-width:68ch}
.prose > * + *{margin-top:1.1em}
.prose h2{font:300 clamp(1.6rem,2.4vw,2.2rem)/1.15 var(--f-display);letter-spacing:-.03em;margin-top:1.8em}
.prose ul,.prose ol{padding-left:1.2em}
.prose ul{list-style:disc}.prose ol{list-style:decimal}
.prose li + li{margin-top:.4em}
.prose a{color:var(--accent);text-decoration:underline;text-underline-offset:3px}
.prose table{width:100%;border-collapse:collapse;font-size:.95rem;display:block;overflow-x:auto}
.prose th,.prose td{text-align:left;padding:.8rem;border-bottom:1px solid var(--rule);vertical-align:top;min-width:110px}
.prose th{font-weight:500;background:var(--paper)}
.prose blockquote{padding:1rem 1.2rem;background:var(--paper);border-left:2px solid var(--accent);font-size:.98rem}
.prose .answer{padding:1.1rem 1.3rem;background:var(--tint);font-size:1.08rem}
.art-grid{row-gap:40px;align-items:start}
.art-grid .prose{grid-column:1 / 4}
.art-aside{grid-column:4;position:sticky;top:calc(var(--hdr) + 32px);display:flex;flex-direction:column;gap:1rem;padding:var(--cell);background:var(--paper)}
.art-aside h3{font:300 1.4rem/1.2 var(--f-display);letter-spacing:-.02em}
.art-aside p{font-size:.9rem;color:var(--soft)}
.post-meta-line{display:flex;flex-wrap:wrap;gap:.4rem 1.2rem;font-size:.9rem;color:var(--soft)}
.sector-name a{color:inherit;text-decoration:none;display:inline-flex;align-items:baseline;gap:.25em;transition:color .3s var(--ease)}
.sector-name a::after{content:"→";font-size:.4em;opacity:0;transform:translateX(-.4em);transition:opacity .3s var(--ease),transform .3s var(--ease)}
.sector-name a:hover{color:var(--accent)}
.sector-name a:hover::after{opacity:1;transform:none}
@media (hover:none){.sector-name a::after{opacity:.6;transform:none}}
@media (max-width:1024px){.art-grid .prose,.art-aside{grid-column:1 / -1}.art-aside{position:static}}
@media (max-width:760px){
  .pg-text,.pg-photo,.sp-head h2,.sp-head p,.sp-split > div:first-child,.sp-split > .sp-list,.sp-split > .prose,.sp-split > .sp-two{grid-column:1 / -1}
  .pg-photo{order:-1}
  .sp-cols{grid-template-columns:minmax(0,1fr)}
  .sp-cols > li + li{border-left:0;border-top:1px solid var(--rule)}
  .sp-cols.is-cards > li + li{border-top:0}
  .sp-row{grid-template-columns:minmax(0,1fr) minmax(0,1fr)}
  .sp-row > :first-child{grid-column:1 / -1;padding-bottom:0}
  .sp-row.is-head > :first-child{display:none}
  .prose{font-size:1rem}
}
</style>
"""


OG = {}  # images d'aperçu par page (assets/og/<clé>.png), rendues en fin de construction
OG_SKIP = {"/", "/mentions-legales/", "/confidentialite/", "/cookies/", "/conditions-du-service/"}


def og_key(path):
    return path.strip("/").replace("/", "-")


def head(title, desc, path, schema=None):
    h = re.sub(r"<title>[^<]*</title>", f"<title>{html.escape(fr(title), quote=False)}</title>", HEAD, count=1)
    h = re.sub(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{html.escape(fr(desc))}">', h, count=1)
    ld = f'<script type="application/ld+json">{json.dumps(schema, ensure_ascii=False, separators=(",", ":"))}</script>\n' if schema else ""
    if path in OG_SKIP:
        og_img, og_alt = f"{SITE}/assets/og.png", "Logo Bartier &amp; Co et slogan : Faire équipe. Faire la différence."
    else:
        OG[path] = re.sub(r"\s*[|–-]\s*Bartier & Co$", "", title).strip()
        og_img, og_alt = f"{SITE}/assets/og/{og_key(path)}.png", html.escape(fr(OG[path]))
    og = (f'<meta property="og:type" content="website">\n<meta property="og:locale" content="fr_FR">\n<meta property="og:site_name" content="Bartier &amp; Co">\n'
          f'<meta property="og:title" content="{html.escape(fr(title))}">\n<meta property="og:description" content="{html.escape(fr(desc))}">\n'
          f'<meta property="og:url" content="{SITE}{path}">\n<meta property="og:image" content="{og_img}">\n<meta property="og:image:width" content="1200">\n<meta property="og:image:height" content="630">\n'
          f'<meta property="og:image:alt" content="{og_alt}">\n<meta name="twitter:card" content="summary_large_image">\n')
    if schema and "@graph" in schema:  # l'organisation et le site sont décrits sur chaque page : les références #org et #website se résolvent partout
        schema = dict(schema, **{"@graph": [dict(n) for n in schema["@graph"]]})  # copie : des nœuds sont partagés entre pages
        for n in schema["@graph"]:
            if n.get("@type") == "Service" and "@id" not in n:
                n["@id"] = SITE + path + "#service"
                break
        have = {n.get("@id") for n in schema["@graph"] if n.get("@type") in ("Organization", "WebSite")}
        if SITE + "/#org" not in have:
            schema["@graph"].append(ORG_PAGE)
        if SITE + "/#website" not in have:
            schema["@graph"].append(WEBSITE)
        ld = f'<script type="application/ld+json">{json.dumps(schema, ensure_ascii=False, separators=(",", ":"))}</script>\n'
    m = re.search(r'<meta name="description" content="[^"]*">\n?', h)
    top_tags = f'<link rel="canonical" href="{SITE}{path}">\n' + og
    return h[:m.end()] + top_tags + h[m.end():] + ld + EXTRA_CSS


def with_form(body, contact, after=2):
    """Le formulaire vient après les deux premières sections : le bouton « Vérifier mon secteur » ne fait plus traverser toute la page."""
    ends = [m.end() for m in re.finditer(r"</section>", body)]
    if len(ends) <= after:
        return body + "\n\n" + contact
    i = ends[after - 1]
    return body[:i] + "\n\n" + contact + body[i:]


def write(path, title, desc, body, nav=None, schema=None, metier=None, form_after=2, form_h2=None):
    top = absolutize(BODY_OPEN).replace('aria-label="Bartier &amp; Co, retour en haut"', 'aria-label="Bartier &amp; Co, accueil"')  # pages intérieures : le logo ramène à l'accueil
    if nav:
        top = top.replace(f'class="link" href="{nav}"', f'class="link" href="{nav}" aria-current="page"', 1)
    contact = CONTACT.replace(f'name="metier" value="{metier}"', f'name="metier" value="{metier}" checked', 1) if metier else CONTACT
    if form_h2:  # pages métiers : un titre de formulaire plus clair que celui de l'accueil
        contact = re.sub(r"<h2 data-split>[^<]*</h2>", f"<h2 data-split>{form_h2}</h2>", contact, count=1)
    doc = head(title, desc, path, schema) + top + "\n" + with_form(fr(body), contact, form_after) + "\n" + absolutize(TAIL)
    out = ROOT / path.strip("/") / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(doc, encoding="utf-8")
    return path


def write_plain(path, title, desc, body, schema=None):
    """Page sans formulaire artisan : les liens #contact renvoient à l'accueil."""
    fix = lambda s: s.replace('href="#contact"', 'href="/#contact"')
    doc = head(title, desc, path, schema) + fix(absolutize(BODY_OPEN)) + "\n" + fr(body) + "\n" + fix(absolutize(TAIL))
    out = ROOT / path.strip("/") / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(doc, encoding="utf-8")
    return path


def crumbs(*items):
    parts = ['<a href="/">Accueil</a>'] + [f'<a href="{h}">{t}</a>' for t, h in items[:-1]] + [f'<span aria-current="page">{items[-1][0]}</span>']
    return '<nav class="crumbs" aria-label="Fil d\'Ariane">' + '<span aria-hidden="true">/</span>'.join(parts) + "</nav>"


def bc_ld(*items):
    el = [{"@type": "ListItem", "position": 1, "name": "Accueil", "item": SITE + "/"}]
    el += [{"@type": "ListItem", "position": i, "name": fr(n), "item": SITE + h} for i, (n, h) in enumerate(items, 2)]
    return {"@type": "BreadcrumbList", "itemListElement": el}


def faq_ld(items):
    clean = lambda t: re.sub("<[^>]+>", "", fr(t))
    return {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": clean(q), "acceptedAnswer": {"@type": "Answer", "text": clean(a)}} for q, a in items]}


def label_tables(frag):
    """Chaque cellule porte le titre de sa colonne : sur téléphone, le tableau devient une liste de fiches."""
    def table(m):
        heads = [re.sub(r"<[^>]+>", "", h) for h in re.findall(r"<th>(.*?)</th>", m.group(0), flags=re.S)]
        def row(r):
            cells = iter(heads)
            out = re.sub(r"<td>", lambda c: f'<td data-label="{html.escape(next(cells, ""))}">', r.group(0))
            if heads and heads[0] == "":  # la première colonne donne le titre de la ligne : en-tête de ligne
                out = re.sub(r'<td data-label="">(.*?)</td>', r'<th scope="row">\1</th>', out, count=1, flags=re.S)
            return out
        t = re.sub(r"<tr>(?:(?!</tr>).)*</tr>", row, m.group(0), flags=re.S)
        return re.sub(r"<thead>(.*?)</thead>", lambda h: "<thead>" + h.group(1).replace("<th>", '<th scope="col">') + "</thead>", t, flags=re.S)
    return re.sub(r"<table>.*?</table>", table, frag, flags=re.S)


MAJ_HTML = '<p class="pg-upd">Mis à jour le <time datetime="@@MAJ@@">@@MAJFR@@</time></p>'
REVIEW = set()  # pages à faire valider : jamais indexées, absentes du plan du site (fiche Habitatpresto validée le 18/11/2026)


def top(kick, h1, lead, crumb, photo=None, cta2=None, meta="", visual=None, dated=False):
    second = f'<a class="link" href="{cta2[1]}">{cta2[0]}</a>' if cta2 else ""
    fig = ""
    if photo:
        url, alt = img(photo)
        fig = f'<figure class="pg-photo frame"><img src="{url}" alt="{html.escape(alt)}" width="1200" height="900"></figure>'
    if visual:
        fig = visual
    lead_html = f'<p class="lead">{lead}</p>' if lead else ""
    meta = meta + (MAJ_HTML if dated else "")
    return f"""<section class="sheet pg-top" data-tone="light">
  <div class="grid pg-grid">
    <div class="pg-text">
      {crumb}
      <p class="kick">{kick}</p>
      <h1>{h1}</h1>
      {lead_html}{meta}
      <div class="actions"><a class="btn" href="https://wa.me/33781018936?text=Bonjour%20Martin%2C%20je%20suis%20artisan%20et%20je%20voudrais%20r%C3%A9server%20un%20appel%20de%2015%20minutes." target="_blank" rel="noopener" data-wa="cta"><span>Réserver un appel</span><svg class="tick" viewBox="0 0 10 10" aria-hidden="true"><path d="M1 1h8v8" fill="none" stroke="currentColor" stroke-width="1.4"/></svg></a>{second}</div>
    </div>
    {fig}
  </div>
</section>"""


def cols(items, title, intro="", tone="light", kick=""):
    lis = "\n".join(f'    <li><span class="sp-n">{i:02d}</span><h3>{h}</h3><p>{p}</p></li>' for i, (h, p) in enumerate(items, 1))
    intro = f"<p>{intro}</p>" if intro else ""
    return f"""<section class="sheet" data-tone="{tone}">
  <div class="grid sp-head"><h2 data-split>{title}</h2>{intro}</div>
  <ol class="sp-cols">
{lis}
  </ol>
</section>"""


def split(title, intro, items, tone="light", cls=""):
    lis = "\n".join(f"      <li>{x}</li>" for x in items)
    return f"""<section class="sheet" data-tone="{tone}">
  <div class="grid sp-split">
    <div><h2 data-split>{title}</h2><p>{intro}</p></div>
    <ul class="sp-list {cls}">
{lis}
    </ul>
  </div>
</section>"""


def faq(items, title="Vos questions, nos réponses", aside='Une autre question ? <a class="link" href="https://wa.me/33781018936?text=Bonjour%20Martin%2C%20j%E2%80%99ai%20une%20question%20avant%20de%20me%20lancer." target="_blank" rel="noopener" data-wa="faq">Écrire à Martin sur WhatsApp</a>', sid=None, all_href=None):
    rows = "\n".join(f'      <details class="fq"><summary><span>{q}</span><i class="fq-icon" aria-hidden="true"></i></summary><div class="fq-a"><p>{a}</p></div></details>' for q, a in items)
    sid_attr = f' id="{sid}"' if sid else ""
    all_link = f'<p><a class="link" href="{all_href}">Voir toutes les questions</a></p>' if all_href else ""
    return f"""<section class="faq sheet"{sid_attr} data-kind="faq" data-tone="paper">
  <div class="grid fq-grid">
    <div class="fq-head"><h2 data-split>{title}</h2><p>{aside}</p>{all_link}</div>
    <div class="fq-list">
{rows}
    </div>
  </div>
</section>"""


def more(title, all_text, all_href, links):
    """Bande de liens vers les pages voisines (autres métiers, autres articles)."""
    items = "".join(f'<li><a class="link" href="{h}">{t}</a></li>' for t, h in list(links) + [(all_text, all_href)])
    return f"""<section class="sheet more" data-tone="light">
  <div class="grid sp-split">
    <div><h2 data-split>{title}</h2></div>
    <ul class="more-list">{items}</ul>
  </div>
</section>"""


TRADE_LABEL = {"couverture": "Couvreurs", "menuiserie-exterieure": "Menuisiers", "facade": "Façadiers", "charpente": "Charpentiers", "isolation": "Entreprises d'isolation"}
READ_ADS = [(a["short"], f"/blog/{a['slug']}/") for a in ARTICLES if a["slug"] in ("google-ads-ou-meta-ads-artisan", "lead-partage-lead-exclusif-rendez-vous-qualifie")]

COMPARE = """<section class="sheet" data-tone="light">
  <div class="grid sp-head"><h2 data-split>Deux canaux, deux demandes</h2><p>Google capte ceux qui cherchent déjà. Meta touche ceux qui n'ont pas encore cherché. Nous choisissons selon votre métier et votre secteur.</p></div>
  <div class="sp-table" role="table" aria-label="Google Ads et Meta Ads">
    <div class="sp-row is-head" role="row"><span role="columnheader"></span><span role="columnheader">Google Ads</span><span role="columnheader">Meta Ads</span></div>
    <div class="sp-row" role="row"><span role="rowheader">La demande</span><span role="cell">Le propriétaire cherche déjà</span><span role="cell">Le propriétaire n'a pas encore cherché</span></div>
    <div class="sp-row" role="row"><span role="rowheader">Typiquement</span><span role="cell">Projets déjà avancés</span><span role="cell">Rénovations pas encore lancées</span></div>
    <div class="sp-row" role="row"><span role="rowheader">Le volume</span><span role="cell">Limité aux recherches locales</span><span role="cell">Tous les propriétaires du rayon</span></div>
    <div class="sp-row" role="row"><span role="rowheader">Le point clé</span><span role="cell">Écarter les recherches inutiles</span><span role="cell">Trier au téléphone</span></div>
  </div>
</section>"""


ROOF_URL = img("Un couvreur pose")[0]
GOOGLE_MOCK = """<figure class="pg-photo mk" aria-label="Exemple d’annonce sur Google pour un couvreur">
  <div class="mk-g">
    <div class="mk-search"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="10.5" cy="10.5" r="6.5" fill="none" stroke="currentColor" stroke-width="2"/><path d="m15.5 15.5 5 5" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg><span>couvreur amiens</span><i></i></div>
    <div class="mk-res is-ad">
      <p class="mk-spon">Sponsorisé</p>
      <p class="mk-site"><span class="mk-fav">TL</span><span><b>Toitures Lemaire</b><small>toitures-lemaire.fr › rendez-vous</small></span></p>
      <p class="mk-title">Couvreur à Amiens · Visite et devis gratuits</p>
      <p class="mk-desc">Réfection, zinguerie, démoussage. Entreprise locale, garantie décennale. Rappel en 5 minutes.</p>
      <p class="mk-links"><span>Réfection de toiture</span><span>Fuite urgente</span><span>Nos chantiers</span></p>
      <p class="mk-call"><span>📞</span>Appeler l’entreprise</p>
    </div>
    <div class="mk-res is-ghost"><i></i><i></i><i></i></div>
    <div class="mk-res is-ghost"><i></i><i></i></div>
  </div>
  <figcaption class="mk-tag">Exemple</figcaption>
</figure>"""
META_MOCK = f"""<figure class="pg-photo mk" aria-label="Exemple d’annonce Facebook et Instagram pour un couvreur">
  <div class="mk-phone">
    <div class="mk-notch"></div>
    <div class="mk-post">
      <p class="mk-site"><span class="mk-fav">TL</span><span><b>Toitures Lemaire</b><small>Sponsorisé · Amiens</small></span></p>
      <p class="mk-text">Votre toiture a plus de 15 ans&nbsp;? Faites-la vérifier par un couvreur de votre secteur. Visite et chiffrage offerts.</p>
      <div class="mk-img"><img src="{ROOF_URL}" alt="" loading="lazy"></div>
      <div class="mk-cta"><span><small>toitures-lemaire.fr</small><b>Visite gratuite à domicile</b></span><em>Demander une visite</em></div>
      
    </div>
  </div>
  <figcaption class="mk-tag">Exemple</figcaption>
</figure>"""

from anim import meta_anim, google_anim, ANIM_CSS, ANIM_JS
ROOF_AD = re.sub(r"w=\d+", "w=720", re.sub(r"h=\d+", "h=480", ROOF_URL)) + "&amp;bc=color"
def _anim_scene(anim, key):
    """Fond de l'animation : une photo du terrain en noir et blanc sous un voile marine, le téléphone reste en couleur."""
    url, _alt = img(key)
    return (anim.replace('<figure class="pg-photo mk mk-anim"', '<figure class="pg-photo mk mk-anim has-scene"', 1)
                .replace('<div class="ph" data-flow', f'<img class="mk-bg" src="{url}" alt="" width="1200" height="800">\n  <div class="ph" data-flow', 1))
GOOGLE_ANIM = _anim_scene(google_anim(ROOF_AD), "Un couvreur pose des tuiles") + ANIM_JS
META_ANIM = _anim_scene(meta_anim(ROOF_AD), "Une rue résidentielle") + ANIM_JS
EXTRA_CSS = EXTRA_CSS.replace("</style>", ANIM_CSS + "</style>", 1)

PHOTO = {"couverture": "Un couvreur pose", "facade": "Une façade en rénovation", "menuiserie-exterieure": "Un menuisier pose",
         "charpente": "Une charpente en bois", "isolation": "Isolation d"}
# Titres des pages métiers : le métier écrit en clair
TRADE_NOUN = {"couverture": "de couverture", "menuiserie-exterieure": "de menuiserie", "facade": "de façade", "charpente": "de charpente", "isolation": "d'isolation"}
TRADE_SOLO = {"couverture": "Un seul couvreur par secteur", "menuiserie-exterieure": "Un seul menuisier par secteur", "facade": "Un seul façadier par secteur",
              "charpente": "Un seul charpentier par secteur", "isolation": "Une seule entreprise d'isolation par secteur"}
# Annonces d'exemple des pages métiers : trois par métier, chacune avec sa photo, des personnes plutôt que des toits
AD_EXTRA = {"charpente": [("Aménager les combles", "Transformer vos combles en pièce à vivre ? Faites vérifier votre charpente par un charpentier de votre secteur. Visite et chiffrage à domicile.")],
            "isolation": [("Un chauffage qui tourne sans arrêt", "Vous chauffez, et la maison reste froide ? Faites étudier l'isolation de vos combles par une entreprise de votre secteur.")]}
AD_PHOTOS = {  # « u: » photo Unsplash (texte alternatif), sinon fichier local de /assets/photos (4:5, voir _build/stock/SOURCES.md)
    "couverture": ["couvreur-repare-toiture-ardoise", "u:Couvreur au travail sur une toiture", "u:Un couvreur pose des tuiles"],
    "menuiserie-exterieure": ["u:Une personne consulte son téléphone chez elle", "u:Un menuisier pose une fenêtre", "menuisier-dans-son-atelier"],
    "facade": ["artisan-enduit-mur-pierre", "u:Un propriétaire voit une annonce locale", "artisan-souriant-chantier-renovation"],
    "charpente": ["charpentier-sur-charpente-bois", "charpentier-travaille-poutre-bois", "deux-personnes-etudient-plans-travaux"],
    "isolation": ["femme-froid-dans-son-salon", "artisan-souriant-chantier-renovation", "u:Une personne consulte son téléphone chez elle"]}
def _ad_src(ph, w):
    h = w * 5 // 4
    if ph.startswith("u:"):
        url, _ = img(ph[2:])
        return re.sub(r"([?&])h=\d+", rf"\g<1>h={h}", re.sub(r"([?&])w=\d+", rf"\g<1>w={w}", url))
    return f"/assets/photos/{ph}-{w}x{h}.webp"

# En-tête des pages métiers : une visite déjà posée dans l'agenda, sur la photo (illustration, sans nom ni adresse)
VISIT = {"couverture": "Réfection de toiture", "facade": "Ravalement de façade", "menuiserie-exterieure": "Fenêtres de toute la maison",
         "charpente": "Reprise de charpente", "isolation": "Isolation des combles"}
VISIT_CARD = ('<div class="tr-visit" aria-hidden="true"><p class="tr-visit-k"><span>Visite de devis</span><b>Mardi, 14 h 30</b></p>'
              '<p class="tr-visit-t">{}</p><ul><li>Propriétaire rappelé</li><li>Projet vérifié</li></ul></div>')
paths = ["/"]

# ——— Métiers ———
for t in TRADES:
    path = f"/metiers/{t['slug']}/"
    short = "Chaque propriétaire est rappelé en moins de 5 minutes en semaine, et vérifié avant votre visite."
    _md_head = t['title'].replace('Trouver', 'Trouvez', 1)
    _md = [f"{_md_head} : des propriétaires qui préparent {PROJECT[t['slug']]}, rappelés en moins de 5 minutes{end}"
           for end in (", visite dans votre agenda.", " et vérifiés avant la visite.", " et vérifiés.", ".")]
    _md += [x.replace("Trouvez des chantiers", "Chantiers", 1) for x in _md]
    meta_desc = max((x for x in _md if len(x) <= 160), key=len)
    _ad_url, _ad_alt = img(PHOTO[t["slug"]])
    angles = "\n".join(f"""    <li><div class="ad-card"><div class="ad-head"><span class="ad-av" aria-hidden="true">VE</span><p class="ad-meta"><b>Votre entreprise</b><span>Sponsorisé</span></p></div><p class="ad-text">{b}</p><figure class="ad-img is-color"><img src="{_ad_src(ph, 800)}" srcset="{_ad_src(ph, 480)} 480w, {_ad_src(ph, 800)} 800w" sizes="(max-width: 760px) 86vw, 25vw" alt="" width="800" height="1000" loading="lazy" decoding="async"></figure><div class="ad-bar"><p class="ad-angle">{a}</p><p class="ad-cta">Demander une visite</p></div></div></li>""" for (a, b), ph in zip(t["angles"] + AD_EXTRA.get(t["slug"], []), AD_PHOTOS[t["slug"]]))
    trade_faq = t["faq"]  # les questions communes (prix, engagement, rappel, délais) sont sur /questions/
    body = "\n\n".join([
        top(f"{t['who']} · Partout en France", f"{t['h1']} {t['h1_em']}", short, crumbs(("Métiers", "/metiers/"), (t["name"], path)), PHOTO[t["slug"]], ("Voir ce que nous vérifions", "#appel"))
            .replace('<section class="sheet pg-top"', '<section class="sheet pg-top is-trade"', 1)
            .replace("</figure>", VISIT_CARD.format(VISIT[t["slug"]]) + "</figure>", 1),
        f"""<section class="sheet tr-hunt" data-tone="paper">
  <div class="grid sp-split">
    <div><h2 data-split>Les chantiers {TRADE_NOUN[t['slug']]} que nous cherchons pour vous</h2><p>Des chantiers qui valent le déplacement. Le reste est écarté avant d'arriver chez vous.</p></div>
    <div class="sp-two tr-card">
      <p class="tr-card-k"><b>Projets retenus</b></p>
      <ul class="sp-list">{''.join(f'<li>{x}</li>' for x in t['keep'])}</ul>
      <p class="tr-card-k is-no"><b>Projets écartés</b></p>
      <ul class="sp-list is-no">{''.join(f'<li>{x}</li>' for x in t['drop'])}</ul>
    </div>
  </div>
</section>""",
        cols([(h.rstrip("."), p) for h, p in t["problems"]], "Ce qui vous coûte des chantiers aujourd'hui", ""),
        f"""<section class="sheet tr-call" id="appel" data-tone="accent">
  <div class="grid sp-split">
    <div><h2 data-split>Ce que nous vérifions avant votre visite</h2><p>Rappel en moins de 5 minutes, en semaine de 8 h à 19 h. Si le projet ne correspond pas, pas de rendez-vous.</p></div>
    <div class="tr-card is-call"><p class="tr-card-k"><b>Les questions de notre appel</b><span>{len(t['questions'])} questions</span></p>
    <ol class="sp-list is-num">{''.join(f'<li>{q}</li>' for q in t['questions'])}</ol></div>
  </div>
</section>""",
        f"""<section class="sheet tr-ads" data-tone="tint">
  <div class="grid sp-head"><h2 data-split>Des annonces à votre nom, autour de votre dépôt</h2><p>Facebook et Instagram, dans un rayon de 25 à 40 km, avec vos photos de chantier. Exemples d'annonces, rédigées ensuite avec vous.</p></div>
  <ul class="sp-cols is-cards">
{angles}
  </ul>
</section>""",
        faq(trade_faq, f"Les questions des {t['who'].lower()}", all_href="/questions/"),
        more("Autres métiers", "Tous les métiers", "/metiers/", [(TRADE_LABEL[x["slug"]], f"/metiers/{x['slug']}/") for x in TRADES if x["slug"] != t["slug"]]),
    ])
    write(path, f"{t['title']} | Bartier & Co" if len(t['title']) <= 45 else t['title'], meta_desc, body, nav="/metiers/", metier=t["radio"], form_h2=TRADE_SOLO[t["slug"]],
          schema={"@context": "https://schema.org", "@graph": [
              {"@type": "Service", "name": fr(t["title"]), "serviceType": "Recherche de clients pour artisans du bâtiment", "audience": {"@type": "BusinessAudience", "audienceType": fr(t["who"])}, "description": fr(meta_desc), "url": SITE + path,
               "areaServed": {"@type": "Country", "name": "France"}, "provider": ORG_REF},
              bc_ld(("Métiers", "/metiers/"), (t["name"], path)), faq_ld(trade_faq)]})
    paths.append(path)

# ——— Page Métiers : tous les métiers, ce que nous cherchons, photos de chantier, saisons, méthode, questions ———
_mb = (ROOT / "_build" / "metiers_blocs.html").read_text(encoding="utf-8")
_blk = {k: re.search(r'<section class="[^"]*" id="%s"[\s\S]*?</section>' % k, _mb).group(0) for k in ("sectors", "gallery", "calendar")}
HUB_SECTORS = _blk["sectors"].replace(
    "<p>Uniquement les métiers où un chantier vaut plusieurs milliers d’euros. Pas de dépannage, pas de petits travaux.</p>",
    "", 1)
HUB_GALLERY = _blk["gallery"]
HUB_SEASONS = _blk["calendar"].replace('data-tone="light"', 'data-tone="paper"', 1)
_lj = lambda xs: ", ".join([xs[0]] + [x[:1].lower() + x[1:] for x in xs[1:]])  # liste dans une phrase : minuscule après la virgule
_rows = "\n".join(
    f'<tr><td class="mt-name"><a href="/metiers/{t["slug"]}/">{t["name"]}</a></td><td class="mt-keep">{_lj(t["keep"][:3])}</td><td class="mt-drop">{_lj(t["drop"][:2])}</td></tr>'
    for t in TRADES)
HUB_TABLE = f"""<section class="sheet" id="par-metier" data-tone="paper">
  <div class="grid sp-head"><h2 data-split>Selon votre métier, les petits travaux sont écartés dès l'appel.</h2></div>
  <div class="grid art-grid">
    <div class="prose is-wide">
<table class="mt-table">
<thead><tr><th>Votre métier</th><th class="mt-keep">Les chantiers que nous cherchons</th><th class="mt-drop">Ceux que nous écartons</th></tr></thead>
<tbody>
{_rows}
</tbody>
</table>
    </div>
  </div>
</section>"""
HUB_FAQ = [
    ("Quels métiers du bâtiment accompagnez-vous ?", "Cinq métiers : la couverture et la zinguerie, la menuiserie extérieure, la façade et le ravalement, la charpente et l'isolation."),
    ("Mon métier n'est pas dans la liste : est-ce possible ?", "Parlons-en. Si vous travaillez chez des propriétaires, Martin vous dit pendant l'appel si notre méthode peut marcher pour vous."),
    ("Pourquoi écarter les petits dépannages ?", "Parce qu'ils coûtent une demi-journée pour un petit montant. Nos annonces et nos questions au téléphone visent des chantiers qui valent le déplacement."),
    ("Travaillez-vous avec deux artisans du même métier dans la même zone ?", "Non. Un seul artisan par métier et par secteur : vos rendez-vous ne sont proposés à personne d'autre."),
    ("Les demandes changent-elles selon la saison ?", "Oui. Les fuites en hiver, les réfections et les ravalements au printemps, l'entretien et les menuiseries à l'automne. Les annonces suivent les saisons pour garder un agenda régulier."),
]
write("/metiers/", "Trouver des chantiers par métier du bâtiment | Bartier & Co",
      "Des clients pour couvreurs, menuisiers, façadiers, charpentiers et entreprises d'isolation, partout en France. Un seul artisan par métier et par secteur.",
      "\n\n".join([
          top("Métiers", "Quel que soit votre métier, nous trouvons vos clients.", "Des propriétaires avec un projet concret, près de chez vous. Un seul artisan par métier et par secteur.", crumbs(("Métiers", "/metiers/")), "Artisan souriant"),
          HUB_SECTORS,
          label_tables(HUB_TABLE),
          HUB_GALLERY,
          HUB_SEASONS,
          """<section class="sheet" data-tone="light">
  <div class="grid sp-split">
    <div><h2 data-split>Une méthode adaptée à votre métier</h2></div>
    <div class="prose">
      <p>Des annonces locales à votre nom, sur <a href="/google-ads/">Google</a> et sur <a href="/meta-ads/">Facebook et Instagram</a>. Chaque demande client est rappelée en moins de 5 minutes, vérifiée, puis la visite est fixée dans votre agenda.</p>
      <p>Pour comparer avec les autres façons de trouver des clients : <a href="/trouver-des-chantiers/">comment trouver des chantiers</a>.</p>
    </div>
  </div>
</section>""",
          faq(HUB_FAQ, title="Des questions ?"),
      ]), nav="/metiers/", schema={"@context": "https://schema.org", "@graph": [
          bc_ld(("Métiers", "/metiers/")),
          {"@type": "ItemList", "name": "Métiers du bâtiment accompagnés par Bartier & Co", "itemListElement": [
              {"@type": "ListItem", "position": i, "name": fr(t["name"]), "url": f"{SITE}/metiers/{t['slug']}/"} for i, t in enumerate(TRADES, 1)]},
          faq_ld(HUB_FAQ)]})
paths.insert(1, "/metiers/")

# ——— Google Ads ———
write("/google-ads/", "Google Ads pour artisans du bâtiment | Bartier & Co",
      "Campagnes Google Ads locales pour artisans du bâtiment : captez les propriétaires qui cherchent déjà, rappelés en moins de 5 minutes, vérifiés avant la visite.",
      "\n\n".join([
          top("Google Ads", "Apparaissez sur Google quand vos clients cherchent un artisan.", "Un propriétaire tape « couvreur » et sa ville : il voit votre annonce. Nous rappelons chaque demande en moins de 5 minutes.", crumbs(("Google Ads", "/google-ads/")), None, ("Comparer avec Meta", "/meta-ads/"), visual=GOOGLE_ANIM),
          cols([("Les gros projets", "Réfection complète, ravalement, toutes les fenêtres à changer : le propriétaire cherche une entreprise sérieuse près de chez lui."),
                ("Les projets déjà avancés", "Le propriétaire compare des entreprises. Celle qui le rappelle la première a souvent la visite."),
                ("Les secteurs où les recherches sont nombreuses", "Assez de recherches autour de chez vous pour que la campagne tourne toute l'année.")],
               "Quand choisir Google ?", "Quand le propriétaire cherche déjà un artisan : il faut être visible, et le rappeler avant les autres."),
          split("Comment nous réglons votre campagne", "Chaque clic se paie : nous écartons ceux qui ne deviendront jamais des devis signés.",
                ["Campagnes par métier et par commune de votre zone", "Recherches inutiles exclues : gratuit, pas cher, emploi, formation, bricolage",
                 "Une page à votre nom, rapide sur mobile", "Chaque appel et chaque formulaire suivi jusqu'au rendez-vous",
                 "Rappel en moins de 5 minutes en semaine, projet vérifié, rendez-vous dans votre agenda"], tone="paper"),
          split("Tout est à votre nom", "Vous gardez ce qui a été construit, même si vous arrêtez.",
                ["Compte Google Ads à votre nom", "Budget payé directement à Google", "Recherches, clics et dépenses visibles en détail"]),
          COMPARE.replace('class="sp-table"', 'class="sp-table is-google"', 1),  # page Google : la colonne Google est mise en avant
          faq(GOOGLE_FAQ),
          more("À lire aussi", "Tous les articles", "/blog/", READ_ADS),
      ]), nav="/google-ads/",
      schema={"@context": "https://schema.org", "@graph": [{"@type": "Service", "name": "Google Ads pour artisans du bâtiment", "serviceType": "Publicité locale sur Google", "url": SITE + "/google-ads/",
                                                            "description": "Campagnes Google Ads locales pour les artisans du bâtiment : les propriétaires qui cherchent un artisan dans leur secteur sont rappelés en moins de 5 minutes.",
                                                            "areaServed": {"@type": "Country", "name": "France"}, "provider": ORG_REF}, bc_ld(("Google Ads", "/google-ads/")), faq_ld(GOOGLE_FAQ)]})
paths.append("/google-ads/")

# ——— Meta Ads ———
write("/meta-ads/", "Publicité Facebook et Instagram pour artisans | Bartier & Co",
      "Annonces Facebook et Instagram locales pour artisans du bâtiment : les propriétaires de votre secteur, rappelés en moins de 5 minutes, vérifiés à l’appel.",
      "\n\n".join([
          top("Meta Ads · Facebook et Instagram", "Apparaissez sur Facebook et Instagram auprès de vos futurs clients.", "Des annonces à votre nom, vues par les propriétaires de votre secteur. Nous rappelons chaque demande en moins de 5 minutes.", crumbs(("Meta Ads", "/meta-ads/")), None, ("Comparer avec Google", "/google-ads/"), visual=META_ANIM),
          cols([("Autour de votre dépôt", "Dans un rayon de 25 à 40 km, réglé commune par commune."),
                ("Avec vos photos de chantier", "Vos chantiers et votre équipe, plutôt que des images de banque."),
                ("Au bon moment de l'année", "Après les intempéries, avant l'hiver, au printemps pour la rénovation.")],
               "Des annonces à votre nom", "Avec vos chantiers, montrées à vos futurs clients."),
          split("Chaque demande vérifiée au téléphone", "Nous appelons chaque personne qui répond à l'annonce. Seuls les projets sérieux arrivent dans votre agenda.",
                ["Formulaire avec questions de tri et accord explicite pour être recontacté", "Preuve du consentement conservée pour chaque demande",
                 "Rappel en moins de 5 minutes, en semaine de 8 h à 19 h", "Propriétaire, projet, commune et délai vérifiés",
                 "Rendez-vous dans votre agenda, rappel par SMS au propriétaire avant la visite", "Flyers dans les rues voisines de chaque chantier signé"], tone="paper"),
          split("Tout est à votre nom", "Tout vous reste si vous arrêtez.",
                ["Page Facebook et compte publicitaire à votre nom", "Budget payé directement à Meta", "Toutes les statistiques des annonces visibles"]),
          COMPARE,
          faq(META_FAQ),
          more("À lire aussi", "Tous les articles", "/blog/", READ_ADS),
      ]), nav="/meta-ads/",
      schema={"@context": "https://schema.org", "@graph": [{"@type": "Service", "name": "Publicité Facebook et Instagram pour artisans du bâtiment", "serviceType": "Publicité locale sur Facebook et Instagram", "url": SITE + "/meta-ads/",
                                                            "description": "Annonces Facebook et Instagram au nom de l'artisan, dans un rayon de 25 à 40 km autour de son dépôt. Chaque demande est rappelée en moins de 5 minutes.",
                                                            "areaServed": {"@type": "Country", "name": "France"}, "provider": ORG_REF}, bc_ld(("Meta Ads", "/meta-ads/")), faq_ld(META_FAQ)]})
paths.append("/meta-ads/")

# ——— Particuliers : capter la demande des propriétaires ———
import particuliers as PF
if NOTICES.get("particulier_consent_label"):
    PF.CONSENT = html.escape(NOTICES["particulier_consent_label"], quote=False)
if "confidentialite" in LEGAL_READY and NOTICES.get("particulier_form_notice"):
    PF.PRIVACY = NOTICES["particulier_form_notice"]
pf_body = PF.build(lambda a: (img(a)[0], html.escape(img(a)[1])), PHONE, PHONE_TXT, crumbs(("Devis travaux", PF.PATH)))
import villes as VL  # pages « Devis travaux à <ville> »
_ARROW = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'
_regs = sorted({c["region"] for c in VL.CITIES})
VL_HUB = "".join(
    f'<section class="vlh-r" aria-label="{r}"><h3>{r}<small>{sum(c["region"] == r for c in VL.CITIES)}</small></h3><ul>' + "".join(
        f'<li class="vlh-c" data-c="{c["slug"]}"><a href="{VL.path(c)}"><b>{c["name"]}</b><span>{c["hook"].rstrip(".")}</span>{_ARROW}</a></li>'
        for c in sorted((c for c in VL.CITIES if c["region"] == r), key=lambda c: c["name"])) + "</ul></section>" for r in _regs)
# survol d'une ville dans la liste : son point s'allume sur la carte ; survol d'un point : la ville s'allume dans la liste
VL_HL = "".join(f'.vlh:has([data-c="{c["slug"]}"]:hover) [data-c="{c["slug"]}"] .vl-dot,.vlh:has([data-c="{c["slug"]}"]:focus-visible) [data-c="{c["slug"]}"] .vl-dot{{fill:var(--accent,#2D5BE3)}}'
                f'.vlh:has([data-c="{c["slug"]}"]:hover) [data-c="{c["slug"]}"] .vl-lab{{fill:var(--accent,#2D5BE3)}}'
                f'.vlh:has([data-c="{c["slug"]}"]:hover) .vlh-c[data-c="{c["slug"]}"] b{{color:var(--accent,#2D5BE3)}}' for c in VL.CITIES)
VL_HUB_CSS = (""".vlh{display:grid;grid-template-columns:minmax(0,520px) minmax(0,1fr);gap:48px clamp(48px,6vw,104px);align-items:start;padding:0 var(--cell)}
.vlh-map{position:sticky;top:112px;margin:0}
.vlh-map .vl-svg{display:block;width:100%;height:auto}
.vlh-map figcaption{max-width:38ch;margin-top:20px;font-size:.88rem;line-height:1.5;color:var(--muted)}
.vlh-list{columns:2;column-gap:56px}
.vlh-r{break-inside:avoid;margin:0 0 44px}
.vlh-r h3{display:flex;align-items:baseline;justify-content:space-between;gap:12px;margin:0;padding-bottom:10px;border-bottom:1px solid currentColor;font-size:.8rem;font-weight:400;line-height:1.3;color:var(--muted)}
.vlh-r h3 small{font-size:.78rem;font-variant-numeric:tabular-nums}
.vlh-r ul{margin:0;padding:0;list-style:none}
.vlh-c a{display:grid;grid-template-columns:minmax(0,1fr) auto;column-gap:16px;padding:16px 0;border-bottom:1px solid var(--rule);color:inherit;text-decoration:none}
.vlh-c b{font:400 1.3rem/1.2 var(--f-display);letter-spacing:-.01em;transition:color .2s}
.vlh-c span{grid-column:1;margin-top:6px;font-size:.9rem;line-height:1.45;color:var(--muted)}
.vlh-c svg{grid-column:2;grid-row:1/span 2;align-self:center;width:20px;height:20px;opacity:.3;transition:transform .2s,opacity .2s,color .2s}
.vlh-c a:hover svg,.vlh-c a:focus-visible svg{opacity:1;color:var(--accent,#2D5BE3);transform:translateX(4px)}
.vlh-c a:focus-visible{outline:2px solid var(--accent,#2D5BE3);outline-offset:2px}
.vl-svg circle.vl-dot{transition:fill .2s}
@media (max-width:1100px){.vlh-list{columns:1}}
@media (max-width:760px){.vlh{grid-template-columns:1fr;gap:32px}.vlh-map{position:static;max-width:400px}.vlh-c b{font-size:1.2rem}}
@media (prefers-reduced-motion:reduce){.vlh-c svg,.vlh-c b,.vl-svg circle.vl-dot{transition:none}}""" + VL_HL)
pf_body = pf_body if not VL.CITIES else pf_body.replace('<section class="sheet pf-leak is-short"', f"""<section class="sheet" id="villes" data-tone="paper">
  <style>{VL.MAP_CSS}{VL_HUB_CSS}</style>
  <div class="grid sp-head"><h2 data-split>Devis travaux par ville</h2><p>Les règles et les aides changent d’une ville à l’autre</p></div>
  <div class="vlh"><figure class="vl-map vlh-map">{VL.carte()}<figcaption>{len(VL.CITIES)} villes, chacune avec ses règles d’urbanisme, ses aides et ses démarches, vérifiées sur les sources officielles.</figcaption></figure><div class="vlh-list">{VL_HUB}</div></div>
</section>

<section class="sheet pf-leak is-short\"""", 1)
pf_top = absolutize(BODY_OPEN)
pf_top = pf_top.replace('class="link" href="/devis-travaux/"', 'class="link" href="/devis-travaux/" aria-current="page"', 1)
pf_top = re.sub(r'<p class="hdr-tag">[^<]*', '<p class="hdr-tag">Vos travaux, un seul artisan près de chez vous', pf_top, count=1)
pf_top = pf_top.replace('<a class="hdr-cta" href="https://wa.me/33781018936?text=Bonjour%20Martin%2C%20je%20suis%20artisan%20et%20je%20voudrais%20r%C3%A9server%20un%20appel%20de%2015%20minutes." target="_blank" rel="noopener" data-wa="header"><span>Réserver un appel</span>', '<a class="hdr-cta" href="#projet"><span>Mon devis</span>', 1)
pf_top = pf_top.replace('<span>Appeler Martin</span>', '<span>Nous appeler</span>', 1)
pf_top = pf_top.replace('<a href="#contact">Contact</a>', '<a href="#projet">Obtenir mon devis gratuit</a>', 1)
pf_top = pf_top.replace('Des clients pour les artisans du bâtiment</p>', 'Un seul artisan près de chez vous, sans frais</p>')
pf_tail = absolutize(TAIL)
pf_tail = pf_tail.replace('<p>Faire équipe.<br> Faire la différence.</p>', '<p>Un projet de travaux&nbsp;?<br> Un seul artisan, près de chez vous.</p>', 1)
pf_tail = pf_tail.replace('<a class="btn" href="https://wa.me/33781018936?text=Bonjour%20Martin%2C%20je%20suis%20artisan%20et%20je%20voudrais%20r%C3%A9server%20un%20appel%20de%2015%20minutes." target="_blank" rel="noopener" data-wa="cta"><span>Réserver un appel</span>', '<a class="btn" href="#projet"><span>Obtenir mon devis gratuit</span>', 1)
pf_tail = pf_tail.replace('<small>Cofondateur</small>', '<small>Bartier &amp; Co · vos travaux</small>', 1)
pf_tail = pf_tail.replace('<b>Parler à Martin<span>, cofondateur</span></b>', '<b>Une question&nbsp;?<span> Écrivez à Martin</span></b>', 1)
pf_tail = re.sub(r'<p class="wa-bubble">[\s\S]*?(?=<div class="wa-actions">)', lambda m: '<p class="wa-bubble">Bonjour. Un projet de travaux ou une question&nbsp;? Écrivez-moi, je vous réponds personnellement.</p>\n      <p class="wa-k">Choisissez une question, ou écrivez la vôtre&nbsp;:</p>\n' + "\n".join(
    f'      <a class="wa-q" href="{html.escape(wa(m))}" target="_blank" rel="noopener" data-wa="question-particulier">{q}</a>' for q, m in [
        ("Combien vont coûter mes travaux&nbsp;?", "Bonjour, j'ai un projet de travaux ([toiture, façade, fenêtres...]) à [ville]. Combien cela peut-il coûter ?"),
        ("Un artisan peut-il passer cette semaine&nbsp;?", "Bonjour, j'ai des travaux à faire à [ville]. Un artisan peut-il passer cette semaine ?"),
        ("J’ai une fuite, que faire&nbsp;?", "Bonjour, j'ai une fuite de toiture à [ville]. Que dois-je faire ?")]) + "\n      ", pf_tail, count=1)
pf_tail = pf_tail.replace('href="#contact"', 'href="/#contact"')
pf_schema = PF.schema(SITE, faq_ld, bc_ld)
def pf_fast(doc):
    """Pages d'atterrissage des annonces : pas d'écran de chargement ; sur téléphone, aucune bibliothèque
    d'animation ; sur ordinateur, les animations se chargent après l'affichage."""
    doc = re.sub(r'<style id="ld-css">[\s\S]*?</script>\n', "", doc)
    doc = re.sub(r'<div class="ld" id="ld"[\s\S]*?</script>\n', "", doc)
    libs = re.findall(r'<script src="(/assets/js/[^"]+)"></script>', doc)
    doc = re.sub(r'<script src="/assets/js/[^"]+"></script>\n?', "", doc)
    i = doc.index("<script>(()=>{const $=(s,r=document)")
    j = doc.index("</script>", i)
    main = doc[i + len("<script>"):j].rstrip()
    assert main.endswith("})();")
    main = "window.__bcMain=" + main[:-3] + ";"
    # Sur téléphone, sans bibliothèque d'animation : l'en-tête prend quand même la couleur de la section qu'il recouvre
    loader = ('<script>(function(){var d=document.documentElement,run=function(){if(window.__bcMain)window.__bcMain()};'
              'function tone(){var h=document.querySelector(".hdr");if(!h||!("IntersectionObserver" in window))return;'
              'var o=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting)h.dataset.tone=e.target.dataset.tone||"light"})},{rootMargin:"-4% 0px -95% 0px"});'
              '[].forEach.call(document.querySelectorAll("main [data-kind], main > section[data-tone], body > footer"),function(x){o.observe(x)})}'
              'if(innerWidth<761||!window.matchMedia||matchMedia("(prefers-reduced-motion: reduce)").matches){d.classList.remove("motion");run();tone();return}'
              'var L=' + json.dumps(libs) + ',k=0;function next(){if(k>=L.length){run();return}var s=document.createElement("script");s.src=L[k++];s.onload=next;s.onerror=next;document.body.appendChild(s)}'
              'if(document.readyState==="complete")next();else addEventListener("load",next)})();</script>')
    return doc[:i] + "<script>" + main + "</script>\n" + loader + doc[j + len("</script>"):]


def pf_write(path, title, desc, body, schema):
    doc = head(title, desc, path, schema) + PF.CSS + PF.CSS_TRADE + "\n" + pf_top + "\n" + fr(body) + "\n" + pf_tail
    doc = doc.replace("</body>", PF.js() + "\n</body>", 1)
    doc = pf_fast(doc)
    out = ROOT / path.strip("/") / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(doc, encoding="utf-8")
    paths.append(path)


pf_write(PF.PATH, PF.TITLE, PF.DESC, pf_body, pf_schema)
for k in PF.SLUG:
    t = next(x for x in PF.TRADES if x[0] == k)
    sub = f"{PF.PATH}{PF.SLUG[k]}/"
    body = PF.build_trade(lambda a: (img(a)[0], html.escape(img(a)[1])), PHONE, PHONE_TXT, crumbs(("Devis travaux", PF.PATH), (t[1], sub)), k)
    if VL.CITIES:
        _tl = "".join(f'<li><a class="link" href="{VL.path(c)}#t-{k}">{VL.TRADE_H3[k].format(a=VL.a_(c))}</a></li>' for c in VL.CITIES)
        body = re.sub(r'(<section class="sheet pf-others".*?</ul>)', lambda m: m.group(1) + '\n  <p style="margin:36px 0 14px;padding:0 var(--cell);font-size:.8rem;color:var(--muted)">Par ville</p>\n  <ul class="pf-olist">' + _tl + '</ul>', body, count=1, flags=re.S)
    pf_write(sub, PF.PAGES[k]["title"], PF.PAGES[k]["desc"], body, PF.trade_schema(SITE, faq_ld, bc_ld, k))
for c in VL.CITIES:
    sub = VL.path(c)
    body = VL.build_city(PF, PHONE, PHONE_TXT, crumbs(("Devis travaux", PF.PATH), (c["name"], sub)), c, img=lambda a: (img(a)[0], html.escape(img(a)[1])))
    pf_write(sub, c["title"], c["desc"], body, VL.schema(SITE, faq_ld, bc_ld, PF, c))

# ——— Qui sommes-nous ———
# En tête de page : les deux fondateurs côte à côte (image composée depuis _build/portraits/, sans métadonnées)
# Qui vous répond : titre à gauche, les deux fondateurs et le contact de Martin à droite
TEAM_ABOUT = """<section class="team-about sheet" id="equipe" data-kind="team" data-tone="dark">
  <div class="grid ta-grid">
    <div class="ta-head">
      <h2 data-split>Vous parlez aux fondateurs</h2>
      <p>Du premier appel au lancement de vos annonces, sans standard.</p>
    </div>
    <div class="ta-body">
      <ul class="ta-people">
        <li id="charles"><img src="/assets/photos/charles-le-cottier-360x450-nb.webp" alt="Portrait de Charles Le Cottier, cofondateur de Bartier &amp; Co" width="360" height="450" loading="lazy" decoding="async"><div><h3>Charles Le Cottier</h3><p>Cofondateur</p></div></li>
        <li id="martin"><img src="/assets/photos/martin-barthelemy-360x450-nb.webp" alt="Portrait de Martin Barthélémy, cofondateur de Bartier &amp; Co" width="360" height="450" loading="lazy" decoding="async"><div><h3>Martin Barthélémy</h3><p>Cofondateur</p></div></li>
      </ul>
      <p class="ta-note">Une question avant de vous lancer ? Appelez Martin en semaine, de 8&nbsp;h à 19&nbsp;h, ou écrivez-lui.</p>
      <div class="ta-acts">
        <a class="dq-wa" href="https://wa.me/33781018936?text=Bonjour%20Martin%2C%20je%20suis%20artisan.%20Mon%20secteur%20est-il%20encore%20libre%20%3F" target="_blank" rel="noopener" data-wa="team">Écrire à Martin sur WhatsApp</a>
        <a class="link" href="tel:+33781018936">Appeler le 07 81 01 89 36</a>
      </div>
    </div>
  </div>
</section>"""

DUO = ('<figure class="pg-photo frame"><img src="/assets/photos/fondateurs-bartier-co-1200x900-nb.webp" '
       'srcset="/assets/photos/fondateurs-bartier-co-480x360-nb.webp 480w, /assets/photos/fondateurs-bartier-co-800x600-nb.webp 800w, /assets/photos/fondateurs-bartier-co-1200x900-nb.webp 1200w" '
       'sizes="(max-width: 760px) 100vw, 50vw" alt="Charles Le Cottier et Martin Barthélémy, cofondateurs de Bartier &amp; Co" width="1200" height="900"></figure>')
write("/qui-sommes-nous/", "Qui sommes-nous : les fondateurs de Bartier & Co",
      "Bartier & Co, société fondée par Charles Le Cottier et Martin Barthélémy, trouve des clients aux artisans du bâtiment : un seul par métier et par secteur.",
      "\n\n".join([
          top("Qui sommes-nous", "Deux fondateurs au service de votre agenda.", "Bartier & Co est une société française fondée par Charles Le Cottier et Martin Barthélémy. Nous trouvons des clients aux artisans du bâtiment, partout en France.", crumbs(("Qui sommes-nous", "/qui-sommes-nous/")), visual=DUO),
          """<section class="sheet" data-tone="light">
  <div class="grid sp-split">
    <div><h2 data-split>Vous n'avez pas à courir après les devis</h2></div>
    <div class="prose">
      <p>Vous avez du métier et des clients satisfaits, mais pas assez de projets sérieux chaque semaine.</p>
      <p>Les plateformes vendent la même demande à vous et à vos concurrents. Le bouche-à-oreille ne se commande pas. Et quand vous êtes sur un toit, vous ne pouvez pas répondre au téléphone.</p>
      <p>Alors nous nous en occupons pour vous : des annonces près de chez vous, chaque demande rappelée en moins de 5 minutes, et des visites rien que pour vous dans votre métier et votre secteur.</p>
    </div>
  </div>
</section>""",
          cols([("Un seul interlocuteur", "Vous avez le numéro direct de Martin. Il vous répond sous un jour ouvré."),
                ("Des engagements écrits", "Exclusivité, un seul artisan par métier et par secteur, rappel en moins de 5 minutes en semaine, aucune durée minimale. Tout est dans le contrat."),
                ("Des chiffres vérifiables", "Le budget est sur votre compte, et chaque rendez-vous est suivi jusqu'au chantier signé.")],
               "Comment nous travaillons", "", tone="paper").replace('<section class="sheet"', '<section class="sheet ws-cols"', 1),
          (ROOT / "_build" / "demarrage.html").read_text(encoding="utf-8").split("-->", 1)[1].strip(),
          TEAM_ABOUT,
          """<section class="sheet" data-tone="light">
  <div class="grid sp-split">
    <div><h2 data-split>Bartier & Co en bref</h2></div>
    <div class="prose">
      <dl class="facts-dl">
        <div><dt>Société</dt><dd>Bartier & Co, SAS. <a href="/mentions-legales/">Mentions légales</a>.</dd></div>
        <div><dt>Activité</dt><dd>Trouver des clients aux artisans du bâtiment : annonces locales Google et Meta, rappel des demandes en moins de 5 minutes, visites fixées dans l'agenda.</dd></div>
        <div><dt>Métiers</dt><dd><a href="/metiers/couverture/">Couverture</a>, <a href="/metiers/facade/">façade</a>, <a href="/metiers/menuiserie-exterieure/">menuiserie extérieure</a>, <a href="/metiers/charpente/">charpente</a>, <a href="/metiers/isolation/">isolation</a>.</dd></div>
        <div><dt>Zone</dt><dd>France. Un seul artisan par métier et par secteur, sans engagement de durée.</dd></div>
        <div><dt>Particuliers</dt><dd><a href="/devis-travaux/">Mise en relation gratuite</a> avec un artisan partenaire.</dd></div>
      </dl>
    </div>
  </div>
</section>""",
      ]), nav="/qui-sommes-nous/",
      schema={"@context": "https://schema.org", "@graph": [
          {"@type": "AboutPage", "name": "Qui sommes-nous", "url": SITE + "/qui-sommes-nous/", "inLanguage": "fr-FR", "mainEntity": {"@id": SITE + "/#org"}},
          dict(ORG, founder=[{"@id": f"{SITE}/qui-sommes-nous/#{k}"} for k, n, j in FOUNDERS]),
          *[{"@type": "Person", "@id": f"{SITE}/qui-sommes-nous/#{k}", "name": n, "jobTitle": j, "image": portrait(k), "url": f"{SITE}/qui-sommes-nous/#{k}", "worksFor": {"@id": SITE + "/#org"}} for k, n, j in FOUNDERS],
          bc_ld(("Qui sommes-nous", "/qui-sommes-nous/"))]})
paths.append("/qui-sommes-nous/")

# ——— Questions : toutes les questions des artisans, par thème ———
import questions as QS
_qs_all = [qa for g in QS.GROUPS for qa in g[3]]
write("/questions/", "Questions fréquentes des artisans | Bartier & Co",
      "Prix, engagement, publicité, exclusivité, rappel en moins de 5 minutes, cadre légal : les réponses aux questions des artisans du bâtiment, en quelques lignes.",
      "\n\n".join([
          top("Questions", "Vos questions, nos réponses", "Ce que les artisans nous demandent avant de commencer : la méthode, le prix, les engagements et le cadre légal.", crumbs(("Questions", "/questions/")),
              visual='<nav class="gd-toc" aria-label="Les sujets"><p class="gd-toc-k">Les sujets</p><ol>' + "".join(f'<li><a href="#{sid}">{title}<small>{len(items)} questions</small></a></li>' for sid, title, intro, items in QS.GROUPS) + '</ol></nav>'),
          *[faq(items, title=title, aside=intro, sid=sid) for sid, title, intro, items in QS.GROUPS],
          more("Aller plus loin", "Le lexique", "/lexique/", [("Comment trouver des chantiers", "/trouver-des-chantiers/"), ("Google Ads pour artisans", "/google-ads/"), ("Meta Ads pour artisans", "/meta-ads/")]),
      ]), nav="/questions/",
      schema={"@context": "https://schema.org", "@graph": [bc_ld(("Questions", "/questions/")), dict(faq_ld(_qs_all), **{"@id": SITE + "/questions/#faq-page"})]})
paths.append("/questions/")

# ——— Blog ———
COVER = {"lead-partage-lead-exclusif-rendez-vous-qualifie": "Tuiles de toiture", "google-ads-ou-meta-ads-artisan": "Une personne consulte", "relance-devis-artisan": "Une chargée de rappel", "dpe-2027": "Isolation d'un mur"}
import contenu as CT
for a in ARTICLES:
    _p = CT.PLUS.get(a["slug"])
    if _p and not a.get("faq"):
        assert _p["before"] in a["body"], a["slug"]
        a["body"] = a["body"].replace(_p["before"], _p["insert"] + _p["before"], 1) + _p["append"] + "\n" + CT.qa_html(_p["faq"]) + "\n"
        a["faq"] = _p["faq"]
    elif a.get("faq") and "<h2>Questions fréquentes</h2>" not in a["body"]:
        a["body"] = a["body"] + "\n" + CT.qa_html(a["faq"]) + "\n"
    a["minutes"] = max(3, round(len(re.sub(r"<[^>]+>", " ", a["body"]).split()) / 200))
posts = []
for a in ARTICLES:
    url, alt = img(COVER[a["slug"]])
    posts.append(f'    <li class="post"><a class="post-link" href="/blog/{a["slug"]}/"><p class="post-meta soft"><time datetime="{a.get('date', TODAY)}">{a.get('date_short', '17 nov. 2026')}</time><br>{a["tag"]}</p><h2 class="post-title">{a["short"]}</h2><figure class="post-photo frame" data-wipe><img src="{url}" alt="{html.escape(alt)}" width="900" height="676"></figure></a></li>')
write("/blog/", "Blog : chantiers, publicité, devis et DPE 2027 | Bartier & Co",
      "Articles courts et sourcés, pour les artisans du bâtiment et les propriétaires : trouver des chantiers, publicité locale, relance des devis, DPE 2027.",
      "\n\n".join([
          top("Blog", "Plus de chantiers, moins de soirées au téléphone.", "Des articles courts et sourcés, pour les artisans du bâtiment et pour les propriétaires.", crumbs(("Blog", "/blog/")),
              visual='<nav class="gd-toc" aria-label="Les articles"><p class="gd-toc-k">Les articles</p><ol>' + "".join(f'<li><a href="/blog/{a["slug"]}/">{a["short"]}<small>{a["tag"]} · {a["minutes"]} min</small></a></li>' for a in ARTICLES) + '</ol></nav>'),
          f"""<section class="journal sheet" data-kind="journal" data-tone="light">
  <ul class="jr-list">
{chr(10).join(posts)}
  </ul>
</section>""",
          cols([("Pour les artisans du bâtiment",
                 'Trouver des chantiers sans attendre le bouche-à-oreille : choisir entre <a class="link" href="/blog/lead-partage-lead-exclusif-rendez-vous-qualifie/">demande partagée, exclusive ou rendez-vous qualifié</a>, '
                 'entre <a class="link" href="/blog/google-ads-ou-meta-ads-artisan/">Google Ads et Meta Ads</a>, et <a class="link" href="/blog/relance-devis-artisan/">relancer ses devis</a>. '
                 'Les plateformes de chantiers sont comparées dans <a class="link" href="/trouver-des-chantiers/">Trouver des chantiers</a>.'),
                ("Pour les propriétaires",
                 'Les règles qui changent et les démarches avant des travaux : <a class="link" href="/blog/dpe-2027/">le DPE en 2027</a>, <a class="link" href="/devis-travaux/#prix">les prix par métier</a>, '
                 'et les règles locales à ' + ", ".join(f'<a class="link" href="{VL.path(c)}">{c["name"]}</a>' for c in VL.CITIES[:5])
                 + (f' et dans <a class="link" href="/devis-travaux/#villes">{len(VL.CITIES) - 5} autres villes</a>.' if len(VL.CITIES) > 6
                    else f' et <a class="link" href="{VL.path(VL.CITIES[-1])}">{VL.CITIES[-1]["name"]}</a>.')),
                ("Comment nous écrivons",
                 'Chaque article est signé par <a class="link" href="/qui-sommes-nous/#charles">Charles Le Cottier</a>, cofondateur, et cite ses sources officielles : Service-Public, Légifrance, ADEME, Insee. '
                 'Quand une règle change, l’article est mis à jour et daté.')],
               "Pour qui nous écrivons", "Chaque article répond à une question précise, avec ses sources et sa date.", tone="paper"),
      ]), nav="/blog/", schema={"@context": "https://schema.org", "@graph": [{"@type": "Blog", "@id": SITE + "/blog/#blog", "name": "Blog Bartier & Co", "url": SITE + "/blog/", "inLanguage": "fr-FR",
                                                                     "publisher": {"@id": SITE + "/#org"}, "blogPost": [{"@id": f"{SITE}/blog/{x['slug']}/#article"} for x in ARTICLES]}, bc_ld(("Blog", "/blog/"))]})
paths.append("/blog/")

def _hero_cta(block, cta):
    """Article pour les propriétaires : le bouton du haut mène au formulaire de devis, pas à l'appel artisan."""
    if not cta:
        return block
    btn = f'<div class="actions"><a class="btn" href="{cta[1]}"><span>{cta[0]}</span><svg class="tick" viewBox="0 0 10 10" aria-hidden="true"><path d="M1 1h8v8" fill="none" stroke="currentColor" stroke-width="1.4"/></svg></a></div>'
    out, n = re.subn(r'<div class="actions">.*?</div>', lambda m: btn, block, count=1, flags=re.S)
    assert n == 1
    return out


ART_ASIDE = """<h3>Votre secteur est-il libre ?</h3>
      <p>Un seul artisan par métier et par secteur.</p>
      <a class="btn" href="https://wa.me/33781018936?text=Bonjour%20Martin%2C%20je%20suis%20artisan%20et%20je%20voudrais%20r%C3%A9server%20un%20appel%20de%2015%20minutes." target="_blank" rel="noopener" data-wa="cta"><span>Réserver un appel</span></a>"""
SEO_TITLE = {"dpe-2027": "DPE 2027 : nouvelle étiquette, location et travaux",
             "lead-partage-lead-exclusif-rendez-vous-qualifie": "Demande partagée, exclusive ou rendez-vous qualifié ?",
             "relance-devis-artisan": "Relance de devis : calendrier, SMS et script d'appel",
             "google-ads-ou-meta-ads-artisan": "Google Ads ou Meta Ads pour un artisan : que choisir ?"}
for a in ARTICLES:
    path = f"/blog/{a['slug']}/"
    meta = f'<p class="post-meta-line"><span>Par <a href="/qui-sommes-nous/#charles">Charles Le Cottier</a>, cofondateur</span><span>Publié le <time datetime="{a.get('date', TODAY)}">{a.get('date_fr', '17 novembre 2026')}</time></span><span>Mis à jour le <time datetime="@@MAJ@@">@@MAJFR@@</time></span><span>{a["minutes"]} min de lecture</span></p>'
    body = "\n\n".join([
        _hero_cta(top(a["tag"], a["title"], "", crumbs(("Blog", "/blog/"), (a["short"], path)), meta=meta, photo=COVER[a["slug"]], dated=False).replace('class="pg-photo frame"', 'class="pg-photo frame is-color"', 1), a.get("cta")),
        f"""<section class="sheet" data-tone="light">
  <div class="grid art-grid">
    <article class="prose">
{label_tables(a['body'])}
    </article>
    <aside class="art-aside">
      {a.get("aside") or ART_ASIDE}
    </aside>
  </div>
</section>""",
        more("À lire aussi", "Tous les articles", "/blog/", [(x["short"], f"/blog/{x['slug']}/") for x in ARTICLES if x["slug"] != a["slug"]]),
    ])
    _w = (lambda *x, nav=None, schema=None: write_plain(*x, schema=schema)) if a.get("cta") else write  # article propriétaires : pas de formulaire artisan
    _w(path, SEO_TITLE.get(a["slug"]) or f"{a['short']} | Bartier & Co", a["desc"], body, nav="/blog/",
          schema={"@context": "https://schema.org", "@graph": [
              {"@type": "BlogPosting", "@id": SITE + path + "#article", "isPartOf": {"@id": SITE + "/blog/#blog"}, "headline": fr(a["title"]), "description": fr(a["desc"]), "datePublished": a.get("date", TODAY) + "T09:00:00+01:00", "dateModified": "@@MAJ@@", "inLanguage": "fr-FR",
               "mainEntityOfPage": SITE + path, "image": [img(COVER[a["slug"]])[0]],
               "author": {"@type": "Person", "@id": SITE + "/qui-sommes-nous/#charles", "name": "Charles Le Cottier", "jobTitle": "Cofondateur", "url": SITE + "/qui-sommes-nous/#charles", "image": portrait("charles")},
               "publisher": dict(ORG_REF, logo={"@type": "ImageObject", "url": SITE + "/assets/logo-bartier.png"}), **({"citation": a["citation"]} if a.get("citation") else {})},
              bc_ld(("Blog", "/blog/"), (a["short"], path))] + ([faq_ld(a["faq"])] if a.get("faq") else [])})
    paths.append(path)

# ——— Guides : comment trouver des chantiers, fiche Habitatpresto Pro (_build/contenu.py) ———
AUTHOR_META = '<p class="post-meta-line"><span>Par <a href="/qui-sommes-nous/#charles">Charles Le Cottier</a>, cofondateur</span></p>'


def _gd_slug(s):
    import unicodedata
    s = unicodedata.normalize("NFKD", re.sub("<[^>]+>", "", s)).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")[:48]


def guide(G, kick, crumb_items, faq_title, links):
    toc = []
    def _h2(m):  # chaque partie reçoit une ancre, reprise dans le sommaire en tête de page
        sid = _gd_slug(m.group(1))
        toc.append((sid, re.sub("<[^>]+>", "", m.group(1)).rstrip(" ?")))
        return f'<h2 id="{sid}">{m.group(1)}</h2>'
    art = re.sub(r"<h2>(.*?)</h2>", _h2, label_tables(G['body']))
    toc_html = ('<nav class="gd-toc" aria-label="Dans ce guide"><p class="gd-toc-k">Dans ce guide</p><ol>'
                + "".join(f'<li><a href="#{i}">{x}</a></li>' for i, x in toc) + "</ol></nav>")
    body = "\n\n".join([
        top(kick, G["h1"], G["lead"], crumbs(*crumb_items), visual=toc_html,
            meta='<p class="post-meta-line"><span>Par <a href="/qui-sommes-nous/#charles">Charles Le Cottier</a>, cofondateur</span><span>Mis à jour le <time datetime="@@MAJ@@">@@MAJFR@@</time></span></p>'),
        f"""<section class="sheet gd-body" data-tone="light">
  <div class="grid art-grid">
    <article class="prose">
{art}
    </article>
    <aside class="art-aside">
      <h3>Votre secteur est-il libre ?</h3>
      <p>Un seul artisan par métier et par secteur. Visites déjà fixées, sans durée d'engagement.</p>
      <a class="btn" href="https://wa.me/33781018936?text=Bonjour%20Martin%2C%20je%20suis%20artisan%20et%20je%20voudrais%20r%C3%A9server%20un%20appel%20de%2015%20minutes." target="_blank" rel="noopener" data-wa="cta"><span>Réserver un appel</span></a>
    </aside>
  </div>
</section>""",
        faq(G["faq"], title=faq_title),
        more("À lire aussi", "Tous les articles", "/blog/", links),
    ])
    write(G["path"], G["title"], G["desc"], body, nav=None,
          schema={"@context": "https://schema.org", "@graph": [
              {"@type": "Article", "headline": fr(G["h1"]), "description": fr(G["desc"]), "datePublished": "2026-11-18", "dateModified": "@@MAJ@@",
               "inLanguage": "fr-FR", "mainEntityOfPage": SITE + G["path"], "image": [SITE + "/assets/og.png"],
               "author": {"@type": "Person", "@id": SITE + "/qui-sommes-nous/#charles", "name": "Charles Le Cottier", "jobTitle": "Cofondateur", "url": SITE + "/qui-sommes-nous/#charles", "image": portrait("charles")},
               "publisher": dict(ORG_REF, logo={"@type": "ImageObject", "url": SITE + "/assets/logo-bartier.png"})},
              faq_ld(G["faq"]), bc_ld(*crumb_items)]})
    paths.append(G["path"])


_art = {x["slug"]: (x["short"], f"/blog/{x['slug']}/") for x in ARTICLES}
# ——— Trouver des chantiers : page courte et visuelle (8 cartes, un calcul, 4 pertes, notre approche, 4 questions) ———
WA_BOOK = "https://wa.me/33781018936?text=Bonjour%20Martin%2C%20je%20suis%20artisan%20et%20je%20voudrais%20r%C3%A9server%20un%20appel%20de%2015%20minutes."
TICK_SVG = '<svg class="tick" viewBox="0 0 10 10" aria-hidden="true"><path d="M1 1h8v8" fill="none" stroke="currentColor" stroke-width="1.4"/></svg>'
TC_CHANNELS = [  # nom, ce que vous payez, ce qu'il faut, la demande (ok : pour vous seul / part : partagée / mix : ça dépend)
    ("Bouche-à-oreille", "Du temps", "Des clients contents", "ok", ""),
    ("Fiche Google", "Gratuit", "Des photos et des avis", "mix", "Comparée à d'autres fiches"),
    ("Plateformes de devis", "Un abonnement ou un prix par demande", "Rappeler très vite", "part", "Souvent partagée"),
    ("Apporteur d'affaires", "Une commission sur le chantier", "Un contrat écrit", "mix", "Selon le contrat"),
    ("Sous-traitance", "Une marge plus faible", "Un réseau d'entreprises générales", "ok", ""),
    ("Annonces locales", "Le budget publicitaire et la gestion", "Un rappel rapide", "ok", ""),
    ("Flyers et panneaux", "L'impression et la distribution", "Des chantiers dans le quartier", "ok", ""),
    ("Réseaux professionnels", "Une cotisation et du temps", "Une présence régulière", "ok", ""),
]
FTR_DD_JS = """<script id="ftr-dd">(function(){var dd=[].slice.call(document.querySelectorAll(".ftr-dd"));if(!dd.length)return;
var still=window.matchMedia("(prefers-reduced-motion: reduce)").matches,ease="cubic-bezier(.22,1,.36,1)",zero={height:"0px",paddingTop:"0px",paddingBottom:"0px",opacity:0};function full(l){var c=getComputedStyle(l);return{height:l.scrollHeight+"px",paddingTop:c.paddingTop,paddingBottom:c.paddingBottom,opacity:1}}function run(l,a,b,ms,done){if(l._a){l._a.cancel();l._a=null}var x=l.animate([a,b],{duration:ms,easing:ease,fill:"forwards"});l._a=x;x.onfinish=function(){if(done)done();x.cancel();if(l._a===x)l._a=null}}function open(d,l,show){if(l._a){l._a.cancel();l._a=null}d.open=true;if(still||!l.animate){if(show)show();return}run(l,zero,full(l),240,show)}function shut(d,l,now){if(!d.open)return;if(now||still||!l.animate){if(l._a){l._a.cancel();l._a=null}d.open=false;return}run(l,full(l),zero,180,function(){d.open=false})}
var mq=window.matchMedia("(max-width: 760px)");function sync(){dd.forEach(function(d){d.open=!mq.matches})}sync();if(mq.addEventListener)mq.addEventListener("change",sync);
dd.forEach(function(d){var s=d.querySelector("summary"),l=d.querySelector(".ftr-links");function show(){var r=l.getBoundingClientRect(),over=r.bottom-(innerHeight-16);if(over>0)window.scrollBy({top:over,behavior:still?"auto":"smooth"})}s.addEventListener("click",function(e){e.preventDefault();if(!mq.matches)return;if(d.open)shut(d,l);else open(d,l,show)})})})();</script>"""


MENU_DD_JS = """<script id="menu-dd">(function(){var dd=[].slice.call(document.querySelectorAll(".menu-dd"));if(!dd.length)return;
var still=window.matchMedia("(prefers-reduced-motion: reduce)").matches,ease="cubic-bezier(.22,1,.36,1)",zero={height:"0px",paddingTop:"0px",paddingBottom:"0px",opacity:0};function full(l){var c=getComputedStyle(l);return{height:l.scrollHeight+"px",paddingTop:c.paddingTop,paddingBottom:c.paddingBottom,opacity:1}}function run(l,a,b,ms,done){if(l._a){l._a.cancel();l._a=null}var x=l.animate([a,b],{duration:ms,easing:ease,fill:"forwards"});l._a=x;x.onfinish=function(){if(done)done();x.cancel();if(l._a===x)l._a=null}}function open(d,l,show){if(l._a){l._a.cancel();l._a=null}d.open=true;if(still||!l.animate){if(show)show();return}run(l,zero,full(l),240,show)}function shut(d,l,now){if(!d.open)return;if(now||still||!l.animate){if(l._a){l._a.cancel();l._a=null}d.open=false;return}run(l,full(l),zero,180,function(){d.open=false})}
var m=document.getElementById("menu");dd.forEach(function(d){var s=d.querySelector("summary"),l=d.querySelector(".menu-dd-list");function show(){if(!m)return;var r=l.getBoundingClientRect(),b=m.getBoundingClientRect(),over=r.bottom-(b.bottom-16);if(over>0)m.scrollBy({top:over,behavior:still?"auto":"smooth"})}s.addEventListener("click",function(e){e.preventDefault();if(d.open){shut(d,l);return}dd.forEach(function(o){if(o!==d)shut(o,o.querySelector(".menu-dd-list"),true)});open(d,l,show)})})})();</script>"""


TC_CALC_JS = r'''<script>(function(){var g=function(i){return document.getElementById(i)},d=g('tc-d'),s=g('tc-s'),m=g('tc-m'),r=g('tc-r'),q=g('tc-p');if(!d)return;
var n=function(e){var v=e.value.replace(/[^0-9,.]/g,'').replace(',','.');return v===''?NaN:parseFloat(v)},f=function(x){return new Intl.NumberFormat('fr-FR',{maximumFractionDigits:0}).format(x)};
function run(){var a=n(d),b=n(s),c=n(m);if(!(a>=0)||!(b>0)){r.textContent='—';q.textContent=b===0?'Ajoutez au moins un chantier signé':'';return}
var k=a/b;r.textContent=f(k)+'\u00a0€';q.textContent=c>0?(k>=c?'soit plus que votre marge sur un chantier':'soit '+f(k/c*100)+'\u00a0% de votre marge'):''}
[d,s,m].forEach(function(e){e.addEventListener('input',run)});run()})();</script>'''


def pillar_page(G):
    def _row(i, n, c, w, k, lab):
        us = n == "Annonces locales"
        dem = '<span class="tc-solo">Pour vous seul</span>' if k == "ok" else f'<span class="tc-mk is-{k}">{lab}</span>'
        tag = '<span class="tc-us-tag">Notre métier</span>' if us else ""
        return (f'      <tr{" class=\"is-us\"" if us else ""}><th scope="row"><span class="tc-n">{i:02d}</span>{n}{tag}</th>'
                f'<td data-l="Coût">{c}</td><td data-l="Il faut">{w}</td><td class="tc-dem">{dem}</td></tr>')
    rows = "\n".join(_row(i, *ch) for i, ch in enumerate(TC_CHANNELS, 1))
    loss = [("Le rappel tardif", "Rappelé le soir, le propriétaire a pu parler à un concurrent."),
            ("La visite inutile", "Un locataire, un projet dans trois ans, une commune hors zone."),
            ("Le devis envoyé tard", "Entre-temps, le propriétaire a reçu d'autres devis."),
            ("Le devis jamais relancé", 'Un appel et un SMS suffisent souvent. <a class="link" href="/blog/relance-devis-artisan/">La méthode</a>')]
    loss_html = "\n".join(f'    <li><span class="tc-n">{i:02d}</span><h3>{h}</h3><p>{p}</p></li>' for i, (h, p) in enumerate(loss, 1))
    def slip(k, d, n, per, s, rate, res, win=False):
        return (f'<article class="tc-slip{" is-win" if win else ""}"><header><p class="tc-slip-k">{k}</p><p class="tc-slip-sub">Sur un mois</p></header><dl>'
                f'<div><dt>Dépensé</dt><dd>{d}</dd></div><div><dt>Demandes reçues</dt><dd>{n}</dd></div>'
                f'<div><dt>Prix d\'une demande</dt><dd>{per}</dd></div><div><dt>Chantiers signés</dt><dd>{s}</dd></div>'
                f'<div class="is-rate"><dt>Demandes signées</dt><dd>{rate}</dd></div></dl>'
                f'<p class="tc-slip-tot"><span>Coût par chantier signé</span><b>{res}</b>'
                + ('<small class="tc-win">Le moins cher par chantier signé</small>' if win else "") + "</p></article>")
    trades = " · ".join(f'<a class="link" href="/metiers/{sl}/">{lb}</a>' for lb, sl in [("Couverture", "couverture"), ("Façade", "facade"), ("Menuiserie", "menuiserie-exterieure"), ("Charpente", "charpente"), ("Isolation", "isolation")])
    faq_items = [G["faq"][i] for i in (0, 1, 3, 5)]
    body = "\n\n".join([
        top("Guide", G["h1"], "Huit façons de trouver des chantiers, comparées. La bonne est celle qui vous coûte le moins par chantier signé.",
            crumbs(("Trouver des chantiers", G["path"])), "Un menuisier pose une fenêtre",
            meta='<p class="post-meta-line"><span>Par <a href="/qui-sommes-nous/#charles">Charles Le Cottier</a>, cofondateur</span><span>Mis à jour le <time datetime="@@MAJ@@">@@MAJFR@@</time></span></p>'),
        f"""<section class="sheet tc-sec" id="canaux" data-tone="light">
  <div class="grid sp-head"><h2 data-split>Les 8 canaux pour trouver des chantiers</h2><p>Ce que chacun vous coûte, et si la demande est pour vous seul.</p></div>
  <table class="tc-table">
    <thead><tr><th scope="col">Canal</th><th scope="col">Ce que vous payez</th><th scope="col">Ce qu'il faut</th><th scope="col">La demande</th></tr></thead>
    <tbody>
{rows}
    </tbody>
  </table>
  <p class="tc-foot">Plateformes : lisez leurs conditions avant de signer. Exemple : <a class="link" href="/trouver-des-chantiers/habitatpresto-pro/">Habitatpresto Pro</a>.</p>
</section>""",
        f"""<section class="sheet tc-sec" id="calcul-cout" data-tone="paper">
  <div class="grid sp-head"><h2 data-split>Comment calculer le coût par chantier signé ?</h2><p>Additionnez ce que le canal vous a coûté, puis divisez par les chantiers signés grâce à lui.</p></div>
  <p class="tc-formula">Dépenses du canal ÷ chantiers signés = <b>coût par chantier signé</b></p>
  <div class="tc-ab">
    {slip("Demandes partagées", "400 €", "40", "10 €", "2", "1 sur 20", "200 €")}
    {slip("Demandes pour vous seul", "900 €", "12", "75 €", "6", "1 sur 2", "150 €", True)}
    <div class="tc-calc" id="calculateur" role="group" aria-labelledby="tc-calc-k">
      <p class="tc-calc-k" id="tc-calc-k">Faites le calcul avec vos chiffres</p>
      <div class="tc-calc-f">
        <label for="tc-d"><span>Dépensé sur le mois</span><span class="tc-in"><input id="tc-d" inputmode="numeric" autocomplete="off" value="1 200"><i>€</i></span></label>
        <label for="tc-s"><span>Chantiers signés</span><span class="tc-in"><input id="tc-s" inputmode="numeric" autocomplete="off" value="4"></span></label>
        <label for="tc-m"><span>Votre marge sur un chantier</span><span class="tc-in"><input id="tc-m" inputmode="numeric" autocomplete="off" value="3 000"><i>€</i></span></label>
      </div>
      <p class="tc-calc-r"><span>Votre coût par chantier signé</span><output id="tc-r" for="tc-d tc-s" aria-live="polite">300 €</output><small id="tc-p">soit 10 % de votre marge</small></p>
    </div>
  </div>
  <p class="tc-foot is-calc">Chiffres d'exemple, pas des moyennes.</p>
</section>""",
        f"""<section class="sheet tc-sec" id="pertes" data-tone="light">
  <div class="grid sp-head"><h2 data-split>Où se perdent les chantiers ?</h2><p>Après la demande, quatre moments font perdre le chantier.</p></div>
  <ol class="tc-loss">
{loss_html}
  </ol>
  <aside class="tc-law"><p class="tc-law-k">Depuis le 11 août 2026</p><p>Appeler un particulier pour lui proposer des travaux demande son accord préalable. Pour la rénovation énergétique, c'est interdit. Rappeler quelqu'un qui l'a demandé reste possible, avec la preuve de sa demande.</p>
    <p class="tc-src">Sources : <a href="https://www.cnil.fr/fr/prospection-commerciale-par-telephone-hors-automate-dappel-quelles-sont-les-regles" target="_blank" rel="noopener">CNIL</a>, <a href="https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069565/LEGISCTA000032221441/2026-08-11" target="_blank" rel="noopener">Code de la consommation, L223-1</a>. <a href="/lexique/#demarchage-telephonique">Définition</a></p></aside>
</section>""",
        f"""<section class="sheet tc-us" id="approche" data-tone="dark">
  <div class="grid tc-us-grid">
    <h2 data-split>Notre approche</h2>
    <div class="tc-us-txt">
      <p>Nous combinons les annonces locales et le rappel de chaque demande client en moins de 5 minutes. La visite arrive dans votre agenda. Un seul artisan par métier et par secteur.</p>
      <p>Le bouche-à-oreille reste votre premier canal. Nous vous apportons des demandes en plus, sans durée d'engagement.</p>
      <div class="actions"><a class="btn" href="{WA_BOOK}" target="_blank" rel="noopener" data-wa="cta"><span>Réserver un appel</span>{TICK_SVG}</a><a class="link" href="/#services">Voir comment ça marche</a></div>
      <p class="tc-trades">Par métier : {trades}</p>
    </div>
  </div>
</section>""",
        faq(faq_items, title="Vos questions sur la recherche de chantiers"),
        more("À lire aussi", "Tous les articles", "/blog/", [_art["google-ads-ou-meta-ads-artisan"], _art["relance-devis-artisan"], _art["lead-partage-lead-exclusif-rendez-vous-qualifie"], ("Lexique des chantiers et des travaux", "/lexique/")]),
    ])
    write(G["path"], G["title"], G["desc"], body, nav=None, form_after=5,
          schema={"@context": "https://schema.org", "@graph": [
              {"@type": "Article", "headline": fr(G["h1"]), "description": fr(G["desc"]), "datePublished": "2026-11-18", "dateModified": "@@MAJ@@",
               "inLanguage": "fr-FR", "mainEntityOfPage": SITE + G["path"], "image": [img("Un menuisier pose une fenêtre")[0]],
               "author": {"@type": "Person", "@id": SITE + "/qui-sommes-nous/#charles", "name": "Charles Le Cottier", "jobTitle": "Cofondateur", "url": SITE + "/qui-sommes-nous/#charles"},
               "publisher": dict(ORG_REF, logo={"@type": "ImageObject", "url": SITE + "/assets/logo-bartier.png"})},
              faq_ld(faq_items), bc_ld(("Trouver des chantiers", G["path"]))]})
    paths.append(G["path"])
pillar_page(CT.PILLAR)
guide(CT.HP, "Plateforme de devis", [("Trouver des chantiers", CT.PILLAR["path"]), ("Habitatpresto Pro", CT.HP["path"])], "Habitatpresto Pro : vos questions",
      [("Comment trouver des chantiers : 8 canaux comparés", CT.PILLAR["path"]), _art["lead-partage-lead-exclusif-rendez-vous-qualifie"], ("Lexique des chantiers et des travaux", "/lexique/")])

# ——— Pages légales : _build/legal/<slug>.html (fragment HTML, métadonnées JSON en commentaire sur la première ligne) ———
# Informations de la société encore inconnues : à renseigner ici dès qu'elles existent. Une information vide s'affiche « à compléter ».
COMPANY = {"SIREN": "", "RCS_VILLE": "", "CAPITAL": "", "TVA": "", "DIRECTEUR_PUBLICATION": "", "MEDIATEUR": "", "TEL_HEBERGEUR": "+1 559 288 7060"}
TOKEN_LABEL = {"SIREN": "numéro SIREN", "RCS_VILLE": "ville du greffe", "CAPITAL": "montant du capital", "TVA": "numéro de TVA",
               "DIRECTEUR_PUBLICATION": "nom du directeur de la publication", "MEDIATEUR": "nom et coordonnées du médiateur", "TEL_HEBERGEUR": "numéro de téléphone"}
MONTHS = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre", "décembre"]
legal_missing = set()
# Société en cours d'immatriculation (novembre 2026) : phrases d'attente, retirées d'elles-mêmes quand COMPANY est rempli
EN_FORMATION = True
PENDING = [
    ("SIREN", "<li>Immatriculation : registre du commerce et des sociétés de {{RCS_VILLE}}, numéro {{SIREN}}</li>",
     "<li>Immatriculation : en cours au registre du commerce et des sociétés. Le numéro SIREN figurera ici dès son attribution.</li>"),
    ("CAPITAL", "<li>Forme : société par actions simplifiée (SAS) au capital de {{CAPITAL}}</li>",
     "<li>Forme : société par actions simplifiée (SAS), en cours d’immatriculation</li>"),
    ("TVA", "<li>TVA intracommunautaire : {{TVA}}</li>", "<li>TVA intracommunautaire : attribuée à l’immatriculation</li>"),
    ("DIRECTEUR_PUBLICATION", '<h2 id="publication">Directeur de la publication</h2>\n<p>{{DIRECTEUR_PUBLICATION}}, représentant légal de Bartier & Co.</p>',
     '<h2 id="publication">Directeurs de la publication</h2>\n<p>Charles Le Cottier et Martin Barthélémy, cofondateurs de Bartier & Co.</p>'),
    ("MEDIATEUR", "vous pouvez saisir gratuitement le médiateur de la consommation : {{MEDIATEUR}}.",
     "vous pourrez saisir gratuitement le médiateur de la consommation : son nom et ses coordonnées figureront ici dès l’adhésion de Bartier & Co, en cours."),
]


def legal_fill(frag):
    if EN_FORMATION:
        for k, old, new in PENDING:
            if not COMPANY.get(k) and old in frag:
                frag = frag.replace(old, new)
                legal_missing.add(k)
    def tok(m):
        k = m.group(1)
        if COMPANY.get(k):
            return html.escape(COMPANY[k])
        legal_missing.add(k)
        return f'<mark class="todo">{TOKEN_LABEL.get(k, k)} à compléter</mark>'
    frag = re.sub(r"\{\{([A-Z_]+)\}\}", tok, frag)
    def table(m):  # chaque cellule porte le titre de sa colonne : sur téléphone le tableau devient une liste
        heads = [re.sub(r"<[^>]+>", "", h) for h in re.findall(r"<th>(.*?)</th>", m.group(0), flags=re.S)]
        def row(r):
            cells = iter(heads)
            return re.sub(r"<td>", lambda c: f'<td data-label="{html.escape(next(cells, ""))}">', r.group(0))
        return re.sub(r"<tr>(?:(?!</tr>).)*</tr>", row, m.group(0), flags=re.S)
    return re.sub(r"<table>.*?</table>", table, frag, flags=re.S)


LEGAL_NAV = [(s, json.loads(re.match(r"<!--\s*(\{.*?\})\s*-->", (ROOT / "_build" / "legal" / f"{s}.html").read_text(encoding="utf-8")).group(1))) for s in LEGAL_READY]
for slug, meta in LEGAL_NAV:
    raw = (ROOT / "_build" / "legal" / f"{slug}.html").read_text(encoding="utf-8")
    frag = legal_fill(raw[raw.index("-->") + 3:].strip())
    path = f"/{slug}/"
    y, mth, d = meta["updated"].split("-")
    others = "".join(f'<a href="/{s}/"{" aria-current=\"page\"" if s == slug else ""}>{m["title"].replace(" pour les particuliers", "")}</a>' for s, m in LEGAL_NAV)
    body = f"""<section class="sheet pg-top lg-top" data-tone="light">
  <div class="grid pg-grid">
    <div class="pg-text">
      {crumbs((meta["title"], path))}
      <p class="kick">Informations légales</p>
      <h1>{meta["title"]}</h1>
      <p class="post-meta-line"><span>Mise à jour le <time datetime="{meta["updated"]}">{int(d)} {MONTHS[int(mth) - 1]} {y}</time></span></p>
      <nav class="lg-nav" aria-label="Pages légales">{others}</nav>
    </div>
  </div>
</section>

<section class="sheet lg" data-tone="light">
  <div class="grid">
    <div class="prose lg-prose">
{frag}
    </div>
  </div>
</section>"""
    write_plain(path, f'{meta["title"]} | Bartier & Co', meta["description"], body,
                schema={"@context": "https://schema.org", "@graph": [{"@type": "WebPage", "name": fr(meta["title"]), "url": SITE + path, "inLanguage": "fr-FR", "dateModified": meta["updated"], "isPartOf": {"@id": SITE + "/#website"}}, bc_ld((meta["title"], path))]})
    paths.append(path)
if legal_missing:
    print("Pages légales : informations à compléter :", ", ".join(sorted(legal_missing)))

# ——— Lexique : définitions courtes et autonomes, sources officielles (_build/lexique.py) ———
import lexique as LX


def lx_items(items):
    out = []
    for slug, term, definition, links, srcs in items:
        more = []
        if links:
            more.append("Voir aussi : " + ", ".join(f'<a href="{h}">{t}</a>' for h, t in links))
        if srcs:
            more.append("Source : " + ", ".join(f'<a href="{LX.SRC[k][1]}" target="_blank" rel="noopener">{LX.SRC[k][0]}</a>' for k in srcs))
        more_html = f'<p class="lx-more">{" · ".join(more)}</p>' if more else ""
        out.append(f'      <div class="lx-item" id="{slug}"><h3>{term}</h3><p>{definition}</p>{more_html}</div>')
    return "\n".join(out)


LX_UPDATED = "2026-11-18"
lx_body = "\n\n".join([
    top("Lexique", "Lexique des chantiers et des travaux",
        "Les mots que croisent artisans et propriétaires, expliqués en deux ou trois phrases, avec la source officielle quand elle existe.",
        crumbs(("Lexique", "/lexique/")), dated=True),
    f"""<section class="sheet lx" id="clients" data-tone="light">
  <div class="grid sp-split">
    <div><h2 data-split>Trouver des clients</h2><p>Pour les artisans du bâtiment : demandes, rendez-vous, coûts et règles d'appel.</p></div>
    <div class="lx-list">
{lx_items(LX.CLIENTS)}
    </div>
  </div>
</section>""",
    f"""<section class="sheet lx" id="travaux" data-tone="paper">
  <div class="grid sp-split">
    <div><h2 data-split>Travaux, garanties et règles</h2><p>Pour les propriétaires, et pour les artisans qui leur répondent.</p></div>
    <div class="lx-list">
{lx_items(LX.TRAVAUX)}
    </div>
  </div>
</section>""",
    more("Passer à l'action", "Toutes les questions fréquentes", "/questions/", [("Vous êtes artisan : vérifier si votre secteur est libre", "/#contact"), ("Vous êtes propriétaire : décrire vos travaux", "/devis-travaux/")]),
])
_lx_clean = lambda s: re.sub("<[^>]+>", "", fr(s))
write_plain("/lexique/", "Lexique des chantiers et des travaux | Bartier & Co",
            "Définitions claires pour artisans et particuliers : demande de devis, rendez-vous qualifié, garantie décennale, déclaration préalable, RGE, démarchage.",
            lx_body.replace('href="#contact"', 'href="/#contact"'),
            schema={"@context": "https://schema.org", "@graph": [
                {"@type": "DefinedTermSet", "@id": SITE + "/lexique/#lexique", "name": "Lexique des chantiers et des travaux", "url": SITE + "/lexique/",
                 "inLanguage": "fr-FR", "dateModified": "@@MAJ@@", "publisher": ORG_REF,
                 "hasDefinedTerm": [{"@type": "DefinedTerm", "@id": f"{SITE}/lexique/#{s}", "name": _lx_clean(t), "description": _lx_clean(d),
                                     "url": f"{SITE}/lexique/#{s}", "inDefinedTermSet": {"@id": SITE + "/lexique/#lexique"}} for s, t, d, _, _ in LX.CLIENTS + LX.TRAVAUX]},
                bc_ld(("Lexique", "/lexique/"))]})
paths.append("/lexique/")

# ——— Page 404 ———
nf_body = """<section class="sheet pg-top" data-tone="light">
  <div class="grid pg-grid">
    <div class="pg-text">
      <p class="kick">Erreur 404</p>
      <h1>Cette page n’existe pas.</h1>
      <p class="lead">Vous êtes propriétaire ou artisan ? Voici par où continuer.</p>
      <div class="actions"><a class="btn" href="/devis-travaux/"><span>Obtenir mon devis gratuit</span></a><a class="link" href="https://wa.me/33781018936?text=Bonjour%20Martin%2C%20je%20suis%20artisan%20et%20je%20voudrais%20r%C3%A9server%20un%20appel%20de%2015%20minutes." target="_blank" rel="noopener">Réserver un appel</a></div>
    </div>
  </div>
</section>"""
nf = head("Page introuvable | Bartier & Co", "Cette page n'existe pas.", "/404.html") + absolutize(BODY_OPEN) + "\n" + fr(nf_body) + "\n" + absolutize(TAIL)
nf = nf.replace('href="#contact"', 'href="/#contact"')
nf = re.sub(r'<link rel="canonical"[^>]*>\n?', "", nf)
(ROOT / "404.html").write_text(nf, encoding="utf-8")

# ——— Passe finale sur toutes les pages : images différées et hébergées chez nous, une seule balise robots ———
import images as IMG


def real_dims(m):
    """Les attributs width et height d'une photo sont ceux du fichier servi (son nom les porte)."""
    tag = m.group(0)
    s = re.search(r'\ssrc="/assets/photos/[\w.-]+?-(\d+)x(\d+)(?:-nb|-brut)?\.webp"', tag)
    if not s or ' width="' not in tag or ' height="' not in tag:
        return tag
    tag = re.sub(r'\swidth="\d+"', f' width="{s.group(1)}"', tag, count=1)
    return re.sub(r'\sheight="\d+"', f' height="{s.group(2)}"', tag, count=1)


def typo(doc):
    """Typographie française dans le texte visible : espace insécable avant ; : ? ! » et après «."""
    parts = re.split(r"(<script[\s\S]*?</script>|<style[\s\S]*?</style>|<textarea[\s\S]*?</textarea>|<!--[\s\S]*?-->|<[^>]+>)", doc)
    for i in range(0, len(parts), 2):
        if parts[i].strip():
            parts[i] = re.sub(r" ([;:?!»])", r"&nbsp;\1", parts[i]).replace("« ", "«&nbsp;").replace("'", "’")
            parts[i] = re.sub(r"(\d) (h|min|minutes|heures|jours|km|ans|mois|%|€)(?![\w])", r"\1&nbsp;\2", parts[i])
    return "".join(parts)


# ——— Vitesse ———
import csspurge as CSSPURGE
_CONSENT_JS = (ROOT / "assets" / "js" / "consent.js").read_text(encoding="utf-8")


_INL = r"(?:a|span|button|b|small|strong|em|time|label|mark|output)"
_GLUE = re.compile(r"(</" + _INL + r">)(?=<" + _INL + r"\b)")
_INL2 = r"(?:span|b|small|strong|em|time|mark|label|output)"
_GLUE_IN = re.compile(r"([\wÀ-ÿ.?!:;)€%»])(<" + _INL2 + r"\b[^>]*>)(?=[\wÀ-ÿ0-9«(€%])")
_GLUE_OUT = re.compile(r"([\wÀ-ÿ.?!:;)€%»]</" + _INL2 + r">)(?=[\wÀ-ÿ0-9«(])")
def unglue(doc):
    """Deux éléments en ligne collés (« 1 minuteVisite ») : une espace entre eux, pour les lecteurs qui ne voient pas
    la mise en page (robots, lecteurs d'écran). Sans effet à l'écran : ces éléments sont posés en bloc ou en flex."""
    i = doc.find("<body")
    head, body = doc[:i], doc[i:]
    parts = re.split(r"(<(?:script|style|svg|textarea|pre)\b[\s\S]*?</(?:script|style|svg|textarea|pre)>)", body)
    for k in range(0, len(parts), 2):
        parts[k] = _GLUE.sub(r"\1 ", parts[k])
        # mot collé à un élément (« 24–48<small>h</small> », « 01<span>…</span>Bouche-à-oreille ») : une espace de taille nulle,
        # lue par les robots, invisible à l'écran (affichage « contents », corps de 0)
        parts[k] = _GLUE_IN.sub(r'\1<span class="u-sp"> </span>\2', parts[k])
        parts[k] = _GLUE_OUT.sub(r'\1<span class="u-sp"> </span>', parts[k])
    return head + "".join(parts)


def hero_preload(doc):
    """La photo d'en-tête (fetchpriority="high") commence à se charger dès le début de la page, avant les styles."""
    if 'rel="preload" as="image"' in doc:
        return doc
    m = re.search(r'<img\b[^>]*\bfetchpriority="high"[^>]*>', doc)
    if not m:
        return doc
    tag = m.group(0)
    srcset = re.search(r'\ssrcset="([^"]+)"', tag)
    sizes = re.search(r'\ssizes="([^"]+)"', tag)
    src = re.search(r'\ssrc="([^"]+)"', tag)
    if srcset:
        link = f'<link rel="preload" as="image" imagesrcset="{srcset.group(1)}"' + (f' imagesizes="{sizes.group(1)}"' if sizes else "") + ' fetchpriority="high">'
    elif src:
        link = f'<link rel="preload" as="image" href="{src.group(1)}" fetchpriority="high">'
    else:
        return doc
    fonts = list(re.finditer(r'<link rel="preload"[^>]*as="font"[^>]*>\n?', doc))
    i = fonts[-1].end() if fonts else doc.index("</title>") + len("</title>")
    return doc[:i] + link + "\n" + doc[i:]


# Vérification Google Search Console (méthode « fichier HTML ») : fichier fourni par Google, recopié à l'octet près, hors des pages
GOOGLE_VERIFY = "google862e3c481c0cb4c7"
(ROOT / f"{GOOGLE_VERIFY}.html").write_bytes(f"google-site-verification: {GOOGLE_VERIFY}.html".encode())
PAGES_OUT = sorted(f for f in ROOT.rglob("*.html") if not (f.name == "8b-original.html" or f.name.startswith("google") or "_build" in f.parts or "_video" in f.parts))
for f in PAGES_OUT:
    IMG.scan(f.read_text(encoding="utf-8"))
for f in PAGES_OUT:
    doc = f.read_text(encoding="utf-8")
    first = doc.find("<img ", doc.find("<main>") if "<main>" in doc else 0)
    _hm = re.compile(r'<figure class="pg-photo frame[^"]*"><img ').search(doc, max(doc.find('class="sheet pg-top'), 0)) if 'class="sheet pg-top' in doc else None
    hero = _hm.end() - len('<img ') if _hm else -2  # photo d'en-tête des pages intérieures (avec ou sans « is-color »)
    def lazy(m):
        tag = m.group(0)
        if m.start() == hero and "fetchpriority=" not in tag:
            return tag.replace("<img ", '<img fetchpriority="high" ', 1)  # photo d'en-tête des pages intérieures : chargée en premier (LCP)
        if m.start() == first or "loading=" in tag:
            return tag
        return tag.replace("<img ", '<img loading="lazy" decoding="async" ', 1)
    doc = re.sub(r"<img [^>]*>", lazy, doc)
    def srcset(m):
        tag = m.group(0)
        if "srcset=" in tag or "images.unsplash.com" not in tag:
            return tag
        u = re.search(r'src="([^"]+)"', tag).group(1)
        w = re.search(r"[?&](?:amp;)?w=(\d+)", u); h = re.search(r"[?&](?:amp;)?h=(\d+)", u)
        if not w:
            return tag
        W = int(w.group(1)); H = int(h.group(1)) if h else None
        cands = []
        for nw in [480, 800, 1200]:
            if nw < W:
                v = re.sub(r"([?&](?:amp;)?w=)\d+", lambda x: x.group(1) + str(nw), u)
                if H: v = re.sub(r"([?&](?:amp;)?h=)\d+", lambda x: x.group(1) + str(round(H * nw / W)), v)
                cands.append(f"{v} {nw}w")
        cands.append(f"{u} {W}w")
        sz = "" if "sizes=" in tag else ' sizes="(max-width: 760px) 100vw, 50vw"'
        return tag.replace("<img ", f'<img srcset="{", ".join(cands)}"{sz} ', 1)
    doc = re.sub(r"<img [^>]*>", srcset, doc)
    doc = IMG.localize(doc, SITE).replace('<link rel="preconnect" href="https://images.unsplash.com">\n', "")
    doc = re.sub(r"<img [^>]*>", real_dims, doc)
    doc = typo(doc)
    if '<nav class="ftr-col' in doc and 'class="ftr-dd"' not in doc:  # pied de page : groupes de liens repliables sur téléphone (ouverts sur ordinateur)
        doc = re.sub(r'(<nav class="ftr-col[^"]*" aria-label="[^"]*">)\s*<p class="ftr-h">([^<]*)</p>(.*?)\s*</nav>',
                     lambda m: m.group(1) + '<details class="ftr-dd" open><summary class="ftr-h">' + m.group(2) + NAV_CHEV + '</summary><div class="ftr-links">' + m.group(3).strip() + '</div></details></nav>', doc, flags=re.S)
        doc = doc.replace("</body>", FTR_DD_JS + "\n</body>", 1)
    if 'class="menu-dd"' in doc and 'id="menu-dd"' not in doc:  # menu téléphone : sous-listes qui glissent
        doc = doc.replace("</body>", MENU_DD_JS + "\n</body>", 1)
    if 'id="calculateur"' in doc and 'id="tc-js"' not in doc:  # calculateur : script ajouté après la typo, qui changerait ses apostrophes
        doc = doc.replace("</body>", TC_CALC_JS.replace("<script>", '<script id="tc-js">', 1) + "\n</body>", 1)
    if 'id="wa"' in doc and "wa-mini" not in doc:  # bulle WhatsApp : réduite à l'icône une fois la page entamée, pour ne rien cacher
        doc = doc.replace("</body>", '<script id="wa-mini">(function(){var w=document.getElementById("wa");if(!w)return;var f=function(){w.classList.toggle("is-mini",scrollY>innerHeight*1.1)};addEventListener("scroll",f,{passive:true});f()})();</script>\n</body>', 1)
    if 'class="hdr-dd"' in doc and 'id="dd-js"' not in doc:
        doc = doc.replace("</body>", DD_JS + "\n</body>", 1)
    if f != ROOT / "index.html":
        doc = doc.replace('aria-label="Bartier &amp; Co, retour en haut"', 'aria-label="Bartier &amp; Co, accueil"')
    if "<main>" in doc and 'class="skip"' not in doc:  # clavier : aller directement au contenu
        doc = doc.replace("<main>", '<main id="contenu" tabindex="-1"' + ('' if f == ROOT / "index.html" else ' class="is-inner"') + '>', 1)  # is-inner : réglages téléphone des pages intérieures (l'accueil garde les siens)
        doc = re.sub(r"(<body[^>]*>)", r'\1\n<a class="skip" href="#contenu">Aller au contenu</a>', doc, count=1)
    _parts = doc.split('<div class="fq-list">')  # Microsoft : ne pas cacher les réponses importantes
    doc = _parts[0] + "".join('<div class="fq-list">' + s.replace('<details class="fq">', '<details class="fq" open>', 2) for s in _parts[1:])
    _rel = f.relative_to(ROOT)
    _page = "/" + ("" if str(_rel.parent) == "." else str(_rel.parent) + "/")
    if 'name="theme-color"' not in doc:
        doc = doc.replace("</title>", '</title>\n<meta name="theme-color" content="#ffffff">', 1)
    for slug in LEGAL_SLUGS:  # pas de lien vers une page légale qui n'existe pas encore
        if slug not in LEGAL_READY:
            doc = re.sub(rf'\s*<a href="/{slug}/">[^<]*</a>', "", doc)
    rob = '<meta name="robots" content="noindex">'
    if LIVE and _page not in REVIEW and f.name != "404.html":  # en ligne (la page 404 reste toujours hors index) : indexation et extraits longs autorisés (moteurs de réponse)
        doc = doc.replace(rob, '<meta name="robots" content="max-snippet:-1, max-image-preview:large, max-video-preview:-1">', 1).replace(rob + "\n", "").replace(rob, "")
    if doc.count(rob) > 1:
        i = doc.index(rob) + len(rob)
        doc = doc[:i] + doc[i:].replace(rob + "\n", "").replace(rob, "")
    if re.fullmatch(r"/blog/[^/]+/", _page):
        doc = doc.replace('<meta property="og:type" content="website">', f'<meta property="og:type" content="article">\n<meta property="article:published_time" content="{TODAY}T09:00:00+01:00">', 1)
    doc = doc.replace('alt="Une chargée de rappel au téléphone"', 'alt="Appel de relance d’un devis"')
    doc = re.sub(r'alt="Isolation d(?:&#39;|&#x27;|\'|’)un mur par l(?:&#39;|&#x27;|\'|’)extérieur"', 'alt="Maison ancienne aux murs extérieurs rénovés"', doc)  # la photo montre une façade rénovée
    doc = re.sub(r'(<meta (?:name="description"|property="og:(?:title|description|image:alt)"|name="twitter:[a-z]+") content=")([^"]*)(")',
                 lambda m: m.group(1) + re.sub(r" ([:;?!»])", "\u00a0\\1", m.group(2)).replace("« ", "«\u00a0") + m.group(3), doc)
    doc = re.sub(r'\b(alt|aria-label|title|placeholder|data-label)="([^"]*)"', lambda m: f'{m.group(1)}="' + re.sub(r"(?<=[A-Za-zÀ-ÿ])(&#39;|&#x27;|')(?=[A-Za-zÀ-ÿ])", "’", m.group(2)) + '"', doc)
    doc = unglue(doc)
    # Vitesse : les bibliothèques d'animation ne bloquent plus l'affichage (defer) ; le script qui les utilise attend l'analyse de la page
    if '<script src="/assets/js/gsap.min.js"></script>' in doc:
        for _lib in ("gsap.min.js", "ScrollTrigger.min.js", "SplitText.min.js"):
            doc = doc.replace(f'<script src="/assets/js/{_lib}"></script>\n', "").replace(f'<script src="/assets/js/{_lib}"></script>', "")
        _i = doc.find("<script>(()=>{const $=(s,r=document)")
        if _i > 0:
            _j = doc.index("</script>", _i)
            _mq = '"(prefers-reduced-motion:no-preference)"' if 'class="hero-pin' in doc else '"(min-width:1025px) and (prefers-reduced-motion:no-preference)"'
            doc = doc[:_i + 8] + ANIM_OPEN + doc[_i + 8:_j] + ANIM_CLOSE.replace("__MQ__", _mq) + doc[_j:]
    # pages Google Ads et Meta Ads : l'image de fond de la maquette est le plus grand élément du haut de page
    if 'fetchpriority="high"' not in doc and 'class="mk-bg"' in doc:
        doc = re.sub(r'<img\b([^>]*class="mk-bg")', r'<img fetchpriority="high"\1', doc, count=1)
    doc = hero_preload(doc)
    doc = CSSPURGE.purge_doc(doc, _CONSENT_JS)  # vitesse : chaque page ne garde que le CSS qui peut la toucher
    f.write_text(doc, encoding="utf-8")

# ——— Sécurité : politique de contenu (CSP) ———
# Rien d'extérieur n'est chargé tant qu'aucun identifiant de mesure n'est configuré (TAGS). Si un identifiant Google ou Meta
# est ajouté, ses adresses sont autorisées ici automatiquement (le bandeau cookies ne les charge qu'après accord).
_G = bool(TAGS.get("ga4") or TAGS.get("gads"))
_M = bool(TAGS.get("meta"))
CSP_SCRIPT = ["'self'"] + (["https://www.googletagmanager.com", "https://www.googleadservices.com", "https://googleads.g.doubleclick.net"] if _G else []) + (["https://connect.facebook.net"] if _M else [])
_CSP_NET = (["https://*.google-analytics.com", "https://*.analytics.google.com", "https://*.googletagmanager.com", "https://www.google.com",
             "https://*.g.doubleclick.net", "https://www.googleadservices.com"] if _G else []) + (["https://www.facebook.com", "https://connect.facebook.net"] if _M else [])
CSP_HEADER = "; ".join([
    "default-src 'self'",
    "script-src " + " ".join(CSP_SCRIPT + ["'unsafe-inline'"]),  # resserré page par page par les empreintes (balise meta)
    "style-src 'self' 'unsafe-inline'",
    "img-src " + " ".join(["'self'", "data:"] + _CSP_NET + (["https://www.google.fr"] if _G else [])),
    "font-src 'self' data:",
    "connect-src " + " ".join(["'self'"] + _CSP_NET),
    "frame-src " + (" ".join(["https://td.doubleclick.net", "https://www.googletagmanager.com"]) if _G else "'none'"),
    "media-src 'self'", "manifest-src 'self'", "worker-src 'self'",
    "object-src 'none'", "base-uri 'none'", "form-action 'self'", "frame-ancestors 'none'",
    "upgrade-insecure-requests"])
SECURITY_HEADERS = [
    {"key": "Content-Security-Policy", "value": CSP_HEADER},
    {"key": "Strict-Transport-Security", "value": "max-age=63072000; includeSubDomains; preload"},
    {"key": "X-Content-Type-Options", "value": "nosniff"},
    {"key": "X-Frame-Options", "value": "DENY"},
    {"key": "Referrer-Policy", "value": "strict-origin-when-cross-origin"},
    {"key": "Permissions-Policy", "value": "camera=(), microphone=(), geolocation=(), payment=(), usb=(), serial=(), bluetooth=(), hid=(), "
                                           "magnetometer=(), gyroscope=(), accelerometer=(), display-capture=(), browsing-topics=()"},
    {"key": "Cross-Origin-Opener-Policy", "value": "same-origin"},
    {"key": "Cross-Origin-Resource-Policy", "value": "same-origin"},
    {"key": "X-Permitted-Cross-Domain-Policies", "value": "none"},
    {"key": "Origin-Agent-Cluster", "value": "?1"},
]

# ——— Images d'aperçu (réseaux sociaux) : titre de la page sur fond encre, carte pour les pages ville ———
def _og_kicker(p):
    if p.startswith("/blog/") and p != "/blog/":
        a = next((x for x in ARTICLES if f"/blog/{x['slug']}/" == p), None)
        return "Blog · " + (a["tag"] if a else "Article")
    c = next((x for x in VL.CITIES if VL.path(x) == p), None)
    if c: return "Devis travaux · " + c["name"]
    if p.startswith("/devis-travaux/"): return "Pour les propriétaires"
    if p.startswith(("/metiers/", "/google-ads/", "/meta-ads/", "/trouver-des-chantiers/")): return "Pour les artisans du bâtiment"
    return {"/blog/": "Blog", "/qui-sommes-nous/": "Qui sommes-nous", "/questions/": "Questions", "/lexique/": "Lexique"}.get(p, "Bartier &amp; Co")
_jobs = []
for p, t in OG.items():
    if p not in paths: continue
    c = next((x for x in VL.CITIES if VL.path(x) == p), None)
    _jobs.append({"file": og_key(p), "kicker": _og_kicker(p), "title": html.escape(fr(t), quote=False), "map": VL.carte(c["slug"]) if c else ""})
_og_dir = ROOT / "assets" / "og"
_og_dir.mkdir(parents=True, exist_ok=True)
_og_json = json.dumps(_jobs, ensure_ascii=False, sort_keys=True)
_og_sig = hashlib.sha1((_og_json + (ROOT / "_build" / "og_render.js").read_text(encoding="utf-8")).encode()).hexdigest()
_og_manifest = ROOT / "_build" / "og_manifest.txt"
if (not _og_manifest.exists() or _og_manifest.read_text().strip() != _og_sig
        or any(not (_og_dir / f"{j['file']}.png").exists() for j in _jobs)):
    (ROOT / "_build" / "og_jobs.json").write_text(_og_json, encoding="utf-8")
    import subprocess as _sp
    _sp.run(["node", str(ROOT / "_build" / "og_render.js")], check=True, cwd="/tmp")
    _og_manifest.write_text(_og_sig + "\n")
for _f in _og_dir.glob("*.png"):
    if _f.stem not in {j["file"] for j in _jobs}:
        _f.unlink()

# ——— vercel.json : redirections utiles et en-têtes ———
(ROOT / "vercel.json").write_text(json.dumps({
    # une seule adresse par page : /blog et /blog/index.html renvoient vers /blog/
    # cleanUrls retiré : il redirigeait aussi le fichier de vérification Google. Toutes les pages sont des dossiers,
    # les adresses en index.html sont redirigées par les deux règles ci-dessous.
    "cleanUrls": False, "trailingSlash": True,
    "redirects": [{"source": s, "destination": d, "permanent": True} for s, d in [
        ("/index.html", "/"), ("/:path*/index.html", "/:path*/"),
        ("/particuliers", "/devis-travaux/"), ("/particuliers/", "/devis-travaux/"), ("/devis", "/devis-travaux/"), ("/devis/", "/devis-travaux/"),
        ("/toiture", "/devis-travaux/toiture/"), ("/toiture/", "/devis-travaux/toiture/")]],
    "headers": [{"source": "/(.*)", "headers": SECURITY_HEADERS},
                {"source": "/(.*)", "has": [{"type": "host", "value": ".*\\.vercel\\.app"}], "headers": [{"key": "X-Robots-Tag", "value": "noindex"}]},  # adresses Vercel : jamais indexées, seul bartierandco.com compte
                {"source": "/assets/(.*)", "headers": [{"key": "Cache-Control", "value": "public, max-age=86400"}]},
                {"source": "/assets/photos/(.*)", "headers": [{"key": "Cache-Control", "value": "public, max-age=2592000"}]},
                {"source": "/assets/fonts/(.*)", "headers": [{"key": "Cache-Control", "value": "public, max-age=31536000, immutable"}]},
                {"source": "/assets/js/(gsap|ScrollTrigger|SplitText|lenis|consent)(.*)", "headers": [{"key": "Cache-Control", "value": "public, max-age=31536000, immutable"}]},
                {"source": "/404(.*)", "headers": [{"key": "X-Robots-Tag", "value": "noindex"}]},
                {"source": f"/(llms.txt|llms-full.txt|{INDEXNOW_KEY}.txt)", "headers": [{"key": "X-Robots-Tag", "value": "noindex"}]},
                {"source": "/favicon(.*)", "headers": [{"key": "Cache-Control", "value": "public, max-age=604800"}]},
                {"source": "/apple-touch-icon.png", "headers": [{"key": "Cache-Control", "value": "public, max-age=604800"}]},
                {"source": "/assets/og/(.*)", "headers": [{"key": "Cross-Origin-Resource-Policy", "value": "cross-origin"}]},
                {"source": "/assets/(og.png|logo-bartier.png)", "headers": [{"key": "Cross-Origin-Resource-Policy", "value": "cross-origin"}]}]}, indent=2), encoding="utf-8")

# ——— Fichiers SEO et GEO ———
for f in ["robots.txt", "llms.txt"]:
    (ROOT / f).write_text((V1.parent / f).read_text(encoding="utf-8"), encoding="utf-8")
# Pas de lien vers une page ville qui n'existe pas encore
_llms = (ROOT / "llms.txt").read_text(encoding="utf-8").split("\n")
_vl_at = next((i for i, l in enumerate(_llms) if l.startswith("- [Devis travaux à ")), None)
_llms = [l for l in _llms if not l.startswith("- [Devis travaux à ")]
if _vl_at is not None:
    _llms[_vl_at:_vl_at] = [f'- [Devis travaux {VL.a_(c)}]({SITE}{VL.path(c)}) : {c["hook"].rstrip(".")}. Règles locales, aides et conseil France Rénov’, par métier.'
                            for c in VL.CITIES if VL.path(c) in paths]
_llms = [l for l in _llms if not (m := re.search(r"/devis-travaux/([a-z-]+)/\)", l)) or f"/devis-travaux/{m.group(1)}/" in paths]
(ROOT / "llms.txt").write_text("\n".join(_llms), encoding="utf-8")
# Date de dernière modification : elle ne change que si le texte de la page change (empreinte gardée dans _build/lastmod.json).
import hashlib as _h
_lm_file = ROOT / "_build" / "lastmod.json"
_lm = json.loads(_lm_file.read_text(encoding="utf-8")) if _lm_file.exists() else {}
def _page_text(p):
    d = (ROOT / p.strip("/") / "index.html").read_text(encoding="utf-8")
    m = d[d.index("<main"):d.index("</main>")] if "<main" in d else d
    m = re.sub(r"<(script|style|svg)[\s\S]*?</\1>", " ", m)
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", m))).strip()
for p in paths:
    sig = _h.sha1(_page_text(p).encode()).hexdigest()[:16]
    if _lm.get(p, {}).get("sig") != sig:
        _lm[p] = {"sig": sig, "date": BUILD}
_lm = {p: _lm[p] for p in paths}
_lm_file.write_text(json.dumps(_lm, indent=1, sort_keys=True) + "\n", encoding="utf-8")
_MOIS = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre", "décembre"]
for p in paths:
    _f = ROOT / p.strip("/") / "index.html"
    _t = _f.read_text(encoding="utf-8")
    if "@@MAJ" in _t:
        _y, _m, _d = _lm[p]["date"].split("-")
        _f.write_text(_t.replace("@@MAJFR@@", f"{int(_d)} {_MOIS[int(_m) - 1]} {_y}").replace("@@MAJ@@", _lm[p]["date"]), encoding="utf-8")
urls = "\n".join(f"  <url><loc>{SITE}{p}</loc><lastmod>{_lm[p]['date']}</lastmod></url>" for p in paths if p not in REVIEW)
(ROOT / f"{INDEXNOW_KEY}.txt").write_text(INDEXNOW_KEY, encoding="utf-8")
import llmsfull
(ROOT / "llms-full.txt").write_text(llmsfull.build(ROOT, SITE, [p for p in paths if p not in ("/mentions-legales/", "/confidentialite/", "/cookies/") and p not in REVIEW]), encoding="utf-8")
_keep = IMG.used()
for _f in (ROOT / "assets" / "photos").glob("*.webp"):
    if _f.name not in _keep:
        _f.unlink()
if LIVE and legal_missing and not EN_FORMATION:
    raise SystemExit("Mise en ligne impossible : informations légales manquantes : " + ", ".join(sorted(legal_missing)))
if LIVE and legal_missing:
    print("En ligne avec des mentions d'attente (société en cours d'immatriculation) :", ", ".join(sorted(legal_missing)))
(ROOT / "sitemap.xml").write_text(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}\n</urlset>\n', encoding="utf-8")
# ——— Sécurité : seuls les scripts intégrés écrits ici peuvent s'exécuter (empreinte SHA-256 de chacun, page par page).
# Le navigateur applique à la fois l'en-tête (vercel.json) et cette balise : un script injecté par un tiers serait refusé.
import base64 as _b64
_SCRIPT_RE = re.compile(r"<script\b([^>]*)>([\s\S]*?)</script>", re.I)
def _csp_meta(doc):
    hashes = []
    for m in _SCRIPT_RE.finditer(doc):
        attrs, body = m.group(1), m.group(2)
        if re.search(r"\bsrc\s*=", attrs, re.I):
            continue
        t = re.search(r'\btype\s*=\s*"([^"]*)"', attrs, re.I)
        if t and t.group(1).lower() not in ("", "text/javascript", "module", "application/javascript"):
            continue  # données structurées (application/ld+json) : jamais exécutées
        hashes.append("'sha256-" + _b64.b64encode(_h.sha256(body.encode("utf-8")).digest()).decode() + "'")
    pol = "script-src " + " ".join(CSP_SCRIPT + sorted(set(hashes))) + "; object-src 'none'; base-uri 'none'"
    doc = re.sub(r'<meta http-equiv="Content-Security-Policy"[^>]*>\n?', "", doc)
    return doc.replace('<meta charset="utf-8">', '<meta charset="utf-8">\n<meta http-equiv="Content-Security-Policy" content="' + pol + '">', 1)
for _f in [ROOT / p.strip("/") / "index.html" for p in paths] + [ROOT / "404.html"]:
    _t = _f.read_text(encoding="utf-8")
    assert '<meta charset="utf-8">' in _t, _f
    _f.write_text(_csp_meta(_t), encoding="utf-8")
print(len(paths), "pages :", ", ".join(paths))

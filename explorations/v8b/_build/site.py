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
TODAY = "2026-11-17"
NB = " "

M = runpy.run_path(str(V1 / "metiers.py"))
P = runpy.run_path(str(V1 / "pages.py"))
TRADES, PROJECT, ARTICLES = M["TRADES"], M["PROJECT"], P["ARTICLES"]
GOOGLE_FAQ, META_FAQ = P["GOOGLE_FAQ"], P["META_FAQ"]


def fr(text):
    text = text.replace("'", "’")
    return re.sub(r" ([;:?!»])", NB + r"\1", text).replace("« ", "«" + NB)


def esc(t):
    return html.escape(fr(t), quote=False)


# ——— Page d'accueil : navigation, héros, liens vers les pages ———
home = (ROOT / "index.html").read_text(encoding="utf-8")

NAV = [("Métiers", "/metiers/"), ("Google Ads", "/google-ads/"), ("Meta Ads", "/meta-ads/"),
       ("Qui sommes-nous", "/qui-sommes-nous/"), ("Blog", "/blog/"), ("Questions", "/#faq")]
nav_html = "\n".join(f'      <a class="link" href="{h}">{t}</a>' for t, h in NAV)
menu_html = "\n".join(f'    <a href="{h}">{t}</a>' for t, h in NAV) + '\n    <a href="#contact">Contact</a>'
home = re.sub(r'(<nav class="hdr-nav" aria-label="Menu">)[\s\S]*?(</nav>)', r"\1\n" + nav_html + r"\n    \2", home, count=1)
home = re.sub(r'(<div class="menu" id="menu">\s*<nav aria-label="Menu">)[\s\S]*?(</nav>)', r"\1\n" + menu_html + r"\n  \2", home, count=1)

# Héros : le résultat rêvé, en un mot
home = re.sub(r'<h1 class="giant" style="--len:\d+">[^<]*</h1>', '<h1 class="giant" style="--len:8">Complet.</h1>', home, count=1)
home = re.sub(r'(<div class="hero-intro">\s*<p class="lead">)[^<]*(</p>)',
              r"\1Votre agenda, rempli toute l’année. Des propriétaires qui ont un vrai projet, rappelés en moins de cinq minutes et installés dans votre planning. Il ne vous reste qu’à chiffrer.\2", home, count=1)

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
@media (max-width:760px){.wa-fab b span{display:none}.wa-fab{padding-right:.9rem}}
@media (prefers-reduced-motion:reduce){.wa-panel,.wa-fab{transition:none}}
</style>
"""
WA_SVG = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2Zm0 18.2a8.2 8.2 0 0 1-4.2-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2Zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8-.2-.1-.4-.1-.6.1l-.8 1c-.1.2-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.2-.4.2-.4.7-1.3.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.1 5.1 0 0 0 1.1 2.7 11.6 11.6 0 0 0 4.5 3.9c1.7.7 2.3.8 3.2.7a2.7 2.7 0 0 0 1.8-1.3 2.2 2.2 0 0 0 .1-1.3c0-.1-.2-.2-.5-.3Z"/></svg>'
TEL_SVG = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2a1 1 0 0 1 1-.2 11.4 11.4 0 0 0 3.6.6 1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1 11.4 11.4 0 0 0 .6 3.6 1 1 0 0 1-.2 1Z"/></svg>'
import urllib.parse as _u
def wa(msg): return WA + "?text=" + _u.quote(msg)
QUESTIONS = [
    ("Mon secteur est-il encore libre ?", "Bonjour Martin, je suis artisan à [ville] ([métier]). Mon secteur est-il encore libre ?"),
    ("Comment se passent les rendez-vous ?", "Bonjour Martin, j'aimerais comprendre comment vous trouvez et qualifiez les rendez-vous."),
    ("Combien cela coûterait pour moi ?", "Bonjour Martin, je voudrais connaître le prix pour mon entreprise ([métier], [ville])."),
]
qs = "\n".join(f'      <a class="wa-q" href="{html.escape(wa(m))}" target="_blank" rel="noopener" data-wa="question">{q.replace(" ?", "&nbsp;?")}</a>' for q, m in QUESTIONS)
WA_HTML = f"""<div class="wa" id="wa">
  <div class="wa-panel" id="wa-panel" role="dialog" aria-modal="false" aria-labelledby="wa-title">
    <div class="wa-head">
      <span class="wa-av" aria-hidden="true">MB</span>
      <p id="wa-title"><b>Martin Barthélémy</b><small>Cofondateur · Head of Sales</small></p>
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
  <button class="wa-fab" type="button" aria-expanded="false" aria-controls="wa-panel"><span class="wa-ico">{WA_SVG}</span><span class="wa-dot" aria-hidden="true"></span><b>Parler à Martin<span>, Head of Sales</span></b></button>
</div>
<script>
(function(){{var w=document.getElementById('wa');if(!w)return;var b=w.querySelector('.wa-fab');
function set(o){{w.classList.toggle('is-open',o);b.setAttribute('aria-expanded',String(o));}}
b.addEventListener('click',function(){{set(!w.classList.contains('is-open'))}});
w.querySelector('[data-wa-close]').addEventListener('click',function(){{set(false);b.focus()}});
document.addEventListener('keydown',function(e){{if(e.key==='Escape')set(false)}});
document.addEventListener('click',function(e){{if(!w.contains(e.target))set(false)}});
w.querySelectorAll('[data-wa]').forEach(function(a){{a.addEventListener('click',function(){{(window.dataLayer=window.dataLayer||[]).push({{event:'contact_martin',canal:a.dataset.wa}})}})}});
}})();
</script>
"""
home = re.sub(r'<style id="wa-css">[\s\S]*?</style>\n', "", home)
home = re.sub(r'<div class="wa" id="wa">[\s\S]*?</script>\n', "", home)
home = home.replace("</head>", WA_CSS + "</head>", 1)
home = home.replace("</body>", WA_HTML + "</body>", 1)

# Données structurées et adresse canonique de l'accueil
if '"@type":"Organization"' not in home:
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "Organization", "@id": SITE + "/#org", "name": "Bartier & Co", "legalName": "Bartier & Co SAS", "url": SITE + "/", "email": "contact@bartierandco.com", "areaServed": ["FR", "BE"],
         "description": "Agence qui trouve des clients aux artisans du bâtiment : annonces locales, rappel des demandes en moins de cinq minutes, visites de devis fixées directement dans leur agenda.",
         "founder": [{"@type": "Person", "name": "Charles Le Cottier"}, {"@type": "Person", "name": "Martin Barthélémy"}]},
        {"@type": "WebSite", "url": SITE + "/", "name": "Bartier & Co", "inLanguage": "fr-FR", "publisher": {"@id": SITE + "/#org"}}]}
    home = home.replace("</head>", f'<link rel="canonical" href="{SITE}/">\n<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False, separators=(",", ":"))}</script>\n</head>', 1)
(ROOT / "index.html").write_text(home, encoding="utf-8")

# ——— Gabarit des pages intérieures ———
HEAD = home[:home.index("</head>")]
HEAD = re.sub(r'<link rel="canonical"[^>]*>\n?', "", HEAD)
HEAD = re.sub(r'<script type="application/ld\+json">[\s\S]*?</script>\n?', "", HEAD)
BODY_OPEN = home[home.index("</head>"):home.index("<main>") + len("<main>")]
CONTACT = home[home.rindex('<section', 0, home.index('id="contact"')):]
CONTACT = CONTACT[:CONTACT.index("</section>") + len("</section>")]
TAIL = home[home.index("</main>"):]
TEAM = home[home.index('<section class="team sheet"'):]
TEAM = TEAM[:TEAM.index("</section>") + len("</section>")]
IMGS = {html.unescape(a): u for u, a in re.findall(r'<img src="([^"]+)" alt="([^"]+)"', home)}


def img(alt_start):
    for alt, url in IMGS.items():
        if alt.startswith(alt_start):
            return url, alt
    raise KeyError(alt_start)


def absolutize(block):
    block = block.replace('href="#hero"', 'href="/"')
    return re.sub(r'href="#(?!contact\b|menu\b)([\w-]+)"', r'href="/#\1"', block)


EXTRA_CSS = """<style>
/* Pages intérieures */
.pg-top{padding-top:calc(var(--hdr) + clamp(48px,7vw,104px))}
.pg-grid{row-gap:40px;align-items:end}
.pg-text{grid-column:1 / 3;display:flex;flex-direction:column;gap:1.4rem}
.pg-text h1{font:300 clamp(2.6rem,5.2vw,5rem)/1.02 var(--f-display);letter-spacing:-.045em;text-wrap:balance}
.pg-text .lead{font-size:clamp(1.05rem,1.3vw,1.2rem);line-height:1.5;max-width:36ch}
.pg-text .actions{display:flex;flex-wrap:wrap;align-items:center;gap:1rem 1.6rem}
.pg-photo{grid-column:3 / 5;aspect-ratio:4 / 3}
.pg-photo img{filter:grayscale(1) contrast(1.05)}
.crumbs{display:flex;flex-wrap:wrap;gap:.5rem;font-size:.85rem;color:var(--soft)}
.crumbs a{color:inherit}
.kick{font-size:.88rem;color:var(--accent)}
[data-tone="dark"] .kick,[data-tone="accent"] .kick{color:var(--soft)}
.sp-head{row-gap:24px;margin-bottom:clamp(40px,5vw,72px)}
.sp-head h2{grid-column:1 / 3}
.sp-head p{grid-column:3 / 5;align-self:end;max-width:44ch}
.sp-cols{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));border-top:1px solid var(--rule)}
.sp-cols > li{padding:clamp(18px,2vw,28px) var(--cell);display:flex;flex-direction:column;gap:.7rem}
.sp-cols > li + li{border-left:1px solid var(--rule)}
.sp-n{font:300 2.2rem/1 var(--f-display);color:var(--accent);letter-spacing:-.04em}
[data-tone="dark"] .sp-n{color:var(--soft)}
.sp-cols h3{font:300 clamp(1.35rem,1.8vw,1.7rem)/1.15 var(--f-display);letter-spacing:-.03em}
.sp-cols p{font-size:.95rem;color:var(--soft);max-width:40ch}
.sp-split{row-gap:32px;align-items:start}
.sp-split > div:first-child{grid-column:1 / 3;display:flex;flex-direction:column;gap:1.2rem}
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


def head(title, desc, path, schema=None):
    h = re.sub(r"<title>[^<]*</title>", f"<title>{html.escape(fr(title), quote=False)}</title>", HEAD, count=1)
    h = re.sub(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{html.escape(fr(desc))}">', h, count=1)
    ld = f'<script type="application/ld+json">{json.dumps(schema, ensure_ascii=False, separators=(",", ":"))}</script>\n' if schema else ""
    return h + f'<link rel="canonical" href="{SITE}{path}">\n' + ld + EXTRA_CSS


def write(path, title, desc, body, nav=None, schema=None, metier=None):
    top = absolutize(BODY_OPEN)
    if nav:
        top = top.replace(f'class="link" href="{nav}"', f'class="link" href="{nav}" aria-current="page"', 1)
    contact = CONTACT.replace(f'name="metier" value="{metier}"', f'name="metier" value="{metier}" checked', 1) if metier else CONTACT
    doc = head(title, desc, path, schema) + top + "\n" + fr(body) + "\n\n" + contact + "\n" + absolutize(TAIL)
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


def top(kick, h1, lead, crumb, photo=None, cta2=None, meta=""):
    second = f'<a class="link" href="{cta2[1]}">{cta2[0]}</a>' if cta2 else ""
    fig = ""
    if photo:
        url, alt = img(photo)
        fig = f'<figure class="pg-photo frame"><img src="{url}" alt="{html.escape(alt)}" width="1200" height="900"></figure>'
    lead_html = f'<p class="lead">{lead}</p>' if lead else ""
    return f"""<section class="sheet pg-top" data-tone="light">
  <div class="grid pg-grid">
    <div class="pg-text">
      {crumb}
      <p class="kick">{kick}</p>
      <h1>{h1}</h1>
      {lead_html}{meta}
      <div class="actions"><a class="btn" href="#contact"><span>Vérifier mon secteur</span><svg class="tick" viewBox="0 0 10 10" aria-hidden="true"><path d="M1 1h8v8" fill="none" stroke="currentColor" stroke-width="1.4"/></svg></a>{second}</div>
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


def faq(items, title="Vos questions, nos réponses"):
    rows = "\n".join(f'      <details class="fq"><summary><span>{q}</span><i class="fq-icon" aria-hidden="true"></i></summary><div class="fq-a"><p>{a}</p></div></details>' for q, a in items)
    return f"""<section class="faq sheet" data-kind="faq" data-tone="paper">
  <div class="grid fq-grid">
    <div class="fq-head"><h2 data-split>{title}</h2><p>Une autre question ? <a class="link" href="#contact">Écrivez-nous</a></p></div>
    <div class="fq-list">
{rows}
    </div>
  </div>
</section>"""


COMPARE = """<section class="sheet" data-tone="light">
  <div class="grid sp-head"><h2 data-split>Deux canaux, deux demandes</h2><p>Google capte ceux qui cherchent déjà. Meta touche ceux qui n'ont pas encore cherché. Nous choisissons selon votre métier et votre secteur.</p></div>
  <div class="sp-table" role="table" aria-label="Google Ads et Meta Ads">
    <div class="sp-row is-head" role="row"><span role="columnheader"></span><span role="columnheader">Google Ads</span><span role="columnheader">Meta Ads</span></div>
    <div class="sp-row" role="row"><span role="rowheader">La demande</span><span role="cell">Exprimée : le propriétaire cherche</span><span role="cell">Suscitée : il n'a pas encore cherché</span></div>
    <div class="sp-row" role="row"><span role="rowheader">Typiquement</span><span role="cell">Urgences, projets mûrs</span><span role="cell">Rénovation, entretien, projets à venir</span></div>
    <div class="sp-row" role="row"><span role="rowheader">Le volume</span><span role="cell">Limité aux recherches locales</span><span role="cell">Tous les propriétaires du rayon</span></div>
    <div class="sp-row" role="row"><span role="rowheader">Le point clé</span><span role="cell">Écarter les recherches inutiles</span><span role="cell">Qualifier au téléphone</span></div>
  </div>
</section>"""

PHOTO = {"couverture": "Un couvreur pose", "facade": "Une façade en rénovation", "menuiserie-exterieure": "Un menuisier pose",
         "charpente": "Une charpente en bois", "isolation": "Isolation d"}
paths = ["/"]

# ——— Métiers ———
for t in TRADES:
    path = f"/metiers/{t['slug']}/"
    short = f"Votre agenda rempli de propriétaires qui préparent {PROJECT[t['slug']]}. Chaque demande est rappelée en moins de cinq minutes, vérifiée, puis posée dans votre planning."
    angles = "\n".join(f"""    <li><div class="ad-card"><p class="ad-meta">Votre entreprise · Sponsorisé</p><p class="ad-angle">{a}</p><p class="ad-text">{b}</p><p class="ad-cta">Demander une visite</p></div></li>""" for a, b in t["angles"])
    trade_faq = t["faq"] + [("Combien cela coûte-t-il ?", "Il dépend de votre secteur et du volume que vous pouvez absorber. Vous avez un prix précis pendant l'appel de quinze minutes, avant toute décision."),
                            ("Y a-t-il un engagement ?", "Non. Aucune durée minimale : vous restez parce que l'agenda se remplit.")]
    body = "\n\n".join([
        top(f"{t['who']} · France et Belgique", f"{t['h1']} {t['h1_em']}", short, crumbs(("Métiers", "/metiers/"), (t["name"], path)), PHOTO[t["slug"]], ("Ce que nous vérifions", "#appel")),
        f"""<section class="sheet" data-tone="paper">
  <div class="grid sp-split">
    <div><h2 data-split>Ce que nous allons chercher</h2><p>Des chantiers qui valent le déplacement. Le reste est écarté avant d'arriver chez vous.</p></div>
    <div class="sp-two">
      <ul class="sp-list">{''.join(f'<li>{x}</li>' for x in t['keep'])}</ul>
      <ul class="sp-list is-no" style="margin-top:2rem">{''.join(f'<li>{x}</li>' for x in t['drop'])}</ul>
    </div>
  </div>
</section>""",
        cols(t["problems"], "Le métier est bon. Les demandes, moins.", "Ce que nous entendons chez les artisans de votre métier."),
        f"""<section class="sheet" id="appel" data-tone="dark">
  <div class="grid sp-split">
    <div><h2 data-split>Ce que nous vérifions avant votre visite</h2><p>Rappel en moins de cinq minutes, en semaine de 8 h à 19 h. Pas de bonnes réponses, pas de rendez-vous.</p></div>
    <ol class="sp-list is-num">{''.join(f'<li>{q}</li>' for q in t['questions'])}</ol>
  </div>
</section>""",
        f"""<section class="sheet" data-tone="tint">
  <div class="grid sp-head"><h2 data-split>À votre nom, autour de chez vous</h2><p>Facebook et Instagram, à 25 à 40 km de votre dépôt, avec vos photos de chantier. Exemples d'angles, écrits ensuite avec vous.</p></div>
  <ul class="sp-cols is-cards">
{angles}
  </ul>
</section>""",
        faq(trade_faq),
    ])
    body = body.replace('class="sp-two"', 'class="sp-two"')
    write(path, f"{t['title']} | Bartier & Co", short, body, nav="/metiers/", metier=t["radio"],
          schema={"@context": "https://schema.org", "@graph": [
              {"@type": "Service", "name": fr(t["title"]), "serviceType": "Recherche de clients pour artisans du bâtiment", "areaServed": ["FR", "BE"], "provider": {"@type": "Organization", "name": "Bartier & Co", "url": SITE + "/"}},
              bc_ld(("Métiers", "/metiers/"), (t["name"], path)), faq_ld(trade_faq)]})
    paths.append(path)

hub_items = "\n".join(f'    <li class="sector"><h3 class="sector-name"><a href="/metiers/{t["slug"]}/">{t["name"].split(" et ")[0]}</a></h3><p class="sector-note">{esc(", ".join(t["keep"][:3]))}</p></li>' for t in TRADES)
write("/metiers/", "Métiers : des clients pour chaque corps de métier | Bartier & Co",
      "Des clients pour couvreurs, menuisiers, façadiers, charpentiers et entreprises d'isolation, en France et en Belgique. Un seul artisan par secteur.",
      "\n\n".join([
          top("Métiers", "Uniquement les métiers où un chantier compte.", "Des chantiers de plusieurs milliers d'euros. Pas de dépannage, pas de petits travaux.", crumbs(("Métiers", "/metiers/")), "Une équipe d"),
          f"""<section class="sectors sheet" data-kind="industries" data-tone="tint">
  <ul class="sc-list">
{hub_items}
  </ul>
</section>""",
      ]), nav="/metiers/", schema={"@context": "https://schema.org", "@graph": [bc_ld(("Métiers", "/metiers/"))]})
paths.insert(1, "/metiers/")

# ——— Google Ads ———
write("/google-ads/", "Google Ads pour artisans du bâtiment | Bartier & Co",
      "Campagnes Google Ads locales pour artisans du bâtiment : captez les propriétaires qui cherchent déjà, rappelés en moins de cinq minutes.",
      "\n\n".join([
          top("Google Ads", "Soyez trouvé au moment où ils cherchent.", "Un propriétaire tape « couvreur » et le nom de sa ville. Il tombe sur vous. Nous le rappelons en moins de cinq minutes, avant vos concurrents.", crumbs(("Google Ads", "/google-ads/")), "Campagne de recherche", ("Comparer avec Meta", "/meta-ads/")),
          cols([("Les urgences", "Fuite, tuiles envolées, gouttière arrachée : la demande est immédiate."),
                ("Les projets mûrs", "Le propriétaire compare déjà des entreprises. Être là et rappeler vite fait la différence."),
                ("Les secteurs denses", "Assez de recherches locales pour qu'une campagne tienne toute l'année.")],
               "Quand Google est le bon canal", "La demande existe déjà. Il faut la capter avant les autres."),
          split("Une campagne qui ne paie que les bonnes recherches", "Chaque clic coûte. L'essentiel du travail consiste à écarter ceux qui ne deviendront jamais des chantiers.",
                ["Campagnes par métier et par commune de votre zone", "Recherches inutiles exclues : gratuit, pas cher, emploi, formation, bricolage",
                 "Une page dédiée à votre entreprise, rapide sur mobile", "Chaque appel et chaque formulaire suivis jusqu'au rendez-vous",
                 "Rappel en moins de cinq minutes, qualification, rendez-vous dans votre agenda"], tone="paper"),
          split("Votre compte, votre budget, vos chiffres", "Tout est créé à votre nom. Vous gardez ce qui a été construit, même si vous arrêtez.",
                ["Compte Google Ads à votre nom", "Budget payé directement à Google", "Chaque recherche, chaque clic, chaque euro visibles"]),
          COMPARE,
          faq(GOOGLE_FAQ),
      ]), nav="/google-ads/",
      schema={"@context": "https://schema.org", "@graph": [{"@type": "Service", "name": "Google Ads pour artisans du bâtiment", "areaServed": ["FR", "BE"], "provider": {"@type": "Organization", "name": "Bartier & Co", "url": SITE + "/"}}, bc_ld(("Google Ads", "/google-ads/")), faq_ld(GOOGLE_FAQ)]})
paths.append("/google-ads/")

# ——— Meta Ads ———
write("/meta-ads/", "Publicité Facebook et Instagram pour artisans | Bartier & Co",
      "Annonces Facebook et Instagram locales pour artisans du bâtiment : les propriétaires de votre secteur, rappelés en moins de cinq minutes et qualifiés.",
      "\n\n".join([
          top("Meta Ads · Facebook et Instagram", "Remplissez votre agenda avant qu'ils ne cherchent.", "Des annonces à votre nom, vues par les propriétaires à 25 à 40 km de votre dépôt. Chaque demande rappelée en moins de cinq minutes, puis vérifiée.", crumbs(("Meta Ads", "/meta-ads/")), "Un propriétaire voit", ("Comparer avec Google", "/google-ads/")),
          cols([("Un rayon autour du dépôt", "25 à 40 km, réglés commune par commune selon vos chantiers."),
                ("Vos vraies photos", "Vos chantiers, votre équipe. Rien ne convainc mieux un voisin."),
                ("Des angles de saison", "Après les intempéries, avant l'hiver, au printemps pour la rénovation.")],
               "Des annonces qui vous ressemblent", "Au nom de votre entreprise, avec vos chantiers."),
          split("Rien ne part sans être vérifié", "Une demande Facebook n'est qu'un début. Le tri se fait au téléphone, pas dans votre agenda.",
                ["Formulaire avec questions de tri et accord explicite d'être recontacté", "Preuve du consentement conservée pour chaque demande",
                 "Rappel en moins de cinq minutes, en semaine de 8 h à 19 h", "Propriétaire, projet, commune et délai vérifiés",
                 "Rendez-vous dans votre agenda, rappels la veille et deux heures avant", "Flyers dans les rues voisines de chaque chantier signé"], tone="paper"),
          split("Votre page, votre compte, vos chiffres", "Tout est créé à votre nom, et le reste si vous arrêtez.",
                ["Page Facebook et compte publicitaire à votre nom", "Budget payé directement à Meta", "Toutes les statistiques des annonces visibles"]),
          COMPARE,
          faq(META_FAQ),
      ]), nav="/meta-ads/",
      schema={"@context": "https://schema.org", "@graph": [{"@type": "Service", "name": "Publicité Facebook et Instagram pour artisans du bâtiment", "areaServed": ["FR", "BE"], "provider": {"@type": "Organization", "name": "Bartier & Co", "url": SITE + "/"}}, bc_ld(("Meta Ads", "/meta-ads/")), faq_ld(META_FAQ)]})
paths.append("/meta-ads/")

# ——— Qui sommes-nous ———
write("/qui-sommes-nous/", "Qui sommes-nous | Bartier & Co",
      "Bartier & Co est une SAS française fondée par Charles Le Cottier et Martin Barthélémy. Des clients pour les artisans du bâtiment.",
      "\n\n".join([
          top("Qui sommes-nous", "Deux fondateurs. Un seul objectif : votre agenda.", "Bartier & Co est une SAS française fondée par Charles Le Cottier et Martin Barthélémy. Nous remplissons l'agenda des artisans du bâtiment, en France et en Belgique.", crumbs(("Qui sommes-nous", "/qui-sommes-nous/")), "Un artisan rencontre"),
          """<section class="sheet" data-tone="light">
  <div class="grid sp-split">
    <div><h2 data-split>Un bon artisan ne devrait pas courir après les devis</h2></div>
    <div class="prose">
      <p>Les artisans que nous accompagnons ont du métier et des clients satisfaits. Ce qui leur manque, c'est un flux régulier de projets sérieux.</p>
      <p>Les plateformes revendent la même demande à plusieurs entreprises. Le bouche-à-oreille ne se commande pas. Et personne ne peut rappeler depuis un toit.</p>
      <p>Nous avons construit un système simple : des annonces locales, un rappel en moins de cinq minutes, et un rendez-vous réservé à un seul artisan par secteur.</p>
    </div>
  </div>
</section>""",
          cols([("Un interlocuteur, pas un standard", "Vous avez le numéro de Charles et de Martin. L'un de nous répond."),
                ("Des engagements écrits", "Exclusivité, un artisan par secteur, rappel en cinq minutes, sans engagement de durée."),
                ("Des chiffres vérifiables", "Le budget est sur votre compte, et chaque rendez-vous est suivi jusqu'au chantier signé.")],
               "Comment nous travaillons", "", tone="paper"),
          TEAM.replace('id="team"', 'id="equipe"'),
      ]), nav="/qui-sommes-nous/",
      schema={"@context": "https://schema.org", "@graph": [{"@type": "AboutPage", "name": "Qui sommes-nous", "url": SITE + "/qui-sommes-nous/"}, bc_ld(("Qui sommes-nous", "/qui-sommes-nous/"))]})
paths.append("/qui-sommes-nous/")

# ——— Blog ———
COVER = {"lead-partage-lead-exclusif-rendez-vous-qualifie": "Tuiles de toiture", "google-ads-ou-meta-ads-artisan": "Une personne consulte", "relance-devis-artisan": "Un artisan prépare"}
posts = []
for a in ARTICLES:
    url, alt = img(COVER[a["slug"]])
    posts.append(f'    <li class="post"><a class="post-link" href="/blog/{a["slug"]}/"><p class="post-meta soft"><time datetime="{TODAY}">17 nov. 2026</time><br>{a["tag"]}</p><h3 class="post-title">{a["short"]}</h3><figure class="post-photo frame" data-wipe><img src="{url}" alt="{html.escape(alt)}" width="900" height="676"></figure></a></li>')
write("/blog/", "Blog : trouver des chantiers, publicité, relance de devis | Bartier & Co",
      "Des articles courts et concrets pour les artisans du bâtiment : trouver des chantiers, publicité locale, relance de devis, rendez-vous qualifiés.",
      "\n\n".join([
          top("Blog", "Plus de chantiers, moins de soirées au téléphone.", "Des articles courts et concrets, écrits pour les artisans du bâtiment.", crumbs(("Blog", "/blog/"))),
          f"""<section class="journal sheet" data-kind="journal" data-tone="light">
  <ul class="jr-list">
{chr(10).join(posts)}
  </ul>
</section>""",
      ]), nav="/blog/", schema={"@context": "https://schema.org", "@graph": [{"@type": "Blog", "name": "Blog Bartier & Co", "url": SITE + "/blog/", "inLanguage": "fr-FR"}, bc_ld(("Blog", "/blog/"))]})
paths.append("/blog/")

for a in ARTICLES:
    path = f"/blog/{a['slug']}/"
    meta = f'<p class="post-meta-line"><span>Par Charles Le Cottier, cofondateur · Head of Performance</span><span>Publié le <time datetime="{TODAY}">17 novembre 2026</time></span><span>{a["minutes"]} min de lecture</span></p>'
    body = "\n\n".join([
        top(a["tag"], a["title"], "", crumbs(("Blog", "/blog/"), (a["short"], path)), meta=meta),
        f"""<section class="sheet" data-tone="light">
  <div class="grid art-grid">
    <article class="prose">
{a['body']}
    </article>
    <aside class="art-aside">
      <h3>Votre secteur est-il libre ?</h3>
      <p>Un seul artisan par métier et par secteur.</p>
      <a class="btn" href="#contact"><span>Vérifier mon secteur</span></a>
    </aside>
  </div>
</section>""",
    ])
    write(path, f"{a['short']} | Bartier & Co", a["desc"], body, nav="/blog/",
          schema={"@context": "https://schema.org", "@graph": [
              {"@type": "BlogPosting", "headline": fr(a["title"]), "description": fr(a["desc"]), "datePublished": TODAY + "T09:00:00+01:00", "dateModified": TODAY + "T09:00:00+01:00", "inLanguage": "fr-FR",
               "mainEntityOfPage": SITE + path, "author": {"@type": "Person", "name": "Charles Le Cottier", "jobTitle": "Cofondateur, Head of Performance", "url": SITE + "/qui-sommes-nous/"},
               "publisher": {"@type": "Organization", "name": "Bartier & Co", "url": SITE + "/"}},
              bc_ld(("Blog", "/blog/"), (a["short"], path))]})
    paths.append(path)

# ——— Fichiers SEO et GEO ———
for f in ["robots.txt", "llms.txt"]:
    (ROOT / f).write_text((V1.parent / f).read_text(encoding="utf-8"), encoding="utf-8")
urls = "\n".join(f"  <url><loc>{SITE}{p}</loc><lastmod>{TODAY}</lastmod></url>" for p in paths)
(ROOT / "sitemap.xml").write_text(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}\n</urlset>\n', encoding="utf-8")
print(len(paths), "pages :", ", ".join(paths))

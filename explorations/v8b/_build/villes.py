# Pages « Devis travaux à <ville> » pour les particuliers : une page par ville, les 5 métiers sur chaque page.
# Contenu local vérifié et sourcé (recherches du 20/11/2026), jamais une page copiée où seul le nom de la ville change :
# Google sanctionne les pages satellites. Aucune promesse de présence locale : la mise en relation dépend de la commune
# (« Hors zone, nous vous le disons à l'appel »), comme sur le reste du site.
import re as _re

from villes_data import CITIES  # données locales, une entrée par ville

TRADE_H3 = {"toiture": "Couvreur à {v}", "facade": "Ravalement de façade à {v}", "fenetres": "Fenêtres et portes à {v}",
            "charpente": "Charpente à {v}", "isolation": "Isolation à {v}"}
TRADE_MORE = {"toiture": "Prix d’une toiture", "facade": "Prix d’un ravalement", "fenetres": "Prix d’une fenêtre",
              "charpente": "Prix d’une charpente", "isolation": "Prix de l’isolation"}
TRADE_PICK = {"toiture": "Devis toiture", "facade": "Devis façade", "fenetres": "Devis fenêtres", "charpente": "Devis charpente",
              "isolation": "Devis isolation"}

CSS = """<style id="vl-css">
.vl-wrap{padding:0 var(--cell)}
.vl-dl .link,.vl-trades .link,.vl-steps .link{display:inline;white-space:normal;min-height:0}
.vl-more{align-items:center}
.vl-more .link{align-self:center}
.vl-dl{grid-column:1 / -1}
.vl-trades{grid-template-columns:repeat(2,minmax(0,1fr))}
.vl-trades p+p{margin-top:10px}
.vl-more{display:flex;flex-wrap:wrap;gap:6px 18px;font-size:.92rem}
.vl-src{margin-top:24px;padding:0 var(--cell);font-size:.8rem;color:var(--muted)}
.vl-figs b small{font-size:.4em;letter-spacing:0}
.vl-figs .vl-fsrc{font-size:.78rem;color:rgba(255,255,255,.55)}
.vl-figs .vl-fsrc a{color:inherit}
.pf-howto.vl-steps li::before{color:var(--accent)}
.pf-howto.vl-steps p{color:inherit}
@media (max-width:760px){.vl-trades{grid-template-columns:1fr}}
</style>"""


def path(c):
    return f"/devis-travaux/{c['slug']}/"


def _ext(label, url):
    return f'<a class="link" href="{url}" target="_blank" rel="noopener">{label}</a>'


def build_city(PF, phone, phone_txt, crumbs, c):
    tick = PF.tick()
    v = c["name"]
    parts = PF.build(lambda a: ("", ""), phone, phone_txt, crumbs, parts=True)
    form = parts["form"]
    form = form.replace('placeholder="Ex. 80000"', f'placeholder="Ex. {c["cp"]}"', 1)
    hero = f"""<section class="sheet pf-hero" id="haut" data-tone="light">
  <div class="grid pf-hero-grid">
    <div class="pf-intro">
      {crumbs}
      <div class="pf-h1"><h1 class="pf-kw">Devis travaux à {v} : toiture, façade, fenêtres, isolation</h1> <p class="pf-big">Pas cinq <span class="pf-who">artisans</span>. <br>Un seul, près de chez vous.</p></div>
      <p class="lead">Décrivez vos travaux en 1 minute.<br>Nous vous rappelons en moins de 5 minutes en semaine, et nous fixons la visite.</p>
      {PF.trust("d-only")}
      <p class="pf-call d-only">Pressé ? <a class="link" href="tel:{phone}">{phone_txt}</a></p>
    </div>
    {form}
    <div class="pf-mtrust m-only">{PF.trust()}</div>
  </div>
</section>"""

    figs = "".join(f'<li><b>{a}</b> <span>{b}</span> <span class="vl-fsrc">{src}</span></li>' for a, b, src in c["figures"])
    figures = f"""<section class="sheet" id="en-chiffres" data-tone="dark">
  <div class="grid sp-head"><h2 data-split>{v} en quelques chiffres</h2><p>{c["figures_intro"]}</p></div>
  <ul class="pf-proms vl-figs">{figs}</ul>
</section>"""
    steps = "".join(f"<li><h3>{a}</h3><p>{b}</p></li>" for a, b in c["steps"])
    steps = f"""<section class="sheet" id="demarches" data-tone="light">
  <div class="grid sp-head"><h2 data-split>Avant vos travaux à {v} : les démarches</h2><p>{c["steps_intro"]}</p></div>
  <ol class="pf-howto vl-steps">{steps}</ol>
</section>"""

    facts = "".join(f"<div><dt>{a}</dt><dd>{b}</dd></div>" for a, b in c["facts"])
    local = f"""<section class="sheet" id="a-savoir" data-tone="paper">
  <div class="grid sp-head"><h2 data-split>Travaux à {v} : ce qu’il faut savoir</h2><p>{c["answer"]}</p></div>
  <div class="grid"><dl class="pf-dl vl-dl">{facts}</dl></div>
</section>"""

    items = []
    for k in ("toiture", "facade", "fenetres", "charpente", "isolation"):
        paras = "".join(f"<p>{p}</p>" for p in c["trades"][k])
        items.append(f'<li><h3>{TRADE_H3[k].format(v=v)}</h3>{paras}<p class="vl-more"><a class="link pf-pick" href="#projet" data-v="{k}">{TRADE_PICK[k]}</a>'
                     f'<a class="link" href="/devis-travaux/{PF.SLUG[k]}/">{TRADE_MORE[k]}</a></p></li>')
    trades = f"""<section class="sheet" id="travaux" data-tone="light">
  <div class="grid sp-head"><h2 data-split>Vos travaux à {v}, métier par métier</h2><p>{c["trades_intro"]}</p></div>
  <ul class="pf-checks vl-trades">{"".join(items)}</ul>
</section>"""

    aid = "".join(f"<li><h3>{a}</h3><p>{b}</p></li>" for a, b in c["aides"])
    aides = f"""<section class="sheet" id="aides" data-tone="paper">
  <div class="grid sp-head"><h2 data-split>Aides et conseils gratuits à {v}</h2><p>{c["aides_intro"]}</p></div>
  <ul class="pf-checks vl-trades">{aid}</ul>
</section>"""

    leak = f"""<section class="sheet pf-leak is-short" id="fuite-toiture" data-tone="accent">
  <div class="grid sp-head"><h2 data-split>Une fuite de toiture à {v} ?</h2><p>Signalez-la : nous vous rappelons en priorité. En attendant, suivez <a class="link" href="/devis-travaux/toiture/#fuite-toiture">les 5 bons réflexes</a>.</p></div>
  <p class="pf-mid"><a class="btn pf-pick" href="#projet" data-v="toiture" data-need="fuite"><span>Signaler une fuite</span>{tick}</a><span class="pf-prio">Rappel prioritaire</span></p>
</section>"""

    brief = [("Le service", f"Bartier &amp; Co vous met gratuitement en relation avec l’artisan partenaire qui couvre votre commune, pour vos travaux de toiture, façade, fenêtres, charpente ou isolation à {v} et alentours.")] + PF.BRIEF[1:]
    brief = "".join(f"<div><dt>{a}</dt><dd>{b}</dd></div>" for a, b in brief)
    brief = f"""<section class="sheet pf-brief" data-tone="light" aria-labelledby="pf-brief-h">
  <div class="grid pf-brief-grid">
    <h2 id="pf-brief-h">Devis travaux à {v} : l’essentiel</h2>
    <dl class="pf-dl">{brief}</dl>
    <p class="pf-upd">Mis à jour le <time datetime="@@MAJ@@">@@MAJFR@@</time></p>
  </div>
</section>"""

    rows = "\n".join(f'      <details class="fq"><summary><span>{q}</span><i class="fq-icon" aria-hidden="true"></i></summary><div class="fq-a"><p>{a}</p></div></details>' for q, a in faq(c))
    faqs = f"""<section class="faq sheet" id="questions" data-kind="faq" data-tone="paper">
  <div class="grid fq-grid">
    <div class="fq-head"><h2 data-split>Travaux à {v} : vos questions</h2><p>Une autre question ? <a class="link" href="tel:{phone}">{phone_txt}</a></p><p><a class="link" href="/devis-travaux/#questions">Voir toutes les questions</a></p></div>
    <div class="fq-list">
{rows}
    </div>
  </div>
</section>"""

    cities = "".join(f'<li><a class="link" href="{path(x)}">Devis travaux à {x["name"]}</a></li>' for x in CITIES if x["slug"] != c["slug"])
    metiers = "".join(f'<li><a class="link" href="/devis-travaux/{PF.SLUG[x[0]]}/">{x[5]}</a></li>' for x in PF.TRADES)
    others = f"""<section class="sheet pf-others" data-tone="light">
  <div class="grid sp-head"><h2 data-split>Autres villes</h2><p><a class="link" href="/devis-travaux/">Tous les devis de travaux</a></p></div>
  <ul class="pf-olist">{cities}</ul>
  <div class="grid sp-head" style="margin-top:40px"><h2 data-split>Par métier</h2></div>
  <ul class="pf-olist">{metiers}</ul>
</section>"""

    return CSS + "\n" + "\n\n".join([hero, figures, local, trades, parts["promise"], steps, aides, leak, brief, faqs, others, parts["end"]])


def faq(c):
    return c["faq"] + [(f"Intervenez-vous partout à {c['name']} ?",
                        "Nous vous mettons en relation avec l’artisan partenaire qui couvre votre commune et votre métier. "
                        "Si aucun ne la couvre, nous vous le disons dès l’appel et votre demande n’est transmise à personne.")]


def schema(SITE, faq_ld, bc_ld, PF, c):
    clean = lambda s: _re.sub("<[^>]+>", "", s).replace("&amp;", "&").replace("&nbsp;", " ")
    p = path(c)
    city = {"@type": "City", "name": c["name"], "sameAs": [c["wiki"], f"https://www.wikidata.org/wiki/{c['wikidata']}"]}
    graph = [
        {"@type": "WebPage", "@id": SITE + p, "url": SITE + p, "name": c["title"], "description": c["desc"], "inLanguage": "fr-FR",
         "dateModified": "@@MAJ@@", "isPartOf": {"@id": SITE + "/#website"}, "publisher": {"@id": SITE + "/#org"}, "about": city},
        {"@type": "Service", "name": f"Devis travaux à {c['name']}", "serviceType": "Mise en relation avec un artisan : toiture, façade, fenêtres, charpente, isolation",
         "description": clean(c["answer"]), "url": SITE + p, "areaServed": city,
         "audience": {"@type": "Audience", "audienceType": "Propriétaires"},
         "provider": {"@type": "Organization", "@id": SITE + "/#org", "name": "Bartier & Co", "url": SITE + "/"},
         "offers": {"@type": "Offer", "price": "0", "priceCurrency": "EUR", "description": "Gratuit pour le particulier : mise en relation, visite et devis de l'artisan"}},
        faq_ld([(q, clean(a)) for q, a in faq(c)]), bc_ld(("Devis travaux", "/devis-travaux/"), (c["name"], p))]
    return PF.link_graph(SITE, p, {"@context": "https://schema.org", "@graph": graph})

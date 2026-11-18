"""Audit AEO (moteurs de réponse) du site statique, à partir des pages générées.

Critères tirés des sources officielles lues le 18/11/2026 :
- Google, « Optimizing your website for generative AI features » et « AI features and your website » :
  page indexée et éligible à un extrait, contenu en texte, liens internes, données structurées identiques au texte visible,
  images et vidéos de qualité, Business Profile à jour.
- Microsoft Bing, « Optimizing your content for inclusion in AI search answers » (08/10/2025) :
  titre, H1 et description alignés ; intertitres explicites (pas « En savoir plus ») ; questions-réponses en 1 ou 2 phrases ;
  listes et tableaux ; phrases autonomes, pas de phrases surchargées ; pas de symboles décoratifs ; informations clés en HTML.
- Aggarwal et al., « GEO: Generative Engine Optimization » (KDD 2024) : citer des sources, des chiffres et des citations
  augmente la visibilité dans les réponses générées.
- Études de citations ChatGPT et AI Overviews (Indig, CXL, AirOps) : la réponse se trouve souvent dans le premier tiers de la page,
  et les intertitres proches de la question sont plus souvent cités.

usage : python3 aeo_audit.py <racine du site> [sortie.json]
"""
import html
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(sys.argv[1])
OUT = sys.argv[2] if len(sys.argv) > 2 else None

VAGUE = {"en savoir plus", "en bref", "le blog", "le tableau", "mesurez", "notre parole", "aperçu", "introduction", "conclusion", "plus", "autres"}
DECOR = "→←★✓✔►▸•»«"  # « » sont typographiques : comptés à part
STOP = set("le la les un une des de du d l et en à au aux pour par sur avec dans votre vos nos notre ce ces qui que quoi est sont pas plus vous nous il elle on se sa son ses leur leurs ou où mais si ne y a as".split())
OFFICIAL = ("legifrance.gouv.fr", "service-public.fr", "economie.gouv.fr", "france-renov.gouv.fr", "annuaire-entreprises.data.gouv.fr",
            "cnil.fr", "ademe.fr", "anah.gouv.fr", "insee.fr", "ecologie.gouv.fr", "entreprendre.service-public.fr")

# Questions que la cible pose vraiment (recherche de mots-clés du 17/11/2026) et termes qu'une bonne réponse doit contenir
QUESTIONS = [
    ("comment trouver des chantiers quand on est artisan", ["trouver", "chantiers"]),
    ("demande de devis exclusive", ["demande", "exclusive"]),
    ("demande de devis partagée entre artisans", ["demande", "partagée"]),
    ("qu'est-ce qu'un rendez-vous qualifié", ["rendez-vous", "qualifié"]),
    ("google ads ou meta ads pour un artisan", ["google", "meta"]),
    ("comment relancer un devis", ["relance", "devis"]),
    ("taux de signature des devis calcul", ["taux", "signature"]),
    ("coût par chantier signé", ["coût", "chantier", "signé"]),
    ("démarchage téléphonique interdit 2026", ["démarchage", "téléphonique"]),
    ("apporteur d'affaires btp", ["apporteur", "affaires"]),
    ("plateforme de devis artisan", ["plateforme", "devis"]),
    ("combien coûte une réfection de toiture", ["réfection", "toiture"]),
    ("faut-il une déclaration préalable pour refaire sa toiture", ["déclaration", "préalable"]),
    ("qu'est-ce que l'assurance décennale", ["assurance", "décennale"]),
    ("garantie de parfait achèvement", ["parfait", "achèvement"]),
    ("comment reconnaître un artisan sérieux", ["artisan", "sérieux"]),
    ("délai de rétractation devis signé à domicile", ["rétractation"]),
    ("devis obligatoire travaux dépannage", ["devis", "obligatoire"]),
    ("artisan rge c'est quoi", ["rge"]),
    ("fuite de toiture que faire", ["fuite", "toiture"]),
]


def text(s):
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", s))).replace(" ", " ").strip()


def words(s):
    return [w for w in re.findall(r"[a-zàâäçéèêëîïôöùûüœ'-]+", s.lower()) if w not in STOP and len(w) > 2]


def norm(w):
    return w.rstrip("s")


def page_url(p):
    rel = p.relative_to(ROOT)
    return "/" + ("" if str(rel.parent) == "." else str(rel.parent) + "/")


pages = {}
for p in sorted(ROOT.rglob("index.html")):
    if p.relative_to(ROOT).parts[0] in ("_build", "node_modules"):
        continue
    d = p.read_text(encoding="utf-8")
    url = page_url(p)
    head = d[: d.index("<body")]
    body = re.sub(r"<script[\s\S]*?</script>|<style[\s\S]*?</style>|<svg[\s\S]*?</svg>|<template[\s\S]*?</template>", "", d[d.index("<body"):])
    main = body[body.index("<main"): body.index("</main>")] if "<main" in body else body
    # on retire les formulaires et l'interface du texte analysé
    main_c = re.sub(r"<form[\s\S]*?</form>|<nav[\s\S]*?</nav>|<button[\s\S]*?</button>", " ", main)
    title = text(re.search(r"<title>(.*?)</title>", head, re.S).group(1))
    desc = html.unescape((re.search(r'<meta name="description" content="([^"]*)"', head) or [None, ""])[1])
    robots = (re.search(r'<meta name="robots" content="([^"]*)"', head) or [None, ""])[1]
    h1 = text((re.search(r"<h1[^>]*>(.*?)</h1>", main, re.S) or [None, ""])[1])
    heads = [text(h) for h in re.findall(r"<h[23][^>]*>(.*?)</h[23]>", main_c, re.S)]
    paras = [text(x) for x in re.findall(r"<p[^>]*>(.*?)</p>", main_c, re.S)]
    paras = [x for x in paras if len(x.split()) >= 6]
    full = text(main_c)
    ld = []
    for blk in re.findall(r'<script type="application/ld\+json">(.*?)</script>', d, re.S):
        j = json.loads(blk)
        ld += j.get("@graph", [j])
    types = sorted({n.get("@type") for n in ld if isinstance(n.get("@type"), str)})
    faq = [q for n in ld if n.get("@type") == "FAQPage" for q in n["mainEntity"]]
    faq_vis = re.findall(r'<details class="fq"><summary><span>(.*?)</span>.*?<div class="fq-a">(.*?)</div>', main, re.S)
    heads = heads + [text(q) for q, _ in faq_vis]  # une question de FAQ joue le rôle d'un intertitre
    ans = [text(a) for _, a in faq_vis]
    ans_ok = [a for a in ans if len(a.split()) <= 60 and len(re.findall(r"[.!?](\s|$)", a)) <= 3]
    blocks = [text(b) for _, b in re.findall(r"<(p|li|dd|blockquote|summary)\b[^>]*>(.*?)</\1>", main_c, re.S)]
    sentences = [s for b in blocks for s in re.split(r"(?<=[.!?])\s+", b)]
    long_s = [s for s in sentences if len(s.split()) > 35]
    ext = re.findall(r'<a [^>]*href="(https?://[^"]+)"', main_c)
    official = [u for u in ext if any(o in u for o in OFFICIAL)]
    first_third = full[: max(1, len(full) // 3)]
    tw, hw, dw = set(map(norm, words(title))), set(map(norm, words(h1))), set(map(norm, words(desc)))
    align = len(tw & (hw | dw)) / max(1, len(tw - {"bartier", "co"}))
    vis_dates = bool(re.search(r"<time[^>]*datetime=|Mis à jour|mise à jour", main))
    pages[url] = dict(
        title=title, h1=h1, robots=robots, words=len(full.split()), types=types,
        indexable="noindex" not in robots, snippet_ok=not re.search(r"nosnippet|max-snippet:0", robots),
        align=round(align, 2),
        first_para_words=len(paras[0].split()) if paras else 0,
        q_heads=sum(1 for h in heads if h.endswith("?")), heads=len(heads),
        vague=[h for h in heads if h.lower().strip(" .") in VAGUE],
        faq_schema=len(faq), faq_visible=len(faq_vis), faq_short=f"{len(ans_ok)}/{len(ans)}",
        lists=len(re.findall(r"<(ul|ol)\b", main_c)), tables=main_c.count("<table"),
        long_sentences=len(long_s), long_ex=long_s[:3], decor=sum(full.count(c) for c in "→★✓✔►▸•"),
        ext_links=len(ext), official_links=len(official), dates=vis_dates,
        img_no_alt=len(re.findall(r'<img(?![^>]*\balt=")[^>]*>', main)),
        first_third=first_third, full=full, heads_list=heads,
    )

# couverture des questions : une page répond si un intertitre ou une question de FAQ contient les termes,
# et si un passage court (≤ 60 mots) qui les contient suit
cover = []
for q, terms in QUESTIONS:
    best = None
    for url, P in pages.items():
        cands = P["heads_list"]
        has = lambda s: all(re.search(r"(?<![a-zàâäçéèêëîïôöùûüœ])" + re.escape(t), s.lower()) for t in terms)
        hit_head = any(has(h) for h in cands)
        passages = [s for s in re.split(r"(?<=[.!?])\s+", P["full"]) if has(s) and len(s.split()) <= 60]
        if hit_head and passages:
            best = (url, "intertitre + réponse")
            break
        if passages and not best:
            best = (url, "réponse sans intertitre")
    cover.append((q, best))

ok_q = sum(1 for _, b in cover if b and b[1] == "intertitre + réponse")
part_q = sum(1 for _, b in cover if b and b[1] != "intertitre + réponse")

print(f"{'page':44} {'mots':>5} idx ext. align 1erP Q-int vagues FAQ(sch/vis/courtes) list tab longues décor sources dates")
for url, P in pages.items():
    print(f"{url[:44]:44} {P['words']:5} {'oui' if P['indexable'] else 'NON':>3} {'oui' if P['snippet_ok'] else 'NON':>4} {P['align']:5} {P['first_para_words']:4} "
          f"{P['q_heads']:2}/{P['heads']:<3} {len(P['vague']):2}     {P['faq_schema']:2}/{P['faq_visible']:<2}/{P['faq_short']:7}   {P['lists']:3} {P['tables']:3} {P['long_sentences']:6} {P['decor']:4} "
          f"{P['official_links']:3}/{P['ext_links']:<3} {'oui' if P['dates'] else '-'}")
print("\nIntertitres vagues :", {u: P["vague"] for u, P in pages.items() if P["vague"]})
print(f"\nCouverture des {len(QUESTIONS)} questions cibles : {ok_q} avec intertitre et réponse courte, {part_q} avec réponse seule, {len(QUESTIONS) - ok_q - part_q} sans réponse")
for q, b in cover:
    print(f"  {'OK ' if b and b[1].startswith('inter') else ('~  ' if b else 'NON')} {q:58} {b[0] if b else ''}")
tot = {
    "pages": len(pages), "indexables": sum(P["indexable"] for P in pages.values()),
    "q_heads": sum(P["q_heads"] for P in pages.values()), "heads": sum(P["heads"] for P in pages.values()),
    "vague": sum(len(P["vague"]) for P in pages.values()), "faq": sum(P["faq_schema"] for P in pages.values()),
    "long": sum(P["long_sentences"] for P in pages.values()), "decor": sum(P["decor"] for P in pages.values()),
    "official": sum(P["official_links"] for P in pages.values()), "cover_ok": ok_q, "cover_part": part_q, "questions": len(QUESTIONS),
}
print("\nTotaux :", tot)
if OUT:
    json.dump({"pages": {u: {k: v for k, v in P.items() if k not in ("full", "first_third", "heads_list")} for u, P in pages.items()},
               "cover": cover, "tot": tot}, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)

"""llms-full.txt : le contenu utile du site en texte simple, pour les moteurs de réponse (ChatGPT, Perplexity, Claude, Mistral).

Chaque page est reprise avec son titre, son adresse, ses intertitres, ses paragraphes, ses listes, ses tableaux et ses questions-réponses.
Le formulaire, la navigation, le pied de page et les éléments d'interface ne sont pas repris.
"""
import html
import re
from html.parser import HTMLParser

SKIP_CLASSES = ("m-only", "check sheet", "pf-card", "pf-sticky", "crumbs", "pf-band", "actions", "lg-nav", "ph ", "mk-", "ad-card", "dq", "wa", "calc", "rng")
BLOCK = {"p", "li", "dt", "dd", "summary", "figcaption", "blockquote", "td", "th"}


class _Text(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.out, self.buf, self.tag, self.skip, self.row = [], [], None, 0, None
        self.stack = []

    def handle_starttag(self, tag, attrs):
        cls = dict(attrs).get("class", "") or ""
        hidden = tag in ("script", "style", "svg", "form", "nav", "button", "figure", "template") or (tag == "a" and "btn" in cls) or any(c in cls for c in SKIP_CLASSES) or dict(attrs).get("aria-hidden") == "true" or "hidden" in dict(attrs)
        if tag in ("br", "img", "input", "hr", "meta", "link"):
            if tag == "br":
                self.buf.append(" ")
            return
        self.stack.append((tag, hidden))
        if hidden:
            self.skip += 1
        if self.skip:
            return
        if tag == "tr":
            self.row = []
        if tag in ("h1", "h2", "h3", "h4") or tag in BLOCK:
            self.flush()
            self.tag = tag

    def handle_endtag(self, tag):
        while self.stack:
            t, hidden = self.stack.pop()
            if hidden:
                self.skip -= 1
            if t == tag:
                break
        if self.skip:
            return
        self.buf.append(" ")
        if tag in ("td", "th") and self.row is not None:
            self.row.append(self.text())
            self.buf = []
            return
        if tag == "tr" and self.row:
            self.out.append("- " + " | ".join(c for c in self.row if c))
            self.row = None
            return
        if tag in ("h1", "h2", "h3", "h4") or tag in BLOCK:
            self.flush()

    def handle_data(self, data):
        if not self.skip:
            self.buf.append(data)

    def text(self):
        return re.sub(r" ([.,)])", r"\1", re.sub(r"\s+", " ", "".join(self.buf))).strip()

    def flush(self):
        txt = self.text()
        self.buf = []
        if not txt or self.row is not None:
            return
        t = self.tag
        if t == "h1":
            pass  # le titre de la page est déjà donné
        elif t == "h2":
            self.out.append("\n### " + txt)
        elif t in ("h3", "h4"):
            self.out.append("\n#### " + txt)
        elif t in ("li", "dd"):
            self.out.append("- " + txt)
        elif t in ("summary", "dt"):
            self.out.append("\n**" + txt + "**")
        else:
            self.out.append(txt)
        self.tag = None


def page(root, site, path):
    doc = (root / path.strip("/") / "index.html").read_text(encoding="utf-8")
    title = html.unescape(re.search(r"<title>(.*?)</title>", doc, re.S).group(1)).replace(" | Bartier & Co", "")
    desc = html.unescape((re.search(r'<meta name="description" content="([^"]*)"', doc) or [None, ""])[1])
    main = doc[doc.index("<main"):doc.index("</main>")] if "<main" in doc else doc
    p = _Text()
    p.feed(main)
    p.flush()
    lines, last = [], None
    for l in p.out:
        if l != last:
            lines.append(l)
        last = l
    return f"## {title}\n\nAdresse : {site}{path}\n\n{desc}\n\n" + "\n".join(lines).strip() + "\n"


def build(root, site, paths):
    head = ("# Bartier & Co : contenu complet du site\n\n"
            "> Bartier & Co trouve des clients aux artisans du bâtiment (couverture, façade, menuiserie extérieure, charpente, isolation) en France : "
            "annonces locales, rappel de chaque demande en moins de 5 minutes du lundi au vendredi de 8 h à 19 h, visite fixée dans l'agenda de l'artisan, "
            "un seul artisan par métier et par secteur. Pour les particuliers, la mise en relation avec un artisan partenaire est gratuite.\n\n"
            "Ce fichier reprend le texte des pages du site. La version courte est " + site + "/llms.txt.\n")
    return head + "\n" + "\n---\n\n".join(page(root, site, p) for p in paths)

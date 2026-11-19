"""Retire, page par page, les règles CSS qui ne peuvent rien toucher sur la page.

Le site met tout son CSS dans chaque page (environ 150 Ko). La plupart des règles visent d'autres pages.
Règle de prudence : une règle est gardée si au moins un de ses sélecteurs peut correspondre, c'est-à-dire si
chaque classe et chaque identifiant qu'il exige figure quelque part dans la page (HTML, scripts compris) ou
dans les scripts externes. Les classes ajoutées par script (is-, has-, cc-, ld-, menu-, js-) sont toujours
gardées, ainsi que tout ce qui est à l'intérieur de :not(), :is(), :where() et :has(), les @keyframes et les
@font-face. Le texte des règles gardées n'est jamais réécrit.
"""
import re

KEEP_PREFIX = ("is-", "has-", "cc-", "ld-", "menu-", "js-")
_WORD = re.compile(r"[A-Za-z_][\w-]*")
_STYLE = re.compile(r"(<style\b[^>]*>)([\s\S]*?)(</style>)")
_FUNC = re.compile(r":(?:not|is|where|has|matches)\(")
_NEED = re.compile(r"([.#])([A-Za-z_][\w-]*)")


def tokens(doc, extra=""):
    """Mots présents dans la page hors feuilles de style (HTML, scripts, données) et dans les scripts externes."""
    bare = _STYLE.sub(lambda m: m.group(1) + m.group(3), doc)
    return set(_WORD.findall(bare)) | set(_WORD.findall(extra))


def _skip_string(s, i):
    q = s[i]
    i += 1
    while i < len(s) and s[i] != q:
        i += 2 if s[i] == "\\" else 1
    return i + 1


def _block_end(s, i):
    """s[i] == '{' : renvoie l'index juste après l'accolade fermante correspondante."""
    depth = 0
    while i < len(s):
        c = s[i]
        if c in "\"'":
            i = _skip_string(s, i)
            continue
        if c == "/" and s.startswith("/*", i):
            j = s.find("*/", i + 2)
            i = len(s) if j < 0 else j + 2
            continue
        if c == "{":
            depth += 1
        elif c == "}":
            depth -= 1
            if depth == 0:
                return i + 1
        i += 1
    raise ValueError("accolade non fermée")


def _split_selectors(prelude):
    out, depth, cur, i = [], 0, [], 0
    while i < len(prelude):
        c = prelude[i]
        if c in "\"'":
            j = _skip_string(prelude, i)
            cur.append(prelude[i:j])
            i = j
            continue
        if c in "([":
            depth += 1
        elif c in ")]":
            depth -= 1
        if c == "," and depth == 0:
            out.append("".join(cur))
            cur = []
        else:
            cur.append(c)
        i += 1
    out.append("".join(cur))
    return [x.strip() for x in out if x.strip()]


def _strip_groups(sel):
    """Retire le contenu des [attributs] et des :not()/:is()/:where()/:has(), qui n'exigent rien de la page."""
    sel = re.sub(r"\[[^\]]*\]", "", sel)
    while True:
        m = _FUNC.search(sel)
        if not m:
            return sel
        i, depth = m.end(), 1
        while i < len(sel) and depth:
            depth += {"(": 1, ")": -1}.get(sel[i], 0)
            i += 1
        sel = sel[:m.start()] + sel[i:]


def _can_match(sel, have):
    for kind, name in _NEED.findall(_strip_groups(sel)):
        if name.startswith(KEEP_PREFIX):
            continue
        if name not in have:
            return False
    return True


def purge(css, have):
    out, i, n = [], 0, len(css)
    while i < n:
        c = css[i]
        if c.isspace():
            i += 1
            continue
        if css.startswith("/*", i):
            j = css.find("*/", i + 2)
            i = n if j < 0 else j + 2
            continue
        j = i
        while j < n and css[j] not in "{;":
            j = _skip_string(css, j) if css[j] in "\"'" else j + 1
        if j >= n:
            out.append(css[i:])
            break
        prelude = css[i:j].strip()
        if css[j] == ";":
            out.append(css[i:j + 1])
            i = j + 1
            continue
        end = _block_end(css, j)
        body = css[j + 1:end - 1]
        if prelude.startswith(("@media", "@supports", "@container", "@layer", "@document")):
            inner = purge(body, have)
            if inner.strip():
                out.append(prelude + "{" + inner + "}")
        elif prelude.startswith("@"):
            out.append(css[i:end])
        elif any(_can_match(s, have) for s in _split_selectors(prelude)):
            out.append(css[i:end])
        i = end
    return "".join(out)


def purge_doc(doc, extra_js=""):
    have = tokens(doc, extra_js)

    def one(m):
        if 'id="fonts"' in m.group(1):
            return m.group(0)
        return m.group(1) + purge(m.group(2), have) + m.group(3)

    return _STYLE.sub(one, doc)

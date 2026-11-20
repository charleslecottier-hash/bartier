"""Icônes isométriques des pages d'estimation : une maison dessinée en code, la partie concernée par les travaux
prend la couleur d'accent du client, et un pictogramme précise le type de travaux. Aucune image externe."""
import math

C30 = math.cos(math.radians(30))
L, W, h, RP = 4.0, 3.0, 2.1, 1.1          # longueur, largeur, hauteur des murs, pente du toit (hauteur par unité)
H = h + 1.5 * RP                           # faîtage
OX, OY, TH = 0.25, 0.3, 0.14               # débords du toit, épaisseur de la couverture
HE = H - (1.5 + OY) * RP                   # bas de la pente avant (égout)

GLYPH = {  # pictogrammes au trait, grille de 24
    "leaf": "M5 19c0-8 5-13 14-14 0 9-5 14-13 14z M5 19l7-7",
    "shield": "M12 3l7 3v5c0 4.5-3 8-7 10-4-2-7-5.5-7-10V6z",
    "drop": "M12 3c3.5 4.2 6 7.4 6 10.5a6 6 0 0 1-12 0C6 10.4 8.5 7.2 12 3z",
    "refresh": "M20 12a8 8 0 1 1-2.4-5.7 M20 4v4h-4",
    "layers": "M12 4l9 5-9 5-9-5z M3 14l9 5 9-5",
    "plus": "M12 5v14 M5 12h14",
    "crack": "M8 3l4 6-3 4 5 8",
    "roller": "M4 4h13v5H4z M17 6.5h3v5h-8v3 M11 14.5h2V21h-2z",
    "therm": "M10 13.5V5a2 2 0 1 1 4 0v8.5a4 4 0 1 1-4 0z",
    "bug": "M9 8a3 3 0 0 1 6 0 M8 9h8v6a4 4 0 0 1-8 0z M4 12h4 M16 12h4 M5 7l3 2 M19 7l-3 2 M5 18l3-2 M19 18l-3-2",
    "wrench": "M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.8-3.8a6 6 0 0 1-7.9 7.9l-6.9 6.9a2.1 2.1 0 0 1-3-3l6.9-6.9a6 6 0 0 1 7.9-7.9z",
    "question": "M9 9a3 3 0 1 1 4.5 2.6c-1 .6-1.5 1.2-1.5 2.4 M12 18h.01",
}


def _mix(a, b, t):
    a, b = [int(a[i:i + 2], 16) for i in (1, 3, 5)], [int(b[i:i + 2], 16) for i in (1, 3, 5)]
    return "#" + "".join(f"{round(x + (y - x) * t):02x}" for x, y in zip(a, b))


def _pal(accent):
    n = dict(slabT="#DDEBD6", slabF="#B9D0B0", slabR="#A9C39F", wallF="#FBF8F3", wallS="#ECE6DB", roofF="#5A6373", roofL="#4B5363",
             roofE="#3F4653", glass="#C9D7F6", frame="#FFFFFF", door="#3C4453", chimF="#ECE6DB", chimS="#DCD4C6", chimT="#4B5363")
    a = dict(A=accent, A2=_mix(accent, "#000000", .2), A3=_mix(accent, "#000000", .34), Al=_mix(accent, "#ffffff", .2),
             Ap=_mix(accent, "#ffffff", .84), Aw=_mix(accent, "#ffffff", .55))
    return n, a


_UID = [0]


def _shade(c, t):
    return _mix(c, "#ffffff", t) if t > 0 else _mix(c, "#000000", -t)


def house(focus="none", badge=None, accent="#2D5BE3", s=10.0, title=""):
    """focus : roof, frame, roofframe, wall, windows, newwin, bay, door, shutters, attic, rampant, floor, extension, none."""
    N, F = _pal(accent)
    shapes = []  # (liste de points 3D, attributs)
    BASE = {"moss": "roofn", "beads": "roof", "leak": "roofn", "strip": "strip", "sarking": "roof", "paint": "wallpaint",
            "render": "wall", "panels": "wallp", "cracks": "wallc", "bugs": "frame", "brace": "frame"}
    variant, focus = focus, BASE.get(focus, focus)

    def poly(pts, fill, extra="", flat=False):
        shapes.append(("p", pts, fill, extra, flat))

    def line(a, b, col, w=1.0, extra=""):
        shapes.append(("l", [a, b], f'stroke="{col}" stroke-width="{w}" stroke-linecap="round"{extra}', "", True))

    def ball(c, r, col):  # buisson : une sphère éclairée en haut à gauche
        shapes.append(("c", [c], col, r, True))

    def dot(c, rx, ry, col, op=1.0):  # tache, goutte, perle : ellipse à plat sur l'écran
        shapes.append(("e", [c], col, (rx, ry, op), True))

    def rp(x, t, dz=.01):  # point sur le pan avant du toit (t = 0 au faîtage, 1 à l'égout)
        return (x, 1.5 + t * (1.5 + OY), H - t * (1.5 + OY) * RP + dz)

    ext = focus == "extension"
    xs = L + (2.1 if ext else 0.7)
    # socle
    poly([(-0.6, -0.6, 0), (xs, -0.6, 0), (xs, 3.7, 0), (-0.6, 3.7, 0)], N["slabT"])
    poly([(-0.6, 3.7, 0), (xs, 3.7, 0), (xs, 3.7, -0.28), (-0.6, 3.7, -0.28)], N["slabF"])
    poly([(xs, 3.7, 0), (xs, -0.6, 0), (xs, -0.6, -0.28), (xs, 3.7, -0.28)], N["slabR"])
    shapes.append(("shadow", [(xs / 2 - 0.3, 1.55, -0.28)], "", (xs + 1.4) * 0.5, True))
    # cheminée (derrière le faîtage)
    cz0, cz1 = H - (1.5 - 1.05) * RP - 0.3, H + 0.45
    poly([(0.7, 1.05, cz0), (1.25, 1.05, cz0), (1.25, 1.05, cz1), (0.7, 1.05, cz1)], N["chimF"])
    poly([(1.25, 1.05, cz0), (1.25, 0.55, cz0), (1.25, 0.55, cz1), (1.25, 1.05, cz1)], N["chimS"])
    poly([(0.7, 0.55, cz1), (1.25, 0.55, cz1), (1.25, 1.05, cz1), (0.7, 1.05, cz1)], N["chimT"])

    wall_f = F["Al"] if focus == "wall" else N["wallF"]
    wall_s = F["A"] if focus == "wall" else N["wallS"]
    if variant == "render":
        wall_f, wall_s = F["Aw"], F["Al"]
    if focus == "attic":  # couche d'isolant sur le plancher des combles, qui suit la pente du toit ; vue à travers le toit
        t = 0.42
        y0 = 1.5 - (H - h - t) / RP
        y1 = 1.5 + (H - h - t) / RP
        poly([(0, y0, h + t), (L, y0, h + t), (L, y1, h + t), (0, y1, h + t)], F["A"])
        poly([(0, y1, h + t), (L, y1, h + t), (L, W, h), (0, W, h)], F["A2"])
        zz, x, k = [], 0.15, 0
        while x <= L - 0.1:
            f_ = 0.72 if k % 2 else 0.22
            zz.append((x, y1 + f_ * (W - y1), h + t - f_ * t))
            x, k = x + 0.3, k + 1
        for p1, p2 in zip(zz, zz[1:]):
            line(p1, p2, "#FFFFFF", 1.3)
    # pignon (côté droit)
    poly([(L, W, 0), (L, 0, 0), (L, 0, h), (L, 1.5, H), (L, W, h)], wall_s)
    if focus in ("attic", "frame", "roofframe"):
        tri = [(L + .01, 0, h), (L + .01, 1.5, H), (L + .01, W, h)]
        if focus == "attic":
            pass
        else:
            poly(tri, F["Ap"])
            line((L + .02, 1.5, H - .05), (L + .02, 1.5, h + .02), F["A"], 1.6)
            line((L + .02, 1.5, h + 0.5), (L + .02, 0.55, h + 0.95), F["A"], 1.4)
            line((L + .02, 1.5, h + 0.5), (L + .02, 2.45, h + 0.95), F["A"], 1.4)
            line((L + .02, 0.05, h + .02), (L + .02, 2.95, h + .02), F["A"], 1.8)
    if not ext:  # fenêtre du pignon
        gcol = F["A"] if focus in ("windows", "newwin") else N["glass"]
        a, b, c, d = 1.05, 1.95, 0.85, 1.55
        poly([(L + .01, b, c), (L + .01, a, c), (L + .01, a, d), (L + .01, b, d)], N["frame"])
        poly([(L + .02, b - .08, c + .08), (L + .02, a + .08, c + .08), (L + .02, a + .08, d - .08), (L + .02, b - .08, d - .08)], gcol)
        line((L + .03, 1.5, c + .08), (L + .03, 1.5, d - .08), N["frame"], 1.0)
        if focus == "newwin":
            poly([(L + .03, b + .14, c - .14), (L + .03, a - .14, c - .14), (L + .03, a - .14, d + .14), (L + .03, b + .14, d + .14)], "none",
                 f' stroke="{F["A"]}" stroke-width="1.2" stroke-dasharray="3 2.4"', flat=True)
    if focus == "floor":
        poly([(L + .01, W, 0), (L + .01, 0, 0), (L + .01, 0, .34), (L + .01, W, .34)], F["A"])
    if ext:  # extension accolée au pignon
        x0, x1, y0, y1, ze = L, L + 1.6, 1.4, W, 1.35
        poly([(x1, y1, 0), (x1, y0, 0), (x1, y0, ze), (x1, y1, ze)], F["A"])
        poly([(x0, y0, ze), (x1, y0, ze), (x1, y1, ze), (x0, y1, ze)], F["A2"])
        poly([(x0, y1, 0), (x1, y1, 0), (x1, y1, ze), (x0, y1, ze)], F["Al"])
        poly([(x0 + .4, y1 + .01, .5), (x0 + 1.2, y1 + .01, .5), (x0 + 1.2, y1 + .01, 1.0), (x0 + .4, y1 + .01, 1.0)], N["glass"])
    # façade avant
    poly([(0, W, 0), (L, W, 0), (L, W, h), (0, W, h)], wall_f)
    if focus == "wallpaint":  # moitié repeinte, rouleau en cours
        poly([(0, W + .005, 0), (2.25, W + .005, 0), (2.25, W + .005, h), (0, W + .005, h)], F["Al"])
        poly([(2.12, W + .2, .95), (2.42, W + .2, .95), (2.42, W + .2, 1.32), (2.12, W + .2, 1.32)], F["A2"], flat=True)
        poly([(2.42, W + .2, .95), (2.42, W + .02, .95), (2.42, W + .02, 1.32), (2.42, W + .2, 1.32)], F["A3"], flat=True)
        line((2.27, W + .2, .95), (2.27, W + .5, .55), "#3C4453", 1.4)
        line((2.27, W + .5, .55), (2.27, W + .5, .1), "#C8955A", 2.4)
    if variant == "render":  # enduit : grain
        for i in range(70):
            x, z = .1 + (i * 0.37) % 3.8, .1 + (i * 0.29) % 1.9
            dot((x, W + .02, z), .045 * s, .03 * s, F["A2"], .35)
    if focus == "wallp":  # panneaux d'isolant posés sur la façade, chantier en cours
        for r in range(4):
            off = .35 if r % 2 else 0
            z0 = r * .52
            x = -off
            while x < 2.7:
                a_, b_ = max(x, 0), min(x + .7, 2.7)
                if b_ - a_ > .1:
                    poly([(a_ + .02, W + .07, z0 + .02), (b_ - .02, W + .07, z0 + .02), (b_ - .02, W + .07, min(z0 + .5, h) - .02), (a_ + .02, W + .07, min(z0 + .5, h) - .02)],
                         F["Aw"], f' stroke="{F["A"]}" stroke-width=".7"', flat=True)
                x += .7
        poly([(2.7, W + .07, 0), (2.7, W, 0), (2.7, W, h), (2.7, W + .07, h)], F["A2"])
    if focus == "wallc":  # fissures
        for pts in ([(1.25, .85), (1.42, .62), (1.33, .42), (1.55, .18), (1.5, 0)], [(3.0, 1.4), (2.82, 1.62), (2.92, 1.82), (2.7, 2.05)], [(.45, 1.6), (.3, 1.82), (.38, 2.0)]):
            for a_, b_ in zip(pts, pts[1:]):
                line((a_[0], W + .02, a_[1]), (b_[0], W + .02, b_[1]), F["A"], 4.4, ' opacity=".3"')
            for a_, b_ in zip(pts, pts[1:]):
                line((a_[0], W + .03, a_[1]), (b_[0], W + .03, b_[1]), "#3B3129", 1.6)
    if focus == "floor":
        poly([(0, W + .01, 0), (L, W + .01, 0), (L, W + .01, .34), (0, W + .01, .34)], F["Al"])

    def win(a, b, c, d, col, mull=True):
        poly([(a, W + .01, c), (b, W + .01, c), (b, W + .01, d), (a, W + .01, d)], N["frame"])
        poly([(a + .08, W + .02, c + .08), (b - .08, W + .02, c + .08), (b - .08, W + .02, d - .08), (a + .08, W + .02, d - .08)], col)
        if mull:
            m = (a + b) / 2
            line((m, W + .03, c + .08), (m, W + .03, d - .08), N["frame"], 1.0)

    wcol = F["A"] if focus == "windows" else N["glass"]
    if focus == "bay":
        win(0.35, 2.55, 0.03, 1.62, F["A"], mull=False)
        for m in (1.08, 1.82):
            line((m, W + .03, 0.11), (m, W + .03, 1.54), N["frame"], 1.0)
    else:
        for a, b in ((0.45, 1.25), (1.7, 2.5)):
            win(a, b, 0.85, 1.6, wcol)
            if focus == "shutters":
                for p, q in ((a - .34, a - .05), (b + .05, b + .34)):
                    poly([(p, W + .01, .85), (q, W + .01, .85), (q, W + .01, 1.6), (p, W + .01, 1.6)], F["A"])
                    for z in (1.1, 1.35):
                        line((p + .05, W + .02, z), (q - .05, W + .02, z), F["A3"], .8)
    poly([(3.0, W + .01, 0), (3.6, W + .01, 0), (3.6, W + .01, 1.4), (3.0, W + .01, 1.4)], F["A"] if focus == "door" else N["door"])

    if not ext:
        ball((-0.45, 3.25, 0.42), 0.62, "#4E9A5B")
        ball((-0.05, 3.45, 0.3), 0.44, "#5FAE6B")
    # toiture
    roof = [(-OX, 1.5, H), (L + OX, 1.5, H), (L + OX, W + OY, HE), (-OX, W + OY, HE)]
    on = focus in ("roof", "rampant", "roofframe", "strip")
    rf, rl, re_ = (F["A"], F["A2"], F["A3"]) if on else (N["roofF"], N["roofL"], N["roofE"])
    if focus == "frame":
        poly(roof, F["Ap"])
        for i in range(6):
            x = -0.1 + i * (L + 0.2) / 5
            line((x, 1.5, H), (x, W + OY, HE), F["A"], 1.6)
        for t in (0.36, 0.7):
            y, z = 1.5 + t * (1.5 + OY), H - t * (1.5 + OY) * RP
            line((-OX, y, z), (L + OX, y, z), F["A2"], 1.1)
        line((-OX, 1.5, H), (L + OX, 1.5, H), F["A3"], 2.0)
        rl, re_ = F["A2"], F["A3"]
    elif focus == "strip":  # couverture en cours : tuiles neuves à gauche, liteaux à droite
        xm = 1.9
        poly([(-OX, 1.5, H), (xm, 1.5, H), (xm, W + OY, HE), (-OX, W + OY, HE)], F["A"])
        for t in (0.25, 0.5, 0.75):
            line(rp(-OX, t), rp(xm, t), F["A2"], .8, ' opacity=".7"')
        poly([(xm, 1.5, H), (L + OX, 1.5, H), (L + OX, W + OY, HE), (xm, W + OY, HE)], "#EAD7B4")
        for i in range(4):
            x = xm + .35 + i * .6
            line(rp(x, 0), rp(x, 1), "#C9A06A", 1.6)
        for k in range(1, 9):
            line(rp(xm + .02, k / 9), rp(L + OX, k / 9), "#A9784A", .9)
        line(rp(xm, 0), rp(xm, 1), F["A3"], 1.1)
    elif focus == "attic":  # toit transparent : on voit l'isolant dessous
        poly(roof, N["roofF"], ' fill-opacity=".22"')
        for i in range(6):
            x = -0.1 + i * (L + 0.2) / 5
            line((x, 1.5, H), (x, W + OY, HE), N["roofL"], .9, ' opacity=".55"')
        line((-OX, 1.5, H), (L + OX, 1.5, H), N["roofE"], 1.2)
        line((-OX, W + OY, HE), (L + OX, W + OY, HE), N["roofE"], 1.0)
    else:
        poly(roof, rf)
        for t in (0.25, 0.5, 0.75):
            y, z = 1.5 + t * (1.5 + OY), H - t * (1.5 + OY) * RP
            line((-OX, y, z), (L + OX, y, z), rl, .8, ' opacity=".7"')
        if focus == "roofframe":
            for i in range(6):
                x = -0.1 + i * (L + 0.2) / 5
                line((x, 1.5, H), (x, W + OY, HE), F["Aw"], 1.0, ' opacity=".8"')
        if focus == "rampant":  # fenêtre de toit : des pièces sous le toit
            poly([rp(1.5, .3), rp(2.3, .3), rp(2.3, .66), rp(1.5, .66)], N["frame"])
            poly([rp(1.58, .36), rp(2.22, .36), rp(2.22, .6), rp(1.58, .6)], N["glass"])
    if variant == "moss":  # avant / après : mousse à gauche, toit propre à droite
        poly([rp(2.15, 0, .005), rp(L + OX, 0, .005), rp(L + OX, 1, .005), rp(2.15, 1, .005)], F["A"])
        for t in (0.25, 0.5, 0.75):
            line(rp(2.15, t), rp(L + OX, t), F["A2"], .8, ' opacity=".7"')
        for i, (x, t, k) in enumerate([(-.05, .2, 1.2), (.45, .55, 1.5), (1.05, .3, 1.1), (1.55, .7, 1.4), (.2, .82, 1.0), (.85, .88, .9), (1.75, .2, .9),
                                       (1.25, .55, .8), (.55, .14, .8), (1.9, .48, .7)]):
            dot(rp(x, t, .02), .34 * s * k, .2 * s * k, "#6E8C3F" if i % 3 else "#8EAA55", .95)
        line(rp(2.15, 0, .02), rp(2.15, 1, .02), "#FFFFFF", 1.2, ' opacity=".75"')
    if variant == "beads":  # traitement hydrofuge : l'eau perle
        for i in range(16):
            x, t = .1 + (i * .53) % 4.1, .12 + (i * .23) % .78
            dot(rp(x, t, .02), .1 * s, .075 * s, "#FFFFFF", .9)
        for k in (.2, .55):
            line(rp(.4 + k * 3, .05, .02), rp(.1 + k * 3, .95, .02), "#FFFFFF", 1.4, ' opacity=".35"')
    if variant == "leak":  # tuiles manquantes, l'eau passe
        poly([rp(1.3, .28), rp(2.6, .28), rp(2.6, .68), rp(1.3, .68)], F["A"])
        poly([rp(1.42, .34, .02), rp(2.48, .34, .02), rp(2.48, .62, .02), rp(1.42, .62, .02)], "#1C2330")
        line(rp(1.42, .48, .03), rp(2.48, .48, .03), "#3A4352", 1.0)
        for k, z in enumerate((HE - .35, HE - .8, HE - 1.25)):
            dot((1.95 + k * .03, W + OY + .1, z), .13 * s, .19 * s, F["A"], 1 - k * .22)
    th, eave_c, side_c = TH, re_, rl
    if variant == "sarking":  # isolant posé sur les chevrons : la couverture s'épaissit
        th, eave_c, side_c = .36, F["Aw"], F["Aw"]
    poly([(-OX, W + OY, HE), (L + OX, W + OY, HE), (L + OX, W + OY, HE - th), (-OX, W + OY, HE - th)], eave_c)
    poly([(L + OX, 1.5, H), (L + OX, W + OY, HE), (L + OX, W + OY, HE - th), (L + OX, 1.5, H - th)], side_c)
    poly([(L + OX, 1.5, H), (L + OX, -OY, HE), (L + OX, -OY, HE - th), (L + OX, 1.5, H - th)], side_c if variant == "sarking" else re_)
    if variant == "sarking":
        zz, x, k = [], -OX + .1, 0
        while x <= L + OX - .05:
            zz.append((x, W + OY + .01, HE - (.27 if k % 2 else .09)))
            x, k = x + .22, k + 1
        for p1, p2 in zip(zz, zz[1:]):
            line(p1, p2, "#FFFFFF", 1.0)
        line((-OX, W + OY + .01, HE - .005), (L + OX, W + OY + .01, HE - .005), F["A3"], 1.0)
    if variant in ("bugs", "brace"):
        xs_ = [-0.1 + i * (L + 0.2) / 5 for i in range(6)]
        if variant == "bugs":  # bois piqué par les insectes, traitement en cours
            for i, x in enumerate(xs_):
                for t in (.28, .5, .74):
                    if (i + int(t * 10)) % 2 == 0:
                        dot(rp(x, t, .03), .1 * s, .1 * s, "#2B1E14", .95)
            for i in range(9):
                dot(rp(2.3 + (i % 3) * .28, .3 + (i // 3) * .14, .05), .07 * s, .07 * s, "#16A34A", .55)
        else:  # renfort : une pièce de bois neuve contre un chevron
            x = xs_[2]
            line(rp(x, 0, .02), rp(x, 1, .02), F["A3"], 3.0)
            line(rp(x + .16, .05, .03), rp(x + .16, .95, .03), "#C8955A", 2.6)
            for t in (.3, .55, .8):
                line(rp(x - .02, t, .04), rp(x + .2, t, .04), "#7A5634", 1.2)
    line((-OX, 1.5, H + .02), (L + OX, 1.5, H + .02), re_, 1.4)
    if focus not in ("frame", "attic"):  # reflet le long du faîtage
        line((-OX + .1, 1.62, H - .12), (L + OX - .1, 1.62, H - .12), "#FFFFFF", .9, ' opacity=".28"')

    # projection et cadrage
    def pr(p):
        x, y, z = p
        return ((x - y) * C30 * s, (x + y) * 0.5 * s - z * s)
    pts = [pr(p) for sh in shapes for p in sh[1]]
    minx, maxx = min(p[0] for p in pts), max(p[0] for p in pts)
    miny, maxy = min(p[1] for p in pts), max(p[1] for p in pts)
    pad, br = 3, 11
    if badge:
        miny = min(miny, -(br * 2 + 2) + miny + 10)
    vx, vy, vw, vh = minx - pad, miny - pad, maxx - minx + 2 * pad, maxy - miny + 2 * pad
    _UID[0] += 1
    u = f"i{_UID[0]}"
    grads, defs, out = {}, [], []

    def grad(c):
        if c not in grads:
            gid = f"{u}g{len(grads)}"
            grads[c] = gid
            defs.append(f'<linearGradient id="{gid}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{_shade(c, .12)}"/><stop offset="1" stop-color="{_shade(c, -.07)}"/></linearGradient>')
        return grads[c]
    for kind, ps, a1, a2, flat in shapes:
        q = [pr(p) for p in ps]
        if kind == "p":
            fill = a1 if flat or not a1.startswith("#") else f"url(#{grad(a1)})"
            stroke = "" if "stroke=" in a2 else f' stroke="{a1}" stroke-width=".6"'
            out.append(f'<path d="M{"L".join(f"{x:.1f} {y:.1f}" for x, y in q)}Z" fill="{fill}"{stroke} stroke-linejoin="round"{a2}/>')
        elif kind == "l":
            out.append(f'<path d="M{q[0][0]:.1f} {q[0][1]:.1f}L{q[1][0]:.1f} {q[1][1]:.1f}" fill="none" {a1}/>')
        elif kind == "c":
            (x, y), r = q[0], a2 * s
            gid = f"{u}b{len(out)}"
            defs.append(f'<radialGradient id="{gid}" cx=".35" cy=".3" r=".8"><stop offset="0" stop-color="{_shade(a1, .28)}"/><stop offset=".6" stop-color="{a1}"/><stop offset="1" stop-color="{_shade(a1, -.25)}"/></radialGradient>')
            out.append(f'<ellipse cx="{x + r * .15:.1f}" cy="{y + r * .82:.1f}" rx="{r * .95:.1f}" ry="{r * .38:.1f}" fill="#0A1424" opacity=".12"/>'
                       f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r:.1f}" fill="url(#{gid})"/>')
        elif kind == "e":
            (x, y), (rx, ry, op) = q[0], a2
            out.append(f'<ellipse cx="{x:.1f}" cy="{y:.1f}" rx="{rx:.1f}" ry="{ry:.1f}" fill="{a1}" opacity="{op}"/>')
        elif kind == "shadow":
            (x, y), rx = q[0], a2 * s * C30 * 1.25
            defs.append(f'<filter id="{u}f" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="{s * .35:.1f}"/></filter>')
            out.append(f'<ellipse cx="{x:.1f}" cy="{y + s * .5:.1f}" rx="{rx:.1f}" ry="{rx * .42:.1f}" fill="#0A1424" opacity=".16" filter="url(#{u}f)"/>')
    if badge:
        cx, cy = vx + vw - br - 2, vy + br + 2
        k = 15 / 24
        out.append(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{br}" fill="#fff" stroke="#0A1424" stroke-opacity=".12"/>'
                   f'<path d="{GLYPH[badge]}" transform="translate({cx - 7.5:.1f} {cy - 7.5:.1f}) scale({k:.4f})" fill="none" stroke="#0A1424" stroke-width="2.1" stroke-linecap="round" stroke-linejoin="round"/>')
    t = f"<title>{title}</title>" if title else ""
    hide = "" if title else ' aria-hidden="true"'
    return f'<svg viewBox="{vx:.1f} {vy:.1f} {vw:.1f} {vh + s * .6:.1f}" xmlns="http://www.w3.org/2000/svg" focusable="false"{hide}>{t}<defs>{"".join(defs)}</defs>{"".join(out)}</svg>'


# ——— Échantillons de matériaux (tuiles de choix) ———
def _rows(y0, step, n, w, col, sw=1.2, stagger=None, joint=None):
    out = []
    for i in range(n):
        y = y0 + i * step
        out.append(f'<path d="M0 {y}H{w}" stroke="{col}" stroke-width="{sw}"/>')
        if stagger:
            off = (i % 2) * stagger / 2
            x = off
            while x < w:
                out.append(f'<path d="M{x:.1f} {y}V{y + step}" stroke="{joint or col}" stroke-width="{sw}"/>')
                x += stagger
    return "".join(out)


def swatch(kind):
    w, hh = 64, 48
    body = {
        "tuile-meca": lambda: '<rect width="64" height="48" fill="#B85A35"/>' + "".join(
            f'<path d="M0 {y}' + "".join(f'q4 5 8 0' for _ in range(8)) + f'" fill="none" stroke="#8F422A" stroke-width="1.3"/>' for y in range(4, 48, 9)),
        "tuile-plate": lambda: '<rect width="64" height="48" fill="#94503A"/>' + _rows(2, 8, 6, w, "#6F3826", 1.1, 10),
        "ardoise": lambda: '<rect width="64" height="48" fill="#3F4754"/>' + _rows(3, 8, 6, w, "#5C6573", 1.1, 13),
        "bac-acier": lambda: '<rect width="64" height="48" fill="#8B95A5"/>' + "".join(
            f'<rect x="{x}" y="0" width="3" height="48" fill="#A9B2C0"/><path d="M{x + 3.5} 0V48" stroke="#6F7989" stroke-width="1"/>' for x in range(2, 64, 9)),
        "enduit": lambda: '<rect width="64" height="48" fill="#E7DECD"/>' + "".join(
            f'<circle cx="{(i * 37) % 61 + 2}" cy="{(i * 23) % 45 + 2}" r="{.8 + (i % 3) * .4}" fill="#CFC3AC"/>' for i in range(46)),
        "pierre": lambda: '<rect width="64" height="48" fill="#CDBD9F"/><path d="M0 14h18l4-14 M18 14l-2 15H0 M22 0l2 13h22l3-13 M24 13l-3 17 M46 13l18 0 M46 13l2 16h16 M16 29l5 1h27 M48 29l-3 19 M21 30l-4 18 M0 29v19" fill="none" stroke="#A5937A" stroke-width="1.3"/>',
        "brique": lambda: '<rect width="64" height="48" fill="#B4553A"/>' + _rows(0, 8, 6, w, "#E3CBBA", 1.4, 16),
        "beton": lambda: '<rect width="64" height="48" fill="#AAB0BA"/><path d="M0 24H64 M32 0V48" stroke="#959CA8" stroke-width="1"/>' + "".join(
            f'<circle cx="{(i * 41) % 60 + 3}" cy="{(i * 29) % 44 + 3}" r="1.1" fill="#8D94A0"/>' for i in range(12)),
        "bois": lambda: '<rect width="64" height="48" fill="#B6844F"/>' + "".join(
            f'<path d="M{x} 0V48" stroke="#8C6237" stroke-width="1.3"/><path d="M{x + 4} 6q2 8 0 16t0 18" fill="none" stroke="#A47442" stroke-width=".8"/>' for x in range(9, 64, 11)),
        "pvc": lambda: '<rect width="64" height="48" fill="#EEF0F3"/><rect x="17" y="6" width="30" height="36" rx="1.5" fill="#fff" stroke="#D3D8E0"/><rect x="21" y="10" width="22" height="28" fill="#C9D7F6"/><path d="M32 10v28" stroke="#fff" stroke-width="2.4"/>',
        "alu": lambda: '<rect width="64" height="48" fill="#EEF0F3"/><rect x="17" y="6" width="30" height="36" rx="1" fill="#5D6573"/><rect x="19.5" y="8.5" width="25" height="31" fill="#C9D7F6"/><path d="M32 8.5v31" stroke="#5D6573" stroke-width="1.6"/>',
        "bois-fen": lambda: '<rect width="64" height="48" fill="#EEF0F3"/><rect x="17" y="6" width="30" height="36" rx="1.5" fill="#A8743F"/><rect x="21" y="10" width="22" height="28" fill="#C9D7F6"/><path d="M32 10v28" stroke="#A8743F" stroke-width="3"/>',
        "inconnu": lambda: '<rect width="64" height="48" fill="#EEF0F3"/><path d="M27 18a5 5 0 1 1 7.5 4.3c-1.6 1-2.5 2-2.5 4 M32 33h.01" transform="translate(-6 -2.5) scale(1.2)" fill="none" stroke="#5B6475" stroke-width="2.2" stroke-linecap="round"/>',
    }[kind]()
    return f'<svg viewBox="0 0 {w} {hh}" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" focusable="false" preserveAspectRatio="xMidYMid slice">{body}</svg>'

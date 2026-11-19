"""Pose les affiches dans les maquettes : perspective, lumière du caisson d'origine, grain, puis export JPG sans métadonnées."""
import json
import sys
import cv2
import numpy as np
from PIL import Image

src, posters, quads_file, out_dir = sys.argv[1:5]
Q = json.load(open(quads_file))


def order(q):
    q = sorted(q, key=lambda p: p[1])
    top = sorted(q[:2], key=lambda p: p[0]); bot = sorted(q[2:], key=lambda p: p[0])
    return np.float32([top[0], top[1], bot[1], bot[0]])  # hg, hd, bd, bg


def inset(q, d):
    c = q.mean(0)
    v = c - q
    return q + v / np.linalg.norm(v, axis=1, keepdims=True) * d


def place(photo, poster_path, quad, d=9, light=0.6, desat=0.0, lift=0.0, sheen=0.06):
    h, w = photo.shape[:2]
    q = inset(order(quad), d)
    pw = int(max(np.linalg.norm(q[1] - q[0]), np.linalg.norm(q[2] - q[3])) * 1.5)
    ph = int(max(np.linalg.norm(q[3] - q[0]), np.linalg.norm(q[2] - q[1])) * 1.5)
    pst = Image.open(poster_path).convert('RGB').resize((pw, ph), Image.LANCZOS)
    pst = np.asarray(pst).astype(np.float32)
    # étalonnage sur la photo : un peu moins saturé, noirs relevés (caisson rétroéclairé)
    gray = pst.mean(-1, keepdims=True)
    pst = gray + (pst - gray) * (1 - desat)
    pst = lift + pst * (1 - lift / 255)
    # ombre portée du cadre sur le bord de l'affiche, plus marquée en haut
    yy, xx = np.mgrid[0:ph, 0:pw].astype(np.float32)
    s0 = 0.014 * pw
    side = np.minimum(np.minimum(xx, pw - 1 - xx), ph - 1 - yy)
    shade = 1 - 0.22 * np.exp(-side / s0) - 0.32 * np.exp(-yy / (s0 * 1.4))
    pst = pst * np.clip(shade, 0.55, 1)[..., None]
    # reflet doux du plexiglas, en diagonale
    t = xx / pw * 0.65 + yy / ph * 0.35
    band = (sheen * np.exp(-((t - 0.30) / 0.13) ** 2) + sheen * 0.35 * np.exp(-((t - 0.62) / 0.05) ** 2))[..., None]
    pst = pst + (255 - pst) * band
    srcq = np.float32([[0, 0], [pw, 0], [pw, ph], [0, ph]])
    M = cv2.getPerspectiveTransform(srcq, q)
    warped = cv2.warpPerspective(pst, M, (w, h), flags=cv2.INTER_LINEAR)
    # masque lissé (bords nets mais sans escalier)
    big = np.ones((ph * 2, pw * 2), np.float32)
    M2 = cv2.getPerspectiveTransform(np.float32([[0, 0], [pw * 2, 0], [pw * 2, ph * 2], [0, ph * 2]]), q)
    mask = cv2.warpPerspective(big, M2, (w, h), flags=cv2.INTER_LINEAR)
    mask = cv2.GaussianBlur(mask, (0, 0), 0.7)[..., None]
    # lumière du panneau d'origine : on garde son dégradé (centre clair, bords plus sombres)
    lum = photo.mean(-1)
    inside = mask[..., 0] > 0.99
    blur = cv2.GaussianBlur(lum, (0, 0), 30)
    ref = np.percentile(blur[inside], 97)
    S = np.clip(blur / ref, 0, 1.05)[..., None]
    shaded = warped * ((1 - light) + light * S)
    # léger flou et grain pour se fondre dans la photo
    shaded = cv2.GaussianBlur(shaded, (0, 0), 0.6)
    rng = np.random.default_rng(7)
    shaded = shaded + rng.normal(0, 2.2, shaded.shape[:2])[..., None]
    return photo * (1 - mask) + shaded * mask


def save(a, name, width=1920):
    im = Image.fromarray(np.clip(a, 0, 255).astype(np.uint8))
    im = im.resize((width, round(im.height * width / im.width)), Image.LANCZOS)
    im.save(f'{out_dir}/{name}.jpg', quality=90, optimize=True, progressive=True)
    print(name, im.size)


def load(n):
    return np.asarray(Image.open(f'{src}/{n}.jpg').convert('RGB')).astype(np.float32)


# 1. Rue : affiche pour les propriétaires
a = load('m1')
a = place(a, f'{posters}/rue-particuliers.png', Q['m1'][0], d=10, light=0.55, desat=0.18, lift=10, sheen=0.07)
save(a, 'affiche-rue-particuliers')

# 2. Mur noir : les trois engagements ; le sol turquoise passe au gris pour rester dans la palette
a = load('m2')
hsv = cv2.cvtColor(np.clip(a, 0, 255).astype(np.uint8), cv2.COLOR_RGB2HSV).astype(np.float32)
ramp = np.clip((np.arange(a.shape[0]) - 1380) / 60, 0, 1)[:, None]
hsv[..., 1] *= 1 - 0.88 * ramp
hsv[..., 2] *= 1 - 0.18 * ramp
a = cv2.cvtColor(np.clip(hsv, 0, 255).astype(np.uint8), cv2.COLOR_HSV2RGB).astype(np.float32)
panels = sorted(Q['m2'], key=lambda q: np.mean([p[0] for p in q]))
for q, n in zip(panels, ('mur-1-artisan', 'mur-2-5-min', 'mur-3-0-mois')):
    a = place(a, f'{posters}/{n}.png', q, d=9, light=0.5, desat=0.08, lift=6, sheen=0.05)
save(a, 'affiches-nos-engagements')

# 3. Grand panneau : la promesse aux artisans
a = load('m3')
a = place(a, f'{posters}/panneau-couverture.png', Q['m3'][0], d=10, light=0.45, desat=0.1, lift=8, sheen=0.06)
save(a, 'panneau-plus-de-chantiers')

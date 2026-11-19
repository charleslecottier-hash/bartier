"""Pose l'affiche artisans dans le caisson de l'abribus, aux formats Meta 4:5 (fil d'actu) et 9:16 (story)."""
import json
import sys
import cv2
import numpy as np
from PIL import Image

work, poster, out_dir = sys.argv[1:4]
Q = json.load(open(f'{work}/abri_quads.json'))


def place(photo, poster_path, quad, d=3, light=0.3, desat=0.05, lift=12, sheen=0.05, bloom=0.16):
    h, w = photo.shape[:2]
    q = np.float32(quad)  # hg, hd, bd, bg
    c = q.mean(0); v = c - q
    q = q + v / np.linalg.norm(v, axis=1, keepdims=True) * d
    pw = int(max(np.linalg.norm(q[1] - q[0]), np.linalg.norm(q[2] - q[3])) * 1.6)
    ph = int(max(np.linalg.norm(q[3] - q[0]), np.linalg.norm(q[2] - q[1])) * 1.6)
    pst = np.asarray(Image.open(poster_path).convert('RGB').resize((pw, ph), Image.LANCZOS)).astype(np.float32)
    gray = pst.mean(-1, keepdims=True)
    pst = gray + (pst - gray) * (1 - desat)
    pst = lift + pst * (1 - lift / 255)
    yy, xx = np.mgrid[0:ph, 0:pw].astype(np.float32)
    s0 = 0.012 * pw
    side = np.minimum(np.minimum(xx, pw - 1 - xx), ph - 1 - yy)
    pst = pst * np.clip(1 - 0.18 * np.exp(-side / s0) - 0.26 * np.exp(-yy / (s0 * 1.4)), 0.6, 1)[..., None]
    t = xx / pw * 0.65 + yy / ph * 0.35
    band = (sheen * np.exp(-((t - 0.30) / 0.13) ** 2) + sheen * 0.35 * np.exp(-((t - 0.62) / 0.05) ** 2))[..., None]
    pst = pst + (255 - pst) * band
    M = cv2.getPerspectiveTransform(np.float32([[0, 0], [pw, 0], [pw, ph], [0, ph]]), q)
    warped = cv2.warpPerspective(pst, M, (w, h), flags=cv2.INTER_LINEAR)
    M2 = cv2.getPerspectiveTransform(np.float32([[0, 0], [pw * 2, 0], [pw * 2, ph * 2], [0, ph * 2]]), q)
    mask = cv2.warpPerspective(np.ones((ph * 2, pw * 2), np.float32), M2, (w, h), flags=cv2.INTER_LINEAR)
    mask = cv2.GaussianBlur(mask, (0, 0), 0.7)[..., None]
    lum = photo.mean(-1)
    inside = mask[..., 0] > 0.99
    blur = cv2.GaussianBlur(lum, (0, 0), 30)
    S = np.clip(blur / np.percentile(blur[inside], 97), 0, 1.05)[..., None]
    shaded = warped * ((1 - light) + light * S)
    shaded = cv2.GaussianBlur(shaded, (0, 0), 0.5)
    shaded = shaded + np.random.default_rng(7).normal(0, 2.0, shaded.shape[:2])[..., None]
    res = photo * (1 - mask) + shaded * mask
    # le texte clair d'un caisson rétroéclairé rayonne un peu à la tombée de la nuit
    glow = cv2.GaussianBlur(np.clip(shaded * mask - 150, 0, None), (0, 0), 6)
    return res + glow * bloom


for name in ('feed', 'story'):
    a = np.asarray(Image.open(f'{work}/{name}_fond.png').convert('RGB')).astype(np.float32)
    a = place(a, poster, Q[name])
    im = Image.fromarray(np.clip(a, 0, 255).astype(np.uint8))
    fn = {'feed': 'pub-meta-artisans-4x5', 'story': 'pub-meta-artisans-9x16'}[name]
    im.save(f'{out_dir}/{fn}.jpg', quality=92, optimize=True, progressive=True)
    print(fn, im.size)

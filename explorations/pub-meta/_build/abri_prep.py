"""Recadre les photos d'abribus aux formats Meta (4:5 et 9:16), puis repère les 4 coins du caisson lumineux."""
import json
import sys
import cv2
import numpy as np
from PIL import Image

dl, out = sys.argv[1], sys.argv[2]
JOBS = {'feed': ('a3', 620, (1080, 1350)), 'story': ('a1', 633, (1080, 1920))}
res = {}
THRS = [int(t) for t in sys.argv[3].split(",")]
for name, (src, x0, size) in JOBS.items():
    im = Image.open(f'{dl}/{src}.png').convert('RGB')
    w = round(im.height * size[0] / size[1])
    im = im.crop((x0, 0, x0 + w, im.height)).resize(size, Image.LANCZOS)
    im.save(f'{out}/{name}_fond.png')
    lum = cv2.cvtColor(np.asarray(im), cv2.COLOR_RGB2GRAY)
    for thr in THRS:
        m = (lum > thr).astype(np.uint8)
        m = cv2.morphologyEx(m, cv2.MORPH_OPEN, np.ones((5, 5), np.uint8))
        k, lab, st, cen = cv2.connectedComponentsWithStats(m)
        i = 1 + int(np.argmax(st[1:, cv2.CC_STAT_AREA]))
        comp = (lab == i).astype(np.uint8)
        cs, _ = cv2.findContours(comp, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        hull = cv2.convexHull(max(cs, key=cv2.contourArea))
        peri = cv2.arcLength(hull, True)
        q = None
        for eps in (0.01, 0.015, 0.02, 0.03, 0.04):
            a = cv2.approxPolyDP(hull, eps * peri, True)
            if len(a) == 4:
                q = a.reshape(-1, 2).tolist(); break
        print(name, 'seuil', thr, 'aire', int(st[i, cv2.CC_STAT_AREA]), 'coins', q)
        if q:
            res[name] = q
            break
    if name in res:
        q = np.float32(sorted(res[name], key=lambda p: p[1]))
        top = q[:2][np.argsort(q[:2, 0])]; bot = q[2:][np.argsort(q[2:, 0])]
        wq = (np.linalg.norm(top[1] - top[0]) + np.linalg.norm(bot[1] - bot[0])) / 2
        hq = (np.linalg.norm(bot[0] - top[0]) + np.linalg.norm(bot[1] - top[1])) / 2
        print(name, 'rapport largeur/hauteur', round(wq / hq, 3))
json.dump(res, open(f'{out}/abri_quads.json', 'w'))

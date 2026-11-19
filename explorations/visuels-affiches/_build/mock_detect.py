"""Repère chaque panneau blanc à partir d'un point en son centre (zone claire fermée par le cadre noir), puis ses 4 coins."""
import json
import sys
import cv2
import numpy as np

src, out = sys.argv[1], sys.argv[2]
SEEDS = {'m1': [(756, 780), (1602, 1044), (1740, 1080)],
         'm2': [(350, 504), (1184, 498), (2010, 504)],
         'm3': [(1170, 666)]}
res = {}
for n, seeds in SEEDS.items():
    img = cv2.imread(f'{src}/{n}.jpg')
    lum = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    res[n] = []
    for (x, y) in seeds:
        found = None
        for thr in (165, 150, 135, 120):
            m = (lum > thr).astype(np.uint8)
            m = cv2.morphologyEx(m, cv2.MORPH_OPEN, np.ones((5, 5), np.uint8))
            k, lab = cv2.connectedComponents(m)
            comp = (lab == lab[y, x]).astype(np.uint8)
            if lab[y, x] == 0:
                continue
            area = int(comp.sum())
            cs, _ = cv2.findContours(comp, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
            c = max(cs, key=cv2.contourArea)
            hull = cv2.convexHull(c)
            peri = cv2.arcLength(hull, True)
            for eps in (0.01, 0.02, 0.03, 0.05):
                q = cv2.approxPolyDP(hull, eps * peri, True)
                if len(q) == 4:
                    break
            print(n, (x, y), 'seuil', thr, 'aire', area, 'coins', len(q), q.reshape(-1, 2).tolist())
            if len(q) == 4 and area < lum.size * 0.4:
                found = q.reshape(-1, 2).tolist()
                break
        res[n].append(found)
json.dump(res, open(out, 'w'))

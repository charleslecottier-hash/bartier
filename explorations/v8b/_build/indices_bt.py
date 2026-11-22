"""Index du bâtiment (BT) de l'Insee, base 2010 : téléchargement et mise en cache.

    python3 _build/indices_bt.py          # met à jour _build/indices_bt.json et les fichiers publics
    python3 _build/indices_bt.py --essai  # affiche le dernier mois sans rien écrire

Source : Insee, Banque de données macro-économiques, jeu « INDEX-BT-TP-DIV-IM-2010 »
(https://bdm.insee.fr/series/sdmx/data/INDEX-BT-TP-DIV-IM-2010), réutilisation libre avec mention de la source.
Le site se construit à partir du cache : la génération ne dépend pas du réseau. À lancer chaque mois, après la publication de l'Insee.
"""
import csv
import io
import json
import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
CACHE = ROOT / "_build" / "indices_bt.json"
PUB = ROOT / "assets" / "data"
URL = "https://bdm.insee.fr/series/sdmx/data/INDEX-BT-TP-DIV-IM-2010?startPeriod=2010-01"


def fetch():
    r = subprocess.run(["curl", "-s", "-m", "180", URL], capture_output=True)
    t = r.stdout.decode("utf-8", "replace")
    out = []
    for attrs, body in re.findall(r"<Series ([^>]*)>([\s\S]*?)</Series>", t):
        a = dict(re.findall(r'(\w+)="([^"]*)"', attrs))
        m = re.match(r"Index du bâtiment - (BT\w+) - (.+?) - Base 2010( - Série arrêtée)?$", a.get("TITLE_FR", "").strip())
        if not m:
            continue
        obs = sorted((p, float(v)) for p, v in re.findall(r'TIME_PERIOD="([^"]+)" OBS_VALUE="([^"]+)"', body))
        out.append({"code": m.group(1), "nom": m.group(2).strip(), "idbank": a["IDBANK"], "arretee": bool(m.group(3)),
                    "maj": a.get("LAST_UPDATE", ""), "valeurs": obs})
    if len(out) < 30:
        raise SystemExit(f"Réponse de l'Insee incomplète ({len(out)} index BT) : cache inchangé.")
    num = lambda c: (int(re.sub(r"\D", "", c)), c)
    return sorted(out, key=lambda x: num(x["code"]))


def write(data):
    CACHE.write_text(json.dumps({"source": URL, "index": data}, ensure_ascii=False, indent=0), encoding="utf-8")
    PUB.mkdir(parents=True, exist_ok=True)
    # Fichier compact pour le calculateur : {code: [[mois, valeur], ...]}
    small = {"source": "Insee, index du bâtiment base 2010", "maj": max(x["maj"] for x in data),
             "index": {x["code"]: {"nom": x["nom"], "v": [[p, v] for p, v in x["valeurs"]]} for x in data}}
    (PUB / "indices-bt.json").write_text(json.dumps(small, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    buf = io.StringIO()
    w = csv.writer(buf, delimiter=";")
    w.writerow(["index", "libelle", "idbank_insee", "mois", "valeur"])
    for x in data:
        for p, v in x["valeurs"]:
            w.writerow([x["code"], x["nom"], x["idbank"], p, f"{v:.1f}".replace(".", ",")])
    (PUB / "indices-bt.csv").write_text(buf.getvalue(), encoding="utf-8")


if __name__ == "__main__":
    d = fetch()
    bt01 = next(x for x in d if x["code"] == "BT01")
    print(f"{len(d)} index BT, dernier mois BT01 : {bt01['valeurs'][-1]}")
    if "--essai" not in sys.argv:
        write(d)
        print("écrit :", CACHE.name, "assets/data/indices-bt.json, assets/data/indices-bt.csv")

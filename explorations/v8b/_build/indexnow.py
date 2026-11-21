"""Signale les pages nouvelles ou modifiées à IndexNow (Bing, et donc ChatGPT et Copilot ; Yandex, Seznam, Naver).

    python3 _build/indexnow.py            # pages dont la date du sitemap a changé depuis le dernier envoi
    python3 _build/indexnow.py --tout     # toutes les pages du sitemap
    python3 _build/indexnow.py --essai    # affiche la liste sans rien envoyer

À lancer après une mise en ligne sur bartierandco.com (la clé doit être servie à la racine du domaine).
Les dates envoyées sont gardées dans _build/indexnow_sent.json.
"""
import json
import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = (ROOT / "_build" / "site.py").read_text(encoding="utf-8")  # constantes lues sans lancer la génération
KEY = re.search(r'^INDEXNOW_KEY = "([0-9a-f]+)"', SRC, re.M).group(1)
SITE = re.search(r'^SITE = "([^"]+)"', SRC, re.M).group(1)
HOST = SITE.split("//", 1)[1]
SENT = ROOT / "_build" / "indexnow_sent.json"


def pages():
    xml = (ROOT / "sitemap.xml").read_text(encoding="utf-8")
    return dict(re.findall(r"<loc>([^<]+)</loc>\s*<lastmod>([^<]+)</lastmod>", xml))


def main():
    now = pages()
    sent = json.loads(SENT.read_text(encoding="utf-8")) if SENT.exists() else {}
    urls = sorted(now) if "--tout" in sys.argv else sorted(u for u, d in now.items() if sent.get(u) != d)
    print(f"{len(urls)} page(s) à signaler")
    for u in urls:
        print(" ", u)
    if not urls or "--essai" in sys.argv:
        return
    key = subprocess.run(["curl", "-sS", "--max-time", "20", f"{SITE}/{KEY}.txt"], capture_output=True, text=True).stdout.strip()
    if key != KEY:
        sys.exit(f"La clé n'est pas servie à {SITE}/{KEY}.txt : mettez le site en ligne d'abord.")
    body = json.dumps({"host": HOST, "key": KEY, "keyLocation": f"{SITE}/{KEY}.txt", "urlList": urls[:10000]})
    r = subprocess.run(["curl", "-sS", "--max-time", "30", "-o", "/dev/null", "-w", "%{http_code}", "-X", "POST", "https://api.indexnow.org/indexnow",
                        "-H", "Content-Type: application/json; charset=utf-8", "--data-binary", body], capture_output=True, text=True)
    code = r.stdout.strip()
    print("IndexNow :", code, {"200": "reçu", "202": "reçu, clé en cours de vérification"}.get(code, r.stderr.strip()[:200]))
    if code in ("200", "202"):
        sent.update({u: now[u] for u in urls})
        SENT.write_text(json.dumps(sent, indent=1, sort_keys=True), encoding="utf-8")


if __name__ == "__main__":
    main()

"""Contenu des pages d'estimation, métier par métier.

Les prix sont des prix moyens publiés, pose comprise, vérifiés sur les pages sources (relevé du 18/11/2026).
Un poste sans prix publié est demandé pour qualifier le projet, puis « chiffré à la visite » : on n'invente aucun prix.
Un client peut remplacer ces prix par ses propres tarifs (champ "tarifs" de sa fiche, voir README.md).
"""

QE = ["QuelleEnergie", "https://www.quelleenergie.fr/prix-travaux/isolation/renovation-toiture"]
SG_TOIT = ["La Maison Saint-Gobain, 03/2026", "https://www.lamaisonsaintgobain.fr/guides-travaux/toiture-charpente/prix-nettoyage-toiture-m2"]
SG_FAC = ["La Maison Saint-Gobain, 08/2026", "https://www.lamaisonsaintgobain.fr/facades/conseils/avant-de-vous-lancer-dans-les-travaux-de-facades/le-prix-d-un-ravalement-de-facade"]
SG_FEN = ["La Maison Saint-Gobain, 02/2026", "https://www.lamaisonsaintgobain.fr/guides-travaux/menuiseries-exterieures/prix-fenetre-pvc"]
OB_CH = ["Obat, 10/2024", "https://travaux.obat.fr/guides/tarif-charpentier/"]
HW_CH = ["Hellowatt, 12/2025", "https://www.hellowatt.fr/prime-energie/renovation-energetique/prix-m2"]
SG_ISO = ["La Maison Saint-Gobain, 07/2026", "https://www.lamaisonsaintgobain.fr/guides-travaux/isolation/prix-isolation-combles"]


def ln(label, lo, hi, unit, src, **kw):
    return dict(l=label, lo=lo, hi=hi, u=unit, src=src, **kw)


DELAI = ["Urgent", "Dans les 3 mois", "Pas pressé"]
STATUT = ["Propriétaire, j’y habite", "Propriétaire, je loue", "Locataire"]
ONSP = ["Oui", "Non", "Je ne sais pas"]

M = {}

M["toiture"] = dict(
    slug="toiture", nom="toiture", artisan="couvreur",
    title="Prix toiture 2026 : estimez vos travaux en 1 minute",
    desc="Nettoyage, démoussage, couverture, réfection : estimez le prix de vos travaux de toiture en 6 questions, à partir des prix publiés en 2026.",
    pill="Tuiles cassées · Fuite · Mousse · Gouttières",
    h1="Combien coûte<br><mark>votre toiture</mark><br>en <em>2026</em> ?",
    sources="QuelleEnergie et La Maison Saint-Gobain",
    hero="roof",
    qty=dict(name="surface", one="m²", many="m²"),
    varie="La surface, le matériau, l’état de la charpente et l’accès au toit.",
    steps=[
        dict(title="Quels travaux sur votre toiture ?", sub="Choisissez ce qui ressemble le plus à votre projet.", auto=True, qs=[
            dict(t="cards", name="travaux", opts=[
                ("Nettoyage et démoussage", "Mousses, lichens, toit noirci", "roof", "leaf",
                 [ln("Nettoyage et démoussage", 25, 35, "€/m²", SG_TOIT)]),
                ("Démoussage et traitement", "Nettoyer, puis protéger les tuiles", "roof", "shield",
                 [ln("Démoussage et traitement hydrofuge", 35, 45, "€/m²", SG_TOIT)]),
                ("Réparation ou fuite", "Tuiles cassées, infiltration", "roof", "drop", []),
                ("Remplacement de la couverture", "Nouvelles tuiles ou ardoises", "roof", "refresh",
                 [ln("Remplacement de la couverture", 60, 300, "€/m²", QE)]),
                ("Réfection complète", "Couverture et charpente refaites", "roofframe", "refresh",
                 [ln("Remplacement de toute la toiture", 180, 500, "€/m²", QE)]),
                ("Isolation par l’extérieur", "Sarking, en refaisant la couverture", "rampant", "layers",
                 [ln("Isolation par l’extérieur (sarking)", 120, 250, "€/m²", QE)]),
            ])]),
        dict(title="Quelle est la surface du toit ?", sub="Une estimation suffit : l’artisan mesure à la visite.", qs=[
            dict(t="range", name="surface", label="Surface du toit", min=20, max=300, step=5, val=100, unit="m²")]),
        dict(title="Quelle est votre couverture actuelle ?", sub="Le matériau change le prix et le savoir-faire demandé.", auto=True, qs=[
            dict(t="tiles", name="couverture", opts=[("Tuiles mécaniques", "tuile-meca"), ("Tuiles plates", "tuile-plate"), ("Ardoise", "ardoise"),
                                                      ("Bac acier", "bac-acier"), ("Je ne sais pas", "inconnu")])]),
        dict(title="Et autour du toit ?", sub="Ces éléments se chiffrent à la visite.", qs=[
            dict(t="range", name="velux", label="Fenêtres de toit à changer ou à créer", min=0, max=6, step=1, val=0, unit="", units=("aucune", "fenêtre", "fenêtres")),
            dict(t="seg", name="gouttieres", label="Gouttières à refaire ?", opts=ONSP)]),
    ],
    visite=[dict(q="velux", gt=0, txt="{v} fenêtre(s) de toit"), dict(q="gouttieres", eq="Oui", txt="Gouttières et zinguerie"),
            dict(q="gouttieres", eq="Je ne sais pas", txt="Gouttières et zinguerie, à vérifier")],
    visite_txt={"Réparation ou fuite": "Une réparation se chiffre sur place : l’artisan doit d’abord trouver d’où vient l’eau."},
)

M["facade"] = dict(
    slug="ravalement-facade", nom="façade", artisan="façadier",
    title="Prix ravalement de façade 2026 : estimation en 1 minute",
    desc="Peinture, enduit, ravalement avec isolation : estimez le prix de votre ravalement de façade en 6 questions, à partir des prix publiés en 2026.",
    pill="Ravalement · Fissures · Façade noircie · Enduit",
    h1="Combien coûte<br><mark>votre façade</mark><br>en <em>2026</em> ?",
    sources="La Maison Saint-Gobain",
    hero="wall",
    qty=dict(name="surface", one="m²", many="m²"),
    varie="La surface, l’état du support, la finition et l’échafaudage.",
    steps=[
        dict(title="Quels travaux sur votre façade ?", sub="Choisissez ce qui ressemble le plus à votre projet.", auto=True, qs=[
            dict(t="cards", name="travaux", opts=[
                ("Mise en peinture", "Façade terne, peinture qui s’écaille", "wall", "roller",
                 [ln("Mise en peinture", 50, 75, "€/m²", SG_FAC)]),
                ("Nouvel enduit", "Enduit fissuré, taché ou qui se décolle", "wall", "layers",
                 [ln("Projection d’enduit", 50, 70, "€/m²", SG_FAC)]),
                ("Ravalement avec isolation", "Isoler les murs par l’extérieur", "wall", "therm",
                 [ln("Ravalement avec isolant", 110, 215, "€/m²", SG_FAC)]),
                ("Fissures à reprendre", "Lézardes, éclats, joints abîmés", "wall", "crack", []),
                ("Je ne sais pas encore", "L’artisan vous conseille à la visite", "wall", "question",
                 [ln("Ravalement sans isolant (peinture ou enduit)", 50, 75, "€/m²", SG_FAC)]),
            ])]),
        dict(title="Quelle surface de façade ?", sub="Une estimation suffit : l’artisan mesure à la visite.", qs=[
            dict(t="range", name="surface", label="Surface des murs", min=20, max=400, step=5, val=100, unit="m²")]),
        dict(title="De quoi est fait le mur ?", sub="Le support décide de la préparation.", auto=True, qs=[
            dict(t="tiles", name="support", opts=[("Enduit", "enduit"), ("Pierre", "pierre"), ("Brique", "brique"), ("Béton", "beton"),
                                                   ("Bardage bois", "bois"), ("Je ne sais pas", "inconnu")])]),
        dict(title="Quelques détails", sub="Pour prévoir l’échafaudage et la préparation.", qs=[
            dict(t="seg", name="hauteur", label="Hauteur de la maison", opts=["Plain-pied", "1 étage", "2 étages ou plus"]),
            dict(t="seg", name="fissures", label="Des fissures visibles ?", opts=ONSP)]),
    ],
    visite=[dict(q="fissures", eq="Oui", txt="Traitement des fissures"), dict(q="hauteur", eq="2 étages ou plus", txt="Échafaudage sur deux étages ou plus")],
    visite_txt={"Fissures à reprendre": "Des fissures se chiffrent sur place : leur cause compte autant que leur longueur."},
)

M["fenetres"] = dict(
    slug="fenetres", nom="fenêtres", artisan="menuisier",
    title="Prix fenêtres 2026 : estimez votre projet en 1 minute",
    desc="Remplacement ou création de fenêtres : estimez le prix de vos fenêtres posées en 6 questions, à partir des prix publiés en 2026.",
    pill="Courants d’air · Condensation · Simple vitrage",
    h1="Combien coûtent<br><mark>vos fenêtres</mark><br>en <em>2026</em> ?",
    sources="La Maison Saint-Gobain",
    hero="windows",
    qty=dict(name="nombre", one="ouverture", many="ouvertures"),
    varie="Le nombre et la taille des fenêtres, le matériau, le vitrage et le type de pose.",
    steps=[
        dict(title="Quel est votre projet ?", sub="Choisissez ce qui ressemble le plus à votre projet.", auto=True, qs=[
            dict(t="cards", name="travaux", opts=[
                ("Remplacer des fenêtres", "Simple vitrage, bois abîmé, courants d’air", "windows", "refresh",
                 [ln("Fenêtre PVC en remplacement", 870, 1170, "€ TTC", SG_FEN)]),
                ("Créer une ouverture", "Une nouvelle fenêtre dans un mur", "newwin", "plus",
                 [ln("Fenêtre PVC en création d’ouverture", 2400, 2400, "€ TTC", SG_FEN, approx=True)]),
                ("Baie vitrée ou porte-fenêtre", "Grande ouverture, coulissant", "bay", None, []),
                ("Porte d’entrée", "Sécurité, isolation, style", "door", None, []),
                ("Volets", "Battants ou roulants", "shutters", None, []),
            ])]),
        dict(title="Combien d’ouvertures ?", sub="Fenêtres, portes ou baies : comptez chacune, même petite.", qs=[
            dict(t="range", name="nombre", label="Nombre d’ouvertures", min=1, max=15, step=1, val=4, unit="", units=("", "ouverture", "ouvertures"))]),
        dict(title="Quel matériau vous tente ?", sub="Les prix publiés sont ceux du PVC. Les autres se chiffrent à la visite.", auto=True, qs=[
            dict(t="tiles", name="materiau", opts=[("PVC", "pvc"), ("Aluminium", "alu"), ("Bois", "bois-fen"), ("Je ne sais pas", "inconnu")])]),
        dict(title="Vos fenêtres aujourd’hui", sub="Pour préparer la visite.", qs=[
            dict(t="seg", name="vitrage", label="Vitrage actuel", opts=["Simple vitrage", "Double vitrage", "Je ne sais pas"]),
            dict(t="seg", name="volets", label="Des volets à changer aussi ?", opts=["Oui", "Non"])]),
    ],
    visite=[dict(q="volets", eq="Oui", txt="Volets")],
    notes=[dict(q="materiau", eq="Aluminium", txt="Ces prix sont ceux du PVC. En aluminium, le prix se donne à la visite."),
           dict(q="materiau", eq="Bois", txt="Ces prix sont ceux du PVC. En bois, le prix se donne à la visite.")],
    visite_txt={"Baie vitrée ou porte-fenêtre": "Une baie ou une porte-fenêtre se chiffre sur mesure, à la visite.",
                "Porte d’entrée": "Une porte d’entrée se chiffre sur mesure, à la visite.",
                "Volets": "Des volets se chiffrent sur mesure, à la visite."},
)

M["charpente"] = dict(
    slug="charpente", nom="charpente", artisan="charpentier",
    title="Prix charpente 2026 : estimez vos travaux en 1 minute",
    desc="Traitement du bois, rénovation, charpente et couverture : estimez le prix de vos travaux de charpente en 6 questions, à partir des prix publiés.",
    pill="Bois attaqué · Poutre qui fléchit · Humidité",
    h1="Combien coûte<br><mark>votre charpente</mark><br>en <em>2026</em> ?",
    sources="Hellowatt et Obat",
    hero="frame",
    qty=dict(name="surface", one="m²", many="m²"),
    varie="L’état du bois, la portée, le traitement et l’accès au chantier.",
    steps=[
        dict(title="Quels travaux sur votre charpente ?", sub="Choisissez ce qui ressemble le plus à votre projet.", auto=True, qs=[
            dict(t="cards", name="travaux", opts=[
                ("Traitement du bois", "Insectes, champignons, humidité", "frame", "bug",
                 [ln("Traitement préventif ou curatif du bois", 40, 180, "€/m²", OB_CH)]),
                ("Réparation ou renfort", "Poutre abîmée, toit qui s’affaisse", "frame", "wrench", []),
                ("Rénovation de la charpente", "Le prix de la charpente seule", "frame", "refresh",
                 [ln("Rénovation de la charpente seule", 150, 200, "€ TTC/m²", HW_CH)]),
                ("Charpente et couverture", "Toute la toiture refaite", "roofframe", "refresh",
                 [ln("Charpente et couverture", 180, 250, "€ TTC/m²", HW_CH)]),
                ("Extension ou surélévation", "Agrandir sous un nouveau toit", "extension", "plus", []),
            ])]),
        dict(title="Quelle surface de toiture ?", sub="Une estimation suffit : l’artisan mesure à la visite.", qs=[
            dict(t="range", name="surface", label="Surface de la toiture", min=20, max=250, step=5, val=90, unit="m²")]),
        dict(title="Qu’avez-vous remarqué ?", sub="Plusieurs réponses possibles.", qs=[
            dict(t="chips", name="signes", label="Signes observés", multi=True, excl="Rien de particulier",
                 opts=["Bois qui s’effrite", "Petits trous, sciure", "Poutre qui fléchit", "Traces d’humidité", "Rien de particulier"])]),
        dict(title="Quelques détails", sub="Pour préparer la visite.", qs=[
            dict(t="seg", name="combles", label="Les combles sont-ils accessibles ?", opts=ONSP),
            dict(t="seg", name="maison", label="Votre maison", opts=["Plain-pied", "À étage"])]),
    ],
    visite=[],
    visite_txt={"Réparation ou renfort": "Une réparation se chiffre sur place, après avoir vu l’état du bois.",
                "Extension ou surélévation": "Une extension se chiffre sur plans, après une visite."},
)

M["isolation"] = dict(
    slug="isolation", nom="isolation", artisan="artisan",
    title="Prix isolation 2026 : estimez vos travaux en 1 minute",
    desc="Combles perdus, combles aménagés, murs par l’extérieur : estimez le prix de votre isolation en 6 questions, à partir des prix publiés en 2026.",
    pill="Maison froide · Factures élevées · Combles non isolés",
    h1="Combien coûte<br><mark>votre isolation</mark><br>en <em>2026</em> ?",
    sources="La Maison Saint-Gobain",
    hero="attic",
    qty=dict(name="surface", one="m²", many="m²"),
    varie="La surface, la technique (combles perdus, rampants, murs) et l’isolant choisi.",
    aides="Des aides peuvent baisser ce montant (MaPrimeRénov’, primes CEE) si l’entreprise est certifiée RGE. Elles se demandent avant de signer le devis.",
    steps=[
        dict(title="Que voulez-vous isoler ?", sub="Choisissez ce qui ressemble le plus à votre projet.", auto=True, qs=[
            dict(t="cards", name="travaux", opts=[
                ("Combles perdus", "Un grenier qu’on n’habite pas", "attic", "therm",
                 [ln("Combles perdus, accès par l’intérieur", 40, 40, "€ TTC/m²", SG_ISO, **{"if": ["acces", "Par l’intérieur"], "g": "c"}),
                  ln("Combles perdus, accès par le toit", 45, 45, "€ TTC/m²", SG_ISO, **{"if": ["acces", "Par le toit"], "g": "c"})],
                 "Combles perdus, accès à préciser"),
                ("Combles aménagés", "Des pièces sous le toit", "rampant", "therm",
                 [ln("Combles aménagés, par l’intérieur", 130, 180, "€ TTC/m²", SG_ISO, **{"if": ["acces", "Par l’intérieur"], "g": "c"}),
                  ln("Combles aménagés, par le toit", 240, 240, "€ TTC/m²", SG_ISO, **{"if": ["acces", "Par le toit"], "g": "c"})],
                 "Combles aménagés, accès à préciser"),
                ("Murs par l’extérieur", "Un isolant posé sur la façade", "wall", "therm",
                 [ln("Ravalement avec isolant", 110, 215, "€/m²", SG_FAC)]),
                ("Plancher bas", "Au-dessus d’un garage ou d’une cave", "floor", "therm", []),
                ("Je ne sais pas encore", "L’artisan vous conseille à la visite", "none", "question", []),
            ])]),
        dict(title="Quelle surface à isoler ?", sub="Une estimation suffit : l’artisan mesure à la visite.", qs=[
            dict(t="range", name="surface", label="Surface à isoler", min=20, max=200, step=5, val=70, unit="m²")]),
        dict(title="Accès et chauffage", sub="Le chauffage compte pour les aides.", qs=[
            dict(t="seg", name="acces", label="Par où isoler les combles ?", opts=["Par l’intérieur", "Par le toit", "Je ne sais pas"],
                 show=["travaux", ["Combles perdus", "Combles aménagés"]]),
            dict(t="chips", name="chauffage", label="Chauffage principal", opts=["Électricité", "Gaz", "Fioul", "Bois", "Pompe à chaleur"])]),
        dict(title="Votre logement", sub="Pour préparer la visite.", qs=[
            dict(t="seg", name="logement", label="Type de logement", opts=["Maison", "Appartement"]),
            dict(t="seg", name="annee", label="Année de construction", opts=["Avant 1975", "1975 à 2000", "Après 2000", "Je ne sais pas"])]),
    ],
    visite=[],
    visite_txt={"Plancher bas": "Un plancher bas se chiffre sur place : tout dépend de l’accès par en dessous.",
                "Je ne sais pas encore": "L’artisan regarde votre maison et vous dit par où commencer."},
)

COMMON = [
    dict(title="Pour quand, et où ?", sub="Pour organiser la visite au bon moment.", key="ou", qs=[
        dict(t="seg", name="delai", label="Quand souhaitez-vous faire les travaux ?", opts=DELAI),
        dict(t="seg", name="statut", label="Vous êtes", opts=STATUT),
        dict(t="cp", name="code_postal", label="Code postal du chantier")]),
]

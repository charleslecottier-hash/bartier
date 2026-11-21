"""Textes des cartes « Nos spécialités » : une carte par type de travaux proposé au questionnaire.

Chaque entrée : (phrase d'introduction, [(terme en gras, précision), ...], aides).
Les textes décrivent le travail lui-même, sans promesse de délai, de garantie ou de qualification :
ces points-là dépendent de l'artisan et se vérifient avec lui avant de publier sa page.
Le prix affiché sous chaque carte vient des prix du questionnaire (metiers.py) ou des tarifs du client.
"""

TEXTES = {
    "toiture": {
        "Nettoyage et démoussage": (
            "Mousses et lichens gardent l’humidité contre les tuiles et finissent par les abîmer. Un nettoyage redonne de l’air à la couverture.",
            [("Brossage et lavage basse pression", "pour décoller les mousses sans casser les tuiles"),
             ("Traitement anti-mousse", "pulvérisé sur toute la toiture, il agit dans les semaines qui suivent"),
             ("Gouttières dégagées", "pour que l’eau s’écoule de nouveau")], False),
        "Démoussage et traitement": (
            "Après le nettoyage, un hydrofuge protège les tuiles de l’eau et ralentit le retour des mousses.",
            [("Démoussage complet", "brossage, lavage, puis anti-mousse"),
             ("Hydrofuge incolore ou coloré", "il limite l’eau absorbée par les tuiles"),
             ("Tuiles abîmées changées avant", "un traitement ne répare pas une tuile fendue")], False),
        "Réparation ou fuite": (
            "Une infiltration abîme vite l’isolant et la charpente. La première étape est de trouver d’où vient l’eau.",
            [("Recherche de la fuite", "tuile cassée, solin décollé, noue ou faîtage"),
             ("Réparation ciblée", "seules les pièces abîmées sont changées"),
             ("Zinguerie", "gouttières, chéneaux et descentes quand l’eau déborde")], False),
        "Remplacement de la couverture": (
            "Quand les tuiles ou les ardoises deviennent poreuses ou cassantes, la couverture se refait sur la charpente existante.",
            [("Dépose de l’ancienne couverture", "et évacuation des déchets"),
             ("Écran sous-toiture et liteaux", "remplacés au passage si besoin"),
             ("Tuiles, ardoises ou bac acier", "selon la pente et le style de la maison")], False),
        "Réfection complète": (
            "Couverture et charpente sont refaites ensemble quand le bois ne peut plus porter une nouvelle couverture.",
            [("État de la charpente", "pièces à changer, à renforcer ou à traiter"),
             ("Charpente remise en état", "ou refaite en partie"),
             ("Couverture neuve", "avec un écran sous-toiture")], False),
        "Isolation par l’extérieur": (
            "Le sarking pose l’isolant au-dessus des chevrons, au moment de refaire la couverture. Les combles gardent toute leur hauteur.",
            [("Isolant continu", "sans coupure au niveau des chevrons, donc moins de pertes"),
             ("Aucune place perdue", "rien n’est posé côté intérieur"),
             ("Couverture neuve", "posée par-dessus l’isolant")], True),
    },
    "facade": {
        "Mise en peinture": (
            "Une peinture de façade protège le mur de la pluie et lui rend sa couleur.",
            [("Nettoyage du mur", "et petites fissures rebouchées avant de peindre"),
             ("Peinture adaptée au support", "enduit, béton ou pierre"),
             ("Choix de la teinte", "dans le respect des règles de la commune")], False),
        "Nouvel enduit": (
            "Un enduit fissuré ou qui se décolle laisse l’eau entrer dans le mur. Le refaire protège la façade et la rafraîchit.",
            [("Ancien enduit retiré", "là où il ne tient plus"),
             ("Nouvel enduit projeté", "en une ou plusieurs passes"),
             ("Finition au choix", "grattée, talochée ou écrasée")], False),
        "Ravalement avec isolation": (
            "L’isolant est fixé sur les murs extérieurs, puis recouvert d’un enduit. La façade est refaite et la maison garde mieux sa chaleur.",
            [("Isolant sur toute la façade", "collé ou fixé mécaniquement"),
             ("Enduit de finition", "dans la teinte choisie"),
             ("Aucune place perdue", "les pièces gardent leur surface")], True),
        "Fissures à reprendre": (
            "Une fissure fine se traite pendant le ravalement. Une fissure qui s’élargit demande d’abord d’en trouver la cause.",
            [("Diagnostic", "fissure de surface ou de structure"),
             ("Ouverture et rebouchage", "avec un mortier ou une résine adaptés"),
             ("Armature", "posée dans l’enduit pour que la fissure ne revienne pas")], False),
    },
    "fenetres": {
        "Remplacer des fenêtres": (
            "Des fenêtres récentes à double vitrage arrêtent les courants d’air et la condensation, et laissent passer moins de bruit.",
            [("Pose en rénovation", "sur l’ancien cadre, sans toucher aux murs"),
             ("Dépose totale", "quand l’ancien cadre est abîmé"),
             ("PVC, bois ou aluminium", "selon le budget et le style de la maison")], True),
        "Créer une ouverture": (
            "Une nouvelle fenêtre demande une ouverture propre dans le mur et un linteau pour le soutenir.",
            [("Découpe du mur", "et pose d’un linteau"),
             ("Pose de la fenêtre", "avec l’étanchéité tout autour"),
             ("Démarches", "une déclaration préalable en mairie est souvent nécessaire")], False),
        "Baie vitrée ou porte-fenêtre": (
            "Une grande ouverture vitrée fait entrer la lumière et ouvre la pièce sur le jardin ou la terrasse.",
            [("Coulissant ou battant", "selon la place disponible"),
             ("Ouverture agrandie", "possible, avec un linteau adapté"),
             ("Vitrage isolant", "pour garder le confort en hiver")], False),
        "Porte d’entrée": (
            "La porte d’entrée compte pour la sécurité, pour l’isolation et pour l’allure de la maison.",
            [("Serrure multipoints", "plus difficile à forcer"),
             ("Porte isolante", "fini les courants d’air dans l’entrée"),
             ("Matériau au choix", "PVC, aluminium, bois ou acier")], False),
        "Volets": (
            "Les volets protègent du soleil, du froid et des regards.",
            [("Volets battants", "en bois, PVC ou aluminium"),
             ("Volets roulants", "manuels, électriques ou solaires"),
             ("Motorisation", "possible sur des volets roulants existants")], False),
    },
    "charpente": {
        "Traitement du bois": (
            "Insectes et champignons affaiblissent le bois bien avant que cela se voie.",
            [("Diagnostic", "repérer les zones attaquées"),
             ("Bûchage", "le bois abîmé est retiré en surface"),
             ("Injection et pulvérisation", "d’un produit contre les insectes et les champignons")], False),
        "Réparation ou renfort": (
            "Une poutre fendue ou un toit qui s’affaisse se répare souvent sans refaire toute la charpente.",
            [("Étaiement", "le toit est soutenu pendant les travaux"),
             ("Renfort", "des pièces de bois neuves fixées contre la poutre affaiblie"),
             ("Remplacement", "des pièces trop abîmées")], False),
        "Rénovation de la charpente": (
            "La charpente est remise en état pour durer, avant de refaire ou de garder la couverture.",
            [("Pièces changées", "chevrons, pannes ou liteaux abîmés"),
             ("Renforts", "là où le bois a fléchi"),
             ("Traitement du bois", "sur l’ensemble de la charpente")], False),
        "Charpente et couverture": (
            "Toute la toiture est refaite : la charpente d’abord, puis la couverture.",
            [("Charpente refaite ou renforcée", "selon son état"),
             ("Écran sous-toiture", "posé avant la couverture"),
             ("Couverture neuve", "tuiles, ardoises ou bac acier")], False),
        "Extension ou surélévation": (
            "Agrandir la maison, c’est aussi construire un nouveau toit.",
            [("Étude de la structure", "les murs existants doivent pouvoir porter la charge"),
             ("Charpente neuve", "traditionnelle ou en fermettes"),
             ("Démarches", "déclaration préalable ou permis de construire, selon la surface")], False),
    },
    "isolation": {
        "Combles perdus": (
            "Une grande part de la chaleur s’échappe par le toit. Isoler un grenier qu’on n’habite pas est le chantier le plus simple pour la garder.",
            [("Isolant soufflé", "laine minérale ou ouate de cellulose, en couche épaisse"),
             ("Repères d’épaisseur", "posés pour vérifier la hauteur d’isolant"),
             ("Trappe isolée", "pour ne pas laisser passer l’air")], True),
        "Combles aménagés": (
            "Quand on vit sous le toit, l’isolant se pose sous les pentes du toit, ou par l’extérieur en refaisant la couverture.",
            [("Par l’intérieur", "isolant entre et sous les chevrons, puis plaques de plâtre"),
             ("Par le toit", "sarking, quand la couverture est à refaire"),
             ("Pare-vapeur", "pour protéger l’isolant de l’humidité")], True),
        "Murs par l’extérieur": (
            "Un isolant posé sur la façade garde la chaleur sans prendre de place à l’intérieur.",
            [("Isolant sur toute la façade", "collé ou fixé mécaniquement"),
             ("Enduit de finition", "la façade est refaite en même temps"),
             ("Ponts thermiques réduits", "aux planchers et aux angles")], True),
        "Plancher bas": (
            "Un sol froid au-dessus d’un garage ou d’une cave se corrige en isolant le plafond de cette pièce.",
            [("Panneaux isolants", "fixés au plafond du garage ou de la cave"),
             ("Isolant projeté", "pour les plafonds irréguliers"),
             ("Sol plus chaud", "dans les pièces du dessus")], True),
    },
}

# Photo de chaque carte : (fichier de photos/, texte de remplacement, cadrage CSS). Photos libres de droits (voir photos/SOURCES.md),
# présentées comme photos d'illustration. Une carte sans photo garde le dessin du projet. Les photos de l'artisan
# (champ « photos_prestations » de sa fiche) passent avant.
PHOTOS = {
    "toiture": {
        "Nettoyage et démoussage": ("toit-mousse-800.webp", "Toiture en tuiles canal couverte de mousse et de lichen", "center"),
        "Démoussage et traitement": ("toiture-tuiles-800.webp", "Tuiles de toiture en gros plan", "center"),
        "Réparation ou fuite": ("toiture-800.webp", "Réparation d’une toiture en tuiles", "center"),
        "Remplacement de la couverture": ("toiture-ardoise-800.webp", "Couvreur au travail sur une toiture en ardoise", "center 40%"),
        "Réfection complète": ("charpente-800.webp", "Charpente en bois en cours de pose", "center"),
        "Isolation par l’extérieur": ("isolation-800.webp", "Pose de laine isolante entre des montants en bois", "center"),
    },
    "facade": {
        "Mise en peinture": ("facade-peinture-800.webp", "Peintre appliquant une peinture blanche au rouleau sur une façade", "center"),
        "Nouvel enduit": ("facade-enduit-800.webp", "Enduit appliqué à la taloche sur un mur en pierre", "center 45%"),
        "Ravalement avec isolation": ("facade-echafaudage-800.webp", "Maison sous échafaudage pendant un ravalement", "center"),
        "Fissures à reprendre": ("fissure-800.webp", "Fissure dans un mur enduit", "center"),
    },
    "fenetres": {
        "Remplacer des fenêtres": ("fenetres-800.webp", "Découpe d’un cadre de fenêtre", "center"),
        "Créer une ouverture": ("ouverture-800.webp", "Artisan fixant un nouveau châssis de fenêtre", "center"),
        "Baie vitrée ou porte-fenêtre": ("baie-800.webp", "Grande baie vitrée coulissante donnant sur une terrasse", "center"),
        "Porte d’entrée": ("porte-800.webp", "Porte d’entrée vitrée à double battant", "center"),
        "Volets": ("volets-800.webp", "Fenêtres à volets battants en bois sur une façade enduite", "center"),
    },
    "charpente": {
        "Traitement du bois": ("bois-traitement-800.webp", "Bois ancien criblé de trous d’insectes xylophages", "center"),
        "Réparation ou renfort": ("charpente-poutre-800.webp", "Travail d’une pièce de bois de charpente", "center 92%"),
        "Rénovation de la charpente": ("charpente-charpentier-800.webp", "Charpentier sur une structure en bois", "center 100%"),
        "Charpente et couverture": ("charpente-800.webp", "Charpente en bois en cours de pose", "center"),
        "Extension ou surélévation": ("extension-800.webp", "Charpente bois neuve en cours de montage sur un étage en construction", "center"),
    },
    "isolation": {
        "Combles perdus": ("combles-perdus-800.webp", "", "center"),
        "Combles aménagés": ("isolation-800.webp", "Pose de laine isolante entre les montants d’un mur", "center"),
        "Murs par l’extérieur": ("facade-echafaudage-800.webp", "Maison sous échafaudage pendant un ravalement", "center"),
        "Plancher bas": ("plancher-bas-800.webp", "", "center"),
    },
}

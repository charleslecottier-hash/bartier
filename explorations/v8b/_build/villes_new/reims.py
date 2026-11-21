from villes_data import L, S, SP, NATIONAL  # liens dans le texte, sources discrètes, Service-Public, aides nationales
REVIEWED = "2026-11-21"

# Sources consultées le 21/11/2026. reims.fr et grandreims.fr renvoient une page anti-robot : rien n'en est repris.
# PLU en vigueur (version du 27/10/2025, Géoportail de l'urbanisme) : l'identifiant du document change à chaque mise à jour du PLU.
_PLU_REG = "https://www.geoportail-urbanisme.gouv.fr/api/document/8fc9b619669be836bd830541f048579e/files/51454_reglement_20251027.pdf"
_PLU_PROC = "https://www.geoportail-urbanisme.gouv.fr/api/document/8fc9b619669be836bd830541f048579e/files/51454_procedure_20251027.pdf"
_INSEE = "https://api.insee.fr/melodi/data/DS_RP_LOGEMENT_PRINC?GEO=COM-51454"  # dossier complet, RP 2023 (page insee.fr en erreur 500 ce jour)
_MRAE = "https://www.mrae.developpement-durable.gouv.fr/IMG/pdf/2024age72.pdf"
_SPR_AR = "https://www.marne.gouv.fr/contenu/telechargement/27458/173676/file/Arr%C3%AAt%C3%A9+SPR+Reims.pdf"
_SPR_MC = "https://www.culture.gouv.fr/regions/drac-grand-est/actu/an/2020/saint-die-des-vosges-et-Reims-SPR"
_MF = "https://donneespubliques.meteofrance.fr/FichesClim/FICHECLIM_51183001.pdf"  # Reims-Courcy ; pas de fiche 1991-2020 publiée pour Reims-Prunay
_CAV = "https://georisques.gouv.fr/api/v1/cavites?code_insee=51454"
_RISQ = "https://georisques.gouv.fr/api/v1/gaspar/risques?code_insee=51454"
_UDAP = "https://www.culture.gouv.fr/fr/regions/drac-grand-est/services/patrimoines-architecture/udap/udap-de-la-marne"
_COUL = "https://www.culture.gouv.fr/Media/Regions/Drac-Grand-Est/Files/Aides-et-demarches/Fiches-conseils-UDAP/UDAP51/Fiche-Les-couleurs-du-bati-marnais"
_SP_DP = SP + "F17578"
_SP_ODP = "https://entreprendre.service-public.gouv.fr/vosdroits/F23509"
_MAIRIE = "https://lannuaire.service-public.gouv.fr/grand-est/marne/d4379967-4f2b-4f03-a111-a6deb19cdb13"
_ECFR = "https://lannuaire.service-public.gouv.fr/grand-est/marne/f6715661-c5fd-4448-9a4d-e41441f8a5c7"
_MDH = "https://www.lamaisondelhabitat-reims.fr/renovation/"
_GRR = "https://www.anil.org/aides-locales-travaux/details/marne-grandreimsrenov-4781/"
_PBC = "https://www.anil.org/aides-locales-travaux/details/marne-prime-bas-carbone-4784/"
_PAB = "https://www.anil.org/aides-locales-travaux/details/marne-prime-air-bois-4785/"

CITY = dict(
    slug="reims", name="Reims", cp="51100", insee="51454",
    lat=49.2628, lon=4.0347, dept="Marne", depcode="51", region="Grand Est",
    wiki="https://fr.wikipedia.org/wiki/Reims", wikidata="Q41876",
    verified="2026-11-21",
    tldr="À Reims, le centre reconstruit après 1918 est un site patrimonial remarquable depuis 2020, et le sous-sol de la commune compte "
         "219 cavités recensées, caves et anciennes carrières",
    hook="Centre de la Reconstruction protégé depuis 2020, caves et carrières sous la ville.",
    title="Devis travaux à Reims : toiture, façade, fenêtres, isolation",
    desc="Travaux à Reims : centre de la Reconstruction protégé, 11 cités-jardins encadrées, caves et carrières, primes du Grand Reims. Un seul artisan vient chiffrer.",
    figures_intro="Ce qui compte avant de lancer des travaux à Reims, du centre aux cités-jardins.",
    figures=[("79,1 <small>%</small>", "des logements sont des appartements", S("Insee, 2023", _INSEE)),
             ("10,6 <small>%</small>", "des résidences principales datent de 1919 à 1945, contre 3,2 % d’avant 1919", S("Insee, 2023", _INSEE)),
             ("201,6 <small>ha</small>", "de site patrimonial remarquable en centre-ville, classé en 2020", S("MRAe Grand Est, 2024", _MRAE)),
             ("219", "cavités souterraines recensées sur la commune, dont 85 caves et 59 carrières", S("Géorisques", _CAV))],
    answer=("À Reims, 79,1 % des logements sont des appartements, et 10,6 % des résidences principales datent de 1919 à 1945, contre 3,2 % d’avant 1919. "
            "Dans le site patrimonial remarquable du centre, classé le 28 mai 2020, tout changement d’aspect extérieur demande l’accord de l’architecte "
            "des Bâtiments de France. Géorisques recense 219 cavités souterraines sous la commune."),
    facts=[("Centre-ville protégé", "Site patrimonial remarquable classé par arrêté du ministère de la Culture du 28 mai 2020, sur 201,6 hectares, des Promenades "
                                    "aux boulevards Lundy, de la Paix et Pasteur. Tout changement d’aspect extérieur y demande une autorisation et l’accord de "
                                    "l’architecte des Bâtiments de France (" + L("arrêté", _SPR_AR) + ", " + L("MRAe", _MRAE) + ")."),
           ("Saint-Nicaise", "Au sud du centre, le quartier Saint-Nicaise forme un second site patrimonial remarquable, issu de l’AVAP approuvée le "
                             "14 novembre 2016 (" + L("MRAe", _MRAE) + ", 2024)."),
           ("Urbanisme", "Le PLU de Reims, approuvé le 28 septembre 2017 et modifié depuis, relève de la Communauté urbaine du Grand Reims. Dans le "
                         "site patrimonial remarquable du centre, le plan de valorisation de l’architecture et du patrimoine (PVAP), approuvé le "
                         "26 juin 2025, s’impose au PLU et fixe les règles des travaux (" + L("règlement du PLU", _PLU_REG) + ", "
                         + L("délibération", _PLU_PROC) + ")."),
           ("Sous-sol", "Géorisques recense 219 cavités souterraines à Reims, dont 85 caves et 59 carrières. La commune est exposée aux affaissements "
                        "et effondrements liés aux anciennes carrières souterraines (" + L("cavités", _CAV) + ", " + L("risques", _RISQ) + ")."),
           ("Climat", "À Reims-Courcy, 62,1 jours de gel par an, dont 15,2 à −5 °C ou moins, et 114,4 jours avec au moins 1 mm de pluie "
                      "(" + L("Météo-France", _MF) + ", normales 1981-2010). Record de froid depuis 1929 : −22,3 °C le 6 janvier 1985."),
           ("Cités-jardins", "Le PLU classe 11 cités-jardins en zone UP, dont le Chemin Vert, Maison Blanche, la Cité du Châlet et la Cité Mulhouse. "
                             "Lors d’un ravalement, supprimer moulures, corniches, bandeaux ou pilastres y est interdit, sauf dégradation ("
                             + L("règlement du PLU", _PLU_REG) + ", 2025).")],
    trades_intro="Immeubles de la Reconstruction, cités-jardins des années 1920, logements de 1946 à 1990, plus de la moitié des résidences principales : à Reims, chaque époque a ses points d’attention.",
    trades={
        "toiture": ["À Reims-Courcy, il gèle 62,1 jours par an, et 43,6 jours connaissent des rafales d’au moins 58 km/h. Faites vérifier couverture, "
                    "solins et gouttières à la sortie de l’hiver (" + L("Météo-France", _MF) + ", normales 1981-2010).",
                    "Dans le site patrimonial remarquable, changer de matériau de couverture, créer une fenêtre de toit ou poser des panneaux solaires "
                    "modifie l’aspect extérieur : déclaration préalable, instruite en deux mois en secteur protégé, accord de l’architecte des Bâtiments "
                    "de France (" + L("Service-Public", _SP_DP) + ") et, dans le centre, respect du PVAP approuvé en 2025 (" + L("règlement du PLU", _PLU_REG) + ")."],
        "facade": ["Le centre classé se distingue par un patrimoine des années 1920 issu de la Reconstruction, comme les demeures du cours Langlet ("
                   + L("ministère de la Culture", _SPR_MC) + "). Seules 3,2 % des résidences principales de la ville datent d’avant 1919 ("
                   + L("Insee", _INSEE) + ", 2023).",
                   "Pour les façades marnaises, le nuancier conseil de l’architecte des Bâtiments de France propose des teintes neutres, dorées, ocrées "
                   "et rosées, ou claires, avec une palette à part pour les fenêtres et les volets (" + L("UDAP de la Marne", _COUL) + ")."],
        "fenetres": ["Dans les cités-jardins de la zone UP, les dimensions et proportions des ouvertures sont propres à chaque cité : évitez de les "
                     "modifier, sauf pour retrouver celles d’origine. Remplacer des menuiseries traditionnelles par des modèles à cote normalisée demande "
                     "une étude d’intégration (" + L("règlement du PLU", _PLU_REG) + ").",
                     "Au Chemin Vert et à Maison Blanche, les volets et les autres éléments en bois gardent leurs couleurs d’origine (" + L("règlement du PLU", _PLU_REG)
                     + "). Dans un site patrimonial remarquable, la déclaration préalable est instruite en deux mois au lieu d’un (" + L("Service-Public", _SP_DP) + ")."],
        "charpente": ["Géorisques recense 219 cavités souterraines à Reims, caves et anciennes carrières comprises. Avant une surélévation ou une "
                      "extension, vérifiez ce qu’il y a sous la parcelle (" + L("Géorisques", _CAV) + ").",
                      "Dans le centre, l’autorité environnementale signale un risque de remontée de nappes près de la Vesle et un aléa de mouvement de "
                      "terrain faible à élevé selon les secteurs (" + L("MRAe", _MRAE) + ", 2024). Signalez-le à l’artisan avant d’alourdir une charpente."],
        "isolation": ["GrandReimsRénov’ complète MaPrimeRénov’ Parcours accompagné : 10 % du hors-taxe pour les ménages très modestes, "
                      "20 % pour les autres, si les travaux font gagner au moins deux classes énergétiques, avec un artisan RGE et Mon Accompagnateur "
                      "Rénov’ (" + L("ANIL", _GRR) + ", 2026).",
                      "Le besoin de chauffage est élevé : 2 829,6 degrés-jours unifiés par an à Reims-Courcy (" + L("Météo-France", _MF) + ", normales 1981-2010). Dans le "
                      "site patrimonial remarquable, une isolation par l’extérieur modifie la façade et passe par l’accord de l’architecte des Bâtiments de France."]},
    steps_intro="Dans l’ordre, du repérage au chantier.",
    steps=[("Vérifiez si votre adresse est dans un site patrimonial remarquable", "Centre-ville et Saint-Nicaise : l’architecte des Bâtiments de France donne "
                                                                                 "son accord. UDAP de la Marne, 38 rue Cérès, sur rendez-vous : 03 26 47 74 39 ("
                                                                                 + L("ministère de la Culture", _UDAP) + ")."),
           ("Regardez le zonage du PLU", "Le règlement graphique montre si votre maison est dans une cité-jardin (zone UP) ou dans le centre, où le "
                                         "PVAP s’ajoute au PLU. Il est consultable sur le " + L("Géoportail de l’urbanisme", "https://www.geoportail-urbanisme.gouv.fr/") + "."),
           ("Déposez la déclaration préalable", "À la mairie, 9 place de l’Hôtel-de-Ville. Reims-Contact répond au 03 26 77 78 79 (" + L("annuaire de l’administration", _MAIRIE)
                                                + "). Comptez un mois d’instruction, deux en secteur protégé."),
           ("Faites autoriser l’échafaudage", "Sur le trottoir, il faut un permis de stationnement délivré par la mairie. L’instruction peut prendre deux mois, "
                                              "et l’absence de réponse vaut refus : déposez la demande tôt (" + L("Service-Public", _SP_ODP) + ")."),
           ("Appelez la Maison de l’habitat", "Conseil gratuit sur la rénovation énergétique et les aides, appel gratuit. Aucun devis ne doit être signé avant le dépôt "
                                              "de la demande d’aide (" + L("Maison de l’habitat", _MDH) + ").")],
    aides_intro="À Reims, les primes du Grand Reims se demandent avant toute commande.",
    aides=[("Maison de l’habitat du Grand Reims", "L’Espace Conseil France Rénov’ de Reims (" + L("annuaire de l’administration", _ECFR) + ") : conseil "
                                                  "gratuit sur la rénovation énergétique, l’adaptation du logement et les aides. 03 52 74 17 18, appel gratuit. "
                                                  "Entrée du public au 39 rue Bacquenois, 1er étage ; courrier au 19 rue de la Magdeleine ("
                                                  + L("lamaisondelhabitat-reims.fr", _MDH) + ")."),
           ("GrandReimsRénov’", "En complément de MaPrimeRénov’ Parcours accompagné : 10 % du montant hors taxes pour les ménages très modestes, "
                                "20 % pour les autres, avec un gain d’au moins deux classes énergétiques (" + L("ANIL", _GRR) + ", 2026)."),
           ("Prime Bas Carbone", "Pour remplacer une chaudière au fioul : jusqu’à 2 000 € pour une pompe à chaleur hors air-air ou une chaudière bois, "
                                 "4 000 € pour une pompe à chaleur hybride gaz, 5 000 € pour la géothermie. Ouverte jusqu’au 31 décembre 2027 ("
                                 + L("ANIL", _PBC) + ")."),
           ("Prime Air Bois", "1 200 € pour remplacer un foyer ouvert ou fermé, ou un appareil de chauffage au bois d’avant 2002, dans une résidence principale, "
                              "avec un professionnel RGE ("
                              + L("ANIL", _PAB) + ")."),
           NATIONAL],
    faq=[("Faut-il une autorisation pour changer ses fenêtres à Reims ?",
          "Oui, une déclaration préalable, instruite en un mois. Dans le site patrimonial remarquable du centre ou de Saint-Nicaise, comptez deux mois et "
          "l’accord de l’architecte des Bâtiments de France. Dans une cité-jardin, gardez les proportions des ouvertures d’origine."),
         ("Quelles règles dans le centre-ville de Reims ?",
          "Le centre est un site patrimonial remarquable de 201,6 hectares depuis l’arrêté du 28 mai 2020. Son PVAP, approuvé le 26 juin 2025, fixe les règles "
          "des travaux. Tout changement d’aspect extérieur demande une autorisation et l’accord de l’architecte des Bâtiments de France (UDAP de la Marne : "
          "03 26 47 74 39)."),
         ("Y a-t-il des caves ou des carrières sous Reims ?",
          "Oui : Géorisques recense 219 cavités souterraines sur la commune, dont 85 caves et 59 carrières. Avant une extension ou une surélévation, "
          "consultez la carte et faites étudier le sol."),
         ("Ma maison de cité-jardin est-elle protégée à Reims ?",
          "Si elle est dans l’une des 11 cités-jardins de la zone UP du PLU, oui : ouvertures à garder dans leurs proportions, décors de façade à conserver "
          "lors d’un ravalement et, au Chemin Vert et à Maison Blanche, couleurs d’origine des volets. Vérifiez le zonage avant de commander."),
         ("Quelles aides pour rénover son logement à Reims ?",
          "GrandReimsRénov’ (10 à 20 % du hors-taxe pour une rénovation d’ampleur), la Prime Bas Carbone (jusqu’à 5 000 € pour quitter le fioul), la Prime "
          "Air Bois (1 200 €) et les aides nationales. Conseil gratuit à la Maison de l’habitat : 03 52 74 17 18.")],
)

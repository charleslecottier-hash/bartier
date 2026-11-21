# Limoges : fiche locale de la page « Devis travaux à Limoges ». Sources officielles consultées le 21/11/2026.
# Chiffres Insee : jeu « Logements, principaux indicateurs (dossier complet) », RP 2023, lu via l'API Melodi
# (la page « dossier complet » d'insee.fr répondait en erreur 500 pendant la recherche).
# limoges.fr renvoie un 403 permanent (protection anti-robot) : règlements de la Ville lus via demarche.numerique.gouv.fr,
# PLU via le Géoportail de l'urbanisme. Le ravalement obligatoire (campagnes « RO ») n'a pas pu être vérifié : laissé de côté.
from villes_data import L, S, SP, NATIONAL  # liens dans le texte, sources discrètes, Service-Public, aides nationales

_INSEE = "https://api.insee.fr/melodi/data/DS_RP_LOGEMENT_PRINC?GEO=COM-87085"
_SPR = "https://www.limoges-metropole.fr/services/amenagement-et-voirie/sites-patrimoniaux-remarquables"
_SPR_CULT = "https://www.culture.gouv.fr/Thematiques/Monuments-Sites/Interventions-demarches/Realiser-des-travaux-dans-un-site-patrimonial-remarquable"
_GPU = "https://www.geoportail-urbanisme.gouv.fr/document/by-id/cc9a8ea272e7d4d9a12b20e51c62e68a"
_PLU = "https://www.geoportail-urbanisme.gouv.fr/api/document/cc9a8ea272e7d4d9a12b20e51c62e68a/files/87085_reglement_20260313.pdf"
_PLUI = "https://www.limoges-metropole.fr/services/amenagement-et-voirie/plu-et-plui-1"
_UDAP = ("https://www.culture.gouv.fr/regions/drac-nouvelle-aquitaine/Patrimoines-et-Architecture-a-la-DRAC-Nouvelle-Aquitaine/"
         "Les-Unites-departementales-de-l-architecture-et-du-patrimoine-en-Nouvelle-Aquitaine/udap-de-la-haute-vienne-87")
_TERM = ("https://www.haute-vienne.gouv.fr/Actions-de-l-Etat/Amenagement-du-territoire-construction-logement/"
         "Amenagement-et-construction-durables/Termites-et-merules")
_RADON = "https://georisques.gouv.fr/api/v1/radon?code_insee=87085"
_FRADON = "https://www.georisques.gouv.fr/sites/default/files/2023-05/Fiche-radon.pdf"
_CATNAT = "https://georisques.gouv.fr/api/v1/gaspar/catnat?code_insee=87085&page_size=100"
_MF = "https://donneespubliques.meteofrance.fr/FichesClim/FICHECLIM_87085006.pdf"
_FAC = "https://demarche.numerique.gouv.fr/commencer/demande-de-subvention-embellissement-facade-limoges"
_ODP = "https://demarche.numerique.gouv.fr/commencer/travaux-et-encombrement"
_GH = "https://guichet-habitat.limoges-metropole.fr/qui-sommes-nous-1"
_GH_AIDES = "https://guichet-habitat.limoges-metropole.fr/particuliers/aides-financieres"
_GH_RENOV = "https://guichet-habitat.limoges-metropole.fr/particuliers/economies-denergie/renover-son-logement"
_OPAH = "https://guichet-habitat.limoges-metropole.fr/particuliers/dispositifs-pour-lhabitat/opah-ru"

CITY = dict(
    slug="limoges", name="Limoges", cp="87000", insee="87085",
    lat=45.8344, lon=1.2617, dept="Haute-Vienne", depcode="87", region="Nouvelle-Aquitaine",
    wiki="https://fr.wikipedia.org/wiki/Limoges", wikidata="Q45656",
    verified="2026-11-21",
    tldr=("À Limoges, un site patrimonial remarquable de plus de 670 hectares encadre façades et toitures, et la Ville aide "
          "à ravaler les immeubles d’avant 1945 du centre élargi"),
    hook="Site patrimonial de 670 ha, aide façade de la Ville, radon à mesurer.",
    title="Devis travaux à Limoges : toiture, façade, fenêtres, isolation",
    desc=("Travaux à Limoges : site patrimonial de 670 ha, aide de la Ville aux façades d’avant 1945, nuancier municipal, "
          "radon. Un seul artisan vient chiffrer."),
    figures_intro="Ce qui compte avant des travaux, des bords de Vienne aux quartiers récents.",
    figures=[("72,0 <small>%</small>", "des logements sont des appartements", S("Insee, 2023", _INSEE)),
             ("46,2 <small>%</small>", "des résidences principales datent d’avant 1971", S("Insee, 2023", _INSEE)),
             ("670 <small>ha</small>", "au moins, couverts par le site patrimonial remarquable", S("Limoges Métropole", _SPR)),
             ("1 018 <small>mm</small>", "de pluie par an à Limoges-Bellegarde", S("Météo-France, normales 1991-2020", _MF))],
    answer=("À Limoges, 72,0 % des logements sont des appartements, et 46,2 % des résidences principales datent d’avant 1971. "
            "Le site patrimonial remarquable couvre plus de 670 hectares : y toucher à une façade, une toiture ou des fenêtres "
            "demande l’accord de l’architecte des Bâtiments de France. La Ville aide à ravaler les immeubles d’avant 1945 du "
            "centre élargi, à hauteur de 20 à 30 % des travaux."),
    facts=[("Site patrimonial", "Créé en 1995, révisé en 2004 et en 2007, il couvre plus de 670 hectares : quartiers historiques, "
                                "bords de Vienne, une partie de la rive gauche et plusieurs hameaux. Limoges Métropole en révise les "
                                "périmètres depuis décembre 2023 (" + L("Limoges Métropole", _SPR) + "). Les travaux sur l’extérieur "
                                "des immeubles y sont soumis à l’accord de l’architecte des Bâtiments de France ("
                                + L("ministère de la Culture", _SPR_CULT) + ")."),
           ("Urbanisme", "Le PLU de Limoges a été révisé et approuvé par Limoges Métropole le 26 juin 2019, puis modifié pour la "
                         "dernière fois le 17 décembre 2025 (" + L("Géoportail de l’urbanisme", _GPU) + "). Un PLU intercommunal est "
                         "en préparation depuis la délibération du 29 juin 2023 (" + L("Limoges Métropole", _PLUI) + ")."),
           ("Couleurs et toits", "Les teintes de façade se choisissent dans le nuancier municipal, selon le type d’architecture de "
                                 "l’immeuble. Dans les quartiers traditionnels, marqués par la tuile « rouge soutenu » ou l’ardoise, "
                                 "le PLU peut imposer des prescriptions de toiture (" + L("règlement du PLU", _PLU) + ")."),
           ("Termites et mérule", "Aucun arrêté préfectoral ne délimite de zone à risque en Haute-Vienne : le risque y est jugé "
                                  "sporadique, sous vigilance renforcée. Une découverte se déclare en mairie avec le formulaire "
                                  "Cerfa 12010 (" + L("préfecture de la Haute-Vienne", _TERM) + ", 2025)."),
           ("Radon", "Limoges est classée en potentiel radon de catégorie 3 (" + L("Géorisques", _RADON) + "). Dans ces communes, "
                     "l’État recommande de mesurer le radon pendant au moins deux mois, de mi-septembre à fin avril, avec un niveau "
                     "de référence de 300 Bq/m³ (" + L("fiche radon", _FRADON) + ")."),
           ("Climat et sols", "À Limoges-Bellegarde, 133,7 jours de pluie, 34,9 jours de gel et 17 jours de neige par an, et une "
                              "rafale record de 41 m/s, environ 148 km/h, le 27 décembre 1999 (" + L("Météo-France", _MF)
                              + ", normales 1991-2020). La commune a été reconnue cinq fois en catastrophe naturelle pour "
                              "sécheresse depuis 2018 (" + L("Géorisques", _CATNAT) + ").")],
    trades_intro="Colombages, immeubles Belle Époque, rues Art déco, pavillons en granit : le site patrimonial distingue six types d’architecture.",
    trades={
        "toiture": ["Dans les quartiers traditionnels, les toits sont en tuile « rouge soutenu » ou en ardoise (" + L("règlement du PLU", _PLU)
                    + "). Sur la carte des toitures de l’architecte des Bâtiments de France, Limoges se trouve en zone de frange entre "
                    "ardoise et tuile canal (" + L("UDAP 87", _UDAP) + ").",
                    "La Ville aide à refaire une couverture en ardoise ou en tuiles courbes : 30 € par m², sur 150 m² au plus, soit "
                    "4 500 € (" + L("Ville de Limoges", _FAC) + ", barème 2025). Avec 34,9 jours de gel et 17 jours de neige par an, "
                    "faites vérifier tuiles, ardoises et solins avant l’hiver."],
        "facade": ["Le centre mêle maisons à colombages sur base de pierre de taille, immeubles Belle Époque et rues Art déco. Le "
                   "quartier Locarno aligne des pavillons des années 1930 en blocage de granit. Chacun des six types d’architecture "
                   "du site patrimonial a ses règles de réhabilitation et son nuancier (" + L("PLU", _PLU) + ").",
                   "L’aide de la Ville vise les maisons et immeubles d’avant 1945 du centre élargi : 20 % des travaux de façade, sur "
                   "130 000 € HT au plus, soit 26 000 €. Avenues Georges-Dumas et De-Lattre-de-Tassigny, le taux passe à 30 %, soit "
                   "39 000 € (" + L("Ville de Limoges", _FAC) + ", barème 2025)."],
        "fenetres": ["Changer des fenêtres modifie l’aspect extérieur : une déclaration préalable est à faire en mairie ("
                     + L("Guichet Habitat", _GH_RENOV) + "). Dans le site patrimonial, l’architecte des Bâtiments de France a un mois "
                     "pour donner son accord, qui peut être assorti de prescriptions (" + L("ministère de la Culture", _SPR_CULT) + ").",
                     "L’aide façade de la Ville finance aussi les menuiseries, sauf en PVC (" + L("Ville de Limoges", _FAC) + "). En "
                     "zone de potentiel radon, l’État rappelle qu’après un changement de fenêtres, l’air doit rester assez renouvelé, "
                     "avec une aération chaque jour (" + L("fiche radon", _FRADON) + ")."],
        "charpente": ["Aucun arrêté termites ni mérule ne vise la Haute-Vienne, mais la préfecture suit le sujet de près. Si le "
                      "chantier révèle des termites ou de la mérule, l’occupant le déclare en mairie (" + L("préfecture", _TERM) + ").",
                      "Les plus vieux immeubles du centre ont des pans de bois apparents, jusqu’à la fin du XVIIIe siècle, ou une "
                      "structure en bois, du milieu du XVIIIe à la fin du XIXe siècle (" + L("PLU", _PLU) + "). Avant de refaire "
                      "l’enduit d’une façade à colombages, faites contrôler l’état des bois."],
        "isolation": ["Limoges Métropole annonce une prime de 1 500 € pour les rénovations en matériaux biosourcés, comme le bois, "
                      "le chanvre, la paille ou la ouate de cellulose, dans ses 20 communes (" + L("Guichet Habitat", _GH_AIDES) + "). "
                      "Dans le centre ancien, l’OPAH-RU aide les propriétaires sous conditions de ressources (" + L("OPAH-RU", _OPAH) + ").",
                      "Dans le site patrimonial, une isolation par l’extérieur change l’aspect de la façade et passe par l’accord de "
                      "l’architecte des Bâtiments de France. Partout, le PLU écarte climatiseurs et paraboles des façades vues de la rue, "
                      "sauf impossibilité technique (" + L("règlement du PLU", _PLU) + ")."]},
    steps_intro="Cinq étapes, de l’architecte des Bâtiments de France au trottoir.",
    steps=[("Vérifiez si vous êtes dans le site patrimonial", "L’UDAP de la Haute-Vienne donne un avis avant le dépôt, en ligne ou sur "
                                                            "rendez-vous. Hôtel Niaud, 35 rue des Vénitiens. 05 55 33 32 72, le lundi "
                                                            "de 14 h à 16 h 30, du mardi au jeudi de 9 h 30 à 12 h (" + L("UDAP 87", _UDAP) + ")."),
           ("Choisissez vos teintes", "Dans le nuancier municipal, selon le type d’architecture de l’immeuble ("
                                      + L("règlement du PLU", _PLU) + ")."),
           ("Déposez la déclaration préalable", "À la mairie de Limoges, en ligne ou sur papier. En site patrimonial, un dossier papier "
                                                "se dépose en 3 exemplaires et l’instruction prend en général 2 mois ("
                                                + L("Service-Public", SP + "F17578") + ")."),
           ("Demandez l’aide façade de la Ville", "En ligne, avec le récépissé de la déclaration préalable et les devis. Direction de la "
                                                  "stratégie urbaine, 64 avenue Georges-Dumas. 05 55 45 65 75 (" + L("démarche", _FAC) + ")."),
           ("Faites autoriser l’échafaudage", "Demande d’arrêté de travaux et d’encombrement du domaine public, en ligne, avec un plan "
                                              "d’installation, des photos et l’autorisation d’urbanisme. Direction des Espaces publics : "
                                              "05 55 45 63 17 (" + L("démarche", _ODP) + ").")],
    aides_intro="Commencez par le Guichet Habitat : le conseil y est gratuit et neutre.",
    aides=[("Guichet Habitat de Limoges Métropole", "Le service public de la rénovation de l’habitat pour les 20 communes de la "
                                                    "Métropole, avec ses conseillers France Rénov’ : conseil neutre et gratuit, sur "
                                                    "rendez-vous. 13 boulevard de la Borie, 87000 Limoges. 05 55 45 78 06. "
                                                    + L("guichet-habitat.limoges-metropole.fr", _GH) + "."),
           ("Aide de la Ville aux façades et toitures", "Pour les immeubles d’avant 1945 du centre élargi : 20 % des travaux de façade, "
                                                       "30 % avenues Georges-Dumas et De-Lattre-de-Tassigny, sur 130 000 € HT au plus. "
                                                       "Pour une couverture en ardoise ou en tuiles courbes, 30 €/m², jusqu’à 4 500 € ("
                                                       + L("Ville de Limoges", _FAC) + ", barème 2025)."),
           ("OPAH-RU du centre ancien", "Limoges Métropole et l’Anah aident, sous conditions de ressources, les propriétaires du centre "
                                        "ancien. Primes : jusqu’à 5 000 € pour acheter et rénover un logement de plus de 15 ans, plus "
                                        "3 000 € s’il est vide depuis plus de deux ans, et jusqu’à 5 000 € pour réunir deux logements "
                                        "en un seul d’au moins 50 m² (" + L("Guichet Habitat", _GH_AIDES) + ")."),
           NATIONAL],
    faq=[("Quelles aides pour ravaler sa façade à Limoges ?",
          "La Ville finance 20 % des travaux de façade des immeubles d’avant 1945 du centre élargi, et 30 % avenues Georges-Dumas "
          "et De-Lattre-de-Tassigny, sur 130 000 € HT au plus. Les menuiseries en PVC n’y ouvrent pas droit. Renseignements à la "
          "direction de la stratégie urbaine : 05 55 45 65 75."),
         ("Quelles règles dans le site patrimonial remarquable de Limoges ?",
          "Il couvre plus de 670 hectares, des quartiers historiques aux bords de Vienne. Les travaux sur l’extérieur d’un immeuble y "
          "demandent une autorisation et l’accord de l’architecte des Bâtiments de France, qui a un mois pour une déclaration préalable."),
         ("Faut-il une autorisation pour changer ses fenêtres à Limoges ?",
          "Oui, une déclaration préalable dès que l’aspect change. Dans le site patrimonial, l’architecte des Bâtiments de France "
          "donne son accord. L’aide façade de la Ville peut financer des menuiseries neuves, sauf en PVC."),
         ("Limoges est-elle en zone termites ou mérule ?",
          "Non. Aucun arrêté préfectoral ne délimite de zone à risque en Haute-Vienne, où le risque reste sporadique (préfecture, 2025). "
          "Une découverte se déclare tout de même en mairie."),
         ("Le radon concerne-t-il des travaux à Limoges ?",
          "Limoges est en potentiel radon de catégorie 3. L’État conseille de mesurer le radon pendant au moins deux mois en période "
          "de chauffe et, après un changement de fenêtres, de garder un renouvellement d’air suffisant. Le niveau de référence est de 300 Bq/m³."),
         ("Comment faire autoriser un échafaudage à Limoges ?",
          "Par la démarche en ligne de demande d’arrêté de travaux et d’encombrement du domaine public, avec un plan d’installation, "
          "des photos et l’autorisation d’urbanisme. Renseignements à la direction des Espaces publics : 05 55 45 63 17.")],
)

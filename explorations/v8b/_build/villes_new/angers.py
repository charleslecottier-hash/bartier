from villes_data import L, S, SP, NATIONAL  # liens dans le texte, sources discrètes, Service-Public, aides nationales
PUBLISH = "2026-12-05"  # vague 2 : publication deux semaines après la vague 1 (voir VILLES.md)

# Sources consultées le 21/11/2026.
_INSEE = "https://api.insee.fr/melodi/data/DS_RP_LOGEMENT_PRINC?GEO=COM-49007"  # dossier complet, RP 2023 (page insee.fr en erreur 500 ce jour)
_ALM = "https://www.angersloiremetropole.fr"
_SPR = _ALM + "/un-territoire-en-mouvement/urbanisme/site-patrimonial-remarquable/index.html"
_ARR_SPR = _ALM + "/fileadmin/user_upload/i.1.1_arrete_delimitation_spr.pdf"
_PSMV = _ALM + "/fileadmin/user_upload/psmv_c01_reglement-ecrit_apres-enquete.pdf"
_FC01 = _ALM + "/fileadmin/user_upload/ficheconseil-01_couverture.pdf"
_PLUI = _ALM + "/un-territoire-en-mouvement/plan-local-d-urbanisme-intercommunal/index.html"
_EVOL = _ALM + "/un-territoire-en-mouvement/plan-local-d-urbanisme-intercommunal/evolutions/index.html"
_MCM = _ALM + "/mon-quotidien/logement/mieux-chez-moi-un-accompagnement-a-la-renovation-de-votre-logement/index.html"
_WEBI = _ALM + "/fileadmin/user_upload/webinaire_-_renovation_globale_alm.pdf"
_TRAV = "https://www.angers.fr/services-demarches/demarches-pour-les-particuliers/demarches-liees-a-vos-travaux"
_FAQ = _TRAV + "/vos-travaux-faq/index.html"
_GNAU_P = (_TRAV + "/quelles-demarches-pour-obtenir-l-autorisation-d-urbanisme/"
           "deposer-un-dossier-sur-le-guichet-numerique-des-autorisations-d-urbanisme/index.html")
_GNAU = "https://gnau3.operis.fr/angers/gnau/#/"
_ODP = ("https://www.angers.fr/vivre-a-angers/voirie-deplacements/la-gestion-des-voies-publiques/"
        "organiser-ses-travaux-sur-l-espace-public-entreprises-et-particuliers/index.html")
_ODP_F = "https://www.angers.fr/fileadmin/user_upload/formulaire_de_demande_d_occupation_du_domaine_public.pdf"
_RAV = "https://presse.angers.fr/private/uploads/piecesjointes/cahier-de-deliberations-conseil-municipal-2909.pdf"
_RAV2 = "https://presse.angers.fr/private/uploads/piecesjointes/cahier-des-deliberations-conseil-municipal-1512.pdf"
_TERM = ("https://www.maine-et-loire.gouv.fr/Actions-de-l-Etat/Urbanisme-amenagement-du-territoire-construction-et-logement/"
         "Batiment-Construction/Termites-et-merule/Les-termites-dans-le-Maine-et-Loire")
_TERM_PL = "https://www.maine-et-loire.gouv.fr/contenu/telechargement/20449/135854/file/A4-Plaquette-Termites_Dec_2023.pdf"
_MERULE = ("https://www.maine-et-loire.gouv.fr/Actions-de-l-Etat/Urbanisme-amenagement-du-territoire-construction-et-logement/"
           "Batiment-Construction/Termites-et-merule/La-merule")
_MF = "https://donneespubliques.meteofrance.fr/FichesClim/FICHECLIM_49020001.pdf"
_SISM = "https://georisques.gouv.fr/api/v1/zonage_sismique?code_insee=49007"
_RADON = "https://georisques.gouv.fr/api/v1/radon?code_insee=49007"
_CATNAT = "https://georisques.gouv.fr/api/v1/gaspar/catnat?code_insee=49007&page_size=100"
_PPRI = "https://www.maine-et-loire.gouv.fr/contenu/telechargement/16720/113771/file/reglement_du_ppr_confluence_maine.pdf"
_MRAE = "https://www.mrae.developpement-durable.gouv.fr/IMG/pdf/pdl-2023-6820_decision_pprm_angers__49_2023dkpdl8.pdf"
_UDAP = "https://demarche.numerique.gouv.fr/commencer/udap49"

CITY = dict(
    slug="angers", name="Angers", cp="49000", insee="49007",
    lat=47.4736, lon=-0.5542, dept="Maine-et-Loire", depcode="49", region="Pays de la Loire",
    wiki="https://fr.wikipedia.org/wiki/Angers", wikidata="Q38380",
    verified="2026-11-21",
    tldr=("À Angers, le centre historique a son plan de sauvegarde depuis octobre 2024 : ardoise naturelle, chaux et menuiseries "
          "en bois y sont la règle, et dans toute la ville, repeindre ses volets demande une déclaration préalable"),
    hook="Plan de sauvegarde de 200 ha, ardoise et tuffeau.",
    title="Devis travaux à Angers : toiture, façade, fenêtres, isolation",
    desc=("Travaux à Angers : plan de sauvegarde de 200 ha, ardoise naturelle, volets sous déclaration, aides de la "
          "Métropole. Un seul artisan vient chiffrer."),
    figures_intro="Le bâti angevin en quatre chiffres, de la Doutre aux quartiers d’après-guerre.",
    figures=[("77,0 <small>%</small>", "des logements sont des appartements", S("Insee, 2023", _INSEE)),
             ("36,3 <small>%</small>", "des résidences principales datent d’avant 1971", S("Insee, 2023", _INSEE)),
             ("200 <small>ha</small>", "couverts par le plan de sauvegarde du centre historique", S("Angers Loire Métropole", _SPR)),
             ("16", "arrêtés de catastrophe naturelle pour inondation depuis 1982", S("Géorisques", _CATNAT))],
    answer=("À Angers, 77,0 % des logements sont des appartements et 36,3 % des résidences principales datent d’avant 1971. "
            "Dans le centre historique, le plan de sauvegarde en vigueur depuis le 24 octobre 2024 impose l’ardoise naturelle, "
            "les enduits à la chaux et interdit le PVC aux fenêtres. Dans toute la ville, ravaler ou repeindre une façade, "
            "et même des volets, demande une déclaration préalable."),
    facts=[("Centre historique", "Le site patrimonial remarquable, classé par arrêté ministériel du 31 janvier 2019, couvre le centre historique, "
                                 "les faubourgs et leurs espaces paysagers (" + L("arrêté", _ARR_SPR) + "). Sur environ 200 ha, le plan de sauvegarde "
                                 "approuvé le 16 octobre 2024 remplace le PLUi depuis le 24 octobre 2024 (" + L("Angers Loire Métropole", _SPR) + ")."),
           ("Façades et volets", "Ravaler une façade, la repeindre ou repeindre ses volets demande une déclaration préalable en mairie, comme "
                                 "percer un mur pour une fenêtre (" + L("Ville d’Angers", _FAQ) + "). Une clôture aussi, depuis la délibération "
                                 "du 17 septembre 2009."),
           ("Ravalement", "La Ville impose le ravalement par campagnes, dans des périmètres définis, et verse une aide municipale après les "
                          "travaux. Hors campagne, elle peut aider un immeuble d’intérêt historique ou architectural ("
                          + L("délibération du 29 septembre 2025", _RAV) + ")."),
           ("Urbanisme", "Le PLUi d’Angers Loire Métropole, approuvé le 13 février 2017 et révisé le 13 septembre 2021, a été modifié "
                         "pour la dernière fois le 17 décembre 2025. Sa révision générale n° 2 est engagée (" + L("Métropole", _EVOL) + ")."),
           ("Termites et mérule", "Angers ne figure dans aucun arrêté préfectoral termites ; dans l’arrondissement, Seiches-sur-le-Loir, "
                                  "La Ménitré et deux secteurs de Corzé sont classés (" + L("préfecture", _TERM) + "). Aucun arrêté mérule "
                                  "dans le Maine-et-Loire (" + L("préfecture", _MERULE) + ", 2026)."),
           ("Risques et climat", "Les bords de Maine relèvent du plan de prévention du risque inondation de la Confluence de la Maine, "
                                 "approuvé le 19 octobre 2009 (" + L("règlement", _PPRI) + ", " + L("Autorité environnementale", _MRAE)
                                 + "). Zone sismique 2, faible, et potentiel radon "
                                 "de catégorie 3, la plus élevée ("
                                 + L("Géorisques", _RADON) + "). À Beaucouzé, 709,3 mm de pluie et 31,6 jours de gel par an ("
                                 + L("Météo-France", _MF) + ", normales 1991-2020).")],
    trades_intro="Ardoise, tuffeau, schiste et pans de bois : dans le centre historique, chaque matériau a son article du plan de sauvegarde.",
    trades={
        "toiture": ["Dans le centre historique, l’ardoise doit être naturelle, de teinte foncée et mate, posée aux clous ou aux crochets. "
                    "Le faîtage se fait en terre cuite scellée à la chaux, dit « à l’angevine », ou en lignolet d’ardoise ; le faîtage en zinc "
                    "pré-patiné et la zinguerie en PVC ou en aluminium sont proscrits (" + L("règlement du PSMV", _PSMV) + ").",
                    "Une fenêtre de toit y est limitée à 80 cm de large sur 100 cm de haut, sur un seul niveau par versant. Beaucouzé compte "
                    "32,6 jours de rafales d’au moins 58 km/h par an, surtout de décembre à février (" + L("Météo-France", _MF) + ") : le faîtage "
                    "à l’angevine est le plus résistant, et le faîtage en zinc, le plus fragile, est à éviter aux vents forts ("
                    + L("fiche conseil n° 1", _FC01) + ")."],
        "facade": ["Les joints du tuffeau se refont au mortier de chaux naturelle avec sablon et poudre de tuffeau ; les joints au ciment sont "
                   "interdits, comme le sablage, le disque ou l’acide sur la pierre. Un enduit ciment qui dégrade le tuffeau doit être retiré, et "
                   "les enduits se font à la chaux naturelle et au sable de Loire (" + L("règlement du PSMV", _PSMV) + ").",
                   "Ravaler demande une déclaration préalable, et l’échafaudage sur le trottoir une autorisation demandée au moins 30 jours avant ("
                   + L("formulaire", _ODP_F) + "). Hors campagne, la Ville a par exemple versé 6 855,65 € pour un immeuble de la place Molière "
                   "en septembre 2025 (" + L("Ville d’Angers", _RAV) + ")."],
        "fenetres": ["Dans le plan de sauvegarde, le bois peint est le matériau de référence et peut être imposé. Le PVC, le noir et le blanc pur "
                     "sont interdits, et les volets roulants ne sont pas admis sur les bâtiments d’avant 1930, sauf s’ils étaient d’origine ("
                     + L("règlement du PSMV", _PSMV) + ").",
                     "Ailleurs, percer un mur pour une fenêtre demande une déclaration préalable. En zone inondable de la Confluence de la Maine, "
                     "le plan de prévention recommande portes, fenêtres et dormants en matériaux insensibles à l’eau (" + L("règlement du PPRi", _PPRI) + ")."],
        "charpente": ["Angers n’est pas classée en zone termites. Deux secteurs de Corzé le sont, par arrêtés de 2018 et 2023, et La Ménitré "
                      "depuis 2009 (" + L("préfecture", _TERM) + "). Dans ces zones, les bois doivent être protégés lors de travaux, et un état "
                      "termites est exigé à la vente (" + L("plaquette de la préfecture", _TERM_PL) + ", 2023).",
                      "Dans le centre historique, une charpente d’intérêt patrimonial doit rester apparente quand on isole les combles, et le "
                      "rehaussement de toiture pour isoler par l’extérieur n’est admis que s’il ne change pas le volume du toit ni des lucarnes ("
                      + L("règlement du PSMV", _PSMV) + ")."],
        "isolation": ["Angers Loire Métropole aide la rénovation globale jusqu’à 4 000 €, plus une prime basse consommation de 1 500 € si le "
                      "logement atteint l’étiquette A ou B après travaux, certaines aides sous conditions de revenus (" + L("Métropole", _WEBI) + ", juin 2026).",
                      "Dans le plan de sauvegarde, l’isolation par l’extérieur est interdite sur les pans de bois, et le polystyrène est refusé "
                      "sur les maçonneries traditionnelles, au profit d’isolants perméables à la vapeur d’eau. Elle reste plutôt réservée aux "
                      "façades ordinaires et aux pignons aveugles (" + L("règlement du PSMV", _PSMV) + ")."]},
    steps_intro="Dans l’ordre, du plan de sauvegarde aux quartiers récents.",
    steps=[("Vérifiez si vous êtes en secteur protégé", "La " + L("cartographie du PLUi et du PSMV", _SPR) + " donne les règles de chaque parcelle. "
                                                      "Pour l’avis de l’architecte des Bâtiments de France, les rendez-vous se prennent auprès de "
                                                      "la Métropole (" + L("UDAP 49", _UDAP) + ")."),
           ("Préparez le projet avec le service Droit des sols", "Ville d’Angers, 83 rue du Mail, sur rendez-vous. 02 41 05 40 99. "
                                                                 "pre-projet.angers@ville.angers.fr (" + L("Ville d’Angers", _FAQ) + ")."),
           ("Déposez la déclaration préalable", "En ligne sur le " + L("guichet GNAU", _GNAU) + ". La Ville envoie un numéro de dossier sous dix "
                                                "jours au plus (" + L("démarche", _GNAU_P) + ")."),
           ("Faites autoriser l’échafaudage", "La demande d’occupation du domaine public doit arriver au moins 30 jours avant, à "
                                              "espace.public@ville.angers.fr. 02 41 21 54 00 (" + L("formulaire", _ODP_F) + ")."),
           ("Passez par Mieux chez moi avant de signer", "Conseil gratuit sur les travaux et les aides, sans rendez-vous en semaine "
                                                         "(" + L("Métropole", _MCM) + ").")],
    aides_intro="Les aides se demandent avant de signer le devis, et le conseil public est gratuit.",
    aides=[("Mieux chez moi", "L’Espace conseil France Rénov’ de l’agglomération angevine : 83 rue du Mail, 49100 Angers. 02 41 43 00 00. "
                              "Sans rendez-vous du lundi au vendredi, de 9 h à 12 h 30 et de 13 h 30 à 17 h 30. Conseiller copropriété : "
                              "06 43 01 41 15. " + L("angersloiremetropole.fr", _MCM) + "."),
           ("Aide de la Métropole à la rénovation globale", "Jusqu’à 4 000 € pour une rénovation globale, plus 1 500 € si le logement atteint "
                                                            "l’étiquette A ou B après travaux. Certaines aides sont sous conditions de revenus ("
                                                            + L("Angers Loire Métropole", _WEBI) + ", 2026)."),
           ("Aide municipale au ravalement", "Dans les périmètres de campagne, et hors campagne pour les immeubles d’intérêt historique ou "
                                             "architectural. Elle est votée en conseil municipal et versée après les travaux : 8 340 € pour un "
                                             "immeuble rue du Chanoine-Colonel-Panaget en décembre 2025 (" + L("Ville d’Angers", _RAV2) + ")."),
           ("Conseil juridique sur le logement", "Des juristes spécialistes du logement étudient le plan de financement, les contrats et les "
                                                 "aides mobilisables. Rendez-vous au 02 41 43 00 00, touche 2 (" + L("Métropole", _MCM) + ")."),
           NATIONAL],
    faq=[("Le ravalement est-il obligatoire à Angers ?",
          "La Ville l’impose par campagnes, dans des périmètres définis, et verse alors une aide municipale après les travaux. "
          "Dans toute la ville, ravaler une façade demande une déclaration préalable."),
         ("Faut-il une autorisation pour repeindre ses volets à Angers ?",
          "Oui. Repeindre sa façade ou ses volets demande une déclaration préalable en mairie. Si l’échafaudage occupe le trottoir, "
          "demandez l’autorisation au moins 30 jours avant."),
         ("Peut-on poser des fenêtres en PVC dans le centre historique d’Angers ?",
          "Non. Le plan de sauvegarde interdit le PVC, le noir et le blanc pur ; le bois peint est la référence. Les volets roulants "
          "n’y sont pas admis sur les bâtiments d’avant 1930, sauf s’ils étaient d’origine."),
         ("Quelle couverture pour un toit dans le centre d’Angers ?",
          "De l’ardoise naturelle, foncée et mate, posée aux clous ou aux crochets, avec un faîtage à l’angevine ou en lignolet "
          "d’ardoise. Une fenêtre de toit est limitée à 80 cm sur 100 cm."),
         ("Angers est-elle en zone termites ?",
          "Non. Aucun arrêté préfectoral ne vise Angers. Dans l’arrondissement, Seiches-sur-le-Loir, La Ménitré et deux secteurs de "
          "Corzé sont classés. Le Maine-et-Loire n’a pas d’arrêté mérule."),
         ("Quelles aides pour rénover son logement à Angers ?",
          "Jusqu’à 4 000 € de la Métropole pour une rénovation globale, plus 1 500 € en étiquette A ou B, l’aide municipale au ravalement "
          "et les aides nationales. Mieux chez moi vous conseille gratuitement : 02 41 43 00 00.")],
)

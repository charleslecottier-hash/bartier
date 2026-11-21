from villes_data import L, S, SP, NATIONAL  # liens dans le texte, sources discrètes, Service-Public, aides nationales

# Sources consultées le 21/11/2026. La page insee.fr de Metz répond en erreur 500 ce jour : chiffres pris par l'API Melodi (RP 2023).
# Le projet de « règlement municipal des constructions » (délibération du 7 décembre 2023) n'est pas repris : son adoption n'a pas pu être vérifiée.
_INSEE = "https://api.insee.fr/melodi/data/DS_RP_LOGEMENT_PRINC?GEO=COM-57463"  # dossier complet, RP 2023
_PSMV = "https://plui.eurometropolemetz.eu/pour-approfondir/plan-de-sauvegarde-et-de-mise-en-valeur-psmv-de-metz"
_PSMV_REG = "https://si.eurometropolemetz.eu/fiches/plui_partage_typo3/psmv/3_Reglement/reglement_ecrit.pdf"  # règlement, décembre 2017
_PSMV_RP = "https://si.eurometropolemetz.eu/fiches/plui_partage_typo3/psmv/1_Rapport_de_presentation/PSMV_diagnostic_rapport.pdf"  # rapport, décembre 2017
_PDA = "https://plui.eurometropolemetz.eu/pour-approfondir/perimetres-delimites-des-abords-pda"
_PLU = "https://www.eurometropolemetz.eu/vivre-habiter/urbanisme-amenagement/consulter-les-informations-des-plu/le-plan-local-durbanisme-de-metz"
_PLUI = "https://www.eurometropolemetz.eu/vivre-habiter/urbanisme-amenagement/consulter-les-informations-des-plu"
_RAV = "https://metz.fr/pages/conseil_municipal/seances/cm220929/doc/6_d1664446346505.pdf"  # DCM 22-09-29-7, campagne Outre-Seille
_MF = "https://donneespubliques.meteofrance.fr/FichesClim/FICHECLIM_57039001.pdf"  # Metz-Frescaty, normales 1991-2020
_PCS = "https://metz.fr/fichiers/2023/02/13/PCS_2022.pdf"  # plan communal de sauvegarde 2022
_SISM = "https://georisques.gouv.fr/api/v1/zonage_sismique?code_insee=57463"
_CATNAT = "https://georisques.gouv.fr/api/v1/gaspar/catnat?code_insee=57463&page_size=100"
_UDAP = "https://www.culture.gouv.fr/regions/drac-grand-est/services/patrimoines-architecture/udap/udap-de-la-moselle"
_URBA = "https://metz.fr/famille/logement/permis_construire.php"
_PORTAIL = "https://urbanisme.eurometropolemetz.eu/"
_GEO = "https://geo.metzmetropole.fr/"
_ODP = "https://metz.fr/fichiers/2026/03/02/Formulaire_ODP_METZ_Stationnement_2026.pdf"
_ALEC = "https://www.alec-paysmessin.fr/maisons-individuelles/"
_RENOV = "https://www.eurometropolemetz.eu/vivre-habiter/se-loger/renover-son-logement"
_PA = "https://www.eurometropolemetz.eu/fileadmin/user_upload/mediatheque_metropole/DECISIONS/DECISIONS_2026/Programme_dActions_-_2026-08-18.pdf"
_FLYER = "https://www.eurometropolemetz.eu/fileadmin/user_upload/mediatheque_metropole/2024_Arborescence/Se_loger/202604_Flyer_permanences-renover_opah-ru.pdf"
_PAB = "https://www.eurometropolemetz.eu/vivre-habiter/se-loger/prime-air-bois"

CITY = dict(
    slug="metz", name="Metz", cp="57000", insee="57463",
    lat=49.1197, lon=6.1769, dept="Moselle", depcode="57", region="Grand Est",
    wiki="https://fr.wikipedia.org/wiki/Metz", wikidata="Q22690",
    verified="2026-11-21",
    tldr="À Metz, le secteur sauvegardé couvre 163 hectares, de la vieille ville à la Ville impériale bâtie sous l’Annexion, et la Ville peut exiger "
         "un ravalement au moins tous les dix ans depuis un arrêté préfectoral de 1984",
    hook="Secteur sauvegardé de 163 hectares, ravalement exigible tous les dix ans.",
    title="Devis travaux à Metz : toiture, façade, fenêtres, isolation",
    desc="Travaux à Metz : secteur sauvegardé de 163 ha, ravalement tous les 10 ans, campagne en Outre-Seille, aides de l’Eurométropole. Un seul artisan vient chiffrer.",
    figures_intro="Ce qui compte avant de lancer des travaux à Metz, de la pierre de Jaumont à la Nouvelle-Ville.",
    figures=[("85,3 <small>%</small>", "des logements sont des appartements", S("Insee, 2023", _INSEE)),
             ("44,9 <small>%</small>", "des résidences principales datent d’avant 1971", S("Insee, 2023", _INSEE)),
             ("163 <small>ha</small>", "de site patrimonial remarquable, sept fois le secteur sauvegardé de 1975", S("Eurométropole de Metz", _PSMV)),
             ("60,9 <small>jours</small>", "de gel par an à Metz-Frescaty", S("Météo-France, normales 1991-2020", _MF))],
    answer=("À Metz, 85,3 % des logements sont des appartements et 44,9 % des résidences principales datent d’avant 1971 (Insee, 2023). "
            "Dans le secteur sauvegardé de 163 hectares, toute construction ou démolition, travaux intérieurs compris, demande l’avis conforme "
            "de l’architecte des Bâtiments de France. Partout dans la commune, la Ville peut exiger un ravalement au moins tous les dix ans."),
    facts=[("Secteur sauvegardé", "Créé en 1975 sur 22,5 hectares, il couvre 163 hectares depuis 2010, de l’Outre-Seille à la Ville impériale. Son plan "
                                  "de sauvegarde révisé, approuvé le 22 décembre 2017, y remplace le PLU. Travaux intérieurs compris, tout y passe par une "
                                  "autorisation et l’avis conforme de l’architecte des Bâtiments de France (" + L("Eurométropole", _PSMV) + ")."),
           ("Abords des monuments", "Cinq périmètres délimités des abords ont été créés à Metz par arrêtés du 25 octobre 2024, dont celui des monuments "
                                    "historiques du centre. Ils remplacent le rayon de 500 mètres, et l’accord de l’architecte des Bâtiments de France "
                                    "y est requis (" + L("Eurométropole", _PDA) + ")."),
           ("Ravalement", "Metz figure sur la liste de l’arrêté préfectoral du 11 juillet 1984 : le maire peut enjoindre un ravalement au moins tous "
                          "les dix ans. Une campagne obligatoire de cinq ans vise depuis 2022 l’Outre-Seille, dont la rue des Allemands et la place "
                          "des Charrons (" + L("délibération du 29 septembre 2022", _RAV) + ")."),
           ("Urbanisme", "Le tribunal administratif de Strasbourg a annulé le PLUi de l’Eurométropole le 24 juillet 2025 (" + L("Eurométropole", _PLUI)
                         + "). Hors secteur sauvegardé, le PLU de Metz approuvé le 18 décembre 2008 s’applique, modifié en dernier lieu le "
                           "21 septembre 2026 (" + L("PLU de Metz", _PLU) + ")."),
           ("Inondation", "Le plan de prévention des risques d’inondation de la Moselle, de la Seille et du ruisseau de Vallières est approuvé par "
                          "arrêté préfectoral du 28 juin 2005. La crue de 1947 sert de référence (" + L("plan communal de sauvegarde", _PCS) + ", 2022)."),
           ("Climat", "À Metz-Frescaty, 713,5 mm de pluie par an, 118,1 jours de pluie et 60,9 jours de gel, dont 11,9 nuits à −5 °C ou moins ("
                      + L("Météo-France", _MF) + ", normales 1991-2020).")],
    trades_intro="Calcaire enduit et pierre de Jaumont dans la ville ancienne, grès et enduits travaillés dans la Nouvelle-Ville : le plan de sauvegarde fixe des règles par type d’immeuble.",
    trades={
        "toiture": ["Sur les immeubles protégés du secteur sauvegardé, seuls certains matériaux sont admis : tuile canal ou tuile mécanique rouge "
                    "pour les pentes de 20 à 30°, tuile queue de castor, tuile écaille ou ardoise naturelle au-delà. Les panneaux solaires et les "
                    "terrasses découpées dans le toit y sont interdits (" + L("règlement du plan de sauvegarde", _PSMV_REG) + ", 2017).",
                    "Chéneaux et gouttières s’y refont en zinc, en cuivre ou en plomb. Metz-Frescaty compte 118,1 jours de pluie et 32,9 jours de "
                    "rafales d’au moins 58 km/h par an, surtout de décembre à mars : faites contrôler tuiles et zinguerie avant l’hiver ("
                    + L("Météo-France", _MF) + ")."],
        "facade": ["Dans la ville ancienne, les murs de moellons calcaires sont enduits à la chaux, et la pierre de Jaumont, calcaire blond extrait à "
                   "13 km au nord, dessine encadrements, soubassements et bandeaux (" + L("rapport du plan de sauvegarde", _PSMV_RP) + ", 2017). "
                   "Dans le secteur sauvegardé, l’enduit ciment est proscrit sur ces murs, et la pierre se nettoie à l’eau à basse ou moyenne "
                   "pression, sans sablage ni hydrofuge (" + L("règlement", _PSMV_REG) + ").",
                   "Le maire peut enjoindre un ravalement partout dans la commune, au moins tous les dix ans. Dans le périmètre de la campagne "
                   "d’Outre-Seille, la déclaration préalable doit recevoir l’accord de l’architecte des Bâtiments de France ("
                   + L("Ville de Metz", _RAV) + ", 2022)."],
        "fenetres": ["Dans le secteur sauvegardé, les fenêtres neuves sont en bois, ou en métal si l’immeuble s’y prête, posées dans la feuillure : "
                     "la pose dite « rénovation » sur l’ancien dormant est interdite. Elles sont peintes, le blanc pur est interdit et le blanc "
                     "cassé est préconisé dans la Nouvelle-Ville (" + L("règlement du plan de sauvegarde", _PSMV_REG) + ").",
                     "Pour mieux isoler une fenêtre ancienne, le règlement privilégie un double vitrage mince dans les feuillures existantes ou une "
                     "seconde fenêtre intérieure, surtout dans les immeubles de l’Annexion. Leurs volets roulants d’origine se remplacent à "
                     "l’identique, coffre à l’intérieur et rails encastrés."],
        "charpente": ["Dans les immeubles protégés du secteur sauvegardé, les charpentes anciennes sont conservées ou restaurées. Retirer un entrait, "
                      "une panne ou un arbalétrier est interdit, ce qui peut empêcher d’aménager certains combles, et créer un second niveau de "
                      "comble l’est aussi (" + L("règlement du plan de sauvegarde", _PSMV_REG) + ").",
                      "Metz est en zone de sismicité 1, très faible (" + L("Géorisques", _SISM) + "). La commune a en revanche été reconnue neuf fois "
                      "en catastrophe naturelle pour sécheresse, de 2003 à 2022 (" + L("Géorisques", _CATNAT) + ") : sur une maison fissurée, faites "
                      "vérifier la structure avant de refaire la toiture."],
        "isolation": ["Dans le secteur sauvegardé, l’isolation par l’extérieur est interdite sur les monuments historiques et les immeubles de type A. "
                      "Elle peut être admise sur les façades invisibles depuis la rue ou sans décor, notamment celles de l’Annexion et de "
                      "l’entre-deux-guerres, avec corniches, bandeaux et encadrements reconstitués (" + L("règlement du plan de sauvegarde", _PSMV_REG) + ").",
                      "En Outre-Seille, l’Eurométropole ajoute aux aides de l’Anah 10 % des travaux d’énergie hors taxes, jusqu’à 3 500 €, pour les "
                      "propriétaires occupants modestes ou très modestes (" + L("Eurométropole", _RENOV) + ", 2026)."]},
    steps_intro="Dans l’ordre, de la carte des secteurs à l’échafaudage.",
    steps=[("Repérez votre secteur", "Secteur sauvegardé, abords d’un monument ou zone du PLU : cherchez votre adresse puis votre parcelle sur "
                                     + L("Géo Metz Métropole", _GEO) + " pour lire le règlement qui s’applique."),
           ("Montrez le projet à l’architecte des Bâtiments de France", "L’UDAP de la Moselle le reçoit chaque semaine à Metz, sur rendez-vous, avant "
                                                                        "le dépôt. 10/12 place Saint-Étienne. 03 87 36 08 27 (" + L("UDAP", _UDAP) + ")."),
           ("Déposez la déclaration préalable", "En ligne sur le " + L("portail urbanisme", _PORTAIL) + " de l’Eurométropole, qui instruit les "
                                                "dossiers de Metz. Par courrier : service Urbanisme réglementaire et qualité urbaine, 144 route de "
                                                "Thionville, 57050 Metz (" + L("Ville de Metz", _URBA) + ")."),
           ("Faites autoriser l’occupation de la rue", "Le permis ne vaut pas autorisation d’occuper le domaine public : le service Travaux et "
                                                       "coordination des espaces publics la délivre, après avis de l’urbanisme. Sur le plateau "
                                                       "piétonnier, un véhicule de chantier paie 19,80 € par jour en 2026, à demander 15 jours "
                                                       "avant : circulation@mairie-metz.fr, 03 87 55 54 52 (" + L("formulaire", _ODP) + ")."),
           ("Obtenez l’attestation de l’ALEC", "Pour MaPrimeRénov’ Parcours accompagné, MaPrimeAdapt’ ou MaPrimeRénov’ Copropriété, l’Eurométropole "
                                               "exige une attestation de l’Espace Conseil France Rénov’ avant le dépôt (" + L("programme d’actions 2026", _PA) + ").")],
    aides_intro="À Metz, l’ALEC du Pays Messin est la porte d’entrée des aides publiques à la rénovation.",
    aides=[("ALEC du Pays Messin", "L’Espace Conseil France Rénov’ de l’Eurométropole de Metz : conseils gratuits et indépendants, sur rendez-vous. "
                                   "2 rue du Four-du-Cloître, 57000 Metz. 03 87 50 82 21. " + L("alec-paysmessin.fr", _ALEC) + "."),
           ("OPAH-RU Outre-Seille 2025-2029", "Pour les propriétaires occupants modestes ou très modestes, l’Eurométropole ajoute aux aides de l’Anah 10 % des travaux "
                                              "d’énergie hors taxes, jusqu’à 3 500 €, et 20 %, jusqu’à 10 000 €, pour un logement très dégradé ("
                                              + L("Eurométropole", _RENOV) + "). Les copropriétés reçoivent 15 %, jusqu’à 6 000 € par logement ("
                                              + L("programme d’actions 2026", _PA) + "). Conseil gratuit de CALM-Soliha Moselle, en permanence le "
                                              "3e vendredi du mois au 71 rue Mazelle (" + L("calendrier 2026", _FLYER) + ")."),
           ("Prime Air Bois", "1 500 € pour remplacer une cheminée ouverte ou un appareil au bois d’avant 2005 par un appareil Flamme verte ou "
                              "équivalent, posé par un artisan RGE, 2 000 € pour les ménages modestes. Les travaux se commandent après la notification ("
                              + L("Eurométropole", _PAB) + ", 2026)."),
           NATIONAL],
    faq=[("Le ravalement est-il obligatoire à Metz ?",
          "Oui, sur injonction du maire, au moins tous les dix ans : Metz figure sur la liste de l’arrêté préfectoral du 11 juillet 1984. Une campagne "
          "obligatoire de cinq ans vise depuis 2022 l’Outre-Seille, et la déclaration préalable y passe par l’accord de l’architecte des Bâtiments de France."),
         ("Quelles règles dans le secteur sauvegardé de Metz ?",
          "Le plan de sauvegarde approuvé en 2017 couvre 163 hectares et remplace le PLU. Constructions, démolitions et même travaux intérieurs y "
          "demandent une autorisation et l’avis conforme de l’architecte des Bâtiments de France. Les panneaux solaires sont interdits sur les immeubles protégés."),
         ("Peut-on poser des fenêtres en PVC dans le centre de Metz ?",
          "Pas dans le secteur sauvegardé : les menuiseries neuves y sont en bois, ou en métal si l’immeuble s’y prête, et la pose dite « rénovation » "
          "est interdite. Dans les six périmètres d’abords de monuments, l’architecte des Bâtiments de France donne aussi son accord."),
         ("Metz est-elle en zone inondable ?",
          "En partie. Le plan de prévention des risques d’inondation, approuvé le 28 juin 2005, couvre la Moselle, la Seille et le ruisseau de "
          "Vallières. Vérifiez le zonage de votre parcelle avant des travaux au rez-de-chaussée."),
         ("Quelles aides pour rénover son logement à Metz ?",
          "En Outre-Seille, l’OPAH-RU ajoute jusqu’à 3 500 € pour des travaux d’énergie et jusqu’à 6 000 € par logement en copropriété. Dans toute "
          "l’Eurométropole, la Prime Air Bois va jusqu’à 2 000 €. Conseil gratuit à l’ALEC du Pays Messin : 03 87 50 82 21."),
         ("Quel PLU s’applique à Metz ?",
          "Depuis l’annulation du PLUi par le tribunal administratif de Strasbourg, le 24 juillet 2025, c’est le PLU communal approuvé le 18 décembre "
          "2008, modifié en dernier lieu le 21 septembre 2026. Dans le secteur sauvegardé, le plan de sauvegarde le remplace.")],
)

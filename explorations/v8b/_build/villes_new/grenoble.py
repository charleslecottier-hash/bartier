from villes_data import L, S, SP, NATIONAL  # liens dans le texte, sources discrètes, Service-Public, aides nationales
REVIEWED = "2026-11-21"

# Sources consultées le 21/11/2026.
_INSEE = "https://api.insee.fr/melodi/data/DS_RP_LOGEMENT_PRINC?GEO=COM-38185"
_SPR = ("https://sitdl.lametro.fr/urba_posplu/PLUI_GAM/5_Annexes/01_Servitudes_Utilite_publique/1C_SPR_Grenoble/"
        "1C_4_SPR_Reglement.pdf")
_RAV = "https://www.grenoble.fr/demarche/607/659-deposer-un-dossier-de-ravalement-de-facade.htm"
_DP = "https://www.grenoble.fr/demarche/478/659-faire-une-declaration-prealable-de-travaux-non-soumis-a-permis-de-construire.htm"
_SECT = "https://www.grenoble.fr/demarche/1048/659-realiser-des-travaux-en-secteur-protege.htm"
_STAT = "https://www.grenoble.fr/demarche/1270/659-demander-une-autorisation-de-stationnement-pour-travaux-ou-demenagement-hors-zone-pietonne.htm"
_GNAU = "https://depotdau.lametro.fr/gnau/#/"
_PLUI_APPRO = ("https://sitdl.lametro.fr/urba_posplu/PLUI_GAM/0_Procedure/Deliberations_Arretes/"
               "01_20191220_Deliberation_Approbation_PLUi.pdf")
_PLUI_EVOL = "https://www.grenoblealpesmetropole.fr/319-les-evolutions-du-plui.htm"
_TERM = "https://www.anil.org/adil-38/la-reglementation-en-isere/taxe-annuelle-sur-les-logements-vacants-1/"
_SISM = "https://georisques.gouv.fr/api/v1/zonage_sismique?code_insee=38185"
_PPRI = "https://www.isere.gouv.fr/contenu/telechargement/68884/550123/file/Plaquette_Informative_PPRi_Drac_Appro.pdf"
_MF = "https://donneespubliques.meteofrance.fr/FichesClim/FICHECLIM_38538002.pdf"
_ALEC = "https://www.alec-grenoble.org/4103-m-informer-et-etre-conseille.htm"
_MM_MAISON = "https://www.grenoblealpesmetropole.fr/180-isoler-ma-maison-avec-mur-mur.htm"
_MM_COPRO = "https://www.grenoblealpesmetropole.fr/181-isoler-une-copropriete-avec-mur-mur.htm"
_CP_COPRO = "https://www.grenoble.fr/uploads/Presse/pse_fichier/28/2169_122_CP-Aides-a-la-renovation-des-coproprietes.pdf"

CITY = dict(
    slug="grenoble", name="Grenoble", cp="38000", insee="38185",
    lat=45.1869, lon=5.7264, dept="Isère", depcode="38", region="Auvergne-Rhône-Alpes",
    wiki="https://fr.wikipedia.org/wiki/Grenoble", wikidata="Q1289",
    verified="2026-11-21",
    tldr=("À Grenoble, plus d’un tiers des résidences principales datent de 1946 à 1970, et la Métropole aide à les isoler "
          "avec Mur Mur, en copropriété comme en maison"),
    hook="Immeubles d’après-guerre, isolés avec l’aide Mur Mur.",
    title="Devis travaux à Grenoble : toiture, façade, fenêtres, isolation",
    desc=("Travaux à Grenoble : ravalement tous les 10 ans, centre en site patrimonial, zone termites, aides Mur Mur "
          "de la Métropole. Un seul artisan vient chiffrer."),
    figures_intro="Le parc grenoblois en quatre chiffres, entre immeubles d’après-guerre et étés chauds.",
    figures=[("95,4 <small>%</small>", "des logements sont des appartements", S("Insee, 2023", _INSEE)),
             ("34,4 <small>%</small>", "des résidences principales datent de 1946 à 1970", S("Insee, 2023", _INSEE)),
             ("1 200", "copropriétés construites entre 1945 et 1975", S("Ville de Grenoble, 2025", _CP_COPRO)),
             ("35,3 <small>jours</small>", "à 30 °C ou plus par an, à Grenoble-Le Versoud", S("Météo-France, 1999-2020", _MF))],
    answer=("À Grenoble, 95,4 % des logements sont des appartements, et 34,4 % des résidences principales datent de 1946 à 1970. "
            "Le ravalement y est obligatoire au moins tous les dix ans, et dans le site patrimonial remarquable du centre, "
            "l’architecte des Bâtiments de France doit donner son accord. La ville est aussi en zone de lutte contre les termites "
            "et en zone de sismicité 4."),
    facts=[("Ravalement", "Obligatoire au moins une fois tous les dix ans, sur rue comme sur cour. La Ville fixe ses campagnes "
                          "pluriannuelles par arrêté municipal, et le ravalement demande une déclaration préalable ("
                          + L("Ville de Grenoble", _RAV) + ")."),
           ("Centre ancien", "L’ancienne AVAP, créée le 18 novembre 2013, est devenue le site patrimonial remarquable. Elle couvre la "
                             "ville ancienne et ses extensions du XIXe siècle, de l’Île Verte au parc Paul-Mistral. Tout changement "
                             "d’aspect y demande l’accord de l’architecte des Bâtiments de France (" + L("règlement du SPR", _SPR) + ")."),
           ("Urbanisme", "Le PLUi de Grenoble-Alpes Métropole a été approuvé le 20 décembre 2019 (" + L("délibération", _PLUI_APPRO)
                         + "). Sa révision allégée n° 1, approuvée le 7 novembre 2025, y intègre le plan de prévention du risque "
                         "d’inondation du Drac aval (" + L("Métropole", _PLUI_EVOL) + "). Il protège certains bâtiments sur trois "
                         "niveaux, chacun avec ses prescriptions de travaux (" + L("Ville de Grenoble", _SECT) + ")."),
           ("Termites", "Grenoble fait partie des 21 communes de la zone de lutte et de surveillance créée par l’arrêté préfectoral "
                        "du 1er octobre 2002, avec Saint-Martin-d’Hères, Meylan ou La Tronche (" + L("ADIL de l’Isère", _TERM) + ")."),
           ("Séisme et inondation", "Grenoble est en zone de sismicité 4, moyenne (" + L("Géorisques", _SISM) + "). Elle entre aussi "
                                    "dans le plan de prévention du risque d’inondation du Drac aval, approuvé le 17 juillet 2023. "
                                    "En zone inondable, les mesures prescrites aux bâtiments existants, comme une zone refuge, sont à "
                                    "réaliser dans les 5 ans suivant l’approbation, dans la limite de 10 % de la valeur vénale du bien ("
                                    + L("préfecture de l’Isère", _PPRI) + ")."),
           ("Climat", "À la station de Grenoble-Le Versoud : 67,2 jours de gel, 35,3 jours à 30 °C ou plus et 981,1 mm de pluie par an, "
                      "mais seulement 13,6 jours de rafales d’au moins 58 km/h (" + L("Météo-France", _MF) + ", 1999-2020).")],
    trades_intro=("Immeubles d’après-guerre, pierre calcaire, ciment moulé du XIXe siècle et toits de tuiles : à Grenoble, "
                  "les règles changent d’un quartier à l’autre."),
    trades={
        "toiture": ["Dans le site patrimonial remarquable, les toits des immeubles protégés gardent leur pente et leur forme. On y "
                    "couvre en tuile canal ou mécanique de terre cuite rouge brun ou rouge vieilli, en tuile plate petit moule ou en "
                    "ardoise, conservée là où elle était d’origine. Fibrociment, tôle ondulée, bac acier et PVC y sont interdits ("
                    + L("règlement du SPR", _SPR) + ").",
                    "Une fenêtre de toit y reste invisible de face depuis la rue, mesure au plus 78 × 140 cm ou moins de 1 m², et prend le modèle "
                    "« patrimoine » à meneau central sur les immeubles d’avant le milieu du XXe siècle. Le règlement conseille de l’équiper "
                    "d’un store extérieur, surtout à l’est, au sud et à l’ouest (" + L("règlement du SPR", _SPR) + ") : on compte 35,3 jours "
                    "à 30 °C ou plus par an à Grenoble-Le Versoud."],
        "facade": ["Le ravalement est obligatoire au moins tous les dix ans, par campagnes fixées par arrêté municipal. L’architecte "
                   "conseil de la Ville aide à définir les travaux (04 76 76 36 12), et un carnet couleurs par type d’immeuble guide "
                   "les teintes. Les propriétaires modestes et très modestes reçoivent 10 % du reste à charge, jusqu’à 2 000 € ("
                   + L("Ville de Grenoble", _RAV) + ").",
                   "Autour de la place Victor-Hugo, les immeubles du XIXe siècle exploitent le ciment moulé : ces décors ne "
                   "s’enduisent pas. Les murs en moellons faits pour être enduits se ré-enduisent à la chaux naturelle ou au ciment "
                   "naturel selon l’époque, "
                   "jamais au ciment artificiel (" + L("règlement du SPR", _SPR) + ")."],
        "fenetres": ["Dans le site patrimonial remarquable, les menuiseries des immeubles protégés sont en bois ou en métal. Le PVC y "
                     "est interdit, et des fenêtres en PVC déjà posées sur la façade ne servent pas d’argument. Le blanc et le bois "
                     "laissé naturel sont refusés, sauf disposition d’origine (" + L("règlement du SPR", _SPR) + ").",
                     "Un remplacement partiel y demande un plan d’ensemble de la façade, approuvé par la copropriété le cas échéant ("
                     + L("règlement du SPR", _SPR) + "). Pendant un ravalement, la "
                     "Ville finance 20 à 30 % du prix hors taxes des menuiseries en bois, selon vos ressources, sur devis global "
                     "de la façade (" + L("Ville de Grenoble", _RAV) + ")."],
        "charpente": ["Grenoble est en zone de lutte et de surveillance contre les termites depuis l’arrêté préfectoral du 1er octobre "
                      "2002. Profitez d’une réfection de toiture pour faire contrôler les bois. À la vente, l’état relatif aux termites "
                      "doit dater de moins de six mois (" + L("ADIL de l’Isère", _TERM) + ").",
                      "Dans le site patrimonial remarquable, faîtages, rives et arêtiers d’origine sont conservés ou refaits à "
                      "l’identique. Les débords de toit gardent au moins 50 cm, à chevrons apparents ou voliges sous rampant, avec "
                      "des planches d’égout en bois de 18 cm de haut au plus (" + L("règlement du SPR", _SPR) + ")."],
        "isolation": ["Mur Mur, l’aide de la Métropole, prend en charge à 100 % l’accompagnement des copropriétés de plus de 15 ans, "
                      "et finance 80 % de l’étude de maîtrise d’œuvre, jusqu’à 8 000 €, si le projet vise au moins 35 % de gain "
                      "énergétique (" + L("Métropole", _MM_COPRO)
                      + "). À Grenoble, 1 200 copropriétés datent de 1945 à 1975, et 300 sont inscrites au dispositif depuis 2015 ("
                      + L("Ville de Grenoble", _CP_COPRO) + ", 2025).",
                      "Dans le site patrimonial remarquable, l’isolation par l’extérieur en panneaux est interdite sur les immeubles "
                      "les plus protégés, et le polystyrène comme le polyuréthane y sont exclus. Un enduit isolant de type chaux-chanvre "
                      "reste possible s’il préserve les décors (" + L("règlement du SPR", _SPR) + "). Pour un enduit isolant, la Ville "
                      "verse 2 % du coût des travaux aux copropriétés qui obtiennent le label de la Fondation du patrimoine ("
                      + L("Ville de Grenoble", _RAV) + ")."]},
    steps_intro="Dans l’ordre, du centre ancien aux quartiers d’après-guerre.",
    steps=[("Vérifiez si votre immeuble est protégé", "Dans le site patrimonial remarquable, l’architecte des Bâtiments de France doit "
                                                      "donner son accord. Aux abords d’un monument historique, son accord est requis en "
                                                      "périmètre délimité ou en covisibilité. Un bâtiment repéré au PLUi suit ses propres prescriptions. Le "
                                                      "Service Conseil et Urbanisme Réglementaire répond les lundis, mardis et jeudis de 9 h "
                                                      "à 12 h. 04 76 76 39 62 (" + L("Ville de Grenoble", _SECT) + ")."),
           ("Préparez le ravalement avec la Ville", "Si vous avez reçu un arrêté de ravalement, la Ville conseille d’appeler l’architecte "
                                                    "conseil pour préciser le programme des travaux : 04 76 76 36 12. Les dossiers d’aide "
                                                    "se demandent au Service Conseil et Urbanisme Réglementaire (" + L("Ville de Grenoble", _RAV)
                                                    + ")."),
           ("Déposez la déclaration préalable", "En ligne sur le " + L("guichet numérique", _GNAU) + " de la Métropole, ou à l’accueil "
                                                "de l’Hôtel de Ville, 11 boulevard Jean-Pain. L’instruction prend un mois, un de plus "
                                                "en secteur protégé (" + L("Ville de Grenoble", _DP) + ")."),
           ("Faites autoriser le chantier sur la voie publique", "Toute occupation du domaine public est soumise à autorisation et à "
                                                                 "redevance. Pour réserver des places de stationnement pendant les "
                                                                 "travaux, l’entreprise fait la demande en ligne à la Ville au moins "
                                                                 "15 jours ouvrés avant. Les arrêtés de circulation pour travaux se "
                                                                 "demandent aussi en ligne (" + L("démarche", _STAT) + ")."),
           ("Appelez l’ALEC avant de signer", "Conseil gratuit sur Mur Mur et les autres aides. 04 76 00 19 09.")],
    aides_intro="Ne commencez pas les travaux avant d’avoir reçu la notification de l’aide.",
    aides=[("ALEC de la métropole grenobloise", "L’Espace Conseil France Rénov’ de la métropole : conseil gratuit, neutre et "
                                                "indépendant, sur rendez-vous. 14 avenue Benoît-Frachon, 38400 Saint-Martin-d’Hères. "
                                                "04 76 00 19 09. " + L("alec-grenoble.org", _ALEC) + "."),
           ("Mur Mur maisons", "Pour une résidence principale de plus de 15 ans : 80 % de l’audit énergétique, jusqu’à 700 €, puis une "
                               "prime travaux de 600 € à 11 800 € selon le projet et vos ressources, avec au moins trois postes dont "
                               "l’isolation des murs ou de la toiture (" + L("Métropole", _MM_MAISON) + ")."),
           ("Mur Mur copropriétés", "Accompagnement pris en charge à 100 % par la Métropole, et 80 % de l’étude de maîtrise d’œuvre, "
                                    "jusqu’à 8 000 €, si le projet vise au moins 35 % de gain énergétique. Jusqu’à 75 % des travaux "
                                    "pour les propriétaires occupants les plus modestes (" + L("Métropole", _MM_COPRO)
                                    + "). La Ville ajoute des aides quand la rénovation vise le niveau BBC ("
                                    + L("Ville de Grenoble", _CP_COPRO) + ", 2025)."),
           ("Aides de la Ville au ravalement", "10 % du reste à charge, jusqu’à 2 000 €, pour les propriétaires modestes et très "
                                               "modestes. 20 à 30 % du prix hors taxes des menuiseries en bois remplacées pendant le "
                                               "ravalement. 2 % du coût pour un enduit isolant labellisé par la Fondation du "
                                               "patrimoine (" + L("Ville de Grenoble", _RAV) + ")."),
           NATIONAL],
    faq=[("Le ravalement est-il obligatoire à Grenoble ?",
          "Oui, au moins une fois tous les dix ans, sur rue comme sur cour. La Ville lance des campagnes par arrêté municipal, et le "
          "ravalement demande une déclaration préalable. Les propriétaires modestes reçoivent 10 % du reste à charge, jusqu’à 2 000 €."),
         ("Peut-on poser des fenêtres en PVC à Grenoble ?",
          "Pas sur les immeubles protégés du site patrimonial remarquable : les menuiseries y sont en bois ou en métal, et le blanc est "
          "refusé sauf disposition d’origine. Ailleurs, modifier l’aspect d’une façade demande une déclaration préalable."),
         ("Grenoble est-elle en zone termites ?",
          "Oui. L’arrêté préfectoral du 1er octobre 2002 place Grenoble et 20 autres communes de l’agglomération en zone de lutte et de "
          "surveillance. À la vente, l’état relatif aux termites doit dater de moins de six mois."),
         ("Quelles aides pour isoler sa copropriété à Grenoble ?",
          "Mur Mur, de la Métropole, accompagne gratuitement les copropriétés de plus de 15 ans et finance 80 % de l’étude de maîtrise "
          "d’œuvre, jusqu’à 8 000 €. La Ville ajoute des aides si le projet vise le niveau BBC. L’ALEC vous conseille : 04 76 00 19 09."),
         ("Peut-on isoler par l’extérieur dans le centre de Grenoble ?",
          "Dans le site patrimonial remarquable, les panneaux isolants sont interdits sur les immeubles les plus protégés, et le "
          "polystyrène comme le polyuréthane sont exclus. Un enduit isolant de type chaux-chanvre reste possible s’il préserve les décors."),
         ("Comment déposer une déclaration préalable à Grenoble ?",
          "En ligne sur le guichet numérique de la Métropole, ou à l’Hôtel de Ville, 11 boulevard Jean-Pain. L’instruction prend un mois, "
          "un de plus si l’architecte des Bâtiments de France est consulté. Renseignements : 04 76 76 39 62.")],
)

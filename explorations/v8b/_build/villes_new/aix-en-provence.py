from villes_data import L, S, SP, NATIONAL  # liens dans le texte, sources discrètes, Service-Public, aides nationales

# Sources consultées le 21/11/2026.
_INSEE = "https://api.insee.fr/melodi/data/DS_RP_LOGEMENT_PRINC?GEO=COM-13001"  # dossier complet, RP 2023 (page insee.fr en erreur 500 ce jour)
_MERIMEE = "https://pop.culture.gouv.fr/notice/merimee/SPR9300019"
_PSMV = "https://www.aixenprovence.fr/Consulter-le-PSMV"
_PSMV_REGL = "https://www.aixenprovence.fr/IMG/pdf/reglement_m3-m4_psmv_aix_approbation.pdf"  # règlement, modification n° 4, juillet 2026
_PSMV_EP = "https://www.aixenprovence.fr/IMG/pdf/2_conclusions_motivees_et_avis_du_commissaire_enqueteur_psmv_aix-2.pdf"
_PLUI = "https://www.aixenprovence.fr/Le-Plan-local-d-urbanisme-intercommunal-PLUi"
_PPRIF = ("https://www.georisques.gouv.fr/donnee-risques/PPR/Fiche-ppr/pprn/13DDTM20210011/document/"
          "5f09ae73-7f24-4b33-b6dc-3da0f6c8326f")  # règlement du PPR incendie de forêt, approuvé le 10 juillet 2026
_RGA = "https://www.aixenprovence.fr/IMG/pdf/3_pprnp_retrait_gonflement_des_argiles_reglement-2.pdf"
_PPRI = "https://www.aixenprovence.fr/IMG/pdf/3_20200302_ppri_aix_reglement_approuve.pdf"
_CATNAT = "https://georisques.gouv.fr/api/v1/gaspar/catnat?code_insee=13001&page_size=100"
_SISM = "https://georisques.gouv.fr/api/v1/zonage_sismique?code_insee=13001"
_MF = "https://donneespubliques.meteofrance.fr/FichesClim/FICHECLIM_13001009.pdf"
_DEPOT = "https://www.aixenprovence.fr/Depot-des-demandes-d-urbanisme-en-ligne"
_VOIRIE = "https://www.aixenprovence.fr/Modalites-travaux-batiments"
_UDAP = ("https://www.culture.gouv.fr/regions/drac-provence-alpes-cote-d-azur/la-direction-regionale-des-affaires-culturelles-"
         "drac-provence-alpes-cote-d-azur/unites-departementales-de-l-architecture-et-du-patrimoine-udap-de-provence-alpes-cote-"
         "d-azur/udap-des-bouches-du-rhone")
_CPIE = "https://cpie-paysdaix.com/contact/"
_ALLO = "https://www.anil.org/adil-13/notre-expertise/lutte-contre-lhabitat-degrade-/allo-metropole-renov/"
_CD13 = "https://www.departement13.fr/sites/default/files/media/downloads/cp_12-09-2025_mesures-rechauffement-climatique.pdf"
_CD13_HAB = "https://www.departement13.fr/en-actions/logement-habitat/les-dispositifs-aides/habitat-des-aides-concretes-pour-realiser-vos-0"

CITY = dict(
    slug="aix-en-provence", name="Aix-en-Provence", cp="13100", insee="13001",
    lat=43.5311, lon=5.4540, dept="Bouches-du-Rhône", depcode="13", region="Provence-Alpes-Côte d’Azur",
    wiki="https://fr.wikipedia.org/wiki/Aix-en-Provence", wikidata="Q47465",
    verified="2026-11-21",
    tldr=("À Aix-en-Provence, le centre ancien est un secteur sauvegardé depuis 1964, et les maisons proches des massifs boisés "
          "ont jusqu’en 2031 pour se protéger du feu de forêt"),
    hook="Secteur sauvegardé depuis 1964, et plan incendie de forêt de 2026.",
    title="Devis travaux à Aix-en-Provence : toiture, façade, fenêtres, isolation",
    desc=("Travaux à Aix-en-Provence : secteur sauvegardé, tuiles creuses et chaux, plan incendie de forêt 2026, argiles, "
          "aides locales. Un seul artisan vient chiffrer."),
    figures_intro="Le parc aixois en quatre chiffres, entre immeubles anciens et étés secs.",
    figures=[("79,6 <small>%</small>", "des logements sont des appartements", S("Insee, 2023", _INSEE)),
             ("37,7 <small>%</small>", "des résidences principales datent d’avant 1971", S("Insee, 2023", _INSEE)),
             ("55,2 <small>jours</small>", "à 30 °C ou plus par an, à la station d’Aix-en-Provence", S("Météo-France, 1991-2020", _MF)),
             ("14", "épisodes de sécheresse reconnus en catastrophe naturelle depuis 1989", S("Géorisques", _CATNAT))],
    answer=("À Aix-en-Provence, 79,6 % des logements sont des appartements et 37,7 % des résidences principales datent d’avant 1971. "
            "Le centre ancien est un secteur sauvegardé depuis 1964 : tuiles creuses, enduits à la chaux et menuiseries sans PVC y sont "
            "la règle. Près des massifs boisés, le plan de prévention des risques d’incendie de forêt approuvé le 10 juillet 2026 "
            "impose aux maisons exposées des travaux de protection d’ici juillet 2031."),
    facts=[("Secteur sauvegardé", "Le centre ancien, à l’intérieur des boulevards de ceinture, est un secteur sauvegardé créé le "
                                  "17 décembre 1964 (" + L("ministère de la Culture", _MERIMEE) + "). Son plan de sauvegarde, approuvé "
                                  "le 27 juin 2012 et modifié le 28 juin 2024, règle chaque façade et chaque toit ("
                                  + L("Ville d’Aix-en-Provence", _PSMV) + "). Les modifications n° 3 et 4 ont reçu un avis favorable "
                                  "après l’enquête publique d’avril 2026 (" + L("commissaire enquêteur", _PSMV_EP) + ")."),
           ("Urbanisme", "Hors secteur sauvegardé, c’est le PLUi du Pays d’Aix qui s’applique. Le conseil de la Métropole "
                         "Aix-Marseille-Provence l’a approuvé le 5 décembre 2024, puis modifié le 15 décembre 2025 ("
                         + L("Ville d’Aix-en-Provence", _PLUI) + ")."),
           ("Feu de forêt", "Le plan de prévention des risques d’incendie de forêt de la commune a été approuvé le 10 juillet 2026. "
                            "En zone rouge ou bleue, le propriétaire d’une maison fait un auto-diagnostic, puis les travaux de "
                            "protection utiles d’ici le 10 juillet 2031, pour un coût plafonné à 10 % de la valeur du bien ("
                            + L("règlement du PPRIF", _PPRIF) + ")."),
           ("Argiles", "Toute la commune relève du plan de prévention du retrait-gonflement des argiles approuvé le 27 juin 2012 ("
                       + L("règlement", _RGA) + "). De 1989 à 2023, 14 épisodes de sécheresse y ont été reconnus en catastrophe "
                       "naturelle (" + L("Géorisques", _CATNAT) + ")."),
           ("Séisme et inondation", "Aix-en-Provence est en zone de sismicité 4, moyenne (" + L("Géorisques", _SISM) + "). Le long "
                                    "de l’Arc et de ses affluents, la Torse, le Grand Vallat, la Petite Jouïne et la Luynes, le plan "
                                    "de prévention du risque d’inondation approuvé le 2 mars 2020 fixe ses propres prescriptions ("
                                    + L("règlement du PPRI", _PPRI) + ")."),
           ("Climat", "À la station d’Aix-en-Provence : 608,8 mm de pluie par an, tombés en 58,9 jours seulement, 55,2 jours à 30 °C "
                      "ou plus et 43,2 jours de gel. Records : 42 °C le 28 juin 2019, et 222 mm en un jour le 22 septembre 1993 ("
                      + L("Météo-France", _MF) + ", normales 1991-2020).")],
    trades_intro=("Hôtels particuliers et immeubles du centre, maisons au bord des massifs : à Aix, les règles changent entre le "
                  "secteur sauvegardé et les zones exposées au feu de forêt."),
    trades={
        "toiture": ["Le toit aixois est pour l’essentiel en tuiles creuses. Dans le secteur sauvegardé, on le restaure à l’identique, "
                    "même pente et même disposition, avec des tuiles de réemploi en chapeau ou des tuiles neuves panachées. Les tuiles "
                    "neuves vieillies artificiellement sont exclues, les terrasses tropéziennes interdites, et seules 2 ou 3 tabatières "
                    "de 0,25 m² par versant éclairent les combles (" + L("règlement du PSMV", _PSMV_REGL) + ").",
                    "Près des massifs boisés, les règles de construction du plan incendie de forêt visent des toitures classées "
                    "Broof (t3), des fenêtres de toit en verre feuilleté 44.2 au moins, et des gouttières en matériau M1 au moins, "
                    "équipées pour évacuer feuilles et aiguilles (" + L("règlement du PPRIF", _PPRIF) + ")."],
        "facade": ["Dans le secteur sauvegardé, la façade est en pierre de taille de tons ocres, ou enduite à la chaux naturelle et "
                   "finie par un badigeon de chaux teinté de pigments de terre naturels. Joints au ciment, enduits prêts à l’emploi à "
                   "base de résine et crépis tyroliens y sont interdits, comme le décroûtage au marteau pneumatique ("
                   + L("règlement du PSMV", _PSMV_REGL) + ").",
                   "Avec 14 épisodes de sécheresse reconnus en catastrophe naturelle depuis 1989, une fissure en façade peut venir du "
                   "sol argileux : faites-en chercher la cause avant de la reboucher. En zone B2 du plan argiles, le règlement "
                   "recommande de rejeter les eaux de pluie à 5 m au moins de la maison (" + L("plan argiles", _RGA) + ")."],
        "fenetres": ["Dans le secteur sauvegardé, les menuiseries en PVC et les coffres de volets roulants apparents sont proscrits. "
                     "Les fenêtres du XVIIIe siècle à petits carreaux se restaurent sans double vitrage, en teinte claire comme le gris "
                     "perle ou le blanc cassé. Celles du XIXe siècle à grands carreaux peuvent recevoir un double vitrage qui garde la "
                     "découpe et la finesse des bois (" + L("règlement du PSMV", _PSMV_REGL) + ").",
                     "Les fenêtres du XIXe siècle s’y peignent en gris moyen ou dans une teinte neutre, moyenne ou sombre, et les volets "
                     "à barre et écharpe sont interdits. Ailleurs, changer l’aspect de ses fenêtres demande une déclaration préalable ("
                     + L("Service-Public", SP + "F17578") + ")."],
        "charpente": ["Sur un immeuble « à conserver » du secteur sauvegardé, une réfection complète de couverture se fait à la manière "
                      "ancienne : tuiles creuses posées sur volige et quartons ou sur malons, sans sous-toiture. Corniches à gorge, "
                      "génoises en tuiles et débords à chevrons sont restaurés selon leur disposition d’origine ("
                      + L("règlement du PSMV", _PSMV_REGL) + ").",
                      "Aix-en-Provence est en zone de sismicité 4, moyenne : signalez-le à l’artisan avant une surélévation ou une "
                      "reprise de charpente. En zone B2 du plan argiles, planter un arbre plus près d’un bâtiment que sa hauteur adulte "
                      "est interdit, sauf écran anti-racines de 2 m de profondeur (" + L("plan argiles", _RGA) + ")."],
        "isolation": ["On compte 55,2 jours à 30 °C ou plus par an à Aix-en-Provence, et 43,2 jours de gel (" + L("Météo-France", _MF)
                      + ", 1991-2020). Isoler la toiture limite la surchauffe des derniers étages l’été comme les pertes de chaleur "
                      "l’hiver.",
                      "Provence Éco-Rénov, l’aide du Département, finance l’isolation du bâti des propriétaires occupants : jusqu’à 25 % "
                      "du coût TTC, dans la limite de 4 000 € (" + L("Département", _CD13) + ", 2025). Près des massifs boisés, les "
                      "règles du plan incendie de forêt s’appliquent aussi à l’isolation par l’extérieur, qui doit atteindre la réaction "
                      "au feu C-s3,d0 (" + L("règlement du PPRIF", _PPRIF) + ")."]},
    steps_intro="Dans l’ordre, du centre ancien aux quartiers proches des massifs.",
    steps=[("Situez votre adresse", "Entre les boulevards de ceinture, du cours Sextius au boulevard du Roi-René, vous êtes dans le "
                                    "secteur sauvegardé : l’architecte des Bâtiments de France se prononce sur le projet. Son service, "
                                    "l’UDAP des Bouches-du-Rhône, reçoit sur rendez-vous. 04 91 90 42 43 (" + L("UDAP 13", _UDAP) + ")."),
           ("Regardez les plans de risques", "Près des massifs, vérifiez le zonage du plan incendie de forêt. Partout, regardez celui "
                                             "du plan argiles. Le règlement du plan incendie se consulte en mairie et sur le site de "
                                             "la préfecture (" + L("PPRIF", _PPRIF) + ")."),
           ("Déposez la déclaration préalable", "En ligne sur Géopermis depuis le 1er janvier 2022, ou sur papier à la Direction de "
                                                "l’urbanisme réglementaire, 3 rue Loubet (" + L("Ville d’Aix-en-Provence", _DEPOT)
                                                + "). En secteur sauvegardé, l’instruction prend 2 mois au lieu d’un ("
                                                + L("Service-Public", SP + "F17578") + ")."),
           ("Faites autoriser l’échafaudage", "Un permis de stationnement, à demander à la Direction Gestion Voirie 10 jours avant le "
                                              "début du chantier, par vous ou par l’entreprise. 04 42 91 99 92 ("
                                              + L("démarche", _VOIRIE) + ")."),
           ("Demandez les aides avant de signer", "Conseil gratuit à la Maison Énergie Habitat Climat, sur rendez-vous. Pour le fonds "
                                                  "Barnier, attendez l’accusé de réception du dossier avant de commencer.")],
    aides_intro="Les aides se demandent avant de commencer les travaux, et le conseil public est gratuit.",
    aides=[("Maison Énergie Habitat Climat", "L’Espace Conseil France Rénov’ du CPIE du Pays d’Aix : conseil gratuit, accueil sur "
                                            "rendez-vous. Parc d’Ariane, bâtiment B, 11 avenue de la Grande Thumine, 13090 "
                                            "Aix-en-Provence. 04 42 93 03 69. " + L("cpie-paysdaix.com", _CPIE) + ". Le numéro de la "
                                            "Métropole, Allo Métropole Rénov’, répond aussi : 04 88 60 21 06 (" + L("ADIL 13", _ALLO)
                                            + ")."),
           ("Provence Éco-Rénov", "Le Département aide les propriétaires occupants de leur résidence principale à isoler le bâti : "
                                  "jusqu’à 25 % du coût TTC, dans la limite de 4 000 €. L’aide se cumule avec la prime Air-Bois, 50 % "
                                  "du coût et 1 000 € au plus, ou avec la prime chaudière fioul (" + L("Département", _CD13)
                                  + ", 2025, " + L("dispositifs", _CD13_HAB) + "). Demande en ligne sur le site du Département."),
           ("Fonds Barnier et feu de forêt", "Les travaux rendus obligatoires par le plan incendie de forêt sur une habitation peuvent "
                                             "être subventionnés à 80 %, jusqu’à 36 000 € par bien. Le dossier va à la DDTM des "
                                             "Bouches-du-Rhône, 16 rue Antoine-Zattara, 13332 Marseille. Les travaux ne commencent "
                                             "qu’après l’accusé de réception (" + L("règlement du PPRIF", _PPRIF) + ")."),
           NATIONAL],
    faq=[("Faut-il une autorisation pour changer ses fenêtres à Aix-en-Provence ?",
          "Oui, une déclaration préalable dès que l’aspect change. Dans le secteur sauvegardé, le PVC et les coffres de volets roulants "
          "apparents sont proscrits, et les fenêtres du XVIIIe siècle à petits carreaux se restaurent sans double vitrage."),
         ("Quelles tuiles pour refaire un toit dans le centre d’Aix-en-Provence ?",
          "Des tuiles creuses, posées à l’identique avec la même pente. Les tuiles neuves vieillies artificiellement sont exclues, les "
          "terrasses tropéziennes interdites, et seules 2 ou 3 tabatières de 0,25 m² par versant sont admises."),
         ("Quelles règles pour un ravalement dans le centre d’Aix-en-Provence ?",
          "La façade se refait en pierre de taille ou en enduit à la chaux naturelle, fini par un badigeon de chaux teinté de pigments "
          "de terre naturels. Le ciment, les enduits à résine et les crépis tyroliens sont interdits. Comptez 2 mois d’instruction pour "
          "la déclaration préalable."),
         ("Ma maison est-elle concernée par le plan incendie de forêt d’Aix-en-Provence ?",
          "Oui, si elle est en zone rouge ou bleue du plan approuvé le 10 juillet 2026 : auto-diagnostic, puis travaux de protection "
          "d’ici le 10 juillet 2031, dans la limite de 10 % de la valeur du bien. Le fonds Barnier peut en financer 80 %, jusqu’à 36 000 €."),
         ("Aix-en-Provence est-elle exposée au retrait-gonflement des argiles ?",
          "Oui. Un plan de prévention couvre la commune depuis le 27 juin 2012, et 14 épisodes de sécheresse y ont été reconnus en "
          "catastrophe naturelle de 1989 à 2023. En zone B2, rejetez les eaux de pluie à 5 m au moins de la maison."),
         ("Quelles aides pour isoler sa maison à Aix-en-Provence ?",
          "Provence Éco-Rénov du Département, jusqu’à 25 % du coût TTC et 4 000 € au plus, puis les aides nationales. Conseil gratuit "
          "à la Maison Énergie Habitat Climat : 04 42 93 03 69.")],
)

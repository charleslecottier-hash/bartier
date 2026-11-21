from villes_data import L, S, SP, NATIONAL  # liens dans le texte, sources discrètes, Service-Public, aides nationales

# Sources consultées le 21/11/2026. tours-metropole.fr renvoie une page anti-robot (JavaScript) : rien n'en est repris directement.
_INSEE = "https://api.insee.fr/melodi/data/DS_RP_LOGEMENT_PRINC?GEO=COM-37261"  # dossier complet, RP 2023 (page insee.fr en erreur 500 ce jour)
_URBA = "https://www.tours.fr/page-portail-ma-mairie/services-pratiques/habitat-urbanisme/"
_DP = "https://www.tours.fr/page-portail-ma-mairie/services-pratiques/habitat-urbanisme/urbanisme/"
_GNAU = "https://gnau.tours-metropole.fr/gnau/#/"
_PSMV = "https://www.tours.fr/app/uploads/2023/07/05-PSMV-REGLEMENT-06-fevrier-2014-Modifie-28-avril-2016.pdf"
_SPR = "https://pop.culture.gouv.fr/notice/merimee/SPR2400028"
_GPU = "https://www.geoportail-urbanisme.gouv.fr/api/document/59baa40ddd9cc0bf789dde128d37aaa9/files/37261_procedure_20260408.pdf"
_PLU = "https://www.geoportail-urbanisme.gouv.fr/api/document/59baa40ddd9cc0bf789dde128d37aaa9/files/37261_reglement_20260119.pdf"
_TERM = ("https://www.indre-et-loire.gouv.fr/actions-de-letat/amenagement-du-territoire-construction-logement/batiment/termites-merules/"
         "lutte-contre-les-termites-et-autres-insectes-xylophages")
_TERM_AP = ("https://www.indre-et-loire.gouv.fr/sites/default/files/contenu/telechargement/32909/210650/file/"
            "Termites_arr%C3%AAt%C3%A9%20pr%C3%A9fectoral_17%20Dec%202021-1.pdf")
_MERULE = ("https://www.indre-et-loire.gouv.fr/actions-de-letat/amenagement-du-territoire-construction-logement/batiment/termites-merules/"
           "lutte-contre-les-merules-et-autres-champignons-lignivores")
_MF = "https://donneespubliques.meteofrance.fr/FichesClim/FICHECLIM_37179001.pdf"  # station Tours (37179001), normales 1991-2020
_PPRI = ("https://www.indre-et-loire.gouv.fr/actions-de-letat/risques-naturels-et-technologiques/plans-de-prevention-des-risques-inondations-ppri/"
         "ppri-val-de-tours-val-de-luynes-loire")
_PPRI_NOTE = "https://www.indre-et-loire.gouv.fr/sites/default/files/contenu/telechargement/16305/117424/file/Note%20de%20pr%C3%A9sentation.pdf"
_UDAP = "https://lannuaire.service-public.gouv.fr/centre-val-de-loire/indre-et-loire/8c10971d-d9a2-4c58-a6b4-06d51fffeec5"
_ODP = "https://formulaires.services.tours.fr/demande-doccupation-du-domaine-public-pour-des-travaux-prives/"
_FR = "https://france-renov.gouv.fr/preparer-projet/trouver-conseiller"  # annuaire officiel : ARTEMIS pour Tours (Insee 37261)
_ADIL = "https://www.anil.org/adil-37/france-renov/"
_VACANT = "https://www.tours.fr/page-portail-tours-solidaire/tours-solidaire/remettre-mon-logement-vacant-sur-le-marche/"

CITY = dict(
    slug="tours", name="Tours", cp="37000", insee="37261",
    lat=47.3928, lon=0.6883, dept="Indre-et-Loire", depcode="37", region="Centre-Val de Loire",
    wiki="https://fr.wikipedia.org/wiki/Tours", wikidata="Q288",
    verified="2026-11-21",
    tldr="À Tours, le centre est un secteur sauvegardé de 150 hectares où le plan de sauvegarde fixe l’ardoise, le tuffeau apparent et les fenêtres "
         "en bois, et deux îlots de la ville sont classés à risque de mérule depuis décembre 2025, une première en Indre-et-Loire",
    hook="Secteur sauvegardé de 150 hectares, tuffeau et ardoise, termites et mérule.",
    title="Devis travaux à Tours : toiture, façade, fenêtres, isolation",
    desc="Travaux à Tours : secteur sauvegardé, tuffeau et ardoise, termites et mérule, val inondable entre Loire et Cher. Un seul artisan vient chiffrer.",
    figures_intro="Ce qui compte avant de lancer des travaux à Tours, entre Loire et Cher.",
    figures=[("80,9 <small>%</small>", "des logements sont des appartements", S("Insee, 2023", _INSEE)),
             ("45,2 <small>%</small>", "des résidences principales datent d’avant 1971", S("Insee, 2023", _INSEE)),
             ("150 <small>ha</small>", "de secteur sauvegardé en centre-ville, depuis son extension de 2008", S("Ville de Tours", _URBA)),
             ("36,3 <small>jours</small>", "de gel par an à la station Météo-France de Tours", S("Météo-France, normales 1991-2020", _MF))],
    answer=("À Tours, 80,9 % des logements sont des appartements et 45,2 % des résidences principales datent d’avant 1971. Dans le secteur sauvegardé "
            "du centre, 150 hectares, le plan de sauvegarde fixe les matériaux : ardoise naturelle, tuffeau laissé apparent, fenêtres en bois. Une partie "
            "de la ville est en zone termites, et deux îlots sont classés à risque de mérule depuis le 2 décembre 2025."),
    facts=[("Secteur sauvegardé", "Créé le 9 novembre 1973 (" + L("ministère de la Culture", _SPR) + "), il couvre 150 hectares depuis 2008, avec les boulevards "
                                  "Heurteloup et Béranger, les Halles et le quartier Lamartine. Son plan de sauvegarde, approuvé le 6 février 2014 et modifié "
                                  "le 28 avril 2016, règle chaque façade et chaque toiture (" + L("Ville de Tours", _URBA) + ")."),
           ("Ravalement", "Dans toute la commune, un ravalement de façade est soumis à autorisation, par délibération municipale du 7 juillet 2014. "
                          "Clôtures et démolitions le sont aussi (" + L("PLU de Tours", _PLU) + ")."),
           ("Urbanisme", "Hors secteur sauvegardé, le PLU de Tours s’applique depuis le 20 janvier 2020. Il a été modifié six fois, la dernière le 29 septembre 2025, puis mis en compatibilité le 19 janvier 2026 ("
                         + L("Géoportail de l’urbanisme", _GPU) + "). Le futur PLU métropolitain vise une entrée en vigueur fin 2027 (" + L("Ville de Tours", _URBA) + ")."),
           ("Termites", "Tours fait partie des 51 communes d’Indre-et-Loire où des zones contaminées par les termites sont délimitées à la parcelle, par "
                        "l’arrêté du 17 décembre 2021 modifié le 3 mars 2025 (" + L("préfecture", _TERM) + ")."),
           ("Mérule", "Premier arrêté mérule du département, signé le 2 décembre 2025 : deux îlots des quartiers Rabelais-Tonnelé et Beaujardin sont classés "
                      "zones de présence d’un risque de mérule. Un immeuble infesté se déclare en mairie (" + L("préfecture", _MERULE) + ")."),
           ("Inondation", "Le val de Tours, entre Loire et Cher, est entièrement endigué et comptait plus de 118 000 habitants en 2016 (" + L("note de présentation", _PPRI_NOTE)
                          + "). Son plan de prévention du risque d’inondation, révisé le 18 juillet 2016, s’applique à Tours et à 17 autres communes ("
                          + L("préfecture", _PPRI) + ").")],
    trades_intro="Tuffeau, ardoise, pans de bois, immeubles de la Reconstruction : dans le secteur sauvegardé, chaque type d’immeuble a ses règles.",
    trades={
        "toiture": ["Sur les immeubles à conserver du secteur sauvegardé, seuls sont admis l’ardoise naturelle de petit format posée à pureau droit, la petite "
                    "tuile plate de pays là où elle existe encore, et le zinc, le cuivre ou le plomb pour les pentes trop faibles. Les châssis de toit ne "
                    "dépassent pas 0,80 × 1,00 m et sont interdits sur les brisis des toits à la Mansart (" + L("plan de sauvegarde", _PSMV) + ").",
                    "Dans les quartiers de lotissements, le PLU interdit la tôle ondulée, le bac acier, le fibrociment et l’ardoise posée en losange. "
                    "La station de Tours compte 37,4 jours de rafales d’au moins 58 km/h par an, surtout de décembre à avril : faites revoir ardoises "
                    "et faîtages avant l’hiver (" + L("Météo-France", _MF) + ")."],
        "facade": ["Dans le secteur sauvegardé, le tuffeau appareillé reste apparent. Le plan de sauvegarde impose un nettoyage à l’eau à basse ou moyenne pression, proscrit le sablage "
                   "et tout hydrofuge, et reprend les joints au mortier de chaux. Les enduits se font à la chaux, avec du sable de Loire ou du Loir ("
                   + L("plan de sauvegarde", _PSMV) + ").",
                   "Dans les quartiers d’habitat, le PLU demande qu’un ravalement améliore si nécessaire la performance énergétique : label BBC Rénovation "
                   "ou moins de 80 kWh/m² par an après travaux. Le bâti ancien, maisons en pierre de taille ou des années 30, en est dispensé, et "
                   "l’isolation par l’intérieur y est privilégiée (" + L("PLU de Tours", _PLU) + ")."],
        "fenetres": ["Dans le secteur sauvegardé, les fenêtres nouvelles sont en bois, ou en métal si l’immeuble s’y prête. Elles se posent dans les feuillures "
                     "de la maçonnerie : la pose dite « rénovation » est interdite. Les menuiseries sont peintes dans une teinte plus soutenue que la "
                     "maçonnerie (" + L("plan de sauvegarde", _PSMV) + ").",
                     "Les persiennes de bois dites « à la tourangelle » sont maintenues quand elles correspondent à l’immeuble. Pour isoler une fenêtre "
                     "ancienne, le plan de sauvegarde préconise un double vitrage mince ou une seconde fenêtre côté intérieur. Ailleurs, le PLU demande "
                     "des caissons de volets roulants posés à l’intérieur, sauf impossibilité technique."],
        "charpente": ["Une partie de Tours est en zone termites, avec des plans à la parcelle. L’arrêté préfectoral de 2021 vise aussi Saint-Pierre-des-Corps, "
                      "Joué-lès-Tours, La Riche, Saint-Avertin et Saint-Cyr-sur-Loire (" + L("arrêté termites", _TERM_AP) + ").",
                      "À Rabelais-Tonnelé et à Beaujardin, deux îlots sont classés à risque de mérule depuis décembre 2025 : faites contrôler planchers et "
                      "charpentes humides ou mal aérés. Dans le secteur sauvegardé, les pièces de charpente anciennes sont conservées, restaurées ou "
                      "reconstituées (" + L("plan de sauvegarde", _PSMV) + ")."],
        "isolation": ["Dans le secteur sauvegardé, l’isolation par l’extérieur n’est admise que sur des façades sans décor ni intérêt patrimonial (parpaing, "
                      "béton, enduit ciment), qui ne donnent pas sur l’espace public et n’en sont pas visibles (" + L("plan de sauvegarde", _PSMV) + "). "
                      "Pour les autres, on isole par l’intérieur ou par les combles.",
                      "Dans les zones d’habitat, le PLU demande qu’une réfection de toiture améliore nettement la performance énergétique, avec des matériaux "
                      "à forte inertie, bio ou géosourcés, contre les surchauffes. La station de Tours compte 14,3 jours à plus de 30 °C par an ("
                      + L("Météo-France", _MF) + ")."]},
    steps_intro="Dans l’ordre, du secteur sauvegardé aux autres quartiers.",
    steps=[("Repérez les règles de votre adresse", "Secteur sauvegardé, abords d’un monument historique ou zone inondable : l’architecte des Bâtiments de France reçoit "
                                                 "sur rendez-vous, 36 rue de Clocheville. 02 47 31 03 03 (" + L("UDAP d’Indre-et-Loire", _UDAP) + ")."),
           ("Déposez la demande d’autorisation", "En ligne sur le " + L("guichet numérique de la Métropole", _GNAU) + ", ou au service urbanisme, 1 à 3 rue des Minimes, "
                                                "du lundi au jeudi de 8 h 30 à 12 h 30 et de 13 h 30 à 17 h. 02 47 21 67 23 (" + L("Ville de Tours", _DP) + ")."),
           ("Faites autoriser l’échafaudage", "Demande en ligne au moins 15 jours calendaires avant le chantier, 20 jours si un arbre est à moins de 2 m. Redevance "
                                              "de 1 € le m² par semaine, 35 € au minimum. 02 47 21 66 80 (" + L("démarche", _ODP) + ")."),
           ("Signalez la mérule", "Un immeuble infesté se déclare en mairie. Dans les deux îlots classés, la vente d’un immeuble entraîne des obligations particulières (" + L("préfecture", _MERULE) + ")."),
           ("Prenez rendez-vous chez ARTEMIS", "Le conseiller de la Métropole vous informe et vous oriente sur les travaux et les aides, gratuitement.")],
    aides_intro="Dans la Métropole, un seul guichet public conseille les propriétaires, sans frais.",
    aides=[("ARTEMIS, Tours Métropole", "L’Espace Conseil France Rénov’ de Tours Métropole Val de Loire : 60 avenue Marcel Dassault, 37200 Tours. 02 47 33 18 88, "
                                       "artemis@tours-metropole.fr. Du lundi au vendredi, uniquement sur rendez-vous (" + L("annuaire France Rénov’", _FR)
                                       + "). L’ADIL 37 renvoie vers ARTEMIS pour les logements de la Métropole (" + L("ADIL 37", _ADIL) + ")."),
           ("Sortie de vacance", "La Métropole verse une aide de 3 000 € à la sortie de vacance d’un logement, indique la Ville. Contact logement vacant : "
                                 "02 47 21 68 22, logementvacant@ville-tours.fr (" + L("Ville de Tours", _VACANT) + ")."),
           NATIONAL],
    faq=[("Faut-il une autorisation pour un ravalement à Tours ?",
          "Oui. Tout ravalement est soumis à autorisation dans toute la commune (délibération du 7 juillet 2014). Dans les quartiers d’habitat, le PLU demande "
          "en plus, si nécessaire, un gain énergétique : label BBC Rénovation ou moins de 80 kWh/m² par an, sauf pour le bâti ancien."),
         ("Quels matériaux de toiture dans le centre de Tours ?",
          "Sur les immeubles à conserver du secteur sauvegardé : ardoise naturelle de petit format posée à pureau droit, petite tuile plate de pays là où "
          "elle existe, zinc, cuivre ou plomb pour les faibles pentes. Les châssis de toit sont limités à 0,80 × 1,00 m."),
         ("Peut-on poser des fenêtres en PVC dans le secteur sauvegardé de Tours ?",
          "Non : le plan de sauvegarde veut des fenêtres nouvelles en bois, ou en métal si l’immeuble s’y prête, posées dans les feuillures de la maçonnerie. "
          "La pose dite « rénovation » y est interdite."),
         ("Tours est-elle en zone termites ou mérule ?",
          "Oui, en partie. Des zones contaminées par les termites sont délimitées à la parcelle (arrêté du 17 décembre 2021 modifié le 3 mars 2025). "
          "Deux îlots, à Rabelais-Tonnelé et à Beaujardin, sont classés à risque de mérule depuis le 2 décembre 2025."),
         ("Quelles aides pour rénover son logement à Tours ?",
          "ARTEMIS, le service gratuit de la Métropole, fait le point sur votre projet et les aides : 02 47 33 18 88. La Métropole aide aussi la sortie de "
          "vacance d’un logement, à hauteur de 3 000 €. Les aides nationales, dont MaPrimeRénov’, s’y ajoutent."),
         ("Comment faire autoriser un échafaudage à Tours ?",
          "Par la " + L("demande en ligne", _ODP) + " d’occupation du domaine public, au moins 15 jours calendaires avant le chantier, 20 jours si un arbre "
          "est à moins de 2 m. La redevance est de 1 € le m² par semaine, 35 € au minimum.")],
)

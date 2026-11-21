from villes_data import L, S, SP, NATIONAL  # liens dans le texte, sources discrètes, Service-Public, aides nationales

REVIEWED = "2026-11-21"

# Sources consultées le 21/11/2026.
_INSEE = "https://www.insee.fr/fr/statistiques/2011101?geo=COM-76351"
_SPR = "https://lehavre.fr/sites/default/files/fichier/plan-graphique-et-reglement-ecrit-avap-spr.pdf"
_UNESCO = "https://lehavre.fr/services-au-quotidien/habitat-urbanisme/travaux-en-secteur-protege-patrimoine-unesco"
_DP = "https://lehavre.fr/services-au-quotidien/habitat-urbanisme/autorisations-durbanisme/declaration-prealable"
_RAV = "https://lehavre.fr/services-au-quotidien/habitat-urbanisme/campagnes-de-ravalement-de-facade"
_RAVB = "https://lehavre.fr/sites/default/files/fichier/campagne_de_ravalement_des_facades_en_briques-thiers_coty_flaubert_2023.pdf"
_TIA = "https://lehavre.fr/actualites/toutes-les-actualites/beneficiez-daides-pour-vos-travaux-dinteret-architectural"
_HAB = "https://lehavre.fr/services-au-quotidien/habitat-urbanisme"
_PLUI = ("https://documents.lehavreseinemetropole.fr/elaboration-plui/Lettres%20d'information/"
         "Lettre%20d%E2%80%99information%20n%C2%B05%20sur%20le%20PLUi%20(avril%202026).pdf")
_DICRIM = "https://www.georisques.gouv.fr/DICRIM/76351"
_MF = "https://donneespubliques.meteofrance.fr/FichesClim/FICHECLIM_76552001.pdf"
_TERM = "https://www.seine-maritime.gouv.fr/contenu/telechargement/57813/406431/file/Arr%C3%AAt%C3%A9%20termites%20SM%20sign%C3%A9%2012062023.pdf"
_DEVIS = "https://www.lehavreseinemetropole.fr/sites/default/files/media/downloads/Mode%CC%80le%20de%20devis_Toiture%20terrasse%202025.pdf"
_ECFR = "https://lannuaire.service-public.gouv.fr/normandie/seine-maritime/e2de16df-1107-46c3-a3be-92a0a13c1387"
_ECR = "https://www.lehavreseinemetropole.fr/espace-conseil-renovation"
_CEE = "https://cheque-eco-energie.normandie.fr/"
_VOIRIE = ("https://plui.lehavreseinemetropole.fr//5.%20Annexes/5.2.%20Annexes%20informatives/5.2.7.%20R%C3%A8glements%20guides/"
           "R%C3%A8glement%20de%20voirie.pdf")

CITY = dict(
    slug="le-havre", name="Le Havre", a="au Havre", cp="76600", insee="76351",
    lat=49.4942, lon=0.1081, dept="Seine-Maritime", depcode="76", region="Normandie",
    wiki="https://fr.wikipedia.org/wiki/Le_Havre", wikidata="Q42810",
    verified="2026-11-21",
    tldr="Au Havre, le centre reconstruit par Auguste Perret a ses règles immeuble par immeuble : béton restauré à l’identique, "
         "ni PVC ni isolation par l’extérieur sur les bâtiments les plus protégés",
    hook="Centre Perret inscrit à l’Unesco, béton restauré à l’identique.",
    title="Devis travaux au Havre : toiture, façade, fenêtres, isolation",
    desc="Travaux au Havre : centre Perret protégé, toits-terrasses, vent de mer, aide au ravalement des façades en brique. Un seul artisan vient chiffrer.",
    figures_intro="Ce qui compte avant de lancer des travaux dans la ville reconstruite.",
    figures=[("73,2 <small>%</small>", "des logements sont des appartements", S("Insee, 2023", _INSEE)),
             ("42,4 <small>%</small>", "des résidences principales datent de 1946 à 1970", S("Insee, 2023", _INSEE)),
             ("2005", "inscription du centre reconstruit au patrimoine mondial de l’Unesco", S("Ville du Havre", _UNESCO)),
             ("180 <small>km/h</small>", "record de rafale au cap de la Hève, le 16 octobre 1987", S("Météo-France", _MF))],
    answer=("Près de trois logements sur quatre sont des appartements (73,2 %), et 42,4 % des résidences principales datent de 1946 à 1970. "
            "Dans le centre reconstruit par Auguste Perret, inscrit à l’Unesco en 2005, tout changement d’aspect demande une autorisation et l’avis "
            "de l’architecte des Bâtiments de France. L’isolation par l’extérieur y est proscrite sur les immeubles de catégories 1 et 2."),
    facts=[("Centre reconstruit", "Inscrit au patrimoine mondial depuis 2005, il forme un site patrimonial remarquable régi par une AVAP approuvée le "
                                  "11 juillet 2016 et modifiée le 18 décembre 2025. Tous les travaux qui changent l’aspect d’un immeuble y sont soumis à "
                                  "autorisation, avec l’avis de l’architecte des Bâtiments de France (" + L("règlement du SPR", _SPR) + ")."),
           ("Urbanisme", "Le PLUi Le Havre Seine Métropole, commun aux 54 communes, a été approuvé le 12 février 2026. Il s’applique depuis le "
                         "1er avril 2026 (" + L("Communauté urbaine", _PLUI) + ")."),
           ("Déclaration préalable", "La Ville la demande pour un ravalement et pour tout travail qui change l’aspect extérieur, comme un remplacement de "
                                     "menuiserie ou une réfection de toiture. Instruction : un mois, davantage si l’architecte des Bâtiments de France "
                                     "est consulté (" + L("Ville du Havre", _DP) + ")."),
           ("Mer et inondation", "Un plan de prévention des risques littoraux, approuvé le 1er juillet 2022, encadre les zones exposées à la submersion "
                                 "marine. Celui des inondations de la Lézarde date du 6 mai 2013 (" + L("DICRIM, 2025", _DICRIM) + ")."),
           ("Falaises et cavités", "Sur la costière, la falaise entre ville basse et ville haute, les propriétaires doivent réaliser des ouvrages de "
                                   "protection, par exemple un mur de soutènement. Le sous-sol garde d’anciennes marnières et des abris de la Seconde "
                                   "Guerre mondiale, parfois avec un périmètre de précaution (" + L("DICRIM, 2025", _DICRIM) + "). Un certificat "
                                   "sur les cavités souterraines se demande en ligne (" + L("Ville du Havre", _HAB) + ")."),
           ("Vent", "Au cap de la Hève, la rafale record atteint 180 km/h, le 16 octobre 1987, et 172,8 km/h le 25 janvier 1990 ("
                    + L("Météo-France", _MF) + "). Les tempêtes arrivent surtout en automne et en hiver (" + L("DICRIM, 2025", _DICRIM) + ").")],
    trades_intro="Béton de la Reconstruction, brique d’avant-guerre, toits-terrasses et ardoise : au Havre, les règles changent d’un immeuble à l’autre, "
                 "surtout dans le centre reconstruit.",
    trades={
        "toiture": ["Le règlement du centre reconstruit voit dans ses toits la « cinquième façade » de la ville, visible des étages et des coteaux. "
                    "Sur un toit-terrasse non accessible, l’étanchéité ne reste pas brute : toit végétalisé de préférence, sinon gravillons clairs. "
                    "Sur un toit en pente, le bac acier et les matériaux précaires sont interdits, et l’ardoise employée est naturelle, au format "
                    "22 × 32 cm. Sur l’île Saint-François, seule l’ardoise naturelle couvre les logements (" + L("règlement du SPR", _SPR) + ").",
                    "Au cap de la Hève, les normales comptent 789,8 mm de pluie et 127,7 jours avec au moins 1 mm par an (" + L("Météo-France", _MF)
                    + ", 1991-2020). La Ville cite l’arrachage de toitures parmi les dangers des tempêtes (" + L("DICRIM, 2025", _DICRIM) + "). "
                    "Faites vérifier relevés d’étanchéité, couvertines et fixations avant l’hiver."],
        "facade": ["Dans le centre reconstruit, un ravalement porte toujours sur un bâtiment entier, et sur tout l’îlot quand ses immeubles viennent "
                   "d’un même projet. Le béton retrouve son aspect d’origine : sablage interdit, aciers oxydés mis à nu, passivés puis enrobés de mortier. "
                   "En catégories 1 et 2, les motifs décoratifs supprimés ou abîmés sont restitués (" + L("règlement du SPR", _SPR) + ").",
                   "À Thiers-Coty-Flaubert, Sainte-Marie et Saint-Léon, la Ville aide le ravalement des façades en brique jusqu’au 31 décembre 2026 : "
                   "30 % des travaux hors taxes, plafonnés à 6 000 € par 100 m² de façade, y compris pour retrouver la brique sous un enduit. "
                   "Les travaux attendent son accord (" + L("Ville du Havre", _RAV) + ")."],
        "fenetres": ["Dans le centre reconstruit, une fenêtre neuve garde les dimensions, la position dans la baie et la couleur de l’ancienne. En catégorie 1, "
                     "tout se remplace à l’identique, et le PVC est proscrit en catégories 1 et 2. Dans les autres cas, la section des profils et la surface vitrée "
                     "peuvent varier de 15 % au plus. La pose en rénovation, qui garde l’ancien dormant, est proscrite pour tous les immeubles de la "
                     "Reconstruction (" + L("règlement du SPR", _SPR) + ").",
                     "Le règlement recommande le bois, matériau des menuiseries de la Reconstruction. En catégories 1 et 2, persiennes et volets en PVC "
                     "sont interdits ; à défaut des couleurs d’origine, ils se peignent en gris RAL 7037 (" + L("règlement du SPR", _SPR) + "). Jusqu’au "
                     "31 décembre 2026, la Ville aide à restaurer menuiseries et persiennes d’origine, ou à les remplacer à l’identique : 30 % ou "
                     "20 % des travaux hors taxes, selon le cas (" + L("Ville du Havre", _TIA) + ")."],
        "charpente": ["Le Havre n’est pas classé en zone termites : l’arrêté préfectoral du 12 juin 2023 ne vise que trois communes de l’agglomération "
                      "de Rouen (" + L("préfecture", _TERM) + "). Dans le centre reconstruit, les immeubles des XVIIIe et XIXe siècles sont couverts de toits "
                      "à deux pentes, de 30° à 60°, ou à combles brisés (" + L("règlement du SPR", _SPR) + ").",
                      "Pour ces immeubles d’avant la Reconstruction, le règlement fait conserver les volumes de toiture et les couvertures en ardoise "
                      "naturelle, zinc ou tuile petit format ; les matériaux synthétiques sont interdits. L’isolation par-dessus les chevrons (sarking) "
                      "est interdite en catégorie 5, autorisée au cas par cas en catégorie 6 (" + L("règlement du SPR", _SPR) + ")."],
        "isolation": ["Dans le centre reconstruit, l’isolation par l’extérieur est proscrite en catégories 1 et 2, car elle cacherait structure, "
                      "remplissages et décors. En catégories 3 et 4, elle reste possible sous conditions, dans un projet d’ensemble, au-dessus du "
                      "soubassement et sans bardage PVC. Sinon, le règlement cite l’isolation par l’intérieur et le remplissage de la lame d’air ("
                      + L("règlement du SPR", _SPR) + ").",
                      "Isoler un toit-terrasse est encouragé, mais oblige souvent à rehausser l’acrotère (" + L("règlement du SPR", _SPR) + "). Pour "
                      "obtenir les aides, le modèle de devis de la Communauté urbaine demande une résistance thermique d’au moins R = 4,5 m².K/W, "
                      "ou 6,5 pour une rénovation d’ampleur, et conseille de viser 8 (" + L("modèle de devis, 2025", _DEVIS) + ")."]},
    steps_intro="Dans l’ordre, du centre reconstruit aux quartiers de brique.",
    steps=[("Trouvez la catégorie de votre immeuble", "Dans le centre reconstruit, le plan du site patrimonial remarquable donne la catégorie de chaque "
                                                     "bâtiment, et donc ses règles (" + L("règlement du SPR", _SPR) + "). Service urbanisme de la Ville : "
                                                     "02 79 92 76 90, urbanisme@lehavre.fr (" + L("Ville du Havre", _UNESCO) + ")."),
           ("Façade en brique : contactez la Ville", "À Thiers-Coty-Flaubert, Sainte-Marie et Saint-Léon, le service Urbanisme et prospective fixe les "
                                                    "prescriptions avant les devis. 02 35 22 27 96 (" + L("campagne de ravalement, 2023", _RAVB) + ")."),
           ("Déposez la déclaration préalable", "En ligne sur le portail Mes démarches (netsve.lehavre.fr), ou au service Droit des sols et permis de "
                                                "construire, rez-de-chaussée « Forum » de l’Hôtel de Ville, 1517 place de l’Hôtel de Ville. 02 35 19 45 47 ("
                                                + L("Ville du Havre", _DP) + ")."),
           ("Faites autoriser l’échafaudage", "Toute occupation du trottoir demande une autorisation et une redevance d’occupation du domaine public. "
                                              "Pour un chantier, le permis de stationnement se demande en principe au maire (" + L("règlement de voirie, 2024", _VOIRIE)
                                              + "). Pour un ravalement aidé, la Ville indique que l’entreprise fait en général la déclaration de voirie ("
                                              + L("campagne de ravalement, 2023", _RAVB) + ")."),
           ("Demandez conseil avant de signer", "L’Espace Conseil France Rénov’ de la Communauté urbaine vous conseille gratuitement sur le projet et les aides possibles.")],
    aides_intro="Au Havre, les aides de la Ville se demandent avant tout début de chantier.",
    aides=[("Espace Conseil France Rénov’ du Havre", "Le service public de conseil de la Communauté urbaine Le Havre Seine Métropole, labellisé Mon "
                                                    "Accompagnateur Rénov’ : 19 rue Georges-Braque, 76600 Le Havre. 02 35 22 25 20, du lundi au vendredi "
                                                    "de 9 h à 17 h (" + L("annuaire Service-Public", _ECFR) + ", " + L("Communauté urbaine", _ECR) + ")."),
           ("Campagnes de ravalement des façades en brique", "Jusqu’au 31 décembre 2026, à Thiers-Coty-Flaubert, Sainte-Marie et Saint-Léon : 30 % des "
                                                           "travaux hors taxes, plafonnés à 6 000 € par 100 m² de façade, et 20 %, plafonnés à 3 500 €, "
                                                           "pour corniches, bandeaux, linteaux, garde-corps ou volets. La façade doit donner sur la rue ("
                                                           + L("Ville du Havre", _RAV) + ")."),
           ("Travaux d’intérêt architectural du centre reconstruit", "Jusqu’au 31 décembre 2026, pour les immeubles d’intérêt de la Reconstruction : "
                                                                    "restauration de portes, menuiseries, garde-corps, persiennes ou claustras d’origine, "
                                                                    "ou remplacement à l’identique. Parties privatives : 30 % hors taxes plafonnés à 5 000 € "
                                                                    "par propriétaire et par an pour une restauration, 20 % plafonnés à 2 500 € pour un "
                                                                    "remplacement. Parties communes : plafonds de 10 000 € et 7 500 € par copropriété et "
                                                                    "par an. Travaux visibles depuis la rue, autorisés, et commencés après l’accord de la Ville ("
                                                                    + L("Ville du Havre, 2026", _TIA) + ")."),
           ("Chèque éco-énergie Normandie", "Pour une maison de plus de 15 ans, résidence principale, secondaire ou locative : 600 € pour l’audit "
                                            "énergétique, puis de 6 500 à 12 000 € pour les travaux (" + L("Région Normandie", _CEE) + ")."),
           NATIONAL],
    faq=[("Y a-t-il une aide au ravalement au Havre ?",
          "Oui, pour les façades en brique de Thiers-Coty-Flaubert, Sainte-Marie et Saint-Léon, jusqu’au 31 décembre 2026 : 30 % des travaux hors taxes, "
          "plafonnés à 6 000 € par 100 m² de façade. Les travaux ne commencent qu’après l’accord de la Ville. Partout, un ravalement demande une "
          "déclaration préalable."),
         ("Faut-il une autorisation pour changer ses fenêtres au Havre ?",
          "Oui, la Ville soumet le remplacement de menuiseries à déclaration préalable. Dans le centre reconstruit, la fenêtre neuve garde dimensions, "
          "position et couleur ; la pose en rénovation est proscrite pour les immeubles de la Reconstruction, et le PVC l’est en catégories 1 et 2."),
         ("Peut-on isoler sa façade par l’extérieur dans le centre reconstruit ?",
          "Pas en catégories 1 et 2. En catégories 3 et 4, c’est possible sous conditions, dans un projet d’ensemble, au-dessus du soubassement "
          "et sans bardage PVC. Sinon, le règlement oriente vers l’isolation par l’intérieur ou le remplissage de la lame d’air."),
         ("Le Havre est-il en zone termites ?",
          "Non. L’arrêté préfectoral du 12 juin 2023 ne classe que trois communes de l’agglomération de Rouen en Seine-Maritime."),
         ("Mon terrain est-il concerné par une cavité souterraine ?",
          "Peut-être : le sous-sol havrais compte d’anciennes marnières, cailloutières et abris de guerre. Un certificat sur les cavités souterraines "
          "se demande en ligne, depuis le site de la Ville. Protection civile urbaine : 02 35 19 60 11."),
         ("Quelles aides pour rénover son logement au Havre ?",
          "L’aide de la Ville au ravalement des façades en brique, celle aux travaux d’intérêt architectural du centre reconstruit, le chèque "
          "éco-énergie Normandie pour les maisons de plus de 15 ans (600 € pour l’audit, de 6 500 à 12 000 € pour les travaux) et les aides nationales. Conseil gratuit à l’Espace Conseil France Rénov’ : 02 35 22 25 20.")],
)

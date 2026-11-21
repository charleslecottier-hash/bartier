from villes_data import L, S, SP, NATIONAL  # liens dans le texte, sources discrètes, Service-Public, aides nationales

# Sources consultées le 21/11/2026.
_INSEE = "https://www.insee.fr/fr/statistiques/2011101?geo=COM-76351"
_SPR = "https://lehavre.fr/sites/default/files/fichier/plan-graphique-et-reglement-ecrit-avap-spr.pdf"
_UNESCO = "https://lehavre.fr/services-au-quotidien/habitat-urbanisme/travaux-en-secteur-protege-patrimoine-unesco"
_DP = "https://lehavre.fr/services-au-quotidien/habitat-urbanisme/autorisations-durbanisme/declaration-prealable"
_RAV = "https://lehavre.fr/services-au-quotidien/habitat-urbanisme/campagnes-de-ravalement-de-facade"
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
    slug="le-havre", name="Le Havre", cp="76600", insee="76351",
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
             ("42,4 <small>%</small>", "des résidences principales datent de 1946 à 1970, les années de la Reconstruction", S("Insee, 2023", _INSEE)),
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
                                   "Guerre mondiale, parfois avec un périmètre de précaution (" + L("DICRIM, 2025", _DICRIM) + "). La Ville "
                                   "délivre en ligne un renseignement sur les cavités (" + L("Ville du Havre", _HAB) + ")."),
           ("Vent", "Au cap de la Hève, la rafale record atteint 180 km/h, le 16 octobre 1987. Le 25 janvier 2020, le vent a soufflé à 172,8 km/h. "
                    "Les tempêtes arrivent surtout en automne et en hiver (" + L("Météo-France", _MF) + ", " + L("DICRIM", _DICRIM) + ").")],
    trades_intro="Béton de la Reconstruction, brique d’avant-guerre, toits-terrasses et ardoise : au Havre, les règles changent d’un immeuble à l’autre, "
                 "surtout dans le centre reconstruit.",
    trades={
        "toiture": ["Le règlement du centre reconstruit voit dans ses toits la « cinquième façade » de la ville, visible des étages et des coteaux. "
                    "Sur un toit-terrasse, l’étanchéité ne reste pas brute : toit végétalisé de préférence, sinon gravillons clairs. Sur un toit en pente, "
                    "le bac acier et les matériaux précaires sont interdits, et l’ardoise naturelle se pose au format 22 × 32 cm. Sur l’île Saint-François, "
                    "seule l’ardoise naturelle couvre les logements (" + L("règlement du SPR", _SPR) + ").",
                    "Au cap de la Hève, les normales comptent 789,8 mm de pluie et 127,7 jours avec au moins 1 mm par an (" + L("Météo-France", _MF)
                    + ", 1991-2020). La Ville cite l’arrachage de toitures parmi les dangers des tempêtes (" + L("DICRIM, 2025", _DICRIM) + "). "
                    "Faites vérifier relevés d’étanchéité, couvertines et fixations avant l’hiver."],
        "facade": ["Dans le centre reconstruit, un ravalement porte toujours sur un bâtiment entier, et sur tout l’îlot quand ses immeubles viennent "
                   "d’un même projet. Le béton retrouve son aspect d’origine : sablage interdit, aciers oxydés mis à nu, passivés puis enrobés de mortier. "
                   "Les immeubles de catégories 1 et 2 sont restitués dans leur état d’origine (" + L("règlement du SPR", _SPR) + ").",
                   "À Thiers-Coty-Flaubert, Sainte-Marie et Saint-Léon, la Ville aide le ravalement des façades en brique jusqu’au 31 décembre 2026 : "
                   "30 % des travaux hors taxes, plafonnés à 6 000 € par 100 m² de façade, y compris pour retrouver la brique sous un enduit. "
                   "Les travaux attendent son accord (" + L("Ville du Havre", _RAV) + ")."],
        "fenetres": ["Dans le centre reconstruit, une fenêtre neuve garde les dimensions, la position dans la baie et la couleur de l’ancienne. En catégorie 1, "
                     "tout se remplace à l’identique et le PVC est proscrit, comme en catégorie 2. Ailleurs, la section des profils et la surface vitrée "
                     "peuvent varier de 15 % au plus. La pose en rénovation, qui garde l’ancien dormant, est proscrite partout dans le site "
                     "(" + L("règlement du SPR", _SPR) + ").",
                     "Le règlement recommande le bois, matériau des menuiseries de la Reconstruction. En catégories 1 et 2, persiennes et volets en PVC "
                     "sont interdits ; à défaut des couleurs d’origine, ils se peignent en gris RAL 7037. Hors du centre reconstruit aussi, un remplacement "
                     "de menuiseries passe par une déclaration préalable (" + L("Ville du Havre", _DP) + ")."],
        "charpente": ["Le Havre n’est pas classé en zone termites : l’arrêté préfectoral du 12 juin 2023 ne vise que trois communes de l’agglomération "
                      "de Rouen (" + L("préfecture", _TERM) + "). Dans le centre reconstruit, les immeubles des XVIIIe et XIXe siècles gardent des toits "
                      "à deux pentes, de 30° à 60°, ou à combles brisés (" + L("règlement du SPR", _SPR) + ").",
                      "Pour ces immeubles d’avant la Reconstruction, le règlement fait conserver les volumes de toiture et les couvertures en ardoise "
                      "naturelle, zinc ou tuile petit format ; les matériaux synthétiques sont interdits. L’isolation par-dessus les chevrons (sarking) "
                      "est interdite en catégorie 5 et étudiée au cas par cas en catégorie 6."],
        "isolation": ["Dans le centre reconstruit, l’isolation par l’extérieur est proscrite en catégories 1 et 2, car elle cacherait structure, "
                      "remplissages et décors. En catégories 3 et 4, elle reste possible dans un projet d’ensemble, au-dessus du soubassement, sans "
                      "bardage PVC. Sinon, le règlement cite l’isolation par l’intérieur et le remplissage de la lame d’air (" + L("règlement du SPR", _SPR) + ").",
                      "Isoler un toit-terrasse est encouragé, mais oblige souvent à rehausser l’acrotère. Le modèle de devis de la Communauté urbaine "
                      "indique une résistance thermique d’au moins R = 4,5 m².K/W, ou 6,5 pour une rénovation d’ampleur, et conseille de viser 8 ("
                      + L("modèle de devis, 2025", _DEVIS) + ")."]},
    steps_intro="Dans l’ordre, du centre reconstruit aux quartiers de la ville haute.",
    steps=[("Trouvez la catégorie de votre immeuble", "Dans le centre reconstruit, le plan du site patrimonial remarquable donne la catégorie de chaque "
                                                     "bâtiment, et donc ses règles (" + L("règlement du SPR", _SPR) + "). Service urbanisme de la Ville : "
                                                     "02 79 92 76 90, urbanisme@lehavre.fr."),
           ("Façade en brique : contactez la Ville", "À Thiers-Coty-Flaubert, Sainte-Marie et Saint-Léon, le service Urbanisme et prospective fixe les "
                                                    "prescriptions avant les devis. 02 35 22 27 96 (" + L("campagnes de ravalement", _RAV) + ")."),
           ("Déposez la déclaration préalable", "En ligne sur le portail Mes démarches (netsve.lehavre.fr), ou au service Droit des sols et permis de "
                                                "construire, rez-de-chaussée « Forum » de l’Hôtel de Ville, 1517 place de l’Hôtel de Ville. 02 35 19 45 47 ("
                                                + L("Ville du Havre", _DP) + ")."),
           ("Faites autoriser l’échafaudage", "Un échafaudage sur le trottoir demande un permis de stationnement, délivré par le maire, et une redevance "
                                              "d’occupation du domaine public (" + L("règlement de voirie, 2024", _VOIRIE) + "). L’entreprise s’en charge en général."),
           ("Demandez conseil avant de signer", "L’Espace Conseil France Rénov’ de la Communauté urbaine vérifie gratuitement votre projet et les aides possibles.")],
    aides_intro="Au Havre, l’aide de la Ville au ravalement se demande avant tout début de chantier.",
    aides=[("Espace Conseil France Rénov’ du Havre", "Le service public de conseil de la Communauté urbaine Le Havre Seine Métropole, labellisé Mon "
                                                    "Accompagnateur Rénov’ : 19 rue Georges-Braque, 76600 Le Havre. 02 35 22 25 20, du lundi au vendredi "
                                                    "de 9 h à 17 h (" + L("annuaire Service-Public", _ECFR) + ", " + L("Communauté urbaine", _ECR) + ")."),
           ("Campagnes de ravalement des façades en brique", "Jusqu’au 31 décembre 2026, à Thiers-Coty-Flaubert, Sainte-Marie et Saint-Léon : 30 % des "
                                                           "travaux hors taxes, plafonnés à 6 000 € par 100 m² de façade, et 20 %, plafonnés à 3 500 €, "
                                                           "pour corniches, bandeaux, linteaux, garde-corps ou volets. La façade doit donner sur la rue ("
                                                           + L("Ville du Havre", _RAV) + ")."),
           ("Chèque éco-énergie Normandie", "Pour une maison de plus de 15 ans, résidence principale, secondaire ou locative : 600 € pour l’audit "
                                            "énergétique, puis de 6 500 à 12 000 € pour les travaux (" + L("Région Normandie", _CEE) + ")."),
           NATIONAL],
    faq=[("Y a-t-il une aide au ravalement au Havre ?",
          "Oui, pour les façades en brique de Thiers-Coty-Flaubert, Sainte-Marie et Saint-Léon, jusqu’au 31 décembre 2026 : 30 % des travaux hors taxes, "
          "plafonnés à 6 000 € par 100 m² de façade. Les travaux ne commencent qu’après l’accord de la Ville. Partout, un ravalement demande une "
          "déclaration préalable."),
         ("Faut-il une autorisation pour changer ses fenêtres au Havre ?",
          "Oui, la Ville soumet le remplacement de menuiseries à déclaration préalable. Dans le centre reconstruit, la fenêtre neuve garde dimensions, "
          "position et couleur ; la pose en rénovation est proscrite, et le PVC l’est en catégories 1 et 2."),
         ("Peut-on isoler sa façade par l’extérieur dans le centre reconstruit ?",
          "Pas en catégories 1 et 2. En catégories 3 et 4, c’est possible dans un projet d’ensemble, au-dessus du soubassement et sans bardage PVC. "
          "Sinon, le règlement oriente vers l’isolation par l’intérieur ou le remplissage de la lame d’air."),
         ("Le Havre est-il en zone termites ?",
          "Non. L’arrêté préfectoral du 12 juin 2023 ne classe que trois communes de l’agglomération de Rouen en Seine-Maritime."),
         ("Mon terrain est-il concerné par une cavité souterraine ?",
          "Peut-être : le sous-sol havrais compte d’anciennes marnières, cailloutières et abris de guerre. La Ville délivre en ligne un renseignement sur les "
          "cavités souterraines. Protection civile urbaine : 02 35 19 60 11."),
         ("Quelles aides pour rénover son logement au Havre ?",
          "L’aide de la Ville au ravalement des façades en brique, le chèque éco-énergie Normandie pour les maisons de plus de 15 ans (600 € pour l’audit, "
          "de 6 500 à 12 000 € pour les travaux) et les aides nationales. Conseil gratuit à l’Espace Conseil France Rénov’ : 02 35 22 25 20.")],
)

from villes_data import L, S, SP, NATIONAL  # liens dans le texte, sources discrètes, Service-Public, aides nationales

# Sources consultées le 21/11/2026.
_INSEE = "https://www.insee.fr/fr/statistiques/2011101?geo=COM-42218"
_SPR = "https://www.saint-etienne.fr/sites-patrimoniaux-remarquables"
_PF = "https://www.saint-etienne.fr/plan-facades-2021-2026"
_UDAP = "https://www.culture.gouv.fr/Media/medias-creation-rapide/fiche-pratique-udap-de-la-loire-mars2025_v2.pdf"
_CULT = "https://www.culture.gouv.fr/Thematiques/Monuments-Sites/Interventions-demarches/Realiser-des-travaux-dans-un-site-patrimonial-remarquable"
_PLU = "https://www.saint-etienne-metropole.fr/sites/default/files/media/paragraphs/file/2023-10/A2023.00155.pdf"
_PLUI = "https://www.saint-etienne-metropole.fr/habiter-se-deplacer/urbanisme/le-plan-local-durbanisme-intercommunal"
_SENAT = "https://www.senat.fr/questions/base/2026/qSEQ26041062S.html"
_MF = "https://donneespubliques.meteofrance.fr/FichesClim/FICHECLIM_42005001.pdf"
_RADON = "https://georisques.gouv.fr/api/v1/radon?code_insee=42218"
_SISMO = "https://georisques.gouv.fr/api/v1/zonage_sismique?code_insee=42218"
_FRADON = "https://www.georisques.gouv.fr/sites/default/files/2023-05/Fiche-radon.pdf"
_GNAU = "https://urbanisme.saint-etienne-metropole.fr/"
_ODP = "https://connect.saint-etienne.fr/demarche/115/4"
_ECFR = "https://lannuaire.service-public.gouv.fr/auvergne-rhone-alpes/loire/8ed3e0b9-cc20-471f-b090-7ab943cc581f"
_R42 = "https://www.renovactions42.org/"
_R42A = "https://www.renovactions42.org/aides-locales-renovactions-42"

CITY = dict(
    slug="saint-etienne", name="Saint-Étienne", cp="42000", insee="42218",
    lat=45.4339, lon=4.3897, dept="Loire", depcode="42", region="Auvergne-Rhône-Alpes",
    wiki="https://fr.wikipedia.org/wiki/Saint-%C3%89tienne", wikidata="Q42716",
    verified="2026-11-21",
    tldr="À Saint-Étienne, le ravalement est imposé dans certaines rues de l’hyper-centre, et la Ville le subventionne pour les immeubles "
         "d’avant 1960 situés en site patrimonial remarquable",
    hook="Ravalement imposé dans l’hyper-centre, aidé par le plan façades.",
    title="Devis travaux à Saint-Étienne : toiture, façade, fenêtres, isolation",
    desc="Travaux à Saint-Étienne : cinq sites patrimoniaux remarquables, ravalement imposé dans l’hyper-centre, plan façades, radon. Un seul artisan vient chiffrer.",
    figures_intro="Ce qui compte avant de lancer des travaux à Saint-Étienne.",
    figures=[("87,1 <small>%</small>", "des logements sont des appartements", S("Insee, 2023", _INSEE)),
             ("34,6 <small>%</small>", "des résidences principales datent de 1946 à 1970", S("Insee, 2023", _INSEE)),
             ("5", "sites patrimoniaux remarquables dans la ville", S("UDAP de la Loire, 2025", _UDAP)),
             ("59,7 <small>jours</small>", "de gel par an à Saint-Étienne-Bouthéon", S("Météo-France, normales 1991-2020", _MF))],
    answer=("87,1 % des logements sont des appartements, et 34,6 % des résidences principales datent de 1946 à 1970. Cinq secteurs sont des sites "
            "patrimoniaux remarquables, où les travaux passent par l’accord de l’architecte des Bâtiments de France. Dans certaines rues de "
            "l’hyper-centre, la Ville impose le ravalement ; son plan façades aide les immeubles d’avant 1960."),
    facts=[("Sites patrimoniaux remarquables", "Crêt-de-Roc et Tarentaize-Beaubrun-Séverine depuis 2004, Centre-Nord et Couriot-Manufacture depuis 2016, "
                                               "Centre-Sud depuis le 28 mars 2024 (" + L("Ville de Saint-Étienne", _SPR) + "). Les autorisations de travaux "
                                               "y sont soumises à l’accord de l’architecte des Bâtiments de France (" + L("ministère de la Culture", _CULT) + ")."),
           ("Ravalement", "Dans certaines rues de l’hyper-centre, la Ville impose le ravalement des immeubles dont l’état le justifie, par injonction "
                          "(article L126-3 du code de la construction et de l’habitation). Les propriétaires concernés ont été prévenus directement ("
                          + L("plan façades", _PF) + ")."),
           ("Urbanisme", "Le PLU de Saint-Étienne, approuvé le 8 janvier 2008, a été modifié plusieurs fois (" + L("Saint-Étienne Métropole", _PLU)
                         + "). Le PLUi de la Métropole est en cours d’élaboration (" + L("PLUi", _PLUI) + ")."),
           ("Anciennes mines", "Des restrictions liées aux risques miniers touchent moins de 8 % de la zone urbanisée de la ville. Elles sont adaptées "
                               "au niveau d’aléa (" + L("réponse ministérielle au Sénat, 2026", _SENAT) + ")."),
           ("Radon", "La commune est classée en zone 3, à potentiel radon significatif (" + L("Géorisques", _RADON) + "). Géorisques recommande d’y "
                     "mesurer le radon dans les pièces occupées les plus basses, pendant au moins 2 mois en période de chauffe ("
                     + L("fiche radon", _FRADON) + ")."),
           ("Climat", "À Saint-Étienne-Bouthéon, à 395 m d’altitude : 59,7 jours de gel, 20,5 jours de neige et 33,9 jours avec des rafales de "
                      "58 km/h ou plus, chaque année (" + L("Météo-France", _MF) + ", normales 1991-2020).")],
    trades_intro="Immeubles anciens du centre, hivers froids, sous-sol minier : à Saint-Étienne, chaque métier a ses points de vigilance.",
    trades={
        "toiture": ["Avec 59,7 jours de gel et 33,9 jours de rafales d’au moins 58 km/h par an à Bouthéon (" + L("Météo-France", _MF) + ", 1991-2020), "
                    "tuiles, solins et gouttières travaillent tout l’hiver. Faites-les contrôler à l’automne, avant les premières gelées.",
                    "Dans les sites patrimoniaux remarquables, les règles d’urbanisme peuvent porter sur les toitures (" + L("Ville de Saint-Étienne", _SPR)
                    + "). Dans le centre, le plan façades subventionne aussi la restauration des parties sommitales de toiture, avec une visite préalable "
                    "des services de la Ville et de l’État (" + L("plan façades", _PF) + ")."],
        "facade": ["Le plan façades 2021-2026 couvre le centre-ville à l’intérieur du boulevard urbain, de Centre Deux à Carnot. Il aide les immeubles "
                   "d’avant 1960 avec façade sur rue, situés en site patrimonial remarquable. Les rez-de-chaussée, occupés ou vacants, doivent entrer "
                   "dans le programme de travaux (" + L("Ville de Saint-Étienne", _PF) + ").",
                   "Dans l’hyper-centre et les secteurs de renouvellement urbain, l’aide est majorée de 5 points si les délais sont tenus, et certaines "
                   "rues sont sous injonction de ravalement. Pour un immeuble labellisé par la Fondation du patrimoine, jusqu’à 100 % des travaux se "
                   "déduisent du revenu imposable (" + L("plan façades", _PF) + ")."],
        "fenetres": ["En site patrimonial remarquable, la déclaration préalable pour changer des fenêtres est soumise à l’accord de l’architecte des "
                     "Bâtiments de France et s’instruit en 2 mois, contre 1 mois ailleurs (" + L("Service-Public", SP + "F17578") + ", "
                     + L("ministère de la Culture", _CULT) + ").",
                     "La Ville rappelle que les règles de ses sites patrimoniaux portent sur les matériaux employés (" + L("Ville de Saint-Étienne", _SPR)
                     + "). Avant de choisir bois, aluminium ou PVC, demandez les préconisations de l’UDAP de la Loire, qui reçoit sur rendez-vous ("
                     + L("UDAP de la Loire", _UDAP) + ")."],
        "charpente": ["Des restrictions liées aux risques miniers touchent moins de 8 % de la zone urbanisée de Saint-Étienne, avec des règles "
                      "adaptées au niveau d’aléa (" + L("Sénat, 2026", _SENAT) + "). Avant une surélévation ou une extension, vérifiez si votre "
                      "parcelle est concernée auprès du service urbanisme.",
                      "Il neige en moyenne 20,5 jours par an à Bouthéon (" + L("Météo-France", _MF) + "). Avant d’alourdir une couverture ou de poser "
                      "un isolant sur les chevrons, faites vérifier que la charpente porte la charge. La commune est en zone de sismicité 2, faible ("
                      + L("Géorisques", _SISMO) + ")."],
        "isolation": ["Bouthéon compte 2 507,6 degrés-jours unifiés par an (" + L("Météo-France", _MF) + ", 1991-2020) : le chauffage pèse. "
                      "En copropriété, Saint-Étienne Métropole finance 10 % des travaux hors taxes, jusqu’à 15 000 € par logement, au-delà de 35 % "
                      "de gain énergétique (" + L("Rénov’actions42, 2026", _R42A) + ").",
                      "En zone 3 de potentiel radon, Géorisques conseille, après une isolation ou un changement de fenêtres, de garder un renouvellement "
                      "d’air suffisant et de refaire une mesure (" + L("fiche radon", _FRADON) + "). Pour un ravalement aidé, le plan façades exige un "
                      "document de Rénov’actions42 sur les travaux de performance énergétique possibles (" + L("plan façades", _PF) + ")."]},
    steps_intro="Dans l’ordre, du centre intra-boulevard aux autres quartiers.",
    steps=[("Vérifiez si votre immeuble est en site protégé", "Crêt-de-Roc, Tarentaize-Beaubrun-Séverine, Centre-Nord, Couriot-Manufacture et "
                                                              "Centre-Sud sont des sites patrimoniaux remarquables. L’UDAP de la Loire reçoit sur "
                                                              "rendez-vous à La Loire Républicaine, 16 place Jean-Jaurès. 04 77 49 35 50 ("
                                                              + L("UDAP de la Loire", _UDAP) + ")."),
           ("Centre-ville : appelez la chargée de mission plan façades", "Avant la déclaration préalable, elle fait le point sur le projet. Une visite "
                                                                        "suit avec l’architecte conseil de la Ville et l’architecte des Bâtiments de "
                                                                        "France. 04 77 48 65 53 (" + L("plan façades", _PF) + ")."),
           ("Faites le point sur l’énergie", "Le plan façades exige un document de Rénov’actions42 sur les travaux de performance énergétique possibles. "
                                             "C’est aussi le moment de demander les aides, avant de signer."),
           ("Déposez la demande en ligne", "Déclaration préalable ou permis se déposent sur le " + L("guichet numérique", _GNAU) + " de Saint-Étienne "
                                           "Métropole. En site patrimonial remarquable, comptez 2 mois d’instruction."),
           ("Faites autoriser l’échafaudage", "Une autorisation d’occupation du domaine public, payante, se demande au moins 12 jours avant le chantier, "
                                              "par courriel à droitdevoirie@saint-etienne.fr. 04 77 48 73 18 (" + L("démarche", _ODP) + ").")],
    aides_intro="À Saint-Étienne, la Ville aide les façades du centre et la Métropole les copropriétés.",
    aides=[("Rénov’actions42", "L’Espace Conseil France Rénov’ de Saint-Étienne, service public de la rénovation porté par les collectivités de la Loire : "
                               "Maison de l’Habitat et du Logement, 20 A rue Balaÿ, 42000 Saint-Étienne. 04 77 41 41 25 ("
                               + L("annuaire Service-Public", _ECFR) + ", " + L("renovactions42.org", _R42) + ")."),
           ("Plan façades 2021-2026", "La Ville subventionne le ravalement et la restauration d’éléments remarquables (sculptures, devantures menuisées, "
                                      "modénatures, parties sommitales de toiture) des immeubles d’avant 1960 du centre intra-boulevard, en site "
                                      "patrimonial remarquable. Aide majorée de 5 points dans l’hyper-centre si les délais sont tenus ("
                                      + L("Ville de Saint-Étienne", _PF) + ")."),
           ("Copropriétés énergivores", "Saint-Étienne Métropole finance 10 % du coût hors taxes des travaux, plafonnés à 15 000 € par logement, quand le "
                                        "gain énergétique dépasse 35 %, avec des primes individuelles pour les propriétaires occupants modestes ("
                                        + L("Rénov’actions42, 2026", _R42A) + ")."),
           ("Label de la Fondation du patrimoine", "Par convention avec la Ville, un immeuble labellisé permet de déduire du revenu imposable jusqu’à 100 % "
                                                   "du montant des travaux de façade (" + L("plan façades", _PF) + ")."),
           NATIONAL],
    faq=[("Le ravalement est-il obligatoire à Saint-Étienne ?",
          "Dans certaines rues de l’hyper-centre, oui : la Ville a pris des injonctions de ravalement (article L126-3 du code de la construction et de "
          "l’habitation) pour les immeubles dont l’état le justifie, et a prévenu les propriétaires. Dans le centre intra-boulevard, le plan façades aide "
          "les immeubles d’avant 1960 situés en site patrimonial remarquable."),
         ("Mon immeuble est-il dans un site patrimonial remarquable ?",
          "Cinq secteurs le sont : Crêt-de-Roc, Tarentaize-Beaubrun-Séverine, Centre-Nord, Couriot-Manufacture et Centre-Sud, approuvé le 28 mars 2024. "
          "Pour une adresse précise, interrogez l’UDAP de la Loire : 04 77 49 35 50."),
         ("Faut-il une autorisation pour changer ses fenêtres à Saint-Étienne ?",
          "Oui, une déclaration préalable dès que l’aspect extérieur change, sur le guichet numérique de Saint-Étienne Métropole. En site patrimonial "
          "remarquable, l’architecte des Bâtiments de France doit donner son accord, et l’instruction prend 2 mois."),
         ("Les anciennes mines limitent-elles les travaux à Saint-Étienne ?",
          "Sur une petite partie de la ville : moins de 8 % de la zone urbanisée est touchée par des restrictions liées aux risques miniers, adaptées au "
          "niveau d’aléa. Pour une extension ou une surélévation, vérifiez votre parcelle auprès du service urbanisme."),
         ("Saint-Étienne est-elle concernée par le radon ?",
          "Oui, la commune est en zone 3, à potentiel radon significatif. Mesurez le radon au moins 2 mois en période de chauffe, et gardez un "
          "renouvellement d’air suffisant après une isolation ou un changement de fenêtres."),
         ("Quelles aides pour rénover son logement à Saint-Étienne ?",
          "Le plan façades de la Ville pour le centre, l’aide de Saint-Étienne Métropole aux copropriétés énergivores (10 % des travaux, jusqu’à "
          "15 000 € par logement) et les aides nationales. Conseil gratuit à Rénov’actions42 : 04 77 41 41 25.")],
)

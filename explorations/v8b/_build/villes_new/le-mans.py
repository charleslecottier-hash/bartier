from villes_data import L, S, SP, NATIONAL  # liens dans le texte, sources discrètes, Service-Public, aides nationales

# Sources consultées le 21/11/2026. La fiche « dossier complet » d'insee.fr renvoyait une erreur 500 ce jour-là :
# chiffres du recensement 2023 pris dans l'API Melodi de l'Insee (même jeu de données).
_INSEE = "https://api.insee.fr/melodi/data/DS_RP_LOGEMENT_PRINC?GEO=COM-72181"
_LMM = "https://www.lemansmetropole.fr/mon-quotidien/logement-et-urbanisme/"
_PLU = _LMM + "le-plan-local-durbanisme/lapprobation"
_REG = "https://www.lemansmetropole.fr/fileadmin/mediatheque_metropole-du-mans/utilisateurs/urbanisme/documents/plu/pieces/reglement_litteral.pdf"
_CAHIER = "https://www.lemansmetropole.fr/fileadmin/mediatheque_metropole-du-mans/utilisateurs/Logement_urbanisme/documents/cahier_communal_le_mans.pdf"
_DECL = _LMM + "le-plan-local-durbanisme/les-declinaisons-communales/le-mans"
_CARTE = "https://geo.lemans.fr/igeonet_plu/"
_PLANTA = "https://www.lemans.fr/vie-municipale/tourisme-et-patrimoine/cite-plantagenet"
_UDAP = ("https://www.culture.gouv.fr/regions/drac-pays-de-la-loire/la-direction-regionale-des-affaires-culturelles-drac-des-pays-de-la-loire/"
         "Pole-patrimoines-architecture-et-espaces-proteges-Drac-Pays-de-la-Loire/UDAP-Unites-Departementales-de-l-Architecture-et-du-Patrimoine-des-Pays-de-la-Loire/"
         "UDAP-de-la-Sarthe")
_FAQ72 = "https://www.culture.gouv.fr/mc/content/download/395445/file/FAQ%20UDAP%2072.pdf"
_PPRI = ("https://www.sarthe.gouv.fr/Actions-de-l-Etat/Environnement-transition-energetique-et-prevention-des-risques/Risques/Risques-naturels/"
         "Inondation/PPRI-Plans-de-Prevention-du-Risque-Inondation/Les-PPRI-approuves/PPRI-de-l-agglomeration-mancelle")
_MF = "https://donneespubliques.meteofrance.fr/FichesClim/FICHECLIM_72181001.pdf"
_CATNAT = "https://georisques.gouv.fr/api/v1/gaspar/catnat?code_insee=72181&page_size=100"
_RISQ = "https://georisques.gouv.fr/api/v1/gaspar/risques?code_insee=72181"
_CAV = "https://georisques.gouv.fr/api/v1/cavites?code_insee=72181"
_GUICHET = "https://www.lemans.fr/annuaires/demarches/detail/utiliser-le-guichet-des-autorisations-durbanisme"
_ODP = "https://www.lemans.fr/ma-ville/voirie/occupation-temporaire-du-domaine-public"
_AIDES = _LMM + "les-proprietaires/les-aides-a-la-renovation"
_SURE = "https://www.paysdumans.fr/energie-et-climat/renovation-energetique-logements-sure/"
_ECFR = "https://lannuaire.service-public.gouv.fr/pays-de-la-loire/sarthe/a6347f9c-311a-4ad6-b18b-b5c77aa8d9ae"

CITY = dict(
    slug="le-mans", name="Le Mans", cp="72000", insee="72181",
    a="au Mans",
    lat=48.0042, lon=0.1969, dept="Sarthe", depcode="72", region="Pays de la Loire",
    wiki="https://fr.wikipedia.org/wiki/Le_Mans", wikidata="Q1476",
    verified="2026-11-21",
    tldr="Au Mans, le Vieux Mans suit son propre plan de sauvegarde depuis 1974, et ailleurs le PLU de la Métropole n’accepte que le bois peint "
         "pour les fenêtres des maisons repérées comme remarquables",
    hook="Vieux Mans sauvegardé, bois peint sur le bâti remarquable.",
    title="Devis travaux au Mans : toiture, façade, fenêtres, isolation",
    desc="Travaux au Mans : Vieux Mans sauvegardé, fenêtres en bois peint sur le bâti remarquable, crues de la Sarthe et de l’Huisne. "
         "Un seul artisan vient chiffrer.",
    figures_intro="Ce qui compte avant de lancer des travaux entre Sarthe et Huisne.",
    figures=[("57,9 <small>%</small>", "des logements sont des appartements", S("Insee, 2023", _INSEE)),
             ("44,9 <small>%</small>", "des résidences principales datent d’avant 1971", S("Insee, 2023", _INSEE)),
             ("1966", "création du secteur sauvegardé du Vieux Mans", S("PLU de Le Mans Métropole", _REG)),
             ("39,8 <small>jours</small>", "de gel par an au Mans", S("Météo-France, normales 1991-2020", _MF))],
    answer=("Au Mans, 44,9 % des résidences principales datent d’avant 1971 et 57,9 % des logements sont des appartements. Le Vieux Mans, secteur "
            "sauvegardé depuis 1966, relève d’un plan de sauvegarde approuvé en 1974 et de l’avis de l’architecte des Bâtiments de France. Ailleurs, "
            "le PLU de la Métropole impose des fenêtres en bois peint sur les immeubles repérés comme remarquables."),
    facts=[("Vieux Mans", "Secteur sauvegardé créé par arrêté du 29 mars 1966 et étendu le 5 janvier 1971. Son plan de sauvegarde et de mise en valeur, "
                          "approuvé par décret du 20 mai 1974, y remplace le PLU (" + L("règlement du PLU", _REG) + "). L’architecte des Bâtiments de "
                          "France y donne son avis sur les travaux."),
           ("Urbanisme", "Le PLU communautaire de Le Mans Métropole a été approuvé le 30 janvier 2020. Sa modification n° 5 date du 28 mai 2026 ("
                         + L("Le Mans Métropole", _PLU) + ")."),
           ("Patrimoine protégé", "La ville compte 26 monuments historiques classés et 62 inscrits. Le PLU repère en plus des immeubles et des "
                                  "ensembles bâtis remarquables, avec des règles propres sur les fenêtres, les lucarnes et les surélévations ("
                                  + L("cahier communal, 2020", _CAHIER) + ")."),
           ("Inondation", "Le plan de prévention du risque inondation de l’agglomération mancelle, approuvé le 20 décembre 2019, encadre les zones "
                          "inondables de la Sarthe et de l’Huisne au Mans et dans six communes voisines (" + L("préfecture de la Sarthe", _PPRI) + ")."),
           ("Sol et sous-sol", "Géorisques recense 30 arrêtés de catastrophe naturelle au Mans, dont 6 pour des sécheresses survenues de 1989 à 2009, et le dernier pour "
                               "les inondations de février 2026 (" + L("Géorisques", _CATNAT) + "). Il signale aussi un risque d’effondrement "
                               "lié à d’anciennes carrières souterraines (" + L("Géorisques", _RISQ) + ")."),
           ("Climat", "693,4 mm de pluie et 112,1 jours avec au moins 1 mm par an. Il gèle 39,8 jours par an et le thermomètre atteint "
                      "30 °C 15,3 jours. Record : 41,1 °C en juillet 2019 (" + L("Météo-France", _MF) + ", normales 1991-2020).")],
    trades_intro="Pans de bois du Vieux Mans, mancelles de faubourg, pavillons des années 1950 à 1970 : au Mans, les règles changent selon le quartier "
                 "et selon que la maison est repérée ou non.",
    trades={
        "toiture": ["Sur un immeuble repéré comme remarquable, une fenêtre de toit qui remplace une ancienne tabatière garde ses dimensions. Elle ne fait "
                    "pas saillie, ne reçoit aucun volet extérieur, et plusieurs châssis ne peuvent pas être groupés (" + L("règlement du PLU", _REG) + ").",
                    "Gel et fortes chaleurs se succèdent : 39,8 jours de gel par an, 15,3 jours à 30 °C ou plus et une rafale record "
                    "de 36 m/s en novembre 1983 (" + L("Météo-France", _MF) + "). Faites contrôler tuiles ou ardoises, faîtage et gouttières après "
                    "l’hiver et avant les fortes chaleurs."],
        "facade": ["Dans la Cité Plantagenêt, plus d’une centaine de maisons en pan-de-bois datent surtout des XVe et XVIe siècles. Elles retrouvent peu "
                   "à peu leurs couleurs médiévales, bleues, vertes ou rouges (" + L("Ville du Mans", _PLANTA) + "). Tout ravalement y passe par "
                   "l’architecte des Bâtiments de France.",
                   "Sur les immeubles remarquables repérés par le PLU, bandeaux, corniches, linteaux et appuis sont conservés et restaurés avec des "
                   "matériaux identiques. Partout, un matériau fait pour être enduit ne peut pas rester à nu (" + L("règlement du PLU", _REG) + ")."],
        "fenetres": ["Sur un immeuble repéré comme remarquable, on restaure d’abord les fenêtres. Trop abîmées, elles ne se remplacent qu’en bois peint, "
                     "avec le même dessin : dimensions, vantaux, imposte et petits bois. L’ancien dormant est déposé, et les volets roulants sont "
                     "interdits sauf s’ils sont d’origine (" + L("règlement du PLU", _REG) + ").",
                     "Pour les menuiseries en secteur protégé, l’UDAP de la Sarthe conseille d’éviter le blanc pur, le noir pur et les gris très "
                     "foncés. Elle cite les blancs cassés, les gris moyens et les ocres rouges ou jaunes comme couleurs des menuiseries locales ("
                     + L("UDAP de la Sarthe", _FAQ72) + ")."],
        "charpente": ["Autour de l’hypercentre dominent les maisons mitoyennes : mancelles de la fin du XIXe et du début du XXe siècle, souvent à un étage, "
                      "et maisons Leroi-Haricot des années 1950 à 1970 (" + L("cahier communal", _CAHIER) + "). Avant d’aménager leurs combles, "
                      "vérifiez si la maison est repérée au PLU.",
                      "Pour un ensemble bâti remarquable, la surélévation côté rue est interdite : le PLU oriente vers un comble modifié à l’arrière. "
                      "Une lucarne ne peut être supprimée que si elle est plus récente que la maison et nuit à sa valeur patrimoniale ("
                      + L("règlement du PLU", _REG) + ")."],
        "isolation": ["Pour une isolation par l’extérieur d’un bâtiment existant, le PLU peut autoriser un débord de 20 cm au plus sur la marge de retrait "
                      "ou sur le domaine public, si le trottoir reste accessible (" + L("règlement du PLU", _REG) + "). Dans le Vieux Mans, c’est le plan "
                      "de sauvegarde qui s’applique.",
                      "Le Mans Métropole exonère pendant trois ans 50 % de sa part de taxe foncière pour un logement achevé avant 1989, après au moins "
                      "10 000 € de travaux d’économie d’énergie sur un an, ou 15 000 € sur trois ans (" + L("Le Mans Métropole", _AIDES) + ")."]},
    steps_intro="Dans l’ordre, du Vieux Mans aux quartiers de faubourg.",
    steps=[("Repérez les règles de votre parcelle", "La carte interactive du PLU affiche zonage, immeubles remarquables et servitudes ("
                                                   + L("carte du PLU", _CARTE) + "). En zone inondable, consultez aussi le plan de prévention de 2019."),
           ("Secteur protégé : consultez l’UDAP", "Dans le Vieux Mans ou aux abords d’un monument historique, l’architecte des Bâtiments de France donne "
                                                  "son avis. UDAP de la Sarthe, Cité administrative, 19 boulevard Paixhans. 02 85 32 79 60, du lundi au "
                                                  "vendredi de 9 h à 12 h (" + L("ministère de la Culture", _UDAP) + ")."),
           ("Déposez la déclaration préalable", "En ligne sur le guichet numérique de la Ville, ou à la direction Urbanisme et Qualité architecturale, "
                                                "16 avenue François-Mitterrand. 02 43 47 45 18, du lundi au vendredi (" + L("Ville du Mans", _GUICHET) + ")."),
           ("Faites autoriser l’échafaudage", "Demande au moins 10 jours ouvrés avant, trois semaines près du tramway. Droits affichés : 1,50 € le m² par "
                                              "période de sept jours. Si le stationnement est neutralisé, l’arrêté s’affiche 36 heures avant ("
                                              + L("Ville du Mans", _ODP) + ")."),
           ("Demandez conseil avant de signer", "Le SURE, Espace Conseil France Rénov’ du Pays du Mans, vérifie gratuitement votre projet et vos aides.")],
    aides_intro="Au Mans, le conseil public est gratuit et se demande avant de signer le devis.",
    aides=[("SURE, Espace Conseil France Rénov’", "Le Service unique pour la rénovation énergétique du Pays du Mans : conseil gratuit et neutre. "
                                               "9 rue du 33e Mobiles, 72000 Le Mans, sur rendez-vous. 02 55 44 10 10, du lundi au vendredi de 8 h 30 "
                                               "à 17 h 30 (" + L("annuaire Service-Public", _ECFR) + ", " + L("Pays du Mans", _SURE) + ")."),
           ("Programme d’amélioration de l’habitat", "Depuis octobre 2023, Le Mans Métropole accompagne gratuitement les propriétaires occupants modestes "
                                                     "et très modestes, les bailleurs et les copropriétés : visite technique, montage du dossier, suivi des "
                                                     "travaux. Ses aides complètent MaPrimeRénov’ Parcours accompagné, sous conditions. Service Habitat-"
                                                     "Logement : 02 43 47 49 81 (" + L("Le Mans Métropole", _AIDES) + ")."),
           ("Exonération de taxe foncière", "50 % de la part communautaire pendant trois ans, pour un logement achevé avant le 1er janvier 1989, après "
                                            "10 000 € de travaux d’économie d’énergie sur un an ou 15 000 € sur trois ans. La demande se fait en ligne "
                                            "dans l’espace particulier des impôts, avant le 1er janvier de la première année exonérée ("
                                            + L("Le Mans Métropole", _AIDES) + ")."),
           NATIONAL],
    faq=[("Quelles règles pour des travaux dans le Vieux Mans ?",
          "Le Vieux Mans est un secteur sauvegardé depuis 1966. Le PLU ne s’y applique pas : c’est le plan de sauvegarde approuvé en 1974 qui fixe les "
          "règles, et l’architecte des Bâtiments de France donne son avis. UDAP de la Sarthe : 02 85 32 79 60."),
         ("Peut-on poser des fenêtres en PVC au Mans ?",
          "Pas sur un immeuble repéré comme remarquable par le PLU : les fenêtres s’y remplacent uniquement en bois peint, avec le dessin d’origine. "
          "Ailleurs, une déclaration préalable suffit quand l’aspect change. Vérifiez votre adresse sur la carte interactive du PLU."),
         ("Peut-on isoler sa façade par l’extérieur au Mans ?",
          "Oui, avec une déclaration préalable. Le PLU de la Métropole accepte un débord de 20 cm au plus sur le domaine public si le trottoir reste "
          "accessible. Dans le Vieux Mans, le plan de sauvegarde et l’architecte des Bâtiments de France décident."),
         ("Ma maison est-elle en zone inondable au Mans ?",
          "Le plan de prévention du risque inondation de l’agglomération mancelle, approuvé le 20 décembre 2019, couvre les bords de la Sarthe et de "
          "l’Huisne. Sa carte réglementaire est sur le site de la préfecture de la Sarthe."),
         ("Comment faire autoriser un échafaudage au Mans ?",
          "Demandez une occupation temporaire du domaine public à la Ville au moins 10 jours ouvrés avant, trois semaines près du tramway. Les droits "
          "se paient au m² occupé, par période de sept jours."),
         ("Quelles aides pour rénover son logement au Mans ?",
          "L’accompagnement gratuit de Le Mans Métropole pour les ménages modestes, ses aides en complément de MaPrimeRénov’ Parcours accompagné, "
          "l’exonération de 50 % de la part communautaire de taxe foncière pendant trois ans et les aides nationales. Conseil gratuit au SURE : "
          "02 55 44 10 10.")],
)

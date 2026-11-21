from villes_data import L, S, SP, NATIONAL  # liens dans le texte, sources discrètes, Service-Public, aides nationales
REVIEWED = "2026-11-21"

# Sources consultées le 21/11/2026.
_INSEE = "https://api.insee.fr/melodi/data/DS_RP_LOGEMENT_PRINC?GEO=COM-83137"  # dossier complet, RP 2023 (page insee.fr en erreur 500 ce jour)
_MF = "https://donneespubliques.meteofrance.fr/FichesClim/FICHECLIM_83137001.pdf"
_URBA = "https://toulon.fr/urbanisme"
_SPR = "https://toulon.fr/site-patrimonial-remarquable-spr"
_PLAQ = "https://toulon.fr/sites/default/files/2025-06/plaquette_avap.pdf"
_AVAP = "https://toulon.fr/sites/default/files/2025-06/reglement_avap_creee.pdf"
_PLU = "https://toulon.fr/plu"
_RAV = "https://toulon.fr/sites/default/files/2026-03/perimetre_campagne_de_ravalements_de_facades_obligatoire_2019-2026_0.pdf"  # règlement de la campagne des Halles
_TERM = ("https://www.var.gouv.fr/Actions-de-l-Etat/Amenagement-du-territoire-construction-logement/Habitat-logement/"
         "Termites-et-insectes-xylophages/Le-Var-et-les-termites")
_TERM_AP = "https://www.var.gouv.fr/contenu/telechargement/32833/218998/file/AP_liste%20des%20communes%20cotamin%C3%A9es%20termites.pdf"
_PAC = "https://toulon.fr/sites/default/files/2026-09/PAC_Le_LAS_TOULON_28_aout_2026_VF.pdf"
_DP = "https://demarches.toulon.fr/infos_demarches/urbanisme-foncier/la-declaration-prealable-de-travaux/"  # lien vers le guichet unique (le guichet lui-même répond 403 aux robots)
_ECHAF = "https://demarches.toulon.fr/infos_demarches/urbanisme-foncier/installation-dechafaudage-palissade-grue/"
_UDAP = ("https://www.culture.gouv.fr/regions/drac-provence-alpes-cote-d-azur/la-direction-regionale-des-affaires-culturelles-drac-provence-alpes-cote-d-azur/"
         "unites-departementales-de-l-architecture-et-du-patrimoine-udap-de-provence-alpes-cote-d-azur/udap-du-var")
_UDAP_FICHES = "https://www.culture.gouv.fr/Media/Regions/Drac-Paca/Files/Aides-demarches/Demarches-et-conseils-architecture-patrimoine/Fiches-conseil/udap-du-var/"
_TUILE = _UDAP_FICHES + "05-Les-toitures-en-tuiles-rondes"
_THERM = _UDAP_FICHES + "15-Le-confort-thermique"
_ECFR = "https://lannuaire.service-public.gouv.fr/provence-alpes-cote-d-azur/var/f075f335-4b08-4959-94ca-2639f1662305"
_BCS = "https://www.bienchezsoi-tpm.fr/"
_TPM = "https://metropoletpm.fr/demarches/aider-la-renovation-et-lamelioration-de-son-logement"
_CD83 = "https://var.fr/documents/d/departement-du-var/brochure-aides-habitat-2025-bat3-pdf"

CITY = dict(
    slug="toulon", name="Toulon", cp="83000", insee="83137",
    lat=43.1222, lon=5.9300, dept="Var", depcode="83", region="Provence-Alpes-Côte d’Azur",
    wiki="https://fr.wikipedia.org/wiki/Toulon", wikidata="Q44160",
    verified="2026-11-21",
    tldr="À Toulon, le grand centre-ville est un site patrimonial remarquable où chaque chantier passe par l’architecte des Bâtiments de France, "
         "et la Ville paie 32 % du hors-taxe, avec plafond, des ravalements qu’elle impose",
    hook="Centre protégé, ravalements imposés et aidés, fortes rafales plus de 100 jours par an.",
    title="Devis travaux à Toulon : toiture, façade, fenêtres, isolation",
    desc="Travaux à Toulon : centre protégé, ravalement imposé et aidé à 32 %, zone termites, fortes rafales, conseil gratuit. Un seul artisan vient chiffrer.",
    figures_intro="Ce qui compte avant de lancer des travaux entre le mont Faron et la rade.",
    figures=[("79,2 <small>%</small>", "des logements sont des appartements", S("Insee, 2023", _INSEE)),
             ("60,1 <small>%</small>", "des résidences principales datent d’avant 1971", S("Insee, 2023", _INSEE)),
             ("108,9 <small>jours</small>", "par an avec des rafales d’au moins 58 km/h", S("Météo-France, normales 1991-2020", _MF)),
             ("32 <small>%</small>", "du hors-taxe d’un ravalement imposé, payés par la Ville avec un plafond", S("Ville de Toulon", _URBA))],
    answer=("À Toulon, 79,2 % des logements sont des appartements et 60,1 % des résidences principales datent d’avant 1971. Dans le site patrimonial "
            "remarquable du centre, tous les travaux demandent une autorisation et l’avis de l’architecte des Bâtiments de France. Toute la commune "
            "est en zone termites depuis l’arrêté préfectoral du 10 décembre 2018."),
    facts=[("Centre protégé", "Le site patrimonial remarquable couvre la ville comprise dans les anciens remparts Napoléon III, en cinq secteurs. Le règlement de "
                              "l’AVAP créée le 28 mai 2014 s’y applique toujours : tout projet demande une autorisation et l’avis motivé de l’architecte des "
                              "Bâtiments de France (" + L("Ville de Toulon", _SPR) + ", " + L("plaquette", _PLAQ) + ")."),
           ("Ravalement", "La Ville impose le ravalement par arrêté d’injonction dans trois secteurs jusqu’en 2026 : quartier des Halles (53 immeubles), place "
                          "Saint-Jean (22) et avenue du XVe-Corps (18). Seuls les propriétaires qui ont reçu l’injonction touchent son aide (" + L("Ville de Toulon", _URBA) + ")."),
           ("Urbanisme", "Le PLU de Toulon, approuvé le 27 juillet 2012, est géré par la Métropole Toulon Provence Méditerranée depuis le 1er janvier 2018. "
                         "Sa modification simplifiée n° 9 a été prescrite le 5 mars 2026 (" + L("Ville de Toulon", _PLU) + ")."),
           ("Termites", "Toulon fait partie des 81 communes du Var classées en zone contaminée sur tout leur territoire par l’arrêté préfectoral du "
                        "10 décembre 2018. Toute présence de termites se déclare en mairie (" + L("arrêté préfectoral", _TERM_AP) + ", "
                        + L("préfecture du Var", _TERM) + ")."),
           ("Vent et chaleur", "À la station de Toulon, 108,9 jours par an de rafales d’au moins 58 km/h, dont 6,3 d’au moins 100 km/h, et 36,6 jours "
                               "à 30 °C ou plus (" + L("Météo-France", _MF) + ", normales 1991-2020)."),
           ("Inondation", "Le préfet a porté à la connaissance de la commune, le 28 août 2026, l’aléa inondation par débordement du Las. "
                          "En zone inondable, les traitements de façade et les réfections de toiture restent admis s’ils n’aggravent pas le risque ("
                          + L("porter à connaissance", _PAC) + ").")],
    trades_intro="Vieille ville médiévale, Haute ville haussmannienne, immeubles bâtis de 1946 à 1970, plus d’un tiers des résidences principales : à Toulon, les règles changent d’un secteur à l’autre.",
    trades={
        "toiture": ["Dans la vieille ville, les tuiles rondes en terre cuite se posent en couvert et courant, en réemployant les anciennes, sur une pente de 30 % "
                    "au plus. Les altanas, ces terrasses de toit, sont à conserver ; une fenêtre de toit, 60 x 80 cm au plus, n’est admise que dans certains cas ("
                    + L("règlement de l’AVAP", _AVAP) + ").",
                    "Avec 108,9 jours de rafales d’au moins 58 km/h par an, faites contrôler faîtage et tuiles de rive après chaque coup de vent. Dans le Var, "
                    "les toits ont une pente faible, de 27 à 33 % (" + L("UDAP du Var", _TUILE) + ")."],
        "facade": ["Dans la vieille ville, les enduits se refont à la chaux en trois couches, finis frottassés, talochés ou regravés en faux appareil « à la marseillaise », puis "
                   "peints au lait de chaux ou à la peinture minérale dans une teinte du nuancier de la Ville. Peindre la pierre de taille est interdit ("
                   + L("règlement de l’AVAP", _AVAP) + ").",
                   "Dans les rues en campagne, la Ville paie 32 % du hors-taxe ; aux Halles, l’aide est plafonnée de 14 000 à 27 000 € selon l’immeuble et "
                   "demande un maître d’œuvre. Détruire volontairement un nid de martinets supprime l’aide : faites-les repérer avant le chantier (" + L("règlement de campagne", _RAV) + ")."],
        "fenetres": ["Dans la vieille ville, les menuiseries neuves sont en principe en bois, sur le modèle de l’immeuble, peintes dans une teinte du nuancier, "
                     "jamais en blanc pur. Les persiennes provençales sont gardées ou refaites à l’identique (" + L("règlement de l’AVAP", _AVAP) + ").",
                     "Dans le site patrimonial remarquable, changer ses menuiseries ou ses volets demande une déclaration préalable et l’avis motivé de "
                     "l’architecte des Bâtiments de France (" + L("plaquette de la Ville", _PLAQ) + "). Dans la vieille ville, les climatiseurs en saillie "
                     "sur la façade sont interdits ; ils peuvent aller dans une cour arrière ou derrière une ventelle (" + L("règlement de l’AVAP", _AVAP) + ")."],
        "charpente": ["Toute la commune est en zone termites depuis 2018. Si vous en trouvez en ouvrant une toiture, déclarez-les en mairie. Dans un "
                      "périmètre d’infestation délimité par arrêté municipal, les bois contaminés d’une démolition sont brûlés sur place ou traités "
                      "avant tout transport (" + L("arrêté préfectoral", _TERM_AP) + ").",
                      "Le long du Las, en zone inondable, une surélévation reste possible si le nouveau plancher est au moins 0,40 m au-dessus de la cote de "
                      "crue de référence, sans créer de logement en plus (" + L("porter à connaissance", _PAC) + ", 2026)."],
        "isolation": ["Ici, isoler sert aussi contre la chaleur : 36,6 jours par an atteignent 30 °C. Dans un mur ancien, gardez l’inertie et des matériaux "
                      "perméables à la vapeur d’eau, conseille l’UDAP du Var, le service de l’architecte des Bâtiments de France ("
                      + L("fiche conseil", _THERM) + ").",
                      "Dans la vieille ville, l’isolation par l’extérieur est interdite sur les façades sur rue et possible en cœur d’îlot. Une pompe à chaleur "
                      "n’y va que dans une cour intérieure ou intégrée à la façade (" + L("règlement de l’AVAP", _AVAP) + ")."]},
    steps_intro="Dans l’ordre, avant de signer le moindre devis.",
    steps=[("Vérifiez si vous êtes dans le site patrimonial remarquable", "Dans les anciens remparts Napoléon III, l’architecte des Bâtiments de France donne "
                                                                          "son avis sur tous les travaux. UDAP du Var, 449 avenue de la Mitre : 04 94 31 59 95, "
                                                                          "de 9 h à 12 h (" + L("ministère de la Culture", _UDAP) + ")."),
           ("Demandez la fiche de l’architecte conseil", "Dans les rues en campagne de ravalement, l’architecte conseil de la Ville fixe les prescriptions, sur "
                                                         "rendez-vous : 04 94 36 33 39. Service Environnement urbain : 04 94 36 33 87 (" + L("règlement de campagne", _RAV) + ")."),
           ("Déposez la déclaration préalable", "En ligne sur le guichet unique de la Ville, par courrier, ou au service Droit des sols, "
                                                "10e étage de l’Hôtel de Ville, les lundis, mercredis et vendredis de 9 h à 12 h sur rendez-vous. "
                                                "04 94 36 30 70 (" + L("démarche et accès au guichet", _DP) + ")."),
           ("Faites autoriser l’échafaudage", "Au moins 45 jours avant le chantier, auprès du service des Emplacements : odp@mairie-toulon.fr, 04 94 36 83 57 ("
                                              + L("démarche", _ECHAF) + ")."),
           ("Appelez Bien chez Soi", "Conseil gratuit sur la rénovation énergétique et les aides. Ne commencez rien avant le dépôt de la demande de subvention ("
                                     + L("Métropole", _TPM) + ").")],
    aides_intro="À Toulon, la demande d’aide se dépose avant le début des travaux, et le conseil public ne coûte rien.",
    aides=[("Bien chez Soi", "L’Espace Conseil France Rénov’ de Toulon, service gratuit de la Métropole Toulon Provence Méditerranée : 217 avenue de la "
                             "Victoire-du-8-Mai-45, 83000 Toulon. 08 05 69 23 20, du lundi au vendredi de 9 h à 17 h (" + L("annuaire de l’administration", _ECFR) + "). "
                             "Il couvre les 12 communes de la Métropole, hors secteurs d’OPAH-RU (" + L("bienchezsoi-tpm.fr", _BCS) + ")."),
           ("Aide au ravalement de la Ville", "32 % du montant hors taxes des travaux subventionnables, avec plafond, pour les propriétaires qui ont reçu un arrêté "
                                              "d’injonction (" + L("Ville de Toulon", _URBA) + "). Aux Halles, le plafond va de 14 000 à 27 000 € par immeuble ("
                                              + L("règlement", _RAV) + ")."),
           ("Aide du Département du Var", "Pour les propriétaires occupants modestes, éligibles aux aides de l’Anah : jusqu’à 14 000 € pour améliorer l’habitat "
                                          "et sa performance énergétique. Plafond de revenus : 19 000 € pour une personne seule. SOLIHA Var : 04 94 22 65 85 ("
                                          + L("guide des aides, 2025", _CD83) + ")."),
           NATIONAL],
    faq=[("Le ravalement est-il obligatoire à Toulon ?",
          "Dans les rues en campagne, oui : la Ville l’impose par arrêté d’injonction aux Halles, place Saint-Jean et avenue du XVe-Corps jusqu’en 2026, et paie "
          "32 % du hors-taxe. Dans le site patrimonial remarquable, un ravalement demande une déclaration préalable et l’avis de l’architecte des Bâtiments de France."),
         ("Quelles règles pour les toits de la vieille ville de Toulon ?",
          "Tuiles rondes en terre cuite posées en couvert et courant, pente de 30 % au plus, débord en génoise ou en chevrons. Les altanas sont conservées, et une "
          "fenêtre de toit de 60 x 80 cm au plus n’est admise que dans certains cas."),
         ("L’isolation par l’extérieur est-elle permise dans la vieille ville de Toulon ?",
          "Sur les façades sur rue, non : le règlement de l’AVAP l’interdit, à cause de l’empiètement sur le domaine public et de l’intérêt des façades. En cœur d’îlot et dans "
          "les cours intérieures, elle est possible."),
         ("Toulon est-elle en zone termites ?",
          "Oui, sur tout son territoire, avec 80 autres communes du Var, depuis l’arrêté préfectoral du 10 décembre 2018. Pour vendre, il faut annexer à l’acte un "
          "diagnostic termites daté de moins de six mois."),
         ("Quelles aides pour rénover son logement à Toulon ?",
          "L’aide de la Ville au ravalement dans les rues en campagne (32 % du hors-taxe), l’aide du Département du Var pour les propriétaires modestes "
          "(jusqu’à 14 000 €) et les aides nationales. Bien chez Soi, l’Espace Conseil France Rénov’, vous guide gratuitement : 08 05 69 23 20."),
         ("Comment faire autoriser un échafaudage à Toulon ?",
          "Écrivez au service des Emplacements au moins 45 jours avant le début des travaux, à odp@mairie-toulon.fr, ou appelez le 04 94 36 83 57. "
          "Une demande tardive n’est pas traitée. Si l’immeuble a un commerce au rez-de-chaussée, la pose est interdite du 15 décembre au 15 janvier "
          "et du 1er juillet au 31 août (" + L("démarche", _ECHAF) + ").")],
)

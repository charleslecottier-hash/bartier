from villes_data import L, S, SP, NATIONAL  # liens dans le texte, sources discrètes, Service-Public, aides nationales

REVIEWED = "2026-11-21"

# Sources consultées le 21/11/2026.
_INSEE = "https://api.insee.fr/melodi/data/DS_RP_LOGEMENT_PRINC?GEO=COM-33063"  # dossier complet, RP 2023 (page insee.fr en erreur 500 ce jour)
_PSMV = "https://www.bordeaux.fr/sites/bor-bdxfr-drupal/files/2025-03/psmv_reglement_annexes_juin2021.pdf"
_PSMV_RP = "https://www.bordeaux.fr/sites/bor-bdxfr-drupal/files/2025-03/psmv_rapport-de-presentation_juin2021.pdf"
_BM_2025 = ("https://www.bordeaux-metropole.fr/sites/MET-BXMETRO-DRUPAL/files/bm_actes/organismes/bordeaux-metropole/conseils/"
            "2025-06-06/Parapheur2025-221-1_0.pdf")
_PLU_EVOL = "https://fichiers.bordeaux-metropole.fr/plu/PLU31_interactif/Fichiers/tableau_evolution.pdf"
_UP1 = ("https://fichiers.bordeaux-metropole.fr/plu/PLU31_interactif/Fichiers/5_Reglement/1_Reglement_pieces_ecrites/"
        "1_Reglement_par_zone/4_zones_UP/UP1.pdf")
_PLU_BDX = "https://www.bordeaux.fr/comprendre-le-plan-local-durbanisme-metropolitain"
_CARTE = "https://geo.bordeaux-metropole.fr/adws/app/f7cd7fbf-2946-11e9-91fd-57b991809803/index.html"
_DEM = "https://www.bordeaux.fr/les-demarches-durbanisme-a-bordeaux"
_GUICHET = "https://urbanisme.bordeaux-metropole.fr/guichet/Login/Particulier"
_ODP = "https://www.bordeaux.fr/demander-une-autorisation-doccupation-de-lespace-public-pour-un-chantier"
_ODP_LIGNE = "https://mesdemarches.bordeaux.fr/portals/public/services?id=bordeaux&page=DEM_Demarches_Presentation&ts=920"
_TERM = "https://www.bordeaux.fr/lutte-contre-les-termites"
_MF = "https://donneespubliques.meteofrance.fr/FichesClim/FICHECLIM_33281001.pdf"
_PPRI = "https://www.georisques.gouv.fr/donnee-risques/PPR/Fiche-ppr/pprn/33DREAL20170013"
_CATNAT = "https://georisques.gouv.fr/api/v1/gaspar/catnat?code_insee=33063&page_size=100"
_AIDES = "https://www.bordeaux.fr/les-aides-a-la-renovation-de-lhabitat-prive-a-bordeaux"
_MARENOV = "https://marenov.bordeaux-metropole.fr/"
_MARENOV_DEM = "https://marenov.bordeaux-metropole.fr/la-demarche-de-a-a-z/demarche-pour-les-logements-individuels"
_THERMO = "https://marenov.bordeaux-metropole.fr/outils-pratiques/thermographie-aerienne"
_UDAP = ("https://www.culture.gouv.fr/fr/regions/drac-nouvelle-aquitaine/patrimoines-et-architecture-a-la-drac-nouvelle-aquitaine/"
         "les-unites-departementales-de-l-architecture-et-du-patrimoine-en-nouvelle-aquitaine/udap-de-la-gironde-33")

CITY = dict(
    slug="bordeaux", name="Bordeaux", cp="33000", insee="33063",
    lat=44.8378, lon=-0.5792, dept="Gironde", depcode="33", region="Nouvelle-Aquitaine",
    wiki="https://fr.wikipedia.org/wiki/Bordeaux", wikidata="Q1479",
    verified="2026-11-21",
    tldr=("À Bordeaux, la façade en pierre reste nue : ni peinture ni isolation par l’extérieur dans la ville de pierre, "
          "et l’architecte des Bâtiments de France valide tout changement dans le secteur sauvegardé"),
    hook="La pierre de taille reste nue, sans peinture ni isolation extérieure.",
    title="Devis travaux à Bordeaux : toiture, façade, fenêtres, isolation",
    desc=("Travaux à Bordeaux : pierre de taille sans peinture, secteur sauvegardé, zone termites, aide Ma Rénov "
          "jusqu’à 29 000 €. Un seul artisan vient chiffrer."),
    figures_intro="Le bâti, la pierre et les sols de Bordeaux en quatre chiffres.",
    figures=[("79,0 <small>%</small>", "des logements sont des appartements", S("Insee, 2023", _INSEE)),
             ("22,8 <small>%</small>", "des résidences principales datent d’avant 1919", S("Insee, 2023", _INSEE)),
             ("150 <small>ha</small>", "de secteur sauvegardé dans le centre ancien, protégé depuis 1967", S("PSMV, 2021", _PSMV_RP)),
             ("23", "reconnaissances de catastrophe naturelle pour sécheresse depuis 1989", S("Géorisques", _CATNAT))],
    answer=("Les logements sont surtout des appartements (79,0 %), et 22,8 % des résidences principales datent d’avant 1919. "
            "Dans la ville de pierre, le PLU interdit de peindre une façade en pierre et de l’isoler par l’extérieur ; dans le "
            "secteur sauvegardé, tout changement passe par l’architecte des Bâtiments de France. Toute la Gironde est en zone "
            "termites depuis 2001."),
    facts=[("Centre ancien", "Secteur sauvegardé depuis le 16 février 1967, devenu site patrimonial remarquable : son plan de sauvegarde "
                             "couvre 150,28 hectares (" + L("rapport de présentation", _PSMV_RP) + "), et sa révision a été approuvée le "
                             "18 février 2022 (" + L("Bordeaux Métropole", _BM_2025) + "). "
                             "Tout travail qui modifie un immeuble, dehors comme dedans, demande l’accord de l’architecte des Bâtiments "
                             "de France (" + L("PSMV", _PSMV) + ")."),
           ("Ville de pierre", "Hors secteur sauvegardé, la zone UP1 du PLU protège la ville de pierre : façades en pierre ou en brique "
                               "sans peinture, film, résine ni hydrofuge, et aucune isolation par l’extérieur sur un mur en pierre de "
                               "taille (" + L("PLU, zone UP1", _UP1) + ")."),
           ("Urbanisme", "Le PLU 3.1 de Bordeaux Métropole, issu de la révision du 16 décembre 2016, s’applique depuis le 24 février "
                         "2017. Sa 11e modification, "
                         "approuvée le 2 février 2024, a mis à jour les plans de la ville de pierre (" + L("Bordeaux Métropole", _PLU_EVOL)
                         + "). Une nouvelle révision a été lancée le 6 juin 2025 (" + L("délibération", _BM_2025) + ")."),
           ("Inondation", "Un plan de prévention du risque d’inondation propre à Bordeaux, pour les crues lentes et la submersion marine, "
                          "est approuvé depuis le 5 décembre 2023. En zone inondable, ses règles s’ajoutent au PLU ("
                          + L("Géorisques", _PPRI) + ")."),
           ("Termites", "Toute la Gironde est déclarée infestée par l’arrêté préfectoral du 12 février 2001. Si des termites sont "
                        "trouvés, le maire peut imposer des travaux de traitement dans un délai de six mois (" + L("Ville de Bordeaux", _TERM) + ")."),
           ("Climat et sols", "À Bordeaux-Mérignac, 924,9 mm de pluie et 25,5 jours à 30 °C ou plus par an (" + L("Météo-France", _MF)
                              + ", normales 1991-2020). La commune compte 23 reconnaissances de catastrophe naturelle pour sécheresse "
                              "depuis 1989 (" + L("Géorisques", _CATNAT) + ").")],
    trades_intro="Dans le centre ancien comme dans la ville de pierre, deux textes encadrent vos travaux : le plan de sauvegarde et le PLU.",
    trades={
        "toiture": ["Dans le secteur sauvegardé, le plan de sauvegarde fixe la couverture : tuile canal dite de Gironde sur les édifices "
                    "anciens, tuile de Marseille à partir du milieu du XIXe siècle, ardoise naturelle ou zinc selon le comble. Gouttières "
                    "et chéneaux y sont en zinc ou en cuivre, et les capteurs photovoltaïques n’y sont pas autorisés sur le bâti "
                    "existant (" + L("PSMV", _PSMV) + ").",
                    "Dans la ville de pierre, un châssis de toit doit faire moins de 0,80 m² et rester dans le plan de la couverture ("
                    + L("PLU, zone UP1", _UP1) + "). En 2018, Bordeaux Métropole a survolé de nuit ses 28 communes en infrarouge pour "
                    "repérer les pertes de chaleur par les toits : un conseiller Ma Rénov vous aide à lire celle de votre maison ("
                    + L("thermographie aérienne", _THERMO) + ")."],
        "facade": ["Dans la ville de pierre, les façades en pierre appareillée ou en brique restent naturelles, sans peinture, film, résine "
                   "ni hydrofuge. Sur une construction protégée, le sablage est exclu : on nettoie par pulvérisation d’eau, micro-fines, "
                   "laser ou gommage (" + L("PLU, zone UP1", _UP1) + ").",
                   "Dans le secteur sauvegardé, la pierre de taille reste apparente. Si elle a été peinte ou enduite, le ravalement lui "
                   "rend son aspect d’origine, et seul un badigeon de chaux coloré par des terres est admis. Les joints se refont au "
                   "mortier de chaux naturelle et sable de rivière (" + L("PSMV", _PSMV) + ")."],
        "fenetres": ["Dans le secteur sauvegardé, on répare d’abord les menuiseries anciennes. Une fenêtre neuve y est en bois ou en acier "
                     "peint, de couleur claire non blanche, plutôt dans les gris, et les volets roulants en PVC ou en aluminium sont "
                     "refusés (" + L("PSMV", _PSMV) + ").",
                     "Dans la ville de pierre, les coffres de volets roulants se posent à l’intérieur, invisibles de la rue. Sur une "
                     "construction protégée, une fenêtre à la française ne peut pas devenir coulissante ou à l’anglaise, et la menuiserie "
                     "ne se pose pas au nu extérieur de la façade (" + L("PLU, zone UP1", _UP1) + ")."],
        "charpente": ["Toute la Gironde est zone infestée par les termites depuis l’arrêté préfectoral du 12 février 2001. Tout foyer "
                      "doit être déclaré, et le traitement doit être fait par une autre entreprise que celle qui a établi le diagnostic ("
                      + L("Ville de Bordeaux", _TERM) + ").",
                      "Pour isoler des combles dans le secteur sauvegardé, l’isolant ne doit pas menacer les bois de charpente, qui restent "
                      "ventilés (" + L("PSMV", _PSMV) + "). Hors secteur, une surélévation doit respecter la hauteur des bâtiments voisins, surtout s’ils sont "
                      "protégés (" + L("Ville de Bordeaux", _PLU_BDX) + ")."],
        "isolation": ["Ma Rénov Bordeaux Métropole complète MaPrimeRénov’ : jusqu’à 29 000 € pour une rénovation d’ampleur, jusqu’à "
                      "15 000 € pour des travaux par geste, isolation comprise (" + L("Ville de Bordeaux", _AIDES) + ", 2026). Le dossier "
                      "se dépose avant les travaux, et les devis se signent après l’accord de la Métropole (" + L("Ma Rénov", _MARENOV_DEM) + ").",
                      "Sur un mur en pierre de taille de la ville de pierre, l’isolation par l’extérieur est interdite. Dans le secteur "
                      "sauvegardé, le plan de sauvegarde privilégie un enduit isolant mince à l’intérieur, perméable à la vapeur d’eau. "
                      "Avec 25,5 jours à 30 °C ou plus par an à Mérignac, pensez aussi au confort d’été (" + L("Météo-France", _MF) + ")."]},
    steps_intro="Dans l’ordre, du repérage de votre adresse à l’échafaudage.",
    steps=[("Repérez la règle de votre adresse", "La " + L("carte interactive du PLU", _CARTE) + " situe votre terrain et renvoie au "
                                                 "règlement de sa zone (" + L("Ville de Bordeaux", _PLU_BDX) + "). En secteur protégé, "
                                                 "l’architecte des Bâtiments de France donne son avis : UDAP de la Gironde, 54 rue Magendie, "
                                                 "05 56 00 87 10, par téléphone du lundi au jeudi de 14 h à 16 h ("
                                                 + L("ministère de la Culture", _UDAP) + ")."),
           ("Rencontrez un conseiller Ma Rénov", "Rendez-vous gratuit au 05 57 20 70 20 ou en ligne. Le dossier d’aide se dépose avant "
                                                 "les travaux, et les devis se signent après l’accord de Bordeaux Métropole."),
           ("Déposez la déclaration préalable", "En ligne sur le " + L("portail urbanisme", _GUICHET) + " de Bordeaux Métropole, ou au "
                                                "service droit des sols, Cité municipale, 4 rue Claude-Bonnier : sans rendez-vous du lundi "
                                                "au vendredi de 9 h à 16 h 45, dès 9 h 30 le jeudi. 05 24 57 16 07 ("
                                                + L("Ville de Bordeaux", _DEM) + ")."),
           ("Faites autoriser l’échafaudage", "Trois semaines avant le chantier, sur le " + L("portail des démarches", _ODP_LIGNE)
                                              + " de la Ville. Une emprise clôturée coûte 0,60 € le m² par jour ; sans autorisation, "
                                              "la taxe monte à 18,73 € le m² par jour (" + L("Ville de Bordeaux", _ODP) + ").")],
    aides_intro="À Bordeaux, le dossier d’aide part avant la signature des devis, et le conseil Ma Rénov est gratuit.",
    aides=[("Ma Rénov Bordeaux Métropole", "L’Espace Conseil France Rénov’ de Bordeaux Métropole : conseil gratuit et neutre, en rendez-vous "
                                           "dans les communes ou en visioconférence. Esplanade Charles-de-Gaulle, 33045 Bordeaux Cedex. "
                                           "05 57 20 70 20, du lundi au vendredi de 8 h à 18 h 30. "
                                           + L("marenov.bordeaux-metropole.fr", _MARENOV) + "."),
           ("Aide Ma Rénov aux logements", "En complément de MaPrimeRénov’ : jusqu’à 29 000 € pour une rénovation d’ampleur, avec au moins "
                                          "deux gestes d’isolation et deux classes énergétiques gagnées, et jusqu’à 15 000 € pour une "
                                          "rénovation par geste, avec au moins un geste d’isolation (" + L("Ville de Bordeaux", _AIDES)
                                          + ", 2026, " + L("Ma Rénov", _MARENOV) + ")."),
           ("Ma Rénov copropriétés", "Jusqu’à 20 % des travaux de rénovation énergétique financés par l’Anah, plus une prime de 750 € ou "
                                    "1 500 € par propriétaire occupant modeste ou très modeste (" + L("Ville de Bordeaux", _AIDES) + ")."),
           ("Expertise structure", "La Ville prend en charge jusqu’à 50 % du montant TTC, plafonné à 1 000 € par immeuble, pour faire "
                                   "expertiser la structure d’un immeuble collectif. Centre de gestion des aides à la pierre : "
                                   "05 56 10 19 20 (" + L("Ville de Bordeaux", _AIDES) + ")."),
           NATIONAL],
    faq=[("Peut-on peindre une façade en pierre à Bordeaux ?",
          "Pas dans la ville de pierre : le PLU impose des façades en pierre ou en brique naturelles, sans peinture, résine ni hydrofuge. "
          "Dans le secteur sauvegardé, seul un badigeon de chaux coloré par des terres est admis, et une pierre déjà peinte retrouve son "
          "aspect d’origine au ravalement."),
         ("Faut-il l’accord de l’architecte des Bâtiments de France à Bordeaux ?",
          "Oui dans le secteur sauvegardé, pour tout travail qui modifie un immeuble, même à l’intérieur. Aux abords d’un monument "
          "historique, l’architecte des Bâtiments de France donne aussi son avis. UDAP de la Gironde : 05 56 00 87 10."),
         ("Peut-on isoler par l’extérieur une maison en pierre à Bordeaux ?",
          "Pas sur un mur en pierre de taille de la ville de pierre : le PLU l’interdit. Restent les combles, les planchers et "
          "l’isolation par l’intérieur, que Ma Rénov Bordeaux Métropole aide jusqu’à 15 000 € en rénovation par geste."),
         ("Bordeaux est-elle en zone termites ?",
          "Oui, comme toute la Gironde depuis l’arrêté préfectoral du 12 février 2001. Un état relatif aux termites est joint à toute "
          "vente, et le maire peut imposer un traitement dans un délai de six mois."),
         ("Quelles aides pour rénover son logement à Bordeaux ?",
          "Ma Rénov Bordeaux Métropole, jusqu’à 29 000 € pour une rénovation d’ampleur et 15 000 € pour une rénovation par geste, "
          "Ma Rénov copropriétés, "
          "l’aide de la Ville aux expertises de structure, et les aides nationales. Conseil gratuit : 05 57 20 70 20."),
         ("Comment faire autoriser un échafaudage à Bordeaux ?",
          "Demandez l’occupation du domaine public trois semaines avant le chantier, sur le portail des démarches de la Ville. "
          "Elle est payante, selon la surface, le type et la durée d’occupation.")],
)

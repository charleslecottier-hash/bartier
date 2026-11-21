from villes_data import L, S, SP, NATIONAL  # liens dans le texte, sources discrètes, Service-Public, aides nationales

# Sources consultées le 21/11/2026. La fiche « dossier complet » d'insee.fr renvoyait une erreur 500 ce jour-là :
# les chiffres logement viennent du même jeu de données (Logements, principaux indicateurs du dossier complet) via l'API Melodi.
_INSEE = "https://api.insee.fr/melodi/data/DS_RP_LOGEMENT_PRINC?GEO=COM-35238"
_SPR = "https://logement.metropole.rennes.fr/sites-patrimoniaux-remarquables/"
_PSMV_DIR = "https://public.sig.rennesmetropole.fr/ressources/donnees/urbanisme/psmv/35238/envigueur/"
_PSMV_RP = _PSMV_DIR + "1_Rapport_de_presentation_35238_rapport_1.pdf.zip"
_PSMV_REGL = _PSMV_DIR + "3_Reglement_Reglement_litteral.zip"
_PLUI = "https://logement.metropole.rennes.fr/documents-du-plui/"
_DEM = "https://logement.metropole.rennes.fr/demarches-urbanisme/"
_NRU = "https://logement.metropole.rennes.fr/rechercher-une-note-de-renseignements-urbanisme/"
_GUICHET = "https://demarchesurbanisme-rennesmetropole.pu.sirap.com/liste-communes"
_VOIRIE = "https://transport.metropole.rennes.fr/realiser-des-travaux-sur-la-voirie"
_UDAP = ("https://www.culture.gouv.fr/regions/drac-bretagne/politique-et-actions-culturelles/patrimoines/"
         "les-unites-departementales-de-l-architecture-et-du-patrimoine-udap-en-bretagne/"
         "unite-departementale-de-l-architecture-et-du-patrimoine-udap-d-ille-et-vilaine-35")
_ECOTRAVO = "https://logement.metropole.rennes.fr/ecotravo-vous-aide-a-renover-votre-logement/"
_ALEC = "https://www.alec-rennes.org/"
_MF = "https://donneespubliques.meteofrance.fr/FichesClim/FICHECLIM_35281001.pdf"
_SISM = "https://georisques.gouv.fr/api/v1/zonage_sismique?code_insee=35238"

CITY = dict(
    slug="rennes", name="Rennes", cp="35000", insee="35238",
    lat=48.1142, lon=-1.6808, dept="Ille-et-Vilaine", depcode="35", region="Bretagne",
    wiki="https://fr.wikipedia.org/wiki/Rennes", wikidata="Q647",
    verified="2026-11-21",
    tldr="À Rennes, le centre ancien est un secteur sauvegardé depuis 1966 : le PVC y est interdit, et les immeubles protégés gardent l’ardoise naturelle, sans isolation par l’extérieur",
    hook="Centre ancien protégé : ni PVC ni isolation par l’extérieur.",
    title="Devis travaux à Rennes : toiture, façade, fenêtres, isolation",
    desc="Travaux à Rennes : centre ancien en secteur sauvegardé, ardoise naturelle, PVC interdit, aides écoTravo jusqu’à 15 000 €. Un seul artisan vient chiffrer.",
    figures_intro="Ce qui compte avant de lancer des travaux dans la capitale bretonne.",
    figures=[("86,7 <small>%</small>", "des logements sont des appartements", S("Insee, 2023", _INSEE)),
             ("35,3 <small>%</small>", "des résidences principales datent d’avant 1971", S("Insee, 2023", _INSEE)),
             ("35 <small>ha</small>", "de secteur sauvegardé dans le centre ancien, créé en 1966", S("Ville de Rennes, PSMV", _PSMV_RP)),
             ("41,7 <small>jours</small>", "de rafales d’au moins 58 km/h par an à Rennes-Saint-Jacques", S("Météo-France, normales 1991-2020", _MF))],
    answer=("À Rennes, 86,7 % des logements sont des appartements et 35,3 % des résidences principales datent d’avant 1971. Dans les 35 hectares du "
            "centre ancien, l’architecte des Bâtiments de France donne son avis sur tous les travaux, et le plan de sauvegarde interdit le PVC et impose "
            "l’ardoise naturelle sur les immeubles protégés. Ailleurs, le PLUi de Rennes Métropole demande qu’un ravalement ou une réfection de toiture améliore de façon significative "
            "la performance énergétique."),
    facts=[("Centre ancien", "Secteur sauvegardé créé le 7 janvier 1966 sur 35 hectares, des quais Chateaubriand, Lamartine et Duguay-Trouin à la place "
                             "Sainte-Anne (" + L("rapport du PSMV", _PSMV_RP) + "). Son plan de sauvegarde, révisé le 16 décembre 2013 et modifié le 6 février "
                             "2024, remplace le PLUi dans ce périmètre, et l’architecte des Bâtiments de France y donne son avis sur tous les travaux ("
                             + L("Rennes Métropole", _SPR) + ")."),
           ("Menuiseries", "Dans le secteur sauvegardé, le PVC est interdit. Sur les immeubles protégés, la pose en « rénovation » sur l’ancien dormant l’est aussi ; dans les maisons "
                           "médiévales et les immeubles reconstruits après l’incendie de 1720, les vitrages multiples sont interdits tant que les fenêtres "
                           "anciennes sont réparables (" + L("règlement du PSMV", _PSMV_REGL) + ", 2024)."),
           ("Toitures", "Sur les immeubles protégés du secteur sauvegardé, ardoise naturelle de provenance locale, de 4 à 6 mm d’épaisseur ; ardoise artificielle, tôle et "
                        "fibrociment y sont interdits. Les fenêtres de toit ne dépassent pas 80 sur 100 cm, encastrées et sans volet roulant en saillie ("
                        + L("règlement du PSMV", _PSMV_REGL) + ")."),
           ("Urbanisme", "Le PLUi de Rennes Métropole, approuvé le 19 décembre 2019 pour 43 communes, a été modifié pour la dernière fois le 19 juin 2025 ; "
                         "ses annexes ont été mises à jour le 17 septembre 2026. Il exige qu’un ravalement ou une réfection de toiture améliore de façon "
                         "significative la performance énergétique (" + L("documents du PLUi", _PLUI) + ")."),
           ("Patrimoine bâti d’intérêt local", "Hors secteur sauvegardé, le PLUi classe des édifices de 1 à 3 étoiles. Pour un 3 étoiles, la conservation de "
                                                "tous les éléments de forte qualité patrimoniale est imposée, et tout travail sur un édifice repéré emploie "
                                                "des techniques et des matériaux traditionnels (" + L("PLUi", _PLUI) + ")."),
           ("Climat", "À Rennes-Saint-Jacques, 691 mm de pluie en 114,6 jours par an, et 41,7 jours de rafales d’au moins 58 km/h, surtout de décembre à "
                      "mars (" + L("Météo-France", _MF) + ", normales 1991-2020). Zone sismique 2, faible (" + L("Géorisques", _SISM) + ").")],
    trades_intro="À Rennes, les règles suivent l’époque : pans de bois médiévaux, immeubles de pierre reconstruits après 1720, maisons de schiste enduit.",
    trades={
        "toiture": ["Sur les immeubles protégés du secteur sauvegardé, la couverture est en ardoise naturelle de 4 à 6 mm, posée au clou sur les pentes fortes, avec un faîtage "
                    "en tuiles de terre cuite demi-rondes ou à lignolet. Gouttières et descentes sont en cuivre, en plomb ou en zinc prépatiné ("
                    + L("règlement du PSMV", _PSMV_REGL) + ").",
                    "Les panneaux solaires n’y sont admis que sur les verrières et les toitures terrasses. Avec 41,7 jours de rafales d’au moins 58 km/h "
                    "par an, surtout l’hiver, faites contrôler ardoises, crochets et solins avant décembre."],
        "facade": ["Sur les immeubles protégés du secteur sauvegardé, les enduits sont à la terre ou à la chaux et au sable, selon l’époque de l’immeuble, et les mortiers prêts à "
                   "l’emploi sont interdits. Les pans de bois apparents reçoivent une peinture perméante à la chaux ou à l’huile, sans enduit gratté ("
                   + L("règlement du PSMV", _PSMV_REGL) + ").",
                   "Hors espace protégé, un simple ravalement se fait sans autorisation à Rennes. Changer la couleur de la façade demande en revanche une "
                   "déclaration préalable (" + L("démarches d’urbanisme", _DEM) + "), et le PLUi demande que le ravalement améliore la performance énergétique."],
        "fenetres": ["Sur les immeubles protégés du secteur sauvegardé, les nouvelles menuiseries reprennent l’essence, les dimensions et les moulures d’origine ; les petits bois "
                     "collés sur le vitrage sont interdits. Noir, blanc, couleurs saturées et bois naturel sont exclus des teintes (" + L("règlement du PSMV", _PSMV_REGL) + ").",
                     "Ailleurs, remplacer une fenêtre par un modèle différent demande une déclaration préalable. En copropriété, écoTravo finance 20 % du "
                     "montant hors taxes du remplacement des menuiseries d’origine (" + L("écoTravo", _ECOTRAVO) + ")."],
        "charpente": ["Sur les immeubles protégés du centre ancien, charpentes, escaliers, planchers et galeries sont conservés, restaurés ou restitués selon les témoins en "
                      "place. La création d’une trémie doit suivre la technique de la charpente existante et rester réversible (" + L("règlement du PSMV", _PSMV_REGL) + ").",
                      "Les doublages intérieurs y sont interdits dans les immeubles en pierre ou à pans de bois, sauf sous les rampants de toiture et dans les pièces d’eau. Lors d’une "
                      "campagne de travaux, leur dépose peut être imposée pour vérifier l’état des structures."],
        "isolation": ["Sur les immeubles protégés du secteur sauvegardé, aucune isolation par l’extérieur n’est admise : seuls des matériaux perméants "
                      "posés à l’intérieur. Sur les autres immeubles du centre, elle est interdite sur les façades sur rue à modénatures et possible en "
                      "cœur d’îlot, sur une façade sans modénature (" + L("règlement du PSMV", _PSMV_REGL) + ").",
                      "Hors centre ancien, le PLUi autorise l’isolation extérieure au-delà des reculs, 0,50 m de hauteur en plus et un débord sur le "
                      "trottoir s’il reste praticable (" + L("PLUi", _PLUI) + "). Pour une maison de plus de 15 ans portée au niveau BBC Rénovation, écoTravo verse jusqu’à 15 000 € ("
                      + L("écoTravo", _ECOTRAVO) + ")."]},
    steps_intro="Dans l’ordre, de la note d’urbanisme au conseil écoTravo.",
    steps=[("Vérifiez les règles de votre adresse", "Centre ancien, abords d’un monument historique, édifice à étoiles du PLUi : la note de "
                                                 "renseignements d’urbanisme, en ligne, indique les règles de votre terrain (" + L("Rennes Métropole", _NRU) + ")."),
           ("Consultez l’architecte des Bâtiments de France", "UDAP d’Ille-et-Vilaine, hôtel de Blossac, 6 rue du Chapitre, 35044 Rennes cedex. "
                                                            "02 99 29 67 60, du lundi au jeudi de 9 h à 12 h (" + L("ministère de la Culture", _UDAP) + ")."),
           ("Déposez la déclaration préalable", "En ligne sur le " + L("portail urbanisme", _GUICHET) + " de Rennes Métropole, ou sur papier au service "
                                                "Droit des sols, hôtel de Rennes Métropole, 4 avenue Henri-Fréville. 02 23 62 23 56, du lundi au vendredi "
                                                "de 13 h 30 à 16 h 30 jusqu’au 31 décembre 2026 (" + L("démarches", _DEM) + ")."),
           ("Faites autoriser l’échafaudage", "Envoyez le formulaire d’occupation temporaire du domaine public à dvgts@rennesmetropole.fr. Une redevance "
                                              "s’applique ; si la circulation change, demandez aussi un arrêté temporaire (" + L("Rennes Métropole", _VOIRIE) + ")."),
           ("Appelez écoTravo", "Conseil gratuit sur les travaux et les aides, avant de choisir le programme de travaux.")],
    aides_intro="Le conseil public est gratuit, et écoTravo vous suit du début à la fin du projet.",
    aides=[("écoTravo", "L’Espace Conseil France Rénov’ de Rennes Métropole, avec l’Alec du Pays de Rennes : 104 boulevard Georges-Clemenceau, 35200 Rennes. "
                        "08 00 00 03 53. Copropriétés : 02 99 35 15 15. " + L("alec-rennes.org", _ALEC) + "."),
           ("écoTravo, maisons individuelles", "Pour une maison de plus de 15 ans en résidence principale, portée au niveau BBC Rénovation : jusqu’à 15 000 € "
                                               "pour les ménages éligibles à l’Anah, jusqu’à 8 000 € pour les ménages intermédiaires (" + L("Rennes Métropole", _ECOTRAVO) + ", 2026)."),
           ("écoTravo, copropriétés", "Immeubles construits avant 1990, visant le niveau BBC Rénovation : 3 500 € par lot principal, 1 500 € de plus en "
                                      "quartier prioritaire, 20 % des menuiseries d’origine remplacées, la moitié de l’audit (100 € par lot au plus) et de la "
                                      "maîtrise d’œuvre (500 € par lot au plus) (" + L("Rennes Métropole", _ECOTRAVO) + ")."),
           ("Programme Anah et Rennes Métropole 2026-2029", "Pour les ménages aux ressources limitées et les bailleurs à loyers plafonnés : visite-diagnostic "
                                                            "et montage des dossiers par le bureau d’études Urbanis, missionné par la Métropole. Premier "
                                                            "contact : l’Alec (" + L("Rennes Métropole", _ECOTRAVO) + ")."),
           NATIONAL],
    faq=[("Faut-il une autorisation pour un ravalement à Rennes ?",
          "Hors espace protégé, un simple ravalement se fait sans autorisation ; changer la couleur de la façade demande une déclaration préalable. Dans le "
          "centre ancien ou aux abords d’un monument historique, une déclaration est exigée et l’architecte des Bâtiments de France donne son avis."),
         ("Peut-on poser des fenêtres en PVC à Rennes ?",
          "Pas dans le secteur sauvegardé du centre ancien, où le plan de sauvegarde interdit le PVC ; sur les immeubles protégés, la pose en rénovation et "
          "les petits bois collés sont aussi interdits. Ailleurs, "
          "remplacer une fenêtre par un modèle différent demande une déclaration préalable."),
         ("Peut-on isoler par l’extérieur dans le centre de Rennes ?",
          "Non sur les immeubles protégés du secteur sauvegardé, ni sur les façades sur rue à modénatures. C’est possible en cœur d’îlot, sur une façade sans "
          "modénature. Hors centre ancien, le PLUi admet un débord sur le trottoir s’il reste praticable pour les personnes à mobilité réduite."),
         ("Quelle ardoise pour un toit dans le centre de Rennes ?",
          "Sur un immeuble protégé du secteur sauvegardé, de l’ardoise naturelle de provenance locale, de 4 à 6 mm d’épaisseur, en petit module 15 sur 25 ou 18 sur 27 selon la pente. Ardoise artificielle, "
          "tôle et fibrociment y sont interdits."),
         ("Quelles aides pour rénover sa maison à Rennes ?",
          "écoTravo verse jusqu’à 15 000 € aux ménages éligibles à l’Anah et jusqu’à 8 000 € aux ménages intermédiaires, pour une maison de plus de 15 ans "
          "portée au niveau BBC Rénovation. S’y ajoutent les aides nationales. Conseil gratuit : 08 00 00 03 53."),
         ("Comment déposer une déclaration préalable à Rennes ?",
          "En ligne sur le portail urbanisme de Rennes Métropole, ou sur papier au service Droit des sols, 4 avenue Henri-Fréville (02 23 62 23 56).")],
)

from villes_data import L, S, SP, NATIONAL  # liens dans le texte, sources discrètes, Service-Public, aides nationales

# Sources consultées le 21/11/2026.
_INSEE = "https://api.insee.fr/melodi/data/DS_RP_LOGEMENT_PRINC?GEO=COM-63113"  # dossier complet, RP 2023 (page insee.fr en erreur 500 ce jour)
_MERIMEE = "https://pop.culture.gouv.fr/notice/merimee/SPR8400115"
_SPR_CENTRE = "https://clermont-ferrand.fr/site-patrimonial-remarquable-du-centre-historique-de-clermont-ferrand"
_SPR_ARRETE = "https://aida.ineris.fr/reglementation/arrete-210725-portant-classement-site-patrimonial-remarquable-clermont-ferrand-puy"
_MONTF = "https://clermont-ferrand.fr/site-patrimonial-remarquable-de-montferrand"
_PSMV = "https://plu.clermontmetropole.eu/wp-content/uploads/2026/01/6.1.3.7_Reglement-annexes-PSMV.pdf"  # règlement du PSMV de Montferrand, modification n° 1
_PLUI_HIST = "https://plu.clermontmetropole.eu/historique-de-la-demarche/"
_PLUI_REGL = "https://plu.clermontmetropole.eu/wp-content/uploads/2026/01/4.1_REGLEMENT_approbation.pdf"
_GUIDE = "https://plu.clermontmetropole.eu/wp-content/uploads/2026/02/guide-utilisation-PLUi-ClermontAuvergneMetropole-fev2026.pdf"
_CAHIER = "https://plu.clermontmetropole.eu/wp-content/uploads/2026/01/4.2_CAHIERS-COMMUNAUX_CLERMONT-FERRAND_approbation.pdf"
_RIOM = "https://www.ville-riom.fr/wp-content/uploads/2025/05/Ravalement_de_fac__ade_-_6.pdf"
_PPRI = "https://plu.clermontmetropole.eu/wp-content/uploads/2026/01/6.1.2_PPRNPI-DE-L-AGGLOMERATION-CLERMONTOISE_reglement.pdf"
_RADON = "https://georisques.gouv.fr/api/v1/radon?code_insee=63113"
_SISM = "https://georisques.gouv.fr/api/v1/zonage_sismique?code_insee=63113"
_CATNAT = "https://georisques.gouv.fr/api/v1/gaspar/catnat?code_insee=63113&page_size=100"
_ARS = "https://www.auvergne-rhone-alpes.ars.sante.fr/le-radon-0"
_MF = "https://donneespubliques.meteofrance.fr/FichesClim/FICHECLIM_63113001.pdf"
_UDAP = ("https://www.culture.gouv.fr/fr/regions/drac-auvergne-rhone-alpes/architecture-et-patrimoines/unites-departementales-"
         "de-l-architecture-et-du-patrimoine-udap-d-auvergne-rhone-alpes/unite-departementale-de-l-architecture-et-du-patrimoine-"
         "udap-du-puy-de-dome-63")
_ODP = "https://clermont-ferrand.fr/travaux-et-stationnement"
_RA = "https://www.renovactions63.fr/"
_RA_RADON = "https://www.renovactions63.fr/actualites/qualite-de-lair-interieur-renovactions63-vous-offre-un-kit-de-mesure-du-radon/"
_RA_MPR = "https://www.renovactions63.fr/actualites/reouverture-du-guichet-des-aides-et-actualites/"
_ADIL = "https://www.anil.org/adil-63/"
_CAM_AIDE = ("https://www.anil.org/aides-locales-travaux/details/"
             "puy-de-dome-aide-travaux-deconomie-denergie-proprietaires-occupants-tres-modestes-cam-4021/")

CITY = dict(
    slug="clermont-ferrand", name="Clermont-Ferrand", cp="63000", insee="63113",
    lat=45.7759, lon=3.0823, dept="Puy-de-Dôme", depcode="63", region="Auvergne-Rhône-Alpes",
    wiki="https://fr.wikipedia.org/wiki/Clermont-Ferrand", wikidata="Q42168",
    verified="2026-11-21",
    tldr=("À Clermont-Ferrand, le centre historique est site patrimonial remarquable depuis juillet 2025, Montferrand suit "
          "son propre plan de sauvegarde, et les encadrements en pierre de Volvic se conservent"),
    hook="Centre classé en 2025, Montferrand protégé, pierre de Volvic.",
    title="Devis travaux à Clermont-Ferrand : toiture, façade, fenêtres, isolation",
    desc=("Travaux à Clermont-Ferrand : centre classé en 2025, Montferrand protégé, pierre de Volvic, radon, aides de la "
          "Métropole. Un seul artisan vient chiffrer."),
    figures_intro="Le parc clermontois en quatre chiffres, entre immeubles anciens et hivers longs.",
    figures=[("82,2 <small>%</small>", "des logements sont des appartements", S("Insee, 2023", _INSEE)),
             ("41,9 <small>%</small>", "des résidences principales datent d’avant 1971", S("Insee, 2023", _INSEE)),
             ("55,7 <small>jours</small>", "de gel par an, à la station de Clermont-Ferrand", S("Météo-France, 1991-2020", _MF)),
             ("2025", "classement du centre historique en site patrimonial remarquable", S("Ville de Clermont-Ferrand", _SPR_CENTRE))],
    answer=("À Clermont-Ferrand, 82,2 % des logements sont des appartements et 41,9 % des résidences principales datent d’avant "
            "1971. Le centre historique est site patrimonial remarquable depuis le 21 juillet 2025, et Montferrand suit son plan de "
            "sauvegarde. Ailleurs, le PLU de la Métropole, en vigueur depuis le 20 janvier 2026, impose de conserver les encadrements "
            "en pierre de Volvic des quartiers anciens."),
    facts=[("Centre historique", "Classé site patrimonial remarquable par arrêté du 21 juillet 2025, publié au Journal officiel du "
                                 "26 juillet (" + L("arrêté", _SPR_ARRETE) + "). Son plan de valorisation de l’architecture et du "
                                 "patrimoine est en préparation. Renseignements : spr@clermontmetropole.eu ("
                                 + L("Ville de Clermont-Ferrand", _SPR_CENTRE) + ")."),
           ("Montferrand", "Secteur sauvegardé depuis 1964 (" + L("ministère de la Culture", _MERIMEE) + "), dont le périmètre suit "
                           "les anciens remparts (" + L("Ville de Clermont-Ferrand", _MONTF) + "). Son plan de sauvegarde, approuvé "
                           "le 28 novembre 1997, remplace le PLU, et l’architecte des Bâtiments de France est compétent sur toutes "
                           "les demandes d’autorisation (" + L("règlement du PSMV", _PSMV) + ")."),
           ("Urbanisme", "Le PLU de la Métropole, approuvé le 19 décembre 2025, s’applique depuis le 20 janvier 2026 ("
                         + L("Métropole", _PLUI_HIST) + "). En zone urbaine, refaire un toit, changer des fenêtres, ravaler une "
                         "façade ou l’isoler par l’extérieur demande une déclaration préalable (" + L("guide du PLU", _GUIDE)
                         + ", 2026)."),
           ("Ravalement", "Clermont-Ferrand figure sur la liste préfectorale des villes où le ravalement est obligatoire tous les "
                          "10 ans, rappelle la Ville de Riom, ajoutée à cette liste par arrêté du 22 octobre 2003 ("
                          + L("Ville de Riom", _RIOM) + ")."),
           ("Risques", "Classe 3 de potentiel radon (" + L("Géorisques", _RADON) + ") et zone de sismicité 3, modérée ("
                       + L("Géorisques", _SISM) + "). De 1989 à 2023, 9 épisodes de sécheresse y ont été reconnus en catastrophe "
                       "naturelle (" + L("Géorisques", _CATNAT) + "). Le long du Bec, de l’Artière, de la Tiretaine et du Bédat, "
                       "un plan de prévention du risque d’inondation s’applique (" + L("règlement", _PPRI) + ")."),
           ("Climat", "À la station de Clermont-Ferrand : 55,7 jours de gel, 17,7 jours de neige et 49 jours de rafales d’au moins "
                      "58 km/h par an. Record de vent : 44 m/s, soit 158 km/h, le 27 décembre 1999 (" + L("Météo-France", _MF)
                      + ", normales 1991-2020).")],
    trades_intro=("Immeubles anciens du centre, maisons de Montferrand, cités-jardins : à Clermont-Ferrand, chaque secteur a ses "
                  "règles d’aspect, et la pierre de Volvic y tient une place à part."),
    trades={
        "toiture": ["Dans les quartiers anciens, en zone UC du PLU de la Métropole, les toits en pente gardent l’aspect des toitures "
                    "traditionnelles, en tuile canal ou romane de couleur rouge. Sur un bâtiment existant, les panneaux solaires "
                    "couvrent au plus 75 % du pan de toiture, pour laisser voir le toit d’origine (" + L("règlement du PLU", _PLUI_REGL)
                    + ").",
                    "À Montferrand, les toits à faible pente se restaurent en tuiles creuses de teinte rouge, sans matériau vieilli "
                    "ou coloré artificiellement. Zinc, plomb, tuile plate ou ardoise sont réservés aux pentes plus fortes ("
                    + L("règlement du PSMV", _PSMV) + "). Avec 17,7 jours de neige et 49 jours de rafales d’au moins 58 km/h par an, "
                    "faites vérifier tuiles et faîtages après l’hiver."],
        "facade": ["À Montferrand, la pierre de taille reste apparente, sans badigeon ni peinture, avec des joints à plat au mortier "
                   "de chaux. Les enduits se font au mortier de chaux, grattés à la truelle, sans blanc, sans teinte vive ni ciment "
                   "gris, après approbation d’un échantillon par l’architecte des Bâtiments de France (" + L("règlement du PSMV", _PSMV) + ").",
                   "Dans les quartiers anciens, le PLU peut imposer de conserver chaînages d’angle et encadrements en pierre de taille, "
                   "corniches, bandeaux et génoises. Les enduits y sont finement talochés ou grattés, et la réfection peut devoir "
                   "reprendre l’aspect existant (" + L("règlement du PLU", _PLUI_REGL) + ")."],
        "fenetres": ["Dans les quartiers anciens, le PLU de la Métropole impose de conserver les encadrements en pierre de Volvic, sauf "
                     "justification technique avérée. Sur une construction d’avant 1950, le coffre d’un volet roulant se pose à l’intérieur ou derrière un "
                     "lambrequin, invisible depuis la rue (" + L("règlement du PLU", _PLUI_REGL) + ").",
                     "À Montferrand, volets métalliques et jalousies « accordéon » sont interdits. Seuls sont admis les volets "
                     "traditionnels en bois et les volets roulants entièrement dissimulés une fois ouverts. Vernis et teintures sur "
                     "le bois y sont aussi interdits (" + L("règlement du PSMV", _PSMV) + ")."],
        "charpente": ["Clermont-Ferrand est en zone de sismicité 3, modérée : signalez-le à l’artisan avant une surélévation ou une "
                      "reprise de charpente. À Montferrand, escaliers et galeries en bois se traitent avec des produits qui gardent "
                      "leur aspect naturel, et les remplissages de pans de bois sont enduits (" + L("règlement du PSMV", _PSMV) + ").",
                      "La ville compte 17 cités-jardins classées en secteur UGcj, comme La Plaine, Chanturgue ou L’Oradou : toute "
                      "transformation y respecte le caractère d’origine du bâti. À la cité de la rue Georges-Méliès, une réfection "
                      "de toiture reprend la même forme et les mêmes matériaux (" + L("cahier communal du PLU", _CAHIER) + ")."],
        "isolation": ["La station de Clermont-Ferrand compte 2 403,9 degrés-jours unifiés de chauffage par an, et 55,7 jours de gel ("
                      + L("Météo-France", _MF) + ", 1991-2020). Dans les quartiers anciens, le PLU autorise l’isolation par "
                      "l’extérieur quand les murs isolent mal, notamment en pierre traditionnelle, si le parement garde l’aspect "
                      "d’origine et si les murs continuent de respirer (" + L("règlement du PLU", _PLUI_REGL) + ").",
                      "La commune est en classe 3 de potentiel radon. Une rénovation énergétique sans approche globale peut dégrader "
                      "l’air intérieur, prévient l’ARS : prévoyez la ventilation en même temps que l’isolation. Mesurez sur 2 mois, "
                      "en période de chauffage, dans les pièces de vie (" + L("ARS Auvergne-Rhône-Alpes", _ARS) + ", 2026)."]},
    steps_intro="Dans l’ordre, du centre historique aux cités-jardins.",
    steps=[("Vérifiez si vous êtes en secteur protégé", "Centre historique ou Montferrand : l’architecte des Bâtiments de France se "
                                                        "prononce sur le projet. UDAP du Puy-de-Dôme, Hôtel de Chazerat, 4 rue "
                                                        "Pascal, accueil de 9 h à 12 h. 04 73 41 27 27 (" + L("UDAP 63", _UDAP) + ")."),
           ("Repérez votre zone au PLU", "Quartier ancien en zone UC, cité-jardin en secteur UGcj : chaque zone a ses règles d’aspect. "
                                         "Pour une question complexe, Direction de l’urbanisme de la Métropole, 64 avenue de "
                                         "l’Union-Soviétique. 04 73 98 34 00 (" + L("guide du PLU", _GUIDE) + ")."),
           ("Déposez la déclaration préalable", "Sur le guichet unique de la Métropole, urbanisme.clermontmetropole.eu, ou en mairie ("
                                                + L("guide du PLU", _GUIDE) + "). En secteur protégé, l’instruction prend 2 mois au "
                                                "lieu d’un (" + L("Service-Public", SP + "F17578") + ")."),
           ("Faites autoriser l’emprise du chantier", "Demande d’arrêté en ligne sur la plateforme ICI Clermont, rubrique des travaux "
                                                      "sur l’espace public. Le Pôle Arrêté compte 10 jours ouvrés de traitement, et "
                                                      "l’occupation donne lieu à une redevance (" + L("démarche", _ODP) + ")."),
           ("Appelez Rénov’actions63 avant de signer", "Conseil gratuit, du mardi au vendredi. Pour une rénovation d’ampleur, ce "
                                                       "rendez-vous France Rénov’ est obligatoire avant de demander MaPrimeRénov’ ("
                                                       + L("Rénov’actions63", _RA_MPR) + ").")],
    aides_intro="Les aides se demandent avant de signer le devis, et le conseil public est gratuit.",
    aides=[("Rénov’actions63", "Le service public de la rénovation de l’habitat du Puy-de-Dôme, porté par le Département, les 14 "
                              "intercommunalités et l’Anah dans le cadre de France Rénov’ : conseil gratuit, du mardi au vendredi, "
                              "de 8 h 30 à 12 h et de 13 h à 17 h 30. 04 73 42 30 72. Permanences sur rendez-vous dans plusieurs "
                              "communes de la Métropole. " + L("renovactions63.fr", _RA) + ". L’ADIL 63 conseille aussi sur le "
                              "logement, à la Maison de l’Habitat, 129 avenue de la République, 63100 Clermont-Ferrand : "
                              "04 73 42 30 75 (" + L("ADIL 63", _ADIL) + ")."),
           ("Aide de la Métropole aux économies d’énergie", "Pour les propriétaires occupants très modestes, sous plafonds de l’Anah : "
                                                           "10 % de la dépense éligible, jusqu’à 1 500 €, pour un logement de plus de "
                                                           "15 ans, avec un artisan RGE et en complément obligatoire des aides de "
                                                           "l’Anah (" + L("ANIL", _CAM_AIDE) + ", 2025)."),
           ("Dosimètre radon offert", "Rénov’actions63 offre un dosimètre pour mesurer le radon chez vous, à retirer sur rendez-vous "
                                      "à partir du 9 novembre 2026, dans la limite des stocks (" + L("Rénov’actions63", _RA_RADON)
                                      + ", 2026)."),
           NATIONAL],
    faq=[("Le ravalement est-il obligatoire à Clermont-Ferrand ?",
          "Clermont-Ferrand figure sur la liste préfectorale des villes où le ravalement est obligatoire tous les 10 ans. En zone "
          "urbaine, un ravalement demande une déclaration préalable, et à Montferrand l’architecte des Bâtiments de France approuve "
          "d’abord un échantillon d’enduit."),
         ("Faut-il une autorisation pour changer ses fenêtres à Clermont-Ferrand ?",
          "Oui, une déclaration préalable. Dans les quartiers anciens, les encadrements en pierre de Volvic se conservent, et sur une "
          "construction d’avant 1950 le coffre de volet roulant reste invisible depuis la rue. À Montferrand, les volets métalliques "
          "sont interdits."),
         ("Quelles règles dans le centre historique de Clermont-Ferrand ?",
          "Il est site patrimonial remarquable depuis le 21 juillet 2025, et son plan de valorisation est en préparation. "
          "L’architecte des Bâtiments de France se prononce sur les travaux, et une déclaration préalable y demande 2 mois "
          "d’instruction."),
         ("Quelles tuiles pour un toit à Montferrand ?",
          "Des tuiles creuses de teinte rouge pour les toits à faible pente, sans tuile vieillie ou colorée artificiellement. Zinc, "
          "plomb, tuile plate ou ardoise restent possibles sur les pentes plus fortes."),
         ("Clermont-Ferrand est-elle concernée par le radon ?",
          "Oui, la commune est en classe 3 de potentiel radon. Mesurez sur 2 mois en période de chauffage : Rénov’actions63 offre un "
          "dosimètre sur rendez-vous. Au-delà de 300 Bq/m³, l’ARS recommande d’agir, et une isolation doit aller avec une bonne "
          "ventilation."),
         ("Quelles aides pour rénover son logement à Clermont-Ferrand ?",
          "La Métropole ajoute 10 % de la dépense, jusqu’à 1 500 €, aux aides de l’Anah pour les propriétaires occupants très "
          "modestes. Conseil gratuit chez Rénov’actions63 : 04 73 42 30 72.")],
)

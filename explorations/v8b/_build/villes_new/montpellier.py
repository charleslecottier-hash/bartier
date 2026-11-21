# Montpellier : fiche locale de la page « Devis travaux à Montpellier ». Sources officielles consultées le 21/11/2026.
# Chiffres Insee : jeu « Logements, principaux indicateurs (dossier complet) », RP 2023, lu via l'API Melodi
# (la page « dossier complet » d'insee.fr répondait en erreur 500 pendant la recherche).
from villes_data import L, S, SP, NATIONAL  # liens dans le texte, sources discrètes, Service-Public, aides nationales

_INSEE = "https://api.insee.fr/melodi/data/DS_RP_LOGEMENT_PRINC?GEO=COM-34172"
_PSMV = "https://montpellier.fr/sites/default/files/2025-01/Guide-du-PSMV-secteur-sauvegarde-%20%281%29.pdf"
_CV = "https://www.montpellier.fr/vie-quotidienne/vivre-ici/construire-renover/realiser-des-travaux-en-centre-ville-de-montpellier"
_RAV = "https://www.montpellier.fr/sites/default/files/2025-01/Reglement-attributif-subvention-ravalement-de-facades-2022-2026.pdf"
_PROC = "https://www.montpellier.fr/sites/default/files/2026-02/Proc%C3%A9dure%20demande%20de%20subvention%20ravalement%20Celleneuve.pdf"
_CPG = "https://www.montpellier.fr/sites/default/files/2026-07/Cahier%20de%20prescriptions%20g%C3%A9n%C3%A9rales%20ravalement.pdf"
_PLUI = "https://encommun.montpellier.fr/articles/2025-07-17-conseil-de-metropole-du-16-juillet-le-plui-climat-est-adopte"
_TERM = ("https://www.herault.gouv.fr/Actions-de-l-Etat/Amenagement-du-territoire-construction-et-logement/Qualite-des-batiments/"
         "Information-Termites-et-Merules")
_DREAL = "https://www.occitanie.developpement-durable.gouv.fr/IMG/pdf/603-3-_termites_-_modif_sept_2023.pdf"
_MF = "https://donneespubliques.meteofrance.fr/FichesClim/FICHECLIM_34154001.pdf"
_DICRIM = "https://encommun.montpellier.fr/sites/default/files/articles/2026-09/dicrim.pdf"
_UDAP = ("https://www.culture.gouv.fr/regions/drac-occitanie/la-direction-regionale-des-affaires-culturelles-drac-occitanie/patrimoines-et-architecture/"
         "espaces-proteges-les-unites-departementales-de-l-architecture-et-du-patrimoine-udap-d-occitanie/udap-34")
_UDAP_FICHE = "https://www.culture.gouv.fr/Media/medias-creation-rapide/les-menuiseries-en-centre-ancien-guide-des-couleurs"
_DUA = "https://www.montpellier.fr/vie-quotidienne/vivre-ici/construire-renover/demande-d-autorisation-urbanisme"
_GNAU = "https://gnau32.operis.fr/montpellier/gnau/#/"
_ALEC = "https://alec-montpellier.org/contact/"
_ALEC_AIDES = ("https://antigonedesassociations.montpellier.fr/sites/default/files/documents_telecharges/"
               "aides_et_eligibilite_synthese_2026-alec_mtp_04_26.pdf")
_PC = "https://www.montpellier.fr/sites/default/files/2025-06/ReglementAidePlanClimat2025.pdf"
_PIG = ("https://www.montpellier.fr/vie-quotidienne/vivre-ici/construire/renover/renover-son-logement/"
        "aides-a-la-renovation-pour-un-habitat-durable-et-solidaire")
_DISPO = "https://www.montpellier.fr/actions/competences/acces-au-logement/dispositifs-daide-la-renovation"

CITY = dict(
    slug="montpellier", name="Montpellier", cp="34000", insee="34172",
    lat=43.6109, lon=3.8772, dept="Hérault", depcode="34", region="Occitanie",
    wiki="https://fr.wikipedia.org/wiki/Montpellier", wikidata="Q6441",
    verified="2026-11-21",
    tldr=("À Montpellier, l’Écusson est un secteur sauvegardé où même les travaux intérieurs passent par l’architecte des Bâtiments de France, "
          "et tout l’Hérault est en zone termites"),
    hook="Écusson sauvegardé, ravalement imposé par quartier, Hérault termité.",
    title="Devis travaux à Montpellier : toiture, façade, fenêtres, isolation",
    desc=("Travaux à Montpellier : Écusson sauvegardé, ravalement imposé par quartier, zone termites, pluies d’automne, aide plan climat. "
          "Un seul artisan vient chiffrer."),
    figures_intro="L’essentiel en chiffres, de l’Écusson aux quartiers récents.",
    figures=[("87,0 <small>%</small>", "des logements sont des appartements", S("Insee, 2023", _INSEE)),
             ("30,6 <small>%</small>", "des résidences principales sont occupées par leur propriétaire", S("Insee, 2023", _INSEE)),
             ("96 <small>ha</small>", "de secteur sauvegardé autour de l’Écusson", S("Ville de Montpellier", _PSMV)),
             ("299,5 <small>mm</small>", "de pluie en un jour, le 29 septembre 2014", S("Météo-France", _MF))],
    answer=("À Montpellier, 87,0 % des logements sont des appartements, et moins d’un tiers des résidences principales datent d’avant 1971. "
            "Dans l’Écusson, secteur sauvegardé de 96 hectares, tout projet, même intérieur, passe par l’avis conforme de l’architecte des "
            "Bâtiments de France. Ailleurs, la Ville peut imposer le ravalement par quartier, et tout l’Hérault est en zone termites depuis 2001."),
    facts=[("Ravalement", "Montpellier est sur la liste préfectorale des communes qui peuvent imposer le ravalement : le conseil municipal "
                          "en fixe les périmètres, comme à Celleneuve (" + L("règlement de 2022", _RAV) + "). Les aides propres au "
                          "ravalement sont actuellement suspendues (" + L("Ville de Montpellier", _CV) + ")."),
           ("Écusson", "Secteur sauvegardé créé en 1967, étendu en 1981 et en 2001 : 96 hectares et 2 182 parcelles. Toute construction, "
                       "démolition ou modification, même intérieure, y est soumise à autorisation avec l’avis conforme de l’architecte des "
                       "Bâtiments de France (" + L("guide du PSMV", _PSMV) + ")."),
           ("Urbanisme", "Le PLUi Climat des 31 communes de la Métropole a été adopté le 16 juillet 2025 (" + L("En Commun", _PLUI) + "). "
                         "Autour de l’Écusson, des AVAP protègent les faubourgs (" + L("Ville de Montpellier", _CV) + ")."),
           ("Termites", "Tout le département de l’Hérault est déclaré termité depuis l’arrêté préfectoral du 20 juin 2001. Aucun arrêté ne "
                        "vise la mérule (" + L("préfecture de l’Hérault", _TERM) + ")."),
           ("Pluie et vent", "639,2 mm de pluie par an à Montpellier-aéroport, dont plus de 40 % de septembre à novembre, et des rafales à "
                             "58 km/h ou plus 69,2 jours par an (" + L("Météo-France", _MF) + ", normales 1991-2020). La Ville compte en moyenne "
                             "5 à 10 épisodes d’inondation par an (" + L("DICRIM", _DICRIM) + ", 2026)."),
           ("Séisme et sols", "Sismicité faible : les règles parasismiques ne visent que les bâtiments stratégiques, comme les hôpitaux. "
                              "Le retrait-gonflement des argiles revient avec les variations climatiques et peut fissurer les façades ("
                              + L("DICRIM", _DICRIM) + ").")],
    trades_intro="De l’Écusson médiéval aux faubourgs du XIXe siècle, chaque secteur a ses règles de façade et de toiture.",
    trades={
        "toiture": ["Dans les faubourgs, les toits anciens se terminent par une génoise en terre cuite, une corniche en pierre ou un avant-toit en bois. Dans ses "
                    "prescriptions de ravalement, la Ville demande des gouttières en zinc ou en cuivre, non peintes, et proscrit "
                    "le PVC pour les gouttières comme pour les descentes (" + L("cahier de prescriptions", _CPG) + ").",
                    "Le 29 septembre 2014, 299,5 mm de pluie sont tombés en un jour à l’aéroport (" + L("Météo-France", _MF) + "). "
                    "En mars 2017, des rafales jusqu’à 120 km/h ont fait de nombreux dégâts (" + L("DICRIM", _DICRIM) + "). Faites revoir "
                    "tuiles, faîtage et chéneaux avant l’automne."],
        "facade": ["Dans l’Écusson, les murs alternent pierres taillées et pierres posées sur chant : c’est l’« appareil de Montpellier ». "
                   "Chacun des 2 200 immeubles a sa fiche de prescriptions, et l’avis de l’architecte des Bâtiments de France s’impose ("
                   + L("guide du PSMV", _PSMV) + ").",
                   "Dans ses prescriptions de ravalement, la Ville demande des joints et des enduits au mortier de chaux, un enduit neuf en trois couches et "
                   "des badigeons de chaux aux pigments naturels (" + L("cahier de prescriptions", _CPG) + "). Les teintes se valident "
                   "sur rendez-vous avec la Mission Grand Cœur, dans son nuancier (" + L("Ville de Montpellier", _PROC) + ")."],
        "fenetres": ["L’architecte des Bâtiments de France de l’Hérault préconise le bois pour les menuiseries des centres anciens. Il "
                     "déconseille le blanc et le gris anthracite RAL 7016, teintes industrielles (" + L("fiche UDAP 34", _UDAP_FICHE) + ").",
                     "Dans l’Écusson, les coffres de volets roulants en saillie sont à supprimer et les climatiseurs à intégrer, par exemple "
                     "derrière une imposte à ventelles en bois (" + L("guide du PSMV", _PSMV) + "). Dans les campagnes de ravalement, une "
                     "fenêtre neuve reprend le modèle ancien et se pose en retrait du nu de la façade (" + L("cahier de prescriptions", _CPG) + ")."],
        "charpente": ["Tout l’Hérault est en zone termites depuis l’arrêté préfectoral du 20 juin 2001 (" + L("préfecture", _TERM) + "). "
                      "Une infestation se déclare en mairie dans le mois qui suit sa découverte, et les bois contaminés retirés d’un chantier sont brûlés "
                      "sur place ou traités avant transport (" + L("DREAL Occitanie", _DREAL) + ").",
                      "Dans l’Écusson, l’étude du plan de sauvegarde a recensé 298 rez-de-chaussée voûtés et des maisons médiévales. Reprendre "
                      "un plancher ou une charpente y demande une autorisation, avec l’avis conforme de l’architecte des Bâtiments de France, "
                      "comme tous les travaux intérieurs (" + L("guide du PSMV", _PSMV) + ")."],
        "isolation": ["La Métropole complète MaPrimeRénov’ Parcours accompagné par son aide « plan climat » : 1 300 € par logement pour les "
                      "ménages très modestes, si les travaux font gagner au moins 40 % d’énergie dans un logement livré avant 2007 ("
                      + L("règlement 2025", _PC) + ").",
                      "À l’aéroport, 34,3 jours par an dépassent 30 °C et il gèle 21,4 jours par an (" + L("Météo-France", _MF) + "). Pour les "
                      "propriétaires occupants modestes ou très modestes, l’étude énergétique est gratuite dans le programme d’intérêt général "
                      "de la Métropole, avec Urbanis : 04 67 64 70 72 (" + L("ALEC", _ALEC_AIDES) + ", 2026)."]},
    steps_intro="Cinq étapes, à franchir avant de signer le devis.",
    steps=[("Vérifiez si votre immeuble est protégé", "Écusson, faubourgs en AVAP, abords d’un monument : l’architecte des Bâtiments de France "
                                                     "donne son avis. L’UDAP 34 propose une consultation en ligne avant le dépôt du dossier. "
                                                     "04 67 02 32 00 (" + L("UDAP 34", _UDAP) + ")."),
           ("Passez par la Mission Grand Cœur", "Pour une façade du centre ou d’un secteur de ravalement : conseil technique, nuancier et "
                                                "validation des teintes. 17 boulevard du Jeu-de-Paume. 04 34 88 79 40 ("
                                                + L("Ville de Montpellier", _PROC) + ")."),
           ("Déposez la déclaration préalable", "En ligne sur le " + L("guichet numérique", _GNAU) + ", ou à la direction de l’urbanisme "
                                                "appliqué, Hôtel de Métropole, 50 place Zeus, de 8 h 30 à 12 h et de 13 h 30 à 17 h. "
                                                "04 67 34 74 55 (" + L("démarche", _DUA) + ")."),
           ("Faites autoriser l’échafaudage", "La demande d’occupation du domaine public se fait en ligne, auprès de la cellule chantier de "
                                              "la direction des usages et de la valorisation de l’espace public. L’entreprise peut la déposer "
                                              "pour vous (" + L("Ville de Montpellier", _PROC) + ")."),
           ("Appelez l’ALEC avant de signer", "Conseil gratuit sur les travaux et les aides : les demandes d’aide se font avant de signer "
                                              "les devis et de commencer le chantier.")],
    aides_intro="Demandez conseil, puis les aides, avant de signer le moindre devis.",
    aides=[("ALEC Montpellier Métropole", "L’Espace Conseil France Rénov’ de la Métropole : conseil gratuit et neutre. 33 bis rue du "
                                          "Faubourg-Saint-Jaumes, 34000 Montpellier. 04 67 91 96 91, du mardi au vendredi de 13 h à 18 h. "
                                          + L("alec-montpellier.org", _ALEC) + "."),
           ("Aide « plan climat » de la Métropole", "1 300 € par logement pour les ménages très modestes, avec un gain d’énergie d’au moins "
                                                   "40 %. En copropriété, 1 300 € ou 2 600 € par lot d’habitation, selon l’étiquette "
                                                   "énergétique de départ et le dispositif (" + L("règlement 2025", _PC) + ")."),
           ("Programmes de la Métropole", "Hors des secteurs d’OPAH, le programme « Rénover pour un habitat durable et solidaire » "
                                          "accompagne les propriétaires avec Urbanis : 04 67 64 70 72 (" + L("Métropole", _PIG) + "). "
                                          "L’OPAH Grand Cœur couvre Courreau, Figuerolles, Nord-Écusson et Carnot jusqu’en 2027 ("
                                          + L("Ville de Montpellier", _DISPO) + ")."),
           NATIONAL],
    faq=[("Le ravalement est-il obligatoire à Montpellier ?",
          "La Ville peut l’imposer : elle figure sur la liste préfectorale, et le conseil municipal fixe des périmètres de ravalement "
          "obligatoire, comme à Celleneuve. Ailleurs, elle préconise un ravalement tous les dix ans. Ses aides au ravalement "
          "sont aujourd’hui suspendues."),
         ("Quelles règles pour des travaux dans l’Écusson ?",
          "L’Écusson est un secteur sauvegardé de 96 hectares. Toute construction, démolition ou modification, même intérieure, y demande "
          "une autorisation avec l’avis conforme de l’architecte des Bâtiments de France, et chaque immeuble a sa fiche de prescriptions."),
         ("Faut-il une autorisation pour changer ses fenêtres à Montpellier ?",
          "Oui, une déclaration préalable dès que l’aspect change, à déposer à la direction de l’urbanisme appliqué ou sur le guichet "
          "numérique. En secteur protégé, l’architecte des Bâtiments de France donne son avis : il préconise le bois et déconseille le blanc "
          "et le gris anthracite."),
         ("Montpellier est-elle en zone termites ?",
          "Oui, comme tout l’Hérault depuis l’arrêté préfectoral du 20 juin 2001. Une infestation se déclare en mairie dans le mois. Aucun "
          "arrêté ne vise la mérule dans le département."),
         ("Peut-on installer un climatiseur en façade dans l’Écusson ?",
          "Il doit être intégré à l’architecture, par exemple derrière une imposte à ventelles en bois, et le projet passe par l’architecte "
          "des Bâtiments de France. Les coffres de volets roulants en saillie sont, eux, à supprimer."),
         ("Quelles aides pour rénover son logement à Montpellier ?",
          "L’aide « plan climat » de la Métropole (1 300 € par logement pour les ménages très modestes, avec au moins 40 % d’énergie "
          "économisée), les programmes de la Métropole avec Urbanis et les aides nationales. Conseil gratuit à l’ALEC : 04 67 91 96 91.")],
)

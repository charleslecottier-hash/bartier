# Perpignan : fiche locale de la page « Devis travaux à Perpignan ». Sources officielles consultées le 21/11/2026.
# Chiffres Insee : jeu « Logements, principaux indicateurs (dossier complet) », RP 2023, lu via l'API Melodi
# (la page « dossier complet » d'insee.fr ne répondait pas pendant la recherche).
# Le règlement écrit du PSMV n'est pas en ligne : matériaux tirés du rapport de présentation de la révision (2019).
from villes_data import L, S, SP, NATIONAL  # liens dans le texte, sources discrètes, Service-Public, aides nationales
REVIEWED = "2026-11-21"
PUBLISH = "2026-12-05"  # vague 2 : publication deux semaines après la vague 1 (voir VILLES.md)

_INSEE = "https://api.insee.fr/melodi/data/DS_RP_LOGEMENT_PRINC?GEO=COM-66136"
_PSMV = "https://perpignanmediterraneemetropole.fr/urbanisme/plan-de-sauvegarde-et-de-mise-en-valeur/"
_PSMV_RP = "https://mairie.perpignan.fr/sites/mairie-perpignan.fr/files/docs/user1/livre_1_sommaire_introduction.pdf"
_PSMV_TYPO = "https://mairie.perpignan.fr/sites/mairie-perpignan.fr/files/docs/user1/livre_2-2_constatstypo-morphologie.pdf"
_OAP8 = "https://mairie.perpignan.fr/sites/default/files/documents/oap_8_habitat_19_06_05.pdf"
_MRAE = "https://www.mrae.developpement-durable.gouv.fr/IMG/pdf/decision_mrae_2022dko14.pdf"
_SPR_CULT = "https://www.culture.gouv.fr/Thematiques/Monuments-Sites/Interventions-demarches/Realiser-des-travaux-dans-un-site-patrimonial-remarquable"
_RO = "https://www.mairie-perpignan.fr/sites/default/files/documents/compte-rendu-2024-06-13.pdf"
_FAC = "https://www.mairie-perpignan.fr/demarches/renovation-facades-et-devantures-commerciales/renovation-facades"
_PLUI = "https://perpignanmediterraneemetropole.fr/urbanisme/plui/"
_TERM = ("https://www.pyrenees-orientales.gouv.fr/Actions-de-l-Etat/Amenagement-du-territoire-construction-logement/"
         "Qualite-des-batiments-et-accessibilite/Termites-et-Merules/Termites")
_MERULE = ("https://www.pyrenees-orientales.gouv.fr/Actions-de-l-Etat/Amenagement-du-territoire-construction-logement/"
           "Qualite-des-batiments-et-accessibilite/Termites-et-Merules/Merules")
_DREAL = "https://www.occitanie.developpement-durable.gouv.fr/IMG/pdf/603-3-_termites_-_modif_sept_2023.pdf"
_MF = "https://donneespubliques.meteofrance.fr/FichesClim/FICHECLIM_66136001.pdf"
_CATNAT = "https://georisques.gouv.fr/api/v1/gaspar/catnat?code_insee=66136&page_size=100"
_SISMO = "https://georisques.gouv.fr/api/v1/zonage_sismique?code_insee=66136"
_UDAP = ("https://www.culture.gouv.fr/regions/drac-occitanie/la-direction-regionale-des-affaires-culturelles-drac-occitanie/"
         "patrimoines-et-architecture/espaces-proteges-les-unites-departementales-de-l-architecture-et-du-patrimoine-udap-d-occitanie/udap-66")
_DAU = "https://www.mairie-perpignan.fr/demarches/urbanisme-amenagement-habitat/autorisation-durbanisme"
_DAU_LIGNE = "https://www.mairie-perpignan.fr/actualites/vos-demarches-durbanisme-en-ligne"
_ODP = "https://www.mairie-perpignan.fr/demarches/travaux-demenagements-et-livraisons"
_ODP_DOCS = "https://www.mairie-perpignan.fr/demarches/travaux-demenagements-et-livraisons/documents-telecharger"
_RENOV = "https://perpignanmediterraneemetropole.fr/developpement-durable/renovation-energetique/"
_ANAH = "https://perpignanmediterraneemetropole.fr/le-logement/anah/rehabiliter-mon-logement/"
_SPL = "https://spl-perpignan-mediterranee.org/contact/"

CITY = dict(
    slug="perpignan", name="Perpignan", cp="66000", insee="66136",
    lat=42.6975, lon=2.8947, dept="Pyrénées-Orientales", depcode="66", region="Occitanie",
    wiki="https://fr.wikipedia.org/wiki/Perpignan", wikidata="Q6730",
    verified="2026-11-21",
    tldr=("À Perpignan, la Ville peut imposer le ravalement des façades et en finance 30 à 40 % dans ses périmètres d’aide, et dans "
          "le secteur sauvegardé de 99 hectares, même l’intérieur des immeubles passe par l’architecte des Bâtiments de France"),
    hook="Ravalement imposé et aidé, secteur sauvegardé de 99 ha, vent et termites.",
    title="Devis travaux à Perpignan : toiture, façade, fenêtres, isolation",
    desc=("Travaux à Perpignan : ravalement obligatoire, aide façade de 30 à 40 %, secteur sauvegardé de 99 ha, termites, "
          "vent fort. Un seul artisan vient chiffrer."),
    figures_intro="Ce qui compte avant des travaux, du Castillet aux faubourgs.",
    figures=[("73,2 <small>%</small>", "des logements sont des appartements", S("Insee, 2023", _INSEE)),
             ("45,4 <small>%</small>", "des résidences principales datent d’avant 1971", S("Insee, 2023", _INSEE)),
             ("99 <small>ha</small>", "de secteur sauvegardé, environ 10 500 habitants", S("MRAe Occitanie, 2022", _MRAE)),
             ("136,6 <small>jours</small>", "de rafales à 58 km/h ou plus chaque année", S("Météo-France, normales 1991-2020", _MF))],
    answer=("À Perpignan, 73,2 % des logements sont des appartements, et 45,4 % des résidences principales datent d’avant 1971. "
            "Depuis 2021, la Ville peut imposer le ravalement des façades, et dans les périmètres de son Action municipale façades, "
            "elle finance 30 à 40 % des travaux. Dans le secteur "
            "sauvegardé de 99 hectares, les travaux sur l’extérieur comme sur l’intérieur du bâti demandent l’accord de "
            "l’architecte des Bâtiments de France."),
    facts=[("Ravalement", "Un arrêté préfectoral du 22 mars 2021 inscrit Perpignan sur la liste des communes qui peuvent imposer le "
                          "ravalement, au moins une fois tous les 10 ans. Après une première campagne en 2022-2024 sur les grands axes "
                          "touristiques du centre, la deuxième vise la rue des Augustins et la place des Poilus jusqu’en 2027 ("
                          + L("délibération du 13 juin 2024", _RO) + ")."),
           ("Secteur sauvegardé", "Son plan de sauvegarde, approuvé en 2007 et révisé le 4 juillet 2019, couvre 99 hectares : "
                                  "Saint-Jean, Saint-Jacques, Saint-Mathieu, La Réal, la Villeneuve et le quartier du XXe siècle au nord des anciens remparts ("
                                  + L("rapport du PSMV", _PSMV_RP) + ", " + L("MRAe", _MRAE) + "). Sa modification n° 1 date du "
                                  "18 mai 2022 (" + L("Perpignan Méditerranée Métropole", _PSMV) + ")."),
           ("Intérieurs protégés", "Dans un secteur doté d’un plan de sauvegarde, les travaux qui modifient l’intérieur du bâti sont "
                                   "eux aussi soumis à autorisation, avec l’accord de l’architecte des Bâtiments de France ("
                                   + L("ministère de la Culture", _SPR_CULT) + ")."),
           ("Urbanisme", "Le PLUi-D de Perpignan Méditerranée Métropole a été approuvé le 24 février 2026, puis mis à jour le "
                         "12 octobre 2026, et une révision est déjà engagée (" + L("Perpignan Méditerranée Métropole", _PLUI) + "). "
                         "Le secteur sauvegardé garde son propre règlement, celui du plan de sauvegarde (" + L("MRAe", _MRAE) + ")."),
           ("Termites", "Un arrêté préfectoral du 27 mars 2001 délimite les communes touchées ou menacées par les termites (" + L("préfecture", _TERM)
                        + ") : Perpignan en fait partie, selon la carte de la DREAL Occitanie (" + L("fiche termites", _DREAL) + ", 2023). "
                        "Aucun arrêté ne vise la mérule dans les Pyrénées-Orientales (" + L("préfecture", _MERULE) + ")."),
           ("Vent, pluie, séisme", "136,6 jours de rafales à 58 km/h ou plus par an, et un record à 51 m/s, environ 184 km/h, le 24 janvier "
                                   "2009. 578,3 mm de pluie par an, mais 222 mm en un seul jour le 12 novembre 1999 (" + L("Météo-France", _MF)
                                   + ", normales 1991-2020). La commune compte 17 arrêtés de catastrophe naturelle pour inondation depuis 1982 ("
                                   + L("Géorisques", _CATNAT) + ") et se trouve en zone de sismicité 3, modérée (" + L("Géorisques", _SISMO) + ").")],
    trades_intro="Galets, cayrous, enduits de chaux et tuile canal : le centre ancien a ses propres techniques de construction.",
    trades={
        "toiture": ["Dans les îlots étudiés pour la révision du plan de sauvegarde, environ 60 % des toits sont en tuile canal, 29 % "
                    "des immeubles ont une terrasse côté rue et 10 % côté cour. Les corniches portent "
                    "parfois des tortugades, des pièces de terre cuite émaillée vertes ou brunes, connues dans la région depuis le XVe siècle, "
                    "qui remplacent le chéneau maçonné (" + L("rapport du PSMV", _PSMV_TYPO) + ").",
                    "Perpignan compte 8,9 jours par an de rafales à 100 km/h ou plus, et le record atteint 51 m/s le 24 janvier 2009 ("
                    + L("Météo-France", _MF) + "). Faites contrôler faîtages, rives et fixations des tuiles après chaque coup de vent fort."],
        "facade": ["Les murs anciens mêlent galets de rivière et rangs de cayrous, la brique catalane, dont l’épaisseur est passée de 7 à "
                   "4 cm au fil des siècles. Ils étaient revêtus d’un enduit de chaux : le rapport du plan de sauvegarde juge anormal de les "
                   "décaper pour montrer des maçonneries disparates (" + L("rapport du PSMV", _PSMV_TYPO) + ").",
                   "L’Action municipale façades finance 40 % des travaux pour les immeubles patrimoniaux du centre ancien et de l’îlot "
                   "Notre-Dame, et 30 % dans les autres secteurs de son périmètre, qui s’étend au quartier de la Gare, au boulevard "
                   "Aristide-Briand et aux axes des quatre faubourgs. Un technicien de la Ville fixe les prescriptions et suit le "
                   "chantier (" + L("Ville de Perpignan", _FAC) + ")."],
        "fenetres": ["Le modèle le plus courant du centre est le volet brisé, dit « à la catalane », qui se replie dans le tableau de la "
                     "baie. Le rapport du plan de sauvegarde qualifie leur suppression de contresens historique et écologique ("
                     + L("rapport du PSMV", _PSMV_TYPO) + ").",
                     "Si de nouvelles fenêtres changent l’aspect de la façade, une déclaration préalable est nécessaire ("
                     + L("Service-Public", SP + "F17578") + "). Dans le secteur sauvegardé, l’architecte des Bâtiments de "
                     "France a un mois pour donner son accord, éventuellement avec des prescriptions (" + L("ministère de la Culture", _SPR_CULT) + ")."],
        "charpente": ["Perpignan est en zone termites. Une infestation se déclare en mairie dans le mois, et les bois contaminés retirés "
                      "pendant les travaux sont brûlés sur place ou traités avant tout transport (" + L("DREAL Occitanie", _DREAL) + ").",
                      "En 2014, le préfet a mis le plan de sauvegarde en révision, notamment à cause des effondrements répétés de certains "
                      "édifices du secteur (" + L("rapport du PSMV", _PSMV_RP) + "). Avant de reprendre une toiture ou un plancher dans un "
                      "immeuble ancien, faites établir un diagnostic de la structure."],
        "isolation": ["Le Guichet Rénov’Occitanie de la Métropole aide à choisir les travaux, à lire les devis et à monter les demandes "
                      "de subventions (" + L("Perpignan Méditerranée Métropole", _RENOV) + "). Ici, 36 jours par an atteignent au moins 30 °C, pour "
                      "9,1 jours de gel (" + L("Météo-France", _MF) + ") : pensez au confort d’été autant qu’au chauffage.",
                      "Dans les îlots anciens, le mur de fond de parcelle est généralement en pisé, sur deux niveaux. Les orientations "
                      "du plan de sauvegarde le montrent conservé et protégé par des enduits, et demandent de repérer ces murs avant "
                      "travaux (" + L("OAP Habitat du PSMV", _OAP8) + "). En secteur sauvegardé, une isolation par l’extérieur passe "
                      "par l’accord de l’architecte des Bâtiments de France."]},
    steps_intro="Cinq étapes, de la façade au trottoir.",
    steps=[("Vérifiez votre secteur", "Dans le secteur sauvegardé, l’architecte des Bâtiments de France donne son accord. "
                                      "UDAP des Pyrénées-Orientales, 7 rue Georges-Bizet. 04 68 34 51 93 (" + L("UDAP 66", _UDAP) + ")."),
           ("Rencontrez l’Action façade", "Un technicien référent vient sur place et fixe les prescriptions. Direction de l’Habitat, "
                                          "11 rue du Castillet, 2e étage, du lundi au vendredi de 9 h à 12 h et de 14 h à 17 h. "
                                          "04 68 66 32 18 (" + L("Ville de Perpignan", _FAC) + ")."),
           ("Déposez la déclaration préalable", "En ligne et gratuitement depuis le 1er janvier 2022 (" + L("Ville de Perpignan", _DAU_LIGNE)
                                                + "), ou à la direction de l’Aménagement et de l’Urbanisme, 11 rue du Castillet, 1er étage, "
                                                "de 8 h 30 à 12 h 30. 04 68 66 31 78 (" + L("démarche", _DAU) + ")."),
           ("Faites autoriser l’échafaudage", "Envoyez le formulaire d’occupation du domaine public à autorisationvoirie@mairie-perpignan.com, "
                                              "au moins deux semaines avant (" + L("Ville de Perpignan", _ODP) + "). L’occupation est "
                                              "soumise à redevance (" + L("documents à télécharger", _ODP_DOCS) + ")."),
           ("Appelez le Guichet Rénov’Occitanie", "Conseil neutre et gratuit sur les travaux et les aides, avant de signer le devis. "
                                                  "04 68 51 70 27 (" + L("Perpignan Méditerranée Métropole", _RENOV) + ").")],
    aides_intro="Le conseil public est gratuit, et le dossier d’aide se monte avant les travaux.",
    aides=[("Guichet Rénov’Occitanie Perpignan Méditerranée", "L’Espace Conseil France Rénov’ de la Métropole, porté par la SPL Perpignan "
                                                             "Méditerranée : conseil neutre et gratuit. 35 boulevard Saint-Assiscle, Centre "
                                                             "del Món, 66000 Perpignan. 04 68 51 70 27. Permanence Anah le vendredi de 9 h à "
                                                             "11 h (" + L("Perpignan Méditerranée Métropole", _ANAH) + ", "
                                                             + L("Rénov’Occitanie", _RENOV) + ", " + L("SPL", _SPL) + ")."),
           ("Action municipale façades", "40 % des travaux pour les immeubles patrimoniaux du centre ancien et de l’îlot Notre-Dame, 30 % "
                                         "dans les autres secteurs, avec un technicien de la Ville pour les prescriptions et le suivi. "
                                         "La Ville a maintenu ses règles de financement de 2020 pour la campagne de ravalement 2024-2027 ("
                                         + L("Ville de Perpignan", _FAC) + ", " + L("délibération 2024", _RO) + ")."),
           ("Aides de l’Anah et de la Métropole", "Pour un logement de plus de 15 ans, Perpignan Méditerranée Métropole instruit les "
                                                  "demandes de l’Anah et ajoute son propre cofinancement, pour les propriétaires occupants "
                                                  "comme pour les bailleurs (" + L("Perpignan Méditerranée Métropole", _ANAH) + ")."),
           NATIONAL],
    faq=[("Le ravalement est-il obligatoire à Perpignan ?",
          "La Ville peut l’imposer depuis l’arrêté préfectoral du 22 mars 2021 : les façades doivent être ravalées au moins une fois "
          "tous les 10 ans. Elle procède par campagnes : la deuxième, de 2024 à 2027, vise la rue des Augustins et la place des Poilus. "
          "L’Action municipale façades finance 30 à 40 % des travaux."),
         ("Quelles règles dans le secteur sauvegardé de Perpignan ?",
          "Il couvre 99 hectares, de Saint-Jean à La Réal. Les travaux qui touchent l’extérieur ou l’intérieur du bâti y demandent une "
          "autorisation et l’accord de l’architecte des Bâtiments de France. Le plan de sauvegarde a été révisé en 2019 et modifié en 2022."),
         ("Faut-il une autorisation pour changer ses fenêtres à Perpignan ?",
          "Oui, dès que l’aspect de la façade change : une déclaration préalable, en ligne ou à la direction de l’Aménagement et de "
          "l’Urbanisme. Dans le secteur sauvegardé, l’architecte des Bâtiments de France donne son accord, et le rapport du plan de "
          "sauvegarde qualifie de contresens la suppression des volets à la catalane."),
         ("Perpignan est-elle en zone termites ?",
          "Oui, en vertu de l’arrêté préfectoral du 27 mars 2001. Une infestation se déclare en mairie dans le mois, et les bois "
          "contaminés se brûlent sur place ou se traitent avant transport. Aucun arrêté ne vise la mérule dans le département."),
         ("Comment protéger sa toiture du vent à Perpignan ?",
          "Les rafales atteignent 58 km/h ou plus 136,6 jours par an, et 100 km/h ou plus 8,9 jours par an. Faites vérifier faîtage, "
          "rives et fixations des tuiles, surtout après un coup de vent."),
         ("Quelles aides pour rénover son logement à Perpignan ?",
          "L’Action municipale façades (30 à 40 %), les aides de l’Anah complétées par la Métropole et les aides nationales. Conseil "
          "gratuit au Guichet Rénov’Occitanie : 04 68 51 70 27.")],
)

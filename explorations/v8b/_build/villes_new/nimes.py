from villes_data import L, S, SP, NATIONAL  # liens dans le texte, sources discrètes, Service-Public, aides nationales
REVIEWED = "2026-11-21"
PUBLISH = "2026-12-05"  # vague 2 : publication deux semaines après la vague 1 (voir VILLES.md)

# Sources consultées le 21/11/2026.
_INSEE = "https://api.insee.fr/melodi/data/DS_RP_LOGEMENT_PRINC?GEO=COM-30189"  # dossier complet, RP 2023 (page insee.fr en erreur 500 ce jour)
_NIMES = "https://www.nimes.fr"
_SPR = _NIMES + "/ma-ville/les-grands-projets/site-patrimonial-remarquable"
_SPR40 = _NIMES + "/fileadmin/mediatheque/nimes/espace-presse/communique-presse/2025/07-juillet/40-ans-SitePatrimonialRemarquable.pdf"
_PSMV = _NIMES + "/fileadmin/mediatheque/nimes/mon-quotidien/urbanisme/PLU/volume-3/plan-sauvegarde-mise-en-valeur.pdf"
_PLU = _NIMES + "/mon-quotidien/urbanisme/regles-durbanisme/plan-local-durbanisme-de-nimes"
_GUIDE = _NIMES + "/fileadmin/mediatheque/nimes/mon-quotidien/urbanisme/autorisations-urbanisme/guide-pratique-2024.pdf"
_AUTO = _NIMES + "/mon-quotidien/urbanisme/autorisations-durbanisme"
_IDEAU = "https://ideau.atreal.fr/"
_RISQ = _NIMES + "/mon-quotidien/urbanisme/regles-durbanisme/reglementations-specifiques"
_PPRI = _NIMES + "/fileadmin/mediatheque/nimes/mon-quotidien/urbanisme/regles-urbanisme/regles-specifiques/PPRI.pdf"
_RGA = _NIMES + "/fileadmin/mediatheque/nimes/mon-quotidien/urbanisme/PLU/volume-3/retrait-gonflement-argile.pdf"
_RAV = "https://mes-demarches.nimes.fr/fiche/128/"
_MENU = "https://mes-demarches.nimes.fr/fiche/161/"  # subvention menuiseries de fenêtres, secteur Écusson
_ODP = "https://formulaires.mes-demarches.nimes.fr/signalement/demande-d-arrete-municipal-occupation-temporaire-du-domaine-public-voirie/"
_ALABRI = "https://nimalabri.fr/"
_MDH = "https://www.nimes-metropole.fr/mon-quotidien/maison-de-lhabitat/contacter-la-maison-de-lhabitat"
_MDH_FLYER = "https://www.nimes-metropole.fr/fileadmin/mediatheque/canm/actualite/2025/mai/maison-habitat-flyer.pdf"
_PAT = "https://www.nimes-metropole.fr/fileadmin/mediatheque/canm/mon-agglo/plan-actions/habitat-programme-actions-territorial-2026.pdf"
_TERM = ("https://www.gard.gouv.fr/actions-de-letat/amenagement-du-territoire-et-construction/"
         "batiment-durable-diagnostic-construction/termites-et-merules")
_MF = "https://donneespubliques.meteofrance.fr/FichesClim/FICHECLIM_30189001.pdf"
_SISM = "https://georisques.gouv.fr/api/v1/zonage_sismique?code_insee=30189"
_CATNAT = "https://georisques.gouv.fr/api/v1/gaspar/catnat?code_insee=30189&page_size=100"

CITY = dict(
    slug="nimes", name="Nîmes", cp="30000", insee="30189",
    lat=43.8383, lon=4.3597, dept="Gard", depcode="30", region="Occitanie",
    wiki="https://fr.wikipedia.org/wiki/N%C3%AEmes", wikidata="Q42807",
    verified="2026-11-21",
    tldr=("À Nîmes, le ravalement est obligatoire dans le site patrimonial remarquable, porté à 109 hectares en 2023, et la Ville "
          "le subventionne au mètre carré ; de nombreux quartiers sont aussi en zone inondable"),
    hook="Ravalement obligatoire et aidé dans l’Écusson, risque inondation.",
    title="Devis travaux à Nîmes : toiture, façade, fenêtres, isolation",
    desc=("Travaux à Nîmes : site patrimonial de 109 ha, ravalement obligatoire et aidé au m², zone inondable, Gard classé "
          "termité. Un seul artisan vient chiffrer."),
    figures_intro="Le bâti nîmois en quatre chiffres, de l’Écusson aux garrigues.",
    figures=[("70,3 <small>%</small>", "des logements sont des appartements", S("Insee, 2023", _INSEE)),
             ("37,7 <small>%</small>", "des résidences principales datent d’avant 1971", S("Insee, 2023", _INSEE)),
             ("109 <small>ha</small>", "de site patrimonial remarquable depuis 2023, contre 41 avant", S("Ville de Nîmes", _SPR40)),
             ("59 <small>jours</small>", "par an à 30 °C ou plus à Nîmes-Courbessac", S("Météo-France, normales 1991-2020", _MF))],
    answer=("À Nîmes, 70,3 % des logements sont des appartements et 37,7 % des résidences principales datent d’avant 1971. "
            "Dans le site patrimonial remarquable, étendu à 109 hectares en 2023, le ravalement est obligatoire et la Ville le "
            "subventionne au mètre carré. De nombreux secteurs relèvent du plan de prévention du risque inondation de 2012, et "
            "tout le Gard est classé zone termites depuis 2003."),
    facts=[("Écusson et site patrimonial", "Le secteur sauvegardé, créé le 15 mars 1985, est devenu site patrimonial remarquable ; il est "
                                           "passé de 41 à 109 hectares en 2023. Son plan de sauvegarde, approuvé le 5 juin 2007 et "
                                           "modifié pour la troisième fois le 14 décembre 2015 (" + L("PSMV", _PSMV) + "), est en cours "
                                           "d’actualisation (" + L("Ville de Nîmes", _SPR40) + ", 2025)."),
           ("Ravalement", "Obligatoire sur tout le périmètre du site patrimonial remarquable et du site inscrit, par cinq campagnes. "
                          "La subvention municipale est calculée sur les métrés, par exemple 9,90 €/m² pour le nettoyage de la pierre, "
                          "6,80 €/m² pour un enduit à la chaux et 3,80 €/m² pour un badigeon, si le cahier des charges est respecté ("
                          + L("Ville de Nîmes", _RAV) + ")."),
           ("Urbanisme", "Le PLU approuvé le 7 juillet 2018 a été modifié pour la dernière fois le 4 novembre 2023, et sa révision est "
                         "engagée depuis le 16 novembre 2024 (" + L("Ville de Nîmes", _PLU) + "). Rénover une toiture, ravaler ou changer "
                         "ses menuiseries demande une déclaration préalable (" + L("guide pratique", _GUIDE) + ")."),
           ("Inondation", "Le plan de prévention du risque inondation est approuvé depuis le 28 février 2012 (" + L("Ville de Nîmes", _RISQ)
                          + "). Nîmes compte 22 arrêtés de catastrophe naturelle pour inondation depuis 1982, le dernier pour "
                          "les pluies des 18 et 19 octobre 2026 (" + L("Géorisques", _CATNAT) + ")."),
           ("Termites et mérule", "Tout le Gard est classé zone termites par l’arrêté préfectoral du 15 octobre 2003 : un état termites "
                                  "est exigé à la vente. Il n’existe pas d’arrêté mérule dans le département (" + L("préfecture", _TERM) + ", 2026)."),
           ("Climat", "À Nîmes-Courbessac, 734,4 mm de pluie tombent en 64,8 jours seulement, avec un record de 266,8 mm en un jour en "
                      "octobre 1990, et 65,8 jours de rafales d’au moins 58 km/h par an (" + L("Météo-France", _MF) + ", normales 1991-2020). "
                      "Zone sismique 2, faible (" + L("Géorisques", _SISM) + ").")],
    trades_intro="Pierre de taille, enduits à la chaux et tuiles canal : dans l’Écusson, l’article 11 du plan de sauvegarde fixe chaque détail.",
    trades={
        "toiture": ["Dans le secteur sauvegardé, la couverture se fait en tuiles de terre cuite canal ou demi-ronde, de teinte claire et "
                    "uniforme. Les tuiles mécaniques, en béton, vieillies ou panachées artificiellement sont interdites, comme les "
                    "panneaux solaires ajoutés en toiture, sauf sur une terrasse sans vue depuis la rue (" + L("règlement du PSMV", _PSMV) + ").",
                    "Nîmes-Courbessac compte 65,8 jours de rafales d’au moins 58 km/h par an, surtout en février et en mars ("
                    + L("Météo-France", _MF) + "). Dans toute la ville, une rénovation de toiture demande une déclaration préalable ("
                    + L("guide pratique", _GUIDE) + ")."],
        "facade": ["La pierre se nettoie à l’eau froide, par brumisation ou par cataplasme ; sablage, boucharde et ponceuse sont interdits. "
                   "Le ciment est proscrit pour les joints et les enduits, faits au mortier de chaux, dans les teintes du nuancier du "
                   "secteur sauvegardé (" + L("règlement du PSMV", _PSMV) + ").",
                   "Dans les cinq campagnes de ravalement obligatoire, la subvention municipale est calculée au mètre carré. Trois "
                   "rendez-vous avec le pôle Site patrimonial remarquable sont obligatoires : avant le montage de l’échafaudage, pendant "
                   "le chantier et à la fin (" + L("Ville de Nîmes", _RAV) + ")."],
        "fenetres": ["Dans le secteur sauvegardé, le PVC et le blanc sont interdits pour les menuiseries, qui doivent être peintes et avoir "
                     "de vrais petits bois assemblés. Les volets en PVC, en aluminium, métalliques ou roulants sont interdits, et les "
                     "climatiseurs ne peuvent être posés ni en façade, ni sur un balcon, ni en appui de fenêtre (" + L("règlement du PSMV", _PSMV) + ").",
                     "En zone d’aléa fort ou très fort du plan de prévention, chaque porte ou fenêtre située sous les plus hautes eaux "
                     "doit recevoir un batardeau de 0,50 m à 0,80 m de haut (" + L("règlement du PPRi", _PPRI) + "). Après un diagnostic "
                     "gratuit, ces protections sont subventionnées de 85 à 100 % (" + L("Nîm’Alabri", _ALABRI) + ")."],
        "charpente": ["Tout le Gard est déclaré termité depuis l’arrêté préfectoral du 15 octobre 2003 : un état termites est joint au "
                      "dossier de diagnostic à la vente, et une construction ou un aménagement neuf doit être protégé contre les termites ("
                      + L("préfecture", _TERM) + ").",
                      "Nîmes compte aussi sept arrêtés de catastrophe naturelle pour sécheresse depuis 2007, le dernier pour 2023 ("
                      + L("Géorisques", _CATNAT) + ") : le PLU annexe la carte de l’aléa retrait-gonflement des argiles, de faible à fort ("
                      + L("carte", _RGA) + ")."],
        "isolation": ["Dans le secteur sauvegardé, l’isolation par l’extérieur des murs, des façades et des pignons est interdite sur tous "
                      "les immeubles anciens (" + L("règlement du PSMV", _PSMV) + "). À Nîmes-Courbessac, le thermomètre atteint 30 °C "
                      "59 jours par an et a atteint 44,4 °C en juin 2019 (" + L("Météo-France", _MF) + ").",
                      "Hors opération programmée, Nîmes Métropole ajoute à MaPrimeRénov’ Parcours accompagné une aide propre de 5 % sur des travaux plafonnés à "
                      "30 000 € ou 40 000 € HT, selon le nombre de classes gagnées. Le passage préalable à la Maison de l’Habitat France "
                      "Rénov’ est une condition pour déposer le dossier (" + L("programme d’actions 2026", _PAT) + ")."]},
    steps_intro="Dans l’ordre, de l’Écusson aux quartiers inondables.",
    steps=[("Vérifiez si vous êtes dans le site patrimonial", "Avant tout projet, la Ville conseille de contacter le pôle Site patrimonial "
                                                             "remarquable ou l’architecte des Bâtiments de France (" + L("Ville de Nîmes", _SPR)
                                                             + "). Pôle SPR, 152 avenue Robert Bompard. 04 66 70 75 63 ("
                                                             + L("démarche", _RAV) + ")."),
           ("Vérifiez le risque inondation", "Le " + L("règlement du PPRi", _PPRI) + " fixe les règles par zone. Nîm’Alabri fait un diagnostic "
                                             "gratuit de votre logement. 04 11 93 25 74."),
           ("Déposez la déclaration préalable", "En ligne sur la plateforme " + L("IDE’AU", _IDEAU) + ", ou au service Urbanisme réglementaire, "
                                                "152 avenue Robert Bompard, ouvert en semaine de 8 h 30 à 12 h et de 14 h à 17 h. "
                                                "04 66 70 75 54 (" + L("Ville de Nîmes", _AUTO) + ")."),
           ("Faites autoriser l’échafaudage", "Demandez l’arrêté d’occupation du domaine public en ligne : le délai moyen de réponse est de "
                                              "10 jours ouvrés. Pour un échafaudage, un rendez-vous avec un contrôleur travaux est fixé 15 jours "
                                              "ouvrés avant la délivrance (" + L("démarche", _ODP) + ")."),
           ("Passez par la Maison de l’Habitat avant de signer", "Son attestation est exigée pour les aides de l’Anah sur le territoire de "
                                                                 "Nîmes Métropole (" + L("programme d’actions 2026", _PAT) + ").")],
    aides_intro="À Nîmes, passez d’abord par la Maison de l’Habitat : son attestation conditionne les aides de l’Anah.",
    aides=[("Maison de l’Habitat France Rénov’", "L’Espace conseil France Rénov’ de Nîmes Métropole : Colisée 2, 1 rue du Colisée, 30900 Nîmes. "
                                                 "04 66 02 54 14. Sur rendez-vous, du lundi au vendredi, de 10 h à 12 h 30 et de 13 h 30 à 16 h 30, "
                                                 "sauf le mardi et le vendredi après-midi (" + L("Nîmes Métropole", _MDH_FLYER) + ", " + L("contact", _MDH) + ")."),
           ("Aide de Nîmes Métropole", "Hors opération programmée, 5 % en plus de MaPrimeRénov’ Parcours accompagné, et 10 % pour "
                                       "l’adaptation du logement à la perte d’autonomie, sous les plafonds de l’Anah. Le passage par la "
                                       "Maison de l’Habitat est obligatoire (" + L("programme d’actions 2026", _PAT) + ")."),
           ("Subventions municipales du site patrimonial", "Ravalement, dans les cinq campagnes : par exemple 9,90 €/m² pour le nettoyage "
                                                   "de la pierre, 6,80 €/m² pour l’enduit et 3,80 €/m² pour le badigeon à la chaux (" + L("ravalement", _RAV)
                                                   + "). Fenêtres, dans le plan de sauvegarde : par exemple 200 €/m² pour une réparation et 120 €/m² "
                                                   "pour un remplacement, dans la limite de 30 % du montant HT (" + L("menuiseries", _MENU) + "). La Ville "
                                                   "aide aussi les murs en pierre sèche (" + L("Ville de Nîmes", _SPR) + ")."),
           ("Nîm’Alabri", "Dispositif public porté par l’EPTB Vistre Vistrenque : diagnostic inondation gratuit, puis mesures de "
                          "protection subventionnées de 85 à 100 % par l’État, le Département, Nîmes Métropole et la Ville. "
                          "184 rue Philippe Maupas. 04 11 93 25 74 (" + L("nimalabri.fr", _ALABRI) + ")."),
           NATIONAL],
    faq=[("Le ravalement est-il obligatoire à Nîmes ?",
          "Oui, sur tout le périmètre du site patrimonial remarquable et du site inscrit, par cinq campagnes. La Ville le subventionne "
          "selon les métrés, par exemple 9,90 €/m² pour le nettoyage de la pierre, 6,80 €/m² pour l’enduit et 3,80 €/m² pour le badigeon à la chaux."),
         ("Faut-il une autorisation pour changer ses fenêtres à Nîmes ?",
          "Oui, une déclaration préalable, pour un changement de matériau comme de peinture. Dans le secteur sauvegardé, le PVC et le "
          "blanc sont interdits, et l’architecte des Bâtiments de France donne son avis."),
         ("Peut-on installer une climatisation sur sa façade dans l’Écusson ?",
          "Non. Le plan de sauvegarde interdit les climatiseurs en façade, sur un balcon ou en appui de fenêtre. En toiture, ils peuvent "
          "être refusés s’ils nuisent à l’aspect de l’immeuble."),
         ("Nîmes est-elle en zone termites ?",
          "Oui. Tout le Gard est classé par l’arrêté préfectoral du 15 octobre 2003 : un état termites est exigé à la vente. Il n’y a "
          "pas d’arrêté mérule dans le département."),
         ("Ma maison est en zone inondable : que dois-je faire ?",
          "Le plan de prévention de 2012 impose un diagnostic en zone d’aléa modéré, fort ou très fort et, en aléa fort ou très fort, "
          "des batardeaux de 0,50 m à 0,80 m devant chaque ouverture sous les plus hautes eaux. Nîm’Alabri fait le diagnostic gratuitement, "
          "et les protections sont subventionnées de 85 à 100 %."),
         ("Quelles aides pour rénover son logement à Nîmes ?",
          "Hors opération programmée, Nîmes Métropole ajoute 5 % à MaPrimeRénov’ Parcours accompagné. Dans le site patrimonial, "
          "la Ville subventionne le ravalement et les fenêtres. Passez d’abord par la Maison de l’Habitat France Rénov’ : 04 66 02 54 14.")],
)

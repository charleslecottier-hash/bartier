from villes_data import L, S, SP, NATIONAL  # liens dans le texte, sources discrètes, Service-Public, aides nationales
REVIEWED = "2026-11-21"

# Sources consultées le 21/11/2026.
_INSEE = "https://api.insee.fr/melodi/data/DS_RP_LOGEMENT_PRINC?GEO=COM-21231"
_DM = "https://www.dijon-metropole.fr/dijon-metropole-a-votre-service/"
_SPR = _DM + "regles-durbanisme-et_patrimoine/sites-patrimoniaux-remarquables/"
_PSMV = "https://www.dijon-metropole.fr/wp-content/uploads/sites/10/2022/11/3-ReglementPSMV.pdf"
_POP = "https://pop.culture.gouv.fr/notice/merimee/SPR2700005"
_AVAP = "https://www.dijon-metropole.fr/wp-content/uploads/sites/25/2024/10/2.1-Reglement-Dijon-modifie.pdf"
_AVAP_RP = "https://www.dijon-metropole.fr/wp-content/uploads/sites/25/2024/10/1-Rapport-de-presentation-modifie.pdf"
_PDA = _DM + "regles-durbanisme-et_patrimoine/perimetres-delimites-des-abords/"
_PLUI = _DM + "plui-hd-outil-de-planification-urbaine/historique-des-procedures/elaboration-du-plui-hd/plui-hd-approuve-le-19-12-2019/"
_MOD1 = _DM + "plui-hd-outil-de-planification-urbaine/historique-des-procedures/modification-n1-du-plui-hd/dossier-dapprobation/"
_MODS = _DM + "plui-hd-outil-de-planification-urbaine/historique-des-procedures/modification-simplifiee-n1-du-plui-hd/"
_DDS = _DM + "regles-durbanisme-et_patrimoine/droit-des-sols-et-autorisation-durbanisme/"
_GUICHET = "https://extrageo.metropole-dijon.fr/guichet-unique/Login/Particulier"
_RDV = "https://eservices.dijon.fr/Pages/RDV/booking-auto?Site=DDS&IdCode=DM"
_ODP = "https://eservices.dijon.fr/Pages/ODP/workfilter"
_FACADES = "https://www.dijon.fr/dijon-a-votre-service/habitat/operation-facades-liberte/"
_RENOVECO = _DM + "renovation-energetique-de-lhabitat/conseillers-renoveco/"
_FR = "https://www.data.gouv.fr/datasets/liste-des-communes-et-espaces-conseil-france-renov-associes-5"
_COPRO = _DM + "renovation-energetique-de-lhabitat/habiter-en-copropriete/"
_MF = "https://donneespubliques.meteofrance.fr/FichesClim/FICHECLIM_21473001.pdf"
_PPRN = "https://www.dijon-metropole.fr/wp-content/uploads/sites/10/2023/02/dijon_note_presentation.pdf"
_SISM = "https://georisques.gouv.fr/api/v1/zonage_sismique?code_insee=21231"

CITY = dict(
    slug="dijon", name="Dijon", cp="21000", insee="21231",
    lat=47.3231, lon=5.0419, dept="Côte-d’Or", depcode="21", region="Bourgogne-Franche-Comté",
    wiki="https://fr.wikipedia.org/wiki/Dijon", wikidata="Q7003",
    verified="2026-11-21",
    tldr=("À Dijon, le centre historique est un secteur sauvegardé de 97 hectares, et les faubourgs anciens ont leur propre "
          "règlement patrimonial, lié aux Climats du vignoble de Bourgogne"),
    hook="Secteur sauvegardé de 97 ha et petites tuiles vernissées.",
    title="Devis travaux à Dijon : toiture, façade, fenêtres, isolation",
    desc=("Travaux à Dijon : secteur sauvegardé de 97 ha, tuiles vernissées, faubourgs protégés, aide Façades Liberté de "
          "la Ville. Un seul artisan vient chiffrer."),
    figures_intro="Le bâti dijonnais en quatre chiffres, du centre historique aux faubourgs.",
    figures=[("85,3 <small>%</small>", "des logements sont des appartements", S("Insee, 2023", _INSEE)),
             ("42,0 <small>%</small>", "des résidences principales datent d’avant 1971", S("Insee, 2023", _INSEE)),
             ("97 <small>ha</small>", "de secteur sauvegardé dans le centre historique", S("Dijon métropole", _SPR)),
             ("61,5 <small>jours</small>", "de gel par an à Dijon-Longvic", S("Météo-France, 1991-2020", _MF))],
    answer=("À Dijon, 85,3 % des logements sont des appartements, et 42,0 % des résidences principales datent d’avant 1971. "
            "Le centre historique est un secteur sauvegardé de 97 hectares, régi par un plan de sauvegarde qui fixe matériaux et "
            "teintes. Les faubourgs anciens ont leur propre règlement patrimonial, lié aux Climats du vignoble de Bourgogne "
            "inscrits à l’Unesco."),
    facts=[("Centre historique", "Secteur sauvegardé depuis le 19 août 1966 (" + L("ministère de la Culture", _POP) + "), il couvre "
                                 "97 hectares. Son " + L("plan de sauvegarde", _PSMV) + ", approuvé par décret le 8 février 1990, "
                                 "remplace le PLUi-HD sur ce périmètre et s’applique à tout projet (" + L("Dijon métropole", _SPR) + ")."),
           ("Faubourgs", "Les faubourgs anciens font partie d’un second site patrimonial remarquable, lié aux Climats du vignoble de "
                         "Bourgogne, inscrits au patrimoine mondial le 4 juillet 2015 (" + L("rapport de présentation", _AVAP_RP)
                         + "). Son règlement, modifié le 27 juin 2024, range chaque bâtiment dans l’une de quatre catégories, des "
                         "« remarquables » aux « autres constructions ». Sans l’accord de l’architecte des Bâtiments de France, "
                         "aucune autorisation de travaux n’y est délivrée (" + L("règlement", _AVAP) + ")."),
           ("Abords des monuments", "Cinq périmètres délimités des abords ont été créés à Dijon par arrêtés préfectoraux du 22 avril "
                                    "2022, dont celui du centre ancien, des faubourgs et du parc de la Colombière. Dans ces périmètres, "
                                    "l’avis de l’architecte des Bâtiments de France est conforme : il s’impose ("
                                    + L("Dijon métropole", _PDA) + ")."),
           ("Urbanisme", "Le PLUi-HD de Dijon métropole, approuvé le 19 décembre 2019, est exécutoire depuis le 23 janvier 2020 ("
                         + L("Dijon métropole", _PLUI) + "). Sa modification n° 1 s’applique depuis le 1er mai 2022 ("
                         + L("Métropole", _MOD1) + "), et sa modification simplifiée n° 1 depuis le 2 mai 2024 ("
                         + L("Métropole", _MODS) + ")."),
           ("Risques naturels", "Le plan de prévention des risques naturels de Dijon, approuvé le 7 décembre 2015, couvre les "
                                "inondations par ruissellement et débordement de cours d’eau, et les mouvements de terrain, dont le "
                                "retrait-gonflement des argiles (" + L("note de présentation", _PPRN) + "). Dijon est en zone de "
                                "sismicité 1, très faible (" + L("Géorisques", _SISM) + ")."),
           ("Climat", "À Dijon-Longvic : 61,5 jours de gel et 8,3 jours sans dégel par an, 743,4 mm de pluie et 29,8 jours de "
                      "rafales d’au moins 58 km/h (" + L("Météo-France", _MF) + ", normales 1991-2020).")],
    trades_intro="Pierre de Bourgogne et toits de petites tuiles : dans le centre et les faubourgs, deux règlements fixent les matériaux.",
    trades={
        "toiture": ["Dans le secteur sauvegardé, le plan rappelle que les petites tuiles colorées et vernissées font l’originalité des "
                    "toits bourguignons, et fait choisir le matériau édifice par édifice. Tuile mécanique, ardoise posée sur la "
                    "diagonale, fibrociment, tôle ondulée et zinc apparent y sont interdits. Pour des tuiles neuves, le panachage des "
                    "teintes est exigé (" + L("plan de sauvegarde", _PSMV) + ").",
                    "L’ardoise doit y être de schiste naturel, de teinte proche de celle d’Angers-Trélazé : le plan écarte les ardoises "
                    "importées qui ne résistent pas aux gels de la région. Les chiens-assis sont interdits, et les lucarnes "
                    "s’accordent à la façade en dimension, forme et matériau (" + L("plan de sauvegarde", _PSMV) + "). À "
                    "Dijon-Longvic, il gèle 61,5 jours par an."],
        "facade": ["Dans le secteur sauvegardé, la pierre de taille ne se peint pas, et ses joints se refont au mortier de chaux sans "
                   "ciment, au nu de la pierre. Une pierre remplacée se choisit après recherche en carrières de Bourgogne. Les façades "
                   "enduites le sont de préférence à la chaux grasse et aux sables colorés. Le sablage, les enduits au mortier de "
                   "ciment gris et les enduits plastiques sont proscrits (" + L("plan de sauvegarde", _PSMV) + ").",
                   "Rue de la Liberté, entre la place François-Rude et la place de la Libération, la Ville finance 50 % hors taxes des "
                   "ravalements, jusqu’à 250 €/m², sur 17 immeubles protégés au titre des monuments historiques. L’opération court "
                   "jusqu’en avril 2027 (" + L("Ville de Dijon", _FACADES) + ")."],
        "fenetres": ["Dans le secteur sauvegardé, les menuiseries se refont à l’identique quand le modèle d’origine existe, sinon d’après "
                     "un immeuble du même type et de la même époque, et le dossier doit montrer le modèle. Elles sont peintes d’un ton "
                     "adapté à l’époque : le plan rappelle que toutes les menuiseries anciennes étaient en bois peint ("
                     + L("plan de sauvegarde", _PSMV) + ").",
                     "Dans les faubourgs, le PVC est interdit sur les bâtiments remarquables, et vu de la rue sur les bâtiments "
                     "caractéristiques. Sur les autres constructions, il reste refusé en façade visible, sauf pour remplacer un élément "
                     "déjà en PVC, et le blanc est exclu sauf parti d’origine (" + L("règlement des faubourgs", _AVAP) + ")."],
        "charpente": ["Dans le secteur sauvegardé, les toits gardent ou retrouvent leur pente d’origine. Un édifice en petites tuiles le "
                      "reste sur ses deux versants, pour équilibrer la charpente, et les tuiles anciennes de récupération vont d’abord "
                      "sur les parties visibles (" + L("plan de sauvegarde", _PSMV) + ").",
                      "Les façades à pans de bois peuvent y être dégagées si leur intérêt archéologique est démontré. Le bois d’ossature "
                      "reçoit alors un traitement insecticide et fongicide avant d’être protégé, avec un colombage pas trop foncé, "
                      "accordé à l’enduit de remplissage (" + L("plan de sauvegarde", _PSMV) + ")."],
        "isolation": ["Dans les faubourgs, un bâtiment remarquable ne s’isole par l’extérieur qu’avec des procédés traditionnels, enduit "
                      "à la chaux ou bardage, conformes à son style. Sur les autres constructions, l’isolation extérieure doit respecter "
                      "l’architecture, et des brise-soleil peuvent être autorisés (" + L("règlement des faubourgs", _AVAP) + ").",
                      "La copropriété Arquebuse, 108 logements construits en 1960, a voté en 2021 une rénovation de niveau BBC : combles, "
                      "façades isolées par l’extérieur, menuiseries et ventilation (" + L("Dijon métropole", _COPRO) + "). Les "
                      "conseillers Rénovéco accompagnent gratuitement ce type de projet."]},
    steps_intro="Dans l’ordre, du secteur sauvegardé aux faubourgs.",
    steps=[("Repérez votre secteur", "Secteur sauvegardé ou faubourgs : les plans et règlements sont en ligne ("
                                     + L("Dijon métropole", _SPR) + "). Dans un périmètre délimité des abords, l’avis de "
                                     "l’architecte des Bâtiments de France s’impose (" + L("Dijon métropole", _PDA) + ")."),
           ("Prenez un rendez-vous technique", "Le service Droit des sols de Dijon métropole reçoit sur rendez-vous les mardis et "
                                               "jeudis, pour 20 minutes, avant le dépôt (" + L("prise de rendez-vous", _RDV) + ")."),
           ("Déposez la déclaration préalable", "Pour un bien à Dijon, le dossier se dépose directement à Dijon métropole, 40 avenue du "
                                                "Drapeau, et non en mairie, ou en ligne sur le " + L("guichet unique", _GUICHET)
                                                + ". 03 80 50 35 35 (" + L("Dijon métropole", _DDS) + ")."),
           ("Faites autoriser l’échafaudage", "Échafaudage, palissade, benne ou dépôt de matériaux sur l’espace public : demande en "
                                              "ligne à la Ville au moins 15 jours avant (" + L("démarche", _ODP) + "). Mairie : 03 80 74 51 51."),
           ("Passez par Rénovéco", "Conseil gratuit sur les travaux et les aides, sur rendez-vous, avant de signer un devis. 03 80 48 89 89.")],
    aides_intro="Rénovéco est le service public de conseil de la métropole : passez-y avant de signer un devis.",
    aides=[("Rénovéco-Dijon métropole", "L’Espace Conseil France Rénov’ des 23 communes de la métropole ("
                                        + L("France Rénov’", _FR) + ") : conseil gratuit, objectif et personnalisé, sur rendez-vous. "
                                        "1 boulevard Voltaire, 21000 Dijon. 03 80 48 89 89. " + L("dijon-metropole.fr", _RENOVECO) + "."),
           ("Opération Façades Liberté", "La Ville finance 50 % hors taxes des travaux sur les 17 immeubles de la rue de la Liberté "
                                         "dite « des arcades » : jusqu’à 250 €/m² de ravalement, 15 000 € pour les menuiseries des "
                                         "étages et 3 000 € pour les cheminées. Devantures : 40 %, jusqu’à 25 000 € HT par commerce. "
                                         "Jusqu’en avril 2027. URBANIS : 03 80 71 17 12 (" + L("Ville de Dijon", _FACADES) + ")."),
           ("Copropriétés", "Un conseiller Rénovéco référent copropriété accompagne les copropriétés à chaque étape d’une rénovation "
                            "globale, de la définition du projet aux travaux. 03 80 59 12 80 (" + L("Dijon métropole", _COPRO) + ")."),
           NATIONAL],
    faq=[("Quelles règles dans le secteur sauvegardé de Dijon ?",
          "Le centre historique, 97 hectares, suit un plan de sauvegarde approuvé en 1990 qui remplace le PLUi-HD. Tout projet doit le "
          "respecter, avec l’avis de l’architecte des Bâtiments de France. Le plan y interdit notamment la tuile mécanique, l’ardoise "
          "posée sur la diagonale et les enduits au mortier de ciment gris."),
         ("Quelles tuiles pour un toit dans le centre de Dijon ?",
          "Le plan de sauvegarde rappelle que les petites tuiles colorées et vernissées font l’originalité des toits bourguignons, et "
          "fait choisir le matériau édifice par édifice. Pour des tuiles neuves, le panachage des teintes est exigé. Un édifice en "
          "petites tuiles le reste sur ses deux versants."),
         ("Peut-on poser des fenêtres en PVC à Dijon ?",
          "Dans le secteur sauvegardé, les menuiseries se refont à l’identique ou d’après un modèle de la même époque, et le plan "
          "rappelle qu’elles étaient toutes en bois peint. Dans les faubourgs, le PVC est interdit sur les bâtiments remarquables, et "
          "vu de la rue sur les bâtiments caractéristiques."),
         ("Quelles aides pour ravaler une façade rue de la Liberté ?",
          "L’opération Façades Liberté finance 50 % hors taxes des travaux, jusqu’à 250 €/m² de ravalement, sur les 17 immeubles des "
          "arcades, entre la place François-Rude et la place de la Libération. Elle court jusqu’en avril 2027. Renseignements chez "
          "URBANIS : 03 80 71 17 12."),
         ("Où déposer une déclaration préalable à Dijon ?",
          "Directement à Dijon métropole, 40 avenue du Drapeau, et non en mairie, ou en ligne sur le guichet unique. Un rendez-vous "
          "technique est possible les mardis et jeudis. 03 80 50 35 35."),
         ("Dijon est-elle exposée aux risques naturels ?",
          "Un plan de prévention approuvé le 7 décembre 2015 couvre les inondations et les mouvements de terrain, dont le "
          "retrait-gonflement des argiles. Le risque sismique est très faible : zone 1.")],
)

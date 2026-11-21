from villes_data import L, S, SP, NATIONAL  # liens dans le texte, sources discrètes, Service-Public, aides nationales
PUBLISH = "2026-12-05"  # vague 2 : publication deux semaines après la vague 1 (voir VILLES.md)

# Sources consultées le 21/11/2026. Les pages insee.fr répondent en erreur 500 ce jour : chiffres pris par l'API Melodi (RP 2023).
# Le règlement de la ZPPAUP (orleans.fr) a un texte illisible (polices mal encodées) : ses prescriptions ne sont pas reprises.
# Aucun arrêté termites n'a été trouvé pour le Loiret : le point est laissé de côté.
_INSEE = "https://api.insee.fr/melodi/data/DS_RP_LOGEMENT_PRINC?GEO=COM-45234"  # dossier complet, RP 2023
_RAV = "https://www.orleans.fr/demarches-et-services/urbanisme-habitat/campagne-de-ravalement"
_GUIDE = "https://www.orleans.fr/fileadmin/orleans/MEDIA/document/urbanisme/entretien_patrimoine/RAVALEMENT.pdf"  # les 9 étapes du ravalement
_PATRI = "https://www.orleans.fr/demarches-et-services/urbanisme-habitat/entretien-du-patrimoine"
_CARTE = "https://mapo.orleans-metropole.fr/exb/urba/Ravalement_Facade_Orleans/"
_PLUM = "https://www.orleans-metropole.fr/actions-et-services/grands-projets-urbains/consulter-le-plum"
_PLUM_DOC = "https://www.orleans-metropole.fr/fileadmin/orleans-metropole/MEDIA/document/urbanisme/plan_local_urbanisme_metropolitain/PLUM/PIECES_5.0.0/"
_REGL = _PLUM_DOC + "5.1.12.a_-_Cahier_communal_Orleans__volet_reglementaire__M3.pdf"  # cahier communal, volet réglementaire
_ANN = _PLUM_DOC + "5.1.12.b_-_Cahier_communal_d_Orleans__annexes_informatives__M2.pdf"  # cahier communal, annexes informatives
_PPRI = ("https://www.loiret.gouv.fr/actions-de-letat/securite-et-risques/securite-civile-risques-et-protection-des-populations/"
         "prevention-et-gestion-des-risques/risques-naturels/inondations/plan-de-prevention-des-risques-dinondation-ppri")
_PPRI_NOTE = "https://www.loiret.gouv.fr/sites/default/files/contenu/telechargement/39868/285153/file/1-%20Note-pr%C3%A9sentation.pdf"
_MF = "https://donneespubliques.meteofrance.fr/FichesClim/FICHECLIM_45055001.pdf"  # station Orléans, normales 1991-2020
_CAV = "https://georisques.gouv.fr/api/v1/cavites?code_insee=45234&page_size=100"
_RISQ = "https://georisques.gouv.fr/api/v1/gaspar/risques?code_insee=45234"
_CATNAT = "https://georisques.gouv.fr/api/v1/gaspar/catnat?code_insee=45234&page_size=100"
_UDAP = "https://www.culture.gouv.fr/Regions/Drac-Centre-Val-de-Loire/Nos-secteurs-d-activite/Les-unites-departementales-de-l-architecture-et-du-patrimoine-UDAP"
_AU = "https://www.orleans.fr/demarches-et-services/urbanisme-habitat/autorisations-durbanisme-sur-orleans"
_ODP = "https://www.orleans-metropole.fr/fileadmin/orleans/MEDIA/editorial/deplacement/travaux_voirie/occupation_tarifs.pdf"  # tarifs 2026
_MMR = "https://www.orleans-metropole.fr/actions-et-services/habitat-et-urbanisme/renovation-energetique-des-habitations-ma-metro-renov"
_ADIL = "https://www.anil.org/adil-45-28/"
_ANIL_BBC = "https://www.anil.org/aides-locales-travaux/details/loiret-prime-renovation-bbc-4551/"
_ANIL_BIO = "https://www.anil.org/aides-locales-travaux/details/loiret-materiaux-biosources-4552/"

CITY = dict(
    slug="orleans", name="Orléans", cp="45000", insee="45234",
    lat=47.9022, lon=1.9042, dept="Loiret", depcode="45", region="Centre-Val de Loire",
    wiki="https://fr.wikipedia.org/wiki/Orl%C3%A9ans", wikidata="Q6548",
    verified="2026-11-21",
    tldr="À Orléans, la Mairie peut imposer le ravalement dans le site patrimonial remarquable du centre et le subventionne jusqu’à 35 %, "
         "et Géorisques recense 700 cavités souterraines sous la commune",
    hook="Ravalement aidé jusqu’à 35 % dans le centre protégé.",
    title="Devis travaux à Orléans : toiture, façade, fenêtres, isolation",
    desc="Travaux à Orléans : centre protégé, ravalement aidé à 35 %, zone inondable de la Loire, 700 cavités, primes de la Métropole. Un seul artisan vient chiffrer.",
    figures_intro="Ce qui compte avant de lancer des travaux à Orléans, du centre médiéval aux pavillons de La Source.",
    figures=[("76,1 <small>%</small>", "des logements sont des appartements", S("Insee, 2023", _INSEE)),
             ("42,2 <small>%</small>", "des résidences principales datent d’avant 1971", S("Insee, 2023", _INSEE)),
             ("35 <small>%</small>", "du ravalement subventionné par la Ville dans le site patrimonial remarquable", S("Ville d’Orléans", _RAV)),
             ("700", "cavités souterraines recensées, dont 483 carrières et 200 caves", S("Géorisques", _CAV))],
    answer=("À Orléans, 76,1 % des logements sont des appartements et 42,2 % des résidences principales datent d’avant 1971 (Insee, 2023). "
            "Dans le site patrimonial remarquable du centre, la Mairie peut imposer le ravalement et le subventionne jusqu’à 35 % hors taxes, "
            "sous le contrôle de l’architecte des Bâtiments de France. Le plan de prévention des risques d’inondation du Val d’Orléans "
            "s’applique depuis le 20 janvier 2015."),
    facts=[("Centre protégé", "Une ZPPAUP protège le centre-ville depuis 2008 (" + L("PLU métropolitain", _ANN) + "). Devenue site patrimonial "
                              "remarquable, elle a un règlement en sept secteurs (" + L("Ville d’Orléans", _PATRI) + "), et l’avis de "
                              "l’architecte des Bâtiments de France accompagne chaque autorisation de ravalement (" + L("guide du ravalement", _GUIDE) + ")."),
           ("Ravalement", "La Mairie peut notifier un ravalement obligatoire dans ce périmètre, élargi en 2012. Tout propriétaire qui ravale de "
                          "lui-même peut aussi recevoir jusqu’à 35 % du montant hors taxes, maîtrise d’œuvre comprise (" + L("Ville d’Orléans", _RAV) + ")."),
           ("Urbanisme", "Le PLU métropolitain est approuvé depuis le 7 avril 2022 et a été modifié pour la dernière fois le 10 juillet 2025 ("
                         + L("Orléans Métropole", _PLUM) + "). Son cahier communal fixe à Orléans l’aspect des façades, des toitures et des clôtures."),
           ("Inondation", "Le plan de prévention des risques d’inondation du Val d’Orléans, agglomération orléanaise, est approuvé par arrêté "
                          "préfectoral du 20 janvier 2015, avec deux cartes de zonage pour Orléans (" + L("préfecture du Loiret", _PPRI) + "). "
                          "Ses plus hautes eaux connues sont celles des crues de 1846, 1856 et 1866 (" + L("note de présentation", _PPRI_NOTE) + ")."),
           ("Sous-sol", "Géorisques recense 700 cavités souterraines sur la commune, dont 483 carrières, 200 caves et 10 cavités naturelles ("
                        + L("cavités", _CAV) + "). Les affaissements liés aux anciennes carrières et les tassements différentiels font partie des "
                        "risques de la commune (" + L("Géorisques", _RISQ) + ")."),
           ("Climat", "À la station Météo-France d’Orléans, 635,5 mm de pluie par an, 109,4 jours de pluie, 48,6 jours de gel et 48,4 jours de "
                      "rafales d’au moins 58 km/h (" + L("Météo-France", _MF) + ", normales 1991-2020).")],
    trades_intro="Maisons à pans de bois du centre médiéval, immeubles des rues Royale et Jeanne-d’Arc, pavillons de La Source : le cahier communal du PLU métropolitain règle l’aspect de chacun.",
    trades={
        "toiture": ["À Orléans, les toitures traditionnelles en ardoise ou en tuile de terre cuite petit moule doivent être conservées, et une "
                    "réfection respecte les pentes et les matériaux d’origine. Ardoise, tuile de terre cuite et zinc sont les couvertures à "
                    "privilégier (" + L("cahier communal du PLU métropolitain", _REGL) + ").",
                    "Dans les zones pavillonnaires de La Source, les toits à pans sont d’aspect ardoise, posée droite : la pose en losange y est "
                    "interdite. Partout, les châssis de toit et les cadres de panneaux solaires sont de teinte foncée, dans le plan de la toiture, "
                    "et les ouvertures de combles ne dépassent pas le tiers de la longueur du toit."],
        "facade": ["La pierre de taille et la brique prévues pour rester apparentes sont conservées. Les enduits blanc pur ou de teinte vive et les "
                   "finitions rustique, tyrolienne ou écrasée sont interdits. Sur un immeuble d’intérêt patrimonial, on passe un badigeon ou on "
                   "nettoie à l’eau plutôt que de peindre l’enduit (" + L("cahier communal du PLU métropolitain", _REGL) + ").",
                   "Dans le site patrimonial remarquable, une expertise patrimoniale de la façade précède le ravalement, qui vise son état "
                   "historique. La Ville verse jusqu’à 35 % du montant hors taxes une fois les travaux jugés conformes par l’architecte des "
                   "Bâtiments de France (" + L("Ville d’Orléans", _RAV) + ")."],
        "fenetres": ["Sur rue, les ouvertures d’origine sont conservées et la suppression des volets qui animent la façade est interdite. Les "
                     "coffres de volets roulants se posent au nu intérieur du mur, y compris lors d’un changement de menuiseries ("
                     + L("cahier communal du PLU métropolitain", _REGL) + ").",
                     "Sur les bâtiments remarquables repérés par le PLU métropolitain, les fenêtres, volets et persiennes traditionnels sont "
                     "conservés tant que leur état le permet. Lors d’un ravalement dans le site patrimonial remarquable, la couleur des menuiseries "
                     "se valide sur place avec les services de la Mairie (" + L("guide du ravalement", _GUIDE) + ")."],
        "charpente": ["Le centre médiéval compte des façades à pans de bois. Un arrêté municipal de 1824 enjoignait de les couvrir de lattes et de "
                      "plâtre contre le feu (" + L("cahier communal, annexes", _ANN) + ") : sous un enduit ancien, la structure peut être en bois, "
                      "à faire vérifier avant de toucher à la façade ou à la toiture.",
                      "La commune a été reconnue neuf fois en catastrophe naturelle pour sécheresse, de 1989 à 2020 (" + L("Géorisques", _CATNAT)
                      + "), et son sous-sol compte 483 anciennes carrières recensées. Sur une maison fissurée, faites diagnostiquer la structure "
                        "avant de refaire la charpente."],
        "isolation": ["Ma Métro Rénov’ verse 2 000 € par logement pour une isolation en matériaux biosourcés, hors combles perdus, sans condition "
                      "de ressources (" + L("ANIL", _ANIL_BIO) + "), et 10 000 € pour une rénovation qui atteint l’étiquette A ou B, sous "
                      "conditions de ressources ou de conventionnement. Ces primes sont ouvertes jusqu’au 31 décembre 2026 (" + L("ANIL", _ANIL_BBC) + ", 2026).",
                      "Avec une isolation par l’extérieur, les volets battants sont reposés à leur emplacement et les coffres de volets roulants "
                      "restent au nu intérieur de la façade (" + L("cahier communal", _REGL) + "). Elle demande une déclaration préalable ("
                      + L("Ville d’Orléans", _AU) + ")."]},
    steps_intro="Dans l’ordre, du périmètre protégé à la redevance de trottoir.",
    steps=[("Vérifiez si l’immeuble est dans le site patrimonial remarquable", "La " + L("carte interactive", _CARTE) + " de la Ville montre le "
                                                                              "périmètre. L’architecte des Bâtiments de France y donne son avis : "
                                                                              "UDAP du Loiret, Cité administrative Coligny, bâtiment E, 131 rue du "
                                                                              "Faubourg-Bannier. 02 38 53 34 26 (" + L("UDAP", _UDAP) + ")."),
           ("Faites expertiser la façade", "Pour un ravalement dans ce périmètre, le service Habitat d’Orléans Métropole vient sur place et remet "
                                           "le cahier des charges. 02 38 78 75 67, campagne-de-ravalement@orleans-metropole.fr ("
                                           + L("Ville d’Orléans", _RAV) + ")."),
           ("Déposez la déclaration préalable", "En ligne sur le guichet unique de la Métropole, ou sur rendez-vous avec le pôle Instruction des "
                                                "autorisations d’urbanisme, à l’Espace Saint-Marc, 5 place du 6-Juin-1944. 02 38 79 25 80 ("
                                                + L("Ville d’Orléans", _AU) + ")."),
           ("Faites autoriser l’échafaudage", "Le dossier se dépose 15 jours ouvrés avant le chantier, à desp-odp@orleans-metropole.fr ou au guichet "
                                              "n° 9 de la mairie. En 2026, la redevance est de 7,93 € par m² et par quinzaine (" + L("tarifs 2026", _ODP) + ")."),
           ("Demandez les aides avant de commencer", "Les aides de la Métropole se demandent avant le début des travaux, confiés à des "
                                                     "professionnels, certifiés RGE pour l’énergie (" + L("Ma Métro Rénov’", _MMR) + ").")],
    aides_intro="À Orléans, la Ville aide le ravalement et la Métropole la rénovation énergétique.",
    aides=[("Ma Métro Rénov’", "Le service public de la rénovation d’Orléans Métropole, porté par l’ADIL du Loiret, dont les conseillers France "
                               "Rénov’ conseillent gratuitement (" + L("ADIL", _ADIL) + "). Sur rendez-vous, 1 bis rue Saint-Euverte, 45000 Orléans. "
                               "02 38 81 37 07. " + L("orleans-metropole.fr", _MMR) + "."),
           ("Subvention au ravalement", "Dans le site patrimonial remarquable, la Ville verse jusqu’à 35 % du montant hors taxes des travaux et de "
                                        "la maîtrise d’œuvre, après une expertise patrimoniale et le contrôle de l’architecte des Bâtiments de "
                                        "France. Service Habitat : 02 38 78 75 67 (" + L("Ville d’Orléans", _RAV) + ")."),
           ("Primes Ma Métro Rénov’", "Audit énergétique financé à 50 %, jusqu’à 500 € par logement. 10 000 € pour atteindre l’étiquette A ou B, "
                                      "sous conditions. 2 000 € pour une isolation biosourcée et 1 000 € pour remplacer un chauffage au bois "
                                      "polluant, sans condition de ressources (" + L("Orléans Métropole", _MMR) + "). Les primes BBC et biosourcée "
                                      "sont ouvertes jusqu’au 31 décembre 2026 (" + L("ANIL", _ANIL_BBC) + ", mise à jour de mars 2026)."),
           ("Ma Métro Rénov’+ Carmes-Madeleine", "Dans ce quartier, Orléans Métropole et l’Anah accompagnent les propriétaires avec des aides "
                                                 "renforcées, depuis 2019 et jusqu’en octobre 2030 (" + L("Orléans Métropole", _MMR) + ")."),
           NATIONAL],
    faq=[("Le ravalement est-il obligatoire à Orléans ?",
          "Dans le site patrimonial remarquable, la Mairie peut notifier un ravalement obligatoire, et ce périmètre a été élargi en 2012. Tout "
          "propriétaire du périmètre peut aussi ravaler de lui-même et recevoir jusqu’à 35 % du montant hors taxes."),
         ("Quels enduits et quelles couleurs pour une façade à Orléans ?",
          "Le PLU métropolitain interdit les enduits blanc pur ou de teinte vive et les finitions rustique, tyrolienne ou écrasée. La pierre de "
          "taille et la brique prévues pour être vues restent apparentes."),
         ("Faut-il une autorisation pour changer ses fenêtres à Orléans ?",
          "Oui, une déclaration préalable, comme pour une réfection de toiture ou une isolation par l’extérieur. Sur rue, les ouvertures d’origine "
          "sont conservées et les coffres de volets roulants se posent au nu intérieur du mur."),
         ("Orléans est-elle en zone inondable ?",
          "En partie. Le plan de prévention des risques d’inondation du Val d’Orléans, approuvé le 20 janvier 2015, s’applique avec deux cartes "
          "de zonage pour la commune. Ses plus hautes eaux connues sont celles des crues de 1846, 1856 et 1866."),
         ("Y a-t-il des carrières sous Orléans ?",
          "Oui. Géorisques recense 700 cavités souterraines sur la commune, dont 483 carrières et 200 caves. Renseignez-vous sur votre parcelle "
          "avant une extension ou une reprise de structure."),
         ("Quelles aides pour rénover son logement à Orléans ?",
          "Jusqu’à 35 % du ravalement dans le site patrimonial remarquable, puis les primes Ma Métro Rénov’ : 10 000 € pour une rénovation BBC, "
          "2 000 € pour une isolation biosourcée, jusqu’au 31 décembre 2026. Conseil gratuit au 02 38 81 37 07.")],
)

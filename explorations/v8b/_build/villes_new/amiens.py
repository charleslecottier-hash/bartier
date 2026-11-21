from villes_data import L, S, SP, NATIONAL  # liens dans le texte, sources discrètes, Service-Public, aides nationales
PUBLISH = "2026-12-05"  # vague 2 : publication deux semaines après la vague 1 (voir VILLES.md)

# Sources consultées le 21/11/2026.
_INSEE = "https://api.insee.fr/melodi/data/DS_RP_LOGEMENT_PRINC?GEO=COM-80021"  # dossier complet, RP 2023 (page insee.fr en erreur 500 ce jour)
_GPU = "https://www.geoportail-urbanisme.gouv.fr/api/document/883081132359e22e6420a7a878988dbb/files/"
_PROC = _GPU + "80021_procedure_20251211.pdf"  # délibération du 11 décembre 2025 approuvant le PLU révisé
_PLU = _GPU + "80021_reglement_20251211.pdf"
_GUIDE = _GPU + "80021_guide_facade_20251211.pdf"  # annexe 3.14, guide de rénovation des façades
_OAP = _GPU + "80021_OAP_2_20251211.pdf"  # OAP thématique patrimoine (fiche « Les amiénoises »)
_URBA = "https://www.amiens.fr/Vivre-a-Amiens/Urbanisme-Logement/Renovation-construction-extension-les-autorisations-d-urbanisme"
_GNAU = "https://urbanisme.amiens-metropole.com/gnau/?ref=#/"
_RENOV = "https://www.amiens.fr/Vivre-a-Amiens/Urbanisme-Logement/Etre-accompagne-pour-la-renovation-de-son-logement"
_FR = "https://france-renov.gouv.fr/preparer-projet/trouver-conseiller"  # annuaire officiel : LAURE pour Amiens (Insee 80021)
_ODP = "https://www.amiens.fr/Liens-utiles/Mes-demarches/Demandes-d-Occupation-du-Domaine-Public/Demande-d-autorisation-d-occupation-du-domaine-public"
_PREF_TM = "https://www.somme.gouv.fr/Actions-de-l-Etat/Habitat-et-construction/Le-batiment/Termites-et-Merules"  # + carte mérule d'octobre 2026
_MF = "https://donneespubliques.meteofrance.fr/FichesClim/FICHECLIM_80379002.pdf"  # Amiens-Glisy, normales 1991-2020
_CATNAT = "https://georisques.gouv.fr/api/v1/gaspar/catnat?code_insee=80021"
_TRI = "https://georisques.gouv.fr/api/v1/gaspar/tri?code_insee=80021"
_UDAP = "https://lannuaire.service-public.gouv.fr/hauts-de-france/somme/9fbb80a5-e181-4faf-9775-6597f0253c88"
_PASS = "https://www.pass-renovation.hautsdefrance.fr/media/files/f-3-4-spee-flyer-particuliers-2026.pdf"

CITY = dict(
    slug="amiens", name="Amiens", cp="80000", insee="80021",
    lat=49.8919, lon=2.2978, dept="Somme", depcode="80", region="Hauts-de-France",
    wiki="https://fr.wikipedia.org/wiki/Amiens", wikidata="Q41604",
    verified="2026-11-21",
    tldr="À Amiens, le PLU approuvé le 11 décembre 2025 interdit de peindre la brique et donne une palette de couleurs à chacun des dix quartiers "
         "anciens, et la Ville comme la Métropole complètent les aides de l’Anah",
    hook="Brique des « amiénoises », une palette de couleurs par quartier, aides de la Ville et de la Métropole.",
    title="Devis travaux à Amiens : toiture, façade, fenêtres, isolation",
    desc="Travaux à Amiens : PLU de 2025, brique des amiénoises, palette de couleurs par quartier, aides de la Ville et de la Métropole. Un seul artisan vient chiffrer.",
    figures_intro="Ce qui compte avant de lancer des travaux à Amiens, de Saint-Leu aux anciens faubourgs.",
    figures=[("33,7 <small>%</small>", "des logements sont des maisons", S("Insee, 2023", _INSEE)),
             ("47,5 <small>%</small>", "des résidences principales datent d’avant 1971", S("Insee, 2023", _INSEE)),
             ("10 <small>palettes</small>", "de couleurs de façade, une par quartier, annexées au PLU", S("Ville d’Amiens, PLU 2025", _GUIDE)),
             ("45,4 <small>jours</small>", "de gel par an à Amiens-Glisy", S("Météo-France, normales 1991-2020", _MF))],
    answer=("À Amiens, 33,7 % des logements sont des maisons, dont beaucoup d’« amiénoises » en brique dans les anciens faubourgs, et 47,5 % des "
            "résidences principales datent d’avant 1971. Le PLU approuvé le 11 décembre 2025 interdit de peindre la brique et fixe une palette de "
            "couleurs par quartier. En complément de l’Anah, la Ville et la Métropole aident chacune un propriétaire occupant jusqu’à 1 400 €."),
    facts=[("Urbanisme", "Le conseil municipal a approuvé le PLU révisé de la Ville le 11 décembre 2025. Il remplace le PLU de 2006, après une révision "
                         "lancée le 28 janvier 2021 (" + L("délibérations", _PROC) + ")."),
           ("Déclaration préalable", "Modifier une façade, une toiture, des menuiseries ou une clôture demande une déclaration préalable. À Amiens, "
                                     "toute démolition, même partielle, demande un permis de démolir (" + L("Ville d’Amiens", _URBA) + ")."),
           ("Couleurs", "Le guide de rénovation des façades annexé au PLU donne une palette pour chacun de dix quartiers : Hem, Henriville, Saint-Honoré, "
                        "La Vallée, Saint-Leu, Saint-Acheul, Sainte-Anne, Saint-Maurice, Saint-Pierre et Saint-Roch, avec dix teintes de joints ("
                        + L("guide des façades", _GUIDE) + ")."),
           ("Patrimoine", "Le PLU classe des bâtiments en patrimoine emblématique, remarquable ou identifié, et fixe des règles par type : maisons à "
                          "colombages, « amiénoises » de 1825 à 1940, quartier anglais, immeubles de 1945 à 1957. Sur le patrimoine emblématique, "
                          "l’isolation par l’extérieur est interdite (" + L("règlement du PLU", _PLU) + ")."),
           ("Termites et mérule", "Aucun arrêté termites dans la Somme. Le dernier arrêté mérule vise 21 communes du département, dont Abbeville, Albert "
                                  "et Conty, mais pas Amiens (" + L("préfecture de la Somme", _PREF_TM) + ", carte d’octobre 2026)."),
           ("Eau et climat", "Amiens est un territoire à risque important d’inondation, cartographié en 2014 (" + L("Géorisques", _TRI) + "). La ville a été "
                             "reconnue en catastrophe naturelle pour les remontées de nappe du 3 décembre 2000 au 25 avril 2001 (" + L("arrêtés", _CATNAT)
                             + "). À Amiens-Glisy, il pleut 114,9 jours par an (" + L("Météo-France", _MF) + ").")],
    trades_intro="Maisons à colombages, « amiénoises » de brique, grandes demeures, immeubles d’après-guerre : le PLU fixe des règles pour chacune.",
    trades={
        "toiture": ["Les « amiénoises » d’avant 1914 ont un toit à deux pans, en tuiles ou en ardoises, souvent sur des combles mansardés ("
                    + L("OAP patrimoine", _OAP) + "). Sur les maisons repérées par le PLU, une lucarne visible de la rue se centre sur la toiture ou "
                    "s’aligne sur les baies des étages, et les panneaux solaires suivent la pente du toit (" + L("règlement du PLU", _PLU) + ").",
                    "Amiens-Glisy compte 39,5 jours de rafales d’au moins 58 km/h par an, surtout de décembre à mars, et 114,9 jours de pluie. "
                    "Faites contrôler tuiles, rives et descentes d’eau dès l’automne (" + L("Météo-France", _MF) + ")."],
        "facade": ["Le PLU impose de nettoyer la brique par sablage ou hydrogommage et interdit de la peindre. Un badigeon coloré peut être admis si la brique "
                   "est trop abîmée. Ses recommandations écartent la haute pression, les détergents chimiques et la meuleuse, et conseillent un "
                   "micro-gommage de 2,5 à 3 bars au plus (" + L("règlement du PLU", _PLU) + ").",
                   "Les joints suivent la teinte de la brique, ni trop clairs ni trop foncés, de préférence au mortier de chaux naturelle légèrement rosé "
                   "par de la brique pilée. Chaque quartier a sa palette de façades et de joints dans le guide annexé au PLU (" + L("guide des façades", _GUIDE) + ")."],
        "fenetres": ["Changer des menuiseries demande une déclaration préalable. Sur les maisons d’avant 1940 repérées par le PLU, les fenêtres visibles de la "
                     "rue gardent les sections, la répartition des ouvrants et les détails d’origine (imposte, petits bois, jet d’eau). Toutes les fenêtres "
                     "d’une même façade ont la même teinte (" + L("règlement du PLU", _PLU) + ").",
                     "Sur les « amiénoises », les menuiseries en bois sont souvent peintes d’une teinte claire, qui contraste avec la porte d’entrée ("
                     + L("OAP patrimoine", _OAP) + "). Le PLU demande des portes d’entrée de ton soutenu, bleu, vert, rouge ou bois, et sur les maisons à "
                     "colombages, des volets roulants posés à l’intérieur, derrière le linteau."],
        "charpente": ["Aucun arrêté ne vise Amiens : la Somme n’a pas d’arrêté termites, et l’arrêté mérule vise 21 autres communes, dont Abbeville et "
                      "Albert. Une mérule découverte se déclare quand même en mairie, dans le mois (" + L("préfecture de la Somme", _PREF_TM) + ").",
                      "Sur les maisons à colombages, le PLU préserve la volumétrie et les pentes de toit d’origine, conserve les matériaux de couverture ou "
                      "les remplace par des matériaux similaires, et interdit l’isolation par l’extérieur. À Amiens, toute démolition, même partielle, "
                      "demande un permis de démolir (" + L("Ville d’Amiens", _URBA) + ")."],
        "isolation": ["Le PLU privilégie l’isolation par l’extérieur sur les façades enduites ou bardées, avec un débord de 30 cm au plus dans la marge de "
                      "recul. Sur une façade en brique d’avant 1940 repérée, elle n’est admise qu’à l’arrière ou en pignon, avec un parement en brique, "
                      "pierre, zinc ou bois si l’arrière se voit de la rue (" + L("règlement du PLU", _PLU) + ").",
                      "Pour un propriétaire occupant, la Ville prend 12 % du reste à charge d’une rénovation énergétique, jusqu’à 1 400 €, et la Métropole "
                      "8 %, jusqu’à 1 400 €, en complément de l’Anah (" + L("Ville d’Amiens", _RENOV) + "). La plateforme LAURE fait le calcul avec vous."]},
    steps_intro="Dans l’ordre, du règlement du PLU au chantier.",
    steps=[("Repérez votre bâtiment dans le PLU", "Patrimoine repéré, abords d’un monument historique ou site protégé : l’architecte des Bâtiments de France "
                                                 "donne son accord. UDAP de la Somme, 5 rue Henri-Daussy. 03 22 22 25 10 (" + L("annuaire", _UDAP) + ")."),
           ("Choisissez vos teintes", "Le guide de rénovation des façades donne la palette de votre quartier pour la façade, les soubassements, les joints "
                                      "et les menuiseries (" + L("guide des façades", _GUIDE) + ")."),
           ("Déposez la déclaration préalable", "En ligne sur le " + L("guichet numérique", _GNAU) + ", ou à la direction de l’urbanisme réglementaire, "
                                                "7 rue de la Malmaison, du lundi au vendredi de 9 h à 12 h 30 et de 13 h 30 à 17 h (" + L("Ville d’Amiens", _URBA) + ")."),
           ("Faites autoriser l’échafaudage", "Formulaire à envoyer à voirie.occupationDP@amiens-metropole.com au moins 15 jours ouvrés avant l’intervention. "
                                              "L’arrêté obtenu s’affiche sur le chantier (" + L("démarche", _ODP) + ")."),
           ("Appelez LAURE avant de signer", "Conseil gratuit sur les travaux, les démarches et les aides, sur rendez-vous en centre-ville.")],
    aides_intro="LAURE oriente vers chaque aide, et la Ville comme la Métropole ajoutent les leurs à celles de l’Anah.",
    aides=[("LAURE, Amiens Métropole", "L’Espace Conseil France Rénov’ d’Amiens Métropole, ouvert à tous sans condition de ressources : 1 place Léon-Gontier, "
                                      "80000 Amiens. 03 22 97 40 40, du lundi au vendredi de 9 h à 12 h et de 14 h à 17 h, conseils sur rendez-vous ("
                                      + L("Ville d’Amiens", _RENOV) + ", " + L("annuaire France Rénov’", _FR) + ")."),
           ("Rénovation énergétique", "En complément de l’Anah, la Ville verse 12 % du reste à charge et la Métropole 8 %, chacune plafonnée à 1 400 € pour un "
                                      "propriétaire occupant et à 1 000 € pour un bailleur. Ces aides se cumulent (" + L("Ville d’Amiens", _RENOV) + ")."),
           ("Logement dégradé, vacant ou divisé", "La Métropole finance 20 % des travaux hors taxes sur un habitat dégradé, jusqu’à 8 000 €. Remettre sur le "
                                                  "marché un logement vacant ouvre droit à 800 € de la Ville et 800 € de la Métropole, regrouper les logements "
                                                  "d’une maison divisée à 1 000 € de la Ville. Jusqu’en 2026, Soliha et Apremis montent gratuitement les "
                                                  "dossiers des propriétaires éligibles (" + L("Ville d’Amiens", _RENOV) + ")."),
           ("Hauts-de-France Pass Rénovation", "Le service de la Région avance le coût des travaux et des aides, et peut monter un éco-prêt à taux zéro, "
                                               "sans condition de revenus ni d’âge. Accompagnement payant. 03 75 14 07 01 (" + L("Pass Rénovation", _PASS) + ")."),
           NATIONAL],
    faq=[("Faut-il une autorisation pour ravaler sa façade à Amiens ?",
          "Oui : modifier une façade, une toiture, des menuiseries ou une clôture demande une déclaration préalable. Pour la brique, le PLU impose le "
          "sablage ou l’hydrogommage et interdit la peinture."),
         ("Quelles couleurs pour sa façade à Amiens ?",
          "Le guide de rénovation des façades, annexé au PLU de 2025, donne une palette par quartier, de Saint-Leu à Henriville, pour la façade, les "
          "soubassements, les joints et les menuiseries."),
         ("Peut-on isoler une amiénoise par l’extérieur ?",
          "Sur une façade en brique repérée par le PLU, seulement à l’arrière ou en pignon, avec un parement en brique, pierre, zinc ou bois si l’arrière "
          "se voit de la rue. Sur une façade enduite, le PLU privilégie au contraire l’isolation par l’extérieur."),
         ("Amiens est-elle concernée par les termites ou la mérule ?",
          "Non, aucun arrêté ne la vise. La Somme n’a pas d’arrêté termites, et Amiens ne figure pas parmi les 21 communes visées par l’arrêté mérule (carte d’octobre 2026). "
          "Une mérule découverte se déclare tout de même en mairie dans le mois."),
         ("Quelles aides pour rénover son logement à Amiens ?",
          "En complément de l’Anah, la Ville et la Métropole versent chacune une part du reste à charge, jusqu’à 1 400 € pour un propriétaire occupant. "
          "LAURE vous conseille gratuitement : 03 22 97 40 40."),
         ("Comment faire autoriser un échafaudage à Amiens ?",
          "Envoyez le " + L("formulaire d’occupation du domaine public", _ODP) + " à voirie.occupationDP@amiens-metropole.com, au moins 15 jours "
          "ouvrés avant l’intervention.")],
)

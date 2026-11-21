# Nice : fiche locale de la page « Devis travaux à Nice ». Sources officielles consultées le 21/11/2026.
# Chiffres Insee : jeu « Logements, principaux indicateurs (dossier complet) », RP 2023, lu via l'API Melodi
# (la page « dossier complet » d'insee.fr répondait en erreur 500 pendant la recherche).
from villes_data import L, S, SP, NATIONAL  # liens dans le texte, sources discrètes, Service-Public, aides nationales

_INSEE = "https://api.insee.fr/melodi/data/DS_RP_LOGEMENT_PRINC?GEO=COM-06088"
_GUIDE = "https://www.nice.fr/ressources/guide-pratique-du-ravalement-et-de-la-restauration-a-nice/"
_TRAVAUX = "https://www.nice.fr/fr/particuliers/faire-des-travaux"
_DP = "https://www.nice.fr/demarches/faire-une-declaration-prealable-de-travaux/"
_SPR = "https://immobilier.nicecotedazur.org/system/documents/pdfs/000/001/296/original/AVAP_reglmt_site_patrimone_remarquable.pdf"
_SPR_RP = "https://www.nicecotedazur.org/wp-content/uploads/2021/07/avap/AVAP%20NICE_RAPPORT%20DE%20PRESENTATION.pdf"
_UNESCO = "https://www.nice.fr/fr/actualites/nice-la-ville-de-la-villegiature-d-hiver-de-riviera-inscrite-sur-la-liste-du-patrimoine-mondial"
_UDAP = ("https://www.culture.gouv.fr/regions/Drac-Provence-Alpes-Cote-d-Azur/La-Direction-regionale-des-affaires-culturelles-DRAC-Provence-Alpes-Cote-d-Azur/"
         "Unites-departementales-de-l-architecture-et-du-patrimoine-UDAP-de-Provence-Alpes-Cote-d-Azur/udap-des-alpes-maritimes")
_PLUM = "https://www.nicecotedazur.org/services/urbanisme/plum/plu-metropolitain-en-vigueur/"
_DICRIM = "https://www.nice.fr/ressources/document-dinformation-communal-sur-les-risques-majeurs-dicrim"
_TERM = "https://www.alpes-maritimes.gouv.fr/Liens-colonne-3-pied-de-page/Termites-merules"
_MF = "https://donneespubliques.meteofrance.fr/FichesClim/FICHECLIM_06088001.pdf"
_ODP = "https://www.nice.fr/type-procedure/logement-urbanisme/"
_VIAZUR = "https://www.nicecotedazur.org/services/voirie-et-espaces-publics/vos-demarches/demandes-d-autorisation-de-travaux/"
_GUICHET = "https://www.nicecotedazur.org/services/environnement/energie/le-guichet-metropolitain-de-la-renovation-energetique/"
_MDH = "https://www.nicecotedazur.org/services/logement/aides-et-subventions-a-la-renovation/proprietaire-du-logement-que-vous-habitez/"

CITY = dict(
    slug="nice", name="Nice", cp="06000", insee="06088",
    lat=43.7019, lon=7.2683, dept="Alpes-Maritimes", depcode="06", region="Provence-Alpes-Côte d’Azur",
    wiki="https://fr.wikipedia.org/wiki/Nice", wikidata="Q33959",
    verified="2026-11-21",
    tldr=("À Nice, l’architecte des Bâtiments de France est consulté dans la majeure partie de la ville, et la commune est en zone de "
          "sismicité 4 et en zone de lutte contre les termites"),
    hook="Ville largement protégée, zone sismique 4 et zone termites.",
    title="Devis travaux à Nice : toiture, façade, fenêtres, isolation",
    desc=("Travaux à Nice : Vieux-Nice et site Unesco protégés, nuancier de la Ville, zone sismique 4, termites, aide aux façades. "
          "Un seul artisan vient chiffrer."),
    figures_intro="Quatre repères pour préparer des travaux entre Vieux-Nice et collines.",
    figures=[("92,7 <small>%</small>", "des logements sont des appartements", S("Insee, 2023", _INSEE)),
             ("53,3 <small>%</small>", "des résidences principales datent d’avant 1971", S("Insee, 2023", _INSEE)),
             ("522 <small>ha</small>", "inscrits au patrimoine mondial de l’Unesco en 2021", S("Ville de Nice", _UNESCO)),
             ("791,3 <small>mm</small>", "de pluie par an, dont un tiers en octobre et novembre", S("Météo-France, normales 1991-2020", _MF))],
    answer=("À Nice, 92,7 % des logements sont des appartements et 53,3 % des résidences principales datent d’avant 1971. "
            "Dans la majeure partie de la ville, abords de monuments ou site patrimonial remarquable, l’architecte des Bâtiments de France "
            "est consulté et l’instruction d’un ravalement prend un mois de plus. La commune est aussi en zone de sismicité 4 et en zone "
            "de lutte contre les termites."),
    facts=[("Secteurs protégés", "Trois sites patrimoniaux remarquables : le Vieux-Nice, secteur sauvegardé depuis 1969 (" + L("guide du ravalement", _GUIDE) + "), le port, et environ "
                                 "600 hectares de la Promenade des Anglais aux quartiers nord (" + L("UDAP 06", _UDAP) + ", "
                                 + L("rapport de l’AVAP", _SPR_RP) + "). Ce dernier couvre les 522 hectares inscrits à l’Unesco ("
                                 + L("Ville de Nice", _UNESCO) + ")."),
           ("Ravalement", "La Ville demande une déclaration préalable pour tout ravalement, même pour repeindre une façade déjà peinte ("
                          + L("guide du ravalement", _GUIDE) + ", 2022). Respecter les teintes de son nuancier peut conditionner "
                          "l’autorisation et la subvention (" + L("Ville de Nice", _TRAVAUX) + ")."),
           ("Urbanisme", "Le PLU métropolitain de Nice Côte d’Azur s’applique depuis le 25 octobre 2019. Sa dernière modification a été "
                         "approuvée le 11 juillet 2025 (" + L("Métropole", _PLUM) + ")."),
           ("Séisme", "Zone de sismicité 4, moyenne. Un plan de prévention des risques sismiques couvre toute la commune depuis le "
                      "28 janvier 2019, avec cinq zones de B0 à B4 selon la nature du sol (" + L("DICRIM", _DICRIM) + ", 2026)."),
           ("Termites", "Nice fait partie des 42 communes des Alpes-Maritimes en zone de surveillance et de lutte contre les termites "
                        "(arrêté préfectoral du 10 mars 2017). Qui découvre des termites doit le déclarer en mairie (" + L("préfecture", _TERM) + ")."),
           ("Climat", "791,3 mm de pluie par an à la station de Nice, dont un tiers en octobre et novembre, et 1,1 jour de gel par an. "
                      "Record : 191,4 mm en une journée, le 13 octobre 1973 (" + L("Météo-France", _MF) + ", normales 1991-2020).")],
    trades_intro="Du bâti néoclassique aux immeubles des années 1980, le guide de la Ville décrit six périodes de construction, chacune avec ses matériaux.",
    trades={
        "toiture": ["Tuiles rondes ou plates, ardoise à la Mansart, dômes, toits-terrasses : Nice a presque tous les types de couverture ("
                    + L("guide du ravalement", _GUIDE) + "). Sur les immeubles repérés du site patrimonial remarquable, la couverture d’époque "
                    "est restaurée (tuile canal rouge orangé, tuile de Marseille, ardoise ou zinc) et les terrasses « tropéziennes » taillées "
                    "dans le toit sont interdites (" + L("règlement", _SPR) + ").",
                    "Octobre et novembre apportent un tiers des 791,3 mm de pluie annuels (" + L("Météo-France", _MF) + "). La plupart des "
                    "dégâts de façade viennent d’une étanchéité défaillante au-dessus : la Ville demande de vérifier couverture, liteaux et "
                    "charpente à chaque ravalement, toits-terrasses et balcons filants compris."],
        "facade": ["Le guide de la Ville décrit les façades niçoises époque par époque, jusqu’aux enduits teintés dans la masse du XXe siècle, "
                   "les « bétons colorés ». Sur les immeubles repérés du site patrimonial remarquable, les décors peints en trompe-l’œil "
                   "se conservent ou se restituent au badigeon de chaux (" + L("règlement", _SPR) + ").",
                   "Le dossier de déclaration préalable décrit les supports, le mode opératoire et les produits. La Ville peut y demander "
                   "de rétablir l’état d’origine ou un décor disparu (" + L("guide du ravalement", _GUIDE) + ", 2022)."],
        "fenetres": ["Sur les immeubles repérés du site patrimonial remarquable, une fenêtre en bois se remplace en bois massif, et poser "
                     "une fenêtre de rénovation sur l’ancien dormant est interdit. Volets roulants, persiennes et portes en PVC y sont aussi "
                     "interdits (" + L("règlement", _SPR) + ").",
                     "Partout, la Ville déconseille la pose sur l’ancien dormant : les profils en PVC, plus larges, réduisent la surface "
                     "vitrée de 20 à 30 % (" + L("guide du ravalement", _GUIDE) + "). Les climatiseurs en applique sur la façade sont "
                     "interdits sur les immeubles repérés du site patrimonial remarquable : prévoyez leur place dès le projet."],
        "charpente": ["Nice est en zone de surveillance et de lutte contre les termites sur tout son territoire (" + L("préfecture", _TERM) + "). "
                      "En démolition, même partielle, les bois contaminés sont brûlés sur place ou traités avant d’être transportés.",
                      "En zone de sismicité 4, les règles parasismiques de l’Eurocode 8 s’imposent aux projets soumis à permis de construire ("
                      "" + L("DICRIM", _DICRIM) + "). Ne déposez pas génoises ni avant-toits pour simplifier "
                      "un ravalement : la Ville rappelle que cela bouleverse la statique de la partie concernée (" + L("guide du ravalement", _GUIDE) + ")."],
        "isolation": ["L’isolation par l’extérieur est interdite dans le Vieux-Nice, et la Ville la déconseille sur les bâtiments d’avant les "
                      "années 1950 et sur les façades très ornées (" + L("guide du ravalement", _GUIDE) + "). Sur les immeubles repérés "
                      "du site patrimonial remarquable, elle peut être refusée (" + L("règlement", _SPR) + ").",
                      "À la station de Nice, 88,3 jours par an dépassent 25 °C et il gèle 1,1 jour par an (" + L("Météo-France", _MF) + "). "
                      "Le guichet métropolitain aide à choisir les travaux et estime les subventions, en priorité pour une rénovation "
                      "globale (" + L("Métropole", _GUICHET) + ")."]},
    steps_intro="Les démarches à suivre, de la vérification du secteur à la demande d’aide.",
    steps=[("Vérifiez si votre immeuble est protégé", "Vieux-Nice, port, Promenade des Anglais et quartiers nord, abords d’un monument : "
                                                     "l’architecte des Bâtiments de France est consulté. UDAP 06, villa Césarie, 41 avenue Thiers. "
                                                     "04 93 16 59 10, le matin (" + L("culture.gouv.fr", _UDAP) + ")."),
           ("Choisissez les teintes", "Dans le nuancier de la Ville : NCS pour la façade, RAL pour les ferronneries, teintes à la chaux pour "
                                      "les enduits à la chaux (" + L("guide du ravalement", _GUIDE) + ")."),
           ("Déposez la déclaration préalable", "En ligne sur le guichet e-permis, ou sur rendez-vous au service des autorisations "
                                                "d’urbanisme, Le Connexio, 7/11 avenue Giscard-d’Estaing, le lundi, le mercredi et le vendredi "
                                                "de 9 h à 12 h 30. Instruction : un mois après le dossier complet, plus si l’ABF est consulté. "
                                                "Allo Mairie : 3906 (" + L("Ville de Nice", _DP) + ")."),
           ("Faites autoriser l’échafaudage", "Une emprise de chantier sur le trottoir demande une autorisation d’occupation du domaine "
                                              "public, en ligne sur le portail Mes démarches de la Ville (" + L("démarches", _ODP) + "). "
                                              "Les travaux qui touchent la voirie passent par la plateforme Viazur de la Métropole, avec un mois "
                                              "d’instruction (" + L("Métropole", _VIAZUR) + ")."),
           ("Demandez les aides avant le chantier", "La subvention de façade doit être validée par le conseil municipal avant le début "
                                                    "des travaux. Pour l’énergie, appelez d’abord le guichet métropolitain.")],
    aides_intro="Conseil public gratuit d’abord, puis les aides locales, toujours avant le début des travaux.",
    aides=[("Guichet métropolitain de la rénovation énergétique", "Le conseil public de la Métropole Nice Côte d’Azur, gratuit et neutre, "
                                                                  "cofinancé par le Pacte territorial France Rénov’ de l’Anah. Immeuble Plaza, "
                                                                  "boulevard René-Cassin, 06200 Nice, sur rendez-vous. 04 97 13 39 44. "
                                                                  + L("nicecotedazur.org", _GUICHET) + "."),
           ("Subvention de la Ville pour les façades", "Pour un immeuble d’habitation situé dans un périmètre fixé par le conseil municipal, "
                                                       "la Ville peut financer une part du ravalement des façades visibles de la rue. Près de "
                                                       "1 500 restaurations de façades privées en ont bénéficié en dix ans, pour plus de 13 millions d’euros. "
                                                       "Renseignements au pôle Architecture et rénovation du service des autorisations "
                                                       "d’urbanisme (" + L("guide du ravalement", _GUIDE) + ", 2022)."),
           ("Aides de l’Anah avec la Métropole", "Pour les propriétaires occupants sous plafonds de ressources, le dossier se prépare avec la "
                                                 "Maison de l’Habitant, 6 allée Philippe-Séguin, 06000 Nice (tram Libération). 04 97 13 55 11 ("
                                                 + L("Métropole", _MDH) + ")."),
           NATIONAL],
    faq=[("Faut-il une autorisation pour un ravalement à Nice ?",
          "Oui. La Ville demande une déclaration préalable pour tout ravalement, même une simple remise en peinture. Dans la majeure partie "
          "de la ville, l’architecte des Bâtiments de France est consulté, et l’instruction dure un mois de plus."),
         ("Peut-on poser des fenêtres en PVC à Nice ?",
          "Pas sur les immeubles repérés du site patrimonial remarquable : une fenêtre en bois s’y remplace en bois massif, et volets roulants, "
          "persiennes et portes en PVC y sont interdits. Ailleurs, la Ville déconseille le PVC posé sur l’ancien dormant, qui réduit la surface "
          "vitrée de 20 à 30 %. Changer ses menuiseries demande une déclaration préalable."),
         ("Nice est-elle en zone sismique ?",
          "Oui, en zone 4, de sismicité moyenne. Le plan de prévention des risques sismiques approuvé le 28 janvier 2019 couvre toute la "
          "commune, avec cinq zones réglementaires selon la nature du sol."),
         ("Nice est-elle concernée par les termites ?",
          "Oui. Nice fait partie des 42 communes des Alpes-Maritimes en zone de surveillance et de lutte contre les termites depuis l’arrêté "
          "préfectoral du 10 mars 2017. Un vendeur doit annexer à l’acte un diagnostic termites datant de moins de six mois."),
         ("Peut-on isoler une façade par l’extérieur à Nice ?",
          "Pas dans le Vieux-Nice, où le règlement du secteur sauvegardé l’interdit, et elle peut être refusée sur les immeubles repérés du "
          "site patrimonial remarquable. La Ville la déconseille sur les bâtiments d’avant les années 1950 et la réserve au béton récent peu isolé."),
         ("Quelles aides pour rénover son logement à Nice ?",
          "La subvention de la Ville pour les façades, dans les périmètres votés par le conseil municipal, les aides de l’Anah préparées avec la "
          "Maison de l’Habitant (04 97 13 55 11) et les aides nationales. Conseil gratuit au guichet métropolitain : 04 97 13 39 44.")],
)

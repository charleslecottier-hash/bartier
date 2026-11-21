from villes_data import L, S, SP, NATIONAL  # liens dans le texte, sources discrètes, Service-Public, aides nationales
PUBLISH = "2026-12-05"  # vague 2 : publication deux semaines après la vague 1 (voir VILLES.md)

# Sources consultées le 21/11/2026. La fiche « dossier complet » d'insee.fr ne répondait pas ce jour-là :
# chiffres du recensement 2023 pris dans l'API Melodi de l'Insee (même jeu de données).
_INSEE = "https://api.insee.fr/melodi/data/DS_RP_LOGEMENT_PRINC?GEO=COM-29019"
_PROPRIO = "https://brest.fr/gerer-mon-quotidien/logement/etre-proprietaire-ou-le-devenir"
_DOCS = "https://brest.fr/sites/default/files/medias/brestfr/documents/gerer_mon_quotidien/logement/"
_AVAP = _DOCS + "acheter_construire_r%C3%A9onver/R%C3%A8glement%20de%20l%27AVAP.pdf"
_ITE = _DOCS + "ITE-Une%20belle%20fa%C3%A7ade.pdf"
_PLU = "https://brest.fr/plu"
_PLU_DOCS = "https://brest.fr/sites/default/files/medias/brestfr/documents/brest_ville_et_metropole/plu/plu_2026-09/"
_REG = _PLU_DOCS + "242900314_reglement_20260928.pdf"
_ACTES = _PLU_DOCS + "242900314_procedure_20260928.pdf"
_DEM = "https://brest.fr/gerer-mon-quotidien/logement/faire-mes-demarches-durbanisme-permis-de-construire-damenager"
_CARTE = "https://bmo.maps.arcgis.com/apps/webappviewer/index.html?id=f2b4cd50894140b2b519ad149ab996f2"
_VOIRIE = "https://brest.fr/gerer-mon-quotidien/demarches/demander-une-permission-de-voirie"
_VOIRIE_F = ("https://brest.fr/sites/default/files/medias/brestfr/documents/gerer_mon_quotidien/demarches/espace_public/"
             "Formulaire%202026%20de%20demande%20de%20permission%20de%20voirie.pdf")
_MF = "https://donneespubliques.meteofrance.fr/FichesClim/FICHECLIM_29075001.pdf"
_DICRIM = "https://www.georisques.gouv.fr/DICRIM/29019"
_RADON = "https://georisques.gouv.fr/api/v1/radon?code_insee=29019"
_CATNAT = "https://georisques.gouv.fr/api/v1/gaspar/catnat?code_insee=29019&page_size=100"
_TIN = "https://tinergie.fr/renovation-energetique/aides-financieres-renovation/"
_TIN_ACC = "https://tinergie.fr/renovation-energetique/les-dispositifs-publics-locaux-daccompagnement/"
_ECFR = "https://lannuaire.service-public.gouv.fr/bretagne/finistere/0ffe00fd-e5f5-465b-bb44-5da691ece82c"

CITY = dict(
    slug="brest", name="Brest", cp="29200", insee="29019",
    lat=48.3908, lon=-4.4856, dept="Finistère", depcode="29", region="Bretagne",
    wiki="https://fr.wikipedia.org/wiki/Brest", wikidata="Q12193",
    verified="2026-11-21",
    tldr="À Brest, l’AVAP du centre-ville et de Recouvrance fixe les couleurs, les menuiseries et l’isolation immeuble par immeuble, "
         "et la métropole aide les voisins qui colorent leur rue ensemble",
    hook="Ville reconstruite, couleurs et isolation encadrées par l’AVAP.",
    title="Devis travaux à Brest : toiture, façade, fenêtres, isolation",
    desc="Travaux à Brest : AVAP du centre-ville et de Recouvrance, rafales de l’Atlantique, radon, aides Tinergie et Colorez votre rue. "
         "Un seul artisan vient chiffrer.",
    figures_intro="Ce qui compte avant de lancer des travaux face à la rade.",
    figures=[("74,4 <small>%</small>", "des logements sont des appartements", S("Insee, 2023", _INSEE)),
             ("39,7 <small>%</small>", "des résidences principales datent de 1946 à 1970", S("Insee, 2023", _INSEE)),
             ("8,8 <small>%</small>", "des résidences principales datent d’avant 1946", S("Insee, 2023", _INSEE)),
             ("83,4 <small>jours</small>", "de rafales d’au moins 58 km/h par an", S("Météo-France, normales 1991-2020", _MF))],
    answer=("À Brest, 39,7 % des résidences principales datent de 1946 à 1970, et 74,4 % des logements sont des appartements. Dans le centre-ville et "
            "à Recouvrance, l’AVAP approuvée en 2019 fixe couleurs, menuiseries et isolation par l’extérieur selon le type d’immeuble. Partout, un "
            "ravalement qui change l’aspect de la façade demande une déclaration préalable."),
    facts=[("AVAP", "L’aire de mise en valeur de l’architecture et du patrimoine, qui vaut site patrimonial remarquable, a été approuvée par le Conseil "
                    "de la métropole le 28 juin 2019. Elle couvre le centre-ville et Recouvrance, avec des règles selon que la construction est "
                    "remarquable, d’intérêt architectural ou non repérée (" + L("règlement de l’AVAP", _AVAP) + ")."),
           ("Urbanisme", "Le PLU facteur 4 de Brest métropole, commun aux 8 communes, a été approuvé le 20 janvier 2014. Sa mise à jour n° 23 date "
                         "du 28 septembre 2026 (" + L("Brest métropole", _PLU) + ", " + L("actes du PLU", _ACTES) + ")."),
           ("Monuments historiques", "Château, Bâtiment aux Lions, villa Mathon, hôpital Morvan, église Saint-Louis et gare ont leurs abords inclus "
                                     "dans l’AVAP. Aux abords, l’architecte des Bâtiments de France donne son avis, le dossier compte un exemplaire "
                                     "de plus et l’instruction dure un mois de plus (" + L("Ville de Brest", _DEM) + ")."),
           ("Ravalement", "Tout ravalement, sauf à l’identique, demande une déclaration préalable. Des opérations de coloration sont en cours en haut "
                          "de la rue Jean-Jaurès, place de la Recouvrance et à Kérinou, avec Soliha : 02 98 44 85 76 (" + L("Brest métropole", _PROPRIO) + ")."),
           ("Vent et pluie", "À Brest-Guipavas, 1 229,8 mm de pluie et 159,5 jours avec au moins 1 mm par an. Les rafales atteignent 58 km/h ou plus "
                             "83,4 jours par an, et le record culmine à 43,2 m/s le 2 novembre 2023 (" + L("Météo-France", _MF) + ", normales 1991-2020)."),
           ("Radon et littoral", "Brest est classée en catégorie 3 pour le radon, la plus élevée des trois. Le DICRIM cite aussi la submersion marine et les "
                                 "cavités souterraines, comme les abris et les tunnels (" + L("DICRIM, 2024", _DICRIM) + ", " + L("Géorisques", _RADON) + ").")],
    trades_intro="Immeubles de la Reconstruction en béton enduit, maisons de l’entre-deux-guerres, granite et kersantite : à Brest, les règles suivent "
                 "le type d’immeuble, surtout dans l’AVAP.",
    trades={
        "toiture": ["Dans l’AVAP, une couverture se refait à l’identique. Le zinc reste en plaques de zinc à faible pente. L’ardoise se refait en "
                    "ardoise naturelle, avec un faîtage en faîteaux de terre cuite posés au mortier de chaux. Un toit de 5 % de pente ou moins se traite "
                    "comme une façade, et les châssis de toit sont encastrés sans saillie (" + L("règlement de l’AVAP", _AVAP) + ").",
                    "À Brest-Guipavas, les rafales d’au moins 100 km/h soufflent 1,9 jour par an en moyenne, surtout d’octobre à mars, et la "
                    "tempête d’octobre 1987 a été reconnue catastrophe naturelle (" + L("Météo-France", _MF) + ", " + L("Géorisques", _CATNAT)
                    + "). Faites vérifier crochets d’ardoise, relevés de zinc et solins avant l’hiver."],
        "facade": ["Pour un immeuble de la Reconstruction, l’AVAP prévoit un ragréage des parements abîmés, avec passivation des aciers du béton armé, "
                   "puis une peinture minérale de couleur claire. Dans la ville reconstruite, les grandes surfaces restent claires selon le nuancier "
                   "de la Reconstruction. Granite et kersantite se restaurent à l’identique, sans enduit ni peinture (" + L("règlement de l’AVAP", _AVAP) + ").",
                   "Plusieurs propriétaires d’une même rue veulent des couleurs vives ? Brest métropole offre une coloriste conseil et des subventions "
                   "de 100 € à 1 500 €. Dans les secteurs en renouvellement urbain, comme Recouvrance ou le haut de Jaurès, l’aide à la "
                   "requalification des façades peut atteindre 25 % des travaux (" + L("Brest métropole", _PROPRIO) + ")."],
        "fenetres": ["Dans l’AVAP, les fenêtres se remplacent à l’identique, en général à la française, en respectant la partition des vitrages. Sur un "
                     "immeuble remarquable, le matériau d’origine est obligatoire. Sur un immeuble d’intérêt architectural, l’aluminium laqué ou le "
                     "PVC sont admis s’ils gardent les mêmes profils. Les petits bois sont extérieurs au vitrage et les doubles fenêtres extérieures "
                     "sont interdites (" + L("règlement de l’AVAP", _AVAP) + ").",
                     "Les volets persiennés en plastique sont interdits dans l’AVAP. Un volet roulant n’est accepté que si son coffre reste invisible "
                     "de l’extérieur (" + L("règlement de l’AVAP", _AVAP) + "). Partout, la Ville publie une notice pour la déclaration préalable "
                     "de changement de menuiseries (" + L("Ville de Brest", _DEM) + ")."],
        "charpente": ["Dans l’AVAP, les lucarnes existantes sont conservées et restaurées, sauf si elles ont été ajoutées plus tard sans respecter "
                      "le type de l’immeuble. Les souches de cheminée se refont selon leur technique d’origine, maçonnerie enduite ou granite, sans bardage "
                      "(" + L("règlement de l’AVAP", _AVAP) + ").",
                      "Isoler par l’extérieur la toiture d’une construction remarquable reste possible : le profil du toit est conservé et les rives "
                      "ne prennent aucune surépaisseur (" + L("règlement de l’AVAP", _AVAP) + "). En zone UC du PLU, une surélévation doit suivre la ligne des toitures voisines ("
                      + L("règlement du PLU", _REG) + ")."],
        "isolation": ["Dans l’AVAP, l’isolation par l’extérieur est interdite sur les façades des constructions remarquables et sur celles d’avant 1948 "
                      "d’intérêt architectural, sauf pignons et façades sur cœur d’îlot. Elle est permise sur la Reconstruction non revêtue de pierre, "
                      "avec une finition enduite et sans bardage plastique (" + L("règlement de l’AVAP", _AVAP) + "). Le PLU admet 20 cm "
                      "de débord au plus, y compris sur le domaine public si l’emprise publique garde 3,50 mètres de large (" + L("règlement du PLU", _REG) + ").",
                      "En catégorie 3 pour le radon, le DICRIM conseille d’étanchéifier l’interface entre sol et bâtiment, de traiter le soubassement "
                      "et d’améliorer la ventilation (" + L("DICRIM, 2024", _DICRIM) + "). Prévoyez-la avec l’isolation : la subvention Tinergie, "
                      "jusqu’à 9 000 €, ajoute des bonus pour l’étanchéité à l’air et l’isolation biosourcée (" + L("Tinergie", _TIN) + ")."]},
    steps_intro="Dans l’ordre, du centre reconstruit aux quartiers.",
    steps=[("Repérez les règles de votre parcelle", "L’outil cartographique de la Ville montre l’AVAP et les abords des monuments ("
                                                   + L("carte", _CARTE) + "). La note de renseignements d’urbanisme se demande en ligne."),
           ("Préparez le dossier avec les notices", "La Ville publie une notice par type de travaux : ravalement, menuiseries, isolation par "
                                                    "l’extérieur, panneaux solaires (" + L("Ville de Brest", _DEM) + ")."),
           ("Déposez la déclaration préalable", "En ligne sur le guichet unique, ou au Conseil architectural et urbain, 24 rue Coat-ar-Guéven. "
                                                "02 98 33 50 50, accueil du lundi au vendredi de 9 h à 12 h 30 (" + L("Ville de Brest", _DEM) + ")."),
           ("Faites autoriser l’échafaudage", "Permission de voirie au moins 10 jours ouvrés avant. Moins de deux mois sans gêne pour la circulation : "
                                              "service du domaine communal, 27 avenue Georges-Clemenceau. Tarif 2026 : 3,00 € par mètre linéaire et "
                                              "par niveau, chaque mois (" + L("Ville de Brest", _VOIRIE) + ", " + L("formulaire 2026", _VOIRIE_F) + ")."),
           ("Appelez Tinergie avant de signer", "Le conseil est gratuit, et les aides se montent avant le devis.")],
    aides_intro="À Brest, le conseil Tinergie est gratuit et se demande avant de signer le devis.",
    aides=[("Tinergie, Espace Conseil France Rénov’", "Le service public de la rénovation du Pays de Brest, porté par Brest métropole : conseil gratuit "
                                                    "et neutre. 3 rue Keravel, 29200 Brest, accueil sur rendez-vous. 02 98 33 20 09, du lundi au "
                                                    "vendredi de 9 h à 17 h 30 (" + L("annuaire Service-Public", _ECFR) + ", " + L("Tinergie", _TIN) + ")."),
           ("Subvention Tinergie", "Pour la rénovation énergétique d’une maison, en complément de MaPrimeRénov’ : jusqu’à 9 000 € selon la "
                                   "performance du projet, avec des bonus. Les copropriétés ont une subvention propre, sous critères ("
                                   + L("Tinergie", _TIN) + ")."),
           ("Accompagnement gratuit des ménages modestes", "Pour un projet aidé par l’Anah, Brest métropole finance l’accompagnement par Ener’gence, "
                                                           "un accompagnement qui peut dépasser 2 000 € TTC. 02 98 33 20 09 (" + L("Tinergie", _TIN_ACC) + ")."),
           ("Colorez votre rue", "Une coloriste conseil et des subventions de 100 € à 1 500 € pour des voisins qui colorent ensemble leurs façades. "
                                 "Dans les secteurs en renouvellement urbain, l’aide à la requalification des façades va jusqu’à 25 % des travaux. Conseil architectural et urbain : 02 98 33 50 50 ("
                                 + L("Brest métropole", _PROPRIO) + ")."),
           NATIONAL],
    faq=[("Faut-il une autorisation pour ravaler sa façade à Brest ?",
          "Oui, une déclaration préalable, sauf pour un ravalement à l’identique. Dans l’AVAP, les immeubles de la Reconstruction gardent des teintes "
          "claires sur les grandes surfaces. Aux abords d’un monument historique, l’architecte des Bâtiments de France donne son avis."),
         ("Peut-on poser des fenêtres en PVC à Brest ?",
          "Hors AVAP, oui, avec une déclaration préalable si l’aspect change. Dans l’AVAP, le matériau d’origine est obligatoire sur un immeuble "
          "remarquable. Sur un immeuble d’intérêt architectural, le PVC est admis s’il garde les profils d’origine."),
         ("Peut-on isoler par l’extérieur un immeuble de la Reconstruction ?",
          "Oui, s’il n’est pas revêtu de pierre : l’AVAP demande une finition enduite, le débord de toit restitué et aucun bardage plastique. Sur "
          "les constructions remarquables et celles d’avant 1948 d’intérêt architectural, elle est interdite en façade."),
         ("Brest est-elle concernée par le radon ?",
          "Oui, la commune est en catégorie 3, la plus exposée. Pendant une rénovation, traitez le soubassement, l’étanchéité entre sol et bâtiment "
          "et la ventilation."),
         ("Comment faire autoriser un échafaudage à Brest ?",
          "Demandez une permission de voirie au moins 10 jours ouvrés avant, au service du domaine communal pour un chantier de moins de deux mois "
          "sans gêne pour la circulation. La redevance se paie chaque mois, au mètre linéaire et par niveau."),
         ("Quelles aides pour rénover son logement à Brest ?",
          "La subvention Tinergie, jusqu’à 9 000 €, l’accompagnement gratuit des ménages modestes, l’aide Colorez votre rue, de 100 € à 1 500 €, et "
          "les aides nationales. Conseil gratuit chez Tinergie : 02 98 33 20 09.")],
)

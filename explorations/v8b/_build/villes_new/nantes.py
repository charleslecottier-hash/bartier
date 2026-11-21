from villes_data import L, S, SP, NATIONAL  # liens dans le texte, sources discrètes, Service-Public, aides nationales

# Sources consultées le 21/11/2026.
_INSEE = "https://www.insee.fr/fr/statistiques/2011101?geo=COM-44109"
_PSMV_PAGE = "https://metropole.nantes.fr/mes-services-mon-quotidien/le-plan-de-sauvegarde-et-de-mise-en-valeur-le-psmv"
_PSMV = ("https://metropole.nantes.fr/static/psmv/2-_Pi%C3%A8ces_r%C3%A9glementaires_%C3%A9crites_et_graphiques_du_PSMV/"
         "2-5_R%C3%A8glement/2-5_PSMV_REGLEMENT.pdf")
_POP = "https://pop.culture.gouv.fr/notice/merimee/SPR5200009"
_PLUM = "https://metropole.nantes.fr/mes-services-mon-quotidien/le-plan-local-d-urbanisme-metropolitain-le-plum"
_DP = "https://metropole.nantes.fr/mes-services-mon-quotidien/permis-de-construire-et-declaration-prealable-de-travaux"
_RESTAURER = "https://metropole.nantes.fr/mes-services-mon-quotidien/entretenir-et-restaurer-votre-immeuble"
_RAV = SP + "F640"
_MF = "https://donneespubliques.meteofrance.fr/FichesClim/FICHECLIM_44020001.pdf"
_PPRI = "https://www.georisques.gouv.fr/donnee-risques/PPR/Fiche-ppr/pprn/44DDTM20080006"
_CATNAT = "https://georisques.gouv.fr/api/v1/gaspar/catnat?code_insee=44109&page_size=100"
_SISMI = "https://georisques.gouv.fr/api/v1/zonage_sismique?code_insee=44109"
_MPR_MAISON = "https://metropole.nantes.fr/mes-services-mon-quotidien/renovation-energetique-de-ma-maison-avec-mon-projet-renov-maison"
_MPR_COPRO = "https://metropole.nantes.fr/mes-services-mon-quotidien/renovation-energetique-de-ma-copropriete-ou-de-mon-logement"
_MDH = "https://metropole.nantes.fr/mes-services-mon-quotidien/se-renseigner-a-la-maison-de-l-habitant-pour-toutes-vos-questions-logement"
_ECHAF = ("https://metropole.nantes.fr/mes-services-mon-quotidien/"
          "demander-une-autorisation-pour-installer-une-benne-a-gravats-un-echafaudage-ou-une-cabane-de-chantier")
_CARTE = "https://experience.arcgis.com/experience/72b2cee5ff2d48c8b98d919222f6f690"
_UDAP = ("https://www.culture.gouv.fr/regions/drac-pays-de-la-loire/la-direction-regionale-des-affaires-culturelles-drac-des-pays-de-la-loire/"
         "pole-patrimoines-architecture-et-espaces-proteges-drac-pays-de-la-loire/"
         "udap-unites-departementales-de-l-architecture-et-du-patrimoine-des-pays-de-la-loire/udap-de-loire-atlantique")

CITY = dict(
    slug="nantes", name="Nantes", cp="44000", insee="44109",
    lat=47.2172, lon=-1.5539, dept="Loire-Atlantique", depcode="44", region="Pays de la Loire",
    wiki="https://fr.wikipedia.org/wiki/Nantes", wikidata="Q12191",
    verified="2026-11-21",
    tldr=("À Nantes, le maire peut imposer le ravalement tous les dix ans, et changer une seule fenêtre demande déjà "
          "une déclaration préalable"),
    hook="Ravalement tous les dix ans, et une déclaration même pour une fenêtre.",
    title="Devis travaux à Nantes : toiture, façade, fenêtres, isolation",
    desc=("Travaux à Nantes : ravalement tous les 10 ans, déclaration même pour une fenêtre, secteur sauvegardé, aide jusqu’à "
          "20 000 €. Un seul artisan vient chiffrer."),
    figures_intro="Le parc, le centre protégé et l’aide de la Métropole en quatre chiffres.",
    figures=[("80,6 <small>%</small>", "des logements sont des appartements", S("Insee, 2023", _INSEE)),
             ("21,7 <small>%</small>", "des résidences principales datent de 1946 à 1970", S("Insee, 2023", _INSEE)),
             ("126 <small>ha</small>", "de secteur sauvegardé dans le centre historique", S("Nantes Métropole", _PSMV_PAGE)),
             ("20 000 <small>€</small>", "d’aide au plus de la Métropole pour rénover une maison au niveau BBC", S("Nantes Métropole, 2026", _MPR_MAISON))],
    answer=("Huit logements sur dix sont des appartements (80,6 %), et 21,7 % des résidences principales datent de 1946 à 1970. "
            "Le maire peut imposer le ravalement au moins tous les dix ans, et tout changement d’aspect, même le remplacement d’une "
            "fenêtre, demande une déclaration préalable. Dans le secteur sauvegardé de 126 hectares, le PVC est interdit pour les fenêtres."),
    facts=[("Ravalement", "Nantes fait partie des communes où un arrêté préfectoral permet au maire d’imposer le ravalement au moins une "
                          "fois tous les 10 ans (" + L("Service-Public", _RAV) + ", 2026). La Ville rappelle cette obligation d’entretien "
                          "des façades aux propriétaires (" + L("Ville de Nantes", _RESTAURER) + ")."),
           ("Centre historique", "Secteur sauvegardé depuis le 22 mars 1972 (" + L("ministère de la Culture", _POP) + "), devenu site "
                                 "patrimonial remarquable : 126 hectares et un peu plus de 10 000 logements, sous un plan de sauvegarde "
                                 "révisé en 2017 et modifié le 6 décembre 2023. Il protège aussi l’intérieur des immeubles ("
                                 + L("Nantes Métropole", _PSMV_PAGE) + ")."),
           ("Déclaration préalable", "Obligatoire pour tous travaux qui changent l’aspect d’un bâtiment, y compris le remplacement d’une "
                                     "menuiserie (" + L("Ville de Nantes", _RESTAURER) + "). Le permis de démolir est exigé sur toute la "
                                     "commune depuis la délibération du 5 octobre 2007 (" + L("démarches", _DP) + ")."),
           ("Urbanisme", "Hors centre historique, le PLU métropolitain s’applique aux 24 communes depuis son approbation du 5 avril 2019. "
                         "Sa modification n° 2 a été approuvée le 7 février 2025 (" + L("Nantes Métropole", _PLUM) + ")."),
           ("Inondation et séisme", "Le plan de prévention du risque inondation de la Loire aval s’applique depuis le 31 mars 2014 ("
                                    + L("Géorisques", _PPRI) + "). La commune compte 14 arrêtés de catastrophe naturelle pour "
                                    "inondation, le dernier pour les inondations du 8 au 23 février 2026 (" + L("Géorisques", _CATNAT)
                                    + "). Zone de sismicité 3, modérée (" + L("Géorisques", _SISMI) + ")."),
           ("Climat", "À Nantes-Bouguenais, 819,5 mm de pluie sur 119,7 jours, 42,8 jours de rafales d’au moins 58 km/h et 29,1 jours "
                      "à 0 °C ou moins par an (" + L("Météo-France", _MF) + ", normales 1991-2020).")],
    trades_intro="Ardoise, tuffeau et granit nantais dans le centre historique ; ailleurs, le PLU métropolitain et une déclaration pour tout changement d’aspect.",
    trades={
        "toiture": ["Dans le secteur sauvegardé, l’ardoise est naturelle, posée au clou ou au crochet teinté, avec des faîteaux nantais "
                    "en terre cuite. Ardoises d’imitation et descentes en PVC y sont interdites, comme les couvertures en fibrociment ou "
                    "métalliques qui n’étaient pas d’origine (" + L("PSMV", _PSMV) + ").",
                    "Un châssis de toit y mesure au plus 0,80 m de large sur 1 m de haut, axé sur les fenêtres du dessous, et il est "
                    "interdit sur les toits qui donnent sur les anciens bras de la Loire, les cours et les places ordonnancés. "
                    "Avec 42,8 jours de rafales d’au moins 58 km/h par an, surtout en décembre et janvier, faites contrôler ardoises et crochets avant l’hiver ("
                    + L("Météo-France", _MF) + ")."],
        "facade": ["Le maire peut imposer le ravalement au moins tous les dix ans. Pour un bâtiment protégé ou d’intérêt patrimonial, "
                   "la Ville finance 80 % du diagnostic patrimonial réalisé par un architecte, plafonné à 2 000 € ou 5 000 € selon le "
                   "nombre de façades (" + L("Ville de Nantes", _RESTAURER) + ").",
                   "Dans le secteur sauvegardé, les façades mêlent tuffeau et autres calcaires, sur des seuils et soubassements en granit "
                   "nantais, le plus souvent beige rosé. Sablage, disque et acide y sont proscrits : on nettoie par brossage, "
                   "lavage à faible pression ou nébulisation, et la peinture des enduits traditionnels est interdite (" + L("PSMV", _PSMV) + ")."],
        "fenetres": ["Remplacer une fenêtre demande une déclaration préalable à Nantes, même hors secteur protégé, dès que l’aspect du "
                     "bâtiment change (" + L("Ville de Nantes", _RESTAURER) + "). Une aide de la Ville prend en charge 80 % du diagnostic "
                     "d’une menuiserie ancienne remarquable, sans plafond.",
                     "Dans le secteur sauvegardé, les fenêtres sont en bois peint et le PVC est interdit. La fenêtre neuve se pose dans la "
                     "feuillure d’origine, sans recul pour loger un isolant, et une double fenêtre intérieure est admise si elle "
                     "ne touche pas un décor. Les volets roulants sont interdits sur les immeubles protégés (" + L("PSMV", _PSMV) + ")."],
        "charpente": ["Dans le secteur sauvegardé, le volume du toit d’un immeuble protégé se garde sans surélévation, sauf cas "
                      "exceptionnels. Une charpente d’intérêt se restaure avec soin, l’isolant ne doit pas menacer sa pérennité, et une "
                      "charpente exceptionnelle peut devoir rester apparente (" + L("PSMV", _PSMV) + ").",
                      "Nantes est en zone de sismicité 3, modérée (" + L("Géorisques", _SISMI) + "). Si vos travaux relèvent d’une "
                      "déclaration préalable, toute démolition, même partielle, demande en parallèle un permis de démolir, "
                      "exigé sur toute la commune ("
                      + L("Ville de Nantes", _DP) + ")."],
        "isolation": ["Mon Projet Rénov Maison aide les propriétaires sans condition de ressources : 250 € pour l’audit, obligatoire, "
                      "puis 7 000 € ou 14 000 € pour une rénovation BBC selon la performance atteinte, et 6 000 € de plus avec "
                      "des isolants biosourcés ("
                      + L("Nantes Métropole", _MPR_MAISON) + ", 2026).",
                      "Dans le secteur sauvegardé, l’isolation par l’extérieur est interdite sur les immeubles protégés, hors rares façades "
                      "secondaires, et les panneaux solaires aussi. Un immeuble non protégé peut être isolé par l’extérieur si le "
                      "projet améliore l’architecture sans rompre l’alignement de la rue (" + L("PSMV", _PSMV) + ")."]},
    steps_intro="Dans l’ordre, de la règle de votre parcelle à l’échafaudage.",
    steps=[("Lisez la règle de votre parcelle", "La " + L("carte interactive du PLUm", _CARTE) + " donne les prescriptions de chaque "
                                                "parcelle, hors secteur sauvegardé. En secteur protégé, l’architecte des Bâtiments de France "
                                                "donne son avis : UDAP de Loire-Atlantique, 02 40 14 28 19, le lundi, le mardi et le jeudi "
                                                "de 9 h à 12 h (" + L("ministère de la Culture", _UDAP) + ")."),
           ("Prenez conseil pour un immeuble ancien", "L’architecte conseil de la direction du patrimoine de la Ville reçoit sur "
                                                      "rendez-vous, 13 rue de Briord, en lien avec l’architecte des Bâtiments de France. "
                                                      "02 40 41 56 80."),
           ("Demandez l’aide avant les travaux", "Rendez-vous France Rénov’ obligatoire, puis demande Mon Projet Rénov en ligne. Des "
                                                 "travaux commencés avant le dépôt de la demande ne sont pas aidés."),
           ("Déposez la déclaration préalable", "En ligne sur les e-services de Nantes Métropole, ou à la direction de l’urbanisme "
                                                "réglementaire, 5 rue Vasco-de-Gama, du lundi au vendredi de 8 h 30 (9 h le mercredi) à "
                                                "12 h et de 14 h à 17 h. 02 40 41 59 55 (" + L("Ville de Nantes", _DP) + ")."),
           ("Faites autoriser l’échafaudage", "Au moins 14 jours avant le chantier, avec un plan, au service Réglementation des usages "
                                              "de l’espace public. S’il prend des places de stationnement, posez les panneaux 48 heures "
                                              "avant (" + L("démarche", _ECHAF) + ").")],
    aides_intro="À Nantes, chaque aide se demande avant de commencer, après un rendez-vous de conseil gratuit.",
    aides=[("La Maison de l’Habitant", "L’Espace Conseil France Rénov’ de Nantes Métropole, avec l’ADIL : 12 rue du Président-Herriot, "
                                      "44000 Nantes. 02 40 89 30 15, puis touche 1. Du lundi au jeudi de 9 h à 12 h 30 et de 13 h 30 à 17 h, "
                                      "fermé le mardi matin. " + L("metropole.nantes.fr", _MDH) + "."),
           ("Mon Projet Rénov Maison", "Sans condition de ressources : 250 € pour l’audit, jusqu’à 20 000 € pour une rénovation BBC, dont "
                                       "6 000 € avec des isolants biosourcés. La demande se dépose avant de commencer ("
                                       + L("Nantes Métropole", _MPR_MAISON) + ", 2026)."),
           ("Mon Projet Rénov Copropriété", "Jusqu’à 5 000 € par bâtiment pour l’audit global et 20 000 € pour la maîtrise d’œuvre. Pour "
                                            "les travaux BBC, un tiers du coût hors taxes, dans la limite de 40 000 € HT de travaux par lot "
                                            "principal (" + L("Nantes Métropole", _MPR_COPRO) + ")."),
           ("Aides patrimoine de la Ville", "Pour un immeuble protégé : 20 % des travaux en secteur prioritaire, jusqu’à 150 000 €, ou 10 % "
                                            "ailleurs, jusqu’à 75 000 €. Un propriétaire occupant d’un seul logement peut recevoir en plus "
                                            "jusqu’à 20 000 €, selon ses revenus (" + L("Ville de Nantes", _RESTAURER) + ", 2025)."),
           NATIONAL],
    faq=[("Le ravalement est-il obligatoire à Nantes ?",
          "Oui. Nantes fait partie des communes où un arrêté préfectoral permet au maire d’imposer le ravalement au moins une fois tous "
          "les 10 ans. Pour un immeuble protégé, la Ville aide le diagnostic patrimonial à 80 % et les travaux à 10 % ou 20 %."),
         ("Faut-il une autorisation pour changer ses fenêtres à Nantes ?",
          "Oui, une déclaration préalable, même pour remplacer une menuiserie, rappelle la Ville. Dans le secteur sauvegardé, les "
          "fenêtres sont en bois peint et le PVC est interdit."),
         ("Peut-on poser des volets roulants dans le centre historique de Nantes ?",
          "Pas sur un immeuble protégé du secteur sauvegardé, sauf dispositif d’origine. Sur un immeuble non protégé, seulement sur une "
          "façade invisible de l’espace public et sans coffre apparent."),
         ("Peut-on isoler par l’extérieur à Nantes ?",
          "Dans le secteur sauvegardé, c’est interdit sur les immeubles protégés ; sur les autres, le projet doit améliorer l’architecture "
          "et respecter l’alignement de la rue. Ailleurs, le PLU métropolitain s’applique, avec une déclaration préalable."),
         ("Quelles aides pour rénover sa maison à Nantes ?",
          "Mon Projet Rénov Maison de Nantes Métropole, sans condition de ressources : 250 € pour l’audit et jusqu’à 20 000 € pour une "
          "rénovation BBC, en plus des aides nationales. Rendez-vous obligatoire avant : Maison de l’Habitant, 02 40 89 30 15."),
         ("Comment faire autoriser un échafaudage à Nantes ?",
          "Demandez une autorisation d’occupation de l’espace public au moins deux semaines avant, avec un plan. Elle est payante, selon la "
          "rue, la durée et la surface occupée.")],
)

# Données locales des pages ville. Chaque fait vient d'une source consultée le 20/11/2026 (lien dans le texte).
# Règles : rien d'inventé ; chiffres repris tels quels de la source ; pas de promesse de présence locale.


def L(label, url):
    return f'<a class="link" href="{url}" target="_blank" rel="noopener">{label}</a>'


def S(label, url):  # source discrète, sous un chiffre
    return f'<a href="{url}" target="_blank" rel="noopener">{label}</a>'


SP = "https://www.service-public.gouv.fr/particuliers/vosdroits/"
NATIONAL = ("Aides nationales",
            "MaPrimeRénov’, primes CEE et éco-prêt à taux zéro, avec une entreprise certifiée RGE. La TVA est de 5,5 % pour les travaux "
            "d’amélioration énergétique et de 10 % pour l’entretien d’un logement de plus de deux ans. Votre cas : "
            + L("france-renov.gouv.fr", "https://france-renov.gouv.fr/") + ".")

# ——— Paris ———
_INSEE_75 = "https://www.insee.fr/fr/statistiques/8581193?geo=COM-75056"
_SDES = "https://www.statistiques.developpement-durable.gouv.fr/media/7205/download?inline"
PARIS = dict(
    tldr="À Paris, presque tout se vote en copropriété, et même des fenêtres remplacées à l’identique demandent une autorisation",
    hook="Une autorisation même pour des fenêtres à l’identique.",
    slug="paris", name="Paris", cp="75011", wiki="https://fr.wikipedia.org/wiki/Paris", wikidata="Q90",
    title="Devis travaux à Paris : toiture, façade, fenêtres, isolation",
    desc="Travaux à Paris : ravalement tous les 10 ans, déclaration préalable, architecte des Bâtiments de France, aides. Un seul artisan vient chiffrer, gratuitement.",
    figures_intro="Ce qui compte avant de lancer des travaux dans la capitale.",
    figures=[("97 <small>%</small>", "des logements sont des appartements", S("Insee, 2022", _INSEE_75)),
             ("48,7 <small>%</small>", "des résidences principales datent d’avant 1946", S("Insee, 2022", _INSEE_75)),
             ("94 <small>%</small>", "des logements sont dans un périmètre de protection du patrimoine", S("SDES, 2024", _SDES)),
             ("10 <small>ans</small>", "au plus entre deux ravalements, sur injonction du maire", S("Service-Public", SP + "F640"))],
    answer=("Sur 100 logements, 97 sont des appartements. Le ravalement est obligatoire au moins tous les dix ans, et 94 % des logements sont "
            "dans un périmètre où l’architecte des Bâtiments de France donne son avis."),
    facts=[("Ravalement", "Obligatoire au moins tous les 10 ans. La Ville écrit, contrôle un an plus tard, puis peut prendre un arrêté d’injonction : "
                          "les travaux doivent alors commencer dans les 6 mois. Amende possible : 3 750 € ("
                          + L("Service-Public", SP + "F640") + ", " + L("Ville de Paris", "https://www.paris.fr/pages/renover-son-logement-ou-son-immeuble-121") + ")."),
           ("Autorisation", "Une déclaration préalable pour tout changement d’aspect extérieur : façade, toiture, fenêtres, même remplacées à l’identique ("
                            + L("Ville de Paris", "https://www.paris.fr/pages/faq-urbanisme-4410") + ")."),
           ("Secteurs protégés", "Le Marais (3e et 4e) et le 7e ont un plan de sauvegarde : l’accord de l’architecte des Bâtiments de France y est obligatoire ("
                                 + L("Ville de Paris", "https://www.paris.fr/pages/secteurs-sauvegardes-psmv-2351") + ")."),
           ("PLU bioclimatique", "Approuvé le 20 novembre 2024. Pour un ravalement important, la Ville demande comment la performance énergétique sera améliorée ("
                                 + L("fiche ravalement", "https://cdn.paris.fr/paris/2026/03/19/fiche-travaux-de-ravalement-NKgK.pdf") + ")."),
           ("Termites", "Tout Paris est en zone de surveillance et de lutte contre les termites ("
                        + L("Ville de Paris", "https://www.paris.fr/pages/lutte-contre-les-termites-8103") + ")."),
           ("Copropriété", "Depuis 2025, toute copropriété de plus de 15 ans doit avoir un projet de plan pluriannuel de travaux ("
                           + L("Service-Public", SP + "F36760") + ").")],
    trades_intro="Toiture et façade sont des parties communes : les travaux se votent en assemblée générale. Le statut des fenêtres dépend du règlement de copropriété.",
    trades={
        "toiture": ["Les toits parisiens sont surtout métalliques : 78 % sont à dominante zinc ou autre matériau, 7 % seulement en tuile ("
                    + L("Apur", "https://www.apur.org/en/climate-environment/material/predominant-roofing-material-paris") + "). Le savoir-faire des "
                    "couvreurs-zingueurs parisiens est inscrit au patrimoine culturel immatériel de l’Unesco depuis 2024 ("
                    + L("Unesco", "https://ich.unesco.org/fr/decisions/19.COM/7.B.37") + ").",
                    "Changer de matériau ou créer une fenêtre de toit demande une déclaration préalable, et l’avis de l’architecte des Bâtiments de France en secteur protégé."],
        "facade": ["Pierre de taille, plâtre sur pans de bois, moellons ou brique : chaque façade a sa technique ("
                   + L("Ville de Paris", "https://cdn.paris.fr/paris/2019/07/24/464dd1e077cc817a02f9293fd72fa3e7.pdf") + "). "
                   "Le ravalement passe par une déclaration préalable, avec la fiche ravalement de la Ville.",
                   "Pour un ravalement important, le PLU bioclimatique demande d’expliquer le gain énergétique : c’est le moment d’étudier l’isolation "
                   "par l’extérieur, quand la façade s’y prête."],
        "fenetres": ["Remplacer une fenêtre demande une autorisation d’urbanisme, même à l’identique. En copropriété, le règlement peut imposer "
                     "le modèle, le matériau et la couleur : vérifiez-le avant de demander un devis.",
                     "Dans le Marais et le 7e, l’architecte des Bâtiments de France doit donner son accord."],
        "charpente": ["Tout Paris est en zone de surveillance et de lutte contre les termites, par arrêté préfectoral. Des indices dans la charpente "
                      "ou les boiseries se déclarent à la mairie d’arrondissement dans le mois ("
                      + L("Ville de Paris", "https://www.paris.fr/pages/lutte-contre-les-termites-8103") + ").",
                      "À la vente, l’état relatif aux termites doit dater de moins de 6 mois."],
        "isolation": ["Pendant une canicule, l’écart de température atteint 6 °C la nuit entre quartiers ("
                      + L("Ville de Paris", "https://www.paris.fr/pages/canicule-avec-cette-carte-visualisez-les-ecarts-de-temperature-en-un-coup-d-oeil-31838") + "). "
                      "Isoler la toiture limite aussi la surchauffe des derniers étages.",
                      "En copropriété, les travaux d’économie d’énergie se votent à la majorité absolue, article 25 de la loi du 10 juillet 1965 ("
                      + L("ANIL", "https://www.anil.org/votre-besoin/gerer-un-bien/copropriete/travaux-et-majorites/") + ")."]},
    steps_intro="Dans l’ordre, pour une maison comme pour un appartement en copropriété.",
    steps=[("Vérifiez la protection de l’adresse", "Dans le Marais, le 7e ou près d’un monument historique, l’architecte des Bâtiments de France donne son avis. "
                                                    "Son service à Paris : " + L("UDAP de Paris", "https://www.culture.gouv.fr/regions/drac-ile-de-france/missions-et-actions/les-udap-d-ile-de-france/udap-de-paris") + ", 01 56 06 50 00."),
           ("En copropriété, passez par le syndic", "Toiture, façade et isolation des parties communes se votent en assemblée générale. Faites inscrire le devis à l’ordre du jour."),
           ("Déposez la déclaration préalable", "En ligne, sur le " + L("téléservice Démarches d’urbanisme", "https://teleservices.paris.fr/demarchesurbanisme/") + " de la Ville."),
           ("Faites autoriser l’échafaudage", "Un échafaudage sur le trottoir demande une autorisation de voirie et des droits de voirie ("
                                              + L("Ville de Paris", "https://www.paris.fr/pages/effectuer-des-travaux-sur-la-voie-publique-3506") + "). L’entreprise fait la demande en ligne."),
           ("Faites le point sur les aides", "Avant de signer : un rendez-vous gratuit à l’Agence parisienne du climat, l’Espace Conseil France Rénov’ de Paris.")],
    aides_intro="Les aides se demandent avant de signer le devis, et le conseil public est gratuit.",
    aides=[("Agence parisienne du climat", "L’Espace Conseil France Rénov’ de Paris : conseil gratuit et neutre sur les travaux et les aides. Pavillon du Lac, "
                                           "parc de Bercy, 3 rue François-Truffaut, 75012 Paris. 01 58 51 90 20. " + L("apc-paris.com", "https://www.apc-paris.com/contact/") + "."),
           ("Éco-rénovons Paris+", "Pour les copropriétés : 5 000 € pour un audit ou un diagnostic technique global, puis jusqu’à 35 % des travaux hors taxes "
                                   "si le gain énergétique atteint au moins 15 % (" + L("Ville de Paris", "https://www.paris.fr/pages/plan-1000-immeubles-pour-la-renovation-thermique-3136") + ")."),
           ("Métropole Rénov’ Copropriété", "La Métropole du Grand Paris cofinance les études et la maîtrise d’œuvre des copropriétés de 50 logements au plus, "
                                            "construites depuis au moins 15 ans, après un rendez-vous France Rénov’ ("
                                            + L("guide", "https://portail.metropolegrandparis.fr/wp-content/uploads/Guide_Usagers_Metropole_Renov_Copro_2606.pdf") + ")."),
           NATIONAL],
    faq=[("Le ravalement est-il obligatoire à Paris ?",
          "Oui, au moins une fois tous les 10 ans. La Ville envoie d’abord un courrier, contrôle un an plus tard, puis peut prendre un arrêté d’injonction : "
          "les travaux doivent alors commencer dans les 6 mois. Sans travaux, l’amende peut atteindre 3 750 € (Service-Public, fiche F640)."),
         ("Faut-il une autorisation pour changer ses fenêtres à Paris ?",
          "Oui. À Paris, toute modification de l’aspect extérieur demande une autorisation d’urbanisme, même un remplacement à l’identique. "
          "En copropriété, vérifiez aussi le règlement et faites voter l’autorisation en assemblée générale si besoin."),
         ("Mon immeuble est-il en secteur protégé ?",
          "C’est probable : 94 % des logements parisiens sont dans un périmètre de protection du patrimoine (SDES, 2024). Le Marais et le 7e ont un plan "
          "de sauvegarde. Le service de l’architecte des Bâtiments de France de Paris (UDAP, 01 56 06 50 00) vous le confirme."),
         ("Qui décide des travaux de toiture ou de façade dans un immeuble ?",
          "L’assemblée générale des copropriétaires. L’entretien se vote à la majorité simple (article 24 de la loi du 10 juillet 1965), "
          "les travaux d’économie d’énergie à la majorité absolue (article 25), selon l’ANIL."),
         ("Quelles aides pour rénover une copropriété à Paris ?",
          "Éco-rénovons Paris+ finance un audit (5 000 €) puis jusqu’à 35 % des travaux hors taxes avec au moins 15 % de gain énergétique. La Métropole "
          "du Grand Paris cofinance les études des petites copropriétés. Commencez par un rendez-vous gratuit à l’Agence parisienne du climat."),
         ("Que faire si je trouve des termites ?",
          "Tout Paris est en zone de surveillance et de lutte contre les termites : déclarez les indices à la mairie d’arrondissement dans le mois, "
          "puis faites traiter par une entreprise spécialisée.")],
)

# ——— Toulouse ———
_MELODI_31 = "https://api.insee.fr/melodi/data/DS_RP_LOGEMENT_PRINC?GEO=COM-31555"
_PSMV_31 = "https://data.geopf.fr/annexes/gpu/documents/PSMV_31555/741fb112ea7a4538c3a0a48afd454c0c/31555_reglement_20250217.pdf"
_TM_RAV = "https://metropole.toulouse.fr/demarches/demander-laide-au-ravalement-de-facades"
_TM_RENOV = "https://renov.toulouse-metropole.fr/"
_SILENCIO = "https://france3-regions.franceinfo.fr/occitanie/haute-garonne/toulouse/bruit-des-avions-jusqu-a-100-des-couts-rembourses-pour-insonoriser-logements-et-batiments-plus-de-12-000-familles-en-ont-deja-beneficie-3340469.html"
_VENT_31 = "https://www.data.gouv.fr/datasets/vent-et-rafales"
TOULOUSE = dict(
    tldr="À Toulouse, le centre ancien de 256 hectares impose bois peint et tuile canal, et la Ville impose le ravalement par campagnes",
    hook="Centre ancien protégé, aide Silencio près de l’aéroport.",
    slug="toulouse", name="Toulouse", cp="31000", wiki="https://fr.wikipedia.org/wiki/Toulouse", wikidata="Q7880",
    title="Devis travaux à Toulouse : toiture, façade, fenêtres",
    desc="Travaux à Toulouse : centre ancien protégé, campagnes de ravalement, termites, aides de la Métropole. Un seul artisan vient chiffrer, gratuitement.",
    figures_intro="Ce qui compte avant de lancer des travaux dans la ville rose.",
    figures=[("84 <small>%</small>", "des logements sont des appartements", S("Insee, 2023", _MELODI_31)),
             ("34,3 <small>%</small>", "des résidences principales datent d’avant 1971", S("Insee, 2023", _MELODI_31)),
             ("256 <small>ha</small>", "de centre ancien protégé, où l’architecte des Bâtiments de France donne son accord", S("PSMV, 2025", _PSMV_31)),
             ("92 <small>jours</small>", "de rafales d’au moins 57 km/h à Blagnac en 2025 : le vent d’autan", S("Météo-France", _VENT_31))],
    answer=("Sur 100 logements, 84 sont des appartements. Dans le centre ancien, l’architecte des Bâtiments de France donne un avis conforme. "
            "Près de l’aéroport, l’aide Silencio finance au moins 80 % de l’insonorisation des logements situés dans le plan de gêne sonore."),
    facts=[("Ravalement", "Toulouse est depuis 1990 sur la liste préfectorale des communes où le maire peut imposer un ravalement au moins tous les dix ans. "
                          "La 12e campagne obligatoire couvre 2025 à 2029 (" + L("Toulouse Métropole", _TM_RAV) + ")."),
           ("Centre ancien", "256 hectares régis depuis le 17 février 2025 par un plan de sauvegarde : PVC interdit pour les menuiseries, tuiles canal de réemploi "
                             "ou d’aspect vieilli, nuancier de couleurs obligatoire (" + L("règlement du PSMV", _PSMV_31) + ")."),
           ("Urbanisme", "Hors centre ancien, le PLUi-H 2025-2035 de Toulouse Métropole s’applique depuis le 26 janvier 2026 ("
                         + L("Toulouse Métropole", "https://metropole.toulouse.fr/actualites/le-nouveau-plui-h-est-applicable") + ")."),
           ("Termites", "Toute la Haute-Garonne est déclarée zone infestée par arrêté préfectoral du 10 décembre 2001. Aucun arrêté ne vise la mérule ("
                        + L("préfecture", "https://www.haute-garonne.gouv.fr/Politiques-publiques/Habitat-logement-et-hebergement/Merules-et-termites/Reglementation-merule") + ")."),
           ("Bruit des avions", "Autour de l’aéroport de Blagnac, le plan de gêne sonore ouvre droit à l’aide Silencio pour insonoriser son logement ("
                                + L("France 3", _SILENCIO) + ")."),
           ("Climat", "Zone climatique H2c. Le vent d’autan, de sud-est, souffle par rafales : 92 jours d’au moins 57 km/h à Blagnac en 2025 ("
                      + L("Météo-France", _VENT_31) + ").")],
    trades_intro="Appartements, hôtels particuliers du centre ou « toulousaines », ces maisons de faubourg à toit à deux pentes : les règles changent selon que vous êtes dans le centre ancien ou non.",
    trades={
        "toiture": ["Le toit toulousain est en tuile canal, avec une pente traditionnelle de 33 % (" + L("ministère de la Culture", "https://www.culture.gouv.fr/Media/medias-creation-rapide/Les-toitures-en-tuiles-canal") + "). "
                    "Dans le centre ancien, tout travail de toiture demande une déclaration préalable avec l’accord de l’architecte des Bâtiments de France, "
                    "et les gouttières sont en zinc ou en cuivre : le PVC est interdit.",
                    "Après un épisode de vent d’autan, faites vérifier les tuiles déplacées avant la pluie."],
        "facade": ["Brique foraine pour les décors, briques de second choix ou galets destinés à être enduits : c’est la façade toulousaine ("
                   + L("Ville de Toulouse et architecte des Bâtiments de France", "https://www.culture.gouv.fr/content/download/106372/file/Toulouse_ville_et_faubourgs.pdf") + ").",
                   "Dans les campagnes obligatoires et le centre ancien, le ravalement demande une déclaration préalable. Les propriétaires concernés peuvent obtenir "
                   "une aide de la Ville : renseignez-vous avant de signer (" + L("Toulouse Métropole", _TM_RAV) + ")."],
        "fenetres": ["Dans le centre ancien, le PVC est interdit et le bois peint sert de référence pour les menuiseries (" + L("PSMV", _PSMV_31) + ").",
                     "Près de l’aéroport, l’aide Silencio finance au moins 80 % de l’insonorisation, jusqu’à 100 % pour les ménages modestes, dans la limite "
                     "d’un plafond, si le logement est dans le plan de gêne sonore."],
        "charpente": ["Toute la Haute-Garonne est zone infestée par les termites depuis 2001 : profitez d’une réfection de toiture pour faire contrôler "
                      "et, si besoin, traiter la charpente.",
                      "À la vente, un état relatif à la présence de termites de moins de 6 mois est obligatoire."],
        "isolation": ["Pour les propriétaires occupants, la prime éco-rénovation de Toulouse Métropole va de 1 000 € pour un gain énergétique d’au moins 40 % "
                      "jusqu’à 8 500 € avec les bonus. Elle demande au moins deux travaux, ou une isolation par l’extérieur seule, et un audit ("
                      + L("Toulouse Métropole Rénov’", "https://renov.toulouse-metropole.fr/particuliers/aides-financieres/proprietaire-occupant/") + ").",
                      "Isolation par l’extérieur : déclaration préalable, et débord sur le trottoir limité à 16 cm par le règlement de voirie ("
                      + L("Toulouse Métropole", "https://renov.toulouse-metropole.fr/wp-content/uploads/sites/15/Demandes-dautorisation-ITE.pdf") + ")."]},
    steps_intro="Dans l’ordre, du centre ancien aux faubourgs.",
    steps=[("Vérifiez si vous êtes dans le centre ancien", "Dans les 256 hectares du site patrimonial remarquable, l’architecte des Bâtiments de France doit donner son accord et le nuancier du plan de sauvegarde s’impose."),
           ("Regardez si votre rue est en campagne", "La Ville mène des campagnes de ravalement obligatoire, avec des aides. Renseignez-vous avant la mise en demeure ("
                                                     + L("Toulouse Métropole", _TM_RAV) + ")."),
           ("Déposez la déclaration préalable", "En ligne pour la commune de Toulouse, ou à l’accueil de l’urbanisme, 6 rue René-Leduc ("
                                                + L("démarche", "https://metropole.toulouse.fr/demarches/faire-une-demande-dautorisation-durbanisme-toulouse") + ")."),
           ("Faites autoriser l’échafaudage", "L’occupation du trottoir se demande à la commune quelques semaines avant le chantier."),
           ("Passez à Toulouse Métropole Rénov’", "Conseil gratuit sur les aides, avant de signer le devis.")],
    aides_intro="Les aides se demandent avant de signer le devis, et le conseil public est gratuit.",
    aides=[("Toulouse Métropole Rénov’", "L’Espace Conseil France Rénov’ de la métropole : conseil gratuit, accueil sans rendez-vous. Maison de l’Énergie, "
                                         "1 allée Jacques-Chaban-Delmas, 31500 Toulouse. 05 34 24 59 59. " + L("renov.toulouse-metropole.fr", _TM_RENOV) + "."),
           ("Prime éco-rénovation", "Pour les propriétaires occupants : de 1 000 € à 8 500 € selon le gain énergétique, le niveau atteint et les matériaux biosourcés, "
                                    "avec un audit préalable."),
           ("Aide au ravalement", "Pour les immeubles en campagne obligatoire et dans le centre ancien : subvention de la Ville et frais d’échafaudage sur le domaine public ("
                                  + L("Toulouse Métropole", _TM_RAV) + ")."),
           ("Silencio", "Insonorisation des logements dans le plan de gêne sonore de l’aéroport : au moins 80 % des travaux, jusqu’à 100 % pour les ménages modestes, "
                        "dans la limite d’un plafond. 05 34 61 80 97."),
           NATIONAL],
    faq=[("Le ravalement est-il obligatoire à Toulouse ?",
          "Le maire peut l’imposer au moins une fois tous les dix ans : Toulouse est sur la liste préfectorale depuis 1990. La Ville procède par campagnes, "
          "rue par rue ; la 12e couvre 2025 à 2029. Les propriétaires concernés peuvent obtenir une aide de la Ville."),
         ("Peut-on poser des fenêtres en PVC dans le centre de Toulouse ?",
          "Pas dans le site patrimonial remarquable : le règlement du plan de sauvegarde de 2025 interdit le PVC et prend le bois peint pour référence. "
          "Ailleurs, déposez une déclaration préalable dès que l’aspect des fenêtres change."),
         ("Ma maison est-elle exposée aux termites ?",
          "Toute la Haute-Garonne est déclarée zone infestée depuis 2001. Faites vérifier les bois lors de travaux de toiture ou de charpente. "
          "À la vente, un état relatif aux termites de moins de 6 mois est obligatoire."),
         ("Quelles aides pour isoler sa maison à Toulouse ?",
          "La prime éco-rénovation de Toulouse Métropole, de 1 000 € à 8 500 € pour les propriétaires occupants, s’ajoute aux aides nationales comme MaPrimeRénov’. "
          "Toulouse Métropole Rénov’ vous conseille gratuitement : 05 34 24 59 59."),
         ("J’habite près de l’aéroport : puis-je faire insonoriser mes fenêtres ?",
          "Si votre logement est dans le plan de gêne sonore de Toulouse-Blagnac, l’aide Silencio finance au moins 80 % des travaux, jusqu’à 100 % pour "
          "les ménages modestes, dans la limite d’un plafond. Contact : 05 34 61 80 97."),
         ("Faut-il une autorisation pour isoler par l’extérieur ?",
          "Oui, une déclaration préalable. À Toulouse, le règlement de voirie limite le débord sur le trottoir à 16 cm.")],
)

# ——— Rouen ———
_INSEE_76 = "https://www.insee.fr/fr/statistiques/2011101?geo=COM-76540"
_PSMV_76 = ("https://metropole-rouen-normandie.fr/sites/default/files/documents/plu_approuve/Ensemble%20des%20documents%20d%27urbanisme%20communaux%20en%20"
            "vigueur%20avant%20l%27approbation%20du%20PLU%20m%C3%A9tropolitain/Rouen-76540/760540_PSMV.pdf")
_MF_76 = "https://donneespubliques.meteofrance.fr/FichesClim/FICHECLIM_76116001.pdf"
_DP_76 = "https://rouen.fr/fr/declaration-prealable-de-travaux"
_OPAH_76 = "https://rouen.fr/sites/default/files/cm/2025-06-26/11-28ann2.pdf"
_TERM_76 = "https://www.seine-maritime.gouv.fr/contenu/telechargement/57813/406431/file/Arr%C3%AAt%C3%A9%20termites%20SM%20sign%C3%A9%2012062023.pdf"
_CEE_76 = "https://cheque-eco-energie.normandie.fr/sites/default/files/2026-07/Fiche%20compatibilit%C3%A9%20BBC%20Normandie%20juin%202026.pdf"
_EM_76 = "https://energies.metropole-rouen-normandie.fr/"
ROUEN = dict(
    tldr="À Rouen, le centre ancien est un secteur sauvegardé depuis 1964 : toute modification d’aspect y demande l’avis de l’architecte des Bâtiments de France",
    hook="Secteur sauvegardé depuis 1964, ardoise et pans de bois.",
    slug="rouen", name="Rouen", cp="76000", wiki="https://fr.wikipedia.org/wiki/Rouen", wikidata="Q30974",
    title="Devis travaux à Rouen : toiture, façade, fenêtres, isolation",
    desc="Travaux à Rouen : secteur sauvegardé, ravalement, ardoise et pans de bois, aides de la Région et de la Métropole. Un seul artisan vient chiffrer, gratuitement.",
    figures_intro="Ce qui compte avant de lancer des travaux dans la ville aux cent clochers.",
    figures=[("85,8 <small>%</small>", "des logements sont des appartements", S("Insee, 2023", _INSEE_76)),
             ("49,3 <small>%</small>", "des résidences principales datent d’avant 1971", S("Insee, 2023", _INSEE_76)),
             ("134 <small>jours</small>", "de pluie par an à Rouen-Boos", S("Météo-France, normales 1991-2020", _MF_76)),
             ("1964", "création du secteur sauvegardé du centre ancien", S("ministère de la Culture", "https://pop.culture.gouv.fr/notice/merimee/SPR2800037"))],
    answer=("Près de la moitié des résidences principales datent d’avant 1971, et 85,8 % des logements sont des appartements. Partout, le ravalement "
            "demande une déclaration préalable ; rue Beauvoisine et rue Saint-Sever, la Ville l’impose. Pour une maison de plus de 15 ans, la Région aide "
            "jusqu’à 10 000 € pour une rénovation globale."),
    facts=[("Ravalement", "Soumis à déclaration préalable (" + L("Ville de Rouen", _DP_76) + "). Rue Beauvoisine et rue Saint-Sever, il est imposé par arrêté du maire, "
                          "avec une aide de 7 000 € au plus par immeuble (" + L("OPAH-RU", _OPAH_76) + ")."),
           ("Centre ancien", "Secteur sauvegardé régi par un plan de sauvegarde approuvé en 1986 : toute modification d’aspect y est soumise à autorisation, "
                             "avec l’avis de l’architecte des Bâtiments de France (" + L("PSMV", _PSMV_76) + ")."),
           ("Urbanisme", "Hors centre ancien, le PLU de la Métropole Rouen Normandie s’applique depuis le 13 février 2020, modifié pour la dernière fois en mai 2026 ("
                         + L("Métropole", "https://www.metropole-rouen-normandie.fr/le-plan-local-durbanisme-plu/les-procedures-devolution-du-plan-local-durbanisme-metropolitain") + ")."),
           ("Termites", "Rouen n’est pas en zone termites, mais trois communes voisines le sont depuis 2023 : Sotteville-lès-Rouen, Le Petit-Quevilly et "
                        "Saint-Étienne-du-Rouvray (" + L("préfecture", _TERM_76) + ")."),
           ("Climat", "847,5 mm de pluie par an et près de 50 jours de rafales d’au moins 58 km/h à Rouen-Boos, surtout de novembre à mars ("
                      + L("Météo-France", _MF_76) + ")."),
           ("Clôtures", "Une déclaration préalable est exigée pour toute clôture dans les 71 communes de la Métropole (délibération du 13 février 2020).")],
    trades_intro="À Rouen, pans de bois, pierre, brique et ardoise ont chacun leurs règles, surtout dans le centre ancien.",
    trades={
        "toiture": ["Dans le centre ancien, la couverture habituelle est l’ardoise naturelle, et la tuile plate sur les maisons à pans de bois les plus anciennes. "
                    "Tuiles mécaniques, fibrociment, ardoises posées en losange, zinc apparent et gouttières en plastique y sont refusés (" + L("PSMV", _PSMV_76) + ").",
                    "Avec 134 jours de pluie par an et des coups de vent l’hiver, faites vérifier ardoises et gouttières avant la mauvaise saison."],
        "facade": ["Pans de bois, pierre apparente, brique et pierre, maçonnerie enduite de préférence à la chaux : dans le centre ancien, les enduits en ciment gris "
                   "ou rugueux sont refusés (" + L("PSMV", _PSMV_76) + ").",
                   "Partout, le ravalement demande une déclaration préalable. Rue Beauvoisine et rue Saint-Sever, il est imposé, avec une aide de 7 000 € au plus par immeuble."],
        "fenetres": ["Dans le secteur sauvegardé, réparer, repeindre ou remplacer les menuiseries extérieures est soumis à autorisation, avec l’avis de "
                     "l’architecte des Bâtiments de France (" + L("PSMV", _PSMV_76) + ").",
                     "Ailleurs, une déclaration préalable suffit dès que l’aspect des fenêtres change."],
        "charpente": ["Rouen n’est pas en zone termites, contrairement à Sotteville-lès-Rouen, au Petit-Quevilly et à Saint-Étienne-du-Rouvray depuis l’arrêté "
                      "préfectoral du 12 juin 2023.",
                      "Pour une maison à pans de bois, faites vérifier les bois apparents et la charpente avant un ravalement."],
        "isolation": ["Le chèque éco-énergie Normandie aide les propriétaires de maisons de plus de 15 ans : 600 € pour l’audit, 6 500 € pour une première étape "
                      "et 10 000 € pour une rénovation globale de niveau BBC (" + L("Région Normandie", _CEE_76) + ").",
                      "Dans le centre ancien, une isolation par l’extérieur change l’aspect de la façade et demande l’avis de l’architecte des Bâtiments de France. "
                      "L’isolation des combles ne touche pas à la façade."]},
    steps_intro="Dans l’ordre, du centre ancien aux quartiers récents.",
    steps=[("Vérifiez si vous êtes dans le secteur sauvegardé", "Dans le centre ancien ou aux abords d’un monument historique, l’architecte des Bâtiments de France donne son avis."),
           ("Regardez si votre rue est en campagne", "Rue Beauvoisine et rue Saint-Sever, le ravalement est imposé par arrêté du maire, avec une aide de l’OPAH-RU."),
           ("Déposez la déclaration préalable", "En ligne sur le " + L("guichet GNAU", "https://gnau.metropole-rouen-normandie.fr/gnauProd/#/") + ", ou à la direction de "
                                                "l’urbanisme, 14 bis avenue Pasteur. 02 76 30 31 00 (" + L("Ville de Rouen", _DP_76) + ")."),
           ("Faites autoriser l’échafaudage", "L’occupation du trottoir se demande à la direction des Espaces publics et naturels de la Ville. 02 35 08 87 45 ("
                                              + L("démarche", "https://rouen.fr/fr/occupation-domaine-public-travaux") + ")."),
           ("Passez par Énergies Métropole", "Conseil gratuit sur les travaux et les aides, avant de signer le devis.")],
    aides_intro="Les aides se demandent avant de signer le devis, et le conseil public est gratuit.",
    aides=[("Énergies Métropole", "L’Espace Conseil France Rénov’ de la Métropole Rouen Normandie : conseil gratuit et neutre. 9 bis rue Jeanne-d’Arc, 76000 Rouen. "
                                  "02 76 30 32 32. " + L("energies.metropole-rouen-normandie.fr", _EM_76) + "."),
           ("OPAH-RU de Rouen 2024-2029", "Ville, Métropole et Anah aident à rénover près de 500 logements du centre-ville, avec un volet ravalement : jusqu’à 7 000 € "
                                          "par immeuble dans les rues concernées (" + L("Métropole", "https://www.metropole-rouen-normandie.fr/file-download/download/public/636734") + ")."),
           ("Chèque éco-énergie Normandie", "Pour les maisons de plus de 15 ans : 600 € pour l’audit, 6 500 € pour une première étape BBC, 10 000 € pour une "
                                            "rénovation globale BBC (" + L("Région Normandie", "https://www.normandie.fr/idee-action-cheque-eco-energie-normandie-aide-travaux") + ")."),
           NATIONAL],
    faq=[("Le ravalement est-il obligatoire à Rouen ?",
          "La Ville l’impose par campagnes et par arrêté du maire : en ce moment rue Beauvoisine et rue Saint-Sever, avec une aide de 7 000 € au plus par immeuble. "
          "Partout, un ravalement demande une déclaration préalable."),
         ("Quelles règles dans le centre ancien de Rouen ?",
          "C’est un secteur sauvegardé depuis 1964, régi par un plan de sauvegarde : toute modification d’aspect y est soumise à autorisation, avec l’avis de "
          "l’architecte des Bâtiments de France. Tuiles mécaniques, ardoises en losange, zinc apparent, gouttières en plastique et enduits en ciment gris y sont refusés."),
         ("Peut-on changer ses fenêtres dans le secteur sauvegardé ?",
          "Oui, avec une autorisation : réparer, repeindre ou remplacer des menuiseries extérieures y est soumis à autorisation et à l’avis de l’architecte des Bâtiments de France."),
         ("Rouen est-elle en zone termites ?",
          "Non. Trois communes voisines le sont depuis l’arrêté préfectoral du 12 juin 2023 : Sotteville-lès-Rouen, Le Petit-Quevilly et Saint-Étienne-du-Rouvray."),
         ("Quelles aides pour rénover sa maison à Rouen ?",
          "Le chèque éco-énergie Normandie (600 € pour l’audit, jusqu’à 10 000 € pour une rénovation globale BBC), l’OPAH-RU dans le centre-ville et les aides nationales "
          "comme MaPrimeRénov’. Énergies Métropole vous conseille gratuitement : 02 76 30 32 32."),
         ("Comment déposer une déclaration préalable à Rouen ?",
          "En ligne sur le guichet numérique GNAU de la Métropole, ou à la direction de l’urbanisme, 14 bis avenue Pasteur (02 76 30 31 00).")],
)

# ——— Marseille ———
_MELODI_13 = "https://api.insee.fr/melodi/data/DS_RP_LOGEMENT_PRINC?GEO=COM-13055"
_AMP_COPRO = "https://ampmetropole.fr/missions/habitat-logement/politique-de-lhabitat/accompagner-les-coproprietes/"
_AVAP_13 = "https://plui.ampmetropole.fr/assets/documents/PLUi_CT1_R1_AVAP_SPR_2_Rglt_T1_Prescriptions_generales.pdf"
_AVAP_13_RP = "https://plui.ampmetropole.fr/assets/documents/PLUi_CT1_R1_AVAP_SPR_1_RP_L1_0_Sommaire_1_Preambule.pdf"
_EIE_13 = "https://plui.ampmetropole.fr/assets/documents/PLUi_CT1_C2_EtatInitialEnviro.pdf"
_SOLEAM = "https://www.soleam.net/projets/ravalements-de-facades/"
_UDAP_13 = ("https://www.culture.gouv.fr/regions/drac-provence-alpes-cote-d-azur/la-direction-regionale-des-affaires-culturelles-drac-provence-alpes-cote-d-azur/"
            "unites-departementales-de-l-architecture-et-du-patrimoine-udap-de-provence-alpes-cote-d-azur/udap-des-bouches-du-rhone")
_TUILE_13 = ("https://www.culture.gouv.fr/Media/Regions/Drac-Paca/Files/Aides-demarches/Demarches-et-conseils-architecture-patrimoine/Fiches-conseil/"
             "Stap-des-Bouches-du-Rhone/16-Les-toitures-en-tuiles-plates-dites-marseillaises")
_CAUE_13 = "https://www.caue13.fr/sites/default/files/2021-09/04_FICHE-PRATIQUE_AUTORISATION-URBA_Modifier%20laspect%20exterieur%20construction.pdf"
_CEREMA = "https://www.cerema.fr/fr/actualites/cartographie-nationale-termites-merules"
_CD13 = "https://departement13.fr/en-actions/logement-habitat/les-dispositifs-aides/habitat-des-aides-concretes-pour-realiser-vos"
_ALEC_13 = "https://www.alecmetropolemarseillaise.fr/ouverture-de-maprimerenov-au-23-fevrier-2026/"
_MP_SON = "https://www.marseille.aeroport.fr/societe/transitions/aide-insonorisation"
MARSEILLE = dict(
    tldr="À Marseille, le maire peut imposer un ravalement tous les dix ans, et tout le département est en zone termites",
    hook="Ravalement imposé, et tout le département en zone termites.",
    slug="marseille", name="Marseille", cp="13008", wiki="https://fr.wikipedia.org/wiki/Marseille", wikidata="Q23482",
    title="Devis travaux à Marseille : toiture, façade, fenêtres",
    desc="Travaux à Marseille : ravalement imposé, centre-ville protégé, mistral, termites, aides du Département. Un seul artisan vient chiffrer, gratuitement.",
    figures_intro="Ce qui compte avant de lancer des travaux à Marseille.",
    figures=[("72 <small>%</small>", "des logements sont en copropriété", S("Métropole Aix-Marseille-Provence", _AMP_COPRO)),
             ("56,7 <small>%</small>", "des résidences principales datent d’avant 1971", S("Insee, 2023", _MELODI_13)),
             ("472 <small>ha</small>", "de site patrimonial remarquable en centre-ville", S("AVAP, 2018", _AVAP_13_RP)),
             ("65 <small>jours</small>", "de mistral par an, avec des rafales au-delà de 100 km/h", S("PLUi, état initial de l’environnement", _EIE_13))],
    answer=("Près de trois logements sur quatre sont en copropriété (72 %), et plus de la moitié des résidences principales datent d’avant 1971. "
            "Le centre-ville forme un site patrimonial remarquable de 472 hectares avec ses propres règles : tuile canal, fenêtres en bois peint, "
            "pas d’isolation par l’extérieur sur les immeubles patrimoniaux."),
    facts=[("Ravalement", "Marseille est sur la liste préfectorale depuis l’arrêté du 4 mars 1982 : le maire peut imposer un ravalement au moins tous les dix ans. "
                          "De 2017 à 2022, quatre campagnes ont visé le centre, avec environ 2 100 immeubles mis en demeure (" + L("SOLEAM", _SOLEAM) + ")."),
           ("Centre-ville protégé", "Site patrimonial remarquable de 472 hectares depuis 2018, plus les abords de 60 monuments historiques : tuile canal en terre cuite, "
                                    "fenêtres en bois peint, isolation par l’extérieur interdite sur les immeubles patrimoniaux (" + L("règlement de l’AVAP", _AVAP_13) + ")."),
           ("Urbanisme", "Le PLUi Marseille Provence s’applique depuis le 28 janvier 2020, modifié pour la quatrième fois le 6 octobre 2025 ("
                         + L("Métropole", "https://ampmetropole.fr/missions/amenagement-du-territoire-et-urbanisme/planification-et-urbanisme/marseille-provence/") + ")."),
           ("Termites", "Tout le département est en zone de surveillance et de lutte contre les termites depuis l’arrêté du 1er septembre 2001. Pas d’arrêté mérule ("
                        + L("Cerema", _CEREMA) + ")."),
           ("Climat", "Zone climatique H3. Le mistral souffle environ 65 jours par an, avec des rafales qui dépassent régulièrement 100 km/h (" + L("PLUi", _EIE_13) + ")."),
           ("Bruit des avions", "Dans le 16e arrondissement, certains logements peuvent obtenir l’aide à l’insonorisation de l’aéroport Marseille Provence ("
                                + L("aéroport", _MP_SON) + ").")],
    trades_intro="À Marseille, la plupart des toitures et des façades se décident en assemblée générale de copropriété, des immeubles « trois fenêtres » aux grands ensembles.",
    trades={
        "toiture": ["Tuile canal et tuile plate mécanique dite « marseillaise » se partagent les toits du centre. Ne remplacez pas des tuiles marseillaises par des "
                    "tuiles canal si la pente et le style ne s’y prêtent pas, conseille l’architecte des Bâtiments de France (" + L("fiche UDAP 13", _TUILE_13) + ").",
                    "Avec environ 65 jours de mistral par an, faites vérifier tuiles et faîtage après un coup de vent."],
        "facade": ["L’immeuble « trois fenêtres » du XIXe siècle a une façade en moellon enduit ou en « enduit marseillais », un ciment naturel aux filets gravés, "
                   "parfois en pierre de La Couronne ou de Cassis (" + L("Agam", "https://www.agam.org/wp-content/uploads/2024/06/Panorama-architectural_Valide-Web.pdf") + ").",
                   "Dans le site patrimonial remarquable, les couleurs doivent correspondre à l’époque de l’immeuble, et la même couleur s’applique à tout un volume."],
        "fenetres": ["Dans le site patrimonial remarquable, les fenêtres sont en bois peint et les climatiseurs en saillie sur la façade sont interdits ("
                     + L("AVAP", _AVAP_13) + ").",
                     "Partout, changer le matériau ou la couleur de ses fenêtres demande une déclaration préalable, avec les matériaux et coloris ("
                     + L("CAUE 13", _CAUE_13) + ")."],
        "charpente": ["Tout le département des Bouches-du-Rhône est en zone de surveillance et de lutte contre les termites depuis 2001 : profitez d’une réfection "
                      "de toiture pour faire contrôler la charpente.",
                      "À la vente, un état relatif à la présence de termites de moins de 6 mois est obligatoire."],
        "isolation": ["Ici, isoler la toiture sert d’abord contre la chaleur. L’architecte des Bâtiments de France conseille d’éviter les fenêtres de toit, qui "
                      "dégradent le confort d’été (" + L("fiche UDAP 13", _TUILE_13) + ").",
                      "Le Département aide les propriétaires occupants : Provence Éco-Rénov finance 25 % des travaux, plafonnés à 4 000 €, sous conditions de revenus, "
                      "avec une entreprise RGE (" + L("Département 13", _CD13) + ")."]},
    steps_intro="Dans l’ordre, pour une maison comme pour un appartement en copropriété.",
    steps=[("Vérifiez si votre immeuble est protégé", "Dans le site patrimonial remarquable ou aux abords d’un monument historique, l’architecte des Bâtiments de France "
                                                     "donne son avis et l’instruction passe à 2 mois. " + L("UDAP 13", _UDAP_13) + " : 04 91 90 42 43, sur rendez-vous."),
           ("En copropriété, passez par le syndic", "Toiture et façade sont des parties communes : les travaux se votent en assemblée générale."),
           ("Déposez la déclaration préalable", "Pour changer les tuiles, ravaler ou changer les fenêtres, en précisant matériaux et coloris (" + L("CAUE 13", _CAUE_13) + ")."),
           ("Faites autoriser l’échafaudage", "Un échafaudage sur le trottoir demande une autorisation d’occupation du domaine public, à demander à la Ville avant le chantier."),
           ("Prenez rendez-vous avec l’ALEC", "Depuis le 23 février 2026, un rendez-vous avec un conseiller France Rénov’ est obligatoire avant de demander une aide ("
                                              + L("ALEC", _ALEC_13) + ").")],
    aides_intro="Les aides se demandent avant de signer le devis, et le conseil public est gratuit.",
    aides=[("ALEC Métropole Marseillaise", "L’Espace Conseil France Rénov’ de Marseille : conseil gratuit et neutre. 1 place du Général-de-Gaulle, 13001 Marseille. "
                                           "04 91 37 21 53. Numéro unique Allo Métropole Rénov’ : 04 88 60 21 06."),
           ("Provence Éco-Rénov", "L’aide du Département : 25 % des travaux plafonnés à 4 000 €, et 50 % plafonnés à 8 000 € dans les périmètres d’éradication de "
                                  "l’habitat indigne de Marseille. Pour les propriétaires occupants d’un logement de plus de 15 ans, sous conditions de revenus. "
                                  "Les parties communes de copropriété sont exclues (" + L("Département 13", _CD13) + ")."),
           ("Prime du Département", "1 300 € ou 2 000 € pour les propriétaires occupants modestes ou très modestes, dans un périmètre d’OPAH ou de PIG ("
                                    + L("Département 13", "https://departement13.fr/en-actions/logement-habitat/les-dispositifs-aides/aide-aux-travaux-des-proprietaires-bailleurs-et") + ")."),
           ("Insonorisation", "Certains logements du 16e arrondissement peuvent obtenir l’aide à l’insonorisation de l’aéroport Marseille Provence ("
                              + L("aéroport", _MP_SON) + ")."),
           NATIONAL],
    faq=[("Le ravalement est-il obligatoire à Marseille ?",
          "Le maire peut l’imposer au moins une fois tous les dix ans : Marseille est sur la liste préfectorale depuis 1982. De 2017 à 2022, quatre campagnes ont visé "
          "le centre-ville, avec environ 2 100 immeubles mis en demeure. Renseignez-vous auprès de la Ville pour votre rue."),
         ("Peut-on isoler par l’extérieur dans le centre de Marseille ?",
          "Pas sur les immeubles patrimoniaux du site patrimonial remarquable : son règlement l’interdit. Ailleurs, l’isolation par l’extérieur demande une déclaration préalable."),
         ("Tuile canal ou tuile marseillaise : laquelle choisir ?",
          "Celle qui correspond à l’immeuble. Dans le site patrimonial remarquable, la couverture est en tuile ronde ou canal en terre cuite. L’architecte des Bâtiments "
          "de France conseille de ne pas remplacer des tuiles marseillaises par des tuiles canal si la pente et le style ne s’y prêtent pas."),
         ("Marseille est-elle en zone termites ?",
          "Oui, comme tout le département depuis l’arrêté préfectoral du 1er septembre 2001. À la vente, un état relatif aux termites de moins de 6 mois est obligatoire."),
         ("Quelles aides pour rénover son logement à Marseille ?",
          "Provence Éco-Rénov, l’aide du Département (25 % des travaux, jusqu’à 4 000 €), la prime de 1 300 € ou 2 000 € en périmètre d’OPAH ou de PIG, et les aides "
          "nationales. Depuis le 23 février 2026, un rendez-vous France Rénov’ est obligatoire avant la demande : ALEC, 04 91 37 21 53."),
         ("Puis-je poser un climatiseur sur ma façade ?",
          "Pas en saillie apparente dans le site patrimonial remarquable : le règlement l’interdit. Ailleurs, vérifiez le PLUi et le règlement de copropriété.")],
)

# ——— Lille ———
_INSEE_59 = "https://www.insee.fr/en/statistiques/9006729?geo=COM-59350"
_GUIDE_FAC = "https://www.lille.fr/content/download/279470/3216951/file/guide-recommandations-facades.pdf"
_GUIDE_AIDES = "https://www.lille.fr/content/download/321685/3533543/file/Guide-aides-renovations.pdf"
_CHARTE = "https://www.lille.fr/Vivre-a-Lille/Mon-logement/Louer-acheter-faire-des-travaux/Faire-des-travaux/Charte-couleurs-des-facades"
_SPR_59 = "https://www.lille.fr/Vivre-a-Lille/Les-travaux-a-Lille/Les-projets-urbains/Le-Site-Patrimonial-Remarquable"
_MF_59 = "https://pas-de-calais.gouv.fr/content/download/34943/225359/file/Fiche%20m%C3%A9t%C3%A9o%20LILLE%20(59).pdf"
_MHD = "https://www.maisonhabitatdurable-lillemetropole.fr"
_ODP_59 = "https://www.lille.fr/Annuaire-des-demarches/Occupation-du-domaine-public"
LILLE = dict(
    tldr="À Lille, le ravalement est obligatoire au moins tous les dix ans, et la Ville aide à le financer, sans condition de revenus",
    hook="Ravalement obligatoire tous les dix ans, et aidé par la Ville.",
    slug="lille", name="Lille", cp="59000", wiki="https://fr.wikipedia.org/wiki/Lille", wikidata="Q648",
    title="Devis travaux à Lille : toiture, façade, fenêtres, isolation",
    desc="Travaux à Lille : ravalement tous les 10 ans, charte couleurs, Vieux-Lille protégé, aides de la Ville et de la Métropole. Un seul artisan vient chiffrer.",
    figures_intro="Ce qui compte avant de lancer des travaux à Lille.",
    figures=[("79,3 <small>%</small>", "des logements sont des appartements", S("Insee, 2023", _INSEE_59)),
             ("27,6 <small>%</small>", "des résidences principales datent d’avant 1946", S("Insee, 2023", _INSEE_59)),
             ("177 <small>ha</small>", "de site patrimonial remarquable, Vieux-Lille et centre", S("Ville de Lille", _SPR_59)),
             ("61 <small>teintes</small>", "pour les maçonneries dans la charte couleurs de la Ville", S("Ville de Lille", _CHARTE))],
    answer=("Les logements sont surtout des appartements (79 %), et plus d’un quart des résidences principales datent d’avant 1946. La façade lilloise mêle "
            "brique, badigeon et pierres locales : toute modification d’aspect demande une autorisation, et dans le Vieux-Lille, l’architecte des Bâtiments "
            "de France donne son avis."),
    facts=[("Ravalement", "Obligatoire au moins tous les 10 ans, sous injonction administrative. Toute intervention qui modifie l’aspect d’une façade demande une "
                          "autorisation d’urbanisme (" + L("guide des façades", _GUIDE_FAC) + ")."),
           ("Vieux-Lille", "Le site patrimonial remarquable couvre 177 hectares depuis l’arrêté du 22 mars 2023 ; son nouveau plan de sauvegarde est encore en "
                           "concertation. L’architecte des Bâtiments de France y donne son avis, comme aux abords des monuments historiques (" + L("Ville de Lille", _SPR_59) + ")."),
           ("Urbanisme", "Le PLU3 de la Métropole européenne de Lille s’applique depuis le 18 octobre 2024 (" + L("MEL", "https://plu.lillemetropole.fr") + ")."),
           ("Couleurs", "La charte de la Ville propose 61 teintes pour les maçonneries, 12 pour les joints et 130 pour les menuiseries. Palettes à l’Hôtel de Ville ("
                        + L("charte couleurs", _CHARTE) + ")."),
           ("Termites et mérule", "Aucun arrêté préfectoral dans le Nord, ni pour les termites ni pour la mérule (" + L("Cerema", "https://www.cerema.fr/fr/actualites/cartographie-nationale-termites-merules") + ", 2025)."),
           ("Climat", "Zone H1a. À Lille-Lesquin, 126 jours de pluie par an et 64 jours de rafales d’au moins 58 km/h, surtout d’octobre à mars ("
                      + L("Météo-France", _MF_59) + ", normales 1971-2000).")],
    trades_intro="Maisons de ville en brique, maisons bourgeoises, hôtels particuliers, immeubles de rapport : la Ville distingue six familles de bâti, chacune avec ses façades.",
    trades={
        "toiture": ["Avec 126 jours de pluie par an et des coups de vent d’octobre à mars, gouttières, chéneaux et solins travaillent : faites-les vérifier avant l’hiver.",
                    "Dans le Vieux-Lille et aux abords des monuments historiques, changer de matériau de couverture ou créer une fenêtre de toit passe par l’avis de "
                    "l’architecte des Bâtiments de France."],
        "facade": ["Brique, badigeon, enduit, grès, pierre blanche et pierre bleue : la Ville recommande des badigeons à la chaux et le soin des joints de brique ("
                   + L("guide des façades", _GUIDE_FAC) + ").",
                   "Son aide au ravalement : 15 €/m² traité, plafonnée à 15 000 €, sans condition de revenus, pour les propriétaires et les copropriétés ("
                   + L("guide des aides", _GUIDE_AIDES) + ", 2024). L’isolation par l’extérieur n’y est pas comptée comme du ravalement."],
        "fenetres": ["Pour remplacer des menuiseries, la Ville recommande le bois peint plutôt que le PVC ou l’aluminium, et sa charte propose 130 teintes pour "
                     "menuiseries et ferronneries.",
                     "Logement exposé au bruit routier, à partir de 65 dB(A) : la Prime Bruit de la Métropole aide à l’isolation acoustique, sous conditions de ressources ("
                     + L("Maison de l’Habitat Durable", "https://www.maisonhabitatdurable-lillemetropole.fr/news/renovation-et-confort-acoustique-une-nouvelle-aide-financiere-metropolitaine-0") + ")."],
        "charpente": ["Ni termites ni mérule : aucun arrêté préfectoral ne vise le Nord. Faites quand même contrôler les bois lors d’une réfection de toiture, "
                      "surtout après une infiltration.",
                      "Une surélévation ou une extension change l’aspect du bâtiment : déclaration préalable ou permis, selon la surface créée."],
        "isolation": ["La Ville aide les propriétaires occupants sous plafonds de l’Anah : de 15 à 25 % des travaux hors taxes, jusqu’à 40 000 €, si le logement "
                      "atteint au moins l’étiquette C après travaux (" + L("guide des aides", _GUIDE_AIDES) + ", 2024).",
                      "Pour de petits travaux d’isolation (joints, portes, fenêtres), la Métropole prend en charge 50 %, jusqu’à 2 500 €, pour les propriétaires "
                      "occupants très modestes (" + L("AMELIO", "https://ameliohabitat.fr/dispositif-petits-travaux-mel") + ")."]},
    steps_intro="Dans l’ordre, du Vieux-Lille aux quartiers.",
    steps=[("Vérifiez si vous êtes en secteur protégé", "Vieux-Lille, centre ou abords d’un monument historique : l’architecte des Bâtiments de France donne son avis. 03 28 36 78 70."),
           ("Choisissez vos teintes", "Palettes de la charte couleurs à l’Hôtel de Ville et en mairie de quartier (" + L("Ville de Lille", _CHARTE) + ")."),
           ("Déposez l’autorisation d’urbanisme", "En ligne sur le " + L("guichet GNAU", "https://gnau.lillemetropole.fr") + " de la Métropole, ou au guichet n° 7 de "
                                                  "l’Hôtel de Ville, du lundi au vendredi de 8 h 30 à 12 h. 03 20 49 51 65."),
           ("Faites autoriser l’échafaudage", "Au moins 10 jours ouvrés avant, par courriel à autorisations.temporaires@mairie-lille.fr. 03 20 49 52 50 ("
                                              + L("démarche", _ODP_59) + ")."),
           ("Demandez les aides avant les travaux", "Les aides de la Ville se demandent avant de commencer. Conseil gratuit à la Maison de l’Habitat Durable.")],
    aides_intro="Les aides se demandent avant de signer le devis, et le conseil public est gratuit.",
    aides=[("Maison de l’Habitat Durable", "L’Espace Conseil France Rénov’ de la Métropole, avec AMELIO : 7 bis rue Racine, 59000 Lille. 03 59 00 03 59. "
                                           "Conseillers AMELIO : 03 20 21 27 77. " + L("maisonhabitatdurable-lillemetropole.fr", _MHD) + "."),
           ("Aide au ravalement", "La Ville verse 15 €/m² traité, plafonnés à 15 000 €, sans condition de revenus, aux propriétaires et aux syndicats de copropriétaires ("
                                  + L("guide des aides", _GUIDE_AIDES) + ", 2024)."),
           ("Passoire thermique et Haute performance", "15 à 25 % des travaux hors taxes, plafonnés à 25 000 ou 40 000 €, pour les propriétaires occupants sous plafonds "
                                                        "de l’Anah, avec au moins l’étiquette C après travaux et un artisan RGE."),
           ("Petits travaux et Prime Bruit", "La Métropole finance 50 % de petits travaux d’isolation, jusqu’à 2 500 €, pour les ménages très modestes, et aide à isoler "
                                             "du bruit routier les logements exposés."),
           NATIONAL],
    faq=[("Le ravalement est-il obligatoire à Lille ?",
          "Oui, au moins tous les dix ans, sous injonction administrative, rappelle la Ville. Toute modification de l’aspect d’une façade demande une autorisation "
          "d’urbanisme. La Ville aide à hauteur de 15 €/m² traité, jusqu’à 15 000 €, sans condition de revenus (guide des aides, 2024)."),
         ("Quelles couleurs pour ma façade à Lille ?",
          "La charte couleurs de la Ville propose 61 teintes pour les maçonneries, 12 pour les joints et 130 pour les menuiseries et ferronneries. "
          "Les palettes sont à l’Hôtel de Ville et en mairie de quartier."),
         ("Peut-on poser des fenêtres en PVC à Lille ?",
          "La Ville recommande le bois peint plutôt que le PVC ou l’aluminium pour remplacer des menuiseries. Dans le Vieux-Lille et aux abords des monuments "
          "historiques, l’architecte des Bâtiments de France donne son avis."),
         ("Lille est-elle concernée par les termites ou la mérule ?",
          "Non : aucun arrêté préfectoral ne vise le Nord, ni pour les termites ni pour la mérule (Cerema, 2025)."),
         ("Quelles aides pour rénover son logement à Lille ?",
          "Aide au ravalement de la Ville, aides Passoire thermique et Haute performance pour les propriétaires occupants, petits travaux et Prime Bruit de la Métropole, "
          "et aides nationales. Conseil gratuit à la Maison de l’Habitat Durable : 03 59 00 03 59."),
         ("Comment faire autoriser un échafaudage à Lille ?",
          "Demandez une autorisation d’occupation du domaine public au moins 10 jours ouvrés avant, par courriel à autorisations.temporaires@mairie-lille.fr (03 20 49 52 50).")],
)

# ——— Lyon ———
_INSEE_69 = "https://www.insee.fr/fr/statistiques/8997194"
_RAV_69 = "https://www.lyon.fr/demarche/logement-habitat/ravalement-de-facades"
_DP_RAV_69 = "https://www.lyon.fr/sites/lyonfr/files/content/documents/2025-02/imprim%C3%A9%20pi%C3%A8ces%20DP%20ravalement.pdf"
_TYPO_69 = "https://www.lyon.fr/sites/lyonfr/files/content/documents/2024-04/Fiches_typogiques_Charte_2024_.pdf"
_CHARTE_69 = "https://www.lyon.fr/sites/lyonfr/files/content/documents/2026-09/charte-2024-cahier-methodologique.pdf"
_UNESCO_69 = "https://www.lyon.fr/node/851616"
_SPR_69 = "https://www.grandlyon.com/services/sites-patrimoniaux-remarquables"
_ALEC_69 = "https://www.alec-lyon.org/services/aides-et-accompagnements/ecorenov-service-aide-eco-renovation-des-logements/"
_MF_69 = "https://donneespubliques.meteofrance.fr/FichesClim/FICHECLIM_69029001.pdf"
_ODP_69 = "https://www.lyon.fr/demarche/stationnement/demander-une-autorisation-pour-loccupation-du-domaine-public-pour-travaux"
LYON = dict(
    tldr="À Lyon, la Ville impose le ravalement rue par rue, et Écoréno’v aide tous les propriétaires à rénover, sans condition de ressources",
    hook="Site Unesco et nichoirs à martinets.",
    slug="lyon", name="Lyon", cp="69003", wiki="https://fr.wikipedia.org/wiki/Lyon", wikidata="Q456",
    title="Devis travaux à Lyon : toiture, façade, fenêtres, isolation",
    desc="Travaux à Lyon : ravalement imposé, site Unesco, nichoirs à martinets, aides Écoréno’v. Un seul artisan vient chiffrer, gratuitement.",
    figures_intro="Ce qui compte avant de lancer des travaux à Lyon.",
    figures=[("96,1 <small>%</small>", "des logements sont des appartements", S("Insee, 2023", _INSEE_69)),
             ("45,5 <small>%</small>", "des résidences principales datent d’avant 1971", S("Insee, 2023", _INSEE_69)),
             ("427 <small>ha</small>", "de site historique inscrit à l’Unesco depuis 1998", S("Ville de Lyon", _UNESCO_69)),
             ("30,6 <small>jours</small>", "par an à 30 °C ou plus à Lyon-Bron", S("Météo-France, normales 1991-2020", _MF_69))],
    answer=("Sur 100 logements, 96 sont des appartements : la plupart des travaux de toiture et de façade se votent en copropriété. Tout ravalement "
            "demande une déclaration préalable. Dans le site historique inscrit à l’Unesco et les deux sites patrimoniaux remarquables, l’architecte des "
            "Bâtiments de France donne son avis."),
    facts=[("Ravalement", "Obligatoire tous les dix ans depuis l’arrêté préfectoral du 18 octobre 1977. L’arrêté pluriannuel 2021-2026 fixe les rues, année par année ; "
                          "après l’injonction, le propriétaire a un an pour faire les travaux (" + L("Ville de Lyon", _RAV_69) + ")."),
           ("Déclaration préalable", "Exigée pour tout ravalement, d’immeuble comme de maison (" + L("Ville de Lyon", _DP_RAV_69) + ")."),
           ("Patrimoine", "Site historique inscrit à l’Unesco : 427 hectares de Fourvière, du Vieux-Lyon, des pentes de la Croix-Rousse et de la Presqu’île. Le Vieux-Lyon "
                          "et les pentes de la Croix-Rousse sont des sites patrimoniaux remarquables (" + L("Métropole de Lyon", _SPR_69) + ")."),
           ("Urbanisme", "Le PLU-H de la Métropole s’applique depuis 2019 ; sa modification n° 4 est exécutoire depuis le 23 janvier 2025 ("
                         + L("Métropole de Lyon", "https://www.grandlyon.com/services/procedures-approuvees-plu-h") + ")."),
           ("Termites et mérule", "Lyon est en partie couverte par un arrêté termites de 2009 et par un arrêté mérule de 2023, le seul du Rhône ("
                                  + L("Cerema", "https://www.cerema.fr/fr/actualites/cartographie-nationale-termites-merules") + ")."),
           ("Martinets", "Avant un ravalement, la Ville demande un diagnostic des oiseaux nicheurs, et le PLU-H prévoit des nichoirs à martinets (article 3.1.7).")],
    trades_intro="Enduit à la chaux, pierre de taille, ciment moulé, pisé de la Croix-Rousse : la charte du ravalement de la Ville recense 12 types de façades.",
    trades={
        "toiture": ["Le Rhône marque la limite nord des toits à faible pente couverts de tuile creuse, dite tuile canal, en terre cuite ("
                    + L("fiche UDAP 69", "https://www.culture.gouv.fr/Media/medias-creation-rapide/Fiche-conseil-n-3-Les-couvertures-dans-le-Rhone2") + "). "
                    "La Ville prévoit aussi des couvertures en zinc et des brisis en ardoise ou en zinc.",
                    "Dans les secteurs protégés, les fenêtres de toit sont limitées en taille et en nombre (" + L("charte 2024", _CHARTE_69) + ")."],
        "facade": ["La façade lyonnaise la plus courante est un enduit à la chaux sur moellons de pierre, avec un rez-de-chaussée en pierre de taille. On trouve aussi "
                   "le ciment prompt moulé rive gauche et le pisé de terre sur le plateau de la Croix-Rousse (" + L("fiches de la Ville", _TYPO_69) + ", 2024).",
                   "Un ravalement d’au moins 50 % d’une paroi oblige en principe à isoler (article R173-4 du code de la construction), sauf exceptions prévues par le texte."],
        "fenetres": ["Dans les secteurs protégés, le PVC et le blanc pur sont proscrits dans de nombreux cas (" + L("charte 2024", _CHARTE_69) + "). "
                     "L’avis de l’architecte des Bâtiments de France est requis en site patrimonial remarquable et aux abords des monuments historiques.",
                     "Ailleurs, changer l’aspect de ses fenêtres demande une déclaration préalable."],
        "charpente": ["Lyon est en partie concernée par l’arrêté préfectoral termites du 27 mai 2009, avec Sainte-Foy-lès-Lyon et Francheville, et par l’arrêté "
                      "mérule du 30 mai 2023. Faites contrôler les bois lors d’une réfection de toiture.",
                      "À la vente, l’état relatif aux termites est obligatoire dans les zones délimitées par arrêté."],
        "isolation": ["Écoréno’v, l’aide de la Métropole, s’adresse à tous les propriétaires, sans condition de ressources : audit, maîtrise d’œuvre et travaux "
                      "de rénovation globale, avec des bonus pour les matériaux biosourcés et le confort d’été (" + L("ALEC Lyon", _ALEC_69) + ").",
                      "Avec 30,6 jours par an à 30 °C ou plus à Lyon-Bron, isoler la toiture protège aussi de la chaleur."]},
    steps_intro="Dans l’ordre, pour un immeuble comme pour une maison.",
    steps=[("Vérifiez si votre rue est en campagne", "L’arrêté pluriannuel 2021-2026 liste les rues, année par année. Après l’injonction, vous avez un an pour faire les travaux ("
                                                    + L("Ville de Lyon", _RAV_69) + ")."),
           ("Vérifiez la protection de l’adresse", "Site Unesco, Vieux-Lyon, pentes de la Croix-Rousse ou abords d’un monument historique : l’architecte des Bâtiments de France donne son avis."),
           ("Faites le diagnostic des oiseaux", "Avant un ravalement, la Ville demande de repérer martinets et hirondelles, et le PLU-H prévoit des nichoirs ("
                                                + L("pièces à fournir", _DP_RAV_69) + ")."),
           ("Déposez la déclaration préalable", "En ligne sur " + L("Toodego", "https://urbanisme.toodego.com/guichet") + ", ou au service urbanisme appliqué, "
                                                "198 avenue Jean-Jaurès, 69007 Lyon. 04 26 99 63 80."),
           ("Demandez le permis de stationnement", "Pour un échafaudage, en ligne au moins 8 jours avant. Le tarif passe de 26,50 € à 1,80 € par m² et par mois pour un "
                                                   "ravalement obligatoire ou des travaux thermiques (" + L("Ville de Lyon", _ODP_69) + ").")],
    aides_intro="Les aides se demandent avant de signer le devis, et le conseil public est gratuit.",
    aides=[("ALEC Lyon", "L’Espace Conseil France Rénov’ de la Métropole : 12-14 avenue Antoine-Dutrievoz, 69100 Villeurbanne. 04 37 48 25 90, du lundi au vendredi, "
                         "de 9 h à 12 h et de 14 h à 17 h. " + L("alec-lyon.org", "https://www.alec-lyon.org/contact/") + "."),
           ("Écoréno’v", "L’aide de la Métropole, pour tous les propriétaires. En copropriété : 3 500 € par lot pour le niveau BBC, 2 000 € pour au moins 35 % de gain, "
                         "plus des bonus (" + L("ALEC Lyon", _ALEC_69) + ", règlement 2024)."),
           ("Aides de la Ville", "Valorisation du patrimoine architectural (40 % de certains travaux), Écopatrimoine pour les enduits correcteurs thermiques, restauration des traboules ("
                                 + L("synthèse des aides", "https://www.lyon.fr/sites/lyonfr/files/content/documents/2024-06/synthese-aides-financieres-renovation.pdf") + ", 2024)."),
           NATIONAL],
    faq=[("Le ravalement est-il obligatoire à Lyon ?",
          "Oui, tous les dix ans, depuis l’arrêté préfectoral de 1977. La Ville l’impose rue par rue selon l’arrêté pluriannuel 2021-2026 : après l’injonction, "
          "le propriétaire a un an pour faire les travaux. Tout ravalement demande une déclaration préalable."),
         ("Pourquoi poser des nichoirs à martinets lors d’un ravalement ?",
          "Le PLU-H de la Métropole le prévoit (article 3.1.7) : avant un ravalement, la Ville demande un diagnostic des oiseaux nicheurs, martinets et hirondelles, "
          "pour ne pas détruire leurs nids et leur offrir des nichoirs."),
         ("Peut-on poser des fenêtres en PVC à Lyon ?",
          "Dans les secteurs protégés, le PVC et le blanc pur sont proscrits dans de nombreux cas, et l’architecte des Bâtiments de France donne son avis. "
          "Ailleurs, une déclaration préalable suffit dès que l’aspect change."),
         ("Lyon est-elle concernée par les termites et la mérule ?",
          "En partie : un arrêté préfectoral de 2009 délimite des zones termites, et un arrêté de 2023 des zones mérule. Faites contrôler les bois lors de travaux de toiture."),
         ("Quelles aides pour rénover son logement à Lyon ?",
          "Écoréno’v, l’aide de la Métropole, sans condition de ressources, les aides patrimoniales de la Ville et les aides nationales. L’ALEC vous conseille "
          "gratuitement : 04 37 48 25 90."),
         ("Combien coûte un échafaudage sur le trottoir à Lyon ?",
          "Le permis de stationnement coûte 20 € de droit fixe, puis 26,50 € par m² et par mois, ou 1,80 € pour un ravalement obligatoire fait dans les deux ans "
          "suivant l’injonction ou des travaux thermiques. Demande en ligne au moins 8 jours avant.")],
)

CITIES = [LILLE, ROUEN, PARIS, LYON, MARSEILLE, TOULOUSE]

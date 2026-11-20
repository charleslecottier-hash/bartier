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
    slug="paris", name="Paris", cp="75011", wiki="https://fr.wikipedia.org/wiki/Paris", wikidata="Q90",
    title="Devis travaux à Paris : toiture, façade, fenêtres, isolation",
    desc="Travaux à Paris : ravalement tous les 10 ans, déclaration préalable, architecte des Bâtiments de France, aides. Un seul artisan vient chiffrer, gratuitement.",
    figures_intro="Ce qui compte avant de lancer des travaux dans la capitale.",
    figures=[("97 <small>%</small>", "des logements sont des appartements", S("Insee, 2022", _INSEE_75)),
             ("48,7 <small>%</small>", "des résidences principales datent d’avant 1946", S("Insee, 2022", _INSEE_75)),
             ("94 <small>%</small>", "des logements sont dans un périmètre de protection du patrimoine", S("SDES, 2024", _SDES)),
             ("10 <small>ans</small>", "au plus entre deux ravalements, sur injonction du maire", S("Service-Public", SP + "F640"))],
    answer=("À Paris, presque tout se joue en copropriété : 97 % des logements sont des appartements. Le ravalement est obligatoire au moins "
            "tous les dix ans, tout changement d’aspect extérieur demande une déclaration préalable, même pour des fenêtres à l’identique, "
            "et 94 % des logements sont dans un périmètre où l’architecte des Bâtiments de France donne son avis."),
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
    aides_intro="Les aides se demandent avant de signer le devis. Le conseil public, lui, est gratuit.",
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
    slug="toulouse", name="Toulouse", cp="31000", wiki="https://fr.wikipedia.org/wiki/Toulouse", wikidata="Q7880",
    title="Devis travaux à Toulouse : toiture, façade, fenêtres",
    desc="Travaux à Toulouse : centre ancien protégé, campagnes de ravalement, termites, aides de la Métropole. Un seul artisan vient chiffrer, gratuitement.",
    figures_intro="Ce qui compte avant de lancer des travaux dans la ville rose.",
    figures=[("84 <small>%</small>", "des logements sont des appartements", S("Insee, 2023", _MELODI_31)),
             ("34,3 <small>%</small>", "des résidences principales datent d’avant 1971", S("Insee, 2023", _MELODI_31)),
             ("256 <small>ha</small>", "de centre ancien protégé, où l’architecte des Bâtiments de France donne son accord", S("PSMV, 2025", _PSMV_31)),
             ("92 <small>jours</small>", "de rafales d’au moins 57 km/h à Blagnac en 2025 : le vent d’autan", S("Météo-France", _VENT_31))],
    answer=("À Toulouse, 84 % des logements sont des appartements et le centre ancien forme un site patrimonial remarquable de 256 hectares, "
            "où l’architecte des Bâtiments de France donne un avis conforme. Le maire peut imposer un ravalement tous les dix ans : la Ville "
            "procède par campagnes, avec des aides."),
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
    aides_intro="Les aides se demandent avant de signer le devis. Le conseil public, lui, est gratuit.",
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
    slug="rouen", name="Rouen", cp="76000", wiki="https://fr.wikipedia.org/wiki/Rouen", wikidata="Q30974",
    title="Devis travaux à Rouen : toiture, façade, fenêtres, isolation",
    desc="Travaux à Rouen : secteur sauvegardé, ravalement, ardoise et pans de bois, aides de la Région et de la Métropole. Un seul artisan vient chiffrer, gratuitement.",
    figures_intro="Ce qui compte avant de lancer des travaux dans la ville aux cent clochers.",
    figures=[("85,8 <small>%</small>", "des logements sont des appartements", S("Insee, 2023", _INSEE_76)),
             ("49,3 <small>%</small>", "des résidences principales datent d’avant 1971", S("Insee, 2023", _INSEE_76)),
             ("134 <small>jours</small>", "de pluie par an à Rouen-Boos", S("Météo-France, normales 1991-2020", _MF_76)),
             ("1964", "création du secteur sauvegardé du centre ancien", S("ministère de la Culture", "https://pop.culture.gouv.fr/notice/merimee/SPR2800037"))],
    answer=("À Rouen, 85,8 % des logements sont des appartements et près de la moitié des résidences principales datent d’avant 1971. Dans le centre ancien, "
            "secteur sauvegardé depuis 1964, toute modification d’aspect passe par l’architecte des Bâtiments de France. Le ravalement demande une "
            "déclaration préalable, et la Ville l’impose rue par rue."),
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
    trades_intro="Pans de bois, pierre, brique, ardoise : à Rouen, chaque matériau a ses règles, surtout dans le centre ancien.",
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
    aides_intro="Les aides se demandent avant de signer le devis. Le conseil public, lui, est gratuit.",
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

CITIES = [ROUEN, PARIS, TOULOUSE]

from villes_data import L, S, SP, NATIONAL  # liens dans le texte, sources discrètes, Service-Public, aides nationales
REVIEWED = "2026-11-21"

# Sources consultées le 21/11/2026. La fiche « dossier complet » d'insee.fr renvoyait une erreur 500 ce jour-là :
# les chiffres logement viennent du même jeu de données (Logements, principaux indicateurs du dossier complet) via l'API Melodi.
_INSEE = "https://api.insee.fr/melodi/data/DS_RP_LOGEMENT_PRINC?GEO=COM-67482"
_PSMV = "https://www.strasbourg.eu/qu-est-ce-qu-un-secteur-sauvegarde-et-son-psmv"
_UNESCO = "https://www.strasbourg.eu/fr/label-patrimoine-mondial-unesco"
_FAQ = "https://www.strasbourg.eu/fr/autorisations-urbanisme-questions-reponses"
_DP = "https://www.strasbourg.eu/fr/declaration-prealable"
_GNAU = "https://www.strasbourg.eu/fr/guichet-numerique-autorisations-urbanisme-gnau"
_PLU = "https://www.strasbourg.eu/plu-eurometropole-c-est-quoi"
_PPRI = "https://www.strasbourg.eu/les-annexes-du-plu"
_ODP = "https://www.strasbourg.eu/fr/autorisation-occupation-domaine-public-arretes-circulation"
_MF = "https://donneespubliques.meteofrance.fr/FichesClim/FICHECLIM_67124001.pdf"
_SISM = "https://georisques.gouv.fr/api/v1/zonage_sismique?code_insee=67482"
_RISQ = "https://georisques.gouv.fr/api/v1/gaspar/risques?code_insee=67482"
_UDAP_FAC = "https://www.culture.gouv.fr/de/mc/content/download/80687/file/fiche_patrimoine_UDAP_Alsace%20-%20Entretenir%20la%20facade.pdf?version=2"
_UDAP_COUV = "https://www.culture.gouv.fr/de/mc/content/download/80679/file/fiche_patrimoine_UDAP_Alsace_Les_couvertures.pdf?version=4"
_UDAP_MEN = ("https://www.culture.gouv.fr/de/mc/content/download/80684/file/"
             "fiche%20patrimoine%20UDAP%20Alsace%20-%20Remplacer%20les%20menuiseries.pdf?version=3")
_UDAP_PDB = ("https://www.culture.gouv.fr/de/mc/content/download/80688/file/"
             "fiche_patrimoine_udap_Alsace%20-%20Ma%C3%A7onnerie%20et%20pans%20de%20bois.pdf?version=3")
_AGENCE = "https://www.strasbourg.eu/web/maison-habitat/w/agence-climat"
_AIDES_MI = "https://www.strasbourg.eu/web/maison-habitat/aides-renovation-energetique-maison-individuelle"
_REGL_MI = ("https://www.strasbourg.eu/documents/533445798/535974597/R%C3%A8glement-attribution+-+aides+de+l%27Eurom%C3%A9tropole+de+"
            "Strasbourg+2025+-+maison+individuelle+-+monopropri%C3%A9t%C3%A9.pdf/d37f5bee-c1e7-ff9a-4653-2c26ec199ca7?version=1.2&t=1749746711646")
_AIDES_CO = "https://www.strasbourg.eu/web/maison-habitat/aides-renovation-energetique-copropriete"
_REGL_CO = ("https://www.strasbourg.eu/documents/533445798/535974605/EMS+-+R%C3%A8glement-attribution-aides+Copropropri%C3%A9t%C3%A9+2026.pdf/"
            "ece171cd-ccac-b527-eb20-7901344891aa?version=3.0&t=1766151408202")
_ANIL_ANAH = "https://www.anil.org/aides-locales-travaux/details/bas-rhin-aide-a-la-renovation-energetique-complementaire-anah-4968/"

CITY = dict(
    slug="strasbourg", name="Strasbourg", cp="67000", insee="67482",
    lat=48.5734, lon=7.7522, dept="Bas-Rhin", depcode="67", region="Grand Est",
    wiki="https://fr.wikipedia.org/wiki/Strasbourg", wikidata="Q6602",
    verified="2026-11-21",
    tldr="À Strasbourg, le secteur sauvegardé couvre 210 hectares depuis 2023, Neustadt comprise, et un immeuble protégé y demande un permis de construire même pour un ravalement",
    hook="Secteur sauvegardé étendu à la Neustadt, tuiles écailles rouges.",
    title="Devis travaux à Strasbourg : toiture, façade, fenêtres, isolation",
    desc="Travaux à Strasbourg : secteur sauvegardé de 210 ha, tuiles écailles, fenêtres en bois aidées, aides de l’Eurométropole. Un seul artisan vient chiffrer.",
    figures_intro="Ce qui compte avant de lancer des travaux entre la Grande-Île et la Neustadt.",
    figures=[("92,4 <small>%</small>", "des logements sont des appartements", S("Insee, 2023", _INSEE)),
             ("22,2 <small>%</small>", "des résidences principales datent d’avant 1946", S("Insee, 2023", _INSEE)),
             ("210 <small>ha</small>", "de secteur sauvegardé depuis son extension à la Neustadt en 2023", S("Ville de Strasbourg", _PSMV)),
             ("59,5 <small>jours</small>", "de gel par an à Strasbourg-Entzheim", S("Météo-France, normales 1991-2020", _MF))],
    answer=("À Strasbourg, 92,4 % des logements sont des appartements et 22,2 % des résidences principales datent d’avant 1946. Depuis juillet 2023, "
            "le secteur sauvegardé couvre 210 hectares, de la Grande-Île au cœur de la Neustadt : un immeuble protégé par le plan de sauvegarde y demande "
            "un permis de construire, même pour un ravalement. Ailleurs, toute modification de l’aspect extérieur passe par une déclaration préalable."),
    facts=[("Secteur sauvegardé", "Créé en 1974, il couvre environ 210 hectares depuis l’arrêté préfectoral du 7 juillet 2023, qui l’a révisé au sud "
                                  "de la Grande-Île et étendu au nord et au cœur de la Neustadt (" + L("plan de sauvegarde", _PSMV) + "). La Grande-Île est "
                                  "inscrite à l’Unesco depuis 1988, la Neustadt depuis 2017 (" + L("Ville de Strasbourg", _UNESCO) + ")."),
           ("Permis ou déclaration", "Ravalement, fenêtre de toit : toute modification de l’aspect extérieur demande une déclaration préalable. Pour un immeuble "
                                     "protégé par le plan de sauvegarde ou inscrit monument historique, il faut un permis de construire (" + L("Eurométropole", _FAQ) + ")."),
           ("Ravalement", "La déclaration joint un échantillon de la teinte retenue, ou les références des teintes et du nuancier ("
                          + L("déclaration préalable", _DP) + "). Elle se dépose sur le guichet numérique : une demande envoyée par courriel "
                          "n’est pas prise en compte (" + L("guichet numérique", _GNAU) + ")."),
           ("Urbanisme", "Le PLU de l’Eurométropole, approuvé le 16 décembre 2016, couvre ses 33 communes depuis le 27 septembre 2019. Dernière "
                         "procédure : la modification simplifiée n° 6, approuvée le 6 février 2026 (" + L("Eurométropole", _PLU) + ")."),
           ("Risques", "Zone sismique 3, modérée (" + L("Géorisques", _SISM) + "). Géorisques recense aussi les inondations par débordement lent et par "
                       "remontée de nappe (" + L("liste des risques", _RISQ) + ") ; le plan de prévention de l’Eurométropole date du 20 avril 2018, modifié "
                       "le 5 septembre 2025 (" + L("annexes du PLU", _PPRI) + ")."),
           ("Climat", "À Strasbourg-Entzheim, 635,7 mm de pluie et 59,5 jours de gel par an. Mai, juin et juillet sont les mois les plus arrosés ("
                      + L("Météo-France", _MF) + ", normales 1991-2020).")],
    trades_intro="Maisons à pans de bois de la Grande-Île, immeubles d’architecture allemande de la Neustadt : à Strasbourg, chaque époque a ses matériaux.",
    trades={
        "toiture": ["Le toit alsacien traditionnel est en tuiles plates écailles de terre cuite rouge, dont la « Biberschwanz » ou queue-de-castor, sur des "
                    "pentes de plus de 40°. Le format courant est de 16 sur 38 cm ; l’UDAP du Bas-Rhin déconseille les tuiles béton et les tuiles noires "
                    "engobées sur le bâti ancien (" + L("fiche couvertures", _UDAP_COUV) + ", 2026).",
                    "À Entzheim, on compte 30,8 jours de rafales d’au moins 58 km/h par an, surtout de décembre à mars (" + L("Météo-France", _MF) + "). "
                    "L’UDAP conseille de sceller faîtières et arêtiers au mortier de chaux plutôt que de les poser à sec (" + L("UDAP", _UDAP_COUV) + ")."],
        "facade": ["Pour la pierre, le grès et le torchis des pans de bois, l’UDAP du Bas-Rhin recommande l’enduit à la chaux, qui laisse respirer le mur. "
                   "Les enduits ciment sont à éviter et les enduits plastiques ribbés ou granités sont proscrits (" + L("fiche façade", _UDAP_FAC) + ").",
                   "Pour repeindre une façade ancienne, immeubles d’architecture allemande compris, seule la peinture minérale au silicate convient ; "
                   "les peintures épaisses plastiques, acryliques ou vinyliques sont interdites (" + L("fiche façade", _UDAP_FAC) + "). Dans le "
                   "secteur sauvegardé, un immeuble protégé demande un permis de construire pour son ravalement (" + L("Eurométropole", _FAQ) + ")."],
        "fenetres": ["Tout changement de menuiseries extérieures demande une autorisation, même pour un remplacement dit à l’identique. La pose en "
                     "« rénovation », un nouveau dormant sur l’ancien, est proscrite ; en espace protégé, le bois peint est conservé ou restauré ("
                     + L("fiche menuiseries", _UDAP_MEN) + ", 2026).",
                     "Dans une rénovation énergétique aidée, l’Eurométropole verse un bonus si toutes les fenêtres du logement sont remplacées : 1 000 € "
                     "en bois, 1 500 € en bois-aluminium. Les fenêtres de toit comptent (" + L("règlement 2025", _REGL_MI) + ")."],
        "charpente": ["Pour un pan de bois abîmé, l’UDAP demande une pièce de bois sec de même espèce et de même dimension, jamais un mur de pierre ou de "
                      "parpaings. Gardez le torchis quand c’est possible, et les sablières à au moins 5 cm du sol (" + L("fiche pans de bois", _UDAP_PDB) + ", 2026).",
                      "Passer d’une couverture en simple recouvrement à une pose double alourdit le toit : faites vérifier que la charpente porte la charge. "
                      "Sur une charpente ancienne et saine, l’UDAP conseille plutôt une couverture plus légère (" + L("fiche couvertures", _UDAP_COUV) + ")."],
        "isolation": ["Pour une maison de plus de 15 ans en résidence principale, l’Eurométropole aide tous les revenus : 600 à 1 000 € pour un bouquet "
                      "de deux ou trois isolations (murs, toiture, plancher), 3 000 à 4 000 € pour atteindre l’étiquette B (" + L("règlement 2025", _REGL_MI) + ").",
                      "Avec un isolant biosourcé, le bonus atteint 1 500 € pour une isolation extérieure sous enduit et 2 000 € sous bardage. En copropriété, "
                      "les critères Climaxion de la Région s’appliquent : chaque paroi traitée est isolée en totalité, murs à R ≥ 5, toiture à R ≥ 7,5, "
                      "plancher bas à R ≥ 3,5 (" + L("règlement copropriétés 2026", _REGL_CO) + ")."]},
    steps_intro="Dans l’ordre, de la protection de l’immeuble à l’échafaudage.",
    steps=[("Vérifiez la protection de votre immeuble", "Secteur sauvegardé, abords d’un monument historique ou rue sans protection : la police du bâtiment "
                                                     "vous renseigne au 03 68 98 51 11 (" + L("Ville de Strasbourg", _PSMV) + ")."),
           ("Consultez l’architecte des Bâtiments de France", "UDAP du Bas-Rhin, Palais du Rhin, 2 place de la République, 67082 Strasbourg cedex. "
                                                            "03 69 08 51 00 (" + L("UDAP", _UDAP_FAC) + ")."),
           ("Déposez la déclaration ou le permis", "En ligne sur le " + L("guichet numérique", _GNAU) + " de Strasbourg, ou sur papier à la mairie, "
                                                   "1 parc de l’Étoile. 03 68 98 50 00."),
           ("Faites autoriser l’échafaudage", "L’occupant de la voie, en pratique l’entreprise, dépose la demande sur demarches.strasbourg.eu au moins 15 jours "
                                              "avant, ou 3 semaines si la circulation est modifiée, avec un plan de l’emprise. 03 68 98 51 56, de 9 h à "
                                              "11 h 30 en semaine (" + L("démarche", _ODP) + ")."),
           ("Déposez les aides avant les travaux", "Ne commencez pas le chantier avant d’avoir déposé le dossier d’aide de l’Eurométropole : c’est une "
                                                   "condition de ses aides. Conseil gratuit à l’Agence du climat.")],
    aides_intro="Les aides de l’Eurométropole se demandent avant les travaux, avec un assistant à maîtrise d’ouvrage obligatoire.",
    aides=[("Agence du climat", "L’Espace Conseil France Rénov’ de l’Eurométropole de Strasbourg : 2 avenue de la Forêt-Noire, 67000 Strasbourg. "
                                "03 69 24 83 10, les lundis, mercredis et vendredis de 9 h à 12 h 15 et de 13 h 45 à 17 h 15, le jeudi de 13 h 45 à 17 h 15. "
                                + L("Agence du climat", _AGENCE) + "."),
           ("Maisons individuelles", "Pour une maison de plus de 15 ans, sans plafond de revenus : 600 à 1 000 € par bouquet d’isolation ou 3 000 à 4 000 € "
                                     "au niveau BBC, 1 000 à 1 500 € pour la maîtrise d’œuvre, et des bonus biosourcés (jusqu’à 2 000 €), fenêtres en bois "
                                     "(jusqu’à 1 500 €) et protections solaires (jusqu’à 1 000 €). Dispositif 2024-2026 (" + L("Eurométropole", _AIDES_MI) + ", "
                                     + L("règlement 2025", _REGL_MI) + ")."),
           ("Copropriétés", "Jusqu’à 80 logements, 750 à 1 000 € par logement pour un bouquet de deux ou trois isolations, davantage au-delà, plus 500 € "
                            "par logement au niveau BBC (" + L("règlement 2026", _REGL_CO) + "). Gain énergétique d’au moins 35 % et copropriété "
                            "immatriculée (" + L("Eurométropole", _AIDES_CO) + ")."),
           ("Complément aux aides de l’Anah", "Pour les ménages modestes ou très modestes en maison de plus de 15 ans : 5 % ou 10 % des dépenses en plus de "
                                              "l’Anah, sur 40 000 € de travaux au plus, avec un gain d’au moins deux classes d’étiquette (" + L("ANIL", _ANIL_ANAH) + ", 2026)."),
           NATIONAL],
    faq=[("Faut-il une autorisation pour un ravalement à Strasbourg ?",
          "Oui. Toute modification de l’aspect extérieur demande une déclaration préalable, avec un échantillon de la teinte. Pour un immeuble protégé par "
          "le plan de sauvegarde ou inscrit monument historique, il faut un permis de construire."),
         ("Quelles règles dans le secteur sauvegardé de Strasbourg ?",
          "Depuis le 7 juillet 2023, il couvre environ 210 hectares, de la Grande-Île au cœur de la Neustadt. L’architecte des Bâtiments de France y donne "
          "son avis, et un immeuble protégé par le plan de sauvegarde demande un permis de construire. Pour savoir si votre immeuble l’est, appelez la "
          "police du bâtiment : 03 68 98 51 11."),
         ("Quelles tuiles pour un toit à Strasbourg ?",
          "Sur le bâti ancien, des tuiles plates écailles en terre cuite rouge, comme la queue-de-castor, au format courant de 16 sur 38 cm. L’UDAP du "
          "Bas-Rhin déconseille les tuiles béton et les tuiles noires engobées."),
         ("Faut-il une autorisation pour changer ses fenêtres à Strasbourg ?",
          "Oui, même à l’identique. En espace protégé, les menuiseries en bois peint sont conservées ou restaurées. Le bonus fenêtres de l’Eurométropole, "
          "jusqu’à 1 500 € par logement, est réservé au bois et au bois-aluminium."),
         ("Quelles aides pour rénover son logement à Strasbourg ?",
          "L’Eurométropole aide les maisons de plus de 15 ans sans plafond de revenus, jusqu’à 4 000 € au niveau BBC plus des bonus, ainsi que les "
          "copropriétés. Conseil gratuit à l’Agence du climat : 03 69 24 83 10."),
         ("Comment faire autoriser un échafaudage à Strasbourg ?",
          "L’entreprise qui occupe la voie demande l’occupation du domaine public sur demarches.strasbourg.eu au moins 15 jours avant, 3 semaines si "
          "la circulation est modifiée. Renseignements : 03 68 98 51 56.")],
)

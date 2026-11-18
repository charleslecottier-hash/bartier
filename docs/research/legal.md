# Cadre juridique du site vitrine B2B : France et Belgique

État au 17 novembre 2026. Recherche documentaire, pas un avis juridique. Chaque source [Sx] a été ouverte pendant la session. Limites : Légifrance n'a pu être lu que par extraction assistée (citations courtes, pas de texte intégral) ; economie.gouv.fr (fiches DGCCRF), le site principal du SPF Économie et ejustice.be étaient inaccessibles. Les points belges reposent donc sur l'APD, la Chambre, DNCM et le droit de l'Union.

## Trois points qui conditionnent le contenu

1. **Rappel de particuliers.** Depuis le 11 août 2026, démarcher un consommateur par téléphone sans consentement préalable est interdit, y compris « par l'intermédiaire d'un tiers agissant pour son compte » [S30]. En rénovation énergétique et adaptation du logement, l'interdiction est totale, sauf rappel d'une demande d'information prouvée, passé sous 5 jours ouvrables et limité à l'objet demandé [S29][S31]. Le site ne peut promettre ni une « conformité garantie », ni un rappel « en moins de 5 minutes » sans condition d'horaires.
2. **Pixel Meta et GA4.** Aucun chargement avant consentement ; refuser doit être aussi simple qu'accepter [S16][S18].
3. **Allégations.** La tromperie est sanctionnée aussi entre professionnels ; commise en ligne, elle est punie de 5 ans et 750 000 € [S41][S42].

## 1. Mentions légales, Belgique, langue

| Règle | À faire sur le site | Risque |
|---|---|---|
| LCEN art. 1-1 (ancien art. 6-III, déplacé par la loi du 21 mai 2024) : dénomination, siège, téléphone, numéro d'immatriculation, capital, directeur de la publication, hébergeur (nom, adresse, téléphone) [S1]. Service-Public ajoute forme juridique, e-mail et numéro de TVA [S2]. | Page « Mentions légales » liée en pied de chaque page, en français et en anglais. Hébergeur : coordonnées de Vercel. | Élevé en sanction : 1 an et 75 000 € pour le dirigeant, 375 000 € pour la société [S1][S2] |
| Code de commerce R123-237 : sur le site, « RCS + ville du greffe », numéro unique d'identification, siège ; R123-238 : « SAS » et capital [S3]. | Bloc d'identité complet en pied de page. | Faible (contravention de 4e classe) |
| Belgique : un prestataire établi en France relève du droit français pour le domaine coordonné (directive 2000/31, art. 3). Exceptions : contrats de consommation, choix de la loi du contrat, licéité des e-mails publicitaires non sollicités [S4]. | Ajouter TVA intracommunautaire, pays desservis, loi applicable et tribunal compétent. Mentions propres au droit belge (numéro BCE) : non vérifiées, a priori sans objet sans établissement belge. | Faible à moyen |
| Loi du 4 août 1994, art. 2 et 4 : français obligatoire pour l'offre et toute publicité ; la version française doit être aussi lisible que la traduction. La loi ne dit pas quelle version fait foi [S5]. | Aucun contenu uniquement en anglais. Clause « la version française fait foi » dans les pages légales des deux langues. | Faible |

## 2. RGPD

| Sujet | Règle | À faire | Risque |
|---|---|---|---|
| Information | Responsable, finalités, base légale, destinataires, durées, droits, réclamation CNIL, transferts ; politique distincte des CGV, lien visible sur chaque page ; 1 500 € par information manquante [S2]. | Page « Confidentialité » et notice courte sous le formulaire. | Moyen |
| Base légale du formulaire | Le consentement n'est pas systématiquement requis [S2]. La prospection B2B peut reposer sur l'intérêt légitime si l'objet est lié à la profession, avec information et opposition simple [S29]. | Pas de case de consentement pour le rappel demandé (mesures précontractuelles ou intérêt légitime : qualification à valider). Aucune case pré-cochée. | Faible |
| Durée | Prospect non client : 3 ans à compter de la collecte ou du dernier contact émanant de lui [S7]. | L'écrire, puis purger la boîte de réception. | Moyen |
| Sous-traitants | Le DPA de Vercel ne couvre que les offres Pro et Enterprise [S11]. L'addendum de traitement de Google vise Cloud, Workspace et Cloud Identity [S14] : une boîte Gmail gratuite n'y figure pas (déduction). Meta : responsabilité conjointe pour la collecte par ses outils, information obligatoire [S15]. | Offre Vercel Pro ; boîte professionnelle sous contrat de sous-traitance ; paragraphe « Meta, responsable conjoint ». | Moyen à élevé (Gmail) |
| Transferts | Décision d'adéquation du 10 juillet 2023 en vigueur : transferts libres vers les entités certifiées [S8][S20]. Recours rejeté par le Tribunal le 3 septembre 2025 ; pourvoi C-703/25 P du 31 octobre 2025 toujours « pendant » au 17 novembre 2026 [S9][S10]. Vercel et Google se déclarent certifiés [S12][S13] ; le DPA Vercel prévoit les clauses contractuelles types [S11]. | Citer DPF et clauses types ; vérifier Meta sur la liste DPF ; mise à jour si la Cour annule. | Moyen |
| Registre | La dérogation « moins de 250 salariés » ne vaut pas pour les traitements non occasionnels (clients, prospects) [S6]. | Tenir un registre simple. | Faible |

## 3. Cookies et traceurs

| Règle CNIL | À faire | Source |
|---|---|---|
| Consentement avant tout dépôt ou lecture ; la poursuite de navigation ne vaut pas accord ; preuve à conserver | Scripts bloqués par défaut | [S16][S17] |
| « Tout refuser » au même niveau et avec le même aspect que « Tout accepter » ; retrait aussi simple que l'accord | Deux boutons équivalents ; lien « Gérer mes cookies » sur toutes les pages | [S18][S28] |
| Conservation du choix, accord ou refus : 6 mois, bonne pratique | Ne pas redemander avant 6 mois | [S18] |
| Mesure d'audience exemptée seulement si finalité strictement limitée, statistiques anonymes, sans recoupement ni réutilisation par le fournisseur ; traceur 13 mois, données 25 mois | GA4 standard : consentement (la CNIL ne nomme pas GA4 dans les pages lues ; déduction) | [S19] |
| Publicité personnalisée, réseaux sociaux, pixels invisibles : consentement ; le pixel relève de l'article 5(3) ePrivacy | Pixel Meta après accord uniquement | [S16][S26] |

- **Consent Mode v2.** En mode de base, aucune donnée ne part vers Google avant interaction avec le bandeau ; en mode avancé, les balises se chargent et envoient des mesures sans cookie même en cas de refus [S24]. Aucune position de la CNIL trouvée : retenir le mode de base.
- **API Conversions.** Meta traite les événements serveur comme ceux du Pixel [S25]. Aucune position de la CNIL lue : la soumettre au même consentement, sans y envoyer les champs du formulaire.
- **Polices.** Le tribunal régional de Munich a condamné un site pour transmission d'adresses IP via des polices chargées chez Google (20 janvier 2022) [S27]. Les auto-héberger.
- **Contrôles.** 38 sanctions simplifiées de juin à octobre 2026, dont une douzaine pour cookies déposés avant accord ou bandeaux incomplets [S21] ; 7 M€ le 22 octobre 2026 pour un traceur sans consentement [S22].
- **Réforme.** La proposition « Digital Omnibus » du 20 novembre 2025 (articles 88a et 88b) était encore discutée au Conseil le 4 juin 2026 [S50]. Droit inchangé.

Risque : élevé.

## 4. Prospection et rappel

| Cas | Règle | Source |
|---|---|---|
| France, B2B, téléphone et e-mail | Intérêt légitime si l'objet est lié à la profession ; information et opposition simple à chaque sollicitation ; adresses génériques hors champ | [S29][S34] |
| Belgique, B2B, e-mail | Consentement préalable (CDE XII.13), sauf client existant pour produits analogues, ou personne morale jointe à une adresse impersonnelle ; une adresse fonctionnelle peut rester une donnée personnelle | [S36][S38] |
| Belgique, téléphone | Opt-out : appels permis sauf opposition ou inscription sur la liste « Ne m'appelez plus », à consulter sous licence, qui couvre consommateurs et entreprises inscrits ; un accord explicite y déroge. Proposition d'opt-in rejetée en commission (rapport du 30 avril 2026) | [S36][S39][S40][S37] |
| France, particuliers | Consentement libre, spécifique, éclairé, univoque, révocable ; preuve à la charge du professionnel ; exception : contrat en cours. La demande nomme le professionnel et le tiers appelant, la nature des travaux, une durée d'un an au plus, le retrait ; preuve gardée 3 ans. Appels du lundi au vendredi, 10 h-13 h et 14 h-20 h, sauf accord pour une date et une heure précises | [S30][S31][S29] |
| Rénovation énergétique, adaptation du logement | Prospection téléphonique interdite hors contrat en cours. L'appel répondant à une demande d'information n'est pas une prospection si la demande est prouvée, l'appel passé sous 5 jours ouvrables et limité à l'objet demandé. Interdiction étendue aux messages, e-mails et réseaux sociaux depuis le 2 juillet 2025 (L223-8) | [S31][S29][S32][S51] |
| Sanctions | 75 000 € et 375 000 € ; le professionnel ayant tiré profit est présumé responsable ; le contrat conclu à la suite d'un démarchage illicite est nul | [S33][S30] |

Conséquences : présenter le rappel comme la réponse à une demande explicite et tracée ; nommer l'artisan destinataire dans chaque formulaire publicitaire [S35] ; borner « moins de 5 minutes » aux plages légales ; ne jamais écrire « 100 % conforme ». Risque : élevé, et il pèse aussi sur les artisans clients.

## 5. Publicité

- **Comparative.** Licite si elle n'est pas trompeuse, porte sur des services répondant au même besoin et compare objectivement des caractéristiques essentielles, pertinentes, vérifiables et représentatives ; ni dénigrement ni confusion ; preuve à fournir à bref délai [S43]. La directive 2006/114 protège aussi les professionnels et vaut en Belgique [S44]. Viser une catégorie (« plateformes qui revendent la même demande ») plutôt qu'une marque ; sinon, preuve datée pour chaque affirmation. Risque : moyen.
- **Trompeuse.** Allégations fausses ou de nature à induire en erreur sur la disponibilité, les caractéristiques essentielles ou la portée des engagements ; règles étendues aux professionnels [S41]. Peines : 2 ans et 300 000 €, jusqu'à 10 % du chiffre d'affaires ; 5 ans et 750 000 € en ligne [S42].

| Formulation | Condition |
|---|---|
| « Rendez-vous exclusifs, jamais revendus » | Clause contractuelle identique ; aucune réaffectation d'une demande |
| « Un seul artisan par métier et par secteur » | Définir métier et secteur (rayon ou codes postaux) ; registre interne |
| « Rappel en moins de 5 minutes » | Préciser plages et mode de mesure ; conserver les journaux d'appels |
| « Sans engagement » | Aucune durée minimale ; préavis et sommes restant dues indiqués |
| « Secteur encore libre » | Vrai au moment de l'affichage ; la fausse disponibilité limitée est trompeuse en toutes circonstances (L121-4, 7°) [S41] |

- **Avis.** L111-7-2 vise les avis de consommateurs : contrôle, date, motifs de rejet [S45]. Faux avis et avis présentés comme vérifiés sans l'être sont trompeurs (L121-4, 27° et 28°) [S41]. Plus tard : témoignages réels, datés, autorisés par écrit, preuve conservée.

Risque : élevé si l'exclusivité ou la rareté affichées ne sont pas tenues.

## 6. Accessibilité

La directive 2019/882 vise les services de commerce électronique fournis à un consommateur en vue d'un contrat de consommation et exonère les microentreprises de services (moins de 10 personnes, 2 M€ au plus) [S46]. France Num limite l'obligation aux PME de plus de 10 salariés et de plus de 2 M€ vendant en ligne à des consommateurs [S47]. Un site vitrine B2B d'une jeune société n'y est donc pas soumis ; Service-Public emploie toutefois une formule plus large [S2]. RGAA : non vérifié. Viser WCAG 2.1 AA par bonne pratique. Risque : faible.

## 7. Conditions contractuelles B2B

- Les CGV, si elles existent, sont communiquées sur support durable à tout professionnel qui les demande ; ni leur publication ni l'affichage des prix ne sont imposés ; pour un prix non déterminable à l'avance, méthode de calcul ou devis sur demande. Amende : 75 000 € pour une société [S48].
- L221-3 étend information précontractuelle et rétractation aux contrats conclus hors établissement avec un professionnel de cinq salariés au plus, hors de son activité principale ; le texte ne vise pas les contrats à distance [S49]. Une signature chez l'artisan déclenche ce régime.
- Sur le site : mentions légales, confidentialité, cookies, conditions d'utilisation courtes. CGV remises avant signature.

Risque : faible à moyen.

## 8. À faire valider par un professionnel du droit

1. Rôles RGPD de l'agence et de l'artisan (sous-traitant ou responsable conjoint) et texte de consentement des formulaires publicitaires.
2. Toiture ou façade avec isolation : champ exact de l'interdiction « économies d'énergie », et statut des publicités Meta au regard de L223-8 (prospection « sur un service de réseaux sociaux en ligne »).
3. Rappel hors plages légales ; appels vers la Belgique.
4. Clauses abusives B2B en droit belge et loi applicable (non vérifié).
5. Toute comparaison nommant une plateforme.
6. Distribution de flyers (non étudiée).

## Sources

Toutes consultées le 17 novembre 2026 ; la date entre parenthèses est celle de la source.

- [S1] Loi n° 2004-575 (LCEN), art. 1-1 et 1-2 (en vigueur depuis le 23 mai 2024) : https://www.legifrance.gouv.fr/loda/id/JORFTEXT000000801164/
- [S2] Service-Public Entreprendre, « Mentions obligatoires sur le site internet d'une entreprise » (vérifié le 13 octobre 2026) : https://entreprendre.service-public.gouv.fr/vosdroits/F37351
- [S3] Code de commerce, R123-237 (15 mai 2022) et R123-238 : https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000005634379/LEGISCTA000006178891/
- [S4] Directive 2000/31/CE, art. 3, art. 5 et annexe : https://eur-lex.europa.eu/legal-content/FR/TXT/HTML/?uri=CELEX:32000L0031
- [S5] Loi n° 94-665 du 4 août 1994, art. 2 et 4 : https://www.legifrance.gouv.fr/loda/id/LEGITEXT000005616341
- [S6] CNIL, registre des activités de traitement : https://www.cnil.fr/fr/RGDP-le-registre-des-activites-de-traitement
- [S7] CNIL, référentiel « gestion des activités commerciales » : https://www.cnil.fr/sites/cnil/files/atoms/files/referentiel_traitements-donnees-caractere-personnel_gestion-activites-commerciales.pdf
- [S8] CNIL, adéquation des États-Unis, questions-réponses (17 juillet 2024) : https://www.cnil.fr/fr/adequation-des-etats-unis-les-premieres-questions-reponses
- [S9] JOUE C/2025/6610, pourvoi C-703/25 P (22 décembre 2025) : https://eur-lex.europa.eu/legal-content/FR/TXT/HTML/?uri=OJ:C_202506610
- [S10] InfoCuria, affaire C-703/25 P, état « pendante », ordonnance du 4 juin 2026 : https://curia.europa.eu/juris/liste.jsf?language=fr&num=C-703/25%20P
- [S11] Vercel, Data Processing Addendum (mis à jour le 17 mars 2026) : https://vercel.com/legal/dpa
- [S12] Vercel, Privacy Policy, section Data Privacy Framework : https://vercel.com/legal/privacy-policy
- [S13] Google, cadres de transfert de données : https://policies.google.com/privacy/frameworks?hl=fr
- [S14] Google, Cloud Data Processing Addendum : https://cloud.google.com/terms/data-processing-addendum
- [S15] Meta, avenant relatif aux responsables du traitement : https://www.facebook.com/legal/controller_addendum
- [S16] CNIL, « Cookies et traceurs : que dit la loi ? » (29 septembre 2020) : https://www.cnil.fr/fr/cookies-et-autres-traceurs/regles/cookies/que-dit-la-loi
- [S17] CNIL, lignes directrices modificatives et recommandation (29 septembre 2020) : https://www.cnil.fr/fr/cookies-et-autres-traceurs/regles/cookies/lignes-directrices-modificatives-et-recommandation
- [S18] CNIL, questions-réponses cookies (questions 21, 37 à 39) : https://www.cnil.fr/fr/cookies-et-autres-traceurs/regles/cookies/FAQ
- [S19] CNIL, solutions de mesure d'audience (4 juillet 2025) : https://www.cnil.fr/fr/cookies-et-autres-traceurs/regles/cookies-solutions-pour-les-outils-de-mesure-daudience
- [S20] CNIL, mesure d'audience et transferts (15 novembre 2023) : https://www.cnil.fr/fr/google-analytics-et-transferts-de-donnees-comment-mettre-son-outil-de-mesure-daudience-en-conformite
- [S21] CNIL, 38 sanctions simplifiées (17 novembre 2026) : https://www.cnil.fr/fr/38-sanctions-simplifiees
- [S22] CNIL, sanction de 7 M€, traceur d'application (29 octobre 2026) : https://www.cnil.fr/fr/sanction-cookies-app-fnac
- [S24] Google, mode Consentement (mis à jour le 30 juillet 2026) : https://developers.google.com/tag-platform/security/concepts/consent-mode?hl=fr
- [S25] Meta, API Conversions (mis à jour le 28 septembre 2026) : https://developers.facebook.com/docs/marketing-api/conversions-api/
- [S26] CEPD, lignes directrices 2/2023, version 2.0 (7 octobre 2024) : https://www.edpb.europa.eu/system/files/2024-10/edpb_guidelines_202302_technical_scope_art_53_eprivacydirective_v2_en_0.pdf
- [S27] LG München I, 20 janvier 2022, 3 O 17493/20 : https://www.gesetze-bayern.de/Content/Document/Y-300-Z-GRURRS-B-2022-N-612
- [S28] Service-Public Entreprendre, « Gérer les cookies et autres traceurs » (vérifié le 13 octobre 2026) : https://entreprendre.service-public.gouv.fr/vosdroits/F31228
- [S29] CNIL, prospection commerciale par téléphone (contenu à jour du régime du 11 août 2026) : https://www.cnil.fr/fr/prospection-commerciale-par-telephone-hors-automate-dappel-quelles-sont-les-regles
- [S30] Code de la consommation, L223-1 à L223-7 (version du 11 août 2026) : https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069565/LEGISCTA000032221441/2026-08-11
- [S31] Décret n° 2026-662 du 23 juillet 2026 (JORF du 25 juillet 2026) : https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000054483939
- [S32] Loi n° 2025-594 du 30 juin 2025, art. 13 : https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000051824277
- [S33] Code de la consommation, L242-16 : https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000042155954
- [S34] CNIL, prospection par courrier électronique (10 juin 2026) : https://www.cnil.fr/fr/la-prospection-commerciale-par-courrier-electronique
- [S35] CNIL, transmission de données à des partenaires pour la prospection (10 juin 2026) : https://www.cnil.fr/fr/la-prospection-b-to-c-quelles-regles-pour-transmettre-des-donnees-des-partenaires
- [S36] APD, avis n° 02/2026 (12 janvier 2026) : https://www.autoriteprotectiondonnees.be/publications/avis-n0-02-2026.pdf
- [S37] Chambre des représentants, DOC 56 1081/004 (30 avril 2026) : https://www.lachambre.be/FLWB/PDF/56/1081/56K1081004.pdf
- [S38] APD, recommandation 01/2026 marketing direct, annexes 1 et 2 : https://www.autoriteprotectiondonnees.be/publications/recommandation-01-2025-relative-aux-traitements-de-donnees-a-caractere-personnel-dans-le-cadre-du-marketing-direct.pdf
- [S39] Do Not Call Me asbl : https://www.dncm.be/fr/
- [S40] SPF Économie, communiqué du 19 mars 2025 : https://news.economie.fgov.be/248054-assez-d-etre-demarche-par-telephone-reagissez/
- [S41] Code de la consommation, L121-2 à L121-5 : https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069565/LEGISCTA000032220953/
- [S42] Code de la consommation, L132-2 (12 mai 2024) et suivants : https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069565/LEGISCTA000032221097/
- [S43] Code de la consommation, L122-1 à L122-7 : https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069565/LEGISCTA000032221021/
- [S44] Directive 2006/114/CE, art. 1 et 4 : https://eur-lex.europa.eu/legal-content/FR/TXT/HTML/?uri=CELEX:32006L0114
- [S45] Code de la consommation, L111-7-2 : https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000049571119
- [S46] Directive (UE) 2019/882, art. 3 et 4 : https://eur-lex.europa.eu/legal-content/FR/TXT/HTML/?uri=CELEX:32019L0882
- [S47] France Num, accessibilité des sites de e-commerce (mis à jour le 17 décembre 2025) : https://www.francenum.gouv.fr/guides-et-conseils/developpement-commercial/site-e-commerce/accessibilite-des-sites-de-e-commerce
- [S48] Code de commerce, L441-1 : https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000038414469
- [S49] Code de la consommation, L221-3 : https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000032226882
- [S50] Conseil de l'UE, note 9773/1/26 REV 1 (4 juin 2026) : https://data.consilium.europa.eu/doc/document/ST-9773-2026-REV-1/en/pdf
- [S51] Code de la consommation, L223-8 (en vigueur depuis le 2 juillet 2025) : https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000051828335

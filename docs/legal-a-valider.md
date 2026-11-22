# Pages légales : ce qu'il reste à fournir, décider et faire valider

État au 18 novembre 2026. Les quatre pages (mentions légales, confidentialité, cookies, conditions du service) sont rédigées, relues par deux relecteurs indépendants (données personnelles, droit de la consommation) et en ligne sur la préversion. Ce document n'est pas un avis d'avocat : les points de la partie 3 doivent être validés par un professionnel avant la mise en ligne du domaine.

Les sources des pages sont dans `explorations/v8b/_build/legal/`. Les informations de la société se renseignent dans `explorations/v8b/_build/site.py`, variable `COMPANY`.

## 1. Informations à fournir (elles s'affichent « à compléter » en jaune)

| Information | Où elle apparaît |
|---|---|
| Numéro SIREN | Mentions légales |
| Ville du greffe (RCS) | Mentions légales |
| Montant du capital social | Mentions légales |
| Numéro de TVA intracommunautaire | Mentions légales |
| Directeur de la publication : une personne physique, en principe le président de la SAS | Mentions légales |
| Médiateur de la consommation : nom, adresse, site (voir la décision 2.4) | Conditions du service |

## 2. Décisions à prendre

1. **Horaires de rappel des particuliers.** Depuis le 11 août 2026, un appel à un particulier n'est permis que du lundi au vendredi, hors jours fériés, de 10 h à 13 h et de 14 h à 20 h, sauf s'il a demandé à être appelé à un moment précis. Le site promet un rappel de 8 h à 19 h. La case du formulaire dit donc maintenant « dès maintenant ou à la réouverture (lundi au vendredi, 8 h à 19 h) ». Deux options : garder ce texte et le faire valider, ou limiter les rappels aux plages légales et corriger la promesse.
2. **Règles d'appel à tenir en interne** (elles sont écrites dans les pages) : quatre essais au plus, dans les cinq jours ouvrables, jamais un jour férié, arrêt immédiat sur demande.
3. **Preuve à conserver 3 ans** pour chaque demande de particulier : date et heure, texte exact de la case et de la notice, numéro, page, journal des appels, accord à la transmission vers l'artisan nommé. La page promet un SMS qui confirme le nom de l'artisan et la date : il sert de preuve écrite.
4. **Médiateur.** L'obligation n'est pas certaine pour un service gratuit. Soit vous signez avec un médiateur référencé et son nom remplace la marque « à compléter », soit la phrase est remplacée par le recours au conciliateur de justice.
5. **Durées de conservation retenues** : artisans, 3 ans après leur dernier contact ; particuliers, 1 an au plus (durée de l'accord) ; preuve de l'accord, 3 ans ; journaux de l'hébergeur, 30 jours au plus. À confirmer, puis à appliquer (purge de la boîte de réception et du CRM).
6. **Ce que vous vérifiez chez un artisan partenaire** (immatriculation, décennale, RGE). La page dit aujourd'hui au particulier de vérifier lui-même. Si vous contrôlez, il faut l'écrire : c'est un argument.
7. **Prestataires.** La page nomme Vercel et décrit les autres par catégorie (messagerie, suivi des demandes, SMS). Donnez la liste réelle. Une boîte Gmail gratuite n'est pas couverte par un contrat de sous-traitance : passer à une messagerie professionnelle. L'offre Vercel doit être Pro pour que le contrat de sous-traitance s'applique.
8. **« Jamais revendu ».** Sur les pages particuliers, la formule a été remplacée par « transmis à un seul artisan, à personne d'autre », plus sûre si la facturation des artisans dépend des demandes ou des visites.

## 3. Points à faire valider par un avocat

1. Le rappel d'un particulier qui en fait la demande par formulaire, entre 8 h et 10 h et entre 13 h et 14 h (article L223-1 du Code de la consommation et décret du 23 juillet 2026).
2. **Travaux d'économies d'énergie** (isolation, et probablement fenêtres, isolation par l'extérieur, toiture isolée). Toute prospection téléphonique est interdite, sauf réponse à une demande d'information, dans les cinq jours ouvrables, limitée à cette demande. La prospection par SMS, messagerie, e-mail ou réseaux sociaux est interdite depuis le 2 juillet 2025 : le statut des annonces Meta pour l'isolation doit être tranché.
3. La qualification du service pour les particuliers (plateforme, obligations d'information, médiation).
4. Le contrat avec chaque artisan partenaire : visite et devis gratuits, aucune retransmission des coordonnées, information du particulier sur l'origine de ses données, suppression sur demande.
5. Les transferts vers les États-Unis : vérifier sur la liste officielle (dataprivacyframework.gov) que Vercel Inc., Google LLC et Meta Platforms, Inc. sont actives. La page écrit qu'elles « déclarent être certifiées ».
6. Si Bartier & Co a une assurance de responsabilité professionnelle : coordonnées de l'assureur à ajouter aux mentions légales.

## 4. Le jour où les balises de mesure et de publicité sont activées

- Renseigner les identifiants dans `site.py`, variable `TAGS` (GA4, Google Ads, Pixel Meta). Rien n'est chargé sans identifiant et sans accord du visiteur.
- Dans Google Analytics : conservation des données réglée sur 14 mois.
- Vérifier la liste des traceurs de la page Cookies avec les cookies réellement déposés.
- Accepter les conditions de responsabilité conjointe de Meta pour le Pixel.

## 5. Avant de brancher le domaine

- Compléter la partie 1 : le générateur signale à chaque construction les informations manquantes.
- Retirer la balise `noindex`, brancher l'envoi automatique des formulaires (fonction `api/lead.js` en ligne depuis le 22 novembre 2026 ; destination : le Google Sheet « Bartier & Co, demandes du site », par le script `_build/sheets/apps-script.gs`, à déployer une fois comme application Web puis adresse /exec à mettre dans LEAD_SHEET_URL sur Vercel), puis relire les quatre pages une dernière fois.

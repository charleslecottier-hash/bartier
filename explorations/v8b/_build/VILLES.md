# Pages « Devis travaux à <ville> » : fabrication et référencement

Une page par ville, pour les propriétaires qui préparent des travaux de toiture, façade, fenêtres, charpente ou isolation.
Chaque page dit ce qui est propre à la ville : règles d'urbanisme, ravalement, secteurs protégés, climat, risques, aides locales, guichets.
Tout est sourcé sur des pages officielles et daté.

## La chaîne

1. **Recherche** : l'agent `ville-chercheur` (`.claude/agents/ville-chercheur.md`) cherche les règles et les aides de la ville et écrit sa fiche dans `_build/villes_new/<slug>.py`.
2. **Contre-vérification** : l'agent `ville-verificateur` (`.claude/agents/ville-verificateur.md`) rouvre chaque source, corrige ou retire ce qui n'est pas prouvé. S'il ne reste pas assez de matière locale, il marque la fiche `DRAFT`.
3. **Contrôle automatique** : `python3 _build/villes_check.py [slug] [--net]` bloque une fiche trop mince, sans source, copiée d'une autre ville, ou qui promet ce que Bartier & Co ne peut pas tenir (présence locale, délai, avis).
4. **Publication** : `python3 _build/site.py` ne publie que les fiches qui passent le contrôle, portent la ligne `REVIEWED` (ajoutée par le vérificateur), ne sont pas `DRAFT` et dont la date `PUBLISH` éventuelle est passée. La page, sa carte, son image d'aperçu, sa ligne dans `llms.txt`, le sitemap, la liste par région et les liens des pages métier se mettent à jour seuls.

Pour ajouter des villes, dans Claude Code : « Lance ville-chercheur pour Angers et Nîmes, puis ville-verificateur sur les deux, puis reconstruis le site. »

Les six premières villes (Paris, Marseille, Lyon, Toulouse, Lille, Rouen) sont dans `villes_data.py` ; les suivantes, une par fichier, dans `villes_new/`.

## Le choix des villes

Priorité aux communes où la demande de travaux est la plus forte : les plus peuplées d'abord (ordre de `ORDER` dans `villes.py`), en privilégiant celles où les maisons et les logements anciens pèsent lourd, car toiture, façade et charpente concernent surtout les maisons.

- Vague 1, en ligne depuis le 21 novembre 2026 : Bordeaux, Nantes, Nice, Montpellier, Strasbourg, Rennes, Toulon, Reims, Le Havre, Saint-Étienne, Grenoble, Dijon.
- Vague 2, écrite et contre-vérifiée le 21 novembre 2026, programmée le 5 décembre 2026 (ligne `PUBLISH` dans chaque fiche) : Angers, Nîmes, Aix-en-Provence, Clermont-Ferrand, Le Mans, Brest, Tours, Amiens, Limoges, Perpignan, Metz, Orléans.
- Vague 3 : Caen, Nancy, Besançon, Mulhouse, Annecy, Avignon, Poitiers, La Rochelle, Pau, Bayonne, Dunkerque, Valence.

Ne pas descendre sous les villes d'environ 50 000 habitants avec ce modèle : en dessous, les règles et les aides locales publiées sont trop rares pour faire une page qui ne soit pas générique.

## SEO : ce qui est en place

- **Pas de pages satellites.** Google sanctionne les pages où seul le nom de la ville change (« doorway pages », « scaled content abuse »). Ici, chaque page a au moins 4 chiffres locaux sourcés, 5 règles locales, 10 paragraphes métier propres à la ville, ses démarches, ses aides et sa FAQ. Le contrôle mesure les passages communs avec les autres villes et bloque au-delà de 12 %.
- **Aucune promesse de présence locale** : la page dit que la mise en relation dépend de la commune, et qu'hors zone la demande n'est transmise à personne. Pas de fausse adresse, pas de faux avis.
- **Titre et description** propres à chaque ville : « Devis travaux à <ville> : toiture, façade, fenêtres, isolation », description de 140 à 160 caractères avec les points locaux les plus forts.
- **Maillage interne** :
  - chaque ville renvoie vers les 6 villes les plus proches, avec la distance, et vers la liste complète ;
  - la page « Devis travaux » liste toutes les villes par région, avec leur point fort, et une carte cliquable ;
  - chaque page métier renvoie vers sa section dans chaque ville (« Couvreur à Bordeaux ») ;
  - le blog renvoie vers les villes.
- **Données structurées** : `WebPage` (auteur, date de vérification `lastReviewed`, date de mise à jour), `Service` avec `areaServed` = la ville (liens Wikipedia et Wikidata, code Insee, coordonnées, département puis région), `FAQPage`, `BreadcrumbList`.
- **Technique** : URL courte `/devis-travaux/<ville>/`, canonique, sitemap avec date de dernière modification réelle, image d'aperçu par ville (titre et carte), pages statiques rapides.

## GEO : être cité par les moteurs de réponse (ChatGPT, Perplexity, Gemini, Copilot, AI Overviews)

- **Réponse directe en tête** : le bloc « Que faut-il savoir avant des travaux à <ville> ? » répond en 2 ou 3 phrases chiffrées qui se suffisent à elles-mêmes. C'est le passage le plus cité.
- **Intertitres en questions**, comme les gens les posent aux assistants, et une FAQ par ville.
- **Chiffres datés avec leur source** juste à côté (Insee 2022, Météo-France, guide des aides 2024) : les moteurs de réponse préfèrent citer ce qu'ils peuvent attribuer.
- **Entités sans ambiguïté** : Wikidata, code Insee, département, région dans les données structurées.
- **llms.txt** : une ligne par ville, avec ce qui la distingue (pas la même phrase répétée), et **llms-full.txt** avec le texte de toutes les pages.
- **robots.txt** ouvert aux robots des assistants (GPTBot, PerplexityBot, ClaudeBot, Google-Extended…).
- **IndexNow** : la clé est servie à la racine. `python3 _build/indexnow.py` signale les nouvelles pages à Bing (index utilisé par ChatGPT et Copilot) et à Yandex dès la mise en ligne.
- **Fraîcheur et auteur** : date de vérification affichée et dans les données structurées, page signée par Charles Le Cottier.

## Publier une vague programmée

Le jour venu (à partir du 5 décembre 2026 pour la vague 2) :

```bash
python3 _build/site.py          # les fiches dont la date PUBLISH est passée entrent dans le site
python3 _build/villes_check.py  # tout doit être « ok »
```

Puis mettre en ligne comme d'habitude, et lancer `python3 _build/indexnow.py`.

Pour voir le site tel qu'il sera à une date donnée, sans rien publier : `VILLES_DATE=2026-12-05 python3 _build/site.py` dans une copie du dossier. Pour publier une vague tout de suite, retirer les lignes `PUBLISH` des fiches concernées.

## À revoir en janvier 2027

- Toulon : les trois campagnes de ravalement aidé se terminent en 2026.
- Le Havre : l'aide au ravalement des façades en brique et l'aide aux éléments d'origine du centre Perret prennent fin le 31 décembre 2026.
- Saint-Étienne : le plan façades court jusqu'en 2026.
- Orléans : les primes BBC et biosourcées de la Métropole prennent fin le 31 décembre 2026 ; la modification n° 4 du PLU métropolitain sera peut-être approuvée.
- Metz : le calendrier des permanences CALM-Soliha est celui de 2026.
- Amiens : l'accompagnement Soliha et Apremis court « jusqu'en 2026 ».
- Rouen : vérifier le montant du chèque éco-énergie Normandie (la Région annonce 6 500 à 12 000 €).

## Rythme de publication et suivi

- **Par vagues de 10 à 15 villes**, espacées de deux semaines environ. Après chaque vague : soumettre le sitemap dans Google Search Console et Bing Webmaster Tools, lancer IndexNow.
- **Surveiller l'indexation** dans Search Console (rapport « Pages ») : si une vague reste en « Explorée, actuellement non indexée » après 4 à 6 semaines, renforcer ces pages (photo de la ville, chiffres en plus) avant d'en publier d'autres.
- **Suivre les requêtes par ville** (Search Console, filtre sur l'URL) et les demandes reçues par page : renforcer les villes qui convertissent.
- **Revérifier chaque fiche tous les 6 mois** avec `ville-verificateur`, et en janvier (les aides changent souvent au 1er janvier). La date de vérification se met à jour dans la fiche.

## À ne pas faire

- Générer des pages par quartier, par petite commune ou par combinaison « métier × ville » sans contenu propre : c'est exactement ce que Google classe en contenu de masse.
- Créer des fiches Google Business Profile dans des villes sans adresse réelle.
- Recopier une fiche d'une ville voisine en changeant le nom.

## Pistes pour aller plus loin

- **Photo de la ville** en tête du bandeau de chiffres, sous licence libre (Wikimedia Commons, avec crédit), comme pour les six premières villes.
- **Un chiffre DPE par ville** (part des logements classés F ou G) depuis l'Observatoire DPE de l'ADEME, en données ouvertes : un chiffre local fort et unique.
- **Liens externes locaux** : la page d'une ville peut être citée par l'Espace Conseil France Rénov' ou une association de propriétaires locale si elle leur est utile ; à demander une fois la page en ligne.

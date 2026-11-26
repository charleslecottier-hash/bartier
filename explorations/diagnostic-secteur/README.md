# Diagnostic secteur

Le diagnostic qu'on envoie à un artisan après sa demande sur bartierandco.com (bouton « Vérifier mon secteur et recevoir mon diagnostic »). Deux pages en PDF, puis 20 minutes au téléphone avec Martin pour le commenter.

Ce qu'il contient :

1. **Les maisons autour de son dépôt** : maisons habitées à l'année dans sa commune et dans le département, part construite avant 1991 (Insee).
2. **Ce que les propriétaires cherchent sur Google** : recherches par mois pour son métier (Planificateur de mots clés Google Ads).
3. **Qui fait déjà de la publicité près de chez lui** : annonces actives sur Facebook et Instagram (Bibliothèque publicitaire Meta).
4. **Sa fiche Google face aux 3 premières** : rang, note et nombre d'avis (Google).
5. **Ce qu'un budget peut lui apporter** : demandes, visites, chantiers signés et chiffre d'affaires pour 1 000, 2 000 et 3 000 € de publicité, avec son chantier moyen. Mêmes hypothèses que la section Tarifs du site.

Exemple : `sortie/Diagnostic secteur - Metropole Couverture.pdf` (couvreur à Amiens, données réelles relevées le 26/11/2026). Il porte la mention « Brouillon » parce que les recherches Google n'ont pas encore été relevées.

## En faire un (environ 15 minutes)

1. **La fiche.** Copiez `prospects/exemple-amiens-couverture.json` sous le nom de l'entreprise. Gardez seulement : `entreprise`, `fiche_google` (le nom exact de sa fiche Google), `metier` (`couverture`, `facade`, `menuiserie`, `charpente` ou `isolation`), `code_postal`, `rayon_km`, `chantier_moyen` (celui qu'il a donné dans le formulaire) et `"chantier_moyen_source": "déclaré"`. Le reste se remplit tout seul.
2. **Les recherches Google.** Dans Google Ads : Outils, puis Planificateur de mots clés, puis « Obtenir le volume de recherche et les prévisions ». Tapez par exemple « couvreur amiens », « toiture amiens », « réparation toiture », « couvreur ». Zone : sa commune et le rayon. Reportez le total mensuel et les 5 premières recherches :
   ```json
   "recherches_google": {"total_mois": 0, "mots_cles": [["couvreur amiens", 0]], "zone": "Amiens et 30 km autour", "releve_le": "2026-11-26"}
   ```
3. **Les publicités.** Sur [la Bibliothèque publicitaire Meta](https://www.facebook.com/ads/library/) : France, Toutes les publicités, statut Actives, puis cherchez « couvreur {ville} » et « toiture {ville} ». Notez jusqu'à 3 annonceurs du secteur dans `pubs` : la page, le titre de l'annonce, la date « Diffusion commencée le » et le lien. Une capture est facultative : connecté à Facebook, faites une capture de l'annonce, mettez-la dans `captures/` et indiquez son nom dans `capture`. Aucune annonce trouvée : laissez `pubs` vide, le PDF l'écrit.
4. **Le PDF.**
   ```bash
   python3 generer.py prospects/<fiche>.json
   ```
   Le script trouve la commune, relève l'Insee et les avis Google, les garde dans la fiche, puis crée `sortie/Diagnostic secteur - <entreprise>.pdf`. Ajoutez `--maj` pour relever à nouveau l'Insee et les avis.
5. **L'envoi.** Envoyez le PDF par e-mail et appelez l'artisan pour fixer les 20 minutes.

Outils nécessaires : Python 3 et Node avec Playwright, déjà présents dans les sessions Claude. Les avis Google passent par l'API Google Places : la clé est ajoutée automatiquement dans une session Claude. Ailleurs, mettez-la dans la variable `GOOGLE_PLACES_KEY`.

## Les règles

- **Aucun chiffre inventé.** Chaque donnée du PDF indique sa source et sa date. Tant que les recherches Google manquent, le PDF porte la mention « Brouillon » : ne l'envoyez pas dans cet état.
- **Le chantier moyen vient de l'artisan.** Sans lui, le script prend 5 000 € et l'écrit en clair dans le PDF (« valeur par défaut, à remplacer par le vôtre »).
- **Pas de prix barré.** Le diagnostic est offert. Afficher une « valeur » barrée qu'on ne facture jamais serait une pratique commerciale trompeuse.
- **Des estimations, pas des promesses.** La section 5 reprend mot pour mot les hypothèses du site.
- **Rester factuel sur les concurrents.** On montre ce qui est public (annonces, notes, adresses), sans commentaire sur eux.

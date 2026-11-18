# Passe « unslop » sur le site Bartier & Co

Nuit du 18 novembre 2026, relevé terminé à 08 h 15 (heure de la machine). Étapes 1 à 4 de la méthode : regarder, relever, décider, fixer la direction. **Aucun fichier du site n'a été modifié.** Les corrections ci-dessous sont à appliquer par l'orchestrateur.

Méthode : unslop, de Damir Sokolovsky (@heydamir), licence CC BY 4.0.

## Ce qui a été regardé

- Écrans réels dans Chromium (Playwright), aperçu local `http://localhost:8766` : accueil en 1440×900 (21 écrans) et en 390×844 (23 écrans), `/blog/` et `/blog/relance-devis-artisan/` aux deux tailles, `/metiers/couverture/`, `/google-ads/` et `/devis-travaux/` en 390×844. En plus : l'écran de chargement, la fenêtre WhatsApp (ouverture automatique, bulle sur téléphone, panneau ouvert), le bandeau cookies.
- Code : `_build/home.src.html`, les feuilles de style des pages construites, recherche d'emoji dans toutes les pages construites.
- Mesures dans le navigateur sur téléphone : débordements, tailles de texte, capitales, rayons, graisses, zones tactiles, position des soulignements.
- Captures : `/tmp/claude-0/-home-user/a8d0e8f0-7c4b-5881-8345-4247167e5eea/scratchpad/unslop-audit/` (avant/après de chaque correction dans le sous-dossier `ab/`, feuille testée dans `candidate.css`).

Limites à connaître :

- Le site a changé pendant le relevé. Vers 07 h 57 les photos de l'accueil sont repassées en couleur (sauf la photo d'ouverture), l'article de blog a reçu une photo d'en-tête, `extra.css` est passé de 2,9 à 8,4 Ko. Tous les sélecteurs et toutes les chaînes citées ont été revérifiés à 08 h 13 sur l'état courant.
- Safari sur iPhone n'a pas pu être testé (pas de WebKit ici).
- Les animations au défilement n'ont pas été jugées image par image : les captures sont faites avec « mouvement réduit », comme demandé. Les effets de survol sont relevés dans les feuilles de style, pas sur capture (mes trois captures de survol étaient mal cadrées).

## 1. Signes relevés

Un signe par ligne : l'écran, puis le sélecteur ou le texte exact.

### Surfaces et couleur

- Accueil, simulateur : halo blanc en dégradé radial dans le panneau bleu, `.ca-out::before`.
- Accueil, simulateur : ombre colorée sous la poignée des curseurs, `.calc input[type=range]::-webkit-slider-thumb` (`0 6px 14px -4px rgba(45,91,227,.6)`).
- `/google-ads/` et `/meta-ads/` : halo bleu en dégradé radial derrière le téléphone, `.mk::before`.
- `/devis-travaux/` (téléphone) : ombre bleue sous le bouton collé en bas, `.pf-sticky` (`rgba(45,91,227,.6)`).
- Accueil, formules : pastille « Recommandé » en vert citron `#c6f14d`, hors palette, `.plan-tag` (jeton `--spark`). Même vert sur les coches du bloc contact, `.dq-checks li::before`, et sur `.ct-form.is-sent .ct-note`.
- Toutes les pages : vert WhatsApp `#25D366` à six endroits. Icône `.wa-ico`, point `.wa-dot` avec anneau lumineux (`box-shadow:0 0 0 3px …`), `.wa-av::after`, bouton `.wa-btn.is-wa`, et surtout le grand bouton vert `.dq-wa` « Écrire à Martin sur WhatsApp » dans le bloc contact, qui concurrence le bleu d'accent.
- Toutes les pages : le gris `--muted` (`#87939c`) sert de couleur de texte en petit corps et n'atteint que 3,1:1 sur blanc, 2,75:1 sur le gris `--paper`. Exemples : `.season-when`, `.rng-mm`, `.wa-k`, `.mk-tag`, `.ph-steps`, et des paragraphes entiers sur `/devis-travaux/` (`.pf-time p`, `.pf-trade p`, `.pf-src`, `.pf-consent`).
- Accueil : grandes ombres portées sous deux cartes, `.ca-box` (`0 30px 60px -36px`) et `.dq` (`0 30px 70px -30px rgba(0,0,0,.6)`). Neutres, mais plus fortes que le reste de l'interface, qui vit de filets fins.
- Rien d'autre à signaler : pas de dégradé de teinte, pas de texte en dégradé, pas de carte en verre. Le bleu `#2D5BE3` passe à 5,65:1 sur blanc.

### Typographie

- `/devis-travaux/`, frise « Votre devis, étape par étape » : étiquettes en capitales espacées, `.pf-t` (« MAINTENANT », « DANS 5 MINUTES », « PENDANT L'APPEL », « AVANT LA VISITE », « LE JOUR J »).
- `/metiers/couverture/` (et les autres pages métiers), annonces d'exemple : capitales espacées en bleu, `.ad-angle` (« APRÈS LES INTEMPÉRIES », « TOITURE DE PLUS DE QUINZE ANS », « RÉNOVATION COMPLÈTE »).
- Règle dormante dans la feuille de l'accueil : `.season dt{text-transform:uppercase;letter-spacing:.06em}`. Elle ne s'applique à rien aujourd'hui.
- Dans les maquettes de téléphone : `.lp-kick` et `.mk-cta small` en capitales. Tolérable, c'est une imitation d'interface tierce.
- Graisse 700 par défaut sur `strong` et `b`, alors que les deux polices s'arrêtent à 600 : `.vc-by strong` (« Fini », six fois), `figcaption strong` (« Charles Le Cottier »), `.wa-head b`, les `b` des articles. Graisses 700 et 800 dans les maquettes.
- Trop de corps : 32 tailles de texte différentes calculées sur l'accueil en 390 px, 31 sur `/meta-ads/`, 32 sur `/google-ads/` (15 à 18 sur les autres pages).
- Formats de nombres mélangés sur l'accueil pour une même durée : « Rappel en 5 minutes » (titre), « en moins de cinq minutes » (texte, deux fois), « Rappel en 5 min » (étiquette et formules), « 5 minutes maximum pour rappeler ». Idem « Un appel de 15 minutes » et « Vous l'avez en quinze minutes ».
- Textes sous 11 px dans les maquettes sur téléphone : `.av` 9,5 px (« TM »), `.cl-b small` 9,6 px (« Refuser », « Accepter »), `.ad-link small` 10,5 px.
- Interlettrage négatif sur petit texte : `.ftr-contact a` (−.01em à 1,05rem), `.lp-logo` (11 px). Négligeable sur `.btn` (−.005em).
- Points finaux sur des titres courts, sans règle : « Complet. », « Six engagements. Écrits. », « Née sur le terrain. », « Plus de chantiers, moins de soirées au téléphone. », mais « Tout, du clic au devis », « Faites le calcul », « Le blog » sans point. C'est le ton du slogan, donc à garder, mais il faut choisir.
- Pas d'italique d'emphase, pas de titre en 800 : rien à signaler.

### Icônes

- Emoji dans la page construite `/meta-ads/` : « 👍❤️ 48 » dans l'annonce d'exemple (`p.ad-re`, source `_build/anim.py` ligne 93). Aucun autre emoji dans les pages construites.
- Caractères utilisés comme icônes à la place d'un tracé : « × » pour fermer (`.wa-x`, `.wa-tip-x`), « ✕ » dans la barre de navigateur des maquettes (`.br-x`), « → » ajouté en CSS (`.season-do::before`, `.wa-q::after`, `.sector-name a::after`), « ← Retour » (`.dq-back`).
- Accueil, services : un « + » dessiné devant chaque étiquette, `.svc-points li::before`. Il ressemble à une commande « ajouter » ou « déplier » alors que rien n'est cliquable.
- Pictogrammes WhatsApp et téléphone pleins, équerre des boutons en trait de 1,4 : deux familles, sans gêne visible.

### Espacements

- **Téléphone, toutes les pages** : le soulignement des liens `.link` flotte 13 à 25 px sous le texte (« Voir comment ça marche », « Voir l'équipe », « Tout lire », « Nous écrire », « Écrivez-nous », les liens de sources et « Tout sur toiture » de `/devis-travaux/`). Cause : la règle mobile `.link{min-height:44px;display:inline-flex}` laisse le trait au bas de la zone de 44 px.
- **Téléphone, accueil, simulateur** : « 12 000 € » sort de 33 px de sa carte, `.rng-h output` (la boîte fait 97 px, le texte 130 px).
- Ordinateur, accueil, formules : la carte « Croissance » est décalée de 4 px vers le bas par rapport aux deux autres (`.plan-top` 36 px contre 32 px, à cause de la pastille).
- Ordinateur, accueil, services : les étiquettes `.svc-points li` sont étirées à 106 px de haut (des tuiles grises presque carrées avec un texte minuscule), alors qu'elles font 32 px sur téléphone.
- Ordinateur, `/blog/` : l'en-tête n'occupe que la moitié gauche, le titre casse sur trois lignes et il reste environ 160 px de vide sous le bouton, `.pg-top` et `.pg-text`.
- Téléphone, article : tableau « Le calendrier » à trois colonnes de 110 px, un ou deux mots par ligne (« Répondre / aux / questions / avant qu'il / compare »), `.prose table`.
- Téléphone : le bouton rond WhatsApp recouvre du texte à droite (« Nous trouvons les clients. », les étiquettes), `.wa-fab`. Sur `/devis-travaux/` il voisine avec le bouton collé `.pf-sticky`.
- Valeurs hors grille de 4 px, peu visibles à l'œil : `.ca-in{gap:34px}`, `.rng-h{margin:0 0 14px}`, `.vc-track{gap:14px}`, `.rule-item{padding:14px …}`, `.ftr-base{padding:18px …}`, `.pf-time li{padding-top:22px}`, `.pf-trades{gap:22px 12px}` puis `30px 14px`, `.pf-sticky{right:78px;padding:6px 18px}`, et dans `extra.css` : `row-gap:30px`, `margin-top:22px`, `min-height:34px`.
- Zones tactiles courtes sur téléphone : fil d'Ariane `.crumbs a` (20 px de haut), `.pf-tl` (24 px).

### Textes

- Accueil, formules : « Un prix clair, sur appel », puis trois fois « Sur devis » en très grand, puis trois fois « sur appel » dessous. Un tableau de prix sans prix.
- Accueil, bloc contact : « Quatre questions, une minute. » juste au-dessus de « Étape 1 sur 5 ». Le formulaire a cinq écrans.
- Titres de poste en anglais sur un site français : « Head of Sales », « Head of Performance », jusque dans le bouton flottant « Parler à Martin, Head of Sales ».
- Pastille « Recommandé » sur une formule sans prix, `.plan-tag`.
- Maquette Meta : « 48 » réactions, « 12 commentaires · 3 partages ». Chiffres inventés, même sous l'étiquette « Exemple ».
- Maquettes : entreprise fictive « Toitures Martin », adresse « toitures-martin.fr ». Non vérifié : ce nom de domaine peut appartenir à une vraie entreprise.
- Rien à signaler pour le reste : pas de point d'exclamation, pas de mots creux, pas de faux avis ni de faux logos.

### Composants

- Accueil : trois cartes de formules de même largeur et de même structure, `.plan`.
- Accueil : six cartes identiques « Fini / Avec Bartier & Co », `.vc-card`. Leur pied `.vc-by` a la forme d'une signature de témoignage.
- `/google-ads/`, `/meta-ads/` : étapes en pastilles complètes sous le téléphone, `.ph-steps li` (`border-radius:99px`), dans une marque au rayon de 2 px.
- Toutes les pages : bouton flottant en pilule, `.wa-fab` (`border-radius:999px`), bulles arrondies `.wa-bubble` (`2px 12px 12px 12px`) et `.wa-tip` (`14px 14px 4px 14px`), pastille ronde « MB ».
- Pages métiers : le bouton gris « Demander une visite », `p.ad-cta`, hérite par accident du style de la maquette Facebook (`.ad-cta` défini deux fois) : rayon 6 px, gris `#e2e5e9` hors palette, graisse 600. Et il a l'air cliquable sans l'être.
- Accueil, simulateur : pistes de curseur au rayon 6 px et poignée ronde, `.calc input[type=range]`.
- `/devis-travaux/` : puces rondes sur la frise, `.pf-time li::before`, alors que l'accueil utilise un repère carré, `.step::before`.
- Barre de progression du formulaire au rayon 4 px, `.dq-bar`.

### Page d'accueil et premier écran

- Rien à reprocher au premier écran : composition asymétrique, un bouton principal et un lien, pas de badge, pas de fond décoratif. « Complet. » ne conviendrait pas à un autre produit.
- En-tête : sept liens tous soulignés, une ligne de description et deux boutons (« Appeler Martin », « Mon secteur »). C'est chargé pour une navigation.
- `/blog/` et articles : premier écran à moitié vide sur ordinateur (voir Espacements).

### Visuels

- Portraits absents : deux grands cadres gris avec les initiales « CL » et « MB », `figure.person-photo.ph-wait` (accueil et `/qui-sommes-nous/`). C'est le signe « cadre vide étiqueté », et le plus visible de la page.
- Photos de banque d'images qui ne viennent pas du monde du produit : toit en bardeaux bitumés et pavillons américains (photo d'ouverture, « Rendez-vous agenda », vue aérienne de « Suivi et flyers »), dalle de gros œuvre avec une équipe en gilets (« Une agence née sur le terrain »), employée souriante devant un iMac (« Rappel en 5 minutes »), charpente à l'américaine, maison en bardage blanc.
- Texte incrusté dans des images : tableau de bord avec faux chiffres sur l'ordinateur portable (« Google Ads locales »), formulaires en anglais (« What goals? », « Which behaviour? ») sur la vignette de l'article « Relance de devis ».
- Vignettes du blog : une texture de tuiles, des mains sur un téléphone, une pile de formulaires. Aucune ne dit de quoi parle l'article. C'est la remarque « pas assez pro ».
- Image et texte qui ne correspondent pas : la photo « isolation » montre une maison blanche ; son texte alternatif dit « Isolation d'un mur par l'extérieur » sur l'accueil et « Isolation de combles en laine minérale » sur `/devis-travaux/`.
- Une photo par section sur l'accueil (cinq services, un collage de cinq, trois vignettes) : aucune ne domine.
- Noir et blanc restant, par filtre CSS : `.pf-trade img` (cinq vignettes de `/devis-travaux/`), `.pg-photo img` (photo d'en-tête des pages métiers), `.person-photo img`. L'accueil est en couleur depuis 07 h 57, sauf la photo d'ouverture.
- Bon point à garder : les téléphones animés de `/google-ads/` et `/meta-ads/` sont de vrais aperçus du produit, construits en code.

### Mouvement

- Écran de chargement, `#ld` : un compteur de 0 à 100 % et une barre, réglés sur une durée fixe (1,3 s sur ordinateur, 0,9 s sur téléphone). Ce pourcentage ne mesure rien.
- Fenêtre WhatsApp : sur ordinateur le panneau complet s'ouvre tout seul après 4,5 s et recouvre la photo d'ouverture et le bloc « Le résultat ». Sur téléphone une bulle apparaît après 7 s (`@keyframes waTip`, avec une deuxième courbe, `cubic-bezier(.2,.8,.2,1)`).
- Survols qui soulèvent : `.wa-fab:hover{transform:translateY(-2px)}`, `.dq-tile:hover span{transform:translateY(-1px)}`.
- Survols lents : remplissage des boutons `.btn` en 0,55 s, soulignement `.link:hover` en 0,7 s, couleurs en 0,4 à 0,5 s. La courbe unique `--ease` est une bonne chose.
- Propriétés de mise en page animées : `.fq::details-content{transition:block-size .5s}`, `.dq-bar i{transition:width .5s}`, `.ph-tap{transition:left .55s,top .55s}`.
- Non jugé : les entrées au défilement (`data-rise`, `data-split`, sections épinglées), faute de captures en mouvement.

### Air de gabarit

- Prix du gabarit d'origine encore dans le code de la page, invisibles à l'écran mais lisibles par n'importe qui : `data-monthly="390" data-yearly="351"`, `data-monthly="890" data-yearly="801"`, `data-monthly="1,690" data-yearly="1,521"` (`_build/home.src.html`, lignes 542, 549, 556). Le brief interdit tout prix.
- Commentaire « Made with 8B AI Website Builder https://8b.com/ from a single prompt » en première et en dernière ligne de chaque page.
- La section formules garde la forme d'un tableau de prix d'abonnement (trois colonnes, une pastille, un grand chiffre) alors qu'il n'y a pas de prix.
- Les cartes « Fini » gardent la forme d'un carrousel de témoignages.
- Fenêtre de discussion flottante, écran de chargement à pourcentage, cadres à initiales : trois éléments que l'on retrouve tels quels sur beaucoup de sites.

## 2. Verdict

**Léger.** Le site est dessiné : une grille, deux polices, une encre, un accent, un rayon, et une feuille de style tenue ; il reste une vingtaine de signes, concentrés sur le téléphone (soulignements flottants, montant qui déborde), sur les restes du gabarit (prix cachés, vert citron, cadres à initiales, fenêtre WhatsApp, chargement) et sur les photos. On reste donc en mode finition : on garde palette, polices, mise en page et marque, on corrige ce que le relevé a trouvé, et les idées plus larges vont en suggestions.

## 3. Direction

Tirée de la marque et du produit existants, sans rien inventer.

- **Produit.** Bartier & Co remplit l'agenda des artisans du bâtiment à gros chantiers : annonces locales, rappel de chaque demande en 5 minutes, visite fixée, un seul artisan par métier et par secteur.
- **Caractère.** Droit, carré, de parole.
- **Monde.** Le plan de chantier et le carnet de rendez-vous : papier blanc, encre bleu nuit, traits de construction fins, bleu de traçage.
- **Moments.** L'agenda de la semaine qui se remplit, construit en code avec des données d'exemple ; et une vraie photo de chantier français par écran, en couleur naturelle, la photo d'ouverture restant seule en noir et blanc.
- **Signature.** L'équerre : le petit angle droit déjà présent sur les boutons, avec le repère carré bleu des étapes. Partout où quelque chose est fixé, et nulle part ailleurs : ni rond, ni pastille.

L'étape 4 de la méthode demande de s'arrêter ici et d'attendre l'accord sur la direction avant de modifier quoi que ce soit.

## 4. Corrections

Vingt corrections, les plus visibles d'abord. Le CSS est à **ajouter à la fin de** `_build/extra.css`. Attention : cette feuille est injectée avant la feuille propre à chaque page (`style#bc-css` précède le bloc de la page et `#pf-css`), donc les sélecteurs ci-dessous ont exprès une spécificité plus forte que les règles qu'ils corrigent. Ne pas les simplifier.

Tout le CSS a été testé en l'ajoutant à `style#bc-css` dans le navigateur sur dix pages : chaque sélecteur existe dans les pages construites, aucune page ne déborde en 390 px. Les remplacements de texte n'ont pas été appliqués ; chaque chaîne « actuelle » a été retrouvée telle quelle dans le fichier à 08 h 13, avec le nombre d'occurrences indiqué.

### 1. Téléphone, toutes les pages : soulignements qui flottent

Le trait des liens est 13 à 25 px sous le texte. Après correction il est sous le texte, la zone tactile de 44 px reste. Vérifié sur 9 pages : écart de 5 px au plus.

```css
@media (max-width:760px){
  .link{background-position:0 calc(50% + .78em)}
  .link.pf-more{display:inline-flex;align-self:flex-start}
  .pf-src .link{display:inline;min-height:0;background-position:0 100%}
  .link.pf-pick{min-height:0;padding:12px 0 .2em;background-position:0 100%}
}
```

### 2. Téléphone, accueil : « 12 000 € » sort du simulateur

```css
@media (max-width:760px){
  .rng-h output{flex:none}
  .rng-h label{min-width:0}
}
```

### 3. Accueil : les prix du gabarit sont encore dans le code

Invisible à l'écran, mais contraire au brief (« pas de prix »). Dans `_build/home.src.html` :

| Ligne | Chaîne actuelle | Nouvelle chaîne |
|---|---|---|
| 542 | `<span class="plan-num" data-monthly="390" data-yearly="351">devis</span>` | `<span class="plan-num">devis</span>` |
| 549 | `<span class="plan-num" data-monthly="890" data-yearly="801">devis</span>` | `<span class="plan-num">devis</span>` |
| 556 | `<span class="plan-num" data-monthly="1,690" data-yearly="1,521">devis</span>` | `<span class="plan-num">devis</span>` |
| 542, 549, 556 (3 fois) | `<span class="plan-per" data-monthly="sur appel" data-yearly="sur appel, sans engagement">sur appel</span>` | `<span class="plan-per">sur appel</span>` |

Aucun script ne lit ces attributs (vérifié dans le fichier).

### 4. Accueil et `/qui-sommes-nous/` : cadres vides « CL » et « MB »

En attendant les portraits, un monogramme compact au lieu de deux grands rectangles gris. La règle ne vise que `.ph-wait` : elle cesse de s'appliquer dès qu'une vraie photo remplace le cadre.

```css
.person-photo.ph-wait{aspect-ratio:auto;width:72px;height:72px;margin-bottom:1rem}
.person-photo.ph-wait span{font-size:1.5rem;letter-spacing:-.02em}
```

### 5. Ordinateur : la fenêtre WhatsApp s'ouvre toute seule sur la photo d'ouverture

Après 4,5 s le panneau complet recouvre le premier écran. Montrer la petite bulle, comme sur téléphone (testé : la bulle s'affiche bien sur ordinateur). Dans `_build/home.src.html`, ligne 815 :

- Actuel : `if(window.innerWidth<761)w.classList.add('is-tip');else set(true);`
- Nouveau : `w.classList.add('is-tip');`

### 6. Accueil : vert citron et formules décalées

Le vert `#c6f14d` est une deuxième couleur d'accent. Il devient la teinte claire de la marque (`--tint`), partout où il sert. Les trois cartes reprennent la même ligne.

```css
:root{--spark:var(--tint)}
.plan-top{min-height:36px}
```

### 7. Toutes les pages : petit texte gris trop pâle

`--muted` passe de 3,1:1 à 5,6:1 sur blanc (4,9:1 sur le gris `--paper`), valeurs mesurées dans le navigateur, en restant un mélange de l'encre et du blanc. Les grands chiffres « 48, 5, 1, 0 » gardent un gris clair (3,4:1, suffisant pour un corps de cette taille).

```css
:root{--muted:color-mix(in oklab,var(--ink) 60%,var(--bg))}
.fact-num{color:color-mix(in oklab,var(--ink) 45%,var(--bg))}
```

### 8. Ordinateur, accueil : étiquettes de services étirées en tuiles

```css
.svc-points{align-items:flex-end}
```

Elles reprennent leur hauteur et se calent sur le bas de la photo.

### 9. Photos : ce qui reste en noir et blanc

Les cinq vignettes de `/devis-travaux/` et la photo d'en-tête des pages métiers sont encore grisées par un filtre CSS, alors que l'accueil est en couleur. Règle proposée : seule la photo d'ouverture de l'accueil reste en noir et blanc.

```css
.pg-photo.frame img{filter:none}
.pf-trades .pf-trade img{filter:none}
```

À coordonner avec la personne qui s'occupe des photos : `extra.css` contient déjà `.pg-photo.is-color img{filter:none}`. Si c'est ce mécanisme qui est retenu, ne garder que la deuxième ligne.

### 10. `/devis-travaux/` : capitales, puces rondes, ombre bleue

```css
.pf-time .pf-t{text-transform:none;letter-spacing:0;font-weight:500}
ol.pf-time li::before{border-radius:var(--r)}
a.pf-sticky{box-shadow:0 14px 30px -14px rgba(10,20,36,.55)}
```

« MAINTENANT » devient « Maintenant », la puce devient le repère carré de l'accueil, l'ombre du bouton collé devient neutre.

### 11. Pages métiers : annonces d'exemple

```css
.ad-card .ad-angle{text-transform:none;letter-spacing:0}
.ad-card .ad-cta{padding:.55em .8em;border-radius:var(--r);background:var(--paper);font-size:.85rem;font-weight:400}
```

### 12. `/google-ads/` et `/meta-ads/` : halo et pastilles autour du téléphone

```css
.pg-photo.mk::before{background:none}
.pg-photo .ph-steps li{border-radius:var(--r)}
```

### 13. Accueil, simulateur : halo, ombre colorée, pistes arrondies

Une règle par pseudo-élément, sinon les navigateurs rejettent la liste entière.

```css
.ca-out::before{display:none}
.calc input[type=range]::-webkit-slider-thumb{box-shadow:0 0 0 1px var(--accent)}
.calc input[type=range]::-webkit-slider-runnable-track{border-radius:var(--r)}
.calc input[type=range]::-moz-range-track{border-radius:var(--r)}
.calc input[type=range]::-moz-range-progress{border-radius:var(--r)}
```

### 14. Bouton et bulle WhatsApp au style de la marque

Sur ordinateur le bouton prend le rayon de 2 px des boutons du site. Sur téléphone le rond reste (c'est l'usage). Plus d'anneau lumineux ni de saut au survol.

```css
@media (min-width:761px){
  .wa-fab{border-radius:var(--r)}
  .wa-fab .wa-ico{border-radius:var(--r)}
}
.wa-dot{box-shadow:none}
.wa-fab:hover{transform:none}
.wa-tip{border-radius:var(--r)}
.wa-bubble{border-radius:var(--r)}
```

### 15. Téléphone, articles : tableaux trop serrés

Gain modeste mais net (quatre lignes au lieu de cinq par case). Vaut aussi pour les tableaux des pages légales.

```css
@media (max-width:760px){
  .prose table{font-size:.9rem}
  .prose th,.prose td{min-width:0;padding:.7rem .6rem}
  .prose th:first-child,.prose td:first-child{min-width:5.5em}
}
```

### 16. Ordinateur, `/blog/` : titre sur une demi-page

Quand l'en-tête n'a pas de photo, le texte prend trois colonnes : le titre tient sur deux lignes.

```css
@media (min-width:761px){
  .pg-grid .pg-text:only-child{grid-column:1 / 4}
}
```

Ne touche aujourd'hui que `/blog/` : les articles ont reçu une photo pendant la nuit.

### 17. Accueil : un seul format pour les durées, et le bon nombre d'étapes

Dans `_build/home.src.html` (une occurrence chacune) :

| Ligne | Chaîne actuelle | Nouvelle chaîne |
|---|---|---|
| 364 | `en moins de cinq minutes, en semaine de 8 h à 19 h.` | `en moins de 5 minutes, en semaine de 8 h à 19 h.` |
| 416 | `Chaque demande est rappelée en moins de cinq minutes, vérifiée` | `Chaque demande est rappelée en moins de 5 minutes, vérifiée` |
| 536 | `Vous l’avez en quinze minutes, avant toute décision.` | `Vous l’avez en 15 minutes, avant toute décision.` |
| 572 | `pendant l’appel de quinze minutes, avant toute décision.` | `pendant l’appel de 15 minutes, avant toute décision.` |
| 596 | `Quatre questions, une minute. Martin vous répond sous un jour ouvré.` | `Cinq étapes, une minute. Martin vous répond sous un jour ouvré.` |

La dernière ligne est à confirmer avec la personne qui reprend le formulaire : il compte aujourd'hui cinq écrans (« Étape 1 sur 5 »). Les deux descriptions pour les moteurs (lignes 8 et 198) disent aussi « cinq minutes » ; elles peuvent rester.

### 18. `/meta-ads/` : emoji et faux compteurs dans l'annonce d'exemple

Dans `_build/anim.py`, ligne 93 :

- Actuel : `<p class="ad-re"><span>👍❤️ 48</span><span>12 commentaires · 3 partages</span></p>`
- Nouveau : `<p class="ad-re"></p>`

Le filet de séparation reste. Fichier hors de mon périmètre : à faire par qui en a la charge.

### 19. Graisses et fil d'Ariane

```css
strong,b{font-weight:600}
@media (max-width:760px){
  .crumbs a{display:inline-flex;align-items:center;min-height:40px}
  .crumbs{align-items:center;row-gap:0}
}
```

### 20. Commentaire du générateur dans chaque page

Dans `_build/home.src.html`, lignes 1 et 821 :

- Actuel : `<!-- Made with 8B AI Website Builder https://8b.com/ from a single prompt -->`
- Nouveau : rien (supprimer les deux lignes)

Fait manquant : je ne sais pas si les conditions de 8B imposent cette mention. À vérifier avant de la retirer.

## 5. Suggestions

À ne pas appliquer sans le propriétaire.

### Les photos

Le problème n'est pas la couleur mais le sujet : presque toutes viennent d'un monde américain ou de bureau. Un filtre commun a été essayé (`saturate(.72) contrast(1.05)`) : il ne change presque rien, je ne le propose pas.

| Emplacement | Photo actuelle | Par quoi la remplacer |
|---|---|---|
| Accueil, ouverture | Couvreur sur bardeaux bitumés, pavillon américain | Un couvreur sur tuiles, ardoise ou zinc, sur une maison française. Peut rester en noir et blanc |
| « Une agence née sur le terrain » | Dalle de gros œuvre, équipe en gilets | Deux ou trois artisans sur l'échafaudage d'une maison |
| « Annonces Meta locales » | Mains et téléphone, manche noire | L'annonce telle que la voit le propriétaire : l'aperçu en code de `/meta-ads/`, en version fixe |
| « Rappel en 5 minutes » | Employée souriante devant un iMac | Une vraie photo de Martin ou de l'équipe au téléphone, ou une fiche d'appel en code (« Demande reçue 14 h 02, rappelée 14 h 05 », marquée Exemple) |
| « Rendez-vous agenda » | Homme à tablette devant une maison américaine et un SUV | L'agenda de la semaine en code (voir plus bas) |
| « Google Ads locales » | Ordinateur avec un tableau de bord aux faux chiffres | Le résultat de recherche en code de `/google-ads/`, en version fixe |
| « Suivi et flyers » | Vue aérienne d'un lotissement américain | Une photo du vrai flyer dans une boîte aux lettres, ou une vue d'une rue pavillonnaire française |
| Collage « Sur le terrain » | Charpente et bardage à l'américaine ; la photo « isolation » montre une façade | Vos vraies photos de chantiers dès qu'il y en a ; d'ici là, réduire le collage à trois images justes et corriger le texte alternatif de la photo « isolation » |
| Blog, trois vignettes | Tuiles en gros plan, mains sur un téléphone, formulaires en anglais | Plus de photo du tout : une couverture dessinée par article (voir plus bas) |

### Des couvertures de blog dessinées en code

C'est la réponse à « pas assez pro » qui ne dépend d'aucune banque d'images. Chaque article reçoit un petit schéma dans la grille du site, avec l'encre, le bleu et le repère carré :

- « Relance de devis » : une frise de quatre repères carrés, « Jour de l'envoi », « Quelques jours après », « Une semaine plus tard », « Deux à trois semaines plus tard » (ce sont les lignes du tableau de l'article).
- « Lead partagé, lead exclusif, rendez-vous qualifié » : une demande et cinq traits qui partent vers cinq carrés, à côté d'une demande et un seul trait.
- « Google Ads ou Meta Ads » : deux colonnes, « Ils cherchent déjà » et « Ils n'ont pas encore cherché » (mots de la page `/google-ads/`).

Esquisse de la première, à placer dans `figure.post-photo` :

```html
<figure class="post-photo frame cover" aria-hidden="true">
  <ol class="cover-line"><li>Jour de l’envoi</li><li>Quelques jours après</li><li>Une semaine plus tard</li><li>Deux à trois semaines plus tard</li></ol>
</figure>
```

```css
.cover{display:grid;align-items:center;padding:var(--cell);background:var(--paper)}
.cover-line{display:grid;gap:12px;margin:0;padding:0 0 0 20px;list-style:none;border-left:1px solid var(--ink);font-size:.8rem}
.cover-line li{position:relative}
.cover-line li::before{content:"";position:absolute;left:-26px;top:.3em;width:12px;height:12px;border-radius:var(--r);background:var(--accent)}
```

Non testé dans la page : c'est une esquisse à valider.

### Un moment pour le premier écran

Le premier écran est bien composé mais il ne montre pas le produit. Sous la photo, à la place du bloc « Le résultat », un aperçu d'agenda en code : une semaine, quatre à cinq créneaux « Visite toiture », « Visite façade », avec le repère carré bleu, et l'étiquette « Exemple ». Il illustre « Complet. » mieux qu'une photo. Les noms et les villes y seraient des exemples : à décider avec le propriétaire, puisque le brief interdit toute preuve inventée.

### L'écran de chargement

Le pourcentage est un décor. Deux options : le supprimer (le site s'affiche déjà vite), ou garder 0,4 s de logo sur fond encre sans compteur ni barre. Les éléments en cause : `<span class="ld-n"><span id="ld-n">0</span>%</span>`, `<i class="ld-bar" id="ld-bar"></i>` et la durée `(innerWidth<761?900:1300)`.

### WhatsApp

- Garder le vert sur le seul pictogramme. Le grand bouton vert `.dq-wa` du bloc contact deviendrait un bouton au trait, comme « Réserver mon appel de 15 min ».
- Sur téléphone, décaler le bouton rond quand il recouvre un titre, ou le masquer tant que le premier écran est visible.

### La section formules

Trois colonnes identiques qui disent « Sur devis » ne comparent rien. Deux pistes : une seule liste « Ce qui est toujours inclus », puis trois lignes « Une équipe, un secteur », « Deux équipes ou plus », « Plusieurs secteurs » ; ou garder les trois colonnes en remplaçant le grand « Sur devis » par ce qui les distingue. Et choisir entre « Un prix clair » et l'absence de prix : le titre promet ce que la section ne montre pas.

### Autres points à trancher

- Les six cartes « Fini » : une seule liste barrée, comme celle des pages métiers (« × Une petite fuite à dépanner »), prendrait un écran de moins sur téléphone.
- « Head of Sales », « Head of Performance » : des titres en français, au moins dans le bouton flottant (« Parler à Martin »).
- Points finaux des titres : soit tous les titres-slogans en portent un, soit aucun.
- Navigation : retirer le soulignement permanent des sept liens de l'en-tête et le garder au survol.
- Survols : ramener les durées vers 0,2 s pour les changements de couleur ; garder le remplissage en deux bandes des boutons, qui fait partie de la marque.
- Maquettes : vérifier que « Toitures Martin » et « toitures-martin.fr » ne désignent pas une entreprise réelle, sinon prendre un nom manifestement fictif.
- Nombre de corps de texte : ramener les 32 tailles de l'accueil à une échelle d'une dizaine. C'est un chantier à part, sans effet visible immédiat.

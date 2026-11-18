# Audit final du site Bartier & Co

Date : 18 novembre 2026, fin de journée. Site audité : https://bartier-8b.vercel.app (version en ligne), 27 pages.

## Verdict

Le site est prêt sur tout ce qui dépend du code : affichage, vitesse, accessibilité, SEO technique, AEO, cookies, formulaires, sécurité. Aucun défaut ouvert.

Il reste 5 actions de votre côté avant la mise en ligne réelle : informations légales, domaine, réception des formulaires, identifiants de mesure (si vous voulez de la publicité), et un test sur un vrai iPhone.

## Résultats

| Contrôle | Résultat |
|---|---|
| Affichage, 27 pages sur téléphone et ordinateur (débordements, textes coupés, erreurs) | Aucun problème |
| Lighthouse sur téléphone, 7 pages en ligne | Performance 97 à 100, accessibilité 100, bonnes pratiques 100 |
| Affichage principal (LCP) et stabilité (CLS) | 1,4 à 2,2 s ; 0 à 0,003 |
| Note SEO de Lighthouse | 66 à 69, pour une seule raison : le blocage d'indexation voulu. Sans lui : 100 |
| Liens internes | 812 vérifiés, 0 cassé |
| Plan du site | 27 adresses, toutes répondent 200 |
| Titre principal, titre et description de chaque page | Conformes partout |
| Données structurées | Valides sur toutes les pages, identiques au texte visible |
| Typographie française (espaces insécables, apostrophes) | 0 défaut |
| AEO : 20 questions cibles | 20 avec un intertitre et une réponse courte |
| Questions-réponses balisées | 148 |
| Sources officielles citées | 29 liens |
| Formulaire artisans | Vérifications, messages d'erreur et repli WhatsApp/e-mail/téléphone : conformes |
| Formulaire particuliers | 5 étapes, texte d'accord conforme, repli prérempli : conforme |
| Cookies | Rien ne se charge avant l'accord. Refuser est aussi simple qu'accepter. L'accord expire après 6 mois. Le clavier fonctionne |
| Sécurité | HTTPS strict, protection contre l'intégration dans un autre site, pas de détection du type de fichier, politique de provenance, accès caméra, micro et position coupés |
| Redirections des anciennes adresses | Toutes mènent à la bonne page ; page inexistante : vrai code 404 |
| robots.txt, llms.txt, llms-full.txt, clé IndexNow | En ligne |
| Navigateurs anciens (simulation) | Même rendu, avec les couleurs de repli |
| JavaScript | Niveau ES2017 au plus : compatible avec tous les navigateurs actuels |
| Photo d'ouverture sur iPhone (émulation) | Ouverture, fermeture et va-et-vient rapides corrects, aucune erreur |
| Photos du blog sur l'accueil | Chargées et affichées, sur téléphone et ordinateur |

## Points mineurs, sans action nécessaire

- Les pages Métiers et Blog sont courtes (178 et 75 mots) : ce sont des sommaires.
- Deux intertitres de l'accueil restent génériques (« Le blog », « Notre parole ») : c'est un choix de mise en page.
- Les anciennes adresses sans barre finale passent par deux redirections au lieu d'une. Sans effet sur le référencement.
- Deux propriétés CSS ne sont pas reconnues par Safari (redimensionnement d'un champ de texte, réglage du toucher). Elles améliorent l'usage ailleurs et n'ont aucun effet visible sur Safari.

## Limites de cet audit

- Les tests de navigateur tournent dans Chromium. Safari et Firefox réels n'ont pas pu être testés ici : un essai sur votre iPhone reste nécessaire, surtout pour la photo d'ouverture.
- Les formulaires n'envoient pas encore les demandes à un serveur : ils finissent sur WhatsApp, l'e-mail ou le téléphone, préremplis.

## Ce qui reste à faire, et qui dépend de vous

1. **Informations légales** : SIREN, ville du greffe, capital, numéro de TVA, directeur de la publication, médiateur. La mise en ligne est bloquée tant qu'elles manquent (voir `docs/legal-a-valider.md`).
2. **Domaine** : brancher bartierandco.com. Ensuite j'ouvre l'indexation (`LIVE = True`), je déclare le site à Google Search Console et à Bing Webmaster Tools, et j'envoie le plan du site.
3. **Réception des formulaires** : choisir où arrivent les demandes (adminbartier@gmail.com, un CRM, ou les deux).
4. **Mesure** : les identifiants Google Analytics, Google Ads et Meta, si vous voulez suivre la publicité. Le bandeau cookies est prêt.
5. **Confiance et AEO** : fiche Google Business Profile, photos et parcours des fondateurs, premières mentions sur d'autres sites, vrais avis et vrais chiffres dès les premiers clients.
6. **Validation juridique** : faire relire par votre avocat les règles d'appel des particuliers et la publicité pour l'isolation (questions ouvertes dans `docs/legal-a-valider.md`).

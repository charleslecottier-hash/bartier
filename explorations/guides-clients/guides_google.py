"""Deux guides Word pour les clients : donner l'accès Google (Google Ads, fiche Google, Analytics) à Bartier & Co.

    python3 guides_google.py   # écrit les deux .docx à côté de ce script

Guide 1 : le client a déjà un compte Google Ads. Guide 2 : il n'en a pas.
Même méthode que l'ancien « Guide accès Google, Bartier & Co.pdf » du 17/11 : le client envoie son numéro de compte,
Bartier & Co envoie une demande de gestion, le client l'accepte. Mise en page commune avec guides_meta.py.
"""
from docx.shared import Cm, Pt
from docx.oxml import OxmlElement

from guides_meta import (ACCENT, INK, PAPER, SOFT, TEL_TXT, TINT, WA, Guide, cell_margins, no_borders, runs, shade)

MCC = "606-439-4700"  # compte administrateur (MCC) de Bartier & Co, créé le 23/11/2026, qui gère les comptes des clients
PUB = "656-734-9439"  # compte publicitaire de Bartier & Co, pour ses propres annonces
GMAIL = "adminbartier@gmail.com"  # compte Google de l'entreprise (propriétaire du compte administrateur)
ADS = "https://ads.google.com"


def intro(g, minutes, extra=None):
    lines = [[("Durée : ", "b"), minutes],
             [("Sur ordinateur : ", "b"), "Google Ads est bien plus simple à utiliser sur un écran d’ordinateur que sur un téléphone."],
             [("Vous restez propriétaire de tout : ", "b"), "vos comptes restent à votre nom, et le budget de vos annonces est payé directement à Google avec votre carte. Vous pouvez retirer notre accès à tout moment."],
             [("Nous ne vous demanderons jamais votre mot de passe.", "b")]]
    if extra:
        lines.append(extra)
    g.box(lines)


def besoin(g):
    g.h1("Ce dont nous avons besoin")
    g.bullets([[("Votre compte Google Ads : ", "b"), "pour créer et suivre vos annonces. C’est la partie principale."],
               [("Votre fiche Google, si vous en avez une : ", "b"), "la fiche qui apparaît sur Google Maps et dans les résultats quand on cherche votre entreprise."],
               [("Google Analytics, si votre site l’utilise : ", "b"), "pour mesurer les demandes qui arrivent par vos annonces."]])
    t = g.d.add_table(rows=1, cols=1); no_borders(t)
    c = t.cell(0, 0); shade(c, TINT); cell_margins(c, 200, 200, 260, 260)
    p = c.paragraphs[0]; runs(p, ["Compte Google Ads de Bartier & Co (celui qui vous envoie la demande d’accès)"], size=10, color=SOFT); p.paragraph_format.space_after = Pt(2)
    p = c.add_paragraph(); r = p.add_run(MCC); r.bold = True; r.font.size = Pt(17); r.font.name = "Consolas"; p.paragraph_format.space_after = Pt(8)
    p = c.add_paragraph(); runs(p, ["Adresse Google de Bartier & Co (pour la fiche Google et Analytics)"], size=10, color=SOFT); p.paragraph_format.space_after = Pt(2)
    p = c.add_paragraph(); r = p.add_run(GMAIL); r.bold = True; r.font.size = Pt(17); r.font.name = "Consolas"; p.paragraph_format.space_after = Pt(4)
    p = c.add_paragraph(); runs(p, ["Ni le numéro ni l’adresse ne sont des mots de passe : ils servent seulement à vérifier que l’accès va bien à Bartier & Co."], size=9.5, color=SOFT)
    g.d.add_paragraph().paragraph_format.space_after = Pt(2)


def exemple_numero(g):
    """Illustration du numéro de compte (exemple, pas une capture)."""
    t = g.d.add_table(rows=1, cols=1); no_borders(t)
    c = t.cell(0, 0); shade(c, PAPER); cell_margins(c, 160, 160, 240, 240)
    p = c.paragraphs[0]; runs(p, ["Exemple : en haut à droite de Google Ads"], size=9.5, color=SOFT); p.paragraph_format.space_after = Pt(2)
    p = c.add_paragraph(); runs(p, ["Votre entreprise   "], size=11); r = p.add_run("123-456-7890"); r.bold = True; r.font.size = Pt(15); r.font.name = "Consolas"
    g.d.add_paragraph().paragraph_format.space_after = Pt(2)


def etapes_ads(g, first=1, new_account=False):
    n = first
    if not new_account:
        g.step(n, "Ouvrez Google Ads et connectez-vous",
               [["Ouvrez ", ("lien", ADS, "ads.google.com"), " et cliquez sur « Se connecter » (encadré en bleu). Utilisez le compte Google de votre entreprise, celui qui gère vos annonces."]],
               img=("g-01-ads-se-connecter.png", 13),
               tip="Google vous propose plusieurs comptes : choisissez celui de votre entreprise. Vous ne savez plus lequel ? Appelez-nous, on cherche avec vous.")
        n += 1
    g.step(n, "Repérez votre numéro de compte Google Ads",
           ["C’est le numéro à 10 chiffres écrit en haut à droite de l’écran, à côté du nom de votre compte. Il ressemble à 123-456-7890. Copiez-le, ou notez-le."],
           tip="Vous voyez plusieurs numéros, ou une liste de comptes : envoyez-nous celui du compte qui diffuse (ou diffusera) vos annonces, ou envoyez-nous une capture d’écran.")
    exemple_numero(g)
    n += 1
    g.step(n, "Envoyez-nous ce numéro",
           [["Sur WhatsApp ou par SMS au ", (TEL_TXT, "b"), ", par exemple : « Mon numéro Google Ads : 123-456-7890 ». ", ("lien", WA, "Ouvrir WhatsApp")],
            "Nous vous envoyons alors une demande d’accès à votre compte."])
    n += 1
    g.step(n, "Acceptez notre demande",
           ["Google vous prévient par e-mail qu’une demande de gestion de votre compte est arrivée de la part de Bartier & Co. Cliquez sur le bouton de l’e-mail, puis sur « Accepter ».",
            [("Vérifiez avant d’accepter : ", "b"), f"la demande vient du compte {MCC}, Bartier & Co. Si un autre nom ou un autre numéro apparaît, ne l’acceptez pas et appelez-nous."],
            [("Pas d’e-mail ? ", "b"), "Dans Google Ads, cliquez sur « Administration » (la roue dentée, dans le menu de gauche), puis « Accès et sécurité », onglet « Gestionnaires ». La demande de Bartier & Co y attend votre accord : cliquez sur « Accepter »."]],
           see=f"Bartier & Co, compte {MCC}, dans la liste des gestionnaires de votre compte. La demande reste valable 20 jours : passé ce délai, prévenez-nous, nous la renvoyons.",
           tip="vous ne trouvez pas « Administration » : sur l’ancienne présentation de Google Ads, passez par l’icône « Outils » (la clé), puis « Accès et sécurité ».")
    g.box([[("Autre méthode, si notre demande ne vous arrive pas : ", "b"), "ajoutez directement notre adresse comme utilisateur de votre compte Google Ads."],
           "1. Dans Google Ads : Administration › Accès et sécurité › onglet « Utilisateurs ».",
           ["2. Cliquez sur le « + » bleu et saisissez ", (GMAIL, "b"), "."],
           "3. Choisissez le niveau d’accès « Administrateur », puis « Envoyer l’invitation ». Prévenez-nous : nous acceptons de notre côté."])
    return n


def etapes_fiche(g, first):
    n = first
    g.para("Votre fiche Google est la fiche de votre entreprise sur Google Maps et dans les résultats de recherche. En nous ajoutant comme gestionnaire, nous pouvons la tenir à jour et l’accorder avec vos annonces.")
    g.step(n, "Ouvrez la gestion de votre fiche",
           ["Connecté au compte Google qui gère la fiche, cherchez le nom de votre entreprise sur Google. Le panneau de gestion de votre fiche apparaît en haut des résultats."],
           tip="le panneau n’apparaît pas : la fiche est sans doute gérée par un autre compte Google (un associé, une ancienne agence). Appelez-nous, on vous aide à la récupérer.")
    n += 1
    g.step(n, "Allez dans « Personnes et accès »",
           ["Dans le panneau, cliquez sur les 3 petits points, puis « Paramètres du profil », puis « Personnes et accès » (parfois appelé « Gestionnaires »). Cliquez ensuite sur « Ajouter »."])
    n += 1
    g.step(n, "Ajoutez notre adresse comme « Gestionnaire »",
           [["Collez l’adresse ", (GMAIL, "b"), ", choisissez le rôle « Gestionnaire », puis cliquez sur « Inviter »."],
            "Avec ce rôle, nous ne pouvons ni supprimer votre fiche ni en changer le propriétaire : vous en restez le seul propriétaire."],
           see="notre adresse dans la liste, avec la mention « Invitation en attente » jusqu’à ce que nous l’acceptions.")
    return n


def analytics(g):
    g.para("Seulement si votre site internet utilise Google Analytics. Sinon, passez directement à la suite.", color=SOFT, size=10.5)
    g.bullets([["Ouvrez ", ("lien", "https://analytics.google.com", "analytics.google.com"), ", connecté au compte Google de votre entreprise."],
               "Cliquez sur « Administration » (la roue dentée, en bas à gauche).",
               "Dans la colonne « Compte », cliquez sur « Gestion des accès au compte ».",
               ["Cliquez sur le « + » bleu, puis « Ajouter des utilisateurs ». Collez l’adresse ", (GMAIL, "b"), "."],
               "Choisissez le rôle « Éditeur », puis cliquez sur « Ajouter »."], style="List Number")


def fin(g, n):
    g.step(n, "Prévenez-nous : écrivez « C’est fait »",
           [["Sur WhatsApp ou par SMS au ", (TEL_TXT, "b"), ". ", ("lien", WA, "Ouvrir WhatsApp")],
            "Nous vérifions de notre côté que tous les accès sont bien arrivés, et nous vous rappelons si un réglage manque."])


def blocages(g, extra=()):
    g.h1("Si quelque chose bloque")
    items = [[("« Je ne vois pas de demande de Bartier & Co. » ", "b"), "Nous ne l’avons peut-être pas encore envoyée : vérifiez que vous nous avez bien transmis votre numéro à 10 chiffres. Regardez aussi dans vos courriers indésirables."],
             [("« Google me demande un code ou une vérification. » ", "b"), "C’est normal : Google protège les comptes professionnels. Suivez ses instructions (code reçu par SMS ou par e-mail)."],
             [("« J’ai accepté par erreur une autre demande. » ", "b"), "Rien de grave : vous pouvez mettre fin à n’importe quel accès (voir « Retirer l’accès », plus bas)."]]
    items += list(extra)
    g.bullets(items)
    g.box([[("Le plus simple si vous êtes bloqué : ", "b"), f"appelez-nous au {TEL_TXT}. Nous faisons les étapes avec vous au téléphone, écran par écran. Comptez un quart d’heure."]], fill=TINT)


def retirer(g):
    g.h1("Retirer l’accès plus tard")
    g.para("Vous gardez la main à tout moment :")
    g.bullets([[("Google Ads : ", "b"), "Administration › Accès et sécurité › onglet « Gestionnaires » › Bartier & Co › mettre fin à l’association."],
               [("Fiche Google : ", "b"), "Paramètres du profil › Personnes et accès › notre adresse › Supprimer."],
               [("Analytics : ", "b"), "Administration › Gestion des accès au compte › notre adresse › Supprimer l’accès."]])
    g.para("Vos comptes, vos annonces et leur historique restent à vous.", color=SOFT, size=10.5)


# ——— Guide 1 : le client a déjà Google Ads ———
def guide_1():
    g = Guide()
    g.logo()
    g.title("Donner l’accès Google à Bartier & Co", "Guide 1 : vous avez déjà un compte Google Ads")
    g.para("Pour créer et suivre vos annonces sur Google, nous avons besoin d’un accès à votre compte Google Ads, et si vous en avez une, à votre fiche Google. "
           "Pour Google Ads, vous n’avez presque rien à faire : vous nous envoyez votre numéro de compte, et vous acceptez notre demande. Ce guide vous accompagne clic par clic.")
    intro(g, "5 à 10 minutes.")
    besoin(g)
    g.h1("Partie 1 : votre compte Google Ads", new_page=True)
    n = etapes_ads(g)
    g.h1("Partie 2 : votre fiche Google (si vous en avez une)", new_page=True)
    n = etapes_fiche(g, n + 1)
    g.h1("Partie 3 : Google Analytics (si votre site l’utilise)")
    analytics(g)
    g.h1("Dernière étape")
    fin(g, n + 1)
    blocages(g, extra=[[("« Je n’ai plus accès à mon compte Google Ads. » ", "b"), "Il a peut-être été ouvert avec une autre adresse, ou par une ancienne agence. Appelez-nous : on retrouve avec vous à qui il appartient."]])
    retirer(g)
    return g.save("Guide accès Google 1 - Vous avez déjà Google Ads - Bartier & Co.docx")


# ——— Guide 2 : le client n'a pas de compte Google Ads ———
def guide_2():
    g = Guide()
    g.logo()
    g.title("Créer votre compte Google Ads et donner l’accès à Bartier & Co", "Guide 2 : vous n’avez pas encore de compte Google Ads")
    g.para("Pour diffuser vos annonces sur Google, votre entreprise a besoin d’un compte Google Ads à son nom. Ce guide vous le fait créer, sans lancer de campagne, "
           "puis donner l’accès à Bartier & Co. Prenez-le partie par partie : vous pouvez faire une pause entre deux parties.")
    intro(g, "20 à 30 minutes au total, en 5 parties.",
          extra=[("Vous préférez le faire avec nous ? ", "b"), f"Appelez-nous au {TEL_TXT} : nous créons le compte ensemble au téléphone, en partageant votre écran. Il sera à votre nom, avec votre carte bancaire, et c’est vous qui la saisissez."])
    g.box([[("Important : ne créez pas de campagne. ", "b"),
            "À l’ouverture du compte, Google pousse à lancer tout de suite une première annonce. Ne le faites pas : c’est notre travail, et une campagne mal réglée dépense votre budget sans vous apporter de clients. "
            "Ne vous occupez pas non plus des offres d’avoir publicitaire affichées : nous regarderons avec vous si l’une vaut le coup."]], fill=TINT)
    g.h1("Le parcours en un coup d’œil")
    tbl = g.d.add_table(rows=1, cols=3); tbl.style = "Table Grid"; tbl.autofit = False
    for c, t in zip(tbl.rows[0].cells, ("Partie", "Ce que vous faites", "Durée")):
        shade(c, PAPER); runs(c.paragraphs[0], [(t, "b")], size=10.5)
    for row in (("1", "Créer votre compte Google (si vous n’en avez pas)", "5 min"), ("2", "Créer votre compte Google Ads, sans campagne", "10 min"),
                ("3", "Ajouter votre moyen de paiement", "5 min"), ("4", "Donner l’accès à Bartier & Co", "5 min"),
                ("5", "Votre fiche Google, et nous prévenir", "5 min")):
        cells = tbl.add_row().cells
        for c, t in zip(cells, row):
            runs(c.paragraphs[0], [t], size=10.5)
    for i, w in enumerate((Cm(1.8), Cm(12.2), Cm(2.6))):
        tbl.columns[i].width = w
        for c in tbl.columns[i].cells:
            c.width = w
    g.d.add_paragraph().paragraph_format.space_after = Pt(2)
    g.h1("Préparez avant de commencer")
    g.checks(["Une adresse e-mail professionnelle, que vous consultez.",
              "Votre téléphone portable : Google envoie des codes de confirmation par SMS.",
              "Le nom exact de votre entreprise et son adresse, comme sur vos factures.",
              "Votre site internet, si vous en avez un.",
              "Une carte bancaire professionnelle, pour le budget de vos annonces (partie 3).",
              "Ce guide ouvert à côté, ou imprimé."])

    # Partie 1
    g.h1("Partie 1 : créer votre compte Google")
    g.box([[("Vous avez déjà une adresse Gmail ou un compte Google pour l’entreprise ? ", "b"), "Passez directement à la partie 2 et utilisez-le."]])
    g.step(1, "Ouvrez la page de création de compte",
           [["Ouvrez ", ("lien", "https://accounts.google.com/signup", "accounts.google.com/signup"), ". La page « Créer un compte Google » s’affiche."]],
           img=("g-03-creer-compte-google.png", 9))
    g.step(2, "Indiquez votre prénom et votre nom, puis « Suivant »",
           ["Google demande ensuite votre date de naissance et votre genre."])
    g.step(3, "Choisissez l’adresse du compte",
           ["Google vous propose une adresse Gmail. Vous pouvez aussi garder votre adresse e-mail professionnelle actuelle : choisissez alors l’option prévue pour cela, sous les propositions d’adresses Gmail."],
           tip="vous hésitez : une adresse Gmail dédiée à l’entreprise (par exemple nomentreprise@gmail.com) fonctionne très bien.")
    g.step(4, "Créez un mot de passe et confirmez votre numéro de portable",
           ["Google vous envoie un code par SMS : tapez-le dans la fenêtre. Acceptez ensuite les conditions d’utilisation."],
           see="la page d’accueil de votre compte Google.")
    g.box([[("À retenir : ", "b"), "notez votre mot de passe dans un endroit sûr. Ne le donnez à personne, pas même à nous : nous n’en aurons jamais besoin."]])

    # Partie 2
    g.h1("Partie 2 : créer votre compte Google Ads, sans campagne", new_page=True)
    g.step(1, "Ouvrez Google Ads et cliquez sur « Commencer »",
           [["Ouvrez ", ("lien", ADS, "ads.google.com"), " et cliquez sur le bouton bleu « Commencer » (encadré en bleu). Connectez-vous avec le compte Google de la partie 1."]],
           img=("g-02-ads-commencer.png", 13))
    g.step(2, "Répondez aux premières questions",
           ["Google vous demande le nom de votre entreprise et votre site internet, s’il existe. Répondez simplement."])
    g.step(3, "Refusez la création de campagne",
           ["Google vous propose alors de créer votre première campagne. Ne le faites pas : cherchez le lien « Créer un compte sans campagne », parfois « Passer en mode Expert », souvent tout en bas de l’écran."],
           tip="vous ne trouvez pas ce lien, ou Google vous oblige à continuer : arrêtez-vous là et appelez-nous. On termine ensemble en deux minutes.")
    g.step(4, "Vérifiez les informations du compte",
           [[("Pays de facturation : ", "b"), "France. ", ("Fuseau horaire : ", "b"), "(GMT+01:00) Paris. ", ("Devise : ", "b"), "euro (EUR)."],
            "Cliquez ensuite sur « Envoyer », puis sur « Explorer votre compte »."],
           see="l’écran d’accueil de Google Ads, avec votre numéro de compte en haut à droite.")
    g.box([[("Attention : ", "b"), "la devise ne peut plus être modifiée une fois le compte créé. Vérifiez-la bien, ainsi que le fuseau horaire, avant de valider."]])

    # Partie 3
    g.h1("Partie 3 : ajouter votre moyen de paiement")
    g.para("Le budget de vos annonces est payé directement à Google avec votre carte : Bartier & Co ne touche pas à cet argent. Aucune somme n’est dépensée tant qu’aucune campagne ne tourne.")
    g.bullets(["Dans le menu de gauche de Google Ads, cliquez sur « Facturation ».",
               "Si Google vous le propose, choisissez le type de compte « Entreprise », puis indiquez le nom et l’adresse de votre entreprise, comme sur vos factures.",
               "Ajoutez votre carte bancaire professionnelle et enregistrez.",
               "Si Google vous demande votre numéro de TVA intracommunautaire, indiquez-le s’il existe."], style="List Number")

    # Partie 4
    g.h1("Partie 4 : donner l’accès à Bartier & Co", new_page=True)
    g.para("Vous n’avez presque rien à faire : vous nous envoyez votre numéro de compte, et vous acceptez notre demande.")
    n = etapes_ads(g, first=1, new_account=True)

    # Partie 5
    g.h1("Partie 5 : votre fiche Google, et nous prévenir", new_page=True)
    g.box([[("Vous n’avez pas de fiche Google ? ", "b"), "Dites-le-nous : c’est souvent le premier moyen d’être trouvé par les clients près de chez vous, et nous vous aidons à la créer."]])
    n = etapes_fiche(g, n + 1)
    g.h2("Si votre site utilise Google Analytics")
    analytics(g)
    fin(g, n + 1)
    g.box([[("C’est terminé. ", "b"), "Votre entreprise a maintenant son compte Google Ads à son nom, avec votre carte, et nous y avons accès. Nous nous occupons de la suite."]], fill=TINT)
    blocages(g, extra=[[("« Google a lancé une campagne sans que je le veuille. » ", "b"), "Ouvrez « Campagnes » dans le menu de gauche, et mettez-la en pause avec le bouton à côté de son nom. Puis appelez-nous."]])
    retirer(g)
    return g.save("Guide accès Google 2 - Vous n'avez pas encore Google Ads - Bartier & Co.docx")


def procedure_interne():
    """Pour Charles et Martin : relier le compte Google Ads d'un client au compte Bartier & Co."""
    g = Guide()
    g.logo()
    g.title("Relier un client Google Ads au compte Bartier & Co", f"Procédure interne · compte {MCC}")
    g.para(f"Tous les comptes Google Ads des clients sont gérés depuis le compte Bartier & Co ({MCC}). Le client garde son compte et sa carte ; nous y accédons depuis ce compte. "
           "Cette fiche décrit ce que nous faisons de notre côté, en face des guides clients 1 et 2.")
    g.h1("Une seule fois : mettre le compte en place")
    g.box([[("Compte administrateur : ", "b"), f"{MCC}, créé le 23 novembre 2026 avec {GMAIL}. C’est lui qui envoie les demandes d’accès aux clients."],
           [("Compte publicitaire de Bartier & Co : ", "b"), f"{PUB}, pour nos propres annonces. Il ne sert pas aux clients."]])
    g.bullets([[("Rattacher notre compte publicitaire : fait le 23 novembre 2026. ", "b"), f"{PUB} apparaît dans Comptes › Performances du compte administrateur."],
               [("Sécuriser ", "b"), f"{GMAIL}, pour l’instant seul administrateur : validation en deux étapes avec deux méthodes (téléphone et codes de secours imprimés), "
                "e-mail et téléphone de récupération (myaccount.google.com › Sécurité). Si cet accès est perdu, tous les comptes clients sont bloqués. "
                "Identifiants partagés entre Charles et Martin par un gestionnaire de mots de passe, jamais par message."],
               [("Notifications : ", "b"), "Admin › Notifications, activer au moins les alertes de refus d’annonces, de problèmes de paiement et de règlement, pour tous les comptes gérés."],
               [("Règlement : ", "b"), "Admin › Règlement › Récapitulatif, traiter les points en attente du compte administrateur."],
               [("Windsor.ai : ", "b"), f"reconnecter Google Ads avec {GMAIL} et cocher {MCC} et {PUB}, pour que les comptes des clients apparaissent dans le suivi."],
               [("Dès que nous avons le SIREN : ", "b"), "faire la vérification « agence » (Admin › Règlement : « Advertiser verification – Agency »), avec le Kbis et le SIREN."],
               [("Facultatif, plus tard : ", "b"), "quand nous aurons des adresses @bartierandco.com, les ajouter au niveau « Administrateur » (Admin › Accès et sécurité › Utilisateurs › « + »), "
                f"vérifier qu’elles fonctionnent, et garder {GMAIL} en secours. Toujours au moins deux administrateurs dès que possible. "
                "Les liens avec les clients ne changent pas : ils sont attachés au compte administrateur, pas aux personnes."]], style="List Number")
    g.h1("Pour chaque client qui a déjà Google Ads (guide 1)")
    g.step(1, "Envoyer le guide au client", ["Guide accès Google 1, par e-mail ou WhatsApp, avec ce message :",
                                              [("« ", ""), "Bonjour, voici le guide pour nous donner l’accès à Google Ads. Il suffit de nous envoyer le numéro à 10 chiffres en haut à droite de votre compte : on s’occupe du reste. ", ("»", "")]])
    g.step(2, "Recevoir son numéro à 10 chiffres", ["Le noter dans la fiche du client dans Pipedrive, avec la date."])
    g.step(3, "Ouvrir la liste des comptes du compte administrateur",
           [f"Dans Google Ads, vérifier en haut à gauche qu’on est bien sur « Bartier & Co {MCC} ». Cliquer sur l’icône « Comptes » dans la barre de gauche : la page « Performances » s’ouvre."],
           img=("g-mcc-01-comptes.png", 4.2))
    g.step(4, "Cliquer sur le bouton bleu rond « + », puis « Associer un compte existant »",
           ["Le bouton est à gauche, juste au-dessus du tableau, à côté de l’entonnoir des filtres. Si une liste déroulante de comptes est ouverte en haut, la fermer d’abord (touche Échap)."],
           img=("g-mcc-02-bouton-plus.png", 11))
    g.step(5, "Remplir le panneau « Associer des comptes existants »",
           ["Coller le numéro du client dans le grand cadre (un numéro par ligne si plusieurs clients). Laisser « This manager: Bartier & Co » comme administrateur direct. "
            "Justification, facultative : « Bartier & Co : gestion de vos annonces Google ». Puis cliquer sur « Envoyer la demande », en bas à gauche du panneau."],
           img=("g-mcc-03-associer.png", 14),
           see="le compte du client dans l’onglet « Demandes d’association envoyées », en attente. La demande expire au bout de 20 jours.")
    g.figure("g-mcc-04-envoyer.png", 6, "Le bouton « Envoyer la demande », en bas du panneau.")
    g.step(6, "Prévenir le client", [[("« ", ""), "C’est envoyé : vous allez recevoir un e-mail de Google. Vérifiez que la demande vient du compte ", (MCC, "b"), ", puis cliquez sur « Accepter ». ", ("»", "")]])
    g.step(7, "Vérifier l’acceptation",
           ["Dans « Comptes » › « Performances », le compte du client apparaît, actif. Pour voir les demandes encore en attente : onglet « Demandes d’association envoyées ». "
            "Sans réponse au bout de 48 heures, appeler le client et faire l’étape avec lui. Au-delà de 20 jours, la demande expire : la renvoyer."],
           tip="le client a utilisé la méthode de secours (il a ajouté notre adresse comme utilisateur) : accepter l’e-mail d’invitation de Google reçu sur " + GMAIL + ".")
    g.step(8, "Régler le compte du client",
           ["Ouvrir le compte du client depuis Comptes › Performances, puis Admin › Règlement › Récapitulatif :",
            "faire la déclaration « annonces politiques dans l’UE » (réponse : non) ;",
            "si Google propose la vérification de l’annonceur (« Client verification »), cliquer sur « Copy link » et envoyer le lien au client : c’est lui qui vérifie son entreprise.",
            [("Propriétaire : ", "b"), "le lien est créé avec « Propriétaire : Non ». On le laisse ainsi : nous gérons les annonces, le client garde la main sur les accès à son compte."]])
    g.step(9, "Fiche Google et Analytics", [f"Accepter les invitations reçues sur {GMAIL} : « gestionnaire » de la fiche Google, « éditeur » d’Analytics."])
    g.step(10, "Brancher le suivi", ["Dans Windsor.ai, le nouveau compte apparaît avec les autres. S’il n’y est pas, reconnecter Google Ads dans Windsor pour actualiser la liste des comptes."])
    g.h1("Pour un client qui n’a pas Google Ads (guide 2)")
    g.para("Deux possibilités :")
    g.bullets([[("Le client crée son compte avec le guide 2, ", "b"), "puis on reprend à l’étape 2 ci-dessus. C’est la solution par défaut : le compte est à son nom dès le départ."],
               [("Ou nous créons le compte depuis le compte Bartier & Co : ", "b"), "Comptes › Performances › bouton bleu rond « + » › « Créer un compte ». Nom : l’entreprise du client ; devise : euro ; fuseau : Paris. "
                "Inviter ensuite le client comme « Administrateur » (Accès et sécurité › Utilisateurs), et lui faire ajouter sa carte dans « Facturation ». Utile au téléphone, avec un client peu à l’aise."]])
    g.box([[("Règle : ", "b"), "jamais de campagne lancée sans l’accord écrit du client sur le budget, et jamais notre carte sur le compte d’un client. Le budget est payé directement à Google par le client."]], fill=TINT)
    return g.save("Procédure interne - Relier un client Google Ads au compte Bartier & Co.docx")


if __name__ == "__main__":
    for f in (guide_1(), guide_2(), procedure_interne()):
        print(f)

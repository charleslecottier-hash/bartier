"""Deux guides Word pour les clients : donner l'accès Meta à Bartier & Co.

    python3 guides_meta.py   # écrit les deux .docx à côté de ce script

Guide 1 : le client a déjà Facebook et une Page. Guide 2 : il n'a pas Facebook.
"""
import pathlib

from docx import Document
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.opc.constants import RELATIONSHIP_TYPE as RT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor

HERE = pathlib.Path(__file__).resolve().parent
LOGO = HERE.parent / "v8b" / "assets" / "logo-bartier.png"
CAP = HERE / "captures"  # captures d'écran de Meta (pages publiques et menu des Paramètres), annotées en bleu
ID = "1167396645943823"
TEL, TEL_TXT, MAIL = "+33781018936", "07 81 01 89 36", "contact@bartierandco.com"
WA = "https://wa.me/33781018936"
VIDEO = "https://drive.google.com/file/d/1GdguuoRIl5nPzljqcj5rnOiUgqpAapos/view?usp=drivesdk"
PARTNERS = "https://business.facebook.com/settings/partners"
INK, ACCENT, SOFT, PAPER, TINT = RGBColor(0x0A, 0x14, 0x24), RGBColor(0x2D, 0x5B, 0xE3), RGBColor(0x4E, 0x5A, 0x66), "EEF0F3", "DCE4FB"


# ——— Outils de mise en page ———
def shade(cell, hex_):
    tcPr = cell._tc.get_or_add_tcPr()
    sh = OxmlElement("w:shd")
    sh.set(qn("w:val"), "clear"); sh.set(qn("w:color"), "auto"); sh.set(qn("w:fill"), hex_)
    tcPr.append(sh)


def no_borders(table):
    tblPr = table._tbl.tblPr
    b = OxmlElement("w:tblBorders")
    for e in ("top", "left", "bottom", "right", "insideH", "insideV"):
        x = OxmlElement(f"w:{e}"); x.set(qn("w:val"), "nil"); b.append(x)
    tblPr.append(b)


def cell_margins(cell, top=120, bottom=120, left=160, right=160):
    tcPr = cell._tc.get_or_add_tcPr()
    m = OxmlElement("w:tcMar")
    for k, v in (("top", top), ("bottom", bottom), ("start", left), ("end", right)):
        x = OxmlElement(f"w:{k}"); x.set(qn("w:w"), str(v)); x.set(qn("w:type"), "dxa"); m.append(x)
    tcPr.append(m)


def keep_with_next(p):
    p.paragraph_format.keep_with_next = True


def link(paragraph, url, text, bold=False):
    r_id = paragraph.part.relate_to(url, RT.HYPERLINK, is_external=True)
    h = OxmlElement("w:hyperlink"); h.set(qn("r:id"), r_id)
    r = OxmlElement("w:r"); rPr = OxmlElement("w:rPr")
    c = OxmlElement("w:color"); c.set(qn("w:val"), "2D5BE3"); rPr.append(c)
    u = OxmlElement("w:u"); u.set(qn("w:val"), "single"); rPr.append(u)
    if bold:
        rPr.append(OxmlElement("w:b"))
    r.append(rPr)
    t = OxmlElement("w:t"); t.text = text; t.set(qn("xml:space"), "preserve"); r.append(t)
    h.append(r); paragraph._p.append(h)


def runs(p, parts, size=None, color=None):
    """parts : texte simple, ou (texte, 'b') pour du gras, ou ('lien', url, texte)."""
    for x in parts:
        if isinstance(x, tuple) and x[0] == "lien":
            link(p, x[1], x[2])
            continue
        txt, style = (x, "") if isinstance(x, str) else x
        r = p.add_run(txt)
        r.bold = "b" in style
        if size:
            r.font.size = Pt(size)
        if color is not None:
            r.font.color.rgb = color
    return p


class Guide:
    def __init__(self):
        self.d = Document()
        s = self.d.sections[0]
        s.page_height, s.page_width = Cm(29.7), Cm(21)
        s.left_margin = s.right_margin = Cm(2.2)
        s.top_margin, s.bottom_margin = Cm(1.8), Cm(1.8)
        st = self.d.styles["Normal"]
        st.font.name = "Calibri"; st.font.size = Pt(11); st.font.color.rgb = INK
        st.element.rPr.rFonts.set(qn("w:eastAsia"), "Calibri")
        st.paragraph_format.space_after = Pt(6); st.paragraph_format.line_spacing = 1.15
        foot = s.footer.paragraphs[0]
        foot.alignment = WD_ALIGN_PARAGRAPH.CENTER
        runs(foot, [f"Bartier & Co · {TEL_TXT} (appel ou WhatsApp) · {MAIL} · bartierandco.com"], size=8.5, color=SOFT)

    # blocs
    def logo(self):
        p = self.d.add_paragraph()
        p.add_run().add_picture(str(LOGO), width=Cm(4.2))
        p.paragraph_format.space_after = Pt(14)

    def title(self, t, sub):
        p = self.d.add_paragraph(); runs(p, [(t, "b")], size=24); p.paragraph_format.space_after = Pt(2)
        p = self.d.add_paragraph(); runs(p, [sub], size=13, color=ACCENT); p.paragraph_format.space_after = Pt(14)

    def h1(self, t, new_page=False):
        p = self.d.add_paragraph()
        if new_page:
            p.paragraph_format.page_break_before = True
        p.paragraph_format.space_before = Pt(16); p.paragraph_format.space_after = Pt(6)
        runs(p, [(t, "b")], size=16); keep_with_next(p)
        return p

    def h2(self, t):
        p = self.d.add_paragraph(); p.paragraph_format.space_before = Pt(10); p.paragraph_format.space_after = Pt(4)
        runs(p, [(t, "b")], size=12.5); keep_with_next(p)

    def para(self, *parts, size=None, color=None, after=6):
        p = self.d.add_paragraph(); runs(p, parts, size=size, color=color); p.paragraph_format.space_after = Pt(after)
        return p

    def bullets(self, items, style="List Bullet"):
        if style == "List Number":  # numérotation écrite à la main : chaque liste repart de 1
            for i, it in enumerate(items, 1):
                p = self.d.add_paragraph(); f = p.paragraph_format
                f.left_indent, f.first_line_indent, f.space_after = Cm(0.8), Cm(-0.6), Pt(3)
                f.tab_stops.add_tab_stop(Cm(0.8))
                runs(p, [(f"{i}.", "b"), "\t"] + (it if isinstance(it, list) else [it]))
            return
        for it in items:
            p = self.d.add_paragraph(style=style)
            runs(p, it if isinstance(it, list) else [it]); p.paragraph_format.space_after = Pt(3)

    def checks(self, items):
        for it in items:
            p = self.d.add_paragraph(); p.paragraph_format.left_indent = Cm(0.2); p.paragraph_format.space_after = Pt(4)
            runs(p, ["☐  "] + (it if isinstance(it, list) else [it]))

    def box(self, lines, fill=PAPER, title=None):
        t = self.d.add_table(rows=1, cols=1); no_borders(t); t.alignment = WD_TABLE_ALIGNMENT.CENTER
        c = t.cell(0, 0); shade(c, fill); cell_margins(c, 180, 180, 240, 240)
        first = c.paragraphs[0]
        if title:
            runs(first, [(title, "b")], size=11.5); first.paragraph_format.space_after = Pt(4)
            first = None
        for i, ln in enumerate(lines):
            p = first if (i == 0 and first is not None) else c.add_paragraph()
            runs(p, ln if isinstance(ln, list) else [ln]); p.paragraph_format.space_after = Pt(3)
        for row in t.rows:
            row._tr.get_or_add_trPr().append(OxmlElement("w:cantSplit"))
        self.d.add_paragraph().paragraph_format.space_after = Pt(2)

    def id_box(self):
        t = self.d.add_table(rows=1, cols=1); no_borders(t)
        c = t.cell(0, 0); shade(c, TINT); cell_margins(c, 200, 200, 260, 260)
        p = c.paragraphs[0]; runs(p, ["Numéro d’identification Meta de Bartier & Co"], size=10, color=SOFT); p.paragraph_format.space_after = Pt(2)
        p = c.add_paragraph(); r = p.add_run(ID); r.bold = True; r.font.size = Pt(22); r.font.color.rgb = INK; r.font.name = "Consolas"
        p.paragraph_format.space_after = Pt(4)
        p = c.add_paragraph(); runs(p, ["16 chiffres. Ce n’est pas un mot de passe : il sert seulement à indiquer à Meta à qui vous donnez l’accès."], size=9.5, color=SOFT)
        self.d.add_paragraph().paragraph_format.space_after = Pt(2)

    def step(self, n, title, do, see=None, tip=None, img=None):
        """Une étape : grand numéro à gauche ; à droite, ce qu'il faut faire, ce qu'on doit voir, et le conseil si ça bloque."""
        t = self.d.add_table(rows=1, cols=2); no_borders(t)
        t.columns[0].width = Cm(1.6); t.columns[1].width = Cm(15)
        a, b = t.cell(0, 0), t.cell(0, 1)
        a.width, b.width = Cm(1.6), Cm(15)
        cell_margins(a, 60, 60, 0, 120); cell_margins(b, 60, 60, 120, 0)
        pa = a.paragraphs[0]; runs(pa, [(str(n), "b")], size=24, color=ACCENT)
        pb = b.paragraphs[0]; runs(pb, [(title, "b")], size=12.5); pb.paragraph_format.space_after = Pt(3)
        for ln in do:
            p = b.add_paragraph(); runs(p, ln if isinstance(ln, list) else [ln]); p.paragraph_format.space_after = Pt(3)
        if see:
            p = b.add_paragraph(); p.paragraph_format.space_after = Pt(3)
            runs(p, [("✓ Vous devez voir : ", "b")] + (see if isinstance(see, list) else [see]), size=10.5, color=SOFT)
        if tip:
            p = b.add_paragraph(); p.paragraph_format.space_after = Pt(3)
            runs(p, [("Si ça bloque : ", "b")] + (tip if isinstance(tip, list) else [tip]), size=10.5, color=SOFT)
        if img:
            f, w = img
            p = b.add_paragraph(); p.paragraph_format.space_before = Pt(4); p.paragraph_format.space_after = Pt(4)
            p.add_run().add_picture(str(CAP / f), width=Cm(w))
        # le tableau d'une étape ne se coupe pas entre deux pages
        for row in t.rows:
            trPr = row._tr.get_or_add_trPr(); cs = OxmlElement("w:cantSplit"); trPr.append(cs)
        sp = self.d.add_paragraph(); sp.paragraph_format.space_after = Pt(4)

    def figure(self, f, w, caption=None):
        p = self.d.add_paragraph(); p.paragraph_format.left_indent = Cm(0.8); p.paragraph_format.space_before = Pt(4)
        p.add_run().add_picture(str(CAP / f), width=Cm(w)); p.paragraph_format.keep_with_next = bool(caption)
        if caption:
            c = self.d.add_paragraph(); c.paragraph_format.left_indent = Cm(0.8)
            runs(c, [caption], size=9.5, color=SOFT)

    def save(self, name):
        out = HERE / name
        self.d.save(out)
        return out


# ——— Blocs communs aux deux guides ———
def intro(g, minutes, extra=None):
    lines = [[("Durée : ", "b"), minutes],
             [("Sur ordinateur : ", "b"), "l’espace professionnel de Meta est bien plus simple à utiliser sur un écran d’ordinateur que sur un téléphone."],
             [("Vous restez propriétaire de tout : ", "b"), "votre Page, votre compte publicitaire et votre budget restent à votre nom. Vous pouvez retirer notre accès à tout moment."],
             [("Nous ne vous demanderons jamais votre mot de passe.", "b")]]
    if extra:
        lines.append(extra)
    g.box(lines)


def video(g, what):
    g.para(("En vidéo : ", "b"), what + " ", ("lien", VIDEO, "voir la vidéo « Comment enregistrer l’ID de Bartier & Co sur Meta »"), ".")


def give_access_steps(g, first=1, from_scratch=False):
    """Les étapes de partage avec Bartier & Co (communes aux deux guides). Renvoie le numéro de la dernière étape."""
    n = first
    g.step(n, "Ouvrez la page « Partenaires » de votre espace professionnel",
           [["Dans votre navigateur, connecté à Facebook, ouvrez cette adresse : ", ("lien", PARTNERS, "business.facebook.com/settings/partners")],
            "Autre chemin : business.facebook.com, puis Paramètres (la roue dentée en bas à gauche), puis Utilisateurs › Partenaires."],
           img=("03-menu-partenaires.png", 6.5),
           see="la page « Partenaires » au nom de votre entreprise, avec un bouton bleu « Ajouter » en haut à droite.",
           tip=("Meta vous demande de choisir une entreprise : cliquez sur la vôtre." if from_scratch else
                ["Meta vous demande de choisir une entreprise : cliquez sur la vôtre. Meta vous propose de créer un portefeuille business : votre Page n’est pas encore rattachée à un espace professionnel. Suivez d’abord l’",
                 ("annexe A", "b"), ", à la fin de ce guide, puis revenez ici."]))
    n += 1
    g.step(n, "Cliquez sur le bouton bleu « Ajouter »", ["Il est en haut à droite de la page. Un petit menu s’ouvre."])
    n += 1
    g.step(n, "Choisissez « Donner à un partenaire l’accès à vos actifs »",
           ["C’est en général la première ligne du menu. Selon votre écran, le mot « actifs » peut être remplacé par « ressources »."],
           tip="ne choisissez pas « Demander à un partenaire de partager ses actifs » : ce choix fait l’inverse.")
    n += 1
    g.step(n, "Collez le numéro de Bartier & Co, puis « Suivant »",
           [["Copiez-collez ce numéro dans le champ : ", (ID, "b")]],
           see="l’écran suivant, qui vous propose vos actifs : Pages, comptes publicitaires, Instagram.",
           tip="Meta indique que le numéro est introuvable : vérifiez-le chiffre par chiffre (16 chiffres, sans espace).")
    n += 1
    g.step(n, "Cochez vos actifs et activez « Contrôle total »",
           ["Pour chaque ligne ci-dessous, cochez la case, puis activez « Contrôle total » :",
            [("Votre Page Facebook", "b"), " (celle de votre entreprise)"],
            [("Votre compte publicitaire", "b"), (" (celui que vous venez de créer)" if from_scratch else " (s’il n’existe pas encore, voyez l’annexe B ou passez : nous le créerons ensemble)")],
            [("Votre compte Instagram", "b"), " si vous en avez un"],
            [("Votre ensemble de données (pixel)", "b"), " s’il apparaît dans la liste"],
            [("Pourquoi « Contrôle total » ? ", "b"), "Pour que nous puissions créer, régler et suivre vos annonces sans vous redemander une autorisation à chaque étape. Vous restez propriétaire, et vous pouvez retirer l’accès quand vous voulez."]])
    n += 1
    g.step(n, "Cliquez sur « Enregistrer »",
           ["Selon votre écran, le bouton peut s’appeler « Attribuer » ou « Confirmer »."],
           see="un message de confirmation, puis Bartier & Co dans la liste de vos partenaires.")
    n += 1
    g.step(n, "Prévenez-nous : écrivez « C’est fait »",
           [["Sur WhatsApp ou par SMS au ", (TEL_TXT, "b"), ". ", ("lien", WA, "Ouvrir WhatsApp")],
            "Nous vérifions de notre côté que tout est bien arrivé, et nous vous rappelons si un réglage manque."])
    return n


def blocages(g, extra=()):
    g.h1("Si quelque chose bloque")
    items = [[("« Je ne vois pas le bouton Ajouter. » ", "b"), "Vous n’avez sans doute pas l’accès complet à l’espace professionnel. Demandez à la personne qui l’a créé de vous donner le contrôle total, ou de faire ces étapes elle-même."],
             [("« Ma Page n’apparaît pas dans la liste. » ", "b"), "Elle n’est pas encore rattachée à votre espace professionnel. Allez dans Paramètres › Comptes › Pages › Ajouter › « Ajouter une Page existante », tapez son nom, puis recommencez au début."],
             [("« Meta me demande un code ou une vérification. » ", "b"), "C’est normal : Meta protège les comptes professionnels. Suivez ses instructions (code reçu par SMS ou par e-mail)."],
             [("« J’ai coché la mauvaise chose. » ", "b"), "Rien de grave : vous pouvez tout retirer et recommencer (voir « Retirer l’accès », plus bas)."]]
    items += list(extra)
    g.bullets(items)
    g.box([[("Le plus simple si vous êtes bloqué : ", "b"), f"appelez-nous au {TEL_TXT}. Nous faisons les étapes avec vous au téléphone, écran par écran. Comptez un quart d’heure."]], fill=TINT)


def retirer(g):
    g.h1("Retirer l’accès plus tard")
    g.para("Vous gardez la main à tout moment. Pour retirer l’accès de Bartier & Co :")
    g.bullets(["Ouvrez business.facebook.com/settings/partners.", "Cliquez sur Bartier & Co.", "Retirez les actifs un par un, ou supprimez le partenaire en entier."], style="List Number")
    g.para("Vos annonces, votre Page et votre historique restent à vous.", color=SOFT, size=10.5)


def annexe_portefeuille(g, title, new_page=True):
    g.h1(title, new_page=new_page)
    g.para("Le portefeuille business est l’espace professionnel gratuit de Meta. Il regroupe votre Page, votre compte publicitaire et les personnes qui y ont accès. Il faut un profil Facebook pour le créer.")
    g.bullets([["Ouvrez ", ("lien", "https://business.facebook.com", "business.facebook.com"), ". Si Meta vous demande de vous connecter, cliquez sur « Continuer avec Facebook » (encadré en bleu ci-dessous)."],
               "Cliquez sur « Créer un compte » ou « Créer un portefeuille business ».",
               "Indiquez le nom de votre entreprise (tel qu’il figure sur vos devis), votre nom et votre e-mail professionnel. Validez.",
               "Ouvrez l’e-mail de confirmation envoyé par Meta et cliquez sur le lien.",
               "Rattachez votre Page : Paramètres › Comptes › Pages › Ajouter › « Ajouter une Page existante ». Tapez le nom de votre Page et validez."], style="List Number")
    g.figure("02-business-continuer-avec-facebook.png", 7.5, "Étape 1 : l’écran de connexion aux outils professionnels de Meta.")
    g.figure("04-menu-pages.png", 6.5, "Étape 5 : dans le menu des Paramètres, Comptes › Pages.")
    g.para(("✓ Vous devez voir : ", "b"), "votre Page dans la liste « Pages » de votre portefeuille.", size=10.5, color=SOFT)


def annexe_compte_pub(g, title, new_page=False):
    g.h1(title, new_page=new_page)
    g.para("Le compte publicitaire est le compte qui paie vos annonces. Il est à votre nom, et le budget est payé directement à Meta avec votre carte : Bartier & Co ne touche pas à cet argent.")
    g.bullets(["Dans votre portefeuille : Paramètres › Comptes › Comptes publicitaires (ci-dessous) › Ajouter › « Créer un compte publicitaire ».",
               "Nom du compte : le nom de votre entreprise.",
               [("Fuseau horaire : ", "b"), "(GMT+01:00) Paris. ", ("Devise : ", "b"), "euro (EUR)."],
               "Indiquez que le compte est utilisé pour votre propre entreprise.",
               "Ajoutez-vous comme personne, avec le contrôle total.",
               "Ajoutez votre carte bancaire professionnelle : dans le compte publicitaire, rubrique « Moyens de paiement » (ou « Facturation et paiements »)."], style="List Number")
    g.figure("05-menu-comptes-publicitaires.png", 6.5, "Étape 1 : dans le menu des Paramètres, Comptes › Comptes publicitaires.")
    g.box([[("Attention : ", "b"), "le fuseau horaire et la devise ne peuvent plus être modifiés une fois le compte créé. Vérifiez-les bien avant de valider."]])


# ——— Guide 1 : le client a Facebook ———
def guide_1():
    g = Guide()
    g.logo()
    g.title("Donner l’accès Meta à Bartier & Co", "Guide 1 : vous avez déjà Facebook et une Page pour votre entreprise")
    g.para("Pour créer et suivre vos publicités sur Facebook et Instagram, nous avons besoin d’un accès à votre Page et à votre compte publicitaire. "
           "Vous allez simplement ajouter Bartier & Co comme « partenaire » dans votre espace professionnel Meta. Ce guide vous accompagne clic par clic.")
    intro(g, "5 à 10 minutes.")
    g.id_box()
    video(g, "toutes les étapes sont montrées à l’écran.")
    g.h1("Avant de commencer : 3 vérifications")
    g.checks(["Vous êtes connecté à Facebook avec votre profil personnel, celui qui gère la Page de votre entreprise.",
              "Vous savez quelle Page partager, si vous en avez plusieurs.",
              "Vous avez ce guide ouvert à côté, ou imprimé."])
    g.h1("Les étapes", new_page=True)
    give_access_steps(g)
    blocages(g, extra=[[("« Je n’ai pas de compte publicitaire. » ", "b"), "Pas de souci : suivez l’annexe B, ou partagez seulement votre Page et nous créerons le compte avec vous au téléphone."]])
    retirer(g)
    annexe_portefeuille(g, "Annexe A : je n’ai pas encore de portefeuille business")
    g.para("Ensuite, revenez à l’étape 1 du guide.")
    annexe_compte_pub(g, "Annexe B : je n’ai pas encore de compte publicitaire")
    g.para("Ensuite, revenez à l’étape 1 du guide et cochez aussi ce compte publicitaire à l’étape 5.")
    return g.save("Guide accès Meta 1 - Vous avez déjà Facebook - Bartier & Co.docx")


# ——— Guide 2 : le client n'a pas Facebook ———
def guide_2():
    g = Guide()
    g.logo()
    g.title("Créer votre présence Meta et donner l’accès à Bartier & Co", "Guide 2 : vous n’avez pas encore Facebook")
    g.para("Pour diffuser vos publicités sur Facebook et Instagram, votre entreprise a besoin de quatre choses à son nom : un profil Facebook, une Page, un espace professionnel Meta et un compte publicitaire. "
           "Ce guide vous fait tout créer dans l’ordre, puis donner l’accès à Bartier & Co. Prenez-le partie par partie : vous pouvez faire une pause entre deux parties.")
    intro(g, "30 à 40 minutes au total, en 6 parties.",
          extra=[("Vous préférez le faire avec nous ? ", "b"), f"Appelez-nous au {TEL_TXT} : nous le faisons ensemble au téléphone, écran par écran."])
    g.h1("Le parcours en un coup d’œil")
    tbl = g.d.add_table(rows=1, cols=3); tbl.style = "Table Grid"; tbl.autofit = False
    hdr = tbl.rows[0].cells
    for c, t in zip(hdr, ("Partie", "Ce que vous créez", "Durée")):
        shade(c, PAPER); runs(c.paragraphs[0], [(t, "b")], size=10.5)
    for row in (("1", "Votre profil Facebook personnel", "10 min"), ("2", "La Page Facebook de votre entreprise", "10 min"),
                ("3", "Votre espace professionnel Meta (portefeuille business)", "5 min"), ("4", "Votre compte publicitaire", "5 min"),
                ("5", "L’accès pour Bartier & Co", "5 min"), ("6", "Nous prévenir", "1 min")):
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
              "Votre téléphone portable : Meta envoie des codes de confirmation par SMS.",
              "Le logo de votre entreprise, et une belle photo de chantier ou de votre équipe.",
              "Vos coordonnées : téléphone, adresse ou zone d’intervention, horaires.",
              "Une carte bancaire professionnelle, pour le budget de vos publicités (partie 4).",
              "Ce guide ouvert à côté, ou imprimé."])

    # Partie 1
    g.h1("Partie 1 : créer votre profil Facebook")
    g.box([[("Pourquoi un profil personnel ? ", "b"), "Meta exige qu’une vraie personne soit derrière chaque Page. Votre profil peut rester discret : vos clients voient la Page de votre entreprise, et vous n’avez rien à publier sur votre profil."]])
    g.step(1, "Ouvrez le formulaire d’inscription", [["Sur ordinateur, ouvrez ", ("lien", "https://www.facebook.com/r.php", "facebook.com/r.php"), " : le formulaire s’ouvre directement. Il est intitulé « Démarrez sur Facebook à l’aide d’un compte Meta »."]])
    g.step(2, "Remplissez le formulaire",
           ["Dans l’ordre : votre vrai prénom et votre vrai nom (Meta peut demander de les vérifier plus tard), votre date de naissance, votre genre, votre numéro de portable ou votre e-mail professionnel, et un mot de passe solide. Cliquez ensuite sur le bouton bleu « Envoyer », en bas du formulaire."],
           img=("01-inscription-facebook.png", 7.5),
           tip="Meta refuse le formulaire : utilisez votre vrai nom, pas celui de l’entreprise. Le nom de l’entreprise servira pour la Page.")
    g.step(3, "Confirmez avec le code reçu", ["Meta vous envoie un code par e-mail ou par SMS. Tapez-le dans la fenêtre qui s’affiche."],
           see="votre fil Facebook, encore presque vide.")
    g.step(4, "Protégez votre compte (fortement conseillé)",
           ["Menu en haut à droite › Paramètres et confidentialité › Paramètres › Espace Comptes › Mot de passe et sécurité › Authentification à deux facteurs. Choisissez « SMS » ou une application d’authentification.",
            "Un compte professionnel piraté peut bloquer vos publicités et votre Page : ces deux minutes vous protègent."])
    g.box([[("À retenir : ", "b"), "notez votre mot de passe dans un endroit sûr. Ne le donnez à personne, pas même à nous : nous n’en aurons jamais besoin."]])

    # Partie 2
    g.h1("Partie 2 : créer la Page de votre entreprise", new_page=True)
    g.step(1, "Lancez la création de la Page",
           [["Ouvrez ", ("lien", "https://www.facebook.com/pages/create", "facebook.com/pages/create"), ". Autre chemin : le menu de Facebook › Pages › « Créer une Page »."]])
    g.step(2, "Donnez le nom de votre entreprise", ["Écrivez-le exactement comme sur vos devis et votre camion, pour que vos clients vous reconnaissent."])
    g.step(3, "Choisissez la catégorie",
           ["Tapez votre métier (couvreur, menuisier, façadier, charpentier, isolation…) et choisissez la proposition la plus proche. Vous pouvez en ajouter jusqu’à trois."])
    g.step(4, "Écrivez une courte présentation",
           ["Une ou deux phrases : votre métier, votre zone et ce que vous faites. Par exemple : « Couvreur à Lyon et alentours. Rénovation de toiture, réparation de fuites, zinguerie. Devis gratuit. »"])
    g.step(5, "Cliquez sur « Créer la Page »", [], see="votre nouvelle Page, encore sans photo.")
    g.step(6, "Ajoutez vos coordonnées",
           ["Téléphone, e-mail, adresse ou zone d’intervention, horaires et site internet si vous en avez un. Ces informations rassurent vos futurs clients."])
    g.step(7, "Ajoutez vos photos",
           ["Photo de profil : votre logo. Photo de couverture : un beau chantier terminé ou votre équipe. Évitez les images trouvées sur internet."],
           see="votre Page avec votre logo et votre photo de couverture.",
           tip="Facebook vous « fait basculer » sur la Page : c’est normal. Pour revenir à votre profil, cliquez sur votre photo en haut à droite.")

    # Partie 3
    annexe_portefeuille(g, "Partie 3 : créer votre espace professionnel Meta")
    g.para("Si la création vous propose directement d’ajouter votre nouvelle Page, acceptez : la dernière étape est alors déjà faite.", color=SOFT, size=10.5)

    # Partie 4
    annexe_compte_pub(g, "Partie 4 : créer votre compte publicitaire", new_page=True)

    # Partie 5
    g.h1("Partie 5 : donner l’accès à Bartier & Co", new_page=True)
    g.para("Dernière partie, la plus courte. Vous allez ajouter Bartier & Co comme « partenaire » dans votre espace professionnel.")
    g.id_box()
    video(g, "cette partie est montrée à l’écran, étape par étape.")
    give_access_steps(g, from_scratch=True)
    g.box([[("C’est terminé. ", "b"), "Votre entreprise a maintenant sa Page, son espace professionnel et son compte publicitaire, tous à votre nom. Nous nous occupons de la suite."]], fill=TINT)

    blocages(g, extra=[[("« Facebook a bloqué mon nouveau compte. » ", "b"), "Cela arrive parfois avec les comptes tout neufs. Suivez les instructions de Facebook pour confirmer votre identité, puis appelez-nous : nous reprenons avec vous là où vous en étiez."]])
    retirer(g)
    return g.save("Guide accès Meta 2 - Vous n'avez pas encore Facebook - Bartier & Co.docx")


if __name__ == "__main__":
    for f in (guide_1(), guide_2()):
        print(f)

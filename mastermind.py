'''
______     _              ___  ___          _                      _           _
| ___ \   | |             |  \/  |         | |                    (_)         | |
| |_/ /___| |_ _ __ ___   | .  . | __ _ ___| |_ ___ _ __ _ __ ___  _ _ __   __| |
|    // _ \ __| '__/ _ \  | |\/| |/ _` / __| __/ _ \ '__| '_ ` _ \| | '_ \ / _` |
| |\ \  __/ |_| | | (_) | | |  | | (_| \__ \ ||  __/ |  | | | | | | | | | | (_| |
\_| \_\___|\__|_|  \___/  \_|  |_/\__,_|___/\__\___|_|  |_| |_| |_|_|_| |_|\__,_|

Projet réalisé en ISN par Paul-Louis Charrière dans le cadre du projet à rendre au baccalauréat.

'''

# -------------------------------------------------------------- Importation des librairies  ----------------------------------------------------------- #

# La librairie pyglet est utilisée pour jouer les effets sonores sur les boutons et quand on gagne ou perd une partie
# Ces effets sonores sont seulement pour l'ambiance sonore et n'impactent pas le gameplay

# Si pyglet est installé, changer la valeur de cette variable en True
ACTIVER_EFFETS_SONORES = True

from tkinter import *
from tkinter import messagebox
#import winsound
import random
import os
import os.path
import sys

if ACTIVER_EFFETS_SONORES:
    import pyglet

# ----------------------------------------------------------- Déclaration des fonctions du programme ----------------------------------------------------------- #

###########################################################################################
#                      Fonctions gérant les sons du programme                             #
###########################################################################################

def JouerMusiqueDeFond():
    # On définie dans cette variable globale :
    # True : la musique est en train d'être jouée
    # False : la musique n'est pas en train d'être jouée
    global musique_en_cours
    musique_en_cours = True

    # On joue une musique au hasard                                                                 Ce sont des drapeaux permettant de donner des paramètres à la fonction
    #winsound.PlaySound('ressources/sons/musiques/musique_1.wav', winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_LOOP)
    # winsound.SND_FILENAME : on joue une musique à partir d'un fichier
    # winsound.SND_ASYNC : la musique est jouée en paralèlle au programme
    # winsound.SND_LOOP : la musique est jouée en boucle

def StopperMusiqueDeFond():

    # Permet d'arrêter la musique
    winsound.PlaySound(None, winsound.SND_PURGE),

    # On change la variable globale pour indiquer que la musique n'est plus en train d'être jouée
    global musique_en_cours
    musique_en_cours = False

# On appelle cette fonction quand la souris survole un bouton
# Elle permet de jouer un son
def BoutonSurvole(event = False):
    if ACTIVER_EFFETS_SONORES == True :
        # pyglet.media.load permet de charger un fichier son dans une variable
        son = pyglet.media.load('ressources/sons/sfx/bouton_survole.wav')
        # permet de jouer le son chargé dans la variable
        son.play()

# On appelle cette fonction quand on clique sur un bouton
def BoutonClick(event = False):
    if ACTIVER_EFFETS_SONORES == True :
        son = pyglet.media.load('ressources/sons/sfx/bouton_click.wav')
        son.play()

# Cette fonction permet d'alterner la musique quand on l'appelle
# Elle est appelée quand on clique sur un bouton permettant d'arrêter ou de lancer la musique
def BoutonMusiqueClick(event):
    # Si la musique est en train d'être jouée, on l'arrête sinon on la lance
    # On change l'image du bouton permettant d'alterner la musique indiquant l'état de la musique

    if musique_en_cours == True:
        StopperMusiqueDeFond()
        canevas.itemconfigure(bouton_musique, image=fichiers["menu_musique_off_btn"], activeimage=fichiers["menu_musique_off_btn_hover"])
    else:
        JouerMusiqueDeFond()
        canevas.itemconfigure(bouton_musique, image=fichiers["menu_musique_on_btn"], activeimage=fichiers["menu_musique_on_btn_hover"])



###########################################################################################
#                     Fonctions gérant les fichiers du programme                          #
###########################################################################################

# Cette fonction charge les fichiers images et sons requis pour l'interface graphique du jeu
# si un fichier est manqué, la fonction arrête le programme et affiche un message d'erreur
def ChargerFichiers():

    # On stockera les fichiers chargés dans cette liste globale
    global fichiers
    fichiers = {}

    try: # On execute le code pour charger les fichiers dans le bloc try, si un erreur intervient, le code dans le bloc except est exécuté

        # Le mot 'btn' signifie bouton
        # Le mot 'hover' signifie que l'on survole l'image avec la souris
        # La fonction PhotoImage permet de charger un fichier image
        # png est un format d'image (Portable Network Graphics)

        # Chargement des images d'intro
        fichiers["intro"] =  PhotoImage(file="ressources/images/ecrans/introduction/intro.png", format="png")

        # Chargements des fonds d'écran du jeu
        # On séléctionne un fond au hasard parmit les 2 fichiers fond_1.png et fond_2.png
        fichiers["fond"] = PhotoImage(file="ressources/images/fonds/fond_" + str(random.randint(1, 4)) + ".png", format="png")

        # Chargement des fichiers pour l'écran du menu
        # btn = bouton
        fichiers["menu_logo"] = PhotoImage(file="ressources/images/ecrans/menu/retro_mastermind_logo.png", format="png")

        fichiers["menu_jouer_btn"] = PhotoImage(file="ressources/images/ecrans/menu/jouer_btn.png", format="png")
        fichiers["menu_jouer_btn_hover"] = PhotoImage(file="ressources/images/ecrans/menu/jouer_btn_hover.png", format="png")

        fichiers["menu_credits_btn"] = PhotoImage(file="ressources/images/ecrans/menu/credits_btn.png", format="png")
        fichiers["menu_credits_btn_hover"] = PhotoImage(file="ressources/images/ecrans/menu/credits_btn_hover.png", format="png")

        fichiers["menu_quitter_btn"] = PhotoImage(file="ressources/images/ecrans/menu/quitter_btn.png", format="png")
        fichiers["menu_quitter_btn_hover"] = PhotoImage(file="ressources/images/ecrans/menu/quitter_btn_hover.png", format="png")

        fichiers["menu_musique_on_btn"] = PhotoImage(file="ressources/images/ecrans/menu/musique_on_btn.png", format="png")
        fichiers["menu_musique_on_btn_hover"] = PhotoImage(file="ressources/images/ecrans/menu/musique_on_btn_hover.png", format="png")
        fichiers["menu_musique_off_btn"] = PhotoImage(file="ressources/images/ecrans/menu/musique_off_btn.png", format="png")
        fichiers["menu_musique_off_btn_hover"] = PhotoImage(file="ressources/images/ecrans/menu/musique_off_btn_hover.png", format="png")

        # Chargement des fichiers pour l'écran des crédits
        fichiers["credits_txt"] = PhotoImage(file="ressources/images/ecrans/credits/credits_txt.png", format="png")

        fichiers["credits_retour_btn"] = PhotoImage(file="ressources/images/ecrans/credits/retour_btn.png", format="png")
        fichiers["credits_retour_btn_hover"] = PhotoImage(file="ressources/images/ecrans/credits/retour_btn_hover.png", format="png")

        # Chargement des fichiers de l'écran de jeu
        fichiers["jeu_grille"] = PhotoImage(file="ressources/images/ecrans/jeu/grille.png", format="png")
        fichiers["jeu_grille_bandeau_ligne"] = PhotoImage(file="ressources/images/ecrans/jeu/grille_bandeau_ligne.png", format="png")
        fichiers["jeu_fond_grille"] = PhotoImage(file="ressources/images/ecrans/jeu/fond_grille.png", format="png")

        fichiers["jeu_menu_btn"] = PhotoImage(file="ressources/images/ecrans/jeu/menu_btn.png", format="png")
        fichiers["jeu_menu_btn_hover"] = PhotoImage(file="ressources/images/ecrans/jeu/menu_btn_hover.png", format="png")

        fichiers["jeu_regles_btn"] = PhotoImage(file="ressources/images/ecrans/jeu/regles_btn.png", format="png")
        fichiers["jeu_regles_btn_hover"] = PhotoImage(file="ressources/images/ecrans/jeu/regles_btn_hover.png", format="png")

        fichiers["jeu_rejouer_btn"] = PhotoImage(file="ressources/images/ecrans/jeu/rejouer_btn.png", format="png")
        fichiers["jeu_rejouer_btn_hover"] = PhotoImage(file="ressources/images/ecrans/jeu/rejouer_btn_hover.png", format="png")

        fichiers["jeu_pion_bleu_40x40"] = PhotoImage(file="ressources/images/ecrans/jeu/pions/pion_bleu_40x40.png", format="png")
        fichiers["jeu_pion_bleu_50x50"] = PhotoImage(file="ressources/images/ecrans/jeu/pions/pion_bleu_50x50.png", format="png")
        fichiers["jeu_pion_bleu_50x50_hover"] = PhotoImage(file="ressources/images/ecrans/jeu/pions/pion_bleu_50x50_hover.png", format="png")

        fichiers["jeu_pion_jaune_40x40"] = PhotoImage(file="ressources/images/ecrans/jeu/pions/pion_jaune_40x40.png", format="png")
        fichiers["jeu_pion_jaune_50x50"] = PhotoImage(file="ressources/images/ecrans/jeu/pions/pion_jaune_50x50.png", format="png")
        fichiers["jeu_pion_jaune_50x50_hover"] = PhotoImage(file="ressources/images/ecrans/jeu/pions/pion_jaune_50x50_hover.png", format="png")

        fichiers["jeu_pion_rouge_40x40"] = PhotoImage(file="ressources/images/ecrans/jeu/pions/pion_rouge_40x40.png", format="png")
        fichiers["jeu_pion_rouge_50x50"] = PhotoImage(file="ressources/images/ecrans/jeu/pions/pion_rouge_50x50.png", format="png")
        fichiers["jeu_pion_rouge_50x50_hover"] = PhotoImage(file="ressources/images/ecrans/jeu/pions/pion_rouge_50x50_hover.png", format="png")

        fichiers["jeu_pion_vert_40x40"] = PhotoImage(file="ressources/images/ecrans/jeu/pions/pion_vert_40x40.png", format="png")
        fichiers["jeu_pion_vert_50x50"] = PhotoImage(file="ressources/images/ecrans/jeu/pions/pion_vert_50x50.png", format="png")
        fichiers["jeu_pion_vert_50x50_hover"] = PhotoImage(file="ressources/images/ecrans/jeu/pions/pion_vert_50x50_hover.png", format="png")

        fichiers["jeu_pion_emplacement"] = PhotoImage(file="ressources/images/ecrans/jeu/pions/emplacement.png", format="png")
        fichiers["jeu_pion_emplacement_opaque"] = PhotoImage(file="ressources/images/ecrans/jeu/pions/emplacement_opaque.png", format="png")
        fichiers["jeu_pion_emplacement_languette"] = PhotoImage(file="ressources/images/ecrans/jeu/pions/emplacement_languette.png", format="png")
        fichiers["jeu_pion_emplacement_languette_opaque"] = PhotoImage(file="ressources/images/ecrans/jeu/pions/emplacement_languette_opaque.png", format="png")

        fichiers["jeu_languette_rouge"] = PhotoImage(file="ressources/images/ecrans/jeu/pions/languette_rouge.png", format="png")
        fichiers["jeu_languette_blanche"] = PhotoImage(file="ressources/images/ecrans/jeu/pions/languette_blanche.png", format="png")

        fichiers["jeu_bandeau_gagne"] = PhotoImage(file="ressources/images/ecrans/jeu/bandeau_gagne.png", format="png")
        fichiers["jeu_bandeau_perdu"] = PhotoImage(file="ressources/images/ecrans/jeu/bandeau_perdu.png", format="png")

        # Chargement des fichiers pour l'écran des règles
        fichiers["regles_txt"] = PhotoImage(file="ressources/images/ecrans/regles/regles_txt.png", format="png")

        fichiers["regles_retour_btn"] = PhotoImage(file="ressources/images/ecrans/regles/retour_btn.png", format="png")
        fichiers["regles_retour_btn_hover"] = PhotoImage(file="ressources/images/ecrans/regles/retour_btn_hover.png", format="png")

    except Exception as e:
        # Une erreur est intervenue, on affiche un message d'erreur et on quitte le programme
        # on stocke l'erreur dans la variable e

        # messagebox est une librairie permettant d'afficher des boites de messages sur Windows
        # showerror permet d'afficher une boite de message d'erreur de Windows, cependant il existe d'autres fonctions permettant d'afficher différents types de boites de messages
        # showerror étant une méthode de la librairie messagebox, on y accède par messagebox.showerror(titre, cors du message)
        messagebox.showerror("Erreur lors du chargement des fichiers", "Une erreur est survenue lors du chargement des ressources du jeu, il est possible qu'un ou plusieurs fichiers soient manquant.")
        # On affiche l'erreur dans la console
        print(str(e))
        # exit() permet de quitter le programme
        exit()






###########################################################################################
#                    Fonctions dessinant les écrans du programme                          #
###########################################################################################


# ------------------- Fonction dessinant l'écran d'introduction ------------------- #

def DessinerIntroduction():
    # On considère que cette fonction est appellée uniquement au début du programme
    # Il n'y a donc pas besoin d'effacer le canevas

    # On crée l'image de l'introduction dans le canevas
    introductionImage = canevas.create_image((0, 0), image=fichiers["intro"], anchor='nw')

    # On associe l'action du clic gauche sur l'image d'introduction à la fonction de dessiner le menu
    canevas.tag_bind(introductionImage, '<ButtonPress-1>', DessinerMenu)

# --------------------------------------------------------------------------------- #




# ------------------------------------------------ Fonction dessinant l'écran du menu ------------------------------------------------------------ #
def DessinerMenu(event = False):
    # On supprime tout ce qu'il y a dans le canevas (l'introduction par exemple) pour pouvoir dessiner le menu
    canevas.delete("all")

    # On ajoute le fond
    canevas.create_image((0, 0), image=fichiers["fond"], anchor='nw')

    # On ajoute le logo du jeu et les boutons
    canevas.create_image(400, 150, image=fichiers["menu_logo"], anchor='center')
    # On associe l'image à une variable pour pouvoir lui attribuer des évènements comme un clic gauche dessus
    bouton_jouer = canevas.create_image(400, 320, image=fichiers["menu_jouer_btn"], activeimage=fichiers["menu_jouer_btn_hover"], anchor='center')
    bouton_credits = canevas.create_image(400, 420, image=fichiers["menu_credits_btn"], activeimage=fichiers["menu_credits_btn_hover"], anchor='center')
    bouton_quitter = canevas.create_image(400, 500, image=fichiers["menu_quitter_btn"], activeimage=fichiers["menu_quitter_btn_hover"], anchor='center')

    # Si la musique est en train d'être jouée, on affiche le bouton avec une image du bouton indiquant que la musique est "ON" sinon "OFF"
    # On définit le bouton comme global pour pouvoir changer son image à l'aide de la fonction BoutonMusiqueClick
    global bouton_musique
    if musique_en_cours == True:
        bouton_musique = canevas.create_image(700, 50, image=fichiers["menu_musique_on_btn"], activeimage=fichiers["menu_musique_on_btn_hover"], anchor='center')
    else:
        bouton_musique = canevas.create_image(700, 50, image=fichiers["menu_musique_off_btn"], activeimage=fichiers["menu_musique_off_btn_hover"], anchor='center')

    # Ici, on associe le clique gauche sur les images à des fonction
    # <ButtonPress-1> signifie l'évènement du clic gauche
    canevas.tag_bind(bouton_jouer, '<ButtonPress-1>', MenuJouerClick)
    canevas.tag_bind(bouton_credits, '<ButtonPress-1>', MenuCreditsClick)
    canevas.tag_bind(bouton_quitter, '<ButtonPress-1>', MenuQuitterClick)
    canevas.tag_bind(bouton_musique, '<ButtonPress-1>', BoutonMusiqueClick)

    # <Enter> signifie que la souris survole l'image
    # On appelle donc la fonction BoutonSurvole pour que le son d'une image survolée soit joué
    canevas.tag_bind(bouton_jouer, '<Enter>', BoutonSurvole)
    canevas.tag_bind(bouton_quitter, '<Enter>', BoutonSurvole)
    canevas.tag_bind(bouton_credits, '<Enter>', BoutonSurvole)
    canevas.tag_bind(bouton_musique, '<Enter>', BoutonSurvole)

    canevas.update()
    return

# Le bouton jouer du menu a été cliquée
def MenuJouerClick(event):
    # On joue le son du bouton cliqué
    BoutonClick()
    # On lance la fonction permettant de démarrer une nouvelle partie
    NouvellePartie()

# Le bouton quitter du menu a été cliquée
def MenuQuitterClick(event):
    # On joue le son du bouton cliqué
    BoutonClick()
    # On quitte le programme
    quit()

# Le bouton crédits du menu a été cliquée
def MenuCreditsClick(event):
    # On joue le son du bouton cliqué
    BoutonClick()
    # On dessine l'écran des crédits
    DessinerCredits()

# -------------------------------------------------------------------------------------------------------------------------------------------------------- #



# ------------------------------------------------ Fonction dessinant l'écran des crédits ---------------------------------------------------------------- #
def DessinerCredits():
    # On supprime tout ce qu'il y a dans le canevas (le menu par exemple) pour pouvoir l'écran des crédits
    canevas.delete("all")

    # On ajoute le fond
    canevas.create_image((0, 0), image=fichiers["fond"], anchor='nw')

    # On ajoute l'image du texte de l'écran des crédits
    canevas.create_image((0, -10), image=fichiers["credits_txt"], anchor='nw')

    bouton_retour = canevas.create_image(400, 540, image=fichiers["credits_retour_btn"], activeimage=fichiers["credits_retour_btn_hover"], anchor='center')

    canevas.tag_bind(bouton_retour, '<ButtonPress-1>', CreditsBoutonRetourClick)
    canevas.tag_bind(bouton_retour, '<Enter>', BoutonSurvole)

def CreditsBoutonRetourClick(event):
    # On joue le son du bouton cliqué
    BoutonClick()
    # On retourne au menu, on le redessine
    DessinerMenu()

# -------------------------------------------------------------------------------------------------------------------------------------------------------- #


# ------------------------------------------------ Fonction dessinant l'écran des règles ---------------------------------------------------------------- #
def DessinerRegles():
    # On supprime tout ce qu'il y a dans le canevas (le menu par exemple) pour pouvoir l'écran des règles
    canevas.delete("all")

    # On ajoute le fond
    canevas.create_image((0, 0), image=fichiers["fond"], anchor='nw')

    # On ajoute l'image du texte de l'écran des règles
    canevas.create_image((0, 0), image=fichiers["regles_txt"], anchor='nw')

    # On crée un bouton retour
    bouton_retour = canevas.create_image(400, 520, image=fichiers["regles_retour_btn"], activeimage=fichiers["regles_retour_btn_hover"], anchor='center')

    # On associe le clic gauche sur le l'image du bouton à la fonction du retour
    canevas.tag_bind(bouton_retour, '<ButtonPress-1>', ReglesBoutonRetourClick)
    canevas.tag_bind(bouton_retour, '<Enter>', BoutonSurvole)

def ReglesBoutonRetourClick(event):
    # On joue le son du bouton cliqué
    BoutonClick()
    # On retourne au menu, on le redessine
    DessinerJeu()

# -------------------------------------------------------------------------------------------------------------------------------------------------------- #


def NouvellePartie():
    global grille, grille_languettes, index_ligne_actuelle, ligne_aleatoire

    couleurs = ["rouge", "vert", "bleu", "jaune"]
    ligne_aleatoire = [random.choice(couleurs), random.choice(couleurs), random.choice(couleurs), random.choice(couleurs)]

    print(ligne_aleatoire)

    grille = []
    grille_languettes = []

    for i in range(10):
        ligne = []
        for j in range(4):
            emplacement = [51 + (59 * j), 46 + (52 * i), "vide"]
            ligne.append(emplacement)
        grille.append(ligne)


    for i in range(10):
        ligne = []
        for j in range(4):
            emplacement = [285 + (35 * j), 55 + (52 * i), "vide"]
            ligne.append(emplacement)
        grille_languettes.append(ligne)

    index_ligne_actuelle = len(grille) - 1

    DessinerJeu()

def DessinerJeu():
    canevas.delete("all")

    canevas.create_image((0, 0), image=fichiers["fond"], anchor='nw')

    canevas.create_image((0, 0), image=fichiers["jeu_fond_grille"], anchor='nw')

    global bandeau
    bandeau = canevas.create_image((23, 38 + (52 * index_ligne_actuelle)), image=fichiers["jeu_grille_bandeau_ligne"], anchor='nw')

    canevas.create_image((0, 0), image=fichiers["jeu_grille"], anchor='nw')

    # -------------- Menu des pions -------------- #

    pion_rouge_btn = canevas.create_image(520, 120, image=fichiers["jeu_pion_rouge_40x40"], activeimage=fichiers["jeu_pion_rouge_50x50_hover"], anchor='center')
    pion_bleu_btn = canevas.create_image(520, 120 * 2, image=fichiers["jeu_pion_bleu_40x40"], activeimage=fichiers["jeu_pion_bleu_50x50_hover"], anchor='center')
    pion_vert_btn = canevas.create_image(520, 120 * 3, image=fichiers["jeu_pion_vert_40x40"], activeimage=fichiers["jeu_pion_vert_50x50_hover"], anchor='center')
    pion_jaune_btn = canevas.create_image(520, 120 * 4, image=fichiers["jeu_pion_jaune_40x40"], activeimage=fichiers["jeu_pion_jaune_50x50_hover"], anchor='center')

    canevas.tag_bind(pion_rouge_btn, '<ButtonPress-1>', selectionnerRouge)
    canevas.tag_bind(pion_bleu_btn, '<ButtonPress-1>', selectionnerBleu)
    canevas.tag_bind(pion_vert_btn, '<ButtonPress-1>', selectionnerVert)
    canevas.tag_bind(pion_jaune_btn, '<ButtonPress-1>', selectionnerJaune)

    canevas.tag_bind(pion_rouge_btn, '<B1-Motion>', BougerPionActuel)
    canevas.tag_bind(pion_bleu_btn, '<B1-Motion>', BougerPionActuel)
    canevas.tag_bind(pion_vert_btn, '<B1-Motion>', BougerPionActuel)
    canevas.tag_bind(pion_jaune_btn, '<B1-Motion>', BougerPionActuel)

    canevas.tag_bind(pion_rouge_btn, '<ButtonRelease-1>', LacherPion)
    canevas.tag_bind(pion_bleu_btn, '<ButtonRelease-1>', LacherPion)
    canevas.tag_bind(pion_vert_btn, '<ButtonRelease-1>', LacherPion)
    canevas.tag_bind(pion_jaune_btn, '<ButtonRelease-1>', LacherPion)


    # ---------- Boutons ------------ #

    bouton_menu = canevas.create_image(690, 545, image=fichiers["jeu_menu_btn"], activeimage=fichiers["jeu_menu_btn_hover"], anchor='center')
    bouton_regles = canevas.create_image(690, 470, image=fichiers["jeu_regles_btn"], activeimage=fichiers["jeu_regles_btn_hover"], anchor='center')

    global bouton_musique
    if musique_en_cours == True:
        bouton_musique = canevas.create_image(700, 50, image=fichiers["menu_musique_on_btn"], activeimage=fichiers["menu_musique_on_btn_hover"], anchor='center')
    else:
        bouton_musique = canevas.create_image(700, 50, image=fichiers["menu_musique_off_btn"], activeimage=fichiers["menu_musique_off_btn_hover"], anchor='center')

    canevas.tag_bind(bouton_menu, '<ButtonPress-1>', JeuMenuBoutonClick)
    canevas.tag_bind(bouton_regles, '<ButtonPress-1>', JeuReglesBoutonClick)
    canevas.tag_bind(bouton_musique, '<ButtonPress-1>', BoutonMusiqueClick)

    canevas.tag_bind(bouton_menu, '<Enter>', BoutonSurvole)
    canevas.tag_bind(bouton_regles, '<Enter>', BoutonSurvole)
    canevas.tag_bind(bouton_musique, '<Enter>', BoutonSurvole)

    # ---------- Grille ----------- #

    for ligne in grille_languettes:
        for emplacement in ligne:
            if emplacement[2] == "vide":
                image = fichiers["jeu_pion_emplacement_languette_opaque"]
            else:
                image = fichiers["jeu_languette_" + emplacement[2]]
            canevas.create_image(emplacement[0], emplacement[1], image=image, anchor='nw')

    for emplacement in grille[index_ligne_actuelle]:
        canevas.create_image(emplacement[0], emplacement[1], image=fichiers["jeu_pion_emplacement"], anchor='nw')

    for ligne in grille:
        for emplacement in ligne:
            if emplacement[2] == "vide" and ligne != grille[index_ligne_actuelle]:
                image = fichiers["jeu_pion_emplacement_opaque"]
            else:
                image = fichiers["jeu_pion_" + emplacement[2] + "_40x40"]
            canevas.create_image(emplacement[0], emplacement[1], image=image, anchor='nw')

def JeuReglesBoutonClick(event):
    # On joue le son du bouton cliqué
    BoutonClick()
    # On retourne au menu, on le redessine
    DessinerRegles()

def JeuMenuBoutonClick(event):
    # On joue le son du bouton cliqué
    BoutonClick()
    # On demande ici une confirmation à l'utilisateur.
    # Si l'utilisateur clique sur OK, la variable quitter prend la valeur True, sinon False
    quitter = messagebox.askokcancel("Retourner au menu ?", "Êtes-vous sûr de vouloir retourner au menu ? La partie en cours sera perdue.")
    if quitter == True: # Si quitter vaut True (l'utilisateur a cliqué sur OK), on redessine le menu
        DessinerMenu()

def JeuFinMenuBoutonClick(event):
    # On joue le son du bouton cliqué
    BoutonClick()

    DessinerMenu()

def JeuFinRejouerBoutonClick(event):
    # On joue le son du bouton cliqué
    BoutonClick()
    # On demande ici une confirmation à l'utilisateur.
    # Si l'utilisateur clique sur OK, la variable quitter prend la valeur True, sinon False
    NouvellePartie()

# Ces fonctions crées un pion temporaire à l'emplacement de la souris lors d'un clic sur un pion dans la barre des pions
def selectionnerRouge(event):
    global pion_actuel, pion_actuel_couleur

    pion_actuel = canevas.create_image(event.x, event.y, image=fichiers["jeu_pion_rouge_40x40"], anchor='center')
    pion_actuel_couleur = "rouge"

def selectionnerBleu(event):
    global pion_actuel, pion_actuel_couleur

    pion_actuel = canevas.create_image(event.x, event.y, image=fichiers["jeu_pion_bleu_40x40"], anchor='center')
    pion_actuel_couleur = "bleu"

def selectionnerVert(event):
    global pion_actuel, pion_actuel_couleur

    pion_actuel = canevas.create_image(event.x, event.y, image=fichiers["jeu_pion_vert_40x40"], anchor='center')
    pion_actuel_couleur = "vert"

def selectionnerJaune(event):
    global pion_actuel, pion_actuel_couleur

    pion_actuel = canevas.create_image(event.x, event.y, image=fichiers["jeu_pion_jaune_40x40"], anchor='center')
    pion_actuel_couleur = "jaune"

def BougerPionActuel(event):
    global pion_actuel

    pion_actuel_position = canevas.coords(pion_actuel)
    canevas.move(pion_actuel, event.x - pion_actuel_position[0], event.y - pion_actuel_position[1])

# Le pion est lâché, on vérifie si les coordonnées du pion correspondent à un emplacement de pion valide
def LacherPion(event):
    global pion_actuel, index_ligne_actuelle, grille

    for emplacement in grille[index_ligne_actuelle]:
        if event.x > emplacement[0] and event.x < emplacement[0] + 40 and event.y > emplacement[1] and event.y < emplacement[1] + 40 :
            canevas.create_image(emplacement[0], emplacement[1], image=fichiers["jeu_pion_" + pion_actuel_couleur + "_40x40"], anchor='nw')
            emplacement[2] = pion_actuel_couleur

    ligne_complete = True
    for emplacement in grille[index_ligne_actuelle]:
        if emplacement[2] == "vide":
            ligne_complete = False

    if ligne_complete == True:
        ligne_actuelle = []
        for emplacement in grille[index_ligne_actuelle]:
            ligne_actuelle.append(emplacement[2])

        if ligne_actuelle == ligne_aleatoire:
            canevas.create_image(0, 0, image=fichiers["jeu_bandeau_gagne"], anchor='nw')
            bouton_rejouer = canevas.create_image(205, 340, image=fichiers["jeu_rejouer_btn"], activeimage=fichiers["jeu_rejouer_btn_hover"], anchor='nw')
            bouton_menu = canevas.create_image(405, 340, image=fichiers["jeu_menu_btn"], activeimage=fichiers["jeu_menu_btn_hover"], anchor='nw')

            canevas.tag_bind(bouton_rejouer, '<ButtonPress-1>', JeuFinRejouerBoutonClick)
            canevas.tag_bind(bouton_menu, '<ButtonPress-1>', JeuFinMenuBoutonClick)
            canevas.tag_bind(bouton_rejouer, '<Enter>', BoutonSurvole)
            canevas.tag_bind(bouton_menu, '<Enter>', BoutonSurvole)

            i = 0
            for couleur in ligne_aleatoire:
                canevas.create_image(400 + 50 * i, 290, image=fichiers["jeu_pion_" + couleur + "_40x40"], anchor='nw')
                i = i + 1

            if ACTIVER_EFFETS_SONORES == True :
                son = pyglet.media.load('ressources/sons/sfx/gagne.wav')
                son.play()
        else:
            if index_ligne_actuelle == 0:
                canevas.create_image(0, 0, image=fichiers["jeu_bandeau_perdu"], anchor='nw')
                bouton_rejouer = canevas.create_image(205, 340, image=fichiers["jeu_rejouer_btn"], activeimage=fichiers["jeu_rejouer_btn_hover"], anchor='nw')
                bouton_menu = canevas.create_image(405, 340, image=fichiers["jeu_menu_btn"], activeimage=fichiers["jeu_menu_btn_hover"], anchor='nw')

                canevas.tag_bind(bouton_rejouer, '<ButtonPress-1>', JeuFinRejouerBoutonClick)
                canevas.tag_bind(bouton_menu, '<ButtonPress-1>', JeuFinMenuBoutonClick)
                canevas.tag_bind(bouton_rejouer, '<Enter>', BoutonSurvole)
                canevas.tag_bind(bouton_menu, '<Enter>', BoutonSurvole)

                i = 0
                for couleur in ligne_aleatoire:
                    canevas.create_image(400 + 50 * i, 290, image=fichiers["jeu_pion_" + couleur + "_40x40"], anchor='nw')
                    i = i + 1

                if ACTIVER_EFFETS_SONORES == True :
                    son = pyglet.media.load('ressources/sons/sfx/perdu.wav')
                    son.play()
            else:
                languettes = []

                copie_ligne_aleatoire = list(ligne_aleatoire)
                ligne_actuelle = []

                for emplacement in grille[index_ligne_actuelle]:
                    ligne_actuelle.append(emplacement[2])

                index = 0;
                for couleur in ligne_actuelle:
                    if ligne_aleatoire[index] == couleur:
                        languettes.append("rouge")
                        copie_ligne_aleatoire.remove(couleur)
                    index += 1

                for couleur in ligne_actuelle:
                    for couleur2 in copie_ligne_aleatoire:
                        if couleur == couleur2:
                            languettes.append("blanche")
                            copie_ligne_aleatoire.remove(couleur)


                languettes = sorted(languettes, reverse=True)

                index = 0
                for languette in languettes:
                    grille_languettes[index_ligne_actuelle][index][2] = languette
                    canevas.create_image(grille_languettes[index_ligne_actuelle][index][0], grille_languettes[index_ligne_actuelle][index][1], image=fichiers["jeu_languette_" + languette], anchor='nw')
                    index += 1

                index_ligne_actuelle = index_ligne_actuelle - 1
                for emplacement in grille[index_ligne_actuelle]:
                    canevas.create_image(emplacement[0], emplacement[1], image=fichiers["jeu_pion_emplacement"], anchor='nw')
                canevas.move(bandeau, 0, -52)

    # On supprime le pion qui se déplaçait avec la souris
    canevas.delete(pion_actuel)



# ----------------------------------------------------------- Partie principale du programme ----------------------------------------------------------- #

# Création de la fenêtre Tkinter
fenetre=Tk()

# Change le titre de la fenêtre
fenetre.title("Retro Mastermind")

# Empêche l'utilisateur de changer la taille de la fenêtre
fenetre.resizable(False, False)

# Change l'icône de la fenêtre
fenetre.iconphoto(True, PhotoImage(file=os.path.join(sys.path[0], "ressources/images/icon.png")))

# Création du canevas
canevas = Canvas(fenetre, width=800, height=600, bg="black")
canevas.pack()

# On appelle la fonction qui charge les fichiers du jeu
ChargerFichiers()

# On appelle la fonction qui lance la musique
JouerMusiqueDeFond()

# On appelle la fonction qui dessine l'introduction
DessinerIntroduction()

# On lance la boucle de la fenetre Tkinter
fenetre.mainloop()

# ------------------------------------------------------------------------------------------------------------------------------------------------------ #

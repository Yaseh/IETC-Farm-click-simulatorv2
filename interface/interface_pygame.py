import pygame
import os
from interface.constantes import *
from utils.constantes import *
from utils.mode_selection import ModeSelection
from utils.constantes import NOMS_ANIMAUX
from interface.affichage import *


class InterfacePygame:
    """
    Interface graphique principale utilisant Pygame pour afficher et interagir
    avec le jeu de ferme.

    Elle gère :
    - La fenêtre et la configuration Pygame.
    - Les boutons d'achat, de sélection et de contrôle.
    - Le rendu des éléments visuels (images, textes, boutons).

    Attributes:
        jeu: Instance du moteur de jeu `Jeu` connecté à cette interface.
        ecran: Surface Pygame principale.
        police: Police Pygame pour les textes.
        horloge: Horloge Pygame pour contrôler le framerate.
        en_cours (bool): État actif de la boucle principale.
        mode_selection (ModeSelection): Mode actif (culture, animal, bâtiment).
    """

    def __init__(self, jeu):
        """
        Initialise la fenêtre, charge les ressources visuelles, crée les boutons
        et configure l'interface graphique.

        Args:
            jeu: Instance du jeu (`Jeu`) à contrôler avec cette interface.
        """
        self.jeu = jeu
        pygame.init()
       
        # Récupère la taille de l'écran
        info = pygame.display.Info()
        screen_width = info.current_w
        screen_height = info.current_h

        window_width = screen_width
        window_height = screen_height - 80  # Laisse la barre du bas visible

        self.ecran = pygame.display.set_mode((window_width, window_height))
        pygame.display.set_caption(TITRE_APPLICATION)
        self.police = pygame.font.SysFont(None, TAILLE_POLICE)
        self.horloge = pygame.time.Clock()
        self.mode_selection = ModeSelection.CULTURE
        self.en_cours = True

        # ✅ BOUTONS fixes
        self.bouton_jour_suivant = self._creer_rect(X_COL1, MARGE_HAUT)
        self.bouton_reset = self._creer_rect(LARGEUR_TOTALE + LARGEUR_BOUTON + 10 - LARGEUR_BOUTON - MARGE_BOUTON,
                                             HAUTEUR_TOTALE - HAUTEUR_BOUTON - MARGE_BOUTON)
        self.bouton_achat_medicament = self._creer_rect(X_COL2, MARGE_HAUT)
        self.bouton_achat_eau = self._creer_rect(X_COL3, MARGE_HAUT)
        self.bouton_achat_nourriture_betails = self._creer_rect(X_COL2, 225 + HAUTEUR_BOUTON)

        # ✅ Sélections
        self.culture_selectionnee = NOMS_CULTURES[0]
        self.animal_selectionne = NOMS_ANIMAUX[0]
        self.batiment_selectionne = NOMS_BATIMENTS[0]
        self.technicien_selectionnee = NOMS_TECHNICIENS[0]

        # ✅ Boutons de sélection
        self.boutons_selection_culture = self._creer_boutons(NOMS_CULTURES, X_COL1, 410, 40, 30)
        self.boutons_selection_animal = self._creer_boutons(NOMS_ANIMAUX, X_COL2, 410, 40, 30)
        self.boutons_selection_batiment = self._creer_boutons(NOMS_BATIMENTS, X_COL1, 600, 40, 30)

        # ✅ Boutons d'achat
        self.boutons_achat_graines = self._creer_boutons(NOMS_CULTURES, X_COL1, 0, LARGEUR_BOUTON, HAUTEUR_BOUTON)
        self.boutons_achat_animaux = self._creer_boutons(NOMS_ANIMAUX, X_COL2, 0, LARGEUR_BOUTON, HAUTEUR_BOUTON)
        self.boutons_achat_batiments = self._creer_boutons(NOMS_BATIMENTS, X_COL3, 0, LARGEUR_BOUTON, HAUTEUR_BOUTON)
        self.boutons_achat_techniciens = self._creer_boutons(NOMS_TECHNICIENS, X_COL3, 250, LARGEUR_BOUTON, HAUTEUR_BOUTON )

        # ✅ Images
        self.images_cultures = self._charger_images(NOMS_CULTURES, 3, SUFFIXE_IMG)
        self.images_animaux = self._charger_images(NOMS_ANIMAUX, 5, SUFFIXE_IMG)
        self.images_batiments = self._charger_images(NOMS_BATIMENTS, 1, SUFFIXE_GRANDE_IMG)
        self.images_techniciens = self._charger_images(NOMS_TECHNICIENS, 1, SUFFIXE_IMG)

        # os.path.join(DIR_IMG, f"{nom}_0{suffixe}")

        self.image_eau = self._charger_images(["eau"], 1 , SUFFIXE_IMG)
        self.image_medicament = self._charger_images(["médicament"], 1, SUFFIXE_IMG)
        self.image_nourriture_betails = self._charger_images(["nourriture_bétails"], 1, SUFFIXE_IMG)
     

    def _creer_rect(self, x, y, largeur=LARGEUR_BOUTON, hauteur=HAUTEUR_BOUTON):
        """Crée un rectangle Pygame pour un bouton donné.""" 
        return pygame.Rect(x, y, largeur, hauteur)

    def _creer_boutons(self, noms, x, y_depart, largeur, hauteur):  
        """
        Crée un dictionnaire de boutons alignés verticalement.

        Args:
            noms (list): Liste des noms d'éléments.
            x (int): Position X de départ.
            y_depart (int): Position Y de départ.
            largeur (int): Largeur de chaque bouton.
            hauteur (int): Hauteur de chaque bouton.

        Returns:
            dict: Dictionnaire { nom: Rect }.
        """             
        return {
            nom: pygame.Rect(x, y_depart + i * hauteur, largeur, hauteur)
            for i, nom in enumerate(noms)
        }

    def _charger_images(self, noms, nombre_images, suffixe):
        """
        Charge une liste d'images Pygame pour chaque élément.

        Args:
            noms (list): Liste des noms d'éléments.
            nombre_images (int): Nombre d'étapes/images par élément.
            suffixe (str): Suffixe pour le nom de fichier.

        Returns:
            dict: Dictionnaire { nom: [Surface, ...] }.
        """ 
        images = {}
        for nom in noms:
            images[nom] = []
            for i in range(nombre_images):
                chemin = os.path.join(DIR_IMG, f"{nom}_{i}{suffixe}")
                images[nom].append(pygame.image.load(chemin).convert_alpha())
        return images

    def afficher_section_titre(self, titre, couleur, x, y):
        """
        Affiche un titre souligné à une position donnée.

        Args:
            titre (str): Texte du titre.
            couleur (tuple): Couleur RGB.
            x (int): Position X.
            y (int): Position Y.

        Returns:
            int: Nouvelle coordonnée Y sous la ligne.
        """ 
        texte_titre = self.police.render(titre, True, couleur)
        self.ecran.blit(texte_titre, (x, y))
        largeur = texte_titre.get_width()
        hauteur = texte_titre.get_height()
        self.dessiner_ligne(x, y + hauteur + 2, x + largeur, y + hauteur + 2, couleur)
        return y + hauteur + 10

    def afficher_section_titre_et_valeur(self, titre, valeur, couleur, x, y):
        """
        Affiche un titre souligné et une valeur en dessous.

        Args:
            titre (str): Titre à afficher.
            valeur (str): Valeur à afficher sous le titre.
            couleur (tuple): Couleur RGB.
            x (int): Position X.
            y (int): Position Y.

        Returns:
            int: Nouvelle coordonnée Y après affichage.
        """
        y = self.afficher_section_titre(titre, couleur, x, y)
        texte_valeur = self.police.render(str(valeur), True, couleur)
        self.ecran.blit(texte_valeur, (x, y))
        return y
        
    def dessiner_ligne(self, x1, y1, x2, y2, couleur=BLANC, epaisseur=2):
        """Dessine une ligne droite entre deux points."""
        pygame.draw.line(self.ecran, couleur, (x1, y1), (x2, y2), epaisseur)

    def dessiner_bouton(self, rect, couleur_fond, texte, couleur_texte, couleur_bordure, icone=None, centrer_texte=False):
        """
        Dessine un bouton rectangulaire avec texte et optionnellement une icône.

        Args:
            rect (Rect): Rectangle du bouton.
            couleur_fond (tuple): Couleur de fond.
            texte (str): Texte à afficher.
            couleur_texte (tuple): Couleur du texte.
            couleur_bordure (tuple): Couleur de la bordure.
            icone (Surface, optional): Icône à afficher à gauche.
            centrer_texte (bool): Si True, centre le texte horizontalement.
        """
        pygame.draw.rect(self.ecran, couleur_fond, rect, border_radius=RAYON)
        pygame.draw.rect(self.ecran, couleur_bordure, rect, width=2, border_radius=RAYON)

        texte_surface = self.police.render(texte, True, couleur_texte)
        texte_rect = texte_surface.get_rect()
        texte_rect.centery = rect.centery

        if icone:
            # Affiche icône et place le texte à droite de l'icône
            icone_rect = icone.get_rect()
            icone_rect.x = rect.x + 8
            icone_rect.centery = rect.centery
            self.ecran.blit(icone, icone_rect)
            texte_rect.left = icone_rect.right + RAYON
        elif centrer_texte:
            # Centrer texte horizontalement sans icône
            texte_rect.centerx = rect.centerx
        else:
            # Si pas d'icône et pas centré explicitement : centrer par défaut
            texte_rect.centerx = rect.centerx

        self.ecran.blit(texte_surface, texte_rect)

    def afficher_achat_elements(self, boutons, images, prix_elements, couleur_bouton,
                                y_depart=90, hauteur_bouton=HAUTEUR_BOUTON, espace=10):
        """
        Affiche une liste de boutons d'achat avec leurs icônes et prix.

        Args:
            boutons (dict): Boutons à afficher.
            images (dict): Images des éléments.
            prix_elements (dict): Prix par élément.
            couleur_bouton (tuple): Couleur du fond du bouton.
            y_depart (int): Coordonnée Y de départ.
            hauteur_bouton (int): Hauteur des boutons.
            espace (int): Espace vertical entre les boutons.
        """
        for index, (nom, rect) in enumerate(boutons.items()):
            rect.y = y_depart + index * (hauteur_bouton + espace)

            # Préparer l'icône redimensionnée si elle existe
            icone = None
            images_elem = images.get(nom)
            if images_elem:
                icone = pygame.transform.scale(images_elem[-1], (28, 28))
            prix = prix_elements.get(nom, 0)
            etiquette = f"{ACHAT} {nom} ({prix}{DEVISE})"

            # ✅ Laisse dessiner_bouton gérer icône + texte
            self.dessiner_bouton(rect, couleur_bouton, etiquette, NOIR, BLANC, icone)

    def afficher_selection_elements(self, boutons, images, selection, couleur_selection, 
                                    y_barre, taille=60, espace=20):
        """
        Affiche une barre de boutons de sélection (culture, animal, bâtiment).

        Args:
            boutons (dict): Boutons à afficher.
            images (dict): Images correspondantes.
            selection (str): Élément actuellement sélectionné.
            couleur_selection (tuple): Couleur de fond pour l'élément sélectionné.
            y_barre (int): Coordonnée Y de la barre.
            taille (int): Taille des boutons.
            espace (int): Espace horizontal entre les boutons.
        """
        x_depart = MARGE_GRILLE
        for index, (nom, rect) in enumerate(boutons.items()):
            rect.x = x_depart + index * (taille + espace)
            rect.y = y_barre
            rect.width = taille
            rect.height = taille

            couleur_fond = couleur_selection if nom == selection else GRIS_FONCE
            image = images.get(nom)[-1]

            self.dessiner_bouton_selection(rect, couleur_fond, image, nom.capitalize())

    def dessine_image_ou_rect(self, images_dict, nom, stade, rect, contour_couleur=None):
        """Dessine l'image correspondante ou un rectangle par défaut."""
        if contour_couleur:
            pygame.draw.rect(self.ecran, contour_couleur, rect, 2)
        images = images_dict.get(nom)
        if images:
            stade_index = min(stade, len(images) - 1)
            self.ecran.blit(images[stade_index], rect.topleft)
        else:
            pygame.draw.rect(self.ecran, GRIS, rect)

    def appliquer_arrondi(self, surface, rayon):
        """Retourne une copie d'une Surface avec coins arrondis."""     
        taille = surface.get_size()
        masque = pygame.Surface(taille, pygame.SRCALPHA)
        # Dessiner un rectangle arrondi blanc opaque sur le masque
        pygame.draw.rect(masque, BLANC, (0, 0, *taille), border_radius=rayon)
        # Créer une copie de l'image avec alpha
        surface_arrondie = surface.copy()
        surface_arrondie.blit(masque, (0, 0), special_flags=pygame.BLEND_RGBA_MIN)
        return surface_arrondie
    
    def dessiner_bouton_selection(self, rect, couleur_fond, image, texte):
        """Dessine un bouton de sélection avec image arrondie et texte dessous."""
        rayon = 12
        pygame.draw.rect(self.ecran, couleur_fond, rect, border_radius=rayon)
        pygame.draw.rect(self.ecran, BLANC, rect, width=2, border_radius=rayon)

        if image:
            icone = pygame.transform.scale(image, (44, 44))
            icone = self.appliquer_arrondi(icone, rayon=RAYON)
            icone_rect = icone.get_rect(center=rect.center)
            self.ecran.blit(icone, icone_rect)

        texte_surface = self.police.render(texte, True, BLANC)
        texte_rect = texte_surface.get_rect(center=(rect.centerx, rect.bottom + 15))
        self.ecran.blit(texte_surface, texte_rect)
        
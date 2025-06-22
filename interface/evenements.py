import pygame
from utils.constantes import CLASSES_CULTURES, CLASSES_ANIMAUX, CLASSES_BATIMENTS
from utils.mode_selection import ModeSelection
from interface.constantes import *

def gerer_evenements(self):
    """
    Gère la boucle des événements Pygame.

    Vérifie les événements système, notamment :
    - Fermeture de la fenêtre.
    - Clics souris.

    Si un clic est détecté, appelle `gerer_clic`.

    Notes:
        Doit être appelée dans la boucle principale de l'interface.
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            self.en_cours = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            self.gerer_clic(event.pos)

def gerer_clic(self, position):
    """
    Traite un clic de souris en fonction de la position.

    Vérifie dans cet ordre :
    - Boutons de sélection (culture, animal, bâtiment).
    - Boutons d'achat (graines, animaux, bâtiments, techniciens, eau, nourriture, médicaments).
    - Boutons spéciaux (passer jour suivant, réinitialiser la carte).
    - Clic direct sur la grille (planter, placer, soigner ou récolter).

    Args:
        position (tuple): Coordonnées (x, y) du clic dans la fenêtre Pygame.
    """
    # Gestion des boutons de sélection
    for nom, rect in self.boutons_selection_culture.items():
        if rect.collidepoint(position):
            self.culture_selectionnee = nom
            self.mode_selection = ModeSelection.CULTURE
            return

    for nom, rect in self.boutons_selection_animal.items():
        if rect.collidepoint(position):
            self.animal_selectionne = nom
            self.mode_selection = ModeSelection.ANIMAL
            return
        
    for nom, rect in self.boutons_selection_batiment.items():
        if rect.collidepoint(position):
            self.batiment_selectionne = nom
            self.mode_selection = ModeSelection.BATIMENT
            return

    # Achats
    for nom_culture, rect in self.boutons_achat_graines.items():
        if rect.collidepoint(position):
            self.jeu.acheter_graine(nom_culture)
            return

    for nom_animal, rect in self.boutons_achat_animaux.items():
        if rect.collidepoint(position):
            self.jeu.acheter_animal(nom_animal)
            return
        
    for nom_batiment, rect in self.boutons_achat_batiments.items():
        if rect.collidepoint(position):
            self.jeu.acheter_batiment(nom_batiment)
            return
        
    for nom_technicien, rect in self.boutons_achat_techniciens.items():
        if rect.collidepoint(position):
            self.jeu.acheter_technicien(nom_technicien)
            return
        
    if self.bouton_achat_eau.collidepoint(position):
        self.jeu.acheter_eau()
        return
    
    if self.bouton_achat_nourriture_betails.collidepoint(position):
        self.jeu.acheter_nourriture_betails()
        return

    if self.bouton_achat_medicament.collidepoint(position):
        self.jeu.acheter_medicament()
        return

    if self.bouton_jour_suivant.collidepoint(position):
        self.jeu.passer_jour_suivant()
        return

    if self.bouton_reset.collidepoint(position):
        self.reinitialiser_ferme()
        return

    # Clique sur la grille
    if position[0] < MARGE_GRILLE or position[1] < MARGE_HAUT:
        return

    grille_x = (position[0] - MARGE_GRILLE) // TAILLE_CASE
    grille_y = (position[1] - MARGE_HAUT) // TAILLE_CASE
    case = self.jeu.obtenir_case(grille_x, grille_y)

    if case:
        # Soigner un animal malade
        animal = self.jeu.repo_animaux.trouver_par_id(case.id_animal)
        if animal:
            if animal.est_malade:
                from models.animaux.animal import Animal
                self.jeu.soigner(case, Animal, animal.nom())
                return
            # ✅ Sinon, si l’animal est mature → vendre
            else:
                self.jeu.vendre_animal(case)
                return


        # 🧺 Sinon, logique culture classique
        if case.id_culture:
            self.jeu.recolter(case)
            return
        
        if case.id_animal is None and case.id_culture is None and case.id_batiment is None:
            cls_animal = CLASSES_ANIMAUX.get(self.animal_selectionne)
            cls_culture = CLASSES_CULTURES.get(self.culture_selectionnee)
            cls_batiment = CLASSES_BATIMENTS.get(self.batiment_selectionne)

            if self.mode_selection == ModeSelection.ANIMAL and cls_animal:
                self.jeu.placer_animal(case, cls_animal, self.animal_selectionne)
            elif self.mode_selection == ModeSelection.CULTURE and cls_culture:
                self.jeu.planter_culture(case, cls_culture, self.culture_selectionnee)
            elif self.mode_selection == ModeSelection.BATIMENT and cls_batiment:
                self.jeu.placer_batiment(grille_x, grille_y, cls_batiment, self.batiment_selectionne)

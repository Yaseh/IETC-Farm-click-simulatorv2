import pygame
from interface.constantes import *

def afficher_selection_animal(self):
    """
    Affiche la barre de sélection des animaux.

    Positionne et dessine la rangée de boutons pour choisir un type d'animal
    à placer dans la ferme.
    """
    y_barre = MARGE_HAUT + 10 * TAILLE_CASE + 10 + 60 + 30
    
    self.afficher_selection_elements(
        self.boutons_selection_animal, self.images_animaux,
        self.animal_selectionne, JAUNE_CLAIR, y_barre)

def afficher_achat_animaux(self):
    """
    Affiche les boutons d'achat pour chaque animal disponible.

    Chaque bouton montre l'image de l'animal et son prix.
    """
    prix_elements = { nom: self.jeu.ressources.catalogue_prix.get(nom)
        for nom in self.boutons_achat_animaux
    }
    self.afficher_achat_elements(self.boutons_achat_animaux, self.images_animaux,
                                prix_elements, JAUNE_CLAIR)

def afficher_achat_nourriture_betails(self):
    """
    Affiche le bouton pour acheter de la nourriture pour le bétail.

    Le bouton indique la quantité et le coût total, avec une icône illustrant la nourriture.
    """
    prix = self.jeu.ressources.catalogue_prix.get("nourriture_betails")
    quant = self.jeu.ressources.catalogue_prix._quantite.get("nourriture_betails")
    self.dessiner_bouton(self.bouton_achat_nourriture_betails, JAUNE_CLAIR, f"{quant} nourriture {prix*quant}€",                   
                        NOIR, BLANC, pygame.transform.scale(self.image_nourriture_betails["nourriture_bétails"][0], (28, 28)), centrer_texte=True)
    
def afficher_achat_medicament(self):
    """
    Affiche le bouton pour acheter des médicaments.

    Le bouton indique la quantité et le coût total, avec une icône de médicament.
    """
    prix = self.jeu.ressources.catalogue_prix.get("médicament")
    quant = self.jeu.ressources.catalogue_prix._quantite.get("médicament")
    self.dessiner_bouton(self.bouton_achat_medicament, ROSE_CLAIR, f"{quant} médicaments {prix*quant}€", 
                        NOIR, BLANC, pygame.transform.scale(self.image_medicament["médicament"][0], (28, 28)), centrer_texte=True)
    
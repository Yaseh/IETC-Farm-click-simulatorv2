from interface.constantes import *

def afficher_selection_batiment(self):
    """
    Affiche la barre de sélection des bâtiments.

    Positionne et dessine la rangée de boutons pour choisir un type de bâtiment
    à installer sur la ferme.
    """
    y_barre = MARGE_HAUT + 10 * TAILLE_CASE + 190    
    self.afficher_selection_elements(self.boutons_selection_batiment, self.images_batiments,
        self.batiment_selectionne, ORANGE_CLAIR, y_barre)
    
def afficher_achat_batiments(self):
    """
    Affiche les boutons d'achat pour chaque bâtiment disponible.

    Chaque bouton montre l'image du bâtiment et son prix unitaire.
    """
    prix_elements = { nom: self.jeu.ressources.catalogue_prix.get(nom)
        for nom in self.boutons_achat_batiments
    }
    self.afficher_achat_elements(self.boutons_achat_batiments, self.images_batiments,
                                prix_elements, ORANGE_CLAIR)
    
def afficher_achat_techniciens(self):
    """
    Affiche les boutons d'achat pour chaque technicien.

    Chaque bouton montre l'image du technicien et son prix.
    Permet au joueur d'embaucher des techniciens pour réparer des pannes.
    """
    prix_elements = { nom: self.jeu.ressources.catalogue_prix.get(nom)
        for nom in self.boutons_achat_techniciens
    }
    self.afficher_achat_elements(self.boutons_achat_techniciens, self.images_techniciens,
                                prix_elements, BLEU_CLAIR, 265)

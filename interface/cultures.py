from interface.constantes import *

def afficher_selection_culture(self):
    """
    Affiche la barre de sélection des cultures.

    Positionne et dessine la rangée de boutons pour choisir
    un type de culture à planter sur la ferme.
    """
    y_barre = MARGE_HAUT + 10 * TAILLE_CASE + 10
    self.afficher_selection_elements(self.boutons_selection_culture, self.images_cultures,
                                    self.culture_selectionnee, VERT_CLAIR, y_barre)
    
def afficher_achat_graines(self):
    """
    Affiche les boutons d'achat pour les graines de cultures.

    Tous les types de graines utilisent le même prix unitaire,
    affiché sur chaque bouton avec l'image correspondante.
    """
    prix_grain = self.jeu.ressources.catalogue_prix.get("graine")
    prix_elements = {nom: prix_grain for nom in self.boutons_achat_graines}
    self.afficher_achat_elements(self.boutons_achat_graines, self.images_cultures, 
                                prix_elements, VERT_CLAIR)
    
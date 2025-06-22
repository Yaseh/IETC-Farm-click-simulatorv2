import pygame
from interface.constantes import *
from interface.animaux import *
from interface.batiments import *
from interface.cultures import *
from interface.ressources import * 
from utils.constantes import NOMS_ANIMAUX

def afficher(self):
    """
    Affiche l'ensemble de l'interface graphique du jeu.

    Cette fonction :
    
    - Remplit le fond de l'écran.
    - Affiche la grille avec cultures, animaux et bâtiments.
    - Affiche toutes les sections d'interaction :
      achats (eau, médicaments, nourriture, animaux, graines, bâtiments, techniciens),
      boutons de sélection et bouton pour réinitialiser la carte.
    """
    self.ecran.fill(VERT)
    afficher_grille(self)   
    afficher_ressources_du_joueur(self)     
    afficher_jour_suivant(self)        
    afficher_achat_eau(self)
    afficher_achat_medicament(self)
    afficher_achat_nourriture_betails(self)
    afficher_achat_animaux(self)
    afficher_selection_animal(self)
    afficher_achat_graines(self) 
    afficher_selection_culture(self)
    afficher_achat_batiments(self)
    afficher_selection_batiment(self)     
    afficher_achat_techniciens(self) 
    afficher_reinitialisation_carte(self)
        
        
def afficher_grille(self):
    """
    Dessine la grille de la ferme sur l'écran.

    Pour chaque case :
    - Affiche un animal, une culture ou un bâtiment si présent.
    - Si un animal est malade, trace un contour rouge.
    - Sinon, dessine le sol par défaut.

    Les bâtiments sont redimensionnés et dessinés uniquement
    sur leur case d'origine.
    """
    for case in self.jeu.cases:
        rect = pygame.Rect( MARGE_GRILLE + case.x * TAILLE_CASE, MARGE_HAUT + case.y * TAILLE_CASE,
                        TAILLE_CASE - 2, TAILLE_CASE - 2)
        # 1️⃣ Vérifie d'abord si c'est un animal
        if case.id_animal:
            animal = self.jeu.repo_animaux.trouver_par_id(case.id_animal)
            if animal:
                # ✅ Contour rouge si malade
                if animal.est_malade:
                    pygame.draw.rect(self.ecran, ROUGE, rect, 2)
                # ✅ Affiche l'image ou un rectangle par défaut
                self.dessine_image_ou_rect(self.images_animaux, animal.nom(), animal.age, rect)
        # 2️⃣ Sinon, vérifier culture
        elif case.id_culture:
            culture = self.jeu.repo_cultures.trouver_par_id(case.id_culture)
            if culture:
                self.dessine_image_ou_rect(self.images_cultures, culture.nom(), culture.age, rect)
       # 3️⃣ Sinon, vérifier batiment - pas de stade pour bâtiment = 0
        elif case.id_batiment:
            batiment = self.jeu.repo_batiments.trouver_par_id(case.id_batiment)
            if batiment:
                # ⚠️ Seulement sur la case d’origine (pour éviter de redessiner N fois)
                if batiment.x == case.x and batiment.y == case.y:
                    rect = pygame.Rect(
                        MARGE_GRILLE + batiment.x * TAILLE_CASE,
                        MARGE_HAUT + batiment.y * TAILLE_CASE,
                        batiment.largeur * TAILLE_CASE,
                        batiment.hauteur * TAILLE_CASE
                    )
                    image = self.images_batiments[batiment.nom()][0]
                    image_redim = pygame.transform.scale(
                        image,
                        (batiment.largeur * TAILLE_CASE, batiment.hauteur * TAILLE_CASE)
                    )
                    self.ecran.blit(image_redim, rect.topleft)
                # 4️⃣ Sinon, case vide = sol normal
        else:
            pygame.draw.rect(self.ecran, BEIGE, rect)


def afficher_jour_suivant(self):
    """
    Affiche le bouton « Jour suivant » permettant de passer au jour suivant dans le jeu.
    """
    self.dessiner_bouton(self.bouton_jour_suivant, ORANGE_CLAIR, "jour suivant", NOIR, BLANC, 
                        centrer_texte=True)

def afficher_achat_eau(self):
    """
    Affiche le bouton pour acheter de l'eau.

    Le bouton indique la quantité et le coût total calculé
    à partir du catalogue des prix.
    """
    prix = self.jeu.ressources.catalogue_prix.get("eau")
    quant = self.jeu.ressources.catalogue_prix._quantite.get("eau", 1)
    img = pygame.transform.scale(self.image_eau["eau"][0], (28, 28))
    self.dessiner_bouton(self.bouton_achat_eau, BLEU_CLAIR, f"{quant}L d'eau {prix*quant}€", NOIR, BLANC, 
                        img, centrer_texte=False)

def afficher_reinitialisation_carte(self):
    """
    Affiche le bouton permettant de réinitialiser toute la carte de la ferme.

    Permet de remettre à zéro toutes les cases, cultures, animaux et bâtiments.
    """
    self.dessiner_bouton(self.bouton_reset, ROUGE, "Réinitialiser la carte",
                        NOIR, BLANC, centrer_texte=True) 

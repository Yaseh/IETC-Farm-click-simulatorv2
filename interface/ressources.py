
"""
ressources.py

Ce module fournit la fonction pour afficher **l'ensemble des ressources** du joueur
sur l'interface Pygame : argent, eau, cultures, animaux, bâtiments, techniciens, météo, pannes, etc.

La fonction est conçue pour être patchée dynamiquement dans la classe `InterfacePygame`
(voir `interface_monkeypatch.py`).

Fonction:
    afficher_ressources_du_joueur(self)

    Affiche dans une colonne latérale gauche toutes les informations utiles pour le joueur :
    - Argent disponible
    - Quantité d'eau
    - Inventaire des graines
    - Inventaire des animaux
    - Nourriture pour bétails
    - Bâtiments possédés
    - Production réelle des bâtiments placés sur la ferme
    - Techniciens disponibles
    - Météo actuelle
    - État de panne technique
    - Nombre de médicaments
    - Alerte si plus de graines

Args:
    self: Instance de `InterfacePygame`.

Affichage :
    Chaque catégorie est affichée avec un titre coloré, suivi des valeurs ligne par ligne.
"""

import pygame
from interface.constantes import *
from utils.constantes import PRODUIT_PAR_BATIMENT


def afficher_ressources_du_joueur(self):
    """
    Affiche la barre latérale des ressources du joueur sur l'écran Pygame.

    Sections affichées :
        - Argent
        - Eau
        - Graines (cultures)
        - Animaux
        - Nourriture pour bétails
        - Bâtiments possédés
        - Production réelle des bâtiments actifs
        - Techniciens
        - Météo du jour
        - Panne technique en cours
        - Médicaments restants
        - Alerte si toutes les graines sont épuisées

    L'affichage se fait dans un rectangle à gauche de l'écran.
    """
    p = pygame.Rect(20, 20, LARGEUR_BOUTON, 800)
    pygame.draw.rect(self.ecran, GRIS_FONCE, p, border_radius=RAYON)
    pygame.draw.rect(self.ecran, BLANC, p, width=2, border_radius=RAYON)

    arg_x = p.x + 10
    # Point de départ vertical pour toutes les sections
    y_offset = p.y + 10 
    # ✅ ARGENT
    y_offset = self.afficher_section_titre_et_valeur(
        "Argent", f"{self.jeu.ressources.argent}{DEVISE}", BLANC, arg_x, y_offset)
    # ✅ EAU
    y_offset = self.afficher_section_titre_et_valeur(
        "Eau", f"{self.jeu.ressources.eau:.2f} L", BLEU_CLAIR, arg_x, y_offset + 30)
    # ✅ CULTURES
    y_offset = self.afficher_section_titre("Cultures", VERT_CLAIR, arg_x, y_offset + 30)
    for nom_culture, quantite in self.jeu.ressources.graines.items():
        texte_culture = self.police.render(f"{nom_culture.capitalize()} : {quantite}", True, VERT_CLAIR)
        self.ecran.blit(texte_culture, (arg_x, y_offset))
        y_offset += 20        
    # ✅ ANIMAUX
    y_offset = self.afficher_section_titre("Animaux", JAUNE_CLAIR, arg_x, y_offset + 10)
    for nom_animal, quantite in self.jeu.ressources.animaux.items():
        texte_animal = self.police.render(f"{nom_animal.capitalize()} : {quantite}", True, JAUNE_CLAIR)
        self.ecran.blit(texte_animal, (arg_x, y_offset))
        y_offset += 20
    # ✅ NOURRITURE BETAILS
    y_offset = self.afficher_section_titre_et_valeur(
        "Nourriture bétails", f"{self.jeu.ressources.nourriture_betails}", JAUNE_CLAIR, arg_x, y_offset + 10)
    # ✅ BÂTIMENTS (inventaire)
    y_offset = self.afficher_section_titre("Bâtiments", ORANGE_CLAIR, arg_x, y_offset + 30)
    for nom_batiment, quantite in self.jeu.ressources.batiments.items():
        texte_batiment = self.police.render(f"{nom_batiment.capitalize()} : {quantite}", True, ORANGE_CLAIR)
        self.ecran.blit(texte_batiment, (arg_x, y_offset))
        y_offset += 20
    # ✅ PRODUCTION RÉELLE (bâtiments posés)
    # Compter combien sont POSÉS
    compteur_poses = {}
    for bat in self.jeu.repo_batiments.tout_recuperer():
        nom = bat.nom()
        compteur_poses[nom] = compteur_poses.get(nom, 0) + 1
    y_offset = self.afficher_section_titre("Production Réelle", ORANGE_CLAIR, arg_x, y_offset + 10)
    for nom_bat, quantite_pose in compteur_poses.items():
        produit = PRODUIT_PAR_BATIMENT.get(nom_bat)
        if produit:
            prod_unitaire = self.jeu.ressources.production_batiments.get(produit, 0)
            prod_totale = prod_unitaire * quantite_pose
            texte_produit = self.police.render(
                f"{produit.capitalize()} : {prod_totale:.0f}", True, ORANGE_CLAIR)
            self.ecran.blit(texte_produit, (arg_x, y_offset))
            y_offset += 20
    # ✅ TECHNICIENS
    y_offset = self.afficher_section_titre("Techniciens", BLEU_CLAIR, arg_x, y_offset + 10)
    for technicien, quantite in self.jeu.ressources.techniciens.items():
        texte_techniciens = self.police.render(f"{technicien.capitalize()} : {quantite}", True, BLEU_CLAIR)
        self.ecran.blit(texte_techniciens, (arg_x, y_offset))
        y_offset += 20               
    # ✅ MÉTÉO
    y_offset += 10
    meteo = self.jeu.meteo_du_jour.afficher()
    texte_meteo = self.police.render(f"Météo : {meteo}", True, BLANC)
    self.ecran.blit(texte_meteo, (arg_x, y_offset))
    y_offset += 25
    # ✅ PANNE TECHNIQUE
    y_offset += 10
    type_de_panne = self.jeu.panne_actuelle
    if type_de_panne == None:
        type_de_panne = "Aucune"
    texte_panne_actuelle = self.police.render(f"Panne : {type_de_panne}", True, BLANC)
    self.ecran.blit(texte_panne_actuelle, (arg_x, y_offset))
    # ✅ MÉDICAMENTS
    y_offset += 25
    texte_medicaments = self.police.render(
        f"Médicaments : {self.jeu.ressources.medicaments}", True, ROSE_CLAIR)
    self.ecran.blit(texte_medicaments, (arg_x, y_offset + 10))
    y_offset += 25
    # ✅ ALERTE si plus de graines
    if all(q == 0 for q in self.jeu.ressources.graines.values()):
        alerte = self.police.render("Plus de graines !", True, ROUGE)
        self.ecran.blit(alerte, (arg_x, y_offset + 20))

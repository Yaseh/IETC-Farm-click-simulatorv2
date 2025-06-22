from interface.interface_pygame import InterfacePygame
from interface.evenements import gerer_evenements, gerer_clic
from interface.actions import lancer, reinitialiser_ferme
from interface.affichage import *
from interface.ressources import afficher_ressources_du_joueur

"""
main_interface.py

Ce module applique dynamiquement (monkey patching) l'ensemble des méthodes
d'affichage, d'interaction et d'actions aux instances de `InterfacePygame`.

Cela permet de garder une organisation modulaire :
chaque groupe de fonctions (événements, actions, affichage) reste dans son fichier,
mais est regroupé et injecté dans la classe principale ici.

Monkey patch appliqué :
    - Méthodes pour la boucle principale (`lancer`)
    - Gestion des événements et clics (`gerer_evenements`, `gerer_clic`)
    - Méthodes d'affichage et de réinitialisation
    - Méthodes spécifiques pour afficher ressources, achats et sélections

Imports:
    InterfacePygame (class) : Interface graphique principale.
    Toutes les fonctions à injecter.

Usage:
    Après import, toute instance de InterfacePygame a accès à ces méthodes.
"""

# Boucle principale et événements
InterfacePygame.lancer = lancer
InterfacePygame.reinitialiser_ferme = reinitialiser_ferme
InterfacePygame.gerer_evenements = gerer_evenements
InterfacePygame.gerer_clic = gerer_clic

# Affichage principal et grille
InterfacePygame.afficher = afficher
InterfacePygame.afficher_grille = afficher_grille

# Bouton principal
InterfacePygame.afficher_jour_suivant = afficher_jour_suivant

# Ressources du joueur
InterfacePygame.afficher_ressources_du_joueur = afficher_ressources_du_joueur

# Achats
InterfacePygame.afficher_achat_graines = afficher_achat_graines
InterfacePygame.afficher_achat_animaux = afficher_achat_animaux
InterfacePygame.afficher_achat_batiments = afficher_achat_batiments
InterfacePygame.afficher_achat_techniciens = afficher_achat_techniciens
InterfacePygame.afficher_achat_medicament = afficher_achat_medicament
InterfacePygame.afficher_achat_eau = afficher_achat_eau
InterfacePygame.afficher_achat_nourriture_betails = afficher_achat_nourriture_betails

# Sélections
InterfacePygame.afficher_selection_culture = afficher_selection_culture
InterfacePygame.afficher_selection_animal = afficher_selection_animal
InterfacePygame.afficher_selection_batiment = afficher_selection_batiment

# Réinitialisation
InterfacePygame.afficher_reinitialisation_carte = afficher_reinitialisation_carte

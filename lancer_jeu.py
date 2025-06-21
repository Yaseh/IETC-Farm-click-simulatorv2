from game.jeu import Jeu
from interface.main_interface import InterfacePygame

"""
Module principal pour lancer le jeu avec l'interface graphique Pygame.

Ce script initialise une instance du jeu et une interface graphique,
puis démarre la boucle principale de l'application.

Classes utilisées:
    - Jeu : la logique principale du jeu.
    - InterfacePygame : l'interface utilisateur graphique basée sur Pygame.
"""

if __name__ == "__main__":
    # Crée une instance du jeu
    jeu = Jeu()

    # Crée l'interface graphique Pygame en lui passant le jeu
    interface = InterfacePygame(jeu)

    # Lance la boucle principale de l'interface graphique
    interface.lancer()
    
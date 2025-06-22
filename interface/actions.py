import pygame

def lancer(self):
    """
    Boucle principale de l'interface graphique du jeu.

    Exécute la boucle :
    - Gère les événements utilisateur.
    - Affiche les éléments à l'écran.
    - Rafraîchit l'affichage avec un framerate de 60 FPS.
    - Quitte proprement Pygame lorsque le jeu se termine.
    """
    while self.en_cours:
        self.gerer_evenements()
        self.afficher()
        pygame.display.flip()
        self.horloge.tick(60)
    pygame.quit()

def reinitialiser_ferme(self):
    # 1️⃣ Réinitialise les cases
    for case in self.jeu.cases:
        case.id_culture = None
        case.id_animal = None
        case.id_batiment = None
        self.jeu.repo_cases.ajouter(case)
    # 2️⃣ Supprime toutes les cultures
    for culture in self.jeu.repo_cultures.tout_recuperer():
        self.jeu.repo_cultures.supprimer(culture.identifiant)
    # 3️⃣ Supprime tous les animaux
    for animal in self.jeu.repo_animaux.tout_recuperer():
        self.jeu.repo_animaux.supprimer(animal.identifiant)
    # 4️⃣ Supprime tous les bâtiments
    for batiment in self.jeu.repo_batiments.tout_recuperer():
        self.jeu.repo_batiments.supprimer(batiment.identifiant)
    print("Carte réinitialisée.")

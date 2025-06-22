from typing import Dict
from utils.generateur_identifiant import generer_identifiant
from utils.mode_selection import ModeSelection

# Accès aux tuiles de la ferme
class CaseFerme:
    """
    Représente une case individuelle de la ferme.

    Chaque case peut contenir :
    - une culture (id_culture)
    - un animal (id_animal)
    - un bâtiment (id_batiment)
    ainsi que ses coordonnées (x, y).

    Attributes:
        identifiant (str): Identifiant unique de la case.
        x (int): Coordonnée horizontale de la case.
        y (int): Coordonnée verticale de la case.
        id_culture (str, optional): Identifiant de la culture placée sur la case.
        id_animal (str, optional): Identifiant de l'animal placé sur la case.
        id_batiment (str, optional): Identifiant du bâtiment placé sur la case.
    """

    def __init__(self, identifiant: str, x: int, y: int, id_culture: str=None,
                 id_animal: str=None, id_batiment: str=None):
        """
        Initialise une nouvelle case de la ferme avec ses coordonnées
        et ses éventuels contenus.

        Args:
            identifiant (str): Identifiant unique de la case.
            x (int): Position en X.
            y (int): Position en Y.
            id_culture (str, optional): Culture placée sur la case.
            id_animal (str, optional): Animal placé sur la case.
            id_batiment (str, optional): Bâtiment placé sur la case.
        """
        self.identifiant = identifiant
        self.x = x
        self.y = y
        self.id_culture = id_culture
        self.id_animal = id_animal
        self.id_batiment = id_batiment

    @staticmethod
    def obtenir_case(cases, x, y):
        """
        Recherche une case dans une liste à partir de ses coordonnées.

        Args:
            cases (list[CaseFerme]): Liste des cases.
            x (int): Coordonnée X recherchée.
            y (int): Coordonnée Y recherchée.

        Returns:
            CaseFerme or None: La case trouvée ou None si aucune ne correspond.
        """
        for case in cases:
            if case.x == x and case.y == y:
                return case
        return None

    def _placer_rapidement(self, attr_id, Classe, nom, repo, stock, jeu):
        """
        Méthode interne pour placer rapidement une culture ou un animal sur la case.

        Args:
            attr_id (str): Nom de l'attribut à définir ('id_culture' ou 'id_animal').
            Classe (class): Classe de l'élément à créer (Culture ou Animal).
            nom (str): Nom de l'élément.
            repo (object): Dépôt où ajouter l'élément.
            stock (dict): Stock du joueur pour cette ressource.
            jeu (object): Instance du jeu pour mise à jour des dépôts.

        Returns:
            bool: True si le placement a réussi, False sinon.
        """  
        if getattr(self, attr_id) is None and stock[nom] > 0:
            element = Classe(identifiant=generer_identifiant(), age=0)
            repo.ajouter(element)
            setattr(self, attr_id, element.identifiant)
            jeu.repo_cases.ajouter(self)
            stock[nom] -= 1
            return True
        return False

    def placer(self, mode, Classe, nom, jeu, largeur=2, hauteur=3):
        """
        Place une culture, un animal ou un bâtiment sur la case selon le mode choisi.

        Args:
            mode (ModeSelection): Type d'élément à placer (CULTURE, ANIMAL ou BATIMENT).
            Classe (class): Classe de l'élément à instancier.
            nom (str): Nom de l'élément.
            jeu (object): Instance du jeu pour mise à jour des dépôts.
            largeur (int, optional): Largeur du bâtiment (mode BATIMENT). Par défaut 2.
            hauteur (int, optional): Hauteur du bâtiment (mode BATIMENT). Par défaut 3.
        """
        ressources = jeu.ressources
        if mode == ModeSelection.CULTURE:
            self._placer_rapidement("id_culture", Classe, nom, jeu.repo_cultures, ressources.graines, jeu)
        elif mode == ModeSelection.ANIMAL:
            self._placer_rapidement("id_animal", Classe, nom, jeu.repo_animaux, ressources.animaux, jeu)
        elif mode == ModeSelection.BATIMENT:
            x, y = self.x, self.y
            if ressources.batiments[nom] > 0:
                batiment = Classe(
                    identifiant=generer_identifiant(), x=x, y=y,
                    largeur=largeur, hauteur=hauteur
                )
                jeu.repo_batiments.ajouter(batiment)
                for dx in range(largeur):
                    for dy in range(hauteur):
                        c = jeu.obtenir_case(x + dx, y + dy)
                        c.id_batiment = batiment.identifiant
                        jeu.repo_cases.ajouter(c)
                ressources.batiments[nom] -= 1
                print(f"Bâtiment placé sur {largeur}x{hauteur} à ({x},{y})")
            else:
                print("Emplacement invalide ou pas de stock !")
        jeu.repo_ressources_joueur.ajouter(ressources)


    def en_dictionnaire(self)-> Dict[str, object]:
        """
        Convertit les informations de la case en dictionnaire.

        Returns:
            dict: Représentation de la case sous forme clé/valeur.
        """
        return {
            "identifiant": self.identifiant,
            "x": self.x,
            "y": self.y,
            "id_culture": self.id_culture,
            "id_animal": self.id_animal,
            "id_batiment": self.id_batiment
        }
    
    def est_vide(self) -> bool:
        """
        Vérifie si la case est vide (aucune culture).

        Returns:
            bool: True si la case n'a pas de culture, False sinon.
        """
        return self.id_culture is None
    
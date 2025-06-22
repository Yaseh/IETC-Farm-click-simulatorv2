import random

class Maladie:
    """
    Classe représentant l'état sanitaire global ou une épidémie dans le jeu.

    La maladie est choisie aléatoirement à chaque instance avec une probabilité
    élevée qu'aucune maladie ne soit présente.

    Attributes:
        maladies_possibles (dict): Dictionnaire des maladies et leur niveau de gravité.
        condition (str): Maladie actuelle sélectionnée aléatoirement.
    """

    def __init__(self):
        """
        Initialise la condition sanitaire avec une maladie aléatoire.

        Par défaut, il y a 70% de chances qu'aucune maladie ne soit active.
        """
        self.maladies_possibles = {
            "Aucune": 0,
            "Grippe aviaire": 1,
            "Fièvre aphteuse": 2,
            "Brucellose": 3
        }
        # 70% de chance de n'avoir aucune maladie
        probabilites = ( ["Aucune"] * 7 + 
            ["Grippe aviaire", "Fièvre aphteuse", "Brucellose"]
        )
        self.condition = random.choice(probabilites)

    def gravite(self) -> int:
        """
        Retourne le niveau de gravité de la maladie.

        Returns:
            int: Niveau de gravité (0 = aucune maladie, 3 = maladie grave).
        """
        return self.maladies_possibles[self.condition]

    def est_active(self) -> bool:
        """
        Vérifie si une maladie est active.

        Returns:
            bool: True si une maladie est présente, False sinon.
        """
        return self.condition != "Aucune"

    def afficher_condition(self) -> str:
        """
        Affiche la maladie actuelle sous forme de texte.

        Returns:
            str: Nom de la maladie actuelle.
        """
        return self.condition

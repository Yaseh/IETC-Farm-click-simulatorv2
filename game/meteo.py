import random

class Meteo:
    """
    Classe représentant la météo quotidienne du jeu.

    La météo influe sur la quantité d'eau disponible chaque jour
    en fonction des conditions climatiques (soleil, nuages, pluie).

    Attributes:
        conditions_possibles (dict): Dictionnaire des conditions météo et leur coefficient d'eau.
        condition (str): Condition météo actuelle sélectionnée aléatoirement.
    """

    def __init__(self):
        """
        Initialise la météo avec une condition aléatoire parmi :
        'Soleil', 'Nuageux' ou 'Pluie'.
        """
        self.conditions_possibles = {
            "Soleil": 1,
            "Nuageux": 2,
            "Pluie": 4
        }
        self.condition = random.choice(list(self.conditions_possibles.keys()))

    def eau_du_jour(self) -> int:
        """
        Retourne la quantité d'eau générée en fonction de la météo du jour.

        Returns:
            int: Quantité d'eau disponible selon la condition actuelle.
        """
        return self.conditions_possibles[self.condition]

    def afficher(self) -> str:
        """
        Retourne la condition météo actuelle sous forme de texte.

        Returns:
            str: Condition météo actuelle.
        """
        return self.condition

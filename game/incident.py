import random

class Incident:
    """
    Classe représentant un incident pouvant survenir dans la ferme.

    Un incident peut être de type mécanique, plomberie ou électrique.
    Il y a une probabilité élevée de ne rencontrer aucun incident.

    Attributes:
        incidents_possibles (dict): Types d'incidents et leur gravité.
        condition (str): Incident actuellement actif ou "Aucune".
    """

    def __init__(self):
        """
        Initialise un incident avec une probabilité aléatoire.

        Par défaut, 90% de chances qu'aucun incident ne se produise.
        """
        self.incidents_possibles = {
            "Aucune": 0,
            "Mécanique": 1,
            "Plomberie": 2,
            "Électrique": 3,
        }
        # 90% de chance de n'avoir aucun incident
        probabilites = ( ["Aucune"] * 9 + 
            ["Mécanique", "Plomberie", "Électrique" ]
        )
        self.condition = random.choice(probabilites)

    def gravite(self) -> int:
        """
        Renvoie le niveau de gravité de l'incident.

        Returns:
            int: Gravité entre 0 (aucun incident) et 3 (incident grave).
        """
        return self.incidents_possibles[self.condition]

    def est_active(self) -> bool:
        """
        Vérifie si un incident est actuellement actif.

        Returns:
            bool: True si un incident est en cours, False sinon.
        """
        return self.condition != "Aucune"

    def afficher_condition(self) -> str:
        """
        Affiche le type d'incident actuel.

        Returns:
            str: Nom de l'incident ou "Aucune".
        """
        return self.condition
    
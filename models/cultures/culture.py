from typing import Dict

# Modèle de culture
class Culture:
    """
    Classe représentant le modèle générique d'une culture agricole.

    Attributes:
        identifiant (str): Identifiant unique de la culture.
        nom (str): Nom de la culture.
        temps_pousse (int): Durée de croissance de la culture (en jours).
        valeur (float): Valeur marchande de la culture.
        besoin_eau (float): Quantité d'eau nécessaire.
        age (int): Âge actuel de la culture.
    """
    
    def __init__(self, identifiant: str, nom: str, temps_pousse: int, valeur: float, 
                 besoin_eau: float, age: int=0):
        """
        Initialise une culture avec ses caractéristiques de base.

        Args:
            identifiant (str): Identifiant unique de la culture.
            nom (str): Nom de la culture.
            temps_pousse (int): Durée de croissance en jours.
            valeur (float): Valeur de revente.
            besoin_eau (float): Quantité d'eau nécessaire.
            age (int, optional): Âge initial de la culture. Par défaut 0.
        """
        self.identifiant = identifiant
        self.nom = nom
        self.temps_pousse = temps_pousse
        self.valeur = valeur
        self.besoin_eau = besoin_eau
        self.age = age

    def en_dictionnaire(self) -> Dict[str, object]:
        """
        Convertit les données de la culture en dictionnaire.

        Returns:
            dict: Représentation clé/valeur de la culture.
        """
        return {
            "identifiant": self.identifiant,
            "nom": self.nom,
            "temps_pousse": self.temps_pousse,
            "valeur": self.valeur,
            "besoin_eau": self.besoin_eau,
            "age": self.age
        }

    def est_mature(self) -> bool:
        """
        Détermine si la culture est arrivée à maturité.

        Returns:
            bool: True si l'âge de la culture est supérieur ou égal à son temps de pousse.
        """
        return self.age >= self.temps_pousse
    

    

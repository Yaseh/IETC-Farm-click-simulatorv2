from abc import ABC, abstractmethod
from typing import Dict

class Culture(ABC):
    """
    Classe abstraite représentant le modèle générique d'une culture agricole.

    Cette classe définit l'interface commune pour toutes les cultures concrètes.
    Elle impose l'implémentation des méthodes `nom`, `temps_pousse`, `valeur` et `besoin_eau`.

    Attributes:
        identifiant (str): Identifiant unique de la culture.
        age (int): Âge actuel de la culture.
    """
    
    def __init__(self, identifiant: str, age: int = 0):
        """
        Initialise une instance de la culture abstraite.

        Args:
            identifiant (str): Identifiant unique.
            age (int, optional): Âge initial. Par défaut 0.
        """
        self.identifiant = identifiant
        self.age = age

    @abstractmethod
    def nom(self) -> str:
        """
        Retourne le nom de la culture.

        Returns:
            str: Nom de la culture.
        """
        pass

    @abstractmethod
    def temps_pousse(self) -> int:
        """
        Retourne le temps de croissance complet pour la culture.

        Returns:
            int: Durée de croissance en jours.
        """
        pass

    @abstractmethod
    def valeur(self) -> float:
        """
        Retourne la valeur marchande de la culture.

        Returns:
            float: Valeur en unités monétaires.
        """
        pass

    @abstractmethod
    def besoin_eau(self) -> float:
        """
        Retourne la quantité d'eau nécessaire pour la culture.

        Returns:
            float: Besoin en eau.
        """
        pass

    def est_mature(self) -> bool:
        """
        Vérifie si la culture est arrivée à maturité.

        Returns:
            bool: True si l'âge est supérieur ou égal au temps de pousse.
        """
        return self.age >= self.temps_pousse()

    def vieillir(self) -> None:
        """
        Fait vieillir la culture d'un jour.
        """
        self.age += 1

    def en_dictionnaire(self) -> Dict[str, object]:
        """
        Convertit la culture en dictionnaire de valeurs clés.

        Returns:
            dict: Dictionnaire contenant le nom, l'identifiant et l'âge de la culture.
        """
        return {
            "nom": self.nom(),
            "identifiant": self.identifiant,
            "age": self.age
        }

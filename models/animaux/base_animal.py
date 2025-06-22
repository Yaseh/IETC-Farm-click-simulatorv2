from abc import ABC, abstractmethod
from typing import Dict

class Animal(ABC):
    """
    Classe abstraite représentant le modèle générique d'un animal de la ferme.

    Cette classe définit l'interface que tout animal concret doit implémenter :
    nom, temps de croissance, type d'alimentation, production, valeur et besoins.

    Attributes:
        identifiant (str): Identifiant unique de l'animal.
        age (int): Âge actuel de l'animal.
        est_malade (bool): Indique si l'animal est malade.
    """

    def __init__(self, identifiant: str, age: int = 0, est_malade: bool = False):
        """
        Initialise les propriétés communes d'un animal.

        Args:
            identifiant (str): Identifiant unique de l'animal.
            age (int, optional): Âge initial. Par défaut 0.
            est_malade (bool, optional): État de santé initial. Par défaut False.
        """
        self.identifiant = identifiant
        self.age = age
        self.est_malade = est_malade

    @abstractmethod
    def nom(self) -> str:
        """
        Retourne le nom de l'animal.

        Returns:
            str: Nom de l'animal.
        """
        pass

    @abstractmethod
    def temps_croissance(self) -> int:
        """
        Retourne le temps de croissance complet de l'animal.

        Returns:
            int: Temps de croissance en jours.
        """
        pass

    """Ex. : herbivore, carnivore, omnivore"""
    @abstractmethod
    def type_alimentation(self) -> str:
        """
        Retourne le type d'alimentation de l'animal.

        Exemple : herbivore, carnivore, omnivore.

        Returns:
            str: Type d'alimentation.
        """
        pass

    """Ex. : lait, œufs, laine"""
    @abstractmethod
    def production(self) -> str:
        """
        Retourne le produit généré par l'animal.

        Exemple : lait, œufs, laine.

        Returns:
            str: Produit généré.
        """
        pass

    @abstractmethod
    def valeur(self) -> float:
        """
        Retourne la valeur marchande de l'animal.

        Returns:
            float: Valeur en unités monétaires.
        """
        pass

    @abstractmethod
    def besoin_eau(self) -> float:
        """
        Retourne la quantité d'eau nécessaire pour l'animal.

        Returns:
            float: Besoin en eau quotidien.
        """
        pass

    @abstractmethod
    def besoin_nourriture(self) -> float:
        """
        Retourne la quantité de nourriture nécessaire pour l'animal.

        Returns:
            float: Besoin en nourriture quotidien.
        """
        pass

    def tomber_malade(self):
        """
        Marque l'animal comme malade.
        """
        self.est_malade = True

    def soigner(self):
        """
        Soigne l'animal et réinitialise son état de santé.
        """
        self.est_malade = False

    def est_adulte(self) -> bool:
        """
        Vérifie si l'animal est adulte.

        Returns:
            bool: True si l'âge est supérieur ou égal au temps de croissance.
        """
        return self.age >= self.temps_croissance()

    def vieillir(self) -> None:
        """
        Fait vieillir l'animal d'un jour en augmentant son âge.
        """
        self.age += 1

    def en_dictionnaire(self) -> Dict[str, object]:
        """
        Convertit les informations de l'animal en dictionnaire.

        Returns:
            dict: Dictionnaire contenant le nom, l'identifiant, l'âge et l'état de santé.
        """
        return {
            "nom": self.nom(),
            "identifiant": self.identifiant,
            "age": self.age,
            "est_malade": self.est_malade
        }

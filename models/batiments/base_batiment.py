from abc import ABC, abstractmethod
from typing import Dict

class Batiment(ABC):
    """
    Classe abstraite représentant le modèle générique d'un bâtiment.

    Cette classe définit l'interface de base pour tous les bâtiments concrets
    de la ferme. Elle impose l'implémentation des méthodes principales et 
    gère les propriétés communes : position, dimensions, âge, état de panne.

    Attributes:
        identifiant (str): Identifiant unique du bâtiment.
        x (int): Coordonnée X.
        y (int): Coordonnée Y.
        largeur (int): Largeur en cases.
        hauteur (int): Hauteur en cases.
        age (int): Âge du bâtiment.
        est_en_panne (bool): Indique si le bâtiment est en panne.
        type_de_panne_metier (str): Type de technicien nécessaire pour réparer la panne.
    """

    def __init__(self, identifiant: str, x: int, y: int, largeur: int, hauteur: int, age: int = 0,
                 est_en_panne:bool = False, type_de_panne_metier:str = None):
        """
        Initialise les propriétés communes d'un bâtiment abstrait.

        Args:
            identifiant (str): Identifiant unique.
            x (int): Coordonnée horizontale.
            y (int): Coordonnée verticale.
            largeur (int): Largeur du bâtiment (en cases).
            hauteur (int): Hauteur du bâtiment (en cases).
            age (int, optional): Âge initial. Par défaut 0.
            est_en_panne (bool, optional): État de panne initial. Par défaut False.
            type_de_panne_metier (str, optional): Type de technicien requis en cas de panne.
        """
        self.identifiant = identifiant
        self.x = x
        self.y = y
        self.largeur = largeur
        self.hauteur = hauteur
        self.age = age

    @abstractmethod
    def nom(self) -> str:
        """
        Retourne le nom du bâtiment.

        Returns:
            str: Nom du bâtiment.
        """
        pass

    @abstractmethod
    def capacite_animaux(self) -> int:
        """
        Retourne le nombre maximal d'animaux pouvant être hébergés.

        Returns:
            int: Capacité maximale.
        """
        pass

    @abstractmethod
    def production_journaliere(self) -> float:
        """
        Retourne la valeur générée chaque jour par le bâtiment (revenus bruts).

        Returns:
            float: Production journalière en unités monétaires.
        """
        return 0.0

    @abstractmethod
    def cout_entretien(self) -> float:
        """
        Retourne le coût d'entretien quotidien du bâtiment.

        Returns:
            float: Coût d'entretien en unités monétaires.
        """
        pass

    def vieillir(self) -> None:
        """
        Fait vieillir le bâtiment d'un jour en augmentant son âge.
        """
        self.age += 1

    def en_dictionnaire(self) -> Dict[str, object]:
        """
        Convertit les informations du bâtiment en dictionnaire.

        Returns:
            dict: Dictionnaire des propriétés principales du bâtiment.
        """
        return {
            "nom": self.nom(),
            "identifiant": self.identifiant,
            "x": self.x,
            "y": self.y,
            "largeur": self.largeur,
            "hauteur": self.hauteur,
            "age": self.age,
        }

from typing import Dict

from utils.constantes import NOMS_TECHNICIENS

# 
class Batiment:    
    """
    Classe représentant le modèle générique d'un bâtiment.

    Cette classe définit les attributs de base partagés par tous les types
    de bâtiments de la ferme, tels que la position, la taille, la capacité,
    la production quotidienne et le coût d'entretien.

    Attributes:
        identifiant (str): Identifiant unique du bâtiment.
        nom (str): Nom du bâtiment.
        x (int): Coordonnée X du bâtiment.
        y (int): Coordonnée Y du bâtiment.
        largeur (int): Largeur du bâtiment (en cases).
        hauteur (int): Hauteur du bâtiment (en cases).
        capacite_animaux (int): Capacité maximale d'animaux hébergés.
        production_journaliere (float): Production quotidienne générée par le bâtiment.
        cout_entretien (float): Coût d'entretien journalier.
        age (int): Âge actuel du bâtiment.
    """

    def __init__( self, identifiant: str, nom: str, x: int, y: int, largeur: int, hauteur: int,
                  capacite_animaux: int, production_journaliere: float, cout_entretien: float, 
                  age: int = 0 ):
        """
        Initialise un bâtiment avec ses propriétés de base.

        Args:
            identifiant (str): Identifiant unique du bâtiment.
            nom (str): Nom du bâtiment.
            x (int): Position horizontale.
            y (int): Position verticale.
            largeur (int): Largeur du bâtiment en nombre de cases.
            hauteur (int): Hauteur du bâtiment en nombre de cases.
            capacite_animaux (int): Capacité d'animaux hébergés.
            production_journaliere (float): Production quotidienne.
            cout_entretien (float): Coût d'entretien journalier.
            age (int, optional): Âge initial du bâtiment. Par défaut 0.
        """
        self.identifiant = identifiant
        self.nom = nom
        self.x = x
        self.y = y
        self.largeur = largeur
        self.hauteur = hauteur
        self.capacite_animaux = capacite_animaux
        self.production_journaliere = production_journaliere
        self.cout_entretien = cout_entretien
        self.age = age

    def vieillir(self) -> None:
        """
        Fait vieillir le bâtiment d'un jour en incrémentant son âge.
        """
        self.age += 1


    @property
    def produit(self) -> str:
        """
        Produit généré par le bâtiment.

        Par défaut, un bâtiment générique ne produit rien.

        Returns:
            str or None: Nom du produit ou None.
        """
        return None

    def en_dictionnaire(self) -> Dict[str, object]:
        """
        Convertit les informations du bâtiment en dictionnaire.

        Returns:
            dict: Dictionnaire contenant toutes les propriétés du bâtiment.
        """
        return {
            "identifiant": self.identifiant,
            "nom": self.nom,
            "x": self.x,
            "y": self.y,
            "largeur": self.largeur,
            "hauteur": self.hauteur,
            "capacite_animaux": self.capacite_animaux,
            "production_journaliere": self.production_journaliere,
            "cout_entretien": self.cout_entretien,
            "age": self.age
        }

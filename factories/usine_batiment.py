from typing import Dict
from models.batiments.base_batiment import Batiment
from utils.constantes import CLASSES_BATIMENTS

def batiment_depuis_dictionnaire(donnees: Dict[str, object]) -> Batiment:
    """
    Crée une instance concrète de `Batiment` à partir des données d'un dictionnaire.

    Cette fonction agit comme une factory pour reconstituer un bâtiment
    à partir des données persistées (JSON).

    Args:
        donnees (Dict[str, object]): Dictionnaire contenant les champs :
            - "nom" (str) : Nom du bâtiment.
            - "identifiant" (str) : Identifiant unique.
            - "x" (int) : Coordonnée X.
            - "y" (int) : Coordonnée Y.
            - "largeur" (int) : Largeur du bâtiment.
            - "hauteur" (int) : Hauteur du bâtiment.
            - "age" (int, optional) : Âge du bâtiment.

    Returns:
        models.batiments.base_batiment.Batiment: Instance concrète de la sous-classe correspondante.

    Raises:
        ValueError: Si le nom du bâtiment n'est pas reconnu dans CLASSES_BATIMENTS.
    """
    nom = donnees.get("nom", "")
    identifiant = donnees["identifiant"]
    x = donnees["x"]
    y = donnees["y"]
    largeur = donnees["largeur"]
    hauteur = donnees["hauteur"]
    age = donnees.get("age", 0)

    if nom not in CLASSES_BATIMENTS:
        raise ValueError(f"Type de bâtiment inconnu : nom={nom}")

    return CLASSES_BATIMENTS[nom](identifiant, x, y, largeur, hauteur, age)

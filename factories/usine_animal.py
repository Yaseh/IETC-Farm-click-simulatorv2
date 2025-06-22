from typing import Dict
from models.animaux.base_animal import Animal
from utils.constantes import CLASSES_ANIMAUX

def animal_depuis_dictionnaire(donnees: Dict[str, object]) -> Animal:
    """
    Crée une instance concrète de `Animal` à partir des données d'un dictionnaire.

    Cette fonction agit comme une factory pour reconstituer un animal
    à partir des données persistées (JSON).

    Args:
        donnees (Dict[str, object]): Dictionnaire contenant les champs :
            - "nom" (str) : Nom de l'animal.
            - "identifiant" (str) : Identifiant unique.
            - "age" (int, optional) : Âge de l'animal.

    Returns:
        models.animaux.base_animal.Animal: Instance concrète de la sous-classe correspondante.

    Raises:
        ValueError: Si le nom de l'animal n'est pas reconnu dans CLASSES_ANIMAUX.
    """
    nom = donnees.get("nom", "")
    identifiant = donnees["identifiant"]
    age = donnees.get("age", 0)

    if nom not in CLASSES_ANIMAUX:
        raise ValueError(f"Type d'animal inconnu : nom={nom}")

    return CLASSES_ANIMAUX[nom](identifiant, age)

from typing import Dict
from models.cultures.base_culture import Culture
from utils.constantes import CLASSES_CULTURES

def culture_depuis_dictionnaire(donnees: Dict[str, object]) -> Culture:
    """
    Crée une instance concrète de `Culture` à partir des données d'un dictionnaire.

    Cette fonction agit comme une factory pour reconstituer une culture
    à partir des données persistées (JSON).

    Args:
        donnees (Dict[str, object]): Dictionnaire contenant les champs :
            - "nom" (str) : Nom de la culture.
            - "identifiant" (str) : Identifiant unique.
            - "age" (int, optional) : Âge de la culture.

    Returns:
        models.cultures.base_culture.Culture: Instance concrète de la sous-classe correspondante.

    Raises:
        ValueError: Si le nom de culture n'est pas reconnu dans CLASSES_CULTURES.
    """
    nom = donnees.get("nom", "")
    identifiant = donnees["identifiant"]
    age = donnees.get("age", 0)

    if nom not in CLASSES_CULTURES:
        raise ValueError(f"Type de culture inconnu : nom={nom}")

    return CLASSES_CULTURES[nom](identifiant, age)

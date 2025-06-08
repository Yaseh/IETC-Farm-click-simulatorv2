from typing import Dict
from models.base_culture import Culture
from models.ble import Ble
from models.carotte import Carotte

''' usine_culture.py ← factory : crée les instances depuis un dictionnaire '''
def culture_depuis_dictionnaire(data: Dict[str, object]) -> Culture:
    nom = data.get("nom", "")
    identifiant = data["identifiant"]
    age = data.get("age", 0)

    if not nom:
        raise ValueError("Le champ 'nom' est manquant ou vide dans les données JSON.")

    if nom == "ble":
        return Ble(identifiant, age)
    elif nom == "carotte":
        return Carotte(identifiant, age)
    else:
        raise ValueError(f"Type de culture inconnu : nom={nom}")

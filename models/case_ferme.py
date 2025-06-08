from typing import Dict

# Accès aux tuiles de la ferme
class CaseFerme:
    def __init__(self, identifiant: str, x: int, y: int, id_culture: str=None):
        self.identifiant = identifiant
        self.x = x
        self.y = y
        self.id_culture = id_culture

    def en_dictionnaire(self)-> Dict[str, object]:
        return {
            "identifiant": self.identifiant,
            "x": self.x,
            "y": self.y,
            "id_culture": self.id_culture
        }
    
    def est_vide(self) -> bool:
        return self.id_culture is None
    
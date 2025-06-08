from typing import Dict

class Joueur:
    def __init__(self, identifiant: str, argent: float = 100, graines: Dict[str, int] = None):
        self.identifiant = identifiant
        self.argent = argent

        if graines is not None:
            self.graines = graines
        else:
            self.graines = {
                "ble": 20,
                "carotte": 25,
                "mais": 15
            }

    def en_dictionnaire(self) -> Dict[str, object]:
        return {
            "identifiant": self.identifiant,
            "argent": self.argent,
            "graines": self.graines
        }

    def peut_planter(self, nom_culture: str) -> bool:
        return self.graines.get(nom_culture, 0) > 0

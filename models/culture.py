from typing import Dict

# Modèle de culture
class Culture:
    def __init__(self, identifiant: str, nom: str, temps_pousse: int, valeur: float, 
                 besoin_eau: float, age: int=0):
        self.identifiant = identifiant
        self.nom = nom
        self.temps_pousse = temps_pousse
        self.valeur = valeur
        self.besoin_eau = besoin_eau
        self.age = age

    def en_dictionnaire(self) -> Dict[str, object]:
        return {
            "identifiant": self.identifiant,
            "nom": self.nom,
            "temps_pousse": self.temps_pousse,
            "valeur": self.valeur,
            "besoin_eau": self.besoin_eau,
            "age": self.age
        }

    def est_mature(self) -> bool:
        return self.age >= self.temps_pousse
    

    

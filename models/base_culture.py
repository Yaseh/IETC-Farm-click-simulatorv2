from abc import ABC, abstractmethod
from typing import Dict

''' base_culture.py ← classe abstraite 'Culture' '''
class Culture(ABC):
    def __init__(self, identifiant: str, age: int = 0):
        self.identifiant = identifiant
        self.age = age

    @abstractmethod
    def nom(self) -> str:
        pass

    @abstractmethod
    def temps_pousse(self) -> int:
        pass

    @abstractmethod
    def valeur(self) -> float:
        pass

    @abstractmethod
    def besoin_eau(self) -> float:
        pass

    def est_mature(self) -> bool:
        return self.age >= self.temps_pousse()

    def vieillir(self) -> None:
        self.age += 1

    def en_dictionnaire(self) -> Dict[str, object]:
        return {
            "nom": self.nom(),
            "identifiant": self.identifiant,
            "age": self.age
        }

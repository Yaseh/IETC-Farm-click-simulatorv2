from repositories.base_depot_json import BaseDepotJson
from models.usine_culture import culture_depuis_dictionnaire
from models.culture import Culture

# Accès aux cultures
class DepotCulture(BaseDepotJson):
    def __init__(self):
        super().__init__(Culture, "data/cultures.json")

    ''' Gestion des exceptions si une mauvaise entrée réapparaît
        le jeu continue de fonctionner.'''
    def tout_recuperer(self):
        donnees = self._charger_donnees()
        cultures = []
        for d in donnees:
            try:
                cultures.append(culture_depuis_dictionnaire(d))
            except Exception as e:
                print(f"[ERREUR] Culture ignorée : {e}")
        return cultures

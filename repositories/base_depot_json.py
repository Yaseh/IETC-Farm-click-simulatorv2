import os
import json

class BaseDepotJson:
    def __init__(self, classe_modele, chemin_fichier):
        self.classe_modele = classe_modele
        self.chemin_fichier = chemin_fichier
        os.makedirs(os.path.dirname(self.chemin_fichier), exist_ok=True)

    def _charger_donnees(self):
        if not os.path.exists(self.chemin_fichier):
            return []
        with open(self.chemin_fichier, "r", encoding="utf-8") as fichier:
            return json.load(fichier)

    def _sauvegarder_donnees(self, donnees):
        with open(self.chemin_fichier, "w", encoding="utf-8") as fichier:
            json.dump(donnees, fichier, indent=4, ensure_ascii=False)

    def tout_recuperer(self):
        return [self.classe_modele(**d) for d in self._charger_donnees()]

    def trouver_par_id(self, identifiant):
        return next((objet for objet in self.tout_recuperer() if objet.identifiant == identifiant), None)

    def ajouter(self, objet):
        tous = self._charger_donnees()
        tous = [d for d in tous if d["identifiant"] != objet.identifiant]
        tous.append(objet.en_dictionnaire())
        self._sauvegarder_donnees(tous)

    def supprimer(self, identifiant):
        tous = self._charger_donnees()
        tous = [d for d in tous if d["identifiant"] != identifiant]
        self._sauvegarder_donnees(tous)

    def sauvegarder_tous(self, objets):
        self._sauvegarder_donnees([obj.en_dictionnaire() for obj in objets])

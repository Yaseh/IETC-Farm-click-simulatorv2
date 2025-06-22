from repositories.base_depot_json import BaseDepotJson
from factories.usine_animal import animal_depuis_dictionnaire
from models.animaux.base_animal import Animal

class DepotAnimal(BaseDepotJson):
    """
    Dépôt spécialisé pour la gestion des animaux.

    Hérite de `BaseDepotJson` et surcharge la méthode `tout_recuperer`
    pour utiliser une usine de création (`animal_depuis_dictionnaire`)
    afin de reconstruire correctement les objets `Animal`.

    Attributes:
        chemin_fichier (str): Chemin du fichier JSON utilisé pour stocker les animaux.
    """

    def __init__(self):
        """
        Initialise le dépôt des animaux avec le fichier JSON par défaut.

        Le fichier est situé dans `data/animaux.json`.
        """
        super().__init__(Animal, "data/animaux.json")

    def tout_recuperer(self):
        """
        Récupère tous les animaux enregistrés, en filtrant les entrées invalides.

        Utilise l'usine `animal_depuis_dictionnaire` pour convertir
        chaque entrée JSON en objet `Animal`.

        Returns:
            list: Liste des objets `Animal` valides.
        """
        donnees = self._charger_donnees()
        animaux = []
        for d in donnees:
            try:
                animaux.append(animal_depuis_dictionnaire(d))
            except Exception as e:
                print(f"[ERREUR] Animal ignoré : {e}")
        return animaux

from repositories.base_depot_json import BaseDepotJson
from factories.usine_batiment import batiment_depuis_dictionnaire
from models.batiments.base_batiment import Batiment

class DepotBatiment(BaseDepotJson):
    """
    Dépôt spécialisé pour la gestion des bâtiments.

    Hérite de `BaseDepotJson` et surcharge la méthode `tout_recuperer`
    pour utiliser une usine de création (`batiment_depuis_dictionnaire`)
    afin de reconstruire correctement les objets `Batiment`.

    Attributes:
        chemin_fichier (str): Chemin du fichier JSON utilisé pour stocker les bâtiments.
    """

    def __init__(self):
        """
        Initialise le dépôt des bâtiments avec le fichier JSON par défaut.

        Le fichier est situé dans `data/batiments.json`.
        """
        super().__init__(Batiment, "data/batiments.json")

    def tout_recuperer(self):
        """
        Récupère tous les bâtiments enregistrés, en filtrant les entrées invalides.

        Utilise l'usine `batiment_depuis_dictionnaire` pour convertir
        chaque entrée JSON en objet `Batiment`.

        Returns:
            list: Liste des objets `Batiment` valides.
        """
        donnees = self._charger_donnees()
        batiments = []
        for d in donnees:
            try:
                batiments.append(batiment_depuis_dictionnaire(d))
            except Exception as e:
                print(f"[ERREUR] Bâtiment ignoré : {e}")
        return batiments

from repositories.base_depot_json import BaseDepotJson
from models.case_ferme import CaseFerme

class DepotTuilesFerme(BaseDepotJson):
    """
    Dépôt spécialisé pour la gestion des tuiles de la ferme.

    Hérite de `BaseDepotJson` pour gérer la persistance des objets `CaseFerme`
    dans un fichier JSON.

    Attributes:
        chemin_fichier (str): Chemin du fichier JSON utilisé pour stocker les tuiles de la ferme.
    """

    def __init__(self):
        """
        Initialise le dépôt des tuiles de la ferme avec le fichier JSON par défaut.

        Le fichier est situé dans `data/ferme_tuiles.json`.
        """        
        super().__init__(CaseFerme, "data/ferme_tuiles.json")
        
from repositories.base_depot_json import BaseDepotJson
from models.ressources_joueur import RessourceJoueur

class DepotRessourceJoueur(BaseDepotJson):
    """
    Dépôt spécialisé pour la gestion des ressources du joueur.

    Hérite de `BaseDepotJson` pour gérer la persistance des objets `RessourceJoueur`
    dans un fichier JSON.

    Attributes:
        chemin_fichier (str): Chemin du fichier JSON utilisé pour stocker les ressources du joueur.
    """

    def __init__(self):
        """
        Initialise le dépôt des ressources du joueur avec le fichier JSON par défaut.

        Le fichier est situé dans `data/joueur.json`.
        """
        super().__init__(RessourceJoueur, "data/joueur.json")

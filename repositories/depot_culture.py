from repositories.base_depot_json import BaseDepotJson
from factories.usine_culture import culture_depuis_dictionnaire
from models.cultures.culture import Culture

class DepotCulture(BaseDepotJson):
    """
    Dépôt spécialisé pour la gestion des cultures.

    Hérite de `BaseDepotJson` et surcharge la méthode `tout_recuperer`
    pour utiliser une usine de création (`culture_depuis_dictionnaire`)
    afin de reconstruire correctement les objets `Culture`.

    Attributes:
        chemin_fichier (str): Chemin du fichier JSON utilisé pour stocker les cultures.
    """

    def __init__(self):
        """
        Initialise le dépôt des cultures avec le fichier JSON par défaut.

        Le fichier est situé dans `data/cultures.json`.
        """
        super().__init__(Culture, "data/cultures.json")

    def tout_recuperer(self):
        """
        Récupère toutes les cultures enregistrées, en filtrant les entrées invalides.

        Utilise l'usine `culture_depuis_dictionnaire` pour convertir
        chaque entrée JSON en objet `Culture`.

        Si une entrée est corrompue ou invalide, elle est ignorée
        et le jeu continue de fonctionner normalement.

        Returns:
            list: Liste des objets `Culture` valides.
        """
        donnees = self._charger_donnees()
        cultures = []
        for d in donnees:
            try:
                cultures.append(culture_depuis_dictionnaire(d))
            except Exception as e:
                print(f"[ERREUR] Culture ignorée : {e}")
        return cultures

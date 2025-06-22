class CataloguePrix:
    """
    Classe représentant un catalogue de prix et quantités standards pour les ressources du jeu.

    Cette classe gère les prix unitaires pour chaque type de ressource ou service,
    ainsi que certaines quantités par défaut pour des achats en gros (ex. : eau, nourriture).

    Attributes:
        _prix (dict): Dictionnaire des prix unitaires par ressource ou service.
        _quantite (dict): Quantité par défaut pour certaines ressources.
    """

    def __init__(self):
        """
        Initialise le catalogue des prix et des quantités par défaut.
        """
        self._prix = {
            "eau": 0.05,
            "médicament": 1,
            "nourriture_betails": 1.2,
            "graine": 5,
            "poule": 10,
            "mouton": 15,
            "vache": 20,
            "poulailler": 1000,
            "étable": 1500,
            "laiterie": 2000,
            "oeuf": 4,
            "lait": 6,
            "laine": 20,
            "mécanicien": 600,
            "plombier": 500,
            "électricien": 800
        }
        self._quantite = {
            "eau": 10000,
            "nourriture_betails": 100,
            "médicament": 10
        }

    def get(self, nom: str) -> float:
        """
        Récupère le prix unitaire d'une ressource ou service.

        Args:
            nom (str): Nom de la ressource ou du service.

        Returns:
            float: Prix unitaire. Retourne 0.0 si non défini.
        """
        return self._prix.get(nom, 0.0)

    def set(self, nom: str, montant: float):
        """
        Modifie ou ajoute le prix unitaire d'une ressource ou service.

        Args:
            nom (str): Nom de la ressource ou du service.
            montant (float): Nouveau prix unitaire.
        """
        self._prix[nom] = montant    
        
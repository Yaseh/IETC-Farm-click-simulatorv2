from models.animaux.base_animal import Animal

class Vache(Animal):
    """
    Classe représentant l'animal spécifique : la vache.

    Hérite de la classe abstraite `Animal` et redéfinit ses méthodes pour
    décrire les caractéristiques propres à la vache.
    """

    def nom(self) -> str:
        """
        Retourne le nom de l'animal.

        Returns:
            str: Le nom 'vache'.
        """
        return "vache"

    def temps_croissance(self) -> int:
        """
        Retourne le temps nécessaire à la croissance complète de la vache.

        Returns:
            int: Temps de croissance en jours (5).
        """
        return 5

    def type_alimentation(self) -> str:
        """
        Retourne le type d'alimentation de la vache.

        Returns:
            str: Type d'alimentation ('herbivore').
        """
        return "herbivore"

    def production(self) -> str:
        """
        Retourne le produit généré par la vache.

        Returns:
            str: Produit généré ('lait').
        """
        return "lait"

    def valeur(self) -> float:
        """
        Retourne la valeur marchande de la vache.

        Returns:
            float: Valeur en unités monétaires (500.0).
        """
        return 500.0

    def besoin_eau(self) -> float:
        """
        Retourne la quantité d'eau nécessaire pour la vache.

        Returns:
            float: Besoin en eau quotidien (50.0).
        """
        return 50.0

    def besoin_nourriture(self) -> float:
        """
        Retourne la quantité de nourriture nécessaire pour la vache.

        Returns:
            float: Besoin en nourriture quotidien (8.0).
        """
        return 8.0

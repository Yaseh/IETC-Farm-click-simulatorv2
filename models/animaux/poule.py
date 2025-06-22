from models.animaux.base_animal import Animal

class Poule(Animal):
    """
    Classe représentant l'animal spécifique : la poule.

    Hérite de la classe abstraite `Animal` et redéfinit ses méthodes pour
    décrire les caractéristiques propres à la poule.
    """

    def nom(self) -> str:
        """
        Retourne le nom de l'animal.

        Returns:
            str: Le nom 'poule'.
        """
        return "poule"

    def temps_croissance(self) -> int:
        """
        Retourne le temps nécessaire à la croissance complète de la poule.

        Returns:
            int: Temps de croissance en jours (5).
        """
        return 5

    def type_alimentation(self) -> str:
        """
        Retourne le type d'alimentation de la poule.

        Returns:
            str: Type d'alimentation ('granivore').
        """
        return "granivore"

    def production(self) -> str:
        """
        Retourne le produit généré par la poule.

        Returns:
            str: Produit généré ('œufs').
        """
        return "œufs"

    def valeur(self) -> float:
        """
        Retourne la valeur marchande de la poule.

        Returns:
            float: Valeur en unités monétaires (25.0).
        """
        return 25.0

    def besoin_eau(self) -> float:
        """
        Retourne la quantité d'eau nécessaire pour la poule.

        Returns:
            float: Besoin en eau quotidien (0.2).
        """
        return 0.2

    def besoin_nourriture(self) -> float:
        """
        Retourne la quantité de nourriture nécessaire pour la poule.

        Returns:
            float: Besoin en nourriture quotidien (1.0).
        """
        return 1.0  


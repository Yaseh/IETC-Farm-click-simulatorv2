from models.animaux.base_animal import Animal

class Mouton(Animal):
    """
    Classe représentant l'animal spécifique : le mouton.

    Hérite de la classe abstraite `Animal` et redéfinit ses méthodes pour
    décrire les caractéristiques propres au mouton.
    """

    def nom(self) -> str:
        """
        Retourne le nom de l'animal.

        Returns:
            str: Le nom 'mouton'.
        """
        return "mouton"

    def temps_croissance(self) -> int:
        """
        Retourne le temps nécessaire à la croissance complète du mouton.

        Returns:
            int: Temps de croissance en jours (5).
        """
        return 5

    def type_alimentation(self) -> str:
        """
        Retourne le type d'alimentation du mouton.

        Returns:
            str: Type d'alimentation ('herbivore').
        """
        return "herbivore"

    def production(self) -> str:
        """
        Retourne le produit généré par le mouton.

        Returns:
            str: Produit généré ('laine').
        """
        return "laine"

    def valeur(self) -> float:
        """
        Retourne la valeur marchande du mouton.

        Returns:
            float: Valeur en unités monétaires (80.0).
        """
        return 80.0

    def besoin_eau(self) -> float:
        """
        Retourne la quantité d'eau nécessaire pour le mouton.

        Returns:
            float: Besoin en eau quotidien (5.0).
        """
        return 5.0

    def besoin_nourriture(self) -> float:
        """
        Retourne la quantité de nourriture nécessaire pour le mouton.

        Returns:
            float: Besoin en nourriture quotidien (2.0).
        """
        return 2.0

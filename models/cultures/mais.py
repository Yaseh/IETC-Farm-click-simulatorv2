from models.cultures.base_culture import Culture

class Mais(Culture):
    """
    Classe représentant la culture spécifique du maïs.

    Hérite de la classe abstraite `Culture` et implémente
    ses méthodes pour fournir les caractéristiques propres au maïs.
    """

    def nom(self) -> str:
        """
        Retourne le nom de cette culture.

        Returns:
            str: Le nom 'maïs'.
        """
        return "maïs"

    def temps_pousse(self) -> int:
        """
        Retourne le nombre de jours nécessaires à la croissance complète du maïs.

        Returns:
            int: Temps de pousse en jours (3).
        """
        return 3

    def valeur(self) -> float:
        """
        Retourne la valeur de revente du maïs une fois récolté.

        Returns:
            float: Valeur marchande (6.0).
        """
        return 6.0 

    def besoin_eau(self) -> float:
        """
        Retourne la quantité d'eau nécessaire pour faire pousser le maïs.

        Returns:
            float: Besoin en eau (0.7).
        """
        return 0.7

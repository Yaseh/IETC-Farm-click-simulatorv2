from models.cultures.base_culture import Culture

class Carotte(Culture):
    """
    Classe représentant la culture spécifique de la carotte.

    Hérite de la classe de base `Culture` et redéfinit ses propriétés
    pour refléter les caractéristiques propres à la carotte.
    """

    def nom(self) -> str:
        """
        Retourne le nom de la culture.

        Returns:
            str: Le nom 'carotte'.
        """
        return "carotte"

    def temps_pousse(self) -> int:
        """
        Retourne le temps de croissance complet pour la carotte.

        Returns:
            int: Nombre de jours nécessaires pour atteindre la maturité (3).
        """
        return 3

    def valeur(self) -> float:
        """
        Retourne la valeur marchande de la carotte.

        Returns:
            float: Valeur en unités monétaires (8.0).
        """
        return 8.0

    # Moins exigeant en eau
    def besoin_eau(self) -> float:
        """
        Retourne la quantité d'eau nécessaire pour la carotte.

        Returns:
            float: Besoin en eau (0.5).
        """
        return 0.5  
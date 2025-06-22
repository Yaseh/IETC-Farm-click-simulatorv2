from models.cultures.base_culture import Culture

class Ble(Culture):
    """
    Classe représentant la culture spécifique du blé.

    Hérite de la classe abstraite `Culture` et redéfinit ses propriétés
    pour refléter les caractéristiques propres au blé.
    """    
    
    def nom(self) -> str:
        """
        Retourne le nom de la culture.

        Returns:
            str: Le nom 'blé'.
        """
        return "blé"
    
    def temps_pousse(self) -> int:
        """
        Retourne le temps de croissance complet pour le blé.

        Returns:
            int: Nombre de jours nécessaires pour atteindre la maturité (3).
        """
        return 3

    def valeur(self) -> float:
        """
        Retourne la valeur marchande du blé.

        Returns:
            float: Valeur en unités monétaires (10.0).
        """
        return 10.0

    # Besoin en eau important
    def besoin_eau(self) -> float:
        """
        Retourne la quantité d'eau nécessaire pour le blé.

        Returns:
            float: Besoin en eau (4.0).
        """
        return 4  
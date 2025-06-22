from models.batiments.base_batiment import Batiment

class Laiterie(Batiment):
    """
    Classe représentant un bâtiment de type laiterie.

    Hérite de la classe `Batiment` et redéfinit ses propriétés et méthodes
    pour décrire les caractéristiques spécifiques d'une laiterie.
    """

    def nom(self) -> str:
        """
        Retourne le nom du bâtiment.

        Returns:
            str: Le nom 'laiterie'.
        """
        return "laiterie"
    
    @property
    def produit(self) -> str:
        """
        Retourne le produit généré par la laiterie.

        Returns:
            str: Le produit 'lait'.
        """
        return "lait"  

    def capacite_animaux(self) -> int:
        """
        Retourne la capacité maximale d'animaux accueillis dans la laiterie.

        Returns:
            int: Capacité maximale (12 animaux).
        """
        return 12
    
    def production_journaliere(self) -> float:
        """
        Retourne la quantité de production quotidienne de la laiterie.

        Returns:
            float: Production journalière (60 unités).
        """
        return 60

    def cout_entretien(self) -> float:
        """
        Retourne le coût d'entretien journalier de la laiterie.

        Returns:
            float: Coût d'entretien (22.0 unités monétaires).
        """
        return 22.0
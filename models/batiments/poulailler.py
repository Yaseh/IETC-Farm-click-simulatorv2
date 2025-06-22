from models.batiments.base_batiment import Batiment

class Poulailler(Batiment):
    """
    Classe représentant un bâtiment de type poulailler.

    Hérite de la classe `Batiment` et redéfinit ses propriétés et méthodes
    pour correspondre aux caractéristiques spécifiques d'un poulailler.
    """
    def nom(self) -> str:
        """
        Retourne le nom du bâtiment.

        Returns:
            str: Le nom 'poulailler'.
        """
        return "poulailler"

    @property
    def produit(self) -> str:
        """
        Retourne le produit généré par le poulailler.

        Returns:
            str: Le produit 'oeuf'.
        """
        return "oeuf"  

    def capacite_animaux(self) -> int:
        """
        Retourne la capacité maximale d'animaux du poulailler.

        Returns:
            int: Nombre maximum d'animaux (40).
        """
        return 40

    def production_journaliere(self) -> float:
        """
        Retourne la quantité de production quotidienne du poulailler.

        Returns:
            float: Production journalière (80 unités).
        """
        return 80

    def cout_entretien(self) -> float:
        """
        Retourne le coût d'entretien journalier du poulailler.

        Returns:
            float: Coût d'entretien (15.0 unités monétaires).
        """
        return 15.0

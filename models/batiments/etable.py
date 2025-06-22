from models.batiments.base_batiment import Batiment

class Etable(Batiment):
    """
    Classe représentant un bâtiment de type étable.

    Hérite de la classe `Batiment` et redéfinit ses propriétés et méthodes
    pour décrire les caractéristiques spécifiques d'une étable.
    """

    def nom(self) -> str:
        """
        Retourne le nom du bâtiment.

        Returns:
            str: Le nom 'étable'.
        """
        return "étable"
    
    @property
    def produit(self) -> str:
        """
        Retourne le produit généré par l'étable.

        Returns:
            str: Le produit 'laine'.
        """
        return "laine"   

    def capacite_animaux(self) -> int:
        """
        Retourne la capacité maximale d'animaux hébergés dans l'étable.

        Returns:
            int: Capacité maximale (24 animaux).
        """
        return 24
    
    def production_journaliere(self) -> float:
        """
        Retourne la quantité de production quotidienne de l'étable.

        Returns:
            float: Production journalière (40 unités).
        """
        return 40

    def cout_entretien(self) -> float:
        """
        Retourne le coût d'entretien journalier de l'étable.

        Returns:
            float: Coût d'entretien (22.0 unités monétaires).
        """
        return 22.0
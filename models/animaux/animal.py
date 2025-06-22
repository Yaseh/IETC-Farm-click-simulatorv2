from typing import Dict

class Animal:
    """
    Classe représentant un modèle concret d'animal.

    Cette classe définit les propriétés et comportements généraux
    pour un animal de la ferme : identité, croissance, santé,
    besoins en ressources et valeur.

    Attributes:
        identifiant (str): Identifiant unique de l'animal.
        nom (str): Nom de l'animal.
        temps_croissance (int): Durée de croissance en jours.
        valeur (float): Valeur marchande de l'animal.
        besoin_eau (float): Besoin quotidien en eau.
        besoin_nourriture (float): Besoin quotidien en nourriture.
        age (int): Âge actuel de l'animal.
    """

    def __init__(self, identifiant: str, nom: str, temps_croissance: int,
        valeur: float, besoin_eau: float, besoin_nourriture: float, age: int = 0):
        """
        Initialise les caractéristiques principales de l'animal.

        Args:
            identifiant (str): Identifiant unique.
            nom (str): Nom de l'animal.
            temps_croissance (int): Durée de croissance en jours.
            valeur (float): Valeur marchande.
            besoin_eau (float): Besoin quotidien en eau.
            besoin_nourriture (float): Besoin quotidien en nourriture.
            age (int, optional): Âge initial. Par défaut 0.
        """
        self.identifiant = identifiant
        self.nom = nom
        self.temps_croissance = temps_croissance
        self.valeur = valeur
        self.besoin_eau = besoin_eau
        self.besoin_nourriture = besoin_nourriture
        self.age = age

    def soigner(self, ressources_joueur, repo_animaux, repo_ressources_joueur):
        """
        Soigne l'animal s'il est malade, en consommant un médicament
        et en mettant à jour les dépôts associés.

        Args:
            ressources_joueur (object): Ressources du joueur (pour les médicaments).
            repo_animaux (object): Dépôt des animaux.
            repo_ressources_joueur (object): Dépôt des ressources du joueur.
        """
        if not self.est_malade:
            print(f"L'animal {self.nom()} n'est pas malade.")
            return
        if ressources_joueur.medicaments <= 0:
            print("Pas de médicaments disponibles.")
            return
        self.est_malade = False
        ressources_joueur.medicaments -= 1
        repo_animaux.ajouter(self)
        repo_ressources_joueur.ajouter(ressources_joueur)
        print(f"{self.nom()} soigné avec succès !")

    def tomber_malade(self):
        """
        Marque l'animal comme malade.
        """
        if not self.est_malade:
            self.est_malade = True

    def est_adulte(self) -> bool:
        """
        Vérifie si l'animal est adulte.

        Returns:
            bool: True si l'âge est au moins égal à l'âge de maturité.
        """
        return self.age >= self.age_maturite

    def en_dictionnaire(self) -> Dict[str, object]:
        """
        Convertit les informations de l'animal en dictionnaire.

        Returns:
            dict: Dictionnaire avec les attributs principaux.
        """
        return {
            "identifiant": self.identifiant,
            "nom": self.nom,
            "temps_croissance": self.temps_croissance,
            "valeur": self.valeur,
            "besoin_eau": self.besoin_eau,
            "besoin_nourriture": self.besoin_nourriture,
            "age": self.age
        }
import os
import json

class BaseDepotJson:
    """
    Classe générique pour gérer la persistance des objets sous forme JSON.

    Cette classe fournit les opérations CRUD (Créer, Lire, Mettre à jour, Supprimer)
    pour toute classe modèle disposant d'une méthode `en_dictionnaire`.

    Attributes:
        classe_modele (type): Classe des objets à manipuler.
        chemin_fichier (str): Chemin du fichier JSON de stockage.
    """

    def __init__(self, classe_modele, chemin_fichier):
        """
        Initialise le dépôt avec une classe modèle et un chemin de fichier.

        Args:
            classe_modele (type): Classe des objets à sérialiser/désérialiser.
            chemin_fichier (str): Chemin vers le fichier JSON.
        """
        self.classe_modele = classe_modele
        self.chemin_fichier = chemin_fichier
        os.makedirs(os.path.dirname(self.chemin_fichier), exist_ok=True)

    def _charger_donnees(self):
        """
        Charge les données JSON depuis le fichier.

        Returns:
            list: Liste des données chargées ou une liste vide si le fichier n'existe pas.
        """
        if not os.path.exists(self.chemin_fichier):
            return []
        with open(self.chemin_fichier, "r", encoding="utf-8") as fichier:
            return json.load(fichier)

    def _sauvegarder_donnees(self, donnees):
        """
        Sauvegarde une liste de données dans le fichier JSON.

        Args:
            donnees (list): Liste de dictionnaires à enregistrer.
        """
        with open(self.chemin_fichier, "w", encoding="utf-8") as fichier:
            json.dump(donnees, fichier, indent=4, ensure_ascii=False)

    def tout_recuperer(self):
        """
        Récupère tous les objets stockés sous forme d'instances de la classe modèle.

        Returns:
            list: Liste d'objets instanciés à partir du fichier JSON.
        """
        return [self.classe_modele(**d) for d in self._charger_donnees()]

    def trouver_par_id(self, identifiant):
        """
        Recherche un objet par son identifiant unique.

        Args:
            identifiant (str): Identifiant de l'objet à trouver.

        Returns:
            object or None: Objet correspondant ou None si non trouvé.
        """
        return next((objet for objet in self.tout_recuperer() if objet.identifiant == identifiant), None)

    def ajouter(self, objet):
        """
        Ajoute un nouvel objet ou met à jour un objet existant
        en le remplaçant s'il a le même identifiant.

        Args:
            objet (object): Objet à ajouter ou mettre à jour.
        """
        tous = self._charger_donnees()
        tous = [d for d in tous if d["identifiant"] != objet.identifiant]
        tous.append(objet.en_dictionnaire())
        self._sauvegarder_donnees(tous)

    def supprimer(self, identifiant):
        """
        Supprime un objet du fichier JSON en fonction de son identifiant.

        Args:
            identifiant (str): Identifiant de l'objet à supprimer.
        """
        tous = self._charger_donnees()
        tous = [d for d in tous if d["identifiant"] != identifiant]
        self._sauvegarder_donnees(tous)

    def sauvegarder_tous(self, objets):
        """
        Sauvegarde une liste complète d'objets en remplaçant toutes les données existantes.

        Args:
            objets (list): Liste d'objets à sauvegarder.
        """
        self._sauvegarder_donnees([obj.en_dictionnaire() for obj in objets])

    def vider(self):
        """
        Vide complètement le fichier JSON (supprime tous les objets).
        """
        self._sauvegarder_donnees([])

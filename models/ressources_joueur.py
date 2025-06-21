from typing import Dict
from repositories.depot_batiment import DepotBatiment
from utils.constantes import *
from utils.catalogue_prix import CataloguePrix
from utils.generateur_identifiant import generer_identifiant
from utils.mode_selection import ModeSelection

class RessourceJoueur:
    """
    Classe représentant les ressources possédées par un joueur, incluant argent,
    graines, animaux, bâtiments, techniciens, eau, nourriture pour bétails et médicaments.

    Attributes:
        identifiant (str): Identifiant unique du joueur.
        argent (float): Montant d'argent disponible.
        medicaments (int): Nombre de médicaments.
        eau (float): Quantité d'eau disponible.
        nourriture_betails (int): Quantité de nourriture pour le bétail.
        catalogue_prix (CataloguePrix): Catalogue des prix des ressources.
        graines (dict): Quantité de graines pour chaque culture.
        animaux (dict): Nombre d'animaux pour chaque type.
        batiments (dict): Nombre de bâtiments pour chaque type.
        production_batiments (dict): Production quotidienne par bâtiment.
        techniciens (dict): Nombre de techniciens par métier.
    """
    
    def __init__(self, identifiant: str, argent: float = 1500, medicaments: int = 0, 
                 graines: Dict[str, int] = None, animaux: Dict[str, int] = None,
                 batiments: Dict[str, int] = None, production_batiments: Dict[str, int] = None, 
                 techniciens: Dict[str, int] = None, eau: float = 100000.0, 
                 nourriture_betails: int = 200):
        """
        Initialise les ressources du joueur avec des valeurs par défaut ou fournies.

        Args:
            identifiant (str): Identifiant unique du joueur.
            argent (float, optional): Montant initial d'argent. Par défaut 1500.
            medicaments (int, optional): Quantité initiale de médicaments. Par défaut 0.
            graines (dict, optional): Quantité initiale de chaque graine. Par défaut valeurs par défaut.
            animaux (dict, optional): Quantité initiale de chaque animal. Par défaut valeurs par défaut.
            batiments (dict, optional): Quantité initiale de chaque bâtiment. Par défaut valeurs par défaut.
            production_batiments (dict, optional): Production initiale par bâtiment. Par défaut valeurs par défaut.
            techniciens (dict, optional): Nombre initial de techniciens. Par défaut valeurs par défaut.
            eau (float, optional): Quantité initiale d'eau. Par défaut 100000.0.
            nourriture_betails (int, optional): Quantité initiale de nourriture pour bétail. Par défaut 200.
        """
        self.identifiant = identifiant
        self.argent = argent
        self.medicaments = medicaments
        self.eau = eau
        self.nourriture_betails = nourriture_betails
        self.catalogue_prix = CataloguePrix()

        if graines is not None:
            self.graines = graines
        else:
            self.graines = {nom: 0 for nom in NOMS_CULTURES}
            self.graines["blé"] = 5
            self.graines["carotte"] = 5
            self.graines["maïs"] = 5

        if animaux is not None:
            self.animaux = animaux
        else:
            self.animaux = {nom: 0 for nom in NOMS_ANIMAUX}
            self.animaux["poule"] = 3
            self.animaux["mouton"] = 2            
            self.animaux["vache"] = 1

        if batiments is not None:
            self.batiments = batiments
        else:
            self.batiments = {nom: 0 for nom in NOMS_BATIMENTS}
            self.batiments["poulailler"] = 2
            self.batiments["étable"] = 1
            self.batiments["laiterie"] = 1

        if production_batiments is not None:
            self.production_batiments = production_batiments
        else:
            self.production_batiments = {nom: 0 for nom in NOMS_PRODUCTION_BATIMENTS}
            self.production_batiments["oeuf"] = 30
            self.production_batiments["laine"] = 50
            self.production_batiments["lait"] = 20

        if techniciens is not None:
            self.techniciens = techniciens
        else:
            self.techniciens = {nom: 0 for nom in NOMS_TECHNICIENS}
            self.techniciens["mécanicien"] = 1
            self.techniciens["plombier"] = 1
            self.techniciens["électricien"] = 1        
            
    def _acheter(self, nom: str, prix: float, type_de_ressources: dict = None, quantite: int = 1,
                  effet=None, repo=None):
        """
        Achète une ressource générique si le joueur a assez d'argent.

        Args:
            nom (str): Nom de la ressource à acheter.
            prix (float): Prix unitaire de la ressource.
            type_de_ressources (dict, optional): Dictionnaire où incrémenter la ressource achetée.
            quantite (int, optional): Quantité à acheter. Par défaut 1.
            effet (callable, optional): Effet spécial à appliquer après achat.
            repo (object, optional): Dépôt pour mettre à jour l'état des ressources.
        """
        if self.argent >= prix * quantite:
            self.argent -= prix * quantite
            if type_de_ressources is not None:
                type_de_ressources[nom] += quantite
            if effet:
                effet()  # pour cas spéciaux : eau, etc.
            if repo is not None:
                repo.ajouter(self)
            print(f"Achat réussi : {nom} (+{quantite}) pour {prix * quantite}€")
        else:
            print(f"Pas assez d'argent pour acheter {nom}.")

    def _vendre(self, case, mode: ModeSelection, repo_cultures, repo_animaux, repo_cases, repo_ressources_joueur):
        """
        Vend une culture ou un animal mature selon le mode de sélection.

        Args:
            case (object): Case contenant l'élément à vendre.
            mode (ModeSelection): Mode de vente (CULTURE ou ANIMAL).
            repo_cultures (object): Dépôt des cultures.
            repo_animaux (object): Dépôt des animaux.
            repo_cases (object): Dépôt des cases.
            repo_ressources_joueur (object): Dépôt pour mettre à jour les ressources du joueur.
        """        
        if mode == ModeSelection.CULTURE and case.id_culture:
            element = repo_cultures.trouver_par_id(case.id_culture)
            age_max = element.temps_pousse() if element else 0
            repo = repo_cultures
            id_attr = "id_culture"
        elif mode == ModeSelection.ANIMAL and case.id_animal:
            element = repo_animaux.trouver_par_id(case.id_animal)
            age_max = element.temps_croissance() if element else 0
            repo = repo_animaux
            id_attr = "id_animal"
        else:
            return  # Rien à vendre

        if element and element.age >= age_max:
            repo.supprimer(element.identifiant)
            setattr(case, id_attr, None)
            repo_cases.ajouter(case)
            self.argent += element.valeur()
            repo_ressources_joueur.ajouter(self)

    def acheter_graine(self, nom_culture: str, repo=None):
        """
        Achète une graine pour une culture spécifique.

        Args:
            nom_culture (str): Nom de la culture dont acheter la graine.
            repo (object, optional): Dépôt pour mise à jour.
        """
        self._acheter(nom_culture, self.catalogue_prix.get("graine"), type_de_ressources=self.graines, repo=repo)

    def acheter_animal(self, nom_animal: str, repo=None):
        """
        Achète un animal spécifique.

        Args:
            nom_animal (str): Nom de l'animal à acheter.
            repo (object, optional): Dépôt pour mise à jour.
        """        
        self._acheter(nom_animal, self.catalogue_prix.get(nom_animal), type_de_ressources=self.animaux, repo=repo)

    def acheter_batiment(self, nom_batiment: str, repo=None):
        """
        Achète un bâtiment spécifique.

        Args:
            nom_batiment (str): Nom du bâtiment à acheter.
            repo (object, optional): Dépôt pour mise à jour.
        """
        self._acheter(nom_batiment, self.catalogue_prix.get(nom_batiment), type_de_ressources=self.batiments, repo=repo)

    def acheter_technicien(self, nom_technicien: str, repo_batiments=None, repo_ressources=None):
        """
        Achète un technicien pour réparer une panne éventuelle ou en ajouter un.

        Args:
            nom_technicien (str): Type de technicien à acheter.
            repo_batiments (object, optional): Dépôt des bâtiments (non utilisé ici).
            repo_ressources (object, optional): Dépôt pour mise à jour des ressources.
        """
        # 1️⃣ Achat normal
        self._acheter(nom_technicien, self.catalogue_prix.get(nom_technicien), type_de_ressources=self.techniciens, 
                      repo=repo_ressources)
        # 2️⃣ Si une panne globale existe et que le technicien correspond, réparer immédiatement
        if hasattr(self, 'jeu') and self.jeu.panne_actuelle == nom_technicien:
            if self.techniciens[nom_technicien] > 0:
                self.techniciens[nom_technicien] -= 1
                self.jeu.panne_actuelle = None
                print(f"🔧 Panne globale réparée grâce au nouveau {nom_technicien} acheté !")
            else:
                print(f"❌ Impossible de réparer la panne globale, pas assez de {nom_technicien}.")

    def acheter_eau(self, repo=None):
        """
        Achète une certaine quantité d'eau.

        Args:
            repo (object, optional): Dépôt pour mise à jour.
        """
        quant = self.catalogue_prix._quantite.get("eau", 1)
        self._acheter("eau", prix=self.catalogue_prix.get("eau"), quantite=quant,
                      effet=lambda: setattr(self, "eau", self.eau + quant), repo=repo)

    def acheter_medicament(self, repo=None):
        """
        Achète une certaine quantité de médicaments.

        Args:
            repo (object, optional): Dépôt pour mise à jour.
        """
        quant = self.catalogue_prix._quantite.get("médicament", 1)      
        self._acheter("médicament", prix=self.catalogue_prix.get("médicament"), quantite=quant,
                      effet=lambda: setattr(self, "medicaments", self.medicaments + quant), repo=repo)

    def acheter_nourriture_betails(self, repo=None):
        """
        Achète une certaine quantité de nourriture pour le bétail.

        Args:
            repo (object, optional): Dépôt pour mise à jour.
        """
        quant = self.catalogue_prix._quantite.get("nourriture_betails", 1)
        self._acheter("nourriture_betails", prix=self.catalogue_prix.get("nourriture_betails"), quantite=quant,
                      effet=lambda: setattr(self, "nourriture_betails", self.nourriture_betails + quant), repo=repo)

    def recolter(self, case, repo_cultures, repo_animaux, repo_cases, repo_ressources_joueur):
        """
        Récolte une culture mature d'une case.

        Args:
            case (object): Case à récolter.
            repo_cultures (object): Dépôt des cultures.
            repo_animaux (object): Dépôt des animaux.
            repo_cases (object): Dépôt des cases.
            repo_ressources_joueur (object): Dépôt pour mise à jour des ressources.
        """
        self._vendre(case, ModeSelection.CULTURE, repo_cultures, repo_animaux, repo_cases, repo_ressources_joueur)

    def vendre_animal(self, case, repo_cultures, repo_animaux, repo_cases, repo_ressources_joueur):
        """
        Vend un animal mature d'une case.

        Args:
            case (object): Case contenant l'animal.
            repo_cultures (object): Dépôt des cultures.
            repo_animaux (object): Dépôt des animaux.
            repo_cases (object): Dépôt des cases.
            repo_ressources_joueur (object): Dépôt pour mise à jour des ressources.
        """
        self._vendre(case, ModeSelection.ANIMAL, repo_cultures, repo_animaux, repo_cases, repo_ressources_joueur)

    def vendre_batiment(self, batiment_id: str, repo_batiments, repo_cases, repo_ressources_joueur, obtenir_case):
        """
        Vend un bâtiment en le supprimant du dépôt et libère ses cases.

        Args:
            batiment_id (str): Identifiant du bâtiment à vendre.
            repo_batiments (object): Dépôt des bâtiments.
            repo_cases (object): Dépôt des cases.
            repo_ressources_joueur (object): Dépôt pour mise à jour des ressources.
            obtenir_case (callable): Fonction pour obtenir une case par coordonnées.
        """
        # Récupère le bâtiment à supprimer
        batiment = repo_batiments.trouver_par_id(batiment_id)
        if not batiment:
            print(f"Aucun bâtiment avec l'id {batiment_id} trouvé.")
            return
        # 1️⃣ Libère toutes les cases occupées par ce bâtiment
        for dx in range(batiment.largeur):
            for dy in range(batiment.hauteur):
                case = obtenir_case(batiment.x + dx, batiment.y + dy)
                if case and case.id_batiment == batiment_id:
                    case.id_batiment = None
                    repo_cases.ajouter(case)
        # 2️⃣ Supprime le bâtiment du dépôt
        repo_batiments.supprimer(batiment_id)
        # 3️⃣ Ajoute un revenu à la vente (optionnel)
        revenu = batiment.production_journaliere() * 10  # ex: 10 jours de revenu
        self.argent += revenu
        repo_ressources_joueur.ajouter(self)
        print(f"{batiment.nom()} vendu pour {revenu}€.")

    def calculer_besoin_eau_et_nourriture_batiments(self) -> tuple[float, float]:
        """
        Calcule le besoin total en nourriture et en eau pour tous les bâtiments existants,
        en tenant compte du type d’animal hébergé par chaque bâtiment.
        
        Returns:
            tuple: Besoin total en nourriture et en eau.
        """
        repo_bat = DepotBatiment()
        liste_batiments = repo_bat.tout_recuperer()
        compteur = {}
        for bat in liste_batiments:
            nom = bat.nom()
            if nom in compteur:
                compteur[nom] += 1
            else:
                compteur[nom] = 1
        total_nourriture = 0.0
        total_eau = 0.0
        for nom_bat, quantite in compteur.items():
            batiments_type = []
            for b in liste_batiments:
                if b.nom() == nom_bat:
                    batiments_type.append(b)
            if batiments_type:
                capacite = batiments_type[0].capacite_animaux()
            else:
                capacite = 0
            # 🐑 Déduire le type d’animal à partir du bâtiment
            if "poulailler" in nom_bat:
                animal = CLASSES_ANIMAUX["poule"](identifiant=generer_identifiant())
            elif "étable" in nom_bat:
                animal = CLASSES_ANIMAUX["mouton"](identifiant=generer_identifiant())
            elif "laiterie" in nom_bat:
                animal = CLASSES_ANIMAUX["vache"](identifiant=generer_identifiant())
            else:
                animal = None
            if animal:
                besoin_nourriture_par_animal = animal.besoin_nourriture()
                besoin_eau_par_animal = animal.besoin_eau()
            else:
                besoin_nourriture_par_animal = 0.0
                besoin_eau_par_animal = 0.0
            total_nourriture += quantite * capacite * besoin_nourriture_par_animal
            total_eau += quantite * capacite * besoin_eau_par_animal
        return total_nourriture, total_eau

    def calculer_revenu_batiments(self, panne_actuelle=None) -> float:
        """
        Calcule le revenu total généré par les bâtiments après déduction des coûts d'entretien.

        Args:
            panne_actuelle (str, optional): Type de panne actuelle qui bloque la production.

        Returns:
            float: Revenu net total généré par les bâtiments.
        """
        revenu_total = 0.0
        repo_bat = DepotBatiment()
        liste_batiments = repo_bat.tout_recuperer()
        compteur = {}
        for bat in liste_batiments:
            nom = bat.nom()
            if nom in compteur:
                compteur[nom] += 1
            else:
                compteur[nom] = 1
        for nom_bat, quantite in compteur.items():
            produit = PRODUIT_PAR_BATIMENT.get(nom_bat)
            if produit is None:
                continue
            batiments_type = []
            for b in liste_batiments:
                if b.nom() == nom_bat:
                    batiments_type.append(b)
            total_production = 0.0
            for b in batiments_type:
                if panne_actuelle is not None:
                    prod = 0.0
                else:
                    prod = b.production_journaliere()
                total_production += prod
            if batiments_type:
                cout_ent = batiments_type[0].cout_entretien()
            else:
                cout_ent = 0.0
            prix_unitaire = self.catalogue_prix.get(produit)
            revenu_brut = total_production * prix_unitaire
            revenu_net = revenu_brut - quantite * cout_ent
            if revenu_net > 0.0:
                revenu_total += revenu_net
            else:
                revenu_total += 0.0
        return revenu_total
    
    def tomber_en_panne(self, batiment, type_de_de_panne_metier: str):
        """
        Déclare un bâtiment en panne et définit le type de technicien requis pour la réparer.

        Args:
            batiment (object): Bâtiment à marquer en panne.
            type_de_de_panne_metier (str): Type de technicien requis pour la réparation.

        Raises:
            ValueError: Si le type de panne est inconnu.
        """
        if not batiment.est_en_panne:
            self.est_en_panne = True
            if type_de_de_panne_metier not in ("mécanicien", "plombier", "électricien"):
                raise ValueError(f"Type de panne inconnue : {type_de_de_panne_metier}")
            batiment.est_en_panne = True
            batiment.type_de_de_panne_metier = type_de_de_panne_metier
            print(f"{self.nom()} en panne ({type_de_de_panne_metier})")

        
    def en_dictionnaire(self) -> Dict[str, object]:
        """
        Convertit l'état actuel des ressources du joueur en dictionnaire.

        Returns:
            dict: Dictionnaire des ressources et de leur valeur actuelle.
        """
        return {
            "identifiant": self.identifiant,
            "argent": self.argent,
            "medicaments": self.medicaments,
            "eau": self.eau,
            "nourriture_betails": self.nourriture_betails,
            "graines": self.graines,
            "animaux": self.animaux,
            "batiments": self.batiments,
            "production_batiments" : self.production_batiments,
            "techniciens": self.techniciens
        }  

import random
from models.case_ferme import CaseFerme
from repositories.depot_tuile_ferme import DepotTuilesFerme
from repositories.depot_culture import DepotCulture
from repositories.depot_animal import DepotAnimal
from repositories.depot_batiment import DepotBatiment
from repositories.depot_ressource_joueur import DepotRessourceJoueur
from models.ressources_joueur import RessourceJoueur
from game.meteo import Meteo
from utils.constantes import HAUTEUR_GRILLE, LARGEUR_GRILLE, NOMS_TECHNICIENS, TAILLE_GRILLE
from utils.generateur_identifiant import generer_identifiant
from utils.mode_selection import ModeSelection

class Jeu:
    """
    Classe principale représentant le moteur du jeu de ferme.

    Cette classe centralise :
    - La gestion des dépôts (cases, cultures, animaux, bâtiments, ressources).
    - La météo quotidienne.
    - La progression du jeu jour après jour.
    - Les actions principales : achat, revente, plantation, soin, production.

    Attributes:
        repo_cases (DepotTuilesFerme): Dépôt des cases de la ferme.
        repo_cultures (DepotCulture): Dépôt des cultures.
        repo_animaux (DepotAnimal): Dépôt des animaux.
        repo_batiments (DepotBatiment): Dépôt des bâtiments.
        repo_ressources_joueur (DepotRessourceJoueur): Dépôt des ressources du joueur.
        meteo_du_jour (Meteo): Météo actuelle.
        ressources (RessourceJoueur): Ressources du joueur actif.
        jour (int): Compteur de jours écoulés.
        panne_actuelle (str or None): Type de panne active ou None.
    """

    def __init__(self):
        """
        Initialise le jeu : charge ou crée les données, configure la météo et le jour courant.
        """
        self.repo_cases = DepotTuilesFerme()
        self.repo_cultures = DepotCulture()
        self.repo_animaux = DepotAnimal()
        self.repo_batiments = DepotBatiment()
        self.repo_ressources_joueur = DepotRessourceJoueur()
        self.meteo_du_jour = Meteo()
        self.cases = self.repo_cases.tout_recuperer()
        self.cultures = self.repo_cultures.tout_recuperer()
        ressources = self.repo_ressources_joueur.tout_recuperer()
        if ressources:
            self.ressources = ressources[0]
        else:
            self.ressources = RessourceJoueur(identifiant=generer_identifiant(), argent=100)
            self.repo_ressources_joueur.ajouter(self.ressources)
        self.jour = 1
        self.panne_actuelle = None

    def _calculer_consommation_eau_animaux(self):
        """
        Calcule la consommation totale d'eau pour tous les animaux existants.

        Returns:
            float: Quantité totale d'eau requise par les animaux.
        """
        consommation_eau_par_jour = 0
        for animal in self.repo_animaux.tout_recuperer():
            consommation_eau_par_jour += animal.besoin_eau()
        return consommation_eau_par_jour
    
    def _ajouter_eau_de_pluie(self):
        """
        Ajoute de l'eau à la réserve si la météo du jour est Pluie.

        Le volume ajouté dépend de la taille de la grille : ici 10x10
        """
        if self.meteo_du_jour.afficher() == "Pluie":
            ajout_eau = 30 * TAILLE_GRILLE[0] * TAILLE_GRILLE[1]
            self.ressources.eau += ajout_eau
            print(f"🌧️ Pluie : +{ajout_eau} d'eau ajoutée (total : {self.ressources.eau})")

    def _consommer_medicaments_batiments(self):
        """
        Calcule et déduit la quantité de médicaments nécessaires
        pour soigner les animaux hébergés dans les bâtiments.

        Si les ressources du joueur sont insuffisantes, affiche un avertissement.
        """
        repo_bat = DepotBatiment()
        batiments = repo_bat.tout_recuperer()
        total_medicaments_bat = 0
        for bat in batiments:
            capacite = bat.capacite_animaux()
            medicaments_pour_batiment = int(round(capacite / 20))  # Ratio ~1 pour 20 animaux
            total_medicaments_bat += medicaments_pour_batiment
        print(f"💊 Médicaments nécessaires pour bâtiments : {total_medicaments_bat}")
        # Déduire les médicaments utilisé pour les bâtimences
        if self.ressources.medicaments >= total_medicaments_bat:
            self.ressources.medicaments -= total_medicaments_bat
            print(f"💊 Médicaments consommés pour bâtiments : {total_medicaments_bat} (reste : {self.ressources.medicaments})")
        else:
            print(f"⚠️ Pas assez de médicaments pour les animaux dans les bâtiments (besoin : {total_medicaments_bat})")


    def _gerer_pannes(self):
        """
        🏚️ Gère le risque de panne globale et tente une réparation automatique
        si le joueur possède le technicien correspondant.

        Une panne peut apparaître aléatoirement si aucune n'est en cours.
        """
        if self.panne_actuelle is None and random.randint(1, 10) == 1:
            self.panne_actuelle = random.choice(NOMS_TECHNICIENS)
            print(f"⚠️ Panne globale : {self.panne_actuelle}")

        if self.panne_actuelle:
            if self.ressources.techniciens.get(self.panne_actuelle, 0) > 0:
                self.ressources.techniciens[self.panne_actuelle] -= 1
                print(f"🔧 Panne réparée grâce à {self.panne_actuelle}")
                self.panne_actuelle = None
            else:
                print(f"❌ Panne toujours active : {self.panne_actuelle}")

    def _vieillir_et_soigner_animaux(self, animaux):
        """
        🐄 Vieillit chaque animal et gère la probabilité qu'il tombe malade.

        Si un animal tombe malade, le jeu essaie automatiquement de le soigner.
        Si les médicaments sont insuffisants, l'animal meurt.

        Args:
            animaux (list): Liste des animaux actuels.
        """
        survivants = []
        for a in animaux:
            a.vieillir()
            if random.randint(1, 20) == 1:
                a.est_malade = True
                print(f"⚠️ {a.nom()} est malade !")
                if self.ressources.medicaments > 0:
                    self.ressources.medicaments -= 1
                    a.est_malade = False
                    print(f"💊 {a.nom()} soigné automatiquement - médicaments restants : {self.ressources.medicaments}")
                    survivants.append(a)
                else:
                    print(f"💀 {a.nom()} mort faute immédiatement de médicament.")
            else:
                survivants.append(a)
        self.repo_animaux.sauvegarder_tous(survivants)

    def _faire_pousser_cultures(self, cultures):
        """
        Vieillit chaque culture pour simuler la croissance quotidienne.

        Args:
            cultures (list): Liste des cultures actuelles.
        """
        for c in cultures:
            c.vieillir()
            print(f"→ {c.nom()} a poussé (âge = {c.age})")

    def _consommer_eau_et_nourriture(self, cultures, animaux):
        """
        Calcule et déduit la consommation quotidienne :
        - Eau pour cultures, animaux et bâtiments.
        - Nourriture pour animaux et bâtiments.

        Si les ressources sont insuffisantes, affiche des avertissements.

        Args:
            cultures (list): Liste des cultures actuelles.
            animaux (list): Liste des animaux actuels.
        """
        total_eau_cultures = sum(c.besoin_eau() for c in cultures)
        total_eau_animaux = sum(a.besoin_eau() for a in animaux)
        cout_nourriture_betails_bat, cout_eau_bat = self.ressources.calculer_besoin_eau_et_nourriture_batiments()    
        total_nourriture_animaux = sum(a.besoin_nourriture() for a in animaux)
        total_nourriture = total_nourriture_animaux + cout_nourriture_betails_bat
        if self.ressources.nourriture_betails >= total_nourriture:
            self.ressources.nourriture_betails -= total_nourriture
            print(f"🍽️ Nourriture bétail consommée : {total_nourriture} (reste : {self.ressources.nourriture_betails})")
        else:
            print(f"⚠️ Pas assez de nourriture pour tout le bétail et bâtiments (besoin : {total_nourriture})")
        if self.ressources.eau >= cout_eau_bat:
            self.ressources.eau -= cout_eau_bat
            print(f"🚰 Eau pour bâtiments : {cout_eau_bat} (reste : {self.ressources.eau})")
        else:
            print(f"⚠️ Pas assez d'eau pour les bâtiments (besoin additionnel : {cout_eau_bat})")
        total_eau_besoin = total_eau_cultures + total_eau_animaux
        if self.ressources.eau >= total_eau_besoin:
            self.ressources.eau -= total_eau_besoin
            print(f"💧 Eau consommée : cultures = {total_eau_cultures}, animaux = {total_eau_animaux}, reste : {self.ressources.eau}")
            # ✅ Faire pousser les cultures
            for culture in cultures:
                culture.vieillir()
                print(f"→ {culture.nom()} a poussé (âge = {culture.age})")
        else:
            print(f"❌ Pas assez d'eau : cultures {total_eau_cultures} + animaux {total_eau_animaux} > disponible {self.ressources.eau}")
        self.repo_cultures.sauvegarder_tous(cultures)
        # 🍽️ Consommer nourriture bétail
        total_nourriture = 0
        for animal in animaux:
            total_nourriture += animal.besoin_nourriture()
        if self.ressources.nourriture_betails >= total_nourriture:
            self.ressources.nourriture_betails -= total_nourriture
            print(f"🍽️ Nourriture bétail consommée : {total_nourriture} (reste : {self.ressources.nourriture_betails})")
        else:
            print(f"⚠️ Pas assez de nourriture pour tout le bétail (besoin : {total_nourriture})")

    def passer_jour_suivant(self):
        """
        Passe au jour suivant :
        - Génère la météo.
        - Ajoute de l'eau de pluie si besoin.
        - Consomme eau, nourriture, médicaments.
        - Gère pannes et réparations automatiques.
        - Vieillit et soigne les animaux.
        - Fait pousser les cultures.
        - Génère le revenu des bâtiments.
        - Sauvegarde les ressources mises à jour.
        """
        self.meteo_du_jour = Meteo()
        niveau_eau = self.meteo_du_jour.eau_du_jour()
        print(f"Météo du jour : {self.meteo_du_jour.afficher()} (eau disponible : {niveau_eau})")
        cultures = self.repo_cultures.tout_recuperer()
        animaux = self.repo_animaux.tout_recuperer()
        self._ajouter_eau_de_pluie()
        self._consommer_eau_et_nourriture(cultures, animaux)
        self._consommer_medicaments_batiments()
        self._gerer_pannes()
        self._vieillir_et_soigner_animaux(animaux)
        self._faire_pousser_cultures(cultures)
        revenu = self.ressources.calculer_revenu_batiments(self.panne_actuelle)
        self.ressources.argent += revenu
        self.repo_ressources_joueur.sauvegarder_tous([self.ressources])
        self.jour += 1


    def generer_revenu_batiments(self):
        """
        Calcule et ajoute le revenu net généré par tous les bâtiments au solde du joueur.
        """
        revenu = self.ressources.calculer_revenu_batiments(self.panne_actuelle)
        self.ressources.argent += revenu
        print(f"💰 Revenu bâtiments : +{revenu:.2f} €")

    def obtenir_case(self, x, y):
        """
        Retourne la case de la ferme aux coordonnées données.

        Args:
            x (int): Coordonnée X.
            y (int): Coordonnée Y.

        Returns:
            CaseFerme or None: La case correspondante ou None.
        """
        return CaseFerme.obtenir_case(self.cases, x, y)
    
    def acheter_graine(self, nom_culture):
        """Achète une graine spécifique et met à jour le stock."""
        self.ressources.acheter_graine(nom_culture, repo=self.repo_ressources_joueur)

    def acheter_animal(self, nom_animal):
        """Achète un animal spécifique et met à jour le stock."""
        self.ressources.acheter_animal(nom_animal, repo=self.repo_ressources_joueur)

    def acheter_batiment(self, nom_batiment):
        """Achète un bâtiment spécifique et met à jour le stock."""
        self.ressources.acheter_batiment(nom_batiment, repo=self.repo_ressources_joueur)

    def acheter_eau(self):
        """Achète de l'eau et met à jour le stock."""
        self.ressources.acheter_eau(repo=self.repo_ressources_joueur)

    def acheter_medicament(self):
        """Achète des médicaments et met à jour le stock."""
        self.ressources.acheter_medicament(repo=self.repo_ressources_joueur)

    def acheter_nourriture_betails(self):
        """Achète de la nourriture pour le bétail et met à jour le stock."""
        self.ressources.acheter_nourriture_betails(repo=self.repo_ressources_joueur)

    def acheter_technicien(self, nom_technicien):
        """Achète un technicien pour réparer une panne ou pour la prévention."""
        self.ressources.acheter_technicien(nom_technicien, self.repo_batiments, self.repo_ressources_joueur)

    def recolter(self, case):
        """Récolte une culture mature d'une case spécifique."""
        self.ressources.recolter(
            case, self.repo_cultures, self.repo_animaux, self.repo_cases, self.repo_ressources_joueur)

    def vendre_animal(self, case):
        """Vend un animal mature d'une case spécifique."""
        self.ressources.vendre_animal(
            case, self.repo_cultures, self.repo_animaux, self.repo_cases, self.repo_ressources_joueur)

    def vendre_batiment(self, batiment_id):
        """Vend un bâtiment et libère les cases occupées."""
        self.ressources.vendre_batiment(
            batiment_id, self.repo_batiments, self.repo_cases, self.repo_ressources_joueur, self.obtenir_case)

    def planter_culture(self, case, Classe, nom):
        """Plante une culture sur une case donnée."""
        case.placer(ModeSelection.CULTURE, Classe, nom, self)

    def placer_animal(self, case, Classe, nom):
        """Place un animal sur une case donnée."""
        case.placer(ModeSelection.ANIMAL, Classe, nom, self)

    def soigner(self, case):
        """Soigne l'animal présent sur une case si possible."""
        if not case.id_animal:
            print("Aucun animal ici.")
            return
        animal = self.repo_animaux.trouver_par_id(case.id_animal)
        if animal:
            animal.soigner(self.ressources, self.repo_animaux, self.repo_ressources_joueur)
        else:
            print("Animal introuvable.")

    def reparer_panne(self, case):
        """Répare un bâtiment en panne sur une case donnée si possible."""
        if not case.id_batiment:
            print("Aucun bâtiment ici.")
            return
        batiment = self.repo_batiments.trouver_par_id(case.id_batiment)
        if batiment:
            batiment.reparer(self.ressources, self.repo_batiments, self.repo_ressources_joueur)
   
    def peut_soigner(self, nom_animal: str) -> bool:
        """
        Vérifie si le joueur a assez de médicaments pour soigner un animal.

        Args:
            nom_animal (str): Nom de l'animal à soigner.

        Returns:
            bool: True si des médicaments sont disponibles, False sinon.
        """        
        return self.medicaments > 0

    def peut_planter(self, nom_culture: str) -> bool:
        """
        Vérifie si le joueur possède une graine pour planter une culture spécifique.

        Args:
            nom_culture (str): Nom de la culture à planter.

        Returns:
            bool: True si une graine est disponible, False sinon.
        """
        return self.graines.get(nom_culture, 0) > 0
    
    def possede_animal(self, nom_animal: str) -> bool:
        """
        Vérifie si le joueur possède au moins un exemplaire d'un animal donné.

        Args:
            nom_animal (str): Nom de l'animal à vérifier.

        Returns:
            bool: True si le joueur possède cet animal, False sinon.
        """
        return self.animaux.get(nom_animal, 0) > 0
    
    def peut_installer_batiment(self, jeu, x, y, largeur, hauteur):
        """
        Vérifie si un bâtiment peut être installé à une position donnée
        sans dépasser la grille et sans chevaucher d'autres bâtiments.

        Args:
            jeu (Jeu): Instance du jeu pour accès aux cases.
            x (int): Coordonnée X de départ.
            y (int): Coordonnée Y de départ.
            largeur (int): Largeur du bâtiment.
            hauteur (int): Hauteur du bâtiment.

        Returns:
            bool: True si l'installation est possible, False sinon.
        """
        for dx in range(largeur):
            for dy in range(hauteur):
                # Vérifie que la case est dans la grille
                if not (0 <= x + dx < LARGEUR_GRILLE and 0 <= y + dy < HAUTEUR_GRILLE):
                    return False
                # Vérifie qu'elle est libre
                case = CaseFerme.obtenir_case(x + dx, y + dy)
                if case is None or case.id_batiment is not None:
                    return False
        return True
    
    def placer_batiment(self, x, y, Classe, nom):
        """
        Place un bâtiment sur la ferme à la position spécifiée.

        Args:
            x (int): Coordonnée X où placer le bâtiment.
            y (int): Coordonnée Y où placer le bâtiment.
            Classe (Type): Classe du bâtiment à instancier.
            nom (str): Nom du bâtiment.
        """
        case = self.obtenir_case(x, y)
        case.placer(ModeSelection.BATIMENT, Classe, nom, self)  
      
    def produire_batiment(self, case):
        """
        Calcule la production quotidienne d'un bâtiment et applique
        son coût d'entretien au solde du joueur.

        Args:
            case (CaseFerme): Case contenant le bâtiment.
        """
        if case.id_batiment:
            batiment = self.repo_batiments.trouver_par_id(case.id_batiment)
            if batiment:
                revenu = batiment.production_journaliere()
                cout = batiment.cout_entretien()
                self.ressources.argent += revenu - cout
                print(f"{batiment.nom()} a produit : +{revenu}€, coût d’entretien : -{cout}€")
                self.repo_ressources_joueur.ajouter(self.ressources)

    def supprimer_batiment(self, batiment_id):
        """
        Supprime un bâtiment et libère toutes les cases qu'il occupait.

        Args:
            batiment_id (str): Identifiant du bâtiment à supprimer.
        """
        for case in self.cases:
            if case.id_batiment == batiment_id:
                case.id_batiment = None
                self.repo_cases.ajouter(case)
        self.repo_batiments.supprimer(batiment_id)
        
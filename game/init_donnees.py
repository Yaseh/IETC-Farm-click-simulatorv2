from repositories.depot_animal import DepotAnimal
from repositories.depot_culture import DepotCulture
from repositories.depot_batiment import DepotBatiment
from repositories.depot_tuile_ferme import DepotTuilesFerme
from repositories.depot_ressource_joueur import DepotRessourceJoueur
from models.case_ferme import CaseFerme
from models.ressources_joueur import RessourceJoueur
from utils.generateur_identifiant import generer_identifiant
from utils.constantes import *

def initialiser_animaux():
    """
    Initialise les animaux de la ferme.

    Crée un exemplaire pour chaque type d'animal défini et les sauvegarde dans le dépôt correspondant.
    """
    animaux = [CLASSES_ANIMAUX[nom](identifiant=generer_identifiant())
               for nom in NOMS_ANIMAUX]
    DepotAnimal().sauvegarder_tous(animaux)
    print("Animaux initialisés.")

def initialiser_cultures():
    """
    Initialise les cultures de la ferme.

    Crée un exemplaire pour chaque type de culture défini et les sauvegarde dans le dépôt correspondant.
    """
    cultures = [CLASSES_CULTURES[nom](identifiant=generer_identifiant())
                for nom in NOMS_CULTURES]
    DepotCulture().sauvegarder_tous(cultures)
    print("Cultures initialisées.")

def initialiser_batiments():
    """
    Initialise les bâtiments de la ferme.

    Crée un exemplaire pour chaque type de bâtiment avec des coordonnées prédéfinies
    et les sauvegarde dans le dépôt correspondant.
    """
    batiments = [CLASSES_BATIMENTS[nom](identifiant=generer_identifiant(), 
                                        x=0, y= i * 2, largeur=2, hauteur=2)
                 for i, nom in enumerate(NOMS_BATIMENTS)]
    DepotBatiment().sauvegarder_tous(batiments)
    print("✔ Bâtiments initialisés.")

def initialiser_grille_ferme():
    """
    Initialise la grille de la ferme.

    Génère toutes les tuiles de la ferme selon les dimensions de la grille
    et les sauvegarde dans le dépôt correspondant.
    """
    colonnes, lignes = TAILLE_GRILLE
    tuiles = [
        CaseFerme(identifiant=generer_identifiant(), x=x, y=y, id_culture=None)
        for x in range(colonnes) for y in range(lignes)
    ]
    DepotTuilesFerme().sauvegarder_tous(tuiles)
    print("Grille de ferme générée.")

def initialiser_ressource():
    """
    Initialise les ressources du joueur.

    Crée une instance de RessourceJoueur avec un identifiant unique
    et la sauvegarde dans le dépôt correspondant.
    """
    ressource = RessourceJoueur(identifiant=generer_identifiant())
    DepotRessourceJoueur().ajouter(ressource)
    print("Joueur initialisé.")


if __name__ == "__main__":
    initialiser_grille_ferme()
    initialiser_cultures()
    initialiser_animaux()
    initialiser_batiments()
    initialiser_ressource()
    print("✅ Toutes les données ont été initialisées.")

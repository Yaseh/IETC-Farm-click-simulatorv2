from typing import Type

# 🌾 Cultures
from models.cultures.ble import Ble
from models.cultures.carotte import Carotte
from models.cultures.mais import Mais
# 🐔 Animaux
from models.animaux.poule import Poule
from models.animaux.mouton import Mouton
from models.animaux.vache import Vache
# 🏠 Bâtiments
from models.batiments.poulailler import Poulailler
from models.batiments.etable import Etable
from models.batiments.laiterie import Laiterie
# Classes abstraites
from models.cultures.base_culture import Culture
from models.animaux.base_animal import Animal
from models.batiments.base_batiment import Batiment

"""
Module de constantes globales pour le jeu de ferme.

Contient :
- Les noms de référence pour les cultures, animaux et bâtiments.
- Les correspondances entre noms et classes concrètes.
- Les dimensions de la grille de jeu.
- Les correspondances entre bâtiments et produits générés.
"""

# ✅ Noms de référence
NOMS_CULTURES = ["blé", "carotte", "maïs"]
"""list: Liste des noms de cultures disponibles."""

NOMS_ANIMAUX = ["poule", "mouton", "vache"]
"""list: Liste des noms d'animaux disponibles."""

NOMS_BATIMENTS = ["poulailler", "laiterie", "étable"]
"""list: Liste des types de bâtiments disponibles."""

NOMS_PRODUCTION_BATIMENTS = ["oeuf", "lait", "laine"]
"""list: Liste des produits générés par les bâtiments."""

NOMS_TECHNICIENS = ["mécanicien", "plombier", "électricien"]
"""list: Liste des types de techniciens disponibles."""

PRODUIT_PAR_BATIMENT = {
    "poulailler": "oeuf",
    "laiterie": "lait",
    "étable": "laine",
}
"""dict: Association entre nom de bâtiment et produit généré."""

TAILLE_GRILLE = (10, 10)
"""tuple: Dimensions de la grille de jeu (colonnes, lignes)."""

TAILLE_CASE = 50
"""int: Taille d'une case de la grille en pixels."""

LARGEUR_GRILLE = TAILLE_GRILLE[0] * TAILLE_CASE
"""int: Largeur totale de la grille en pixels."""

HAUTEUR_GRILLE = TAILLE_GRILLE[1] * TAILLE_CASE
"""int: Hauteur totale de la grille en pixels."""

# 🧭 Correspondance nom → classe
CLASSES_CULTURES: dict[str, Type[Culture]] = dict(zip( NOMS_CULTURES, [Ble, Carotte, Mais] ))
"""dict: Association entre nom de culture et classe de culture concrète."""

CLASSES_ANIMAUX: dict[str, Type[Animal]] = dict(zip( NOMS_ANIMAUX, [Poule, Mouton, Vache] ))
"""dict: Association entre nom d'animal et classe d'animal concrète."""

CLASSES_BATIMENTS: dict[str, Type[Batiment]] = dict(zip( NOMS_BATIMENTS, [Poulailler, Etable, Laiterie] ))
"""dict: Association entre nom de bâtiment et classe de bâtiment concrète."""

CLASSES_PRODUIT_BATIMENTS: dict[str, Type[Batiment]] = dict(zip( NOMS_PRODUCTION_BATIMENTS, [Poulailler, Etable, Laiterie] ))
"""dict: Association entre nom de produit et classe de bâtiment producteur."""

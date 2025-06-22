"""
interface.constantes
=====================

Définit l'ensemble des **constantes graphiques** et **paramètres d'affichage**
utilisés pour l'interface Pygame du simulateur de ferme.

Contient :
- Les couleurs standard pour le thème.
- Les dimensions générales (fenêtre, grille, images).
- Les marges, tailles de boutons et colonnes.
- Les chemins et suffixes pour les images.

Toutes ces valeurs servent à garantir une interface cohérente et facilement configurable.
"""

# Couleurs standards
BEIGE = (222, 184, 135)
VERT_CLAIR = (144, 238, 144)
VERT = (34, 139, 34)
JAUNE_CLAIR = (255, 255, 153)
BLEU_CLAIR = (0, 191, 255)
ROSE_CLAIR = (255, 182, 193)
ORANGE_CLAIR = (255, 138, 101)
BLANC = (255, 255, 255)
GRIS_FONCE = (50, 50, 50)
GRIS = (100, 100, 100)
NOIR = (0, 0, 0)
ROUGE_VIF = (255, 0, 0)
ROUGE = (200, 50, 50)

# Dimensions et positions générales
TITRE_APPLICATION = "Farming simulator"
LARGEUR_TOTALE = 1240
HAUTEUR_TOTALE = 840
TAILLE_CASE = 50
TAILLE_IMG = TAILLE_CASE - 2
MARGE_GRILLE = 250
MARGE_HAUT = 20 
TAILLE_POLICE = 24

# Emplacements et suffixes des images
DIR_IMG = "assets"
SUFFIXE_IMG = "_48.png"
SUFFIXE_GRANDE_IMG = "_96.png"
ACHAT = ""
DEVISE = "€"

# Dimensions et positions spécifiques
MARGE_BOUTON = 20
LARGEUR_BOUTON = 220
HAUTEUR_BOUTON = 40
LARGEUR_BOUTON
RAYON = 8
MARGE_COL_1 = 50
MARGE_COL_2 = 150
X_COL1 = 760
X_COL2 = 990
X_COL3 = 1220

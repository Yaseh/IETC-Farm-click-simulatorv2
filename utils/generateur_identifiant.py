import uuid

"""
Module utilitaire pour générer des identifiants uniques.

Ce module fournit une fonction simple pour créer des UUID,
utilisés comme identifiants uniques pour les objets du jeu.
"""

def generer_identifiant():
    """
    Génère un identifiant unique sous forme de chaîne de caractères.

    Returns:
        str: Un UUID4 sous forme de chaîne.
    """
    return str(uuid.uuid4())

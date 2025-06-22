from enum import Enum

class ModeSelection(Enum):
    """
    Enumération représentant les différents modes de sélection possibles dans le jeu.

    Cette énumération est utilisée pour déterminer le type d'action
    ou de ressource à manipuler : culture, animal ou bâtiment.

    Attributes:
        CULTURE (str): Mode pour sélectionner une culture.
        ANIMAL (str): Mode pour sélectionner un animal.
        BATIMENT (str): Mode pour sélectionner un bâtiment.
    """
    CULTURE = "culture"
    ANIMAL = "animal"
    BATIMENT = "bâtiment"
    
from repositories.depot_culture import DepotCulture
from models.ble import Ble
from models.carotte import Carotte
from utils.generateur_identifiant import generer_identifiant

def initialiser_cultures():
    cultures = [
        Ble(identifiant=generer_identifiant()),
        Carotte(identifiant=generer_identifiant())
    ]
    depot = DepotCulture()
    depot.sauvegarder_tous(cultures)

if __name__ == "__main__":
    initialiser_cultures()
    print("Cultures initialisées.")

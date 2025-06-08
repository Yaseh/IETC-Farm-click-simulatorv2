from models.base_culture import Culture

''' ble.py ← sous-classe concrète 'Ble' '''
class Ble(Culture):
    def nom(self) -> str:
        return "ble"
    
    def temps_pousse(self) -> int:
        return 3

    def valeur(self) -> float:
        return 10.0

    # Besoin en eau important
    def besoin_eau(self) -> float:
        return 4  
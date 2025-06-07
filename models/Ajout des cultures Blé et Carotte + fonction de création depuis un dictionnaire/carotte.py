from models.base_culture import Culture

''' carotte.py ← sous-classe concrète 'Carotte' '''
class Carotte(Culture):
    def nom(self) -> str:
        return "carotte"

    def temps_pousse(self) -> int:
        return 2

    def valeur(self) -> float:
        return 8.0

    # Moins exigeant en eau
    def besoin_eau(self) -> float:
        return 0.5  
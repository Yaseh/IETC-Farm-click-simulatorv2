import unittest
from unittest.mock import MagicMock, patch
from models.ressources_joueur import RessourceJoueur

class TestRessourceJoueur(unittest.TestCase):
    """Tests unitaires pour vérifier les opérations d'achat, de vente et de gestion des ressources du joueur."""

    def test_initialisation_defaut(self):
        """Vérifie l'initialisation par défaut du joueur."""
        joueur = RessourceJoueur("p1")
        self.assertEqual(joueur.identifiant, "p1")
        self.assertEqual(joueur.argent, 1500)

    def test_acheter_graine(self):
        """Teste l'achat d'une graine."""
        joueur = RessourceJoueur("p1")
        repo = MagicMock()
        before = joueur.graines["blé"]
        joueur.acheter_graine("blé", repo)
        self.assertEqual(joueur.graines["blé"], before + 1)
        repo.ajouter.assert_called_once()

    def test_acheter_animal(self):
        """Teste l'achat d'un animal."""
        joueur = RessourceJoueur("p1")
        repo = MagicMock()
        before = joueur.animaux["poule"]
        joueur.acheter_animal("poule", repo)
        self.assertEqual(joueur.animaux["poule"], before + 1)
        repo.ajouter.assert_called_once()

    def test_acheter_batiment(self):
        """Teste l'achat d'un bâtiment."""
        joueur = RessourceJoueur("p1")
        repo = MagicMock()
        before = joueur.batiments["poulailler"]
        joueur.acheter_batiment("poulailler", repo)
        self.assertEqual(joueur.batiments["poulailler"], before + 1)
        repo.ajouter.assert_called_once()

    def test_acheter_technicien(self):
        """Teste l'achat d'un technicien."""
        joueur = RessourceJoueur("p1")
        repo = MagicMock()
        before = joueur.techniciens["mécanicien"]
        joueur.acheter_technicien("mécanicien", repo_ressources=repo)
        self.assertEqual(joueur.techniciens["mécanicien"], before + 1)
        repo.ajouter.assert_called_once()

    def test_acheter_eau(self):
        """Teste l'achat d'eau."""
        joueur = RessourceJoueur("p1")
        repo = MagicMock()
        before = joueur.eau
        joueur.acheter_eau(repo)
        self.assertGreater(joueur.eau, before)
        repo.ajouter.assert_called_once()

    def test_acheter_medicament(self):
        """Teste l'achat de médicament."""
        joueur = RessourceJoueur("p1")
        repo = MagicMock()
        before = joueur.medicaments
        joueur.acheter_medicament(repo)
        self.assertGreater(joueur.medicaments, before)
        repo.ajouter.assert_called_once()

    def test_acheter_nourriture_betails(self):
        """Teste l'achat de nourriture pour bétail."""
        joueur = RessourceJoueur("p1")
        repo = MagicMock()
        before = joueur.nourriture_betails
        joueur.acheter_nourriture_betails(repo)
        self.assertGreater(joueur.nourriture_betails, before)
        repo.ajouter.assert_called_once()

    def test_pas_assez_d_argent(self):
        """Vérifie le comportement quand le joueur n'a pas assez d'argent."""
        joueur = RessourceJoueur("p1", argent=0)
        repo = MagicMock()
        joueur.acheter_graine("blé", repo)
        self.assertEqual(joueur.graines["blé"], 5)  # pas acheté
        repo.ajouter.assert_not_called()

    def test_en_dictionnaire(self):
        """Teste la conversion en dictionnaire."""
        joueur = RessourceJoueur("p1")
        d = joueur.en_dictionnaire()
        self.assertIn("argent", d)
        self.assertIn("graines", d)

class TestRessourceJoueurExtra(unittest.TestCase):
    """Tests unitaires supplémentaires pour valider les fonctionnalités avancées : 
    récolte de culture, vente d'animaux et bâtiments, calcul des besoins en ressources, 
    et gestion des pannes.
    """

    def test_recolter_culture_mature(self):
        """Teste la récolte d'une culture mature."""
        joueur = RessourceJoueur("p1")
        argent_avant = joueur.argent

        case = MagicMock()
        case.id_culture = "c1"

        culture = MagicMock()
        culture.age = 10
        culture.temps_pousse.return_value = 5
        culture.valeur.return_value = 100

        repo_cultures = MagicMock()
        repo_cultures.trouver_par_id.return_value = culture
        repo_animaux = MagicMock()
        repo_cases = MagicMock()
        repo_ressources = MagicMock()

        joueur.recolter(case, repo_cultures, repo_animaux, repo_cases, repo_ressources)
        self.assertEqual(joueur.argent, argent_avant + 100)
        repo_cultures.supprimer.assert_called_once_with(culture.identifiant)
        repo_cases.ajouter.assert_called_once()
        repo_ressources.ajouter.assert_called_once_with(joueur)

    def test_vendre_animal_mature(self):
        """Teste la vente d'un animal mature."""
        joueur = RessourceJoueur("p1")
        argent_avant = joueur.argent

        case = MagicMock()
        case.id_animal = "a1"

        animal = MagicMock()
        animal.age = 12
        animal.temps_croissance.return_value = 5
        animal.valeur.return_value = 200

        repo_animaux = MagicMock()
        repo_animaux.trouver_par_id.return_value = animal
        repo_cultures = MagicMock()
        repo_cases = MagicMock()
        repo_ressources = MagicMock()

        joueur.vendre_animal(case, repo_cultures, repo_animaux, repo_cases, repo_ressources)
        self.assertEqual(joueur.argent, argent_avant + 200)
        repo_animaux.supprimer.assert_called_once_with(animal.identifiant)
        repo_cases.ajouter.assert_called_once()
        repo_ressources.ajouter.assert_called_once_with(joueur)

    def test_vendre_batiment(self):
        """Teste la vente d'un bâtiment."""
        joueur = RessourceJoueur("p1")
        argent_avant = joueur.argent

        batiment = MagicMock()
        batiment.nom.return_value = "poulailler"
        batiment.production_journaliere.return_value = 30
        batiment.largeur = 2
        batiment.hauteur = 2
        batiment.x = 0
        batiment.y = 0

        repo_batiments = MagicMock()
        repo_batiments.trouver_par_id.return_value = batiment
        repo_cases = MagicMock()
        repo_ressources = MagicMock()

        case = MagicMock()
        case.id_batiment = "bat1"

        def fake_obtenir_case(x, y):
            return case

        joueur.vendre_batiment("bat1", repo_batiments, repo_cases, repo_ressources, fake_obtenir_case)
        self.assertEqual(joueur.argent, argent_avant + 30 * 10)
        repo_batiments.supprimer.assert_called_once_with("bat1")
        repo_cases.ajouter.assert_called()
        repo_ressources.ajouter.assert_called_once_with(joueur)

    @patch("models.ressources_joueur.DepotBatiment")
    @patch("models.ressources_joueur.CLASSES_ANIMAUX", {
        "poule": MagicMock(return_value=MagicMock(
            besoin_nourriture=MagicMock(return_value=2.0),
            besoin_eau=MagicMock(return_value=1.0))),
        "mouton": MagicMock(return_value=MagicMock(
            besoin_nourriture=MagicMock(return_value=3.0),
            besoin_eau=MagicMock(return_value=2.0))),
        "vache": MagicMock(return_value=MagicMock(
            besoin_nourriture=MagicMock(return_value=5.0),
            besoin_eau=MagicMock(return_value=4.0)))
    })

    @patch("models.ressources_joueur.DepotBatiment")
    @patch("models.ressources_joueur.CLASSES_ANIMAUX", {
        "poule": MagicMock(return_value=MagicMock(
            besoin_nourriture=MagicMock(return_value=2.0),
            besoin_eau=MagicMock(return_value=1.0))),
        "mouton": MagicMock(return_value=MagicMock(
            besoin_nourriture=MagicMock(return_value=3.0),
            besoin_eau=MagicMock(return_value=2.0))),
    })

    def test_calculer_besoin_eau_et_nourriture_batiments(self, mock_animaux, mock_DepotBatiment):
        """Teste le calcul des besoins en nourriture et eau pour les bâtiments."""
        # ✅ Simuler 2 poulaillers et 2 étables comme ton JSON
        bat1 = MagicMock()
        bat1.nom.return_value = "poulailler"
        bat1.capacite_animaux.return_value = 10

        bat2 = MagicMock()
        bat2.nom.return_value = "étable"
        bat2.capacite_animaux.return_value = 5

        bat3 = MagicMock()
        bat3.nom.return_value = "poulailler"
        bat3.capacite_animaux.return_value = 10

        bat4 = MagicMock()
        bat4.nom.return_value = "étable"
        bat4.capacite_animaux.return_value = 5

        # Mock liste JSON
        mock_repo = MagicMock()
        mock_repo.tout_recuperer.return_value = [bat1, bat2, bat3, bat4]
        mock_DepotBatiment.return_value = mock_repo

        joueur = RessourceJoueur("p1")
        nourriture, eau = joueur.calculer_besoin_eau_et_nourriture_batiments()

        # ✅ Vérifie avec les valeurs : 
        # 2 poulaillers * 10 * 2.0 = 40 nourriture
        # 2 étables * 5 * 3.0 = 30 nourriture
        # Total : 70 nourriture
        # Eau : poulailler -> 2 * 10 * 1.0 = 20
        #         étable -> 2 * 5 * 2.0 = 20
        # Total : 40 eau
        self.assertEqual(nourriture, 40 + 30)
        self.assertEqual(eau, 20 + 20)


    def tomber_en_panne(self, batiment, type_de_de_panne_metier: str):
        """Simule une panne sur un bâtiment."""
        if not batiment.est_en_panne:
            self.est_en_panne = True
            if type_de_de_panne_metier not in ("mécanicien", "plombier", "électricien"):
                raise ValueError(f"Type de panne inconnue : {type_de_de_panne_metier}")
            batiment.est_en_panne = True
            batiment.type_de_de_panne_metier = type_de_de_panne_metier
            print(f"{batiment.nom()} en panne ({type_de_de_panne_metier})")


    def test_tomber_en_panne_invalide(self):
        """Vérifie qu'une panne invalide déclenche une erreur."""
        joueur = RessourceJoueur("p1")
        bat = MagicMock()
        bat.est_en_panne = False

        with self.assertRaises(ValueError):
            joueur.tomber_en_panne(bat, "inconnu")

if __name__ == "__main__":
    unittest.main()

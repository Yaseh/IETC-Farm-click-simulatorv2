# ✅ PV 3 – Réunion du mardi 17/06/2025

**Heure :** 11h00 à 13h00  
**Lieu :** Visio  
**Participants :** Youssef, Soufian, Benjamin, Harry  

## Sujets abordés

### 🔹 Soufian
- Finalisation de `usine_animal.py` pour générer dynamiquement les animaux
- Ajout de la classe `depot_animal.py` dans le dépôt des animaux
- Début des animations d’évolution pour la poule et le mouton

### 🔹 Youssef
- Intégration de `usine_culture.py` avec génération des cultures depuis un dictionnaire
- Ajout de la classe `depot_culture.py` pour stocker les cultures actives
- Réglage des collisions et des vérifications de cases libres avec `case_ferme.py`

### 🔹 Benjamin
- Création de `usine_batiment.py` pour instancier les bâtiments
- Ajout de `depot_batiment.py` pour la gestion des structures
- Début de la logique d’achat/vente dans `actions.py`

### 🔹 Harry
- Rédaction de documentation automatisée sur les modules `jeu.py` et `ressources.py`
- Ajout de tests initiaux dans `base_depot_json.py`
- Mise en lien de `requirements.txt` avec les dépendances Sphinx

## Décisions prises
- Chaque dépôt (`depot_animal`, `depot_culture`, `depot_batiment`) doit implémenter une méthode `tout_recuperer()`
- La logique de météo et de maladies doit être liée à des événements temporels à déclencher dans `jeu.py`
- Priorité à la cohérence visuelle dans les interfaces : mise en place de conventions sur les noms d’assets

Synthèse de PV rédigée par ChatGPT
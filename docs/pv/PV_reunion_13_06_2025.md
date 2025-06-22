# ✅ PV 2 – Réunion du vendredi 13/06/2025

**Heure :** 12h00 à 14h00  
**Lieu :** Visio  
**Participants :** Youssef, Soufian, Benjamin, Harry  

## Sujets abordés

### 🔹 Soufian
- Ajout de la classe `animal.py` avec comportement commun aux animaux
- Amélioration de la classe `main_interface.py` pour afficher les animaux
- Création d’un début de gestion des maladies dans `maladie.py`

### 🔹 Youssef
- Finalisation des classes `carotte.py` et `culture.py`
- Mise en place des modes de sélection dans `mode_selection.py`
- Tests des premières cultures dans l’interface `cultures.py`

### 🔹 Benjamin
- Ajout de `batiment.py` pour centraliser les types de bâtiments
- Début d’intégration des événements dans `evenements.py`
- Rédaction de la logique d'initialisation dans `init_donnees.py`

### 🔹 Harry
- Ajout des fonctions de calcul de prix dans `catalogue_prix.py`
- Ajout des premières lignes de documentation dans les docstrings
- Début de génération automatique de la doc avec Sphinx dans `docs/`

## Décisions prises
- Tous les types (`Culture`, `Animal`, `Bâtiment`) doivent être testés individuellement dans `main_interface.py` avant intégration globale.
- Un seul point d’entrée : `interface_pygame.py` doit centraliser tous les appels de modules d’affichage.
- Validation d’un format commun pour les fichiers JSON stockés dans `data/`.

Synthèse de PV rédigée par ChatGPT
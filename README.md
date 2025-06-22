# 🐄🌽🏠 Farm Game

**Gestion de ferme** est une simulation de gestion de ferme codée en Python avec une architecture modulaire et orientée objet.  
Le projet s’appuie sur un moteur interne (models, factories, repositories) et une interface utilisateur (interface, game) pour offrir une expérience interactive. Ce jeu sa base sur le principe du click game.

---

## 🗂️ **Architecture du projet**

Voici la structure **logique et technique** du projet, telle qu’elle ressort de l’arborescence et du code :

### 📁 **1. `assets/`**
- Contient **toutes les images** : cultures, animaux, bâtiments, icônes de ressources et techniciens.
- Sert de **banque de sprites** pour rendre le jeu visuellement immersif.

### 📁 **2. `data/`**
- Regroupe les **fichiers JSON** servant de **système de sauvegarde** :
  - `animaux.json` — état de chaque animal
  - `batiments.json` — état et position de chaque bâtiment
  - `cultures.json` — progression des cultures
  - `ferme_tuiles.json` — structure de la ferme sous forme de grille de tuiles
  - `joueur.json` — ressources et statistiques du joueur

### 📁 **3. `models/`**
- Définit les **classes cœur** de la simulation :
  - `animaux/` — `Animal`, `Poule`, `Mouton`, `Vache`
  - `cultures/` — `Culture`, `Ble`, `Carotte`, `Mais`
  - `batiments/` — `Batiment`, `Etable`, `Laiterie`, `Poulailler`
  - `case_ferme.py` — représentation d’une tuile de la ferme
  - `ressources_joueur.py` — état global du joueur

### 📁 **4. `factories/`**
- Contient les **usines (Factories)** pour créer dynamiquement des instances de :
  - Animaux
  - Cultures
  - Bâtiments
- Facilite l’ajout d’entités sans dupliquer du code.

### 📁 **5. `repositories/`**
- Gère la **lecture/écriture JSON**.
- Fournit une abstraction propre pour charger et sauvegarder :
  - Animaux, cultures, bâtiments, tuiles, ressources du joueur.

### 📁 **6. `game/`**
- Cœur de la **logique de jeu** :
  - `init_donnees.py` — initialise la ferme à partir des données.
  - `jeu.py` — boucle principale.
  - `meteo.py`, `maladie.py`, `incidents.py` — gèrent les événements dynamiques (météo, maladies, imprévus).

### 📁 **7. `interface/`**
- Tout le **front-end du jeu** (basé sur Pygame) :
  - `affichage.py` — rend le jeu visuel.
  - `actions.py` — gère les actions utilisateur.
  - `interface_pygame.py` — lance et contrôle l’interface graphique.
  - `evenements.py` — lie les événements clavier/souris à la logique.

### 📁 **8. `utils/`**
- Fichiers utilitaires :
  - `constantes.py` — constantes globales.
  - `catalogue_prix.py` — prix des ressources et entités.
  - `generateur_identifiant.py` — pour donner des IDs uniques aux objets.
  - `mode_selection.py` — gère la sélection d’éléments.

### 📄 **9. `lancer_jeu.py`**
- Script principal pour démarrer le jeu.

---

## 🧩 **Fonctionnalités du jeu**

Voici ce que **Farm Game** propose concrètement :

✅ **🌾 Cultures**
- Trois types principaux : blé, carottes, maïs.
- Chaque culture a des stades de croissance visibles.
- Le joueur peut planter, suivre et récolter.

✅ **🐓 Animaux**
- Trois espèces : poule, mouton, vache.
- Chaque animal évolue en âge et produit (œufs, lait, laine).
- Animaux susceptibles d'attraper des maladies et donc de nécessiter des soins.

✅ **🏠 Bâtiments**
- Étable, poulailler, laiterie.
- Chaque bâtiment peut produire et donc nécessite parfois de la maintenance.
- Les bâtiments ont une position sur la ferme.

✅ **🔧 Techniciens**
- Trois types : mécanicien, plombier, électricien.
- Assurent la réparation des bâtiments ou la gestion des incidents.

✅ **🌤️ Incidents et météo**
- Le jeu intègre une météo dynamique et des événements imprévus (maladies, pannes).

✅ **💰 Gestion des ressources**
- Argent, eau, nourriture pour bétail, médicaments.
- Gestion des stocks pour maintenir la ferme productive.

✅ **💾 Sauvegarde & Chargement**
- Le jeu sauvegarde chaque élément dans des fichiers JSON.
- À l’ouverture, tout est rechargé fidèlement.

✅ **🎮 Interface graphique (Pygame)**
- Vue visuelle de la ferme.
- Interaction par clic pour gérer, acheter, réparer, soigner.

---

## ⚙️ Installation

Voici comment installer et préparer **Farm Game** sur votre machine :

### 1️⃣ **Cloner le dépôt**
```bash
git clone https://github.com/<VOTRE_UTILISATEUR>/<VOTRE_DEPOT>.git
cd <VOTRE_DEPOT>
```

### 2️⃣ Créer un **environnement virtuel** (optionnel mais recommandé)
#### Sous macOS / Linux :
```sh
python3 -m venv venv
source venv/bin/activate
```

#### Sous Windows
```bash
python -m venv venv
venv\Scripts\activate
```

###3️⃣ Installer les dépendances
Le jeu est basé sur Python et Pygame.

#### Installez Pygame via pip :
```bash
pip install pygame
pip install sphinx
pip install sphinx-rtd-theme
```

#### ou
```bash
pip install -r requirements.txt
```

### 4️⃣ Vérifier la version de Python

Assurez-vous d’utiliser Python 3.10+ (certaines versions de Pygame nécessitent Python récent).
```bash
python --version
```

#### ou
```bash
python3 --version
```

### 5️⃣ Lancer le jeu

Depuis le dossier racine :
```bash
python lancer_jeu.py
```

✅ Le jeu se lance !
Une fenêtre Pygame s’ouvrira pour vous permettre de gérer votre ferme.

💡 Astuces
Les données de jeu sont sauvegardées automatiquement dans le dossier **data/** sous forme de fichiers JSON.

Vous pouvez supprimer ou éditer ces fichiers pour réinitialiser votre progression.

### 📚 Documentation technique

Tout le projet est soigneusement **documenté directement dans le code** grâce aux **docstrings Python**.  
Chaque **classe**, **méthode** et **module** contient une explication précise de son rôle, de ses attributs et de ses paramètres.

Pour rendre cette documentation plus accessible, nous utilisons **[Sphinx](https://www.sphinx-doc.org/)** pour générer automatiquement une **version web** claire et interactive.

---

### ✅ En résumé

- **Docstrings complètes** : tous les éléments du projet sont commentés.
- **Documentation HTML** : générée automatiquement via Sphinx.
- **Navigation intuitive** : index des modules, classes et méthodes.
- **Toujours à jour** : il suffit d’exécuter une commande pour régénérer la documentation après chaque modification du code.

---

### ⚡ Comment générer la documentation

Si vous souhaitez générer ou mettre à jour la version HTML :

#### Depuis le dossier racine, pour régénérer la documentation :
```bash
make html
 ```
ou bien :

```bash
sphinx-build -b html source/ build/
```

---

Le dossier `docs/` est une **brique essentielle** pour :

- documenter **tout le projet Python** de manière **cohérente et centralisée**,
- garantir une documentation **toujours alignée** avec l’implémentation réelle,
- offrir à toute l’équipe (ou aux utilisateurs) une **référence claire, accessible et à jour**.

> 📚 Une **documentation toujours à jour** = un projet plus robuste et une équipe plus efficace !**

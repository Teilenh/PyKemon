# PyKemon 🎮

**PyKemon** est un jeu Pokémon développé en Python, conçu à l'origine comme un projet pour maîtriser la **Programmation Orientée Objet (POO)**. Il est doté d'une interface graphique moderne et réactive construite avec **PyQt6**.

![PyKemon Battle](Assets/battle_bg.png)

## 🌟 Fonctionnalités Principales

*   **Pokédex 1ère Génération Complet** : Les 151 premiers Pokémon avec leurs statistiques de base authentiques, récupérés dynamiquement via l'API officielle *PokéAPI*.
*   **Team Builder Avancé** : Créez votre équipe de 6 Pokémon, attribuez-leur un set de 4 attaques personnalisées et sauvegardez votre équipe. Elle se rechargera automatiquement à chaque lancement !
*   **Moteur de Combat Authentique (Gen 1)** :
    *   Gestion des multiplicateurs de faiblesses et de résistances.
    *   Modificateurs de statistiques temporels (Buffs/Debuffs) calculés fidèlement (ex: *Danse Lames* = Attaque x2).
*   **Interface Graphique (UI) Moderne** :
    *   Basculement fluide entre un *Mode Clair* et un *Mode Sombre*.
    *   Historique des actions de combat intégré à l'écran.

## 🛠️ Installation

1. **Clonez le dépôt :**
```bash
git clone https://github.com/Teilenh/PyKemon.git
cd PyKemon
```

2. **Créez un environnement virtuel (recommandé) et activez-le :**
```bash
python -m venv venv
source venv/bin/activate  # Sur Linux/Mac
# ou venv\Scripts\activate sur Windows
```

3. **Installez les dépendances :**
```bash
pip install PyQt6 requests
```

4. **Lancez le jeu :**
```bash
python main.py
```

## 🏗️ Structure du projet

```text
PyKemon/
├── Assets/             # Sauvegardes d'équipe et fonds (battle_bg.png, equipe.csv)
├── src/
│   ├── assets/
│   │   └── sprites/    # Téléchargement automatique des sprites
│   ├── core/           # Moteur du jeu (Logique métier)
│   │   ├── pokemon.py      # Entité Pokémon, Movesets, Statuts
│   │   ├── combat.py       # Mathématiques, Dégâts, Altérations
│   │   ├── team_builder.py # Sérialisation et chargement de l'équipe
│   │   └── config.py       # Configuration globale (ex: Versioning)
│   ├── gui/            # Interface graphique PyQt6
│   │   ├── components/     # Composants réutilisables (Boutons, Barres de vie)
│   │   ├── combat.py       # Affichage de l'Arène et UI Combat
│   │   ├── team_builder_GUI.py # Fenêtre de conception d'équipe
│   │   └── theme.py        # Gestion centralisée du CSS et du clair/sombre
│   └── utils/
│       └── sprite_downloader.py # Client requêtant PokéAPI
├── gen_pokemon.py      # Script de génération du Pokédex
├── test_pykemon.py     # Tests de robustesse du moteur
└── main.py             # Point d'entrée de l'application
```

## 🤝 Contribution

Les contributions sont les bienvenues ! PyKemon est un projet ludique et open-source. N'hésitez pas à ouvrir une *issue* ou une *pull request* pour ajouter de nouvelles attaques ou améliorer le moteur.

## 📄 Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.

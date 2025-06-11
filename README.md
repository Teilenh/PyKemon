# PyKemon
projet pour apprendre python OO
Un jeu Pokémon en Python avec interface graphique PyQt6.

## Fonctionnalités

- Team Builder pour créer et gérer votre équipe de Pokémon
- Système de combat tour par tour
- Interface graphique moderne avec PyQt6 et Tk
- affichage d'images
- Système de types et de dégâts fidèle à la première génération

## Installation

1. Clonez le dépôt :
```bash
git clone https://github.com/Teilenh/PyKemon.git
cd PyKemon
```

2. Installez les dépendances :
```bash
pip install PyQt6
```

3. Lancez le jeu :
```bash
python main.py
```

## Structure du projet

```
src/
├── core/           # Logique métier
│   ├── pokemon.py      # Gestion des Pokémon et attaques
│   ├── combat.py       # Système de combat
│   ├── team_builder.py # Gestion des équipes
│   └── adversaire.py   # IA de l'adversaire
├── gui/            # Interface graphique
│   ├── components/     # Composants réutilisables
│   ├── combat.py      # Interface de combat
│   └── team_builder_GUI.py  # Interface du Team Builder
└── assets/         # Ressources (sprites, etc.)
    └── sprites/        # Images des Pokémon
```

## Contribution

Les contributions sont les bienvenues ! N'hésitez pas à ouvrir une issue ou une pull request.

## Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.

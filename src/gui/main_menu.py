from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton, QApplication
)
from PyQt6.QtCore import Qt
from .theme import get_platform_style, ThemeSwitchButton
from .team_builder_GUI import TeamBuilderGUI
from .combat import CombatGUI
from src.core.config import VERSION

class MenuPrincipal(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        
        # Layout principal (vertical)
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        
        # === Zone centrale (Titres et Boutons) ===
        center_container = QWidget()
        center_layout = QVBoxLayout(center_container)
        center_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        center_layout.setSpacing(15)
        
        # Titre
        titre = QLabel("PyKemon")
        titre.setProperty("class", "title")
        titre.setAlignment(Qt.AlignmentFlag.AlignCenter)
        center_layout.addWidget(titre)
        
        # Sous-titre
        sous_titre = QLabel("Combat Pokémon - 1ère Génération")
        sous_titre.setProperty("class", "subtitle")
        sous_titre.setAlignment(Qt.AlignmentFlag.AlignCenter)
        center_layout.addWidget(sous_titre)
        
        center_layout.addSpacing(40)
        
        # Boutons
        btn_team = QPushButton("Créer une équipe")
        btn_team.setProperty("class", "custom-button")
        btn_team.setMinimumWidth(250)
        btn_team.clicked.connect(self.ouvrir_team_builder)
        center_layout.addWidget(btn_team)
        
        btn_combat = QPushButton("Lancer un combat")
        btn_combat.setProperty("class", "custom-button")
        btn_combat.setMinimumWidth(250)
        btn_combat.clicked.connect(self.lancer_combat)
        center_layout.addWidget(btn_combat)
        
        btn_quitter = QPushButton("Quitter")
        btn_quitter.setObjectName("btn_quitter")
        btn_quitter.setMinimumWidth(250)
        btn_quitter.clicked.connect(self.quitter_application)
        center_layout.addWidget(btn_quitter)
        
        # Ajouter le conteneur central au layout principal
        main_layout.addWidget(center_container, stretch=1)
        
        # === Zone inférieure (Bouton de thème et Version) ===
        bottom_container = QWidget()
        bottom_layout = QHBoxLayout(bottom_container)
        bottom_layout.setContentsMargins(20, 10, 20, 20)
        
        # Bouton de changement de thème (en bas à gauche)
        self.theme_switch = ThemeSwitchButton()
        bottom_layout.addWidget(self.theme_switch)
        
        # Espace flexible
        bottom_layout.addStretch()
        
        # Version (centrée)
        version = QLabel(f"Version {VERSION} - Première Génération")
        version.setProperty("class", "subtitle")
        bottom_layout.addWidget(version)
        
        # Espace flexible
        bottom_layout.addStretch()
        
        # Espaceur invisible pour équilibrer parfaitement le bouton de thème
        spacer = QWidget()
        spacer.setFixedSize(36, 36)
        bottom_layout.addWidget(spacer)
        
        # Ajouter le conteneur inférieur au layout principal
        main_layout.addWidget(bottom_container)
        
        # Application du style
        self.setStyleSheet(get_platform_style())

    def ouvrir_team_builder(self):
        self.main_window.show_team_builder()

    def lancer_combat(self):
        self.main_window.show_combat()

    def quitter_application(self):
        QApplication.quit() 
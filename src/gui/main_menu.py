from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout,
    QLabel, QPushButton, QApplication
)
from PyQt6.QtCore import Qt
from .theme import get_platform_style, ThemeSwitchButton
from .team_builder_GUI import TeamBuilderGUI
from .combat import CombatGUI

class MenuPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyKemon")
        self.setMinimumSize(800, 600)
        
        # Widget central
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Layout principal
        layout = QVBoxLayout(central_widget)
        layout.setSpacing(20)
        layout.setContentsMargins(30, 30, 30, 30)
        
        # Titre
        titre = QLabel("PyKemon")
        titre.setProperty("class", "title")
        titre.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(titre)
        
        # Sous-titre
        sous_titre = QLabel("Combat Pokémon - 1ère Génération")
        sous_titre.setProperty("class", "subtitle")
        sous_titre.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(sous_titre)
        
        # Boutons
        btn_team = QPushButton("Créer une équipe")
        btn_team.setProperty("class", "custom-button")
        btn_team.clicked.connect(self.ouvrir_team_builder)
        layout.addWidget(btn_team)
        
        btn_combat = QPushButton("Lancer un combat")
        btn_combat.setProperty("class", "custom-button")
        btn_combat.clicked.connect(self.lancer_combat)
        layout.addWidget(btn_combat)
        
        btn_quitter = QPushButton("Quitter")
        btn_quitter.setObjectName("btn_quitter")
        btn_quitter.clicked.connect(self.quitter_application)
        layout.addWidget(btn_quitter)
        
        # Bouton de changement de thème
        self.theme_switch = ThemeSwitchButton()
        layout.addWidget(self.theme_switch, alignment=Qt.AlignmentFlag.AlignRight)
        
        # Version
        version = QLabel("Version 1.0 - Première Génération")
        version.setProperty("class", "subtitle")
        version.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(version)
        
        # Application du style
        self.setStyleSheet(get_platform_style())

    def ouvrir_team_builder(self):
        self.team_builder_window = QMainWindow(self)
        self.team_builder_window.setWindowTitle("PyKemon - Team Builder")
        self.team_builder_window.setMinimumSize(1000, 600)
        
        team_builder = TeamBuilderGUI()
        self.team_builder_window.setCentralWidget(team_builder)
        self.team_builder_window.setStyleSheet(get_platform_style())
        self.team_builder_window.show()

    def lancer_combat(self):
        self.combat_window = CombatGUI()
        self.combat_window.show()

    def quitter_application(self):
        QApplication.quit() 
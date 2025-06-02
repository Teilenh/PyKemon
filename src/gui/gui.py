from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout,
    QHBoxLayout, QLabel, QPushButton, QFrame, QDialog,
    QListWidget, QMessageBox, QDialogButtonBox, QScrollArea,
    QGridLayout
)
from PyQt6.QtCore import Qt, QPropertyAnimation, QRect, QEasingCurve, QSettings
from PyQt6.QtGui import QFont, QPixmap
import platform
import os
from pathlib import Path
from random import choice
from ..core.pokemon import POKEMONS_DISPONIBLES, creer_pokemon
from ..core.combat import calcul_degats
from ..core.team_builder import TeamBuilder
from ..core.adversaire import Adversaire
from ..utils.sprite_downloader import normalize_name

class ThemeManager:
    """Gestionnaire de thème pour l'application"""
    def __init__(self):
        self.settings = QSettings('PyKemon', 'Theme')
        self._is_dark = self.settings.value('is_dark', True, type=bool)

    @property
    def is_dark(self):
        return self._is_dark

    @is_dark.setter
    def is_dark(self, value):
        self._is_dark = value
        self.settings.setValue('is_dark', value)
        self.settings.sync()

    def toggle_theme(self):
        self.is_dark = not self.is_dark
        return self.is_dark

# Instance globale du gestionnaire de thème
theme_manager = ThemeManager()

def is_dark_theme_active():
    """Détecte si le thème sombre est actif sur le système"""
    if platform.system().lower() == 'linux':
        # Détection pour GTK
        try:
            import subprocess
            result = subprocess.run(
                ['gsettings', 'get', 'org.gnome.desktop.interface', 'gtk-theme'],
                capture_output=True,
                text=True
            )
            theme_name = result.stdout.strip().lower().replace("'", "")
            return 'dark' in theme_name
        except:
            # Si gsettings n'est pas disponible, on vérifie la variable d'environnement
            return os.environ.get('GTK_THEME', '').lower().endswith(':dark')
    return False

def get_platform_style():
    """Retourne le style approprié selon la plateforme et le thème"""
    system = platform.system().lower()
    
    # Utilisation du thème forcé si on est sous Linux
    if system == 'linux':
        is_dark = theme_manager.is_dark
    else:
        is_dark = True  # Toujours sombre pour Windows et autres

    if is_dark:
        # Couleurs du thème sombre
        colors = {
            'background': '#36393f',
            'secondary': '#2f3136',
            'surface': '#40444b',
            'accent': '#5865f2',
            'accent_hover': '#4752c4',
            'text': '#dcddde',
            'text_secondary': '#96989d',
            'success': '#43b581',
            'danger': '#f04747',
            'border': '#202225'
        }
    else:
        # Thème clair avec intégration système
        colors = {
            'background': 'palette(window)',
            'secondary': 'palette(base)',
            'surface': 'palette(button)',
            'accent': 'palette(highlight)',
            'accent_hover': 'palette(highlight)',
            'text': 'palette(text)',
            'text_secondary': 'palette(text)',
            'success': '#43b581',
            'danger': '#f04747',
            'border': 'palette(mid)'
        }

    return f"""
        /* Style global */
        QWidget {{
            font-family: system-ui;
            background-color: {colors['background']};
            color: {colors['text']};
        }}
        
        /* Style des fenêtres */
        QMainWindow, QDialog {{
            background-color: {colors['background']};
        }}
        
        /* Style des boutons standard */
        QPushButton.custom-button {{
            background-color: {colors['surface']};
            color: {colors['text']};
            border: none;
            border-radius: 4px;
            padding: 8px 16px;
            font-weight: 500;
            min-height: 38px;
        }}
        
        QPushButton.custom-button:hover {{
            background-color: {colors['accent']};
            color: palette(light);
        }}
        
        QPushButton.custom-button:pressed {{
            background-color: {colors['accent_hover']};
        }}
        
        /* Style des frames */
        QFrame.custom-frame {{
            background-color: {colors['secondary']};
            border: 1px solid {colors['border']};
            border-radius: 8px;
        }}
        
        /* Style des labels */
        QLabel.title {{
            color: {colors['text']};
            font-size: 24px;
            font-weight: bold;
        }}
        
        QLabel.subtitle {{
            color: {colors['text_secondary']};
            font-size: 16px;
        }}
        
        /* Style des listes */
        QListWidget {{
            background-color: {colors['secondary']};
            border: 1px solid {colors['border']};
            border-radius: 4px;
        }}
        
        QListWidget::item {{
            color: {colors['text']};
            border-radius: 2px;
            padding: 6px;
        }}
        
        QListWidget::item:hover {{
            background-color: {colors['surface']};
        }}
        
        QListWidget::item:selected {{
            background-color: {colors['accent']};
            color: palette(light);
        }}
        
        /* Style des boutons spéciaux */
        QPushButton#btn_sauvegarder {{
            background-color: {colors['success']};
            color: white;
        }}
        
        QPushButton#btn_quitter {{
            background-color: {colors['danger']};
            color: white;
        }}
        
        /* Style de la barre de vie */
        QFrame#barre_vie {{
            background-color: {colors['danger']};
            border-radius: 4px;
        }}
        
        QFrame#barre_vie > QFrame {{
            background-color: {colors['success']};
            border-radius: 4px;
        }}
        
        /* Style du bouton de thème */
        QPushButton#theme_switch {{
            font-size: 20px;
            border-radius: 15px;
            min-width: 30px;
            min-height: 30px;
            padding: 5px;
            background-color: {colors['surface']};
            color: {colors['text']};
        }}
        
        QPushButton#theme_switch:hover {{
            background-color: {colors['accent']};
        }}
    """

class BoutonAttaque(QPushButton):
    def __init__(self, text="", parent=None):
        super().__init__(text, parent)
        self.setMinimumHeight(50)
        self.setProperty("class", "custom-button")
        self.setStyleSheet("""
            QPushButton {
                font-size: 14px;
            }
        """)

class BarreVie(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMinimumHeight(20)
        self.setMaximumHeight(20)
        self.value = 100
        self.setObjectName("barre_vie")
        
        # Création de la barre interne
        self.barre_interne = QFrame(self)
        self.barre_interne.setGeometry(0, 0, self.width(), self.height())
        
        self.animation = QPropertyAnimation(self.barre_interne, b"geometry")
        self.animation.setDuration(500)
        self.animation.setEasingCurve(QEasingCurve.Type.OutCubic)

    def setValue(self, value):
        self.value = max(0, min(100, value))
        nouvelle_largeur = int(self.width() * (self.value / 100))
        
        self.animation.setStartValue(self.barre_interne.geometry())
        self.animation.setEndValue(QRect(0, 0, nouvelle_largeur, self.height()))
        self.animation.start()

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.barre_interne.setGeometry(0, 0, int(self.width() * (self.value / 100)), self.height())

class ThemeSwitchButton(QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("theme_switch")
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.update_icon()
        self.clicked.connect(self.toggle_theme)

    def update_icon(self):
        # Utilisation d'émojis Unicode pour les icônes
        self.setText("🌙" if theme_manager.is_dark else "☀️")

    def toggle_theme(self):
        is_dark = theme_manager.toggle_theme()
        self.update_icon()
        # Mettre à jour le style de toutes les fenêtres
        for widget in QApplication.topLevelWidgets():
            widget.setStyleSheet(get_platform_style())
            # Forcer la mise à jour visuelle
            widget.style().unpolish(widget)
            widget.style().polish(widget)
            widget.update()

class MenuPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyKemon")
        self.setMinimumSize(400, 500)
        
        # Application du style de la plateforme
        self.setStyleSheet(get_platform_style())
        
        # Widget central
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        
        # Titre
        titre = QLabel("PyKemon")
        titre.setProperty("class", "title")
        titre.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(titre)
        
        # Description
        description = QLabel("Combat Pokémon - 1ère Génération")
        description.setProperty("class", "subtitle")
        description.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(description)
        
        layout.addStretch()
        
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
        btn_quitter.setProperty("class", "custom-button")
        btn_quitter.clicked.connect(self.quitter_application)
        layout.addWidget(btn_quitter)
        
        layout.addStretch()
        
        # Version
        version = QLabel("Version 1.0 - Première Génération")
        version.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(version)

        # Ajout du bouton de thème en bas à gauche
        bottom_layout = QHBoxLayout()
        theme_switch = ThemeSwitchButton()
        bottom_layout.addWidget(theme_switch)
        bottom_layout.addStretch()  # Pour pousser le bouton à gauche
        layout.addLayout(bottom_layout)

        # Garder une référence aux fenêtres
        self.team_builder_window = None
        self.combat_window = None

    def ouvrir_team_builder(self):
        self.team_builder_window = TeamBuilderGUI()
        self.team_builder_window.show()

    def lancer_combat(self):
        self.combat_window = CombatGUI()
        self.combat_window.show()

    def quitter_application(self):
        QApplication.quit()

class PokemonFrame(QFrame):
    def __init__(self, index, parent=None):
        super().__init__(parent)
        self.setProperty("class", "custom-frame")
        self.setMinimumSize(150, 150)
        
        # Layout principal
        layout = QVBoxLayout(self)
        
        # Label pour le sprite
        self.sprite_label = QLabel()
        self.sprite_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.sprite_label.setMinimumSize(96, 96)
        layout.addWidget(self.sprite_label)
        
        # Label pour le nom
        self.nom_label = QLabel("Vide")
        self.nom_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.nom_label)
        
        self.index = index
        self.vide = True
        
        # Rendre le widget cliquable
        self.setMouseTracking(True)
        self.setCursor(Qt.CursorShape.PointingHandCursor)
    
    def mousePressEvent(self, event):
        if not self.vide and event.button() == Qt.MouseButton.LeftButton:
            # Trouver le parent TeamBuilderGUI
            parent = self.parent()
            while parent and not isinstance(parent, TeamBuilderGUI):
                parent = parent.parent()
            
            if parent:
                parent.configurer_attaques(self.index)
    
    def charger_pokemon(self, nom_pokemon=None):
        if nom_pokemon:
            # Charger le sprite
            sprite_path = Path("src/assets/sprites") / f"{nom_pokemon.lower()}.png"
            if sprite_path.exists():
                pixmap = QPixmap(str(sprite_path))
                self.sprite_label.setPixmap(pixmap.scaled(96, 96, Qt.AspectRatioMode.KeepAspectRatio))
            else:
                self.sprite_label.setText("Pas de sprite")
            
            self.nom_label.setText(nom_pokemon)
            self.vide = False
        else:
            self.sprite_label.clear()
            self.nom_label.setText("Vide")
            self.vide = True

class TeamBuilderGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Team Builder")
        self.setMinimumSize(800, 600)
        
        # Création du widget central et du layout principal
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        
        # Titre
        titre = QLabel("Team Builder")
        titre.setProperty("class", "title")
        titre.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(titre)
        
        # Zone de l'équipe (haut)
        equipe_frame = QFrame()
        equipe_frame.setProperty("class", "custom-frame")
        layout_equipe = QVBoxLayout(equipe_frame)
        
        # Titre de l'équipe
        titre_equipe = QLabel("Votre Équipe")
        titre_equipe.setProperty("class", "subtitle")
        titre_equipe.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout_equipe.addWidget(titre_equipe)
        
        # Grille des emplacements Pokémon
        grid_layout = QGridLayout()
        self.emplacements = []
        for i in range(6):
            emplacement = PokemonFrame(i)
            self.emplacements.append(emplacement)
            grid_layout.addWidget(emplacement, i // 3, i % 3)
        layout_equipe.addLayout(grid_layout)
        
        layout.addWidget(equipe_frame, stretch=2)
        
        # Zone PC (bas)
        pc_frame = QFrame()
        pc_frame.setProperty("class", "custom-frame")
        layout_pc = QVBoxLayout(pc_frame)
        
        # Titre du PC
        titre_pc = QLabel("Boîte PC")
        titre_pc.setProperty("class", "subtitle")
        titre_pc.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout_pc.addWidget(titre_pc)
        
        # Grille de Pokémon disponibles avec scroll
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setFrameShape(QFrame.Shape.NoFrame)
        
        pc_grid_widget = QWidget()
        pc_grid = QGridLayout(pc_grid_widget)
        pc_grid.setSpacing(10)
        
        # Création des boutons pour chaque Pokémon disponible
        pokemons_disponibles = sorted(POKEMONS_DISPONIBLES.keys())
        row, col = 0, 0
        max_cols = 6
        
        for pokemon_nom in pokemons_disponibles:
            pokemon_btn = QPushButton(pokemon_nom)
            pokemon_btn.setMinimumSize(120, 120)
            pokemon_btn.setProperty("class", "custom-button")
            pokemon_btn.clicked.connect(lambda checked, nom=pokemon_nom: self.ajouter_pokemon(nom))
            pc_grid.addWidget(pokemon_btn, row, col)
            
            col += 1
            if col >= max_cols:
                col = 0
                row += 1
        
        scroll_area.setWidget(pc_grid_widget)
        layout_pc.addWidget(scroll_area)
        layout.addWidget(pc_frame, stretch=3)
        
        # Boutons de contrôle
        boutons_layout = QHBoxLayout()
        
        btn_sauvegarder = QPushButton("Sauvegarder Équipe")
        btn_sauvegarder.setProperty("class", "custom-button")
        btn_sauvegarder.setObjectName("btn_sauvegarder")
        btn_sauvegarder.clicked.connect(self.sauvegarder_equipe)
        boutons_layout.addWidget(btn_sauvegarder)
        
        btn_quitter = QPushButton("Quitter")
        btn_quitter.setProperty("class", "custom-button")
        btn_quitter.setObjectName("btn_quitter")
        btn_quitter.clicked.connect(self.close)
        boutons_layout.addWidget(btn_quitter)
        
        layout.addLayout(boutons_layout)
        
        # Initialisation du TeamBuilder
        self.team_builder = TeamBuilder()
        self.charger_equipe_existante()
        
        # Application du style
        self.setStyleSheet(get_platform_style())
    
    def ajouter_pokemon(self, nom_pokemon):
        """Ajoute un Pokémon à l'équipe"""
        if len(self.team_builder.equipe) >= 6:
            QMessageBox.warning(self, "Erreur", "L'équipe est déjà complète (6 Pokémon maximum)")
            return
            
        success, message = self.team_builder.ajouter_pokemon(nom_pokemon)
        if success:
            self.mettre_a_jour_emplacement(len(self.team_builder.equipe) - 1, self.team_builder.equipe[-1])
    
    def mettre_a_jour_emplacement(self, index, pokemon=None):
        """Met à jour l'affichage d'un emplacement"""
        if 0 <= index < len(self.emplacements):
            self.emplacements[index].charger_pokemon(pokemon.nom if pokemon else None)
    
    def charger_equipe_existante(self):
        """Charge l'équipe existante"""
        success, _ = self.team_builder.charger_equipe()
        if success:
            for i, pokemon in enumerate(self.team_builder.equipe):
                self.mettre_a_jour_emplacement(i, pokemon)

    def sauvegarder_equipe(self):
        """Sauvegarde l'équipe actuelle"""
        succes, message = self.team_builder.sauvegarder_equipe()
        if succes:
            QMessageBox.information(self, "Succès", message)
        else:
            QMessageBox.warning(self, "Erreur", message)

    def configurer_attaques(self, index):
        """Ouvre la fenêtre de configuration des attaques pour un Pokémon"""
        if 0 <= index < len(self.team_builder.equipe):
            pokemon = self.team_builder.equipe[index]
            dialog = ConfigurationAttaquesDialog(pokemon, self)
            if dialog.exec() == QDialog.DialogCode.Accepted:
                # Mise à jour des attaques du Pokémon
                attaques_selectionnees = []
                for item in dialog.liste_attaques.selectedItems():
                    attaques_selectionnees.append(item.text())
                
                success, message = self.team_builder.configurer_attaques(index, attaques_selectionnees)
                if not success:
                    QMessageBox.warning(self, "Erreur", message)

class ConfigurationAttaquesDialog(QDialog):
    def __init__(self, pokemon, parent=None):
        super().__init__(parent)
        self.pokemon = pokemon
        self.setWindowTitle(f"Configuration des attaques - {pokemon.nom}")
        self.setMinimumSize(400, 400)
        
        # Application du style de la plateforme
        self.setStyleSheet(get_platform_style())
        
        layout = QVBoxLayout(self)
        
        # Titre
        titre = QLabel(f"Attaques de {pokemon.nom}")
        titre.setProperty("class", "title")
        titre.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(titre)
        
        # Zone des emplacements d'attaques
        emplacements_widget = QWidget()
        emplacements_layout = QGridLayout(emplacements_widget)
        emplacements_layout.setSpacing(10)
        
        self.emplacements_attaques = []
        for i in range(4):
            emplacement = QPushButton("Aucune attaque")
            emplacement.setMinimumSize(180, 60)
            emplacement.setProperty("class", "custom-button")
            row, col = divmod(i, 2)
            emplacements_layout.addWidget(emplacement, row, col)
            self.emplacements_attaques.append(emplacement)
            
        layout.addWidget(emplacements_widget)
        
        # Liste des attaques disponibles
        self.liste_attaques = QListWidget()
        self.liste_attaques.setSelectionMode(QListWidget.SelectionMode.MultiSelection)
        self.liste_attaques.setProperty("class", "custom-frame")
        
        # Ajout des attaques disponibles
        for attaque in pokemon.attaques_possibles:
            self.liste_attaques.addItem(attaque)
            
        # Pré-sélection des attaques actuelles
        for attaque in pokemon.attaques:
            items = self.liste_attaques.findItems(attaque.nom, Qt.MatchFlag.MatchExactly)
            for item in items:
                item.setSelected(True)
        
        # Connecter le signal de changement de sélection
        self.liste_attaques.itemSelectionChanged.connect(self.mettre_a_jour_emplacements)
        
        layout.addWidget(self.liste_attaques)
        
        # Boutons OK/Annuler
        buttons = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel
        )
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        layout.addWidget(buttons)
        
        # Mise à jour initiale des emplacements
        self.mettre_a_jour_emplacements()

    def mettre_a_jour_emplacements(self):
        """Met à jour l'affichage des emplacements d'attaques"""
        attaques_selectionnees = [item.text() for item in self.liste_attaques.selectedItems()]
        
        # Réinitialisation des emplacements
        for emplacement in self.emplacements_attaques:
            emplacement.setText("Aucune attaque")
            emplacement.setEnabled(False)
        
        # Mise à jour avec les attaques sélectionnées
        for i, attaque in enumerate(attaques_selectionnees[:4]):
            self.emplacements_attaques[i].setText(attaque)
            self.emplacements_attaques[i].setEnabled(True)

    def accept(self):
        attaques_selectionnees = [item.text() for item in self.liste_attaques.selectedItems()]
        if len(attaques_selectionnees) > 4:
            QMessageBox.warning(self, "Erreur", "Vous ne pouvez sélectionner que 4 attaques maximum")
            return
            
        if not attaques_selectionnees:
            QMessageBox.warning(self, "Erreur", "Veuillez sélectionner au moins une attaque")
            return
            
        self.pokemon.attaques = []  # Réinitialisation des attaques
        
        erreurs = []
        for attaque in attaques_selectionnees:
            if not self.pokemon.apprendre_attaque(attaque):
                erreurs.append(f"Impossible d'apprendre {attaque}")
        
        if erreurs:
            QMessageBox.warning(self, "Erreur", "\n".join(erreurs))
            return
            
        super().accept()

class CombatGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyKemon Combat")
        self.setMinimumSize(800, 600)
        
        # Application du style avec le thème actuel
        self.setStyleSheet(get_platform_style())

        # Chargement de l'équipe du joueur
        self.team_builder = TeamBuilder()
        success, message = self.team_builder.charger_equipe()
        
        if success and self.team_builder.equipe:
            self.equipe_joueur = self.team_builder.equipe
            self.pokemon_joueur = self.equipe_joueur[0]  # Premier Pokémon de l'équipe
        else:
            self.pokemon_joueur = creer_pokemon("Pikachu")  # Pokémon par défaut
            self.equipe_joueur = [self.pokemon_joueur]
            
        # Création d'un adversaire aléatoire
        self.adversaire = Adversaire(4)  # Deux Pokémon pour l'adversaire
        self.pokemon_adversaire = self.adversaire.pokemon_actif
        
        if not self.pokemon_adversaire:
            self.pokemon_adversaire = creer_pokemon("Carapuce")  # Adversaire par défaut

        # Configuration des attaques initiales
        if not self.pokemon_joueur.attaques:
            for attaque in self.pokemon_joueur.attaques_possibles[:4]:
                self.pokemon_joueur.apprendre_attaque(attaque)
        if not self.pokemon_adversaire.attaques:
            for attaque in self.pokemon_adversaire.attaques_possibles[:4]:
                self.pokemon_adversaire.apprendre_attaque(attaque)

        # Création du widget central et configuration de l'interface
        self.initialiser_interface()
        
        # Mise à jour initiale de l'interface
        self.mettre_a_jour_interface()
        self.mettre_a_jour_interface_adversaire()
        self.ajouter_message("Le combat commence!")

    def initialiser_interface(self):
        # Création du widget central
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Layout principal
        layout_principal = QVBoxLayout(central_widget)
        
        # Zone de combat
        zone_combat = QWidget()
        layout_combat = QHBoxLayout(zone_combat)
        
        # Zone joueur
        zone_joueur = self.creer_zone_pokemon(self.pokemon_joueur, True)
        layout_combat.addWidget(zone_joueur)
        
        # Espace entre les zones
        layout_combat.addStretch()
        
        # Zone adversaire
        zone_adversaire = self.creer_zone_pokemon(self.pokemon_adversaire, False)
        layout_combat.addWidget(zone_adversaire)
        
        layout_principal.addWidget(zone_combat)
        
        # Zone de message
        self.message_frame = QFrame()
        self.message_frame.setObjectName("message_frame")
        layout_principal.addWidget(self.message_frame)
        
        message_layout = QVBoxLayout(self.message_frame)
        self.historique_messages = QLabel()
        self.historique_messages.setStyleSheet("""
            QLabel {
                font-size: 14px;
                min-height: 60px;
            }
        """)
        self.historique_messages.setAlignment(Qt.AlignmentFlag.AlignCenter)
        message_layout.addWidget(self.historique_messages)
        self.messages = []

        # Zone des boutons d'attaque
        self.zone_boutons = QWidget()
        self.zone_boutons.setObjectName("zone_boutons")
        self.layout_boutons = QHBoxLayout(self.zone_boutons)
        
        # Création des boutons d'attaque
        self.boutons_attaque = []
        for attaque in self.pokemon_joueur.attaques:
            bouton = self.creer_bouton_attaque(attaque)
            self.layout_boutons.addWidget(bouton)
            self.boutons_attaque.append(bouton)
        
        layout_principal.addWidget(self.zone_boutons)

        # Zone des Pokémon disponibles
        self.zone_pokemon_dispo = QWidget()
        layout_pokemon_dispo = QHBoxLayout(self.zone_pokemon_dispo)
        self.zone_pokemon_dispo.hide()

        # Création des boutons pour chaque Pokémon
        self.boutons_pokemon = []
        for pokemon in self.equipe_joueur:
            bouton = QPushButton(f"{pokemon.nom}\n{pokemon.pv}/{pokemon.pv_max} PV")
            bouton.setMinimumHeight(50)
            bouton.clicked.connect(lambda checked, p=pokemon: self.changer_pokemon(p))
            layout_pokemon_dispo.addWidget(bouton)
            self.boutons_pokemon.append(bouton)

        layout_principal.addWidget(self.zone_pokemon_dispo)

        # Zone des boutons de fin de combat
        self.zone_fin_combat = QWidget()
        layout_fin_combat = QHBoxLayout(self.zone_fin_combat)
        
        # Bouton recommencer
        self.btn_recommencer = QPushButton("Recommencer")
        self.btn_recommencer.setProperty("class", "custom-button")
        self.btn_recommencer.setObjectName("btn_sauvegarder")
        self.btn_recommencer.clicked.connect(self.recommencer_combat)
        layout_fin_combat.addWidget(self.btn_recommencer)
        
        # Bouton quitter
        self.btn_quitter = QPushButton("Quitter")
        self.btn_quitter.setProperty("class", "custom-button")
        self.btn_quitter.setObjectName("btn_quitter")
        self.btn_quitter.clicked.connect(self.close)
        layout_fin_combat.addWidget(self.btn_quitter)
        
        self.zone_fin_combat.hide()
        layout_principal.addWidget(self.zone_fin_combat)

    def creer_zone_pokemon(self, pokemon, est_joueur):
        zone = QWidget()
        layout = QVBoxLayout(zone)
        
        # Nom du Pokémon
        nom = QLabel(pokemon.nom)
        nom.setFont(QFont("Arial", 16, QFont.Weight.Bold))
        nom.setAlignment(Qt.AlignmentFlag.AlignCenter)
        if est_joueur:
            self.label_nom_joueur = nom
        else:
            self.label_nom_adversaire = nom
        layout.addWidget(nom)
        
        # Sprite du Pokémon
        sprite = QLabel()
        sprite.setMinimumSize(150, 150)
        sprite.setAlignment(Qt.AlignmentFlag.AlignCenter)
        if est_joueur:
            self.sprite_joueur = sprite
        else:
            self.sprite_adversaire = sprite
        
        # Charger le sprite initial
        self.mettre_a_jour_sprite(pokemon, est_joueur)
        layout.addWidget(sprite)
        
        # Barre de vie
        barre_vie = BarreVie()
        if est_joueur:
            self.barre_vie_joueur = barre_vie
        else:
            self.barre_vie_adversaire = barre_vie
        layout.addWidget(barre_vie)
        
        # Information PV
        info_pv = QLabel(f"PV: {pokemon.pv}/{pokemon.pv_max}")
        info_pv.setAlignment(Qt.AlignmentFlag.AlignCenter)
        if est_joueur:
            self.label_pv_joueur = info_pv
        else:
            self.label_pv_adversaire = info_pv
        layout.addWidget(info_pv)
        
        return zone

    def mettre_a_jour_sprite(self, pokemon, est_joueur):
        """Met à jour le sprite d'un Pokémon"""
        sprite_label = self.sprite_joueur if est_joueur else self.sprite_adversaire
        normalized_name = normalize_name(pokemon.nom)
        sprite_filename = f"{normalized_name}_back.png" if est_joueur else f"{normalized_name}.png"
        sprite_path = Path("src/assets/sprites") / sprite_filename
        
        if sprite_path.exists():
            pixmap = QPixmap(str(sprite_path))
            sprite_label.setPixmap(pixmap.scaled(150, 150, Qt.AspectRatioMode.KeepAspectRatio))
        else:
            sprite_label.setText("[ Sprite manquant ]")
            sprite_label.setStyleSheet("""
                QLabel {
                    background-color: #dcdde1;
                    border-radius: 10px;
                    padding: 20px;
                    font-size: 20px;
                }
            """)

    def creer_bouton_attaque(self, attaque):
        bouton = BoutonAttaque(f"{attaque.nom}\n{attaque.type} - {attaque.puissance}")
        bouton.clicked.connect(lambda: self.utiliser_attaque(attaque))
        return bouton

    def changer_pokemon(self, nouveau_pokemon):
        if nouveau_pokemon.est_ko():
            self.ajouter_message(f"{nouveau_pokemon.nom} est K.O. et ne peut pas combattre!")
            return

        self.pokemon_joueur = nouveau_pokemon
        self.mettre_a_jour_interface()
        self.zone_pokemon_dispo.hide()

        # Tour de l'adversaire après le changement
        self.tour_adversaire()

    def mettre_a_jour_interface(self):
        # Mise à jour des informations du Pokémon joueur
        self.label_nom_joueur.setText(self.pokemon_joueur.nom)
        self.label_pv_joueur.setText(f"PV: {self.pokemon_joueur.pv}/{self.pokemon_joueur.pv_max}")
        pourcentage_vie = (self.pokemon_joueur.pv / self.pokemon_joueur.pv_max) * 100
        self.barre_vie_joueur.setValue(pourcentage_vie)
        self.mettre_a_jour_sprite(self.pokemon_joueur, True)

        # Mise à jour des boutons d'attaque
        for bouton in self.boutons_attaque:
            bouton.setParent(None)
        self.boutons_attaque.clear()

        layout_boutons = self.findChild(QWidget, "zone_boutons").layout()
        for attaque in self.pokemon_joueur.attaques:
            bouton = self.creer_bouton_attaque(attaque)
            layout_boutons.addWidget(bouton)
            self.boutons_attaque.append(bouton)

        # Mise à jour des boutons Pokémon
        for i, pokemon in enumerate(self.equipe_joueur):
            self.boutons_pokemon[i].setText(f"{pokemon.nom}\n{pokemon.pv}/{pokemon.pv_max} PV")
            self.boutons_pokemon[i].setEnabled(not pokemon.est_ko())

    def mettre_a_jour_interface_adversaire(self):
        self.label_pv_adversaire.setText(f"PV: {self.pokemon_adversaire.pv}/{self.pokemon_adversaire.pv_max}")
        pourcentage_vie = (self.pokemon_adversaire.pv / self.pokemon_adversaire.pv_max) * 100
        self.barre_vie_adversaire.setValue(pourcentage_vie)
        self.label_nom_adversaire.setText(self.pokemon_adversaire.nom)
        self.mettre_a_jour_sprite(self.pokemon_adversaire, False)

    def ajouter_message(self, message):
        """Ajoute un message à l'historique et met à jour l'affichage"""
        self.messages.append(message)
        if len(self.messages) > 3:  # Garde les 3 derniers messages
            self.messages.pop(0)
        self.historique_messages.setText("\n".join(self.messages))

    def tour_adversaire(self):
        if self.pokemon_adversaire.est_ko():
            nouveau_pokemon = self.adversaire.choisir_pokemon()
            if nouveau_pokemon:
                self.pokemon_adversaire = nouveau_pokemon
                self.ajouter_message(f"L'adversaire envoie {self.pokemon_adversaire.nom}!")
                self.mettre_a_jour_interface_adversaire()
                # Réactiver les boutons après le changement de Pokémon
                for bouton in self.boutons_attaque:
                    bouton.setEnabled(True)
                return
            else:
                self.ajouter_message("Vous avez gagné le combat!")
                self.zone_boutons.hide()
                self.zone_fin_combat.show()
                return

        # Ne pas attaquer si le Pokémon est KO
        if self.pokemon_adversaire.est_ko():
            return

        attaque_adversaire = choice(self.pokemon_adversaire.attaques)
        degats_adversaire = calcul_degats(self.pokemon_adversaire, self.pokemon_joueur, attaque_adversaire)
        self.pokemon_joueur.subir_degats(degats_adversaire)

        self.ajouter_message(f"{self.pokemon_adversaire.nom} utilise {attaque_adversaire.nom} et inflige {degats_adversaire} dégâts!")
        self.mettre_a_jour_interface()

        if self.pokemon_joueur.est_ko():
            pokemon_disponibles = [p for p in self.equipe_joueur if not p.est_ko()]
            if pokemon_disponibles:
                self.ajouter_message(f"{self.pokemon_joueur.nom} est K.O.! Choisissez un autre Pokémon!")
                self.zone_pokemon_dispo.show()
                for bouton in self.boutons_attaque:
                    bouton.setEnabled(False)
            else:
                self.ajouter_message("Tous vos Pokémon sont K.O.! Vous avez perdu!")
                self.zone_boutons.hide()
                self.zone_fin_combat.show()

    def recommencer_combat(self):
        # Fermer la fenêtre actuelle
        self.close()
        # Créer une nouvelle fenêtre de combat
        nouvelle_fenetre = CombatGUI()
        nouvelle_fenetre.show()

    def utiliser_attaque(self, attaque):
        # Calcul et application des dégâts
        degats = calcul_degats(self.pokemon_joueur, self.pokemon_adversaire, attaque)
        self.pokemon_adversaire.subir_degats(degats)
        
        # Mise à jour de l'interface
        message_joueur = f"{self.pokemon_joueur.nom} utilise {attaque.nom} et inflige {degats} dégâts!"
        self.ajouter_message(message_joueur)
        self.mettre_a_jour_interface_adversaire()
        
        # Désactiver les boutons pendant le tour de l'adversaire
        for bouton in self.boutons_attaque:
            bouton.setEnabled(False)
        
        # Tour de l'adversaire
        self.tour_adversaire() 
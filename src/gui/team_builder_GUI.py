from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QGridLayout,
    QLabel, QPushButton, QFrame, QListWidget, QListWidgetItem, QDialog, QMessageBox
)
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QPixmap, QIcon, QFont
from src.core.team_builder import TeamBuilder
from src.core.pokemon import POKEMONS_DISPONIBLES, Pokemon
from src.utils.sprite_downloader import normalize_name
from src.gui.theme import get_platform_style
import os

class ConfigAttaquesDialog(QDialog):
    def __init__(self, pokemon, parent=None):
        super().__init__(parent)
        self.pokemon = pokemon
        self.setWindowTitle(f"Configuration de {pokemon.nom}")
        self.setMinimumSize(450, 500)
        self.setStyleSheet(get_platform_style() + """
            QLabel.cadre-attaque {
                background-color: rgba(255, 255, 255, 0.1);
                border: 2px solid #555;
                border-radius: 8px;
                padding: 10px;
                font-weight: bold;
            }
        """)
        
        layout = QVBoxLayout(self)
        layout.setSpacing(15)

        # En-tête
        header = QLabel(f"Attaques de {pokemon.nom}")
        header.setProperty("class", "title")
        header.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(header)

        # Cadres pour les attaques sélectionnées
        self.cadres_attaques = []
        cadre_layout = QGridLayout()
        cadre_layout.setSpacing(10)
        for i in range(4):
            cadre = QLabel("Vide")
            cadre.setProperty("class", "cadre-attaque")
            cadre.setAlignment(Qt.AlignmentFlag.AlignCenter)
            cadre.setMinimumSize(100, 50)
            self.cadres_attaques.append(cadre)
            cadre_layout.addWidget(cadre, i // 2, i % 2)
        layout.addLayout(cadre_layout)

        layout.addWidget(QLabel("<b>Sélectionnez jusqu'à 4 attaques :</b>"))

        # Liste des attaques disponibles
        self.liste_attaques = QListWidget()
        self.liste_attaques.setSelectionMode(QListWidget.SelectionMode.MultiSelection)
        self.liste_attaques.setStyleSheet("font-size: 14px; border-radius: 8px;")
        for attaque in pokemon.attaques_possibles:
            item = QListWidgetItem(attaque)
            self.liste_attaques.addItem(item)
            if attaque in [a.nom for a in pokemon.attaques]:
                item.setSelected(True)
        self.liste_attaques.itemSelectionChanged.connect(self.maj_cadres)
        layout.addWidget(self.liste_attaques)

        # Boutons bas
        boutons = QHBoxLayout()
        btn_suppr = QPushButton("Relâcher le Pokémon")
        btn_suppr.setProperty("class", "custom-button")
        btn_suppr.setObjectName("btn_quitter") # Rouge via le thème
        btn_suppr.clicked.connect(self.supprimer_pokemon)
        
        btn_fermer = QPushButton("Valider")
        btn_fermer.setProperty("class", "custom-button")
        btn_fermer.setObjectName("btn_sauvegarder") # Vert via le thème
        btn_fermer.clicked.connect(self.accept)
        
        boutons.addWidget(btn_suppr)
        boutons.addStretch()
        boutons.addWidget(btn_fermer)
        layout.addLayout(boutons)

        self.maj_cadres()
        self.supprime = False

    def maj_cadres(self):
        attaques = [item.text() for item in self.liste_attaques.selectedItems()][:4]
        for i, cadre in enumerate(self.cadres_attaques):
            if i < len(attaques):
                cadre.setText(attaques[i])
                cadre.setStyleSheet("background-color: #3584e4; color: white; border-color: #1b6acb;")
            else:
                cadre.setText("Vide")
                cadre.setStyleSheet("")

    def accept(self):
        attaques = [item.text() for item in self.liste_attaques.selectedItems()][:4]
        self.pokemon.attaques = []
        for nom in attaques:
            self.pokemon.apprendre_attaque(nom)
        super().accept()

    def supprimer_pokemon(self):
        self.supprime = True
        self.accept()


class TeamBuilderGUI(QWidget):
    def __init__(self, main_window=None):
        super().__init__()
        self.main_window = main_window
        self.team_builder = TeamBuilder()
        self.team_builder.charger_equipe()
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(20)

        # Titre
        titre = QLabel("Gestionnaire d'Équipe")
        titre.setProperty("class", "title")
        titre.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(titre)

        # === ZONE 1 : ÉQUIPE ===
        equipe_label = QLabel("Mon Équipe Actuelle (cliquez pour configurer/retirer)")
        equipe_label.setProperty("class", "subtitle")
        main_layout.addWidget(equipe_label)

        equipe_frame = QFrame()
        equipe_frame.setProperty("class", "custom-frame")
        equipe_layout = QHBoxLayout(equipe_frame)
        equipe_layout.setSpacing(10)
        
        self.equipe_widgets = []
        for i in range(6):
            widget = self.create_pokemon_slot(i)
            equipe_layout.addWidget(widget)
            self.equipe_widgets.append(widget)
        main_layout.addWidget(equipe_frame)

        # === ZONE 2 : BOUTONS DE SAUVEGARDE ===
        boutons_frame = QWidget()
        boutons_layout = QHBoxLayout(boutons_frame)
        boutons_layout.setContentsMargins(0, 0, 0, 0)
        
        self.btn_retour = QPushButton("Retour au Menu")
        self.btn_retour.setProperty("class", "custom-button")
        self.btn_retour.setMinimumHeight(40)
        self.btn_retour.clicked.connect(self.retour_menu)
        
        self.btn_save = QPushButton("Sauvegarder l'équipe")
        self.btn_save.setProperty("class", "custom-button")
        self.btn_save.setObjectName("btn_sauvegarder")
        self.btn_save.setMinimumHeight(40)
        self.btn_save.clicked.connect(self.save_team)
        
        self.btn_delete = QPushButton("Vider l'équipe")
        self.btn_delete.setProperty("class", "custom-button")
        self.btn_delete.setObjectName("btn_quitter")
        self.btn_delete.setMinimumHeight(40)
        self.btn_delete.clicked.connect(self.delete_team)
        
        boutons_layout.addWidget(self.btn_retour)
        boutons_layout.addStretch()
        boutons_layout.addWidget(self.btn_save)
        boutons_layout.addWidget(self.btn_delete)
        main_layout.addWidget(boutons_frame)

        # === ZONE 3 : BOÎTE PC ===
        pc_label = QLabel("Système de Stockage (Boîte PC - double-cliquez pour ajouter)")
        pc_label.setProperty("class", "subtitle")
        main_layout.addWidget(pc_label)

        pc_frame = QFrame()
        pc_frame.setProperty("class", "custom-frame")
        pc_layout = QVBoxLayout(pc_frame)
        
        self.pc_list = QListWidget()
        self.pc_list.setViewMode(QListWidget.ViewMode.IconMode)
        self.pc_list.setIconSize(QSize(64, 64))
        self.pc_list.setResizeMode(QListWidget.ResizeMode.Adjust)
        self.pc_list.setSpacing(10)
        self.pc_list.setStyleSheet("""
            QListWidget { border: none; background: transparent; }
            QListWidget::item { padding: 10px; border-radius: 8px; }
            QListWidget::item:hover { background-color: rgba(53, 132, 228, 0.2); }
            QListWidget::item:selected { background-color: rgba(53, 132, 228, 0.4); color: inherit; }
        """)
        
        for nom in POKEMONS_DISPONIBLES:
            item = QListWidgetItem(nom)
            normalized = normalize_name(nom)
            sprite_path = f"src/assets/sprites/{normalized}.png"
            if os.path.exists(sprite_path):
                item.setIcon(QIcon(QPixmap(sprite_path)))
            # Centrer le texte sous l'icône
            item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            self.pc_list.addItem(item)
            
        self.pc_list.itemDoubleClicked.connect(self.add_pokemon_from_pc)
        pc_layout.addWidget(self.pc_list)
        main_layout.addWidget(pc_frame, stretch=1)

        self.maj_affichage()

    def create_pokemon_slot(self, index):
        frame = QFrame()
        frame.setStyleSheet("""
            QFrame {
                background-color: rgba(0,0,0,0.05);
                border: 2px dashed #999;
                border-radius: 8px;
            }
            QFrame:hover {
                border-color: #3584e4;
                background-color: rgba(53, 132, 228, 0.1);
            }
        """)
        frame.setCursor(Qt.CursorShape.PointingHandCursor)
        layout = QVBoxLayout(frame)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.sprite = QLabel()
        self.sprite.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.sprite.setFixedSize(80, 80)
        self.sprite.setStyleSheet("border: none; background: transparent;")
        
        self.nom = QLabel("Vide")
        self.nom.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.nom.setFont(QFont("Arial", 11, QFont.Weight.Bold))
        self.nom.setStyleSheet("border: none; background: transparent;")
        
        layout.addWidget(self.sprite)
        layout.addWidget(self.nom)
        
        # On rend tout le frame cliquable
        frame.mousePressEvent = lambda event, idx=index: self.config_pokemon(idx) if event.button() == Qt.MouseButton.LeftButton else None
        return frame

    def maj_affichage(self):
        for i, widget in enumerate(self.equipe_widgets):
            layout = widget.layout()
            sprite_label = layout.itemAt(0).widget()
            nom_label = layout.itemAt(1).widget()
            
            if i < len(self.team_builder.equipe):
                pokemon = self.team_builder.equipe[i]
                normalized = normalize_name(pokemon.nom)
                sprite_path = f"src/assets/sprites/{normalized}.png"
                
                if os.path.exists(sprite_path):
                    pixmap = QPixmap(sprite_path)
                    # Mise à l'échelle sans lissage
                    pixmap = pixmap.scaled(80, 80, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.FastTransformation)
                    sprite_label.setPixmap(pixmap)
                else:
                    sprite_label.setText("?")
                    
                nom_label.setText(pokemon.nom)
                widget.setStyleSheet("""
                    QFrame {
                        background-color: rgba(53, 132, 228, 0.1);
                        border: 2px solid #3584e4;
                        border-radius: 8px;
                    }
                    QFrame:hover { background-color: rgba(53, 132, 228, 0.2); }
                """)
            else:
                sprite_label.clear()
                nom_label.setText("Vide")
                widget.setStyleSheet("""
                    QFrame {
                        background-color: rgba(0,0,0,0.05);
                        border: 2px dashed #999;
                        border-radius: 8px;
                    }
                    QFrame:hover { border-color: #3584e4; }
                """)

    def config_pokemon(self, index):
        if index >= len(self.team_builder.equipe):
            return
        pokemon = self.team_builder.equipe[index]
        dialog = ConfigAttaquesDialog(pokemon, self)
        if dialog.exec():
            if dialog.supprime:
                self.team_builder.equipe.pop(index)
            self.maj_affichage()

    def add_pokemon_from_pc(self, item):
        if len(self.team_builder.equipe) >= 6:
            QMessageBox.warning(self, "Erreur", "L'équipe est déjà complète (6 Pokémon max)")
            return
        nom = item.text()
        if nom in [p.nom for p in self.team_builder.equipe]:
            QMessageBox.warning(self, "Erreur", f"{nom} est déjà dans l'équipe")
            return
        self.team_builder.ajouter_pokemon(nom)
        self.maj_affichage()

    def save_team(self):
        success, message = self.team_builder.sauvegarder_equipe()
        if success:
            QMessageBox.information(self, "Succès", message)
        else:
            QMessageBox.warning(self, "Erreur", message)

    def delete_team(self):
        reponse = QMessageBox.question(self, "Confirmation", "Vider toute l'équipe ?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if reponse == QMessageBox.StandardButton.Yes:
            self.team_builder.equipe.clear()
            self.maj_affichage()

    def retour_menu(self):
        if self.main_window:
            self.main_window.show_menu()
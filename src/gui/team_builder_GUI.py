from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QPixmap, QIcon
from src.core.team_builder import TeamBuilder
from src.core.pokemon import POKEMONS_DISPONIBLES, Pokemon
import os

class ConfigAttaquesDialog(QDialog):
    def __init__(self, pokemon, parent=None):
        super().__init__(parent)
        self.pokemon = pokemon
        self.setWindowTitle(f"Configuration de {pokemon.nom}")
        self.setMinimumSize(400, 400)
        layout = QVBoxLayout(self)

        # Cadres pour les attaques sélectionnées
        self.cadres_attaques = []
        cadre_layout = QHBoxLayout()
        for i in range(4):
            cadre = QLabel("Vide")
            cadre.setFrameShape(QFrame.Shape.Box)
            cadre.setAlignment(Qt.AlignmentFlag.AlignCenter)
            cadre.setMinimumSize(80, 40)
            self.cadres_attaques.append(cadre)
            cadre_layout.addWidget(cadre)
        layout.addLayout(cadre_layout)

        # Liste des attaques disponibles
        self.liste_attaques = QListWidget()
        self.liste_attaques.setSelectionMode(QListWidget.SelectionMode.MultiSelection)
        for attaque in pokemon.attaques_possibles:
            item = QListWidgetItem(attaque)
            self.liste_attaques.addItem(item)
            if attaque in [a.nom for a in pokemon.attaques]:
                item.setSelected(True)
        self.liste_attaques.itemSelectionChanged.connect(self.maj_cadres)
        layout.addWidget(self.liste_attaques)

        # Boutons bas
        boutons = QHBoxLayout()
        btn_suppr = QPushButton("Supprimer le Pokémon")
        btn_suppr.setStyleSheet("background-color: #dc3545; color: white;")
        btn_suppr.clicked.connect(self.supprimer_pokemon)
        boutons.addWidget(btn_suppr, alignment=Qt.AlignmentFlag.AlignLeft)
        boutons.addStretch()
        btn_fermer = QPushButton("Fermer")
        btn_fermer.clicked.connect(self.accept)
        boutons.addWidget(btn_fermer, alignment=Qt.AlignmentFlag.AlignRight)
        layout.addLayout(boutons)

        self.maj_cadres()
        self.supprime = False

    def maj_cadres(self):
        attaques = [item.text() for item in self.liste_attaques.selectedItems()][:4]
        for i, cadre in enumerate(self.cadres_attaques):
            if i < len(attaques):
                cadre.setText(attaques[i])
            else:
                cadre.setText("Vide")

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
    def __init__(self, parent=None):
        super().__init__(parent)
        self.team_builder = TeamBuilder()
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout(self)
        # === ZONE 1 : ÉQUIPE ===
        equipe_frame = QFrame()
        equipe_layout = QHBoxLayout(equipe_frame)
        self.equipe_widgets = []
        for i in range(6):
            widget = self.create_pokemon_slot(i)
            equipe_layout.addWidget(widget)
            self.equipe_widgets.append(widget)
        main_layout.addWidget(equipe_frame)

        # === ZONE 2 : BOUTONS ===
        boutons_frame = QFrame()
        boutons_layout = QHBoxLayout(boutons_frame)
        self.btn_save = QPushButton("Sauvegarder l'équipe")
        self.btn_save.setStyleSheet("background-color: #43b581; color: white;")
        self.btn_save.clicked.connect(self.save_team)
        self.btn_delete = QPushButton("Supprimer l'équipe")
        self.btn_delete.setStyleSheet("background-color: #dc3545; color: white;")
        self.btn_delete.clicked.connect(self.delete_team)
        boutons_layout.addWidget(self.btn_save, alignment=Qt.AlignmentFlag.AlignLeft)
        boutons_layout.addStretch()
        boutons_layout.addWidget(self.btn_delete, alignment=Qt.AlignmentFlag.AlignRight)
        main_layout.addWidget(boutons_frame)

        # === ZONE 3 : BOÎTE PC ===
        pc_frame = QFrame()
        pc_layout = QHBoxLayout(pc_frame)
        self.pc_list = QListWidget()
        self.pc_list.setViewMode(QListWidget.ViewMode.IconMode)
        self.pc_list.setIconSize(QSize(48, 48))
        self.pc_list.setResizeMode(QListWidget.ResizeMode.Adjust)
        self.pc_list.setSpacing(8)
        for nom in POKEMONS_DISPONIBLES:
            item = QListWidgetItem(nom)
            sprite_path = f"src/assets/sprites/{nom.lower()}.png"
            if os.path.exists(sprite_path):
                item.setIcon(QIcon(QPixmap(sprite_path)))
            self.pc_list.addItem(item)
        self.pc_list.itemDoubleClicked.connect(self.add_pokemon_from_pc)
        pc_layout.addWidget(self.pc_list)
        main_layout.addWidget(pc_frame)

        self.maj_affichage()

    def create_pokemon_slot(self, index):
        frame = QFrame()
        layout = QVBoxLayout(frame)
        self.sprite = QLabel()
        self.sprite.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.sprite.setFixedSize(64, 64)
        self.nom = QLabel("Vide")
        self.nom.setAlignment(Qt.AlignmentFlag.AlignCenter)
        btn = QPushButton()
        btn.setFlat(True)
        btn.setStyleSheet("background: transparent;")
        btn.clicked.connect(lambda _, idx=index: self.config_pokemon(idx))
        layout.addWidget(self.sprite)
        layout.addWidget(self.nom)
        layout.addWidget(btn)
        frame.setLayout(layout)
        frame.mousePressEvent = lambda event, idx=index: self.config_pokemon(idx) if event.button() == Qt.MouseButton.LeftButton else None
        return frame

    def maj_affichage(self):
        for i, widget in enumerate(self.equipe_widgets):
            layout = widget.layout()
            sprite_label = layout.itemAt(0).widget()
            nom_label = layout.itemAt(1).widget()
            if i < len(self.team_builder.equipe):
                pokemon = self.team_builder.equipe[i]
                sprite_path = f"src/assets/sprites/{pokemon.nom.lower()}.png"
                if os.path.exists(sprite_path):
                    sprite_label.setPixmap(QPixmap(sprite_path).scaled(64, 64, Qt.AspectRatioMode.KeepAspectRatio))
                else:
                    sprite_label.clear()
                nom_label.setText(pokemon.nom)
            else:
                sprite_label.clear()
                nom_label.setText("Vide")

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
        reponse = QMessageBox.question(self, "Confirmation", "Supprimer toute l'équipe ?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if reponse == QMessageBox.StandardButton.Yes:
            self.team_builder.equipe.clear()
            self.maj_affichage() 
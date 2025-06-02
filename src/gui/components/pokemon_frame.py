from PyQt6.QtWidgets import QFrame, QVBoxLayout, QLabel
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from pathlib import Path

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
            # Import ici pour éviter l'import circulaire
            from ...gui.team_builder import TeamBuilderGUI
            
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
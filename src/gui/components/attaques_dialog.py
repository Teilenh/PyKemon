from PyQt6.QtWidgets import (
    QDialog, QVBoxLayout, QLabel, QPushButton,
    QListWidget, QDialogButtonBox, QGridLayout,
    QWidget, QMessageBox
)
from PyQt6.QtCore import Qt

class ConfigurationAttaquesDialog(QDialog):
    def __init__(self, pokemon, parent=None):
        super().__init__(parent)
        self.pokemon = pokemon
        self.setWindowTitle(f"Configuration des attaques - {pokemon.nom}")
        self.setMinimumSize(400, 400)
        
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
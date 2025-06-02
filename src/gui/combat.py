from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton, QFrame, QGridLayout
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QPixmap
from pathlib import Path
from random import choice

from src.core.pokemon import creer_pokemon
from src.core.combat import calcul_degats
from src.core.team_builder import TeamBuilder
from src.core.adversaire import Adversaire
from src.utils.sprite_downloader import normalize_name
from src.gui.components.common import BoutonAttaque, BarreVie
from src.gui.theme import get_platform_style

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

        ancien_pokemon = self.pokemon_joueur
        self.pokemon_joueur = nouveau_pokemon
        self.mettre_a_jour_interface()
        self.zone_pokemon_dispo.hide()

        # Tour de l'adversaire seulement si le changement n'est pas dû à un KO
        if not ancien_pokemon.est_ko():
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
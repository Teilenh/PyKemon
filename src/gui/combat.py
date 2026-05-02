from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton, QFrame, QGridLayout, QSizePolicy
)
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QFont, QPixmap, QIcon
from pathlib import Path
from random import choice

from src.core.pokemon import creer_pokemon
from src.core.combat import calcul_degats
from src.core.team_builder import TeamBuilder
from src.core.adversaire import Adversaire
from src.utils.sprite_downloader import normalize_name
from src.gui.components.common import BoutonAttaque, BarreVie
from src.gui.theme import get_platform_style

class AreneCombat(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("zone_combat")
        self.setStyleSheet("""
            #zone_combat {
                border-image: url('Assets/battle_bg.png') 0 0 0 0 stretch stretch;
                border-radius: 12px;
                border: 2px solid #333;
            }
        """)
        
        self.sprite_adversaire = QLabel(self)
        self.sprite_adversaire.setFixedSize(200, 200)
        self.sprite_adversaire.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.sprite_adversaire.setStyleSheet("background: transparent;")
        
        self.sprite_joueur = QLabel(self)
        self.sprite_joueur.setFixedSize(200, 200)
        self.sprite_joueur.setAlignment(Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignCenter)
        self.sprite_joueur.setStyleSheet("background: transparent;")

    def resizeEvent(self, event):
        super().resizeEvent(event)
        w = self.width()
        h = self.height()
        sw, sh = 200, 200
        
        # Plateforme adverse (droite)
        self.sprite_adversaire.setGeometry(int(w * 0.75 - sw/2), int(h * 0.55 - sh/2), sw, sh)
        
        # Plateforme joueur (gauche)
        self.sprite_joueur.setGeometry(int(w * 0.25 - sw/2), int(h * 0.80 - sh), sw, sh)


class CombatGUI(QWidget):
    def __init__(self, main_window=None):
        super().__init__()
        self.main_window = main_window
        
        # Style de base GTK + Surcharges Pokémon
        style = get_platform_style() + """
            QFrame#zone_combat {
                background-color: #d1e8d6; /* Vert Gameboy clair */
                border: 3px solid #4a4a4a;
                border-radius: 8px;
            }
            QFrame#historique {
                background-color: #242424;
                color: #ffffff;
                border-radius: 6px;
                padding: 10px;
                font-family: monospace;
                border: 2px solid #5865f2;
                font-size: 14px;
            }
            QLabel#trainer_sprite {
                font-size: 72px;
            }
            QFrame#team_zone, QFrame#trainer_zone {
                background-color: rgba(255, 255, 255, 0.05);
            }
            QPushButton.type-plante { background-color: #78C850; color: white; border: 1px solid #4A892B; }
            QPushButton.type-feu { background-color: #F08030; color: white; border: 1px solid #A1551D; }
            QPushButton.type-eau { background-color: #6890F0; color: white; border: 1px solid #415A96; }
            QPushButton.type-electrique { background-color: #F8D030; color: black; border: 1px solid #A1871F; }
            QPushButton.type-normal { background-color: #A8A878; color: white; border: 1px solid #6D6D4E; }
            QPushButton.type-vol { background-color: #A890F0; color: white; border: 1px solid #6D5E9C; }
            QPushButton.type-poison { background-color: #A040A0; color: white; border: 1px solid #682A68; }
            QPushButton.type-sol { background-color: #E0C068; color: white; border: 1px solid #927D44; }
            QPushButton.type-combat { background-color: #C03028; color: white; border: 1px solid #7D1F1A; }
            QPushButton.type-insecte { background-color: #A8B820; color: white; border: 1px solid #6D7815; }
            QPushButton.type-roche { background-color: #B8A038; color: white; border: 1px solid #786824; }
            QPushButton.type-spectre { background-color: #705898; color: white; border: 1px solid #493963; }
            QPushButton.type-dragon { background-color: #7038F8; color: white; border: 1px solid #4924A1; }
            QPushButton.type-psy { background-color: #F85888; color: white; border: 1px solid #A13959; }
            QPushButton.type-glace { background-color: #98D8D8; color: black; border: 1px solid #638D8D; }
        """
        self.setStyleSheet(style)

        # Initialisation du jeu
        self.team_builder = TeamBuilder()
        success, message = self.team_builder.charger_equipe()
        
        if success and self.team_builder.equipe:
            self.equipe_joueur = self.team_builder.equipe
            self.pokemon_joueur = self.equipe_joueur[0]
        else:
            self.pokemon_joueur = creer_pokemon("Pikachu")
            self.equipe_joueur = [self.pokemon_joueur]
            
        self.adversaire = Adversaire(4)
        self.pokemon_adversaire = self.adversaire.pokemon_actif
        
        if not self.pokemon_adversaire:
            self.pokemon_adversaire = creer_pokemon("Carapuce")

        if not self.pokemon_joueur.attaques:
            for attaque in self.pokemon_joueur.attaques_possibles[:4]:
                self.pokemon_joueur.apprendre_attaque(attaque)
        if not self.pokemon_adversaire.attaques:
            for attaque in self.pokemon_adversaire.attaques_possibles[:4]:
                self.pokemon_adversaire.apprendre_attaque(attaque)

        self.messages = []
        self.initialiser_interface()
        self.mettre_a_jour_interface()
        self.mettre_a_jour_interface_adversaire()
        self.ajouter_message("Un dresseur veut se battre !")

    def initialiser_interface(self):
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(15, 15, 15, 15)
        main_layout.setSpacing(15)

        # ==========================================
        # MOITIÉ HAUTE : ZONE DE COMBAT (1/5 - 3/5 - 1/5)
        # ==========================================
        top_half = QWidget()
        top_layout = QHBoxLayout(top_half)
        top_layout.setContentsMargins(0, 0, 0, 0)
        top_layout.setSpacing(10)
        
        # --- GAUCHE (1/5) : Mon Équipe ---
        left_zone = QFrame()
        left_zone.setObjectName("team_zone")
        left_zone.setProperty("class", "custom-frame")
        left_layout = QVBoxLayout(left_zone)
        left_layout.addWidget(QLabel("<b>Mon Équipe</b>"), alignment=Qt.AlignmentFlag.AlignCenter)
        
        self.equipe_sprites_labels = []
        team_grid = QGridLayout()
        team_grid.setSpacing(5)
        for i in range(6):
            lbl = QLabel()
            lbl.setFixedSize(48, 48)
            lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
            lbl.setStyleSheet("background-color: rgba(0,0,0,0.1); border-radius: 24px;")
            # Zig-zag simple
            row = i % 3
            col = i // 3
            if col == 1:
                team_grid.addWidget(lbl, row, col, Qt.AlignmentFlag.AlignBottom)
            else:
                team_grid.addWidget(lbl, row, col, Qt.AlignmentFlag.AlignTop)
                
            self.equipe_sprites_labels.append(lbl)
            
        left_layout.addLayout(team_grid)
        left_layout.addStretch()
        top_layout.addWidget(left_zone, stretch=1)

        # --- CENTRE (3/5) : L'Arène ---
        self.center_zone = AreneCombat()
        self.sprite_adversaire = self.center_zone.sprite_adversaire
        self.sprite_joueur = self.center_zone.sprite_joueur
        
        center_layout = QVBoxLayout(self.center_zone)
        center_layout.setContentsMargins(20, 20, 20, 20)
        
        # Infos Ennemi
        ennemi_layout = QHBoxLayout()
        
        self.zone_info_adversaire = QFrame()
        self.zone_info_adversaire.setProperty("class", "custom-frame")
        self.zone_info_adversaire.setFixedWidth(220)
        self.zone_info_adversaire.setStyleSheet("background-color: rgba(255,255,255,0.8); color: black;")
        info_adv_layout = QVBoxLayout(self.zone_info_adversaire)
        
        self.label_nom_adversaire = QLabel()
        self.label_nom_adversaire.setFont(QFont("Arial", 14, QFont.Weight.Bold))
        self.barre_vie_adversaire = BarreVie()
        self.label_pv_adversaire = QLabel()
        self.label_stats_adversaire = QLabel("")
        self.label_stats_adversaire.setTextFormat(Qt.TextFormat.RichText)
        
        info_adv_layout.addWidget(self.label_nom_adversaire)
        info_adv_layout.addWidget(self.barre_vie_adversaire)
        info_adv_layout.addWidget(self.label_pv_adversaire)
        info_adv_layout.addWidget(self.label_stats_adversaire)
        
        ennemi_layout.addWidget(self.zone_info_adversaire, alignment=Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)
        ennemi_layout.addStretch()
        
        center_layout.addLayout(ennemi_layout)
        center_layout.addStretch()
        
        # Infos Joueur
        joueur_layout = QHBoxLayout()
        joueur_layout.addStretch()
        
        self.zone_info_joueur = QFrame()
        self.zone_info_joueur.setProperty("class", "custom-frame")
        self.zone_info_joueur.setFixedWidth(220)
        self.zone_info_joueur.setStyleSheet("background-color: rgba(255,255,255,0.8); color: black;")
        info_joueur_layout = QVBoxLayout(self.zone_info_joueur)
        
        self.label_nom_joueur = QLabel()
        self.label_nom_joueur.setFont(QFont("Arial", 14, QFont.Weight.Bold))
        self.barre_vie_joueur = BarreVie()
        self.label_pv_joueur = QLabel()
        self.label_stats_joueur = QLabel("")
        self.label_stats_joueur.setTextFormat(Qt.TextFormat.RichText)
        
        info_joueur_layout.addWidget(self.label_nom_joueur)
        info_joueur_layout.addWidget(self.barre_vie_joueur)
        info_joueur_layout.addWidget(self.label_pv_joueur)
        info_joueur_layout.addWidget(self.label_stats_joueur)
        
        joueur_layout.addWidget(self.zone_info_joueur, alignment=Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignRight)
        
        center_layout.addLayout(joueur_layout)
        
        top_layout.addWidget(self.center_zone, stretch=3)

        # --- DROITE (1/5) : Dresseur Adverse ---
        right_zone = QFrame()
        right_zone.setObjectName("trainer_zone")
        right_zone.setProperty("class", "custom-frame")
        right_layout = QVBoxLayout(right_zone)
        right_layout.addWidget(QLabel("<b>Adversaire</b>"), alignment=Qt.AlignmentFlag.AlignCenter)
        
        self.label_pokemons_restants = QLabel()
        self.label_pokemons_restants.setAlignment(Qt.AlignmentFlag.AlignCenter)
        right_layout.addWidget(self.label_pokemons_restants)
        
        sprite_dresseur = QLabel("🥷") # Ninja/Dresseur
        sprite_dresseur.setObjectName("trainer_sprite")
        sprite_dresseur.setAlignment(Qt.AlignmentFlag.AlignCenter)
        right_layout.addWidget(sprite_dresseur)
        
        right_layout.addStretch()
        top_layout.addWidget(right_zone, stretch=1)
        
        main_layout.addWidget(top_half, stretch=3)

        # ==========================================
        # MOITIÉ BASSE : ACTIONS ET HISTORIQUE
        # ==========================================
        bottom_half = QWidget()
        bottom_layout = QVBoxLayout(bottom_half)
        bottom_layout.setContentsMargins(0, 0, 0, 0)
        bottom_layout.setSpacing(15)
        
        # --- Attaques ---
        self.zone_attaques = QWidget()
        layout_attaques = QGridLayout(self.zone_attaques)
        layout_attaques.setSpacing(10)
        self.boutons_attaque = []
        for i in range(4):
            btn = QPushButton("Attaque")
            btn.setProperty("class", "custom-button")
            btn.setMinimumHeight(60)
            btn.setFont(QFont("Arial", 12, QFont.Weight.Bold))
            layout_attaques.addWidget(btn, i//2, i%2)
            self.boutons_attaque.append(btn)
        bottom_layout.addWidget(self.zone_attaques)
        
        # --- Changement de Pokémon ---
        self.zone_switch = QWidget()
        layout_switch = QHBoxLayout(self.zone_switch)
        layout_switch.setSpacing(10)
        self.boutons_pokemon = []
        for i in range(6):
            btn = QPushButton()
            btn.setProperty("class", "custom-button")
            btn.setMinimumHeight(70)
            layout_switch.addWidget(btn)
            self.boutons_pokemon.append(btn)
        bottom_layout.addWidget(self.zone_switch)
        
        # --- Historique ---
        self.historique_messages = QLabel()
        self.historique_messages.setObjectName("historique")
        self.historique_messages.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
        self.historique_messages.setMinimumHeight(100)
        bottom_layout.addWidget(self.historique_messages, stretch=1)

        main_layout.addWidget(bottom_half, stretch=2)

        # --- Écran de fin ---
        self.zone_fin_combat = QWidget()
        layout_fin = QHBoxLayout(self.zone_fin_combat)
        btn_recommencer = QPushButton("Recommencer")
        btn_recommencer.setProperty("class", "custom-button")
        btn_recommencer.clicked.connect(self.recommencer_combat)
        btn_quitter = QPushButton("Retour au Menu")
        btn_quitter.setProperty("class", "custom-button")
        btn_quitter.clicked.connect(self.quitter)
        layout_fin.addWidget(btn_recommencer)
        layout_fin.addWidget(btn_quitter)
        self.zone_fin_combat.hide()
        main_layout.addWidget(self.zone_fin_combat)

    def mettre_a_jour_sprite(self, pokemon, est_joueur):
        normalized_name = normalize_name(pokemon.nom)
        sprite_filename = f"{normalized_name}_back.png" if est_joueur else f"{normalized_name}.png"
        sprite_path = Path("src/assets/sprites") / sprite_filename
        
        label = self.sprite_joueur if est_joueur else self.sprite_adversaire
        if sprite_path.exists():
            pixmap = QPixmap(str(sprite_path))
            pixmap = pixmap.scaled(200, 200, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.FastTransformation)
            label.setPixmap(pixmap)
        else:
            label.setText("[ ? ]")
            label.setStyleSheet("font-size: 32px; color: gray;")

    def format_type_class(self, p_type):
        return f"custom-button type-{p_type.lower()}"

    def format_stat_stages(self, stat_stages):
        mapping = {"attaque": "Atk", "defense": "Def", "special": "Spé", "vitesse": "Vit"}
        res = []
        for k, v in stat_stages.items():
            if v == 0:
                continue
            if v > 0:
                mult = (v + 2) / 2
                res.append(f"<b>{mapping[k]}</b> <span style='color:green;'>x{mult:g}</span>")
            elif v < 0:
                mult = 2 / (abs(v) + 2)
                res.append(f"<b>{mapping[k]}</b> <span style='color:red;'>x{mult:.2f}</span>")
        return " | ".join(res)

    def mettre_a_jour_interface(self):
        # Stats joueur
        status_txt = f" [{self.pokemon_joueur.statut}]" if self.pokemon_joueur.statut else ""
        self.label_nom_joueur.setText(f"{self.pokemon_joueur.nom}{status_txt}")
        self.label_pv_joueur.setText(f"{self.pokemon_joueur.pv} / {self.pokemon_joueur.pv_max} PV")
        self.barre_vie_joueur.setValue((self.pokemon_joueur.pv / self.pokemon_joueur.pv_max) * 100)
        self.label_stats_joueur.setText(self.format_stat_stages(self.pokemon_joueur.stat_stages))
        self.mettre_a_jour_sprite(self.pokemon_joueur, True)

        # Attaques
        for i, btn in enumerate(self.boutons_attaque):
            try: btn.clicked.disconnect() 
            except: pass
            
            if i < len(self.pokemon_joueur.attaques):
                atk = self.pokemon_joueur.attaques[i]
                btn.setText(f"{atk.nom}  [{atk.type}]\nPuissance: {atk.puissance}")
                btn.setProperty("class", self.format_type_class(atk.type))
                
                btn.style().unpolish(btn)
                btn.style().polish(btn)
                
                btn.clicked.connect(lambda checked, a=atk: self.utiliser_attaque(a))
                
                if self.pokemon_joueur.est_ko():
                    btn.setEnabled(False)
                else:
                    btn.setEnabled(True)
                btn.show()
            else:
                btn.hide()

        # Équipe Switch
        for i, btn in enumerate(self.boutons_pokemon):
            try: btn.clicked.disconnect() 
            except: pass
            
            if i < len(self.equipe_joueur):
                pkmn = self.equipe_joueur[i]
                normalized = normalize_name(pkmn.nom)
                sprite_path = f"src/assets/sprites/{normalized}.png"
                
                icon = QIcon(sprite_path) if Path(sprite_path).exists() else QIcon()
                btn.setIcon(icon)
                btn.setIconSize(QSize(48, 48))
                btn.setText(f"{pkmn.nom}\n{pkmn.type}")
                
                lbl = self.equipe_sprites_labels[i]
                if Path(sprite_path).exists():
                    pix = QPixmap(sprite_path).scaled(48, 48, Qt.AspectRatioMode.KeepAspectRatio)
                    lbl.setPixmap(pix)
                
                if pkmn.est_ko():
                    btn.setEnabled(False)
                    btn.setProperty("class", "custom-button")
                    btn.setStyleSheet("background-color: #333333; color: #888888; border: 1px solid #222;")
                    lbl.setStyleSheet("opacity: 0.2;")
                else:
                    btn.setEnabled(True)
                    btn.setProperty("class", self.format_type_class(pkmn.type))
                    btn.setStyleSheet("")
                    lbl.setStyleSheet("")
                    btn.clicked.connect(lambda checked, p=pkmn: self.changer_pokemon(p))
                
                btn.style().unpolish(btn)
                btn.style().polish(btn)
                btn.show()
            else:
                btn.hide()
                self.equipe_sprites_labels[i].clear()

    def mettre_a_jour_interface_adversaire(self):
        if self.pokemon_adversaire:
            status_txt = f" [{self.pokemon_adversaire.statut}]" if self.pokemon_adversaire.statut else ""
            self.label_nom_adversaire.setText(f"{self.pokemon_adversaire.nom} N.{getattr(self.pokemon_adversaire, 'niveau', 50)}{status_txt}")
            self.label_pv_adversaire.setText(f"{self.pokemon_adversaire.pv} / {self.pokemon_adversaire.pv_max} PV")
            self.barre_vie_adversaire.setValue((self.pokemon_adversaire.pv / self.pokemon_adversaire.pv_max) * 100)
            self.label_stats_adversaire.setText(self.format_stat_stages(self.pokemon_adversaire.stat_stages))
            self.mettre_a_jour_sprite(self.pokemon_adversaire, False)
        
        restants = sum(1 for p in self.adversaire.equipe if not p.est_ko())
        self.label_pokemons_restants.setText(f"Pokémon restants: {restants}")

    def ajouter_message(self, message):
        self.messages.append(f"▶ {message}")
        if len(self.messages) > 4:
            self.messages.pop(0)
        self.historique_messages.setText("\n".join(self.messages))

    def changer_pokemon(self, nouveau_pokemon):
        if nouveau_pokemon == self.pokemon_joueur:
            return
            
        ancien_pokemon = self.pokemon_joueur
        ancien_pokemon.reset_stats()
        self.pokemon_joueur = nouveau_pokemon
        self.ajouter_message(f"Reviens {ancien_pokemon.nom} ! En avant {nouveau_pokemon.nom} !")
        self.mettre_a_jour_interface()

        if not ancien_pokemon.est_ko():
            self.tour_adversaire()

    def handle_status_move(self, attaque, lanceur, cible, is_joueur):
        stat_effects = {
            "Danse Lames": ("attaque", 2, "self"), "Aiguisage": ("attaque", 1, "self"),
            "Groz'Yeux": ("defense", -1, "target"), "Mimi-Queue": ("defense", -1, "target"),
            "Rugissement": ("attaque", -1, "target"), "Rugissement": ("attaque", -1, "target"),
            "Amnésie": ("special", 2, "self"), "Croissance": ("special", 1, "self"),
            "Hâte": ("vitesse", 2, "self"),
            "Repli": ("defense", 1, "self"), "Armure": ("defense", 1, "self"), "Boul'Armure": ("defense", 1, "self"),
            "Sécrétion": ("vitesse", -1, "target"), "Grincement": ("defense", -2, "target"),
            "Reflet": ("esquive", 1, "self"), "Jet de Sable": ("precision", -1, "target"),
            "Toxik": ("precision", 0, "target") # Toxik can be handled as PSN status
        }
        
        status_effects = {
            "Cage Éclair": "PAR", "Para-Spore": "PAR",
            "Poudre Toxik": "PSN", "Toxik": "PSN", "Gaz Toxik": "PSN",
            "Feu Follet": "BRU",
            "Poudre Dodo": "SOM", "Berceuse": "SOM", "Spore": "SOM", "Hypnose": "SOM",
            "Poudreuse": "GEL"
        }
        
        if attaque.nom in stat_effects:
            stat_name, amount, target = stat_effects[attaque.nom]
            target_poke = lanceur if target == "self" else cible
            if stat_name in ["esquive", "precision"]:
                self.ajouter_message(f"La {stat_name} de {target_poke.nom} {'augmente' if amount>0 else 'baisse'} !")
                return True
            
            if target_poke.modify_stat(stat_name, amount):
                action = "augmente beaucoup" if amount > 1 else "augmente" if amount > 0 else "baisse beaucoup" if amount < -1 else "baisse"
                self.ajouter_message(f"La {stat_name} de {target_poke.nom} {action} !")
            else:
                self.ajouter_message(f"La {stat_name} de {target_poke.nom} ne peut plus {'augmenter' if amount>0 else 'baisser'} !")
            return True
            
        elif attaque.nom in status_effects:
            new_status = status_effects[attaque.nom]
            if cible.statut is None:
                cible.statut = new_status
                if new_status == "PAR": msg = f"{cible.nom} est paralysé ! Il peut ne pas attaquer !"
                elif new_status == "SOM": msg = f"{cible.nom} s'endort profondément !"
                elif new_status == "PSN": msg = f"{cible.nom} est empoisonné !"
                elif new_status == "BRU": msg = f"{cible.nom} est brûlé !"
                elif new_status == "GEL": msg = f"{cible.nom} est complètement gelé !"
                else: msg = f"{cible.nom} souffre du statut {new_status} !"
                self.ajouter_message(msg)
            else:
                self.ajouter_message(f"{cible.nom} est déjà affecté par un statut !")
            return True
        else:
            self.ajouter_message(f"Mais cela n'a aucun effet...")
            return False

    def handle_pre_attack_status(self, pokemon):
        if pokemon.statut == "PAR":
            import random
            if random.random() < 0.25:
                self.ajouter_message(f"{pokemon.nom} est paralysé ! Il ne peut pas attaquer !")
                return False
        elif pokemon.statut == "SOM":
            import random
            if random.random() < 0.33:
                pokemon.statut = None
                self.ajouter_message(f"{pokemon.nom} se réveille !")
                return True
            self.ajouter_message(f"{pokemon.nom} dort profondément...")
            return False
        elif pokemon.statut == "GEL":
            self.ajouter_message(f"{pokemon.nom} est gelé ! Il ne peut pas bouger !")
            return False
        return True

    def handle_post_attack_status(self, pokemon):
        if pokemon.statut in ["PSN", "BRU"]:
            degats = max(1, pokemon.pv_max // 16)
            pokemon.subir_degats(degats)
            self.ajouter_message(f"{pokemon.nom} souffre de son statut... ({degats} dégâts)")

    def utiliser_attaque(self, attaque):
        if self.handle_pre_attack_status(self.pokemon_joueur):
            self.ajouter_message(f"{self.pokemon_joueur.nom} lance {attaque.nom} !")
            if attaque.puissance == 0:
                self.handle_status_move(attaque, self.pokemon_joueur, self.pokemon_adversaire, True)
            else:
                degats = calcul_degats(self.pokemon_joueur, self.pokemon_adversaire, attaque)
                self.pokemon_adversaire.subir_degats(degats)
                self.ajouter_message(f"Ça inflige {degats} dégâts !")
        
        self.handle_post_attack_status(self.pokemon_joueur)
        self.mettre_a_jour_interface_adversaire()
        self.mettre_a_jour_interface()
        
        for btn in self.boutons_attaque:
            btn.setEnabled(False)
            
        if not self.pokemon_joueur.est_ko():
            self.tour_adversaire()
        elif self.pokemon_adversaire.est_ko():
            self.tour_adversaire() # Force next poke selection

    def tour_adversaire(self):
        if self.pokemon_adversaire.est_ko():
            self.ajouter_message(f"Le {self.pokemon_adversaire.nom} ennemi est K.O. !")
            nouveau_pokemon = self.adversaire.choisir_pokemon()
            if nouveau_pokemon:
                self.pokemon_adversaire = nouveau_pokemon
                self.ajouter_message(f"Le dresseur envoie {self.pokemon_adversaire.nom} !")
                self.mettre_a_jour_interface_adversaire()
                for btn in self.boutons_attaque:
                    btn.setEnabled(True)
                return
            else:
                self.ajouter_message("Vous avez vaincu le dresseur !")
                self.zone_attaques.hide()
                self.zone_switch.hide()
                self.zone_fin_combat.show()
                return

        if self.handle_pre_attack_status(self.pokemon_adversaire):
            attaque_adversaire = choice(self.pokemon_adversaire.attaques)
            self.ajouter_message(f"Le {self.pokemon_adversaire.nom} ennemi lance {attaque_adversaire.nom} !")

            if attaque_adversaire.puissance == 0:
                self.handle_status_move(attaque_adversaire, self.pokemon_adversaire, self.pokemon_joueur, False)
            else:
                degats_adversaire = calcul_degats(self.pokemon_adversaire, self.pokemon_joueur, attaque_adversaire)
                self.pokemon_joueur.subir_degats(degats_adversaire)
                self.ajouter_message(f"Ça inflige {degats_adversaire} dégâts !")

        self.handle_post_attack_status(self.pokemon_adversaire)
        self.mettre_a_jour_interface()
        self.mettre_a_jour_interface_adversaire()

        if self.pokemon_joueur.est_ko():
            pokemon_disponibles = [p for p in self.equipe_joueur if not p.est_ko()]
            if pokemon_disponibles:
                self.ajouter_message(f"{self.pokemon_joueur.nom} est K.O. ! Choisissez un remplaçant.")
                for btn in self.boutons_attaque:
                    btn.setEnabled(False)
            else:
                self.ajouter_message("Vous n'avez plus de Pokémon en état de combattre...")
                self.zone_attaques.hide()
                self.zone_switch.hide()
                self.zone_fin_combat.show()
        else:
            for btn in self.boutons_attaque:
                btn.setEnabled(True)

    def recommencer_combat(self):
        if self.main_window:
            self.main_window.show_combat()
        else:
            self.close()
            nouvelle_fenetre = CombatGUI()
            nouvelle_fenetre.show()

    def quitter(self):
        if self.main_window:
            self.main_window.show_menu()
        else:
            self.close()
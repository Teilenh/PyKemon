import tkinter as tk
from tkinter import ttk, messagebox
from src.core.pokemon import POKEMONS_DISPONIBLES, creer_pokemon
from src.core.combat import calcul_degats
from src.core.team_builder import TeamBuilder
from src.core.adversaire import Adversaire
from random import choice

class MenuPrincipal:
    def __init__(self, root):
        self.root = root
        self.root.title("PyKemon")
        self.root.geometry("400x500")
        
        # Style
        style = ttk.Style()
        style.configure("Title.TLabel", font=("Arial", 24, "bold"))
        style.configure("Subtitle.TLabel", font=("Arial", 12))
        
        # Titre
        titre = ttk.Label(root, text="PyKemon", style="Title.TLabel")
        titre.pack(pady=20)
        
        # Description
        description = ttk.Label(root, text="Combat Pokémon - 1ère Génération", style="Subtitle.TLabel")
        description.pack(pady=10)
        
        # Boutons
        btn_team = ttk.Button(root, text="Créer une équipe", command=self.ouvrir_team_builder)
        btn_team.pack(pady=10, padx=50, fill=tk.X)
        
        btn_combat = ttk.Button(root, text="Lancer un combat", command=self.lancer_combat)
        btn_combat.pack(pady=10, padx=50, fill=tk.X)
        
        btn_quitter = ttk.Button(root, text="Quitter", command=self.quitter_application)
        btn_quitter.pack(pady=10, padx=50, fill=tk.X)
        
        # Version
        version = ttk.Label(root, text="Version 1.0 - Première Génération")
        version.pack(side=tk.BOTTOM, pady=20)

    def ouvrir_team_builder(self):
        fenetre_team = tk.Toplevel(self.root)
        TeamBuilderGUI(fenetre_team)

    def lancer_combat(self):
        fenetre_combat = tk.Toplevel(self.root)
        CombatGUI(fenetre_combat)

    def quitter_application(self):
        self.root.quit()

class TeamBuilderGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("PyKemon - Team Builder")
        self.root.geometry("800x600")
        
        self.team_builder = TeamBuilder()
        
        # Menu contextuel
        self.menu_contextuel = tk.Menu(root, tearoff=0)
        self.menu_contextuel.add_command(label="Retirer le Pokémon", command=self.retirer_pokemon)
        self.index_selectionne = None
        
        # Frame principale
        main_frame = ttk.Frame(root)
        main_frame.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)
        
        # Frame équipe (haut)
        frame_equipe = ttk.LabelFrame(main_frame, text="Votre Équipe")
        frame_equipe.pack(fill=tk.X, padx=5, pady=5)
        
        # Frame pour les emplacements d'équipe
        frame_emplacements = ttk.Frame(frame_equipe)
        frame_emplacements.pack(pady=5)
        
        # Création des 6 emplacements d'équipe
        self.emplacements_equipe = []
        for i in range(6):
            emplacement = ttk.Button(frame_emplacements, text="Vide", width=20)
            emplacement.grid(row=0, column=i, padx=2)
            emplacement.bind('<Button-1>', lambda e, idx=i: self.configurer_pokemon(idx))
            emplacement.bind('<Button-3>', lambda e, idx=i: self.afficher_menu_contextuel(e, idx))
            self.emplacements_equipe.append(emplacement)
        
        # Frame PC (bas)
        frame_pc = ttk.LabelFrame(main_frame, text="Pokémon Disponibles")
        frame_pc.pack(expand=True, fill=tk.BOTH, padx=5, pady=5)
        
        # Liste des Pokémon disponibles
        self.liste_pokemon = tk.Listbox(frame_pc)
        self.liste_pokemon.pack(expand=True, fill=tk.BOTH, padx=5, pady=5)
        
        # Frame pour les boutons
        frame_boutons = ttk.Frame(main_frame)
        frame_boutons.pack(fill=tk.X, pady=5)
        
        # Boutons
        btn_ajouter = ttk.Button(frame_boutons, text="Ajouter à l'équipe",
                                command=self.ajouter_pokemon)
        btn_ajouter.pack(side=tk.LEFT, padx=5)
        
        btn_sauvegarder = ttk.Button(frame_boutons, text="Sauvegarder Équipe",
                                    command=self.sauvegarder_equipe)
        btn_sauvegarder.pack(side=tk.LEFT, padx=5)
        
        btn_quitter = ttk.Button(frame_boutons, text="Quitter",
                                command=self.root.destroy)
        btn_quitter.pack(side=tk.RIGHT, padx=5)
        
        # Initialisation des listes
        self.mettre_a_jour_listes()
        self.charger_equipe_existante()

    def mettre_a_jour_listes(self):
        """Met à jour la liste des Pokémon disponibles"""
        self.liste_pokemon.delete(0, tk.END)
        for pokemon in self.team_builder.obtenir_liste_pokemon_disponibles():
            self.liste_pokemon.insert(tk.END, pokemon)

    def mettre_a_jour_emplacement(self, index, pokemon=None):
        """Met à jour l'affichage d'un emplacement d'équipe"""
        if pokemon:
            attaques = ", ".join(a.nom for a in pokemon.attaques) if pokemon.attaques else "Aucune attaque"
            self.emplacements_equipe[index].configure(text=f"{pokemon.nom}\n{attaques}")
        else:
            self.emplacements_equipe[index].configure(text="Vide")

    def charger_equipe_existante(self):
        """Charge et affiche l'équipe existante"""
        success, _ = self.team_builder.charger_equipe()
        if success:
            for i, pokemon in enumerate(self.team_builder.equipe):
                self.mettre_a_jour_emplacement(i, pokemon)

    def ajouter_pokemon(self):
        """Ajoute un Pokémon à l'équipe"""
        if not self.liste_pokemon.curselection():
            messagebox.showwarning("Erreur", "Veuillez sélectionner un Pokémon")
            return
            
        if len(self.team_builder.equipe) >= 6:
            messagebox.showwarning("Erreur", "L'équipe est déjà complète (6 Pokémon maximum)")
            return
            
        nom_pokemon = self.liste_pokemon.get(self.liste_pokemon.curselection())
        succes, message = self.team_builder.ajouter_pokemon(nom_pokemon)
        
        if succes:
            index = len(self.team_builder.equipe) - 1
            self.mettre_a_jour_emplacement(index, self.team_builder.equipe[index])
        else:
            messagebox.showwarning("Erreur", message)

    def configurer_pokemon(self, index):
        """Ouvre la fenêtre de configuration des attaques pour un Pokémon"""
        if index >= len(self.team_builder.equipe):
            return
            
        pokemon = self.team_builder.equipe[index]
        fenetre_attaques = tk.Toplevel(self.root)
        ConfigurationAttaquesGUI(fenetre_attaques, pokemon, 
                               lambda: self.mettre_a_jour_emplacement(index, pokemon))

    def sauvegarder_equipe(self):
        """Sauvegarde l'équipe actuelle"""
        succes, message = self.team_builder.sauvegarder_equipe()
        if succes:
            messagebox.showinfo("Succès", message)
        else:
            messagebox.showwarning("Erreur", message)

    def afficher_menu_contextuel(self, event, index):
        """Affiche le menu contextuel pour un emplacement d'équipe"""
        if index < len(self.team_builder.equipe):
            self.index_selectionne = index
            self.menu_contextuel.tk_popup(event.x_root, event.y_root)

    def retirer_pokemon(self):
        """Retire le Pokémon sélectionné de l'équipe"""
        if self.index_selectionne is not None and self.index_selectionne < len(self.team_builder.equipe):
            pokemon = self.team_builder.equipe[self.index_selectionne]
            self.team_builder.equipe.pop(self.index_selectionne)
            
            # Mise à jour de l'affichage
            for i in range(len(self.team_builder.equipe), 6):
                self.mettre_a_jour_emplacement(i)
            
            messagebox.showinfo("Succès", f"{pokemon.nom} a été retiré de l'équipe!")
            self.index_selectionne = None

class ConfigurationAttaquesGUI:
    def __init__(self, root, pokemon, callback_maj):
        self.root = root
        self.pokemon = pokemon
        self.callback_maj = callback_maj
        
        self.root.title(f"Configuration des attaques - {pokemon.nom}")
        self.root.geometry("400x400")
        
        # Titre
        titre = ttk.Label(root, text=f"Attaques de {pokemon.nom}", 
                         font=("Arial", 14, "bold"))
        titre.pack(pady=10)
        
        # Frame pour les emplacements d'attaques
        frame_emplacements = ttk.Frame(root)
        frame_emplacements.pack(pady=10)
        
        # Création des 4 emplacements d'attaques
        self.emplacements_attaques = []
        for i in range(4):
            row, col = divmod(i, 2)
            emplacement = ttk.Label(frame_emplacements, 
                                  text="Aucune attaque",
                                  relief="solid",
                                  padding=10)
            emplacement.grid(row=row, column=col, padx=5, pady=5)
            self.emplacements_attaques.append(emplacement)
        
        # Liste des attaques disponibles
        self.liste_attaques = tk.Listbox(root, selectmode=tk.MULTIPLE)
        self.liste_attaques.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)
        
        # Ajout des attaques disponibles
        for attaque in pokemon.attaques_possibles:
            self.liste_attaques.insert(tk.END, attaque)
            if attaque in [a.nom for a in pokemon.attaques]:
                index = self.liste_attaques.size() - 1
                self.liste_attaques.selection_set(index)
                
        # Mise à jour des emplacements d'attaques
        self.mettre_a_jour_emplacements()
        
        # Frame pour les boutons
        frame_boutons = ttk.Frame(root)
        frame_boutons.pack(pady=10)
        
        btn_ok = ttk.Button(frame_boutons, text="OK", command=self.valider)
        btn_ok.pack(side=tk.LEFT, padx=5)
        
        btn_annuler = ttk.Button(frame_boutons, text="Annuler", 
                                command=self.root.destroy)
        btn_annuler.pack(side=tk.LEFT, padx=5)
        
        # Binding pour la mise à jour des emplacements
        self.liste_attaques.bind('<<ListboxSelect>>', lambda e: self.mettre_a_jour_emplacements())

    def mettre_a_jour_emplacements(self):
        """Met à jour l'affichage des emplacements d'attaques"""
        selections = self.liste_attaques.curselection()
        attaques = [self.liste_attaques.get(i) for i in selections]
        
        # Réinitialisation des emplacements
        for emplacement in self.emplacements_attaques:
            emplacement.configure(text="Aucune attaque")
        
        # Mise à jour avec les attaques sélectionnées
        for i, attaque in enumerate(attaques[:4]):
            self.emplacements_attaques[i].configure(text=attaque)

    def valider(self):
        selections = self.liste_attaques.curselection()
        if len(selections) > 4:
            messagebox.showwarning("Erreur", "Vous ne pouvez sélectionner que 4 attaques maximum")
            return
            
        if not selections:
            messagebox.showwarning("Erreur", "Veuillez sélectionner au moins une attaque")
            return
            
        attaques = [self.liste_attaques.get(i) for i in selections]
        self.pokemon.attaques = []  # Réinitialisation des attaques
        
        erreurs = []
        for attaque in attaques:
            if not self.pokemon.apprendre_attaque(attaque):
                erreurs.append(f"Impossible d'apprendre {attaque}")
        
        if erreurs:
            messagebox.showwarning("Erreur", "\n".join(erreurs))
            return
            
        self.callback_maj()  # Mise à jour de l'interface principale
        self.root.destroy()

class CombatGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("PyKemon Combat")
        self.root.geometry("600x500")  # Augmenté pour l'espace des Pokémon

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
        self.adversaire = Adversaire(6)  # Deux Pokémon pour l'adversaire
        self.pokemon_adversaire = self.adversaire.pokemon_actif
        
        if not self.pokemon_adversaire:
            self.pokemon_adversaire = creer_pokemon("Carapuce")  # Adversaire par défaut

        # Frame pour les informations des Pokémon
        self.info_frame = ttk.Frame(root)
        self.info_frame.pack(pady=10)

        # Informations du Pokémon joueur
        self.label_joueur = ttk.Label(self.info_frame, text="", font=("Courier", 10))
        self.label_joueur.pack()

        # Informations du Pokémon adversaire
        self.label_adversaire = ttk.Label(self.info_frame, text="", font=("Courier", 10))
        self.label_adversaire.pack()

        # Zone de messages avec historique
        self.messages_frame = ttk.Frame(root)
        self.messages_frame.pack(pady=10, fill=tk.X, padx=20)
        
        # Style pour la zone de messages
        style = ttk.Style()
        style.configure("Messages.TFrame", background="white")
        self.messages_frame.configure(style="Messages.TFrame")
        
        # Liste des derniers messages
        self.messages = []
        self.historique_messages = ttk.Label(
            self.messages_frame,
            text="",
            wraplength=500,
            justify=tk.CENTER,
            font=("Arial", 10)
        )
        self.historique_messages.pack(pady=10)

        # Frame pour les boutons d'attaque
        self.boutons_frame = ttk.Frame(root)
        self.boutons_frame.pack(pady=10)

        # Création des boutons d'attaque
        self.boutons_attaque = []
        for i in range(2):
            for j in range(2):
                btn = ttk.Button(self.boutons_frame, text="", width=20)
                btn.grid(row=i, column=j, padx=5, pady=5)
                self.boutons_attaque.append(btn)

        # Frame pour les Pokémon disponibles
        self.frame_pokemon_dispo = ttk.Frame(root)
        self.frame_pokemon_dispo.pack(pady=10)
        self.frame_pokemon_dispo.pack_forget()  # Caché par défaut

        # Création des boutons pour chaque Pokémon
        self.boutons_pokemon = []
        for pokemon in self.equipe_joueur:
            btn = ttk.Button(self.frame_pokemon_dispo, 
                           text=f"{pokemon.nom} - {pokemon.pv}/{pokemon.pv_max} PV",
                           command=lambda p=pokemon: self.changer_pokemon(p))
            btn.pack(side=tk.LEFT, padx=5)
            self.boutons_pokemon.append(btn)

        # Frame pour les boutons de fin de combat
        self.frame_fin_combat = ttk.Frame(root)
        self.frame_fin_combat.pack(pady=10)
        
        # Bouton recommencer
        self.btn_recommencer = ttk.Button(self.frame_fin_combat, text="Recommencer", 
                                        command=self.recommencer_combat)
        self.btn_recommencer.pack(side=tk.LEFT, padx=5)
        
        # Bouton quitter
        self.btn_quitter = ttk.Button(self.frame_fin_combat, text="Quitter",
                                     command=self.root.destroy)
        self.btn_quitter.pack(side=tk.LEFT, padx=5)
        
        # Cacher les boutons de fin de combat au début
        self.frame_fin_combat.pack_forget()

        self.mettre_a_jour_affichage()
        self.configurer_boutons()

    def ajouter_message(self, message):
        """Ajoute un message à l'historique et met à jour l'affichage"""
        self.messages.append(message)
        if len(self.messages) > 3:  # Garde les 3 derniers messages
            self.messages.pop(0)
        self.historique_messages.configure(text="\n".join(self.messages))

    def changer_pokemon(self, nouveau_pokemon):
        if nouveau_pokemon.est_ko():
            self.ajouter_message(f"{nouveau_pokemon.nom} est K.O. et ne peut pas combattre!")
            return

        self.pokemon_joueur = nouveau_pokemon
        self.mettre_a_jour_affichage()
        self.configurer_boutons()
        self.frame_pokemon_dispo.pack_forget()

        # Tour de l'adversaire après le changement
        self.root.after(1000, self.tour_adversaire)

    def tour_adversaire(self):
        if self.pokemon_adversaire.est_ko():
            nouveau_pokemon = self.adversaire.choisir_pokemon()
            if nouveau_pokemon:
                self.pokemon_adversaire = nouveau_pokemon
                self.ajouter_message(f"L'adversaire envoie {self.pokemon_adversaire.nom}!")
                self.mettre_a_jour_affichage()
                # Réactiver les boutons après le changement de Pokémon
                for bouton in self.boutons_attaque:
                    bouton.config(state="normal")
                return
            else:
                self.ajouter_message("Vous avez gagné le combat!")
                self.boutons_frame.pack_forget()
                self.frame_fin_combat.pack()
                return

        # Ne pas attaquer si le Pokémon est KO
        if self.pokemon_adversaire.est_ko():
            return

        attaque_adversaire = choice(self.pokemon_adversaire.attaques)
        degats_adversaire = calcul_degats(self.pokemon_adversaire, self.pokemon_joueur, attaque_adversaire)
        self.pokemon_joueur.subir_degats(degats_adversaire)

        self.ajouter_message(f"{self.pokemon_adversaire.nom} utilise {attaque_adversaire.nom} et inflige {degats_adversaire} dégâts!")
        self.mettre_a_jour_affichage()

        if self.pokemon_joueur.est_ko():
            pokemon_disponibles = [p for p in self.equipe_joueur if not p.est_ko()]
            if pokemon_disponibles:
                self.ajouter_message(f"{self.pokemon_joueur.nom} est K.O.! Choisissez un autre Pokémon!")
                self.frame_pokemon_dispo.pack()
                for bouton in self.boutons_attaque:
                    bouton.config(state="disabled")
            else:
                self.ajouter_message("Tous vos Pokémon sont K.O.! Vous avez perdu!")
                self.boutons_frame.pack_forget()
                self.frame_fin_combat.pack()
        else:
            for bouton in self.boutons_attaque:
                bouton.config(state="normal")

    def mettre_a_jour_affichage(self):
        # Mise à jour des informations des Pokémon
        info_joueur = f"JOUEUR: {self.pokemon_joueur.nom}\nPV: {self.pokemon_joueur.pv}/{self.pokemon_joueur.pv_max}"
        info_adversaire = f"ADVERSAIRE: {self.pokemon_adversaire.nom}\nPV: {self.pokemon_adversaire.pv}/{self.pokemon_adversaire.pv_max}"
        
        self.label_joueur.config(text=info_joueur)
        self.label_adversaire.config(text=info_adversaire)

        # Mise à jour des boutons Pokémon
        for i, pokemon in enumerate(self.equipe_joueur):
            self.boutons_pokemon[i].config(
                text=f"{pokemon.nom} - {pokemon.pv}/{pokemon.pv_max} PV",
                state="normal" if not pokemon.est_ko() else "disabled"
            )

    def configurer_boutons(self):
        # Configuration des boutons avec les attaques disponibles
        for i, bouton in enumerate(self.boutons_attaque):
            if i < len(self.pokemon_joueur.attaques):
                attaque = self.pokemon_joueur.attaques[i]
                bouton.config(
                    text=f"{attaque.nom}\n{attaque.type} - {attaque.puissance}",
                    command=lambda a=attaque: self.utiliser_attaque(a)
                )
            else:
                bouton.config(text="-", state="disabled")

    def utiliser_attaque(self, attaque):
        # Désactiver les boutons pendant l'attaque
        for bouton in self.boutons_attaque:
            bouton.config(state="disabled")
            
        # Calcul et application des dégâts
        degats = calcul_degats(self.pokemon_joueur, self.pokemon_adversaire, attaque)
        self.pokemon_adversaire.subir_degats(degats)
        
        # Mise à jour du message et de l'interface
        message_joueur = f"{self.pokemon_joueur.nom} utilise {attaque.nom} et inflige {degats} dégâts!"
        self.ajouter_message(message_joueur)
        self.mettre_a_jour_affichage()
        
        # Tour de l'adversaire après un délai
        self.root.after(1000, self.tour_adversaire)

    def recommencer_combat(self):
        # Fermer la fenêtre actuelle
        self.root.destroy()
        # Créer une nouvelle fenêtre de combat
        nouvelle_fenetre = tk.Toplevel()
        CombatGUI(nouvelle_fenetre)

if __name__ == "__main__":
    root = tk.Tk()
    app = MenuPrincipal(root)
    root.mainloop() 
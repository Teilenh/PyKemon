import csv
import os
from .pokemon import POKEMONS_DISPONIBLES, ATTAQUES, creer_pokemon

class TeamBuilder:
    def __init__(self):
        self.equipe = []
        self.fichier_equipe = "Assets/equipe.csv"
        self._observers = []  # Pour le pattern Observer

    def add_observer(self, observer):
        """Ajoute un observateur pour les changements d'équipe"""
        self._observers.append(observer)

    def notify_observers(self, event_type, data=None):
        """Notifie tous les observateurs d'un changement"""
        for observer in self._observers:
            if hasattr(observer, 'on_team_update'):
                observer.on_team_update(event_type, data)

    def ajouter_pokemon(self, nom_pokemon):
        """Ajoute un Pokémon à l'équipe"""
        if len(self.equipe) >= 6:
            return False, "L'équipe est déjà complète (6 Pokémon maximum)"
        
        pokemon = creer_pokemon(nom_pokemon)
        if pokemon is None:
            return False, f"Pokémon {nom_pokemon} non trouvé"
        
        self.equipe.append(pokemon)
        self.notify_observers('add_pokemon', {'index': len(self.equipe) - 1, 'pokemon': pokemon})
        return True, f"{nom_pokemon} ajouté à l'équipe"

    def retirer_pokemon(self, index):
        """Retire un Pokémon de l'équipe"""
        if 0 <= index < len(self.equipe):
            pokemon = self.equipe.pop(index)
            self.notify_observers('remove_pokemon', {'index': index, 'pokemon': pokemon})
            return True, f"{pokemon.nom} retiré de l'équipe"
        return False, "Index invalide"

    def echanger_pokemon(self, index1, index2):
        """Échange la position de deux Pokémon dans l'équipe"""
        if 0 <= index1 < len(self.equipe) and 0 <= index2 < len(self.equipe):
            self.equipe[index1], self.equipe[index2] = self.equipe[index2], self.equipe[index1]
            self.notify_observers('swap_pokemon', {'index1': index1, 'index2': index2})
            return True, f"Pokémon échangés aux positions {index1} et {index2}"
        return False, "Index invalides"

    def remplacer_pokemon(self, index, nouveau_nom_pokemon):
        """Remplace un Pokémon par un nouveau"""
        if 0 <= index < len(self.equipe):
            ancien_pokemon = self.equipe[index]
            nouveau_pokemon = creer_pokemon(nouveau_nom_pokemon)
            if nouveau_pokemon is None:
                return False, f"Pokémon {nouveau_nom_pokemon} non trouvé"
            
            self.equipe[index] = nouveau_pokemon
            self.notify_observers('replace_pokemon', {
                'index': index,
                'old_pokemon': ancien_pokemon,
                'new_pokemon': nouveau_pokemon
            })
            return True, f"{ancien_pokemon.nom} remplacé par {nouveau_pokemon.nom}"
        return False, "Index invalide"

    def configurer_attaques(self, index_pokemon, attaques):
        """Configure les attaques d'un Pokémon"""
        if not (0 <= index_pokemon < len(self.equipe)):
            return False, "Pokémon non trouvé dans l'équipe"
        
        pokemon = self.equipe[index_pokemon]
        anciennes_attaques = pokemon.attaques.copy()
        pokemon.attaques = []  # Réinitialiser les attaques
        
        for nom_attaque in attaques:
            if not pokemon.apprendre_attaque(nom_attaque):
                pokemon.attaques = anciennes_attaques  # Restaurer les anciennes attaques
                return False, f"Impossible d'apprendre {nom_attaque}"
        
        self.notify_observers('update_moves', {
            'index': index_pokemon,
            'pokemon': pokemon,
            'old_moves': anciennes_attaques,
            'new_moves': pokemon.attaques
        })
        return True, "Attaques configurées avec succès"

    def sauvegarder_equipe(self):
        """Sauvegarde l'équipe dans un fichier CSV"""
        os.makedirs(os.path.dirname(self.fichier_equipe), exist_ok=True)
        
        with open(self.fichier_equipe, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["Pokemon", "Attaque1", "Attaque2", "Attaque3", "Attaque4"])
            
            for pokemon in self.equipe:
                attaques = [attaque.nom for attaque in pokemon.attaques]
                while len(attaques) < 4:
                    attaques.append("")
                writer.writerow([pokemon.nom] + attaques)
        
        self.notify_observers('save_team', {'file_path': self.fichier_equipe})
        return True, f"Équipe sauvegardée dans {self.fichier_equipe}"

    def charger_equipe(self):
        """Charge une équipe depuis le fichier CSV"""
        if not os.path.exists(self.fichier_equipe):
            return False, "Aucune équipe sauvegardée"
        
        ancienne_equipe = self.equipe.copy()
        self.equipe = []  # Réinitialiser l'équipe
        
        try:
            with open(self.fichier_equipe, 'r') as f:
                reader = csv.reader(f)
                next(reader)  # Ignorer l'en-tête
                
                for row in reader:
                    if len(row) >= 5:  # Pokemon + 4 attaques
                        nom_pokemon = row[0]
                        attaques = [a for a in row[1:5] if a]  # Ignorer les attaques vides
                        
                        success, message = self.ajouter_pokemon(nom_pokemon)
                        if success:
                            self.configurer_attaques(len(self.equipe) - 1, attaques)
            
                self.notify_observers('load_team', {
                    'file_path': self.fichier_equipe,
                    'old_team': ancienne_equipe,
                    'new_team': self.equipe
                })
                return True, f"Équipe chargée depuis {self.fichier_equipe}"
                
        except Exception as e:
            self.equipe = ancienne_equipe  # Restaurer l'ancienne équipe en cas d'erreur
            return False, f"Erreur lors du chargement de l'équipe : {str(e)}"

    def supprimer_equipe(self):
        """Supprime l'équipe et le fichier de sauvegarde"""
        ancienne_equipe = self.equipe.copy()
        self.equipe.clear()
        
        try:
            if os.path.exists(self.fichier_equipe):
                os.remove(self.fichier_equipe)
            
            self.notify_observers('delete_team', {'old_team': ancienne_equipe})
            return True, "Équipe supprimée avec succès"
        except Exception as e:
            self.equipe = ancienne_equipe  # Restaurer l'ancienne équipe en cas d'erreur
            return False, f"Erreur lors de la suppression de l'équipe : {str(e)}"

    def obtenir_liste_pokemon_disponibles(self):
        """Retourne la liste des Pokémon disponibles"""
        return list(POKEMONS_DISPONIBLES.keys())

    def obtenir_attaques_disponibles(self, index_pokemon):
        """Retourne la liste des attaques disponibles pour un Pokémon"""
        if 0 <= index_pokemon < len(self.equipe):
            return self.equipe[index_pokemon].attaques_possibles
        return []

    def __str__(self):
        if not self.equipe:
            return "Équipe vide"
        
        resultat = "Équipe actuelle:\n"
        for i, pokemon in enumerate(self.equipe, 1):
            resultat += f"\n{i}. {pokemon}"
        return resultat 
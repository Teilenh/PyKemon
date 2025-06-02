import random
from .pokemon import POKEMONS_DISPONIBLES, creer_pokemon

class Adversaire:
    def __init__(self, nombre_pokemon=2):
        self.equipe = []
        self.pokemon_actif = None
        self.generer_equipe(nombre_pokemon)

    def generer_equipe(self, nombre):
        """Génère une équipe aléatoire pour l'adversaire"""
        pokemons_disponibles = list(POKEMONS_DISPONIBLES.keys())
        nombre = min(nombre, len(pokemons_disponibles))
        
        # Sélection aléatoire des Pokémon
        for _ in range(nombre):
            if not pokemons_disponibles:
                break
                
            nom_pokemon = random.choice(pokemons_disponibles)
            pokemons_disponibles.remove(nom_pokemon)
            
            pokemon = creer_pokemon(nom_pokemon)
            if pokemon:
                # Sélection aléatoire de 4 attaques parmi les attaques possibles
                attaques_possibles = pokemon.attaques_possibles.copy()
                nombre_attaques = min(4, len(attaques_possibles))
                
                attaques_choisies = random.sample(attaques_possibles, nombre_attaques)
                for attaque in attaques_choisies:
                    pokemon.apprendre_attaque(attaque)
                
                self.equipe.append(pokemon)

        if self.equipe:
            self.pokemon_actif = self.equipe[0]

    def choisir_pokemon(self):
        """Choisit aléatoirement un nouveau Pokémon dans l'équipe"""
        pokemons_vivants = [p for p in self.equipe if not p.est_ko()]
        if not pokemons_vivants:
            return None
            
        if self.pokemon_actif in pokemons_vivants:
            pokemons_vivants.remove(self.pokemon_actif)
            
        if pokemons_vivants:
            self.pokemon_actif = random.choice(pokemons_vivants)
        
        return self.pokemon_actif

    def choisir_attaque(self):
        """Choisit aléatoirement une attaque pour le Pokémon actif"""
        if self.pokemon_actif and self.pokemon_actif.attaques:
            return random.choice(self.pokemon_actif.attaques)
        return None

    def a_perdu(self):
        """Vérifie si tous les Pokémon de l'adversaire sont K.O."""
        return all(pokemon.est_ko() for pokemon in self.equipe)

    def __str__(self):
        resultat = "Équipe adverse:\n"
        for i, pokemon in enumerate(self.equipe, 1):
            status = " (Actif)" if pokemon == self.pokemon_actif else ""
            resultat += f"\n{i}. {pokemon.nom}{status} - PV: {pokemon.pv}/{pokemon.pv_max}"
        return resultat 
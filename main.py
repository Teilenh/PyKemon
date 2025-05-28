from dresseur import *
from combat import *
from PKMtypes import *
from pokemon import *
import time


# Initialisation
pikachu = POKEMONS_DE_BASE["Pikachu"]
carapuce = POKEMONS_DE_BASE["Carapuce"]

print(pikachu)
print()
print(carapuce)

sacha = Dresseur("Sacha")
ondine = Dresseur("Ondine")

sacha.ajouter_pokemon(pikachu)
ondine.ajouter_pokemon(carapuce)

print(f"\nCombat entre {sacha.nom} et {ondine.nom} !\n")

# Boucle de combat
while not sacha.equipe_ko() and not ondine.equipe_ko():
    pokemon_sacha = sacha.choisir_pokemon_actif()
    pokemon_ondine = ondine.choisir_pokemon_actif()

    if pokemon_sacha is None or pokemon_ondine is None:
        break

    # Tour de Sacha
    attaque_sacha = choisir_attaque(pokemon_sacha)
    print(tour_combat(pokemon_sacha, pokemon_ondine, attaque_sacha))
    print(f"{pokemon_sacha.nom}: {pokemon_sacha.pv} PV | {pokemon_ondine.nom}: {pokemon_ondine.pv} PV")
    if pokemon_ondine.est_ko():
        print(f"{pokemon_ondine.nom} est KO !\n")
        time.sleep(1)
        continue

    time.sleep(1)

    # Tour d’Ondine (attaque aléatoire pour l'instant)
    from random import choice
    attaque_ondine = choice(pokemon_ondine.attaques)
    print(tour_combat(pokemon_ondine, pokemon_sacha, attaque_ondine))
    print(f"{pokemon_sacha.nom}: {pokemon_sacha.pv} PV | {pokemon_ondine.nom}: {pokemon_ondine.pv} PV")
    if pokemon_sacha.est_ko():
        print(f"{pokemon_sacha.nom} est KO !\n")

    time.sleep(1)

# Fin de combat
print("\n--- Résultat final ---")
if sacha.equipe_ko():
    print(f"{ondine.nom} remporte le combat !")
else:
    print(f"{sacha.nom} remporte le combat !")

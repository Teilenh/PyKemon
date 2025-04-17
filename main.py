from pokemon import Pokemon
from dresseur import Dresseur
from combat import tour_combat
from PKMtypes import get_multiplicateur
import time

# Initialisation des Pokémon
pikachu = Pokemon("Pikachu", "Électrique", 100, 50, 30, 50)
carapuce = Pokemon("Carapuce", "Eau", 120, 40, 50, 50)

# Initialisation des Dresseurs
sacha = Dresseur("Sacha")
ondine = Dresseur("Ondine")

sacha.ajouter_pokemon(pikachu)
ondine.ajouter_pokemon(carapuce)

# Combat
print(f"Combat entre {sacha.nom} et {ondine.nom} !\n")

while not sacha.equipe_ko() and not ondine.equipe_ko():
    pokemon_sacha = sacha.choisir_pokemon_actif()
    pokemon_ondine = ondine.choisir_pokemon_actif()

    if pokemon_sacha is None or pokemon_ondine is None:
        break

    print(tour_combat(pokemon_sacha, pokemon_ondine))
    print(f"{pokemon_sacha.nom}: {pokemon_sacha.pv} PV | {pokemon_ondine.nom}: {pokemon_ondine.pv} PV")
    if pokemon_ondine.est_ko():
        print(f"{pokemon_ondine.nom} est KO !\n")
        time.sleep(1)
        continue

    time.sleep(1)

    print(tour_combat(pokemon_ondine, pokemon_sacha))
    print(f"{pokemon_sacha.nom}: {pokemon_sacha.pv} PV | {pokemon_ondine.nom}: {pokemon_ondine.pv} PV")
    if pokemon_sacha.est_ko():
        print(f"{pokemon_sacha.nom} est KO !\n")

    time.sleep(1)

# Résultat
print("\n--- Résultat final ---")
if sacha.equipe_ko():
    print(f"{ondine.nom} remporte le combat !")
else:
    print(f"{sacha.nom} remporte le combat !")

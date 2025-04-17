from PKMtypes import get_multiplicateur

def calcul_degats(pokemon_atk, pokemon_def):
    mult = get_multiplicateur(pokemon_atk.type, pokemon_def.type)
    base_degats = max(1, pokemon_atk.attaque - pokemon_def.defense)
    return int(base_degats * mult)

def tour_combat(attacker, defender):
    degats = calcul_degats(attacker, defender)
    defender.subir_degats(degats)
    return f"{attacker.nom} attaque {defender.nom} et inflige {degats} dégâts !"

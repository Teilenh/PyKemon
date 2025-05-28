table_types = {
    'Feu': {'Plante': 2.0, 'Eau': 0.5, 'Feu': 1},
    'Eau': {'Feu': 2.0, 'Plante': 0.5, 'Eau': 1},
    'Plante': {'Eau': 2.0, 'Feu': 0.5, 'Plante': 1},
    'Électrique': {'Eau': 2.0, 'Plante': 0.5, 'Sol': 0.0},
}

def get_multiplicateur(type_attaquant, type_cible):
    return table_types.get(type_attaquant, {}).get(type_cible, 1.0)

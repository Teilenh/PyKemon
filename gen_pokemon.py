import requests
import json
import time

TYPE_TRANSLATION = {
    "normal": "Normal", "fire": "Feu", "water": "Eau", "electric": "Électrique",
    "grass": "Plante", "ice": "Glace", "fighting": "Combat", "poison": "Poison",
    "ground": "Sol", "flying": "Vol", "psychic": "Psy", "bug": "Insecte",
    "rock": "Roche", "ghost": "Spectre", "dragon": "Dragon"
}

def generate_data():
    print("Fetching species for French names...")
    species_res = requests.get("https://pokeapi.co/api/v2/pokemon-species?limit=151").json()
    french_names = []
    for s in species_res['results']:
        s_data = requests.get(s['url']).json()
        name = s_data['name']
        for n in s_data['names']:
            if n['language']['name'] == 'fr':
                name = n['name']
                break
        # Override special names
        if name == "Nidoran♀": name = "Nidoran-f"
        elif name == "Nidoran♂": name = "Nidoran-m"
        elif name == "M. Mime": name = "M. Mime"
        french_names.append(name)
        
    print("Fetching moves...")
    moves_cache = {}
    for i in range(1, 166): # Gen 1 moves
        try:
            m_data = requests.get(f"https://pokeapi.co/api/v2/move/{i}").json()
            fname = m_data['name']
            for n in m_data['names']:
                if n['language']['name'] == 'fr':
                    fname = n['name']
                    break
            # Handle status damage class properly
            category = "physique" if m_data['damage_class']['name'] == 'physical' else "special"
            moves_cache[m_data['name']] = {
                "fr_name": fname.replace('"', '\\"'),
                "power": m_data['power'] or 0,
                "accuracy": m_data['accuracy'] or 100,
                "type": TYPE_TRANSLATION.get(m_data['type']['name'], "Normal"),
                "category": category
            }
        except:
            pass

    print("Fetching pokemon data...")
    pokemon_dict = {}
    all_used_moves = {}
    
    for i in range(1, 152):
        p_data = requests.get(f"https://pokeapi.co/api/v2/pokemon/{i}").json()
        name = french_names[i-1]
        
        stats = {s['stat']['name']: s['base_stat'] for s in p_data['stats']}
        
        type_ = TYPE_TRANSLATION.get(p_data['types'][0]['type']['name'], "Normal")
        
        valid_moves = []
        for m in p_data['moves']:
            m_name = m['move']['name']
            if m_name in moves_cache:
                for v in m['version_group_details']:
                    if v['version_group']['name'] in ['red-blue', 'yellow']:
                        valid_moves.append(moves_cache[m_name])
                        all_used_moves[m_name] = moves_cache[m_name]
                        break
            if len(valid_moves) >= 6:
                break
                
        # Fallback if somehow no moves
        if not valid_moves:
            valid_moves = [moves_cache.get("tackle", {"fr_name": "Charge", "power": 40, "accuracy": 100, "type": "Normal", "category": "physique"})]
            
        pokemon_dict[name] = {
            "type": type_,
            "stats": [stats['hp'], stats['attack'], stats['defense'], stats['special-attack'], stats['speed']],
            "moves": valid_moves
        }
        
    with open("gen_output.py", "w", encoding="utf-8") as f:
        f.write('ATTAQUES = {\n')
        for m in all_used_moves.values():
            f.write(f'    "{m["fr_name"]}": Attaque("{m["fr_name"]}", "{m["type"]}", {m["power"]}, "{m["category"]}", {m["accuracy"]}),\n')
        f.write('}\n\n')
        
        f.write('POKEMONS_DISPONIBLES = {\n')
        for p_name, p_data in pokemon_dict.items():
            f.write(f'    "{p_name}": {{\n')
            moves_str = '", "'.join([m["fr_name"] for m in p_data["moves"]])
            f.write(f'        "base": Pokemon("{p_name}", "{p_data["type"]}", {p_data["stats"][0]}, {p_data["stats"][1]}, {p_data["stats"][2]}, {p_data["stats"][3]}, {p_data["stats"][4]}, ["{moves_str}"]),\n')
            f.write('        "niveau": 50\n')
            f.write('    },\n')
        f.write('}\n')
    print("Done!")

generate_data()

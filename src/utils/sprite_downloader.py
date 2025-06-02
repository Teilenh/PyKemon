import os
import requests
from pathlib import Path
import unicodedata
import re

def normalize_name(name):
    """Normalise le nom du Pokémon pour l'URL et le nom de fichier"""
    # Supprime les accents
    name = unicodedata.normalize('NFKD', name).encode('ASCII', 'ignore').decode('ASCII')
    # Convertit en minuscules
    name = name.lower()
    # Remplace les caractères spéciaux par des tirets
    name = re.sub(r'[^a-z0-9]', '-', name)
    # Supprime les tirets multiples
    name = re.sub(r'-+', '-', name)
    # Supprime les tirets au début et à la fin
    name = name.strip('-')
    return name

def download_sprite(pokemon_name, sprite_url, output_dir, backup_url=None, is_back=False):
    """Télécharge le sprite d'un Pokémon avec URL de backup"""
    normalized_name = normalize_name(pokemon_name)
    # Ajouter le suffixe _back pour les sprites de dos
    filename = f"{normalized_name}_back.png" if is_back else f"{normalized_name}.png"
    output_path = Path(output_dir) / filename
    
    if output_path.exists():
        return True
        
    urls_to_try = [sprite_url]
    if backup_url:
        urls_to_try.append(backup_url)

    for url in urls_to_try:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                output_path.parent.mkdir(parents=True, exist_ok=True)
                with open(output_path, 'wb') as f:
                    f.write(response.content)
                print(f"Sprite de {pokemon_name} {'(dos) ' if is_back else ''}téléchargé avec succès depuis {url}")
                return True
        except Exception as e:
            print(f"Erreur lors du téléchargement du sprite de {pokemon_name} depuis {url}: {e}")
            continue
    
    return False

def download_all_sprites():
    """Télécharge tous les sprites des Pokémon de la première génération"""
    base_url = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon"
    backup_base_url = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-i/red-blue"
    back_base_url = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back"
    output_dir = "src/assets/sprites"
    
    # Dictionnaire des Pokémon et leurs numéros
    pokemon_numbers = {
        "Bulbizarre": 1, "Herbizarre": 2, "Florizarre": 3,
        "Salamèche": 4, "Reptincel": 5, "Dracaufeu": 6,
        "Carapuce": 7, "Carabaffe": 8, "Tortank": 9,
        "Chenipan": 10, "Chrysacier": 11, "Papilusion": 12,
        "Aspicot": 13, "Coconfort": 14, "Dardargnan": 15,
        "Roucool": 16, "Roucoups": 17, "Roucarnage": 18,
        "Rattata": 19, "Rattatac": 20,
        "Piafabec": 21, "Rapasdepic": 22,
        "Abo": 23, "Arbok": 24,
        "Pikachu": 25, "Raichu": 26,
        "Sabelette": 27, "Sablaireau": 28,
        "Nidoran♀": 29, "Nidorina": 30, "Nidoqueen": 31,
        "Nidoran♂": 32, "Nidorino": 33, "Nidoking": 34,
        "Mélofée": 35, "Mélodelfe": 36,
        "Goupix": 37, "Feunard": 38,
        "Rondoudou": 39, "Grodoudou": 40
    }
    
    for pokemon_name, number in pokemon_numbers.items():
        # Télécharger le sprite frontal
        sprite_url = f"{base_url}/{number}.png"
        backup_url = f"{backup_base_url}/{number}.png"
        if not download_sprite(pokemon_name, sprite_url, output_dir, backup_url):
            print(f"Échec du téléchargement du sprite frontal de {pokemon_name}")
            
        # Télécharger le sprite de dos
        back_url = f"{back_base_url}/{number}.png"
        if not download_sprite(pokemon_name, back_url, output_dir, None, True):
            print(f"Échec du téléchargement du sprite de dos de {pokemon_name}")

if __name__ == "__main__":
    download_all_sprites() 
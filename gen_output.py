ATTAQUES = {
    "Danse Lames": Attaque("Danse Lames", "Normal", 0, "special", 100),
    "Coupe": Attaque("Coupe", "Normal", 50, "physique", 95),
    "Fouet Lianes": Attaque("Fouet Lianes", "Plante", 45, "physique", 100),
    "Charge": Attaque("Charge", "Normal", 40, "physique", 100),
    "Plaquage": Attaque("Plaquage", "Normal", 85, "physique", 100),
    "Bélier": Attaque("Bélier", "Normal", 90, "physique", 85),
    "Ultimapoing": Attaque("Ultimapoing", "Normal", 80, "physique", 85),
    "Griffe": Attaque("Griffe", "Normal", 40, "physique", 100),
    "Ultimawashi": Attaque("Ultimawashi", "Normal", 120, "physique", 75),
    "Vol": Attaque("Vol", "Vol", 90, "physique", 95),
    "Damoclès": Attaque("Damoclès", "Normal", 120, "physique", 100),
    "Sécrétion": Attaque("Sécrétion", "Insecte", 0, "special", 95),
    "Armure": Attaque("Armure", "Normal", 0, "special", 100),
    "Coupe-Vent": Attaque("Coupe-Vent", "Normal", 80, "special", 100),
    "Tornade": Attaque("Tornade", "Vol", 40, "special", 100),
    "Cyclone": Attaque("Cyclone", "Normal", 0, "special", 100),
    "Ultrason": Attaque("Ultrason", "Normal", 0, "special", 55),
    "Dard-Venin": Attaque("Dard-Venin", "Poison", 15, "physique", 100),
    "Furie": Attaque("Furie", "Normal", 15, "physique", 85),
    "Double Dard": Attaque("Double Dard", "Insecte", 25, "physique", 100),
    "Cru-Ailes": Attaque("Cru-Ailes", "Vol", 60, "physique", 100),
    "Jet de Sable": Attaque("Jet de Sable", "Sol", 0, "special", 100),
    "Mimi-Queue": Attaque("Mimi-Queue", "Normal", 0, "special", 100),
    "Pistolet à O": Attaque("Pistolet à O", "Eau", 40, "special", 100),
    "Ligotage": Attaque("Ligotage", "Normal", 15, "physique", 90),
    "Groz’Yeux": Attaque("Groz’Yeux", "Normal", 0, "special", 100),
    "Jackpot": Attaque("Jackpot", "Normal", 40, "physique", 100),
    "Souplesse": Attaque("Souplesse", "Normal", 80, "physique", 75),
    "Double Pied": Attaque("Double Pied", "Combat", 30, "physique", 100),
    "Empal’Korne": Attaque("Empal’Korne", "Normal", 0, "physique", 30),
    "Koud’Korne": Attaque("Koud’Korne", "Normal", 65, "physique", 100),
    "Écras’Face": Attaque("Écras’Face", "Normal", 40, "physique", 100),
    "Torgnoles": Attaque("Torgnoles", "Normal", 15, "physique", 85),
    "Hurlement": Attaque("Hurlement", "Normal", 0, "special", 100),
    "Flammèche": Attaque("Flammèche", "Feu", 40, "special", 100),
    "Morsure": Attaque("Morsure", "Normal", 60, "physique", 100),
    "Acide": Attaque("Acide", "Poison", 40, "special", 100),
    "Vole-Vie": Attaque("Vole-Vie", "Plante", 20, "special", 100),
    "Entrave": Attaque("Entrave", "Normal", 0, "special", 100),
    "Rafale Psy": Attaque("Rafale Psy", "Psy", 65, "special", 100),
    "Poing Karaté": Attaque("Poing Karaté", "Combat", 50, "physique", 100),
    "Hydrocanon": Attaque("Hydrocanon", "Eau", 110, "special", 80),
    "Sacrifice": Attaque("Sacrifice", "Combat", 80, "physique", 80),
    "Écrasement": Attaque("Écrasement", "Normal", 65, "physique", 100),
    "Coup d’Boule": Attaque("Coup d’Boule", "Normal", 70, "physique", 100),
    "Rugissement": Attaque("Rugissement", "Normal", 0, "special", 100),
    "Sonic Boom": Attaque("Sonic Boom", "Normal", 0, "special", 90),
    "Éclair": Attaque("Éclair", "Électrique", 40, "special", 100),
    "Ultralaser": Attaque("Ultralaser", "Normal", 150, "special", 90),
    "Méga-Sangsue": Attaque("Méga-Sangsue", "Plante", 40, "special", 100),
    "Tonnerre": Attaque("Tonnerre", "Électrique", 90, "special", 100),
    "Fatal-Foudre": Attaque("Fatal-Foudre", "Électrique", 110, "special", 70),
    "Surf": Attaque("Surf", "Eau", 90, "special", 100),
    "Laser Glace": Attaque("Laser Glace", "Glace", 90, "special", 100),
    "Toxik": Attaque("Toxik", "Poison", 0, "special", 90),
    "Psyko": Attaque("Psyko", "Psy", 90, "special", 100),
    "Hypnose": Attaque("Hypnose", "Psy", 0, "special", 60),
    "Étreinte": Attaque("Étreinte", "Normal", 15, "physique", 85),
    "Force Poigne": Attaque("Force Poigne", "Normal", 55, "physique", 100),
    "Guillotine": Attaque("Guillotine", "Normal", 0, "physique", 30),
    "Cage Éclair": Attaque("Cage Éclair", "Électrique", 0, "special", 90),
    "Vampigraine": Attaque("Vampigraine", "Plante", 0, "special", 90),
    "Lance-Soleil": Attaque("Lance-Soleil", "Plante", 120, "special", 100),
    "Poudre Toxik": Attaque("Poudre Toxik", "Poison", 0, "special", 75),
    "Para-Spore": Attaque("Para-Spore", "Plante", 0, "special", 75),
    "Force": Attaque("Force", "Normal", 80, "physique", 100),
    "Mania": Attaque("Mania", "Normal", 120, "physique", 100),
    "Pied Sauté": Attaque("Pied Sauté", "Combat", 100, "physique", 95),
    "Mawashi Geri": Attaque("Mawashi Geri", "Combat", 60, "physique", 85),
    "Poing Comète": Attaque("Poing Comète", "Normal", 18, "physique", 85),
    "Poing Feu": Attaque("Poing Feu", "Feu", 75, "physique", 100),
    "Poing Glace": Attaque("Poing Glace", "Glace", 75, "physique", 100),
    "Poing Éclair": Attaque("Poing Éclair", "Électrique", 75, "physique", 100),
    "Frénésie": Attaque("Frénésie", "Normal", 20, "physique", 100),
    "Copie": Attaque("Copie", "Normal", 0, "special", 100),
    "Trempette": Attaque("Trempette", "Normal", 0, "special", 100),
    "Berceuse": Attaque("Berceuse", "Normal", 0, "special", 55),
    "Morphing": Attaque("Morphing", "Normal", 0, "special", 100),
    "Blizzard": Attaque("Blizzard", "Glace", 110, "special", 70),
    "Brume": Attaque("Brume", "Glace", 0, "special", 100),
}

POKEMONS_DISPONIBLES = {
    "Bulbizarre": {
        "base": Pokemon("Bulbizarre", "Plante", 45, 49, 49, 65, 45, ["Danse Lames", "Coupe", "Fouet Lianes", "Charge", "Plaquage", "Bélier"]),
        "niveau": 50
    },
    "Herbizarre": {
        "base": Pokemon("Herbizarre", "Plante", 60, 62, 63, 80, 60, ["Danse Lames", "Coupe", "Fouet Lianes", "Charge", "Plaquage", "Bélier"]),
        "niveau": 50
    },
    "Florizarre": {
        "base": Pokemon("Florizarre", "Plante", 80, 82, 83, 100, 80, ["Danse Lames", "Coupe", "Fouet Lianes", "Charge", "Plaquage", "Bélier"]),
        "niveau": 50
    },
    "Salamèche": {
        "base": Pokemon("Salamèche", "Feu", 39, 52, 43, 60, 65, ["Ultimapoing", "Griffe", "Danse Lames", "Coupe", "Ultimawashi", "Plaquage"]),
        "niveau": 50
    },
    "Reptincel": {
        "base": Pokemon("Reptincel", "Feu", 58, 64, 58, 80, 80, ["Ultimapoing", "Griffe", "Danse Lames", "Coupe", "Ultimawashi", "Plaquage"]),
        "niveau": 50
    },
    "Dracaufeu": {
        "base": Pokemon("Dracaufeu", "Feu", 78, 84, 78, 109, 100, ["Ultimapoing", "Griffe", "Danse Lames", "Coupe", "Vol", "Ultimawashi"]),
        "niveau": 50
    },
    "Carapuce": {
        "base": Pokemon("Carapuce", "Eau", 44, 48, 65, 50, 43, ["Ultimapoing", "Ultimawashi", "Charge", "Plaquage", "Bélier", "Damoclès"]),
        "niveau": 50
    },
    "Carabaffe": {
        "base": Pokemon("Carabaffe", "Eau", 59, 63, 80, 65, 58, ["Ultimapoing", "Ultimawashi", "Charge", "Plaquage", "Bélier", "Damoclès"]),
        "niveau": 50
    },
    "Tortank": {
        "base": Pokemon("Tortank", "Eau", 79, 83, 100, 85, 78, ["Ultimapoing", "Ultimawashi", "Charge", "Plaquage", "Bélier", "Damoclès"]),
        "niveau": 50
    },
    "Chenipan": {
        "base": Pokemon("Chenipan", "Insecte", 45, 30, 35, 20, 45, ["Charge", "Sécrétion"]),
        "niveau": 50
    },
    "Chrysacier": {
        "base": Pokemon("Chrysacier", "Insecte", 50, 20, 55, 25, 30, ["Armure"]),
        "niveau": 50
    },
    "Papilusion": {
        "base": Pokemon("Papilusion", "Insecte", 60, 45, 50, 90, 70, ["Coupe-Vent", "Tornade", "Cyclone", "Bélier", "Damoclès", "Ultrason"]),
        "niveau": 50
    },
    "Aspicot": {
        "base": Pokemon("Aspicot", "Insecte", 40, 35, 30, 20, 50, ["Dard-Venin", "Sécrétion"]),
        "niveau": 50
    },
    "Coconfort": {
        "base": Pokemon("Coconfort", "Insecte", 45, 25, 50, 25, 35, ["Armure"]),
        "niveau": 50
    },
    "Dardargnan": {
        "base": Pokemon("Dardargnan", "Insecte", 65, 90, 40, 45, 75, ["Danse Lames", "Coupe", "Furie", "Bélier", "Damoclès", "Double Dard"]),
        "niveau": 50
    },
    "Roucool": {
        "base": Pokemon("Roucool", "Normal", 40, 45, 40, 35, 56, ["Coupe-Vent", "Tornade", "Cru-Ailes", "Cyclone", "Vol", "Jet de Sable"]),
        "niveau": 50
    },
    "Roucoups": {
        "base": Pokemon("Roucoups", "Normal", 63, 60, 55, 50, 71, ["Coupe-Vent", "Tornade", "Cru-Ailes", "Cyclone", "Vol", "Jet de Sable"]),
        "niveau": 50
    },
    "Roucarnage": {
        "base": Pokemon("Roucarnage", "Normal", 83, 80, 75, 70, 101, ["Coupe-Vent", "Tornade", "Cru-Ailes", "Cyclone", "Vol", "Jet de Sable"]),
        "niveau": 50
    },
    "Rattata": {
        "base": Pokemon("Rattata", "Normal", 30, 56, 35, 25, 72, ["Charge", "Plaquage", "Bélier", "Damoclès", "Mimi-Queue", "Pistolet à O"]),
        "niveau": 50
    },
    "Rattatac": {
        "base": Pokemon("Rattatac", "Normal", 55, 81, 60, 50, 97, ["Charge", "Plaquage", "Bélier", "Damoclès", "Mimi-Queue", "Pistolet à O"]),
        "niveau": 50
    },
    "Piafabec": {
        "base": Pokemon("Piafabec", "Normal", 40, 60, 30, 31, 70, ["Coupe-Vent", "Cyclone", "Vol", "Furie", "Bélier", "Damoclès"]),
        "niveau": 50
    },
    "Rapasdepic": {
        "base": Pokemon("Rapasdepic", "Normal", 65, 90, 65, 61, 100, ["Coupe-Vent", "Cyclone", "Vol", "Furie", "Bélier", "Damoclès"]),
        "niveau": 50
    },
    "Abo": {
        "base": Pokemon("Abo", "Poison", 35, 60, 44, 40, 55, ["Plaquage", "Ligotage", "Bélier", "Damoclès", "Dard-Venin", "Groz’Yeux"]),
        "niveau": 50
    },
    "Arbok": {
        "base": Pokemon("Arbok", "Poison", 60, 95, 69, 65, 80, ["Plaquage", "Ligotage", "Bélier", "Damoclès", "Dard-Venin", "Groz’Yeux"]),
        "niveau": 50
    },
    "Pikachu": {
        "base": Pokemon("Pikachu", "Électrique", 35, 55, 40, 50, 90, ["Ultimapoing", "Jackpot", "Souplesse", "Ultimawashi", "Plaquage", "Bélier"]),
        "niveau": 50
    },
    "Raichu": {
        "base": Pokemon("Raichu", "Électrique", 60, 90, 55, 90, 110, ["Ultimapoing", "Jackpot", "Ultimawashi", "Plaquage", "Bélier", "Damoclès"]),
        "niveau": 50
    },
    "Sabelette": {
        "base": Pokemon("Sabelette", "Sol", 50, 75, 85, 20, 40, ["Griffe", "Danse Lames", "Coupe", "Jet de Sable", "Plaquage", "Bélier"]),
        "niveau": 50
    },
    "Sablaireau": {
        "base": Pokemon("Sablaireau", "Sol", 75, 100, 110, 45, 65, ["Griffe", "Danse Lames", "Coupe", "Jet de Sable", "Plaquage", "Bélier"]),
        "niveau": 50
    },
    "Nidoran-f": {
        "base": Pokemon("Nidoran-f", "Poison", 55, 47, 52, 40, 41, ["Griffe", "Double Pied", "Charge", "Plaquage", "Bélier", "Damoclès"]),
        "niveau": 50
    },
    "Nidorina": {
        "base": Pokemon("Nidorina", "Poison", 70, 62, 67, 55, 56, ["Griffe", "Double Pied", "Empal’Korne", "Charge", "Plaquage", "Bélier"]),
        "niveau": 50
    },
    "Nidoqueen": {
        "base": Pokemon("Nidoqueen", "Poison", 90, 92, 87, 75, 76, ["Ultimapoing", "Jackpot", "Griffe", "Double Pied", "Ultimawashi", "Empal’Korne"]),
        "niveau": 50
    },
    "Nidoran-m": {
        "base": Pokemon("Nidoran-m", "Poison", 46, 57, 40, 40, 50, ["Double Pied", "Koud’Korne", "Furie", "Empal’Korne", "Charge", "Plaquage"]),
        "niveau": 50
    },
    "Nidorino": {
        "base": Pokemon("Nidorino", "Poison", 61, 72, 57, 55, 65, ["Double Pied", "Koud’Korne", "Furie", "Empal’Korne", "Charge", "Plaquage"]),
        "niveau": 50
    },
    "Nidoking": {
        "base": Pokemon("Nidoking", "Poison", 81, 102, 77, 85, 85, ["Ultimapoing", "Jackpot", "Double Pied", "Ultimawashi", "Koud’Korne", "Empal’Korne"]),
        "niveau": 50
    },
    "Mélofée": {
        "base": Pokemon("Mélofée", "Normal", 70, 45, 48, 60, 35, ["Écras’Face", "Torgnoles", "Ultimapoing", "Ultimawashi", "Plaquage", "Bélier"]),
        "niveau": 50
    },
    "Mélodelfe": {
        "base": Pokemon("Mélodelfe", "Normal", 95, 70, 73, 95, 60, ["Torgnoles", "Ultimapoing", "Ultimawashi", "Plaquage", "Bélier", "Damoclès"]),
        "niveau": 50
    },
    "Goupix": {
        "base": Pokemon("Goupix", "Feu", 38, 41, 40, 50, 65, ["Plaquage", "Bélier", "Damoclès", "Mimi-Queue", "Hurlement", "Flammèche"]),
        "niveau": 50
    },
    "Feunard": {
        "base": Pokemon("Feunard", "Feu", 73, 76, 75, 81, 100, ["Plaquage", "Bélier", "Damoclès", "Mimi-Queue", "Hurlement", "Flammèche"]),
        "niveau": 50
    },
    "Rondoudou": {
        "base": Pokemon("Rondoudou", "Normal", 115, 45, 20, 45, 20, ["Écras’Face", "Torgnoles", "Ultimapoing", "Ultimawashi", "Plaquage", "Bélier"]),
        "niveau": 50
    },
    "Grodoudou": {
        "base": Pokemon("Grodoudou", "Normal", 140, 70, 45, 85, 45, ["Torgnoles", "Ultimapoing", "Ultimawashi", "Plaquage", "Bélier", "Damoclès"]),
        "niveau": 50
    },
    "Nosferapti": {
        "base": Pokemon("Nosferapti", "Poison", 40, 45, 35, 30, 55, ["Coupe-Vent", "Cru-Ailes", "Cyclone", "Bélier", "Damoclès", "Morsure"]),
        "niveau": 50
    },
    "Nosferalto": {
        "base": Pokemon("Nosferalto", "Poison", 75, 80, 70, 65, 90, ["Coupe-Vent", "Cru-Ailes", "Cyclone", "Bélier", "Damoclès", "Morsure"]),
        "niveau": 50
    },
    "Mystherbe": {
        "base": Pokemon("Mystherbe", "Plante", 45, 50, 55, 75, 30, ["Danse Lames", "Coupe", "Bélier", "Damoclès", "Acide", "Vole-Vie"]),
        "niveau": 50
    },
    "Ortide": {
        "base": Pokemon("Ortide", "Plante", 60, 65, 70, 85, 40, ["Danse Lames", "Coupe", "Bélier", "Damoclès", "Acide", "Vole-Vie"]),
        "niveau": 50
    },
    "Rafflesia": {
        "base": Pokemon("Rafflesia", "Plante", 75, 80, 85, 110, 50, ["Danse Lames", "Coupe", "Plaquage", "Bélier", "Damoclès", "Acide"]),
        "niveau": 50
    },
    "Paras": {
        "base": Pokemon("Paras", "Insecte", 35, 70, 55, 45, 25, ["Griffe", "Danse Lames", "Coupe", "Plaquage", "Bélier", "Damoclès"]),
        "niveau": 50
    },
    "Parasect": {
        "base": Pokemon("Parasect", "Insecte", 60, 95, 80, 60, 30, ["Griffe", "Danse Lames", "Coupe", "Plaquage", "Bélier", "Damoclès"]),
        "niveau": 50
    },
    "Mimitoss": {
        "base": Pokemon("Mimitoss", "Insecte", 60, 55, 50, 40, 45, ["Charge", "Bélier", "Damoclès", "Ultrason", "Entrave", "Rafale Psy"]),
        "niveau": 50
    },
    "Aéromite": {
        "base": Pokemon("Aéromite", "Insecte", 70, 65, 60, 90, 90, ["Coupe-Vent", "Cyclone", "Charge", "Bélier", "Damoclès", "Ultrason"]),
        "niveau": 50
    },
    "Taupiqueur": {
        "base": Pokemon("Taupiqueur", "Sol", 10, 55, 25, 35, 95, ["Griffe", "Coupe", "Jet de Sable", "Plaquage", "Bélier", "Damoclès"]),
        "niveau": 50
    },
    "Triopikeur": {
        "base": Pokemon("Triopikeur", "Sol", 35, 100, 50, 50, 120, ["Griffe", "Coupe", "Jet de Sable", "Plaquage", "Bélier", "Damoclès"]),
        "niveau": 50
    },
    "Miaouss": {
        "base": Pokemon("Miaouss", "Normal", 40, 45, 35, 40, 90, ["Jackpot", "Griffe", "Plaquage", "Bélier", "Damoclès", "Morsure"]),
        "niveau": 50
    },
    "Persian": {
        "base": Pokemon("Persian", "Normal", 65, 70, 60, 65, 115, ["Jackpot", "Griffe", "Plaquage", "Bélier", "Damoclès", "Morsure"]),
        "niveau": 50
    },
    "Psykokwak": {
        "base": Pokemon("Psykokwak", "Eau", 50, 52, 48, 65, 55, ["Ultimapoing", "Jackpot", "Griffe", "Ultimawashi", "Plaquage", "Bélier"]),
        "niveau": 50
    },
    "Akwakwak": {
        "base": Pokemon("Akwakwak", "Eau", 80, 82, 78, 95, 85, ["Ultimapoing", "Jackpot", "Griffe", "Ultimawashi", "Plaquage", "Bélier"]),
        "niveau": 50
    },
    "Férosinge": {
        "base": Pokemon("Férosinge", "Combat", 40, 80, 35, 35, 70, ["Poing Karaté", "Ultimapoing", "Jackpot", "Griffe", "Ultimawashi", "Plaquage"]),
        "niveau": 50
    },
    "Colossinge": {
        "base": Pokemon("Colossinge", "Combat", 65, 105, 60, 60, 95, ["Poing Karaté", "Ultimapoing", "Jackpot", "Griffe", "Ultimawashi", "Plaquage"]),
        "niveau": 50
    },
    "Caninos": {
        "base": Pokemon("Caninos", "Feu", 55, 70, 45, 70, 60, ["Plaquage", "Bélier", "Damoclès", "Groz’Yeux", "Morsure", "Hurlement"]),
        "niveau": 50
    },
    "Arcanin": {
        "base": Pokemon("Arcanin", "Feu", 90, 110, 80, 100, 95, ["Plaquage", "Bélier", "Damoclès", "Groz’Yeux", "Hurlement", "Flammèche"]),
        "niveau": 50
    },
    "Ptitard": {
        "base": Pokemon("Ptitard", "Eau", 40, 50, 40, 40, 90, ["Torgnoles", "Plaquage", "Bélier", "Damoclès", "Pistolet à O", "Hydrocanon"]),
        "niveau": 50
    },
    "Têtarte": {
        "base": Pokemon("Têtarte", "Eau", 65, 65, 65, 50, 90, ["Torgnoles", "Ultimapoing", "Ultimawashi", "Plaquage", "Bélier", "Damoclès"]),
        "niveau": 50
    },
    "Tartard": {
        "base": Pokemon("Tartard", "Eau", 90, 95, 95, 70, 70, ["Torgnoles", "Ultimapoing", "Ultimawashi", "Plaquage", "Bélier", "Damoclès"]),
        "niveau": 50
    },
    "Abra": {
        "base": Pokemon("Abra", "Psy", 25, 20, 15, 105, 90, ["Ultimapoing", "Ultimawashi", "Plaquage", "Bélier", "Damoclès", "Sacrifice"]),
        "niveau": 50
    },
    "Kadabra": {
        "base": Pokemon("Kadabra", "Psy", 40, 35, 30, 120, 105, ["Ultimapoing", "Ultimawashi", "Plaquage", "Bélier", "Damoclès", "Entrave"]),
        "niveau": 50
    },
    "Alakazam": {
        "base": Pokemon("Alakazam", "Psy", 55, 50, 45, 135, 120, ["Ultimapoing", "Ultimawashi", "Plaquage", "Bélier", "Damoclès", "Entrave"]),
        "niveau": 50
    },
    "Machoc": {
        "base": Pokemon("Machoc", "Combat", 70, 80, 50, 35, 35, ["Poing Karaté", "Ultimapoing", "Ultimawashi", "Plaquage", "Bélier", "Damoclès"]),
        "niveau": 50
    },
    "Machopeur": {
        "base": Pokemon("Machopeur", "Combat", 80, 100, 70, 50, 45, ["Poing Karaté", "Ultimapoing", "Ultimawashi", "Plaquage", "Bélier", "Damoclès"]),
        "niveau": 50
    },
    "Mackogneur": {
        "base": Pokemon("Mackogneur", "Combat", 90, 130, 80, 65, 55, ["Poing Karaté", "Ultimapoing", "Ultimawashi", "Plaquage", "Bélier", "Damoclès"]),
        "niveau": 50
    },
    "Chétiflor": {
        "base": Pokemon("Chétiflor", "Plante", 50, 75, 35, 70, 40, ["Danse Lames", "Coupe", "Souplesse", "Fouet Lianes", "Ligotage", "Bélier"]),
        "niveau": 50
    },
    "Boustiflor": {
        "base": Pokemon("Boustiflor", "Plante", 65, 90, 50, 85, 55, ["Danse Lames", "Coupe", "Souplesse", "Fouet Lianes", "Ligotage", "Bélier"]),
        "niveau": 50
    },
    "Empiflor": {
        "base": Pokemon("Empiflor", "Plante", 80, 105, 65, 100, 70, ["Danse Lames", "Coupe", "Plaquage", "Ligotage", "Bélier", "Damoclès"]),
        "niveau": 50
    },
    "Tentacool": {
        "base": Pokemon("Tentacool", "Eau", 40, 40, 35, 50, 70, ["Danse Lames", "Coupe", "Ligotage", "Bélier", "Damoclès", "Dard-Venin"]),
        "niveau": 50
    },
    "Tentacruel": {
        "base": Pokemon("Tentacruel", "Eau", 80, 70, 65, 80, 100, ["Danse Lames", "Coupe", "Ligotage", "Bélier", "Damoclès", "Dard-Venin"]),
        "niveau": 50
    },
    "Racaillou": {
        "base": Pokemon("Racaillou", "Roche", 40, 80, 100, 30, 20, ["Ultimapoing", "Charge", "Plaquage", "Bélier", "Damoclès", "Sacrifice"]),
        "niveau": 50
    },
    "Gravalanch": {
        "base": Pokemon("Gravalanch", "Roche", 55, 95, 115, 45, 35, ["Ultimapoing", "Charge", "Plaquage", "Bélier", "Damoclès", "Sacrifice"]),
        "niveau": 50
    },
    "Grolem": {
        "base": Pokemon("Grolem", "Roche", 80, 120, 130, 55, 45, ["Ultimapoing", "Ultimawashi", "Charge", "Plaquage", "Bélier", "Damoclès"]),
        "niveau": 50
    },
    "Ponyta": {
        "base": Pokemon("Ponyta", "Feu", 50, 85, 55, 65, 90, ["Écrasement", "Empal’Korne", "Plaquage", "Bélier", "Damoclès", "Mimi-Queue"]),
        "niveau": 50
    },
    "Galopa": {
        "base": Pokemon("Galopa", "Feu", 65, 100, 70, 80, 105, ["Écrasement", "Empal’Korne", "Plaquage", "Bélier", "Damoclès", "Mimi-Queue"]),
        "niveau": 50
    },
    "Ramoloss": {
        "base": Pokemon("Ramoloss", "Eau", 90, 65, 65, 40, 15, ["Jackpot", "Coup d’Boule", "Plaquage", "Bélier", "Damoclès", "Rugissement"]),
        "niveau": 50
    },
    "Flagadoss": {
        "base": Pokemon("Flagadoss", "Eau", 95, 75, 110, 100, 30, ["Ultimapoing", "Jackpot", "Ultimawashi", "Coup d’Boule", "Plaquage", "Bélier"]),
        "niveau": 50
    },
    "Magnéti": {
        "base": Pokemon("Magnéti", "Électrique", 25, 35, 70, 95, 45, ["Charge", "Bélier", "Damoclès", "Ultrason", "Sonic Boom", "Éclair"]),
        "niveau": 50
    },
    "Magnéton": {
        "base": Pokemon("Magnéton", "Électrique", 50, 60, 95, 120, 70, ["Charge", "Bélier", "Damoclès", "Ultrason", "Sonic Boom", "Ultralaser"]),
        "niveau": 50
    },
    "Canarticho": {
        "base": Pokemon("Canarticho", "Normal", 52, 90, 55, 58, 60, ["Coupe-Vent", "Danse Lames", "Coupe", "Cyclone", "Vol", "Jet de Sable"]),
        "niveau": 50
    },
    "Doduo": {
        "base": Pokemon("Doduo", "Normal", 35, 85, 45, 35, 75, ["Cyclone", "Vol", "Furie", "Plaquage", "Bélier", "Damoclès"]),
        "niveau": 50
    },
    "Dodrio": {
        "base": Pokemon("Dodrio", "Normal", 60, 110, 70, 60, 110, ["Cyclone", "Vol", "Furie", "Plaquage", "Bélier", "Damoclès"]),
        "niveau": 50
    },
    "Otaria": {
        "base": Pokemon("Otaria", "Eau", 65, 45, 55, 45, 45, ["Jackpot", "Coup d’Boule", "Empal’Korne", "Plaquage", "Bélier", "Damoclès"]),
        "niveau": 50
    },
    "Lamantine": {
        "base": Pokemon("Lamantine", "Eau", 90, 70, 80, 70, 70, ["Jackpot", "Coup d’Boule", "Empal’Korne", "Plaquage", "Bélier", "Damoclès"]),
        "niveau": 50
    },
    "Tadmorv": {
        "base": Pokemon("Tadmorv", "Poison", 80, 80, 50, 40, 25, ["Écras’Face", "Plaquage", "Entrave", "Méga-Sangsue", "Tonnerre", "Fatal-Foudre"]),
        "niveau": 50
    },
    "Grotadmorv": {
        "base": Pokemon("Grotadmorv", "Poison", 105, 105, 75, 65, 50, ["Écras’Face", "Plaquage", "Entrave", "Ultralaser", "Méga-Sangsue", "Tonnerre"]),
        "niveau": 50
    },
    "Kokiyas": {
        "base": Pokemon("Kokiyas", "Eau", 30, 65, 100, 45, 40, ["Charge", "Bélier", "Damoclès", "Groz’Yeux", "Ultrason", "Pistolet à O"]),
        "niveau": 50
    },
    "Crustabri": {
        "base": Pokemon("Crustabri", "Eau", 50, 95, 180, 85, 70, ["Bélier", "Damoclès", "Ultrason", "Pistolet à O", "Surf", "Laser Glace"]),
        "niveau": 50
    },
    "Fantominus": {
        "base": Pokemon("Fantominus", "Spectre", 30, 35, 30, 100, 80, ["Méga-Sangsue", "Tonnerre", "Fatal-Foudre", "Toxik", "Psyko", "Hypnose"]),
        "niveau": 50
    },
    "Spectrum": {
        "base": Pokemon("Spectrum", "Spectre", 45, 50, 45, 115, 95, ["Méga-Sangsue", "Tonnerre", "Fatal-Foudre", "Toxik", "Psyko", "Hypnose"]),
        "niveau": 50
    },
    "Ectoplasma": {
        "base": Pokemon("Ectoplasma", "Spectre", 60, 65, 60, 130, 110, ["Ultimapoing", "Ultimawashi", "Plaquage", "Bélier", "Damoclès", "Ultralaser"]),
        "niveau": 50
    },
    "Onix": {
        "base": Pokemon("Onix", "Roche", 35, 45, 160, 30, 70, ["Étreinte", "Souplesse", "Charge", "Plaquage", "Bélier", "Damoclès"]),
        "niveau": 50
    },
    "Soporifik": {
        "base": Pokemon("Soporifik", "Psy", 60, 48, 45, 43, 42, ["Écras’Face", "Ultimapoing", "Ultimawashi", "Coup d’Boule", "Plaquage", "Bélier"]),
        "niveau": 50
    },
    "Hypnomade": {
        "base": Pokemon("Hypnomade", "Psy", 85, 73, 70, 73, 67, ["Écras’Face", "Ultimapoing", "Ultimawashi", "Coup d’Boule", "Plaquage", "Bélier"]),
        "niveau": 50
    },
    "Krabby": {
        "base": Pokemon("Krabby", "Eau", 30, 105, 90, 25, 50, ["Force Poigne", "Guillotine", "Danse Lames", "Coupe", "Écrasement", "Plaquage"]),
        "niveau": 50
    },
    "Krabboss": {
        "base": Pokemon("Krabboss", "Eau", 55, 130, 115, 50, 75, ["Force Poigne", "Guillotine", "Danse Lames", "Coupe", "Écrasement", "Plaquage"]),
        "niveau": 50
    },
    "Voltorbe": {
        "base": Pokemon("Voltorbe", "Électrique", 40, 30, 50, 55, 100, ["Charge", "Bélier", "Sonic Boom", "Tonnerre", "Cage Éclair", "Fatal-Foudre"]),
        "niveau": 50
    },
    "Électrode": {
        "base": Pokemon("Électrode", "Électrique", 60, 50, 70, 80, 150, ["Charge", "Bélier", "Sonic Boom", "Ultralaser", "Tonnerre", "Cage Éclair"]),
        "niveau": 50
    },
    "Noeunoeuf": {
        "base": Pokemon("Noeunoeuf", "Plante", 60, 40, 80, 60, 40, ["Bélier", "Damoclès", "Vampigraine", "Lance-Soleil", "Poudre Toxik", "Para-Spore"]),
        "niveau": 50
    },
    "Noadkoko": {
        "base": Pokemon("Noadkoko", "Plante", 95, 95, 85, 125, 55, ["Écrasement", "Bélier", "Damoclès", "Ultralaser", "Force", "Méga-Sangsue"]),
        "niveau": 50
    },
    "Osselait": {
        "base": Pokemon("Osselait", "Sol", 50, 50, 95, 40, 35, ["Ultimapoing", "Ultimawashi", "Coup d’Boule", "Plaquage", "Bélier", "Mania"]),
        "niveau": 50
    },
    "Ossatueur": {
        "base": Pokemon("Ossatueur", "Sol", 60, 80, 110, 50, 45, ["Ultimapoing", "Ultimawashi", "Coup d’Boule", "Plaquage", "Bélier", "Mania"]),
        "niveau": 50
    },
    "Kicklee": {
        "base": Pokemon("Kicklee", "Combat", 50, 120, 53, 35, 87, ["Ultimapoing", "Double Pied", "Ultimawashi", "Pied Sauté", "Mawashi Geri", "Plaquage"]),
        "niveau": 50
    },
    "Tygnon": {
        "base": Pokemon("Tygnon", "Combat", 50, 105, 79, 35, 76, ["Poing Comète", "Ultimapoing", "Poing Feu", "Poing Glace", "Poing Éclair", "Ultimawashi"]),
        "niveau": 50
    },
    "Excelangue": {
        "base": Pokemon("Excelangue", "Normal", 90, 55, 75, 60, 30, ["Ultimapoing", "Danse Lames", "Coupe", "Souplesse", "Écrasement", "Ultimawashi"]),
        "niveau": 50
    },
    "Smogo": {
        "base": Pokemon("Smogo", "Poison", 40, 65, 95, 60, 35, ["Charge", "Tonnerre", "Fatal-Foudre", "Toxik", "Frénésie", "Copie"]),
        "niveau": 50
    },
    "Smogogo": {
        "base": Pokemon("Smogogo", "Poison", 65, 90, 120, 85, 60, ["Charge", "Ultralaser", "Tonnerre", "Fatal-Foudre", "Toxik", "Frénésie"]),
        "niveau": 50
    },
    "Rhinocorne": {
        "base": Pokemon("Rhinocorne", "Sol", 80, 85, 95, 30, 25, ["Écrasement", "Koud’Korne", "Furie", "Empal’Korne", "Plaquage", "Bélier"]),
        "niveau": 50
    },
    "Rhinoféros": {
        "base": Pokemon("Rhinoféros", "Sol", 105, 130, 120, 45, 40, ["Ultimapoing", "Jackpot", "Écrasement", "Ultimawashi", "Koud’Korne", "Furie"]),
        "niveau": 50
    },
    "Leveinard": {
        "base": Pokemon("Leveinard", "Normal", 250, 5, 5, 35, 50, ["Écras’Face", "Torgnoles", "Ultimapoing", "Ultimawashi", "Plaquage", "Bélier"]),
        "niveau": 50
    },
    "Saquedeneu": {
        "base": Pokemon("Saquedeneu", "Plante", 65, 55, 115, 100, 60, ["Danse Lames", "Coupe", "Étreinte", "Souplesse", "Fouet Lianes", "Plaquage"]),
        "niveau": 50
    },
    "Kangourex": {
        "base": Pokemon("Kangourex", "Normal", 105, 95, 80, 40, 90, ["Poing Comète", "Ultimapoing", "Ultimawashi", "Plaquage", "Bélier", "Damoclès"]),
        "niveau": 50
    },
    "Hypotrempe": {
        "base": Pokemon("Hypotrempe", "Eau", 30, 40, 70, 70, 60, ["Bélier", "Damoclès", "Groz’Yeux", "Pistolet à O", "Hydrocanon", "Surf"]),
        "niveau": 50
    },
    "Hypocéan": {
        "base": Pokemon("Hypocéan", "Eau", 55, 65, 95, 95, 85, ["Bélier", "Damoclès", "Groz’Yeux", "Pistolet à O", "Hydrocanon", "Surf"]),
        "niveau": 50
    },
    "Poissirène": {
        "base": Pokemon("Poissirène", "Eau", 45, 67, 60, 35, 63, ["Koud’Korne", "Furie", "Empal’Korne", "Bélier", "Damoclès", "Mimi-Queue"]),
        "niveau": 50
    },
    "Poissoroy": {
        "base": Pokemon("Poissoroy", "Eau", 80, 92, 65, 65, 68, ["Koud’Korne", "Furie", "Empal’Korne", "Bélier", "Damoclès", "Mimi-Queue"]),
        "niveau": 50
    },
    "Stari": {
        "base": Pokemon("Stari", "Eau", 30, 45, 55, 70, 85, ["Charge", "Bélier", "Damoclès", "Pistolet à O", "Hydrocanon", "Surf"]),
        "niveau": 50
    },
    "Staross": {
        "base": Pokemon("Staross", "Eau", 60, 75, 85, 100, 115, ["Charge", "Bélier", "Damoclès", "Pistolet à O", "Surf", "Laser Glace"]),
        "niveau": 50
    },
    "M. Mime": {
        "base": Pokemon("M. Mime", "Psy", 40, 45, 65, 100, 90, ["Torgnoles", "Ultimapoing", "Ultimawashi", "Plaquage", "Bélier", "Damoclès"]),
        "niveau": 50
    },
    "Insécateur": {
        "base": Pokemon("Insécateur", "Insecte", 70, 110, 80, 55, 105, ["Danse Lames", "Coupe", "Cru-Ailes", "Bélier", "Damoclès", "Groz’Yeux"]),
        "niveau": 50
    },
    "Lippoutou": {
        "base": Pokemon("Lippoutou", "Glace", 65, 50, 35, 115, 95, ["Écras’Face", "Torgnoles", "Ultimapoing", "Poing Glace", "Ultimawashi", "Plaquage"]),
        "niveau": 50
    },
    "Élektek": {
        "base": Pokemon("Élektek", "Électrique", 65, 83, 57, 95, 105, ["Ultimapoing", "Poing Éclair", "Ultimawashi", "Plaquage", "Bélier", "Damoclès"]),
        "niveau": 50
    },
    "Magmar": {
        "base": Pokemon("Magmar", "Feu", 65, 95, 57, 100, 93, ["Ultimapoing", "Poing Feu", "Ultimawashi", "Plaquage", "Bélier", "Damoclès"]),
        "niveau": 50
    },
    "Scarabrute": {
        "base": Pokemon("Scarabrute", "Insecte", 65, 125, 100, 55, 85, ["Force Poigne", "Guillotine", "Danse Lames", "Coupe", "Étreinte", "Plaquage"]),
        "niveau": 50
    },
    "Tauros": {
        "base": Pokemon("Tauros", "Normal", 75, 100, 95, 40, 110, ["Écrasement", "Empal’Korne", "Charge", "Plaquage", "Bélier", "Damoclès"]),
        "niveau": 50
    },
    "Magicarpe": {
        "base": Pokemon("Magicarpe", "Eau", 20, 10, 55, 15, 80, ["Charge", "Trempette"]),
        "niveau": 50
    },
    "Léviator": {
        "base": Pokemon("Léviator", "Eau", 95, 125, 79, 60, 81, ["Charge", "Plaquage", "Bélier", "Damoclès", "Groz’Yeux", "Morsure"]),
        "niveau": 50
    },
    "Lokhlass": {
        "base": Pokemon("Lokhlass", "Eau", 130, 85, 80, 85, 60, ["Empal’Korne", "Plaquage", "Bélier", "Damoclès", "Rugissement", "Berceuse"]),
        "niveau": 50
    },
    "Métamorph": {
        "base": Pokemon("Métamorph", "Normal", 48, 48, 48, 48, 48, ["Morphing"]),
        "niveau": 50
    },
    "Évoli": {
        "base": Pokemon("Évoli", "Normal", 55, 55, 50, 45, 55, ["Jet de Sable", "Charge", "Plaquage", "Bélier", "Damoclès", "Mimi-Queue"]),
        "niveau": 50
    },
    "Aquali": {
        "base": Pokemon("Aquali", "Eau", 130, 65, 60, 110, 65, ["Jet de Sable", "Charge", "Plaquage", "Bélier", "Damoclès", "Mimi-Queue"]),
        "niveau": 50
    },
    "Voltali": {
        "base": Pokemon("Voltali", "Électrique", 65, 65, 60, 110, 130, ["Double Pied", "Jet de Sable", "Charge", "Plaquage", "Bélier", "Damoclès"]),
        "niveau": 50
    },
    "Pyroli": {
        "base": Pokemon("Pyroli", "Feu", 65, 130, 60, 95, 65, ["Jet de Sable", "Charge", "Plaquage", "Bélier", "Damoclès", "Mimi-Queue"]),
        "niveau": 50
    },
    "Porygon": {
        "base": Pokemon("Porygon", "Normal", 65, 60, 70, 85, 40, ["Charge", "Bélier", "Damoclès", "Laser Glace", "Blizzard", "Rafale Psy"]),
        "niveau": 50
    },
    "Amonita": {
        "base": Pokemon("Amonita", "Roche", 35, 40, 100, 90, 35, ["Koud’Korne", "Plaquage", "Bélier", "Damoclès", "Groz’Yeux", "Pistolet à O"]),
        "niveau": 50
    },
    "Amonistar": {
        "base": Pokemon("Amonistar", "Roche", 70, 60, 125, 115, 55, ["Koud’Korne", "Empal’Korne", "Plaquage", "Bélier", "Damoclès", "Groz’Yeux"]),
        "niveau": 50
    },
    "Kabuto": {
        "base": Pokemon("Kabuto", "Roche", 30, 80, 90, 55, 55, ["Griffe", "Plaquage", "Bélier", "Damoclès", "Groz’Yeux", "Pistolet à O"]),
        "niveau": 50
    },
    "Kabutops": {
        "base": Pokemon("Kabutops", "Roche", 60, 115, 105, 65, 80, ["Griffe", "Coupe-Vent", "Danse Lames", "Coupe", "Ultimawashi", "Plaquage"]),
        "niveau": 50
    },
    "Ptéra": {
        "base": Pokemon("Ptéra", "Roche", 80, 105, 65, 60, 130, ["Coupe-Vent", "Cru-Ailes", "Cyclone", "Vol", "Bélier", "Damoclès"]),
        "niveau": 50
    },
    "Ronflex": {
        "base": Pokemon("Ronflex", "Normal", 160, 110, 65, 65, 30, ["Ultimapoing", "Jackpot", "Ultimawashi", "Coup d’Boule", "Plaquage", "Bélier"]),
        "niveau": 50
    },
    "Artikodin": {
        "base": Pokemon("Artikodin", "Glace", 90, 85, 100, 95, 85, ["Coupe-Vent", "Cyclone", "Vol", "Bélier", "Damoclès", "Brume"]),
        "niveau": 50
    },
    "Électhor": {
        "base": Pokemon("Électhor", "Électrique", 90, 90, 85, 125, 100, ["Coupe-Vent", "Cyclone", "Vol", "Bélier", "Damoclès", "Ultralaser"]),
        "niveau": 50
    },
    "Sulfura": {
        "base": Pokemon("Sulfura", "Feu", 90, 100, 90, 125, 90, ["Coupe-Vent", "Cyclone", "Vol", "Bélier", "Damoclès", "Groz’Yeux"]),
        "niveau": 50
    },
    "Minidraco": {
        "base": Pokemon("Minidraco", "Dragon", 41, 64, 45, 50, 50, ["Souplesse", "Plaquage", "Ligotage", "Bélier", "Damoclès", "Groz’Yeux"]),
        "niveau": 50
    },
    "Draco": {
        "base": Pokemon("Draco", "Dragon", 61, 84, 65, 70, 70, ["Souplesse", "Empal’Korne", "Plaquage", "Ligotage", "Bélier", "Damoclès"]),
        "niveau": 50
    },
    "Dracolosse": {
        "base": Pokemon("Dracolosse", "Dragon", 91, 134, 95, 100, 80, ["Coupe-Vent", "Souplesse", "Empal’Korne", "Plaquage", "Ligotage", "Bélier"]),
        "niveau": 50
    },
    "Mewtwo": {
        "base": Pokemon("Mewtwo", "Psy", 106, 110, 90, 154, 130, ["Ultimapoing", "Jackpot", "Ultimawashi", "Plaquage", "Bélier", "Damoclès"]),
        "niveau": 50
    },
    "Mew": {
        "base": Pokemon("Mew", "Psy", 100, 100, 100, 100, 100, ["Écras’Face", "Ultimapoing", "Jackpot", "Coupe-Vent", "Danse Lames", "Coupe"]),
        "niveau": 50
    },
}

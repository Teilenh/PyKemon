# Table des types de la première génération
TABLE_TYPES = {
    "Normal": {
        "super_efficace": [],
        "peu_efficace": ["Combat"],
        "inefficace": ["Spectre"]
    },
    "Feu": {
        "super_efficace": ["Plante", "Glace", "Insecte"],
        "peu_efficace": ["Feu", "Eau", "Roche", "Dragon"],
        "inefficace": []
    },
    "Eau": {
        "super_efficace": ["Feu", "Sol", "Roche"],
        "peu_efficace": ["Eau", "Plante", "Dragon"],
        "inefficace": []
    },
    "Électrique": {
        "super_efficace": ["Eau", "Vol"],
        "peu_efficace": ["Électrique", "Plante", "Dragon"],
        "inefficace": ["Sol"]
    },
    "Plante": {
        "super_efficace": ["Eau", "Sol", "Roche"],
        "peu_efficace": ["Feu", "Plante", "Poison", "Vol", "Insecte", "Dragon"],
        "inefficace": []
    },
    "Glace": {
        "super_efficace": ["Plante", "Sol", "Vol", "Dragon"],
        "peu_efficace": ["Eau", "Glace"],
        "inefficace": []
    },
    "Combat": {
        "super_efficace": ["Normal", "Glace", "Roche"],
        "peu_efficace": ["Poison", "Vol", "Psy", "Insecte"],
        "inefficace": ["Spectre"]
    },
    "Poison": {
        "super_efficace": ["Plante", "Insecte"],
        "peu_efficace": ["Poison", "Sol", "Roche", "Spectre"],
        "inefficace": []
    },
    "Sol": {
        "super_efficace": ["Feu", "Électrique", "Poison", "Roche"],
        "peu_efficace": ["Plante", "Insecte"],
        "inefficace": ["Vol"]
    },
    "Vol": {
        "super_efficace": ["Plante", "Combat", "Insecte"],
        "peu_efficace": ["Électrique", "Roche"],
        "inefficace": []
    },
    "Psy": {
        "super_efficace": ["Combat", "Poison"],
        "peu_efficace": ["Psy"],
        "inefficace": []
    },
    "Insecte": {
        "super_efficace": ["Plante", "Psy", "Poison"],
        "peu_efficace": ["Feu", "Combat", "Vol", "Spectre"],
        "inefficace": []
    },
    "Roche": {
        "super_efficace": ["Feu", "Glace", "Vol", "Insecte"],
        "peu_efficace": ["Combat", "Sol"],
        "inefficace": []
    },
    "Spectre": {
        "super_efficace": ["Spectre"],
        "peu_efficace": [],
        "inefficace": ["Normal", "Psy"]
    },
    "Dragon": {
        "super_efficace": ["Dragon"],
        "peu_efficace": [],
        "inefficace": []
    }
}

def get_multiplicateur(type_attaque, type_defenseur):
    """Calcule le multiplicateur de dégâts selon les types"""
    if type_attaque not in TABLE_TYPES or type_defenseur not in TABLE_TYPES:
        return 1.0

    if type_defenseur in TABLE_TYPES[type_attaque]["super_efficace"]:
        return 2.0
    elif type_defenseur in TABLE_TYPES[type_attaque]["peu_efficace"]:
        return 0.5
    elif type_defenseur in TABLE_TYPES[type_attaque]["inefficace"]:
        return 0.0
    
    return 1.0

class Attaque:
    def __init__(self, nom, type_, puissance, categorie, precision=100):
        """
        :param nom: Nom de l'attaque
        :param type_: Type élémentaire (Feu, Eau, Plante, etc.)
        :param puissance: Puissance de l'attaque (ex: 40, 60, 100)
        :param categorie: "physique" ou "special"
        :param precision: Précision (0 à 100, optionnel)
        """
        self.nom = nom
        self.type = type_
        self.puissance = puissance
        self.categorie = categorie  # "physique" ou "special"
        self.precision = precision

    def __str__(self):
        return (
            f"{self.nom} - {self.type} ({self.categorie}) | "
            f"Puissance: {self.puissance}, Précision: {self.precision}%"
        )

# === Définition de toutes les attaques disponibles ===
ATTAQUES = {
    # Attaques Normal
    "Charge": Attaque("Charge", "Normal", 35, "physique"),
    "Tacle": Attaque("Tacle", "Normal", 30, "physique"),
    "Ecras'Face": Attaque("Ecras'Face", "Normal", 40, "physique"),
    "Coup d'Boule": Attaque("Coup d'Boule", "Normal", 70, "physique"),
    "Ultimapoing": Attaque("Ultimapoing", "Normal", 80, "physique"),
    "Griffe": Attaque("Griffe", "Normal", 40, "physique"),
    "Tranche": Attaque("Tranche", "Normal", 70, "physique"),
    "Plaquage": Attaque("Plaquage", "Normal", 85, "physique"),
    "Damoclès": Attaque("Damoclès", "Normal", 120, "physique"),
    "Ultralaser": Attaque("Ultralaser", "Normal", 150, "special", 90),
    "Morsure": Attaque("Morsure", "Normal", 60, "physique"),
    "Métronome": Attaque("Métronome", "Normal", 0, "special"),
    "Double-Slap": Attaque("Double-Slap", "Normal", 15, "physique", 85),
    "Berceuse": Attaque("Berceuse", "Normal", 0, "special"),
    "Vive-Attaque": Attaque("Vive-Attaque", "Normal", 40, "physique", 100),
    "Armure": Attaque("Armure", "Normal", 0, "special"),
    
    # Attaques Vol
    "Picpic": Attaque("Picpic", "Vol", 35, "physique"),
    "Tornade": Attaque("Tornade", "Vol", 40, "special"),
    "Cru-Aile": Attaque("Cru-Aile", "Vol", 60, "physique"),
    "Aéropique": Attaque("Aéropique", "Vol", 60, "physique"),
    
    # Attaques Eau
    "Pistolet à O": Attaque("Pistolet à O", "Eau", 40, "special"),
    "Bulles d'O": Attaque("Bulles d'O", "Eau", 65, "special"),
    "Hydrocanon": Attaque("Hydrocanon", "Eau", 120, "special", 80),
    "Surf": Attaque("Surf", "Eau", 95, "special"),
    "Cascade": Attaque("Cascade", "Eau", 80, "physique"),
    
    # Attaques Plante
    "Fouet Lianes": Attaque("Fouet Lianes", "Plante", 45, "physique"),
    "Tranch'Herbe": Attaque("Tranch'Herbe", "Plante", 55, "physique", 95),
    "Lance-Soleil": Attaque("Lance-Soleil", "Plante", 120, "special", 100),
    "Méga-Sangsue": Attaque("Méga-Sangsue", "Plante", 40, "special"),
    "Poudre Dodo": Attaque("Poudre Dodo", "Plante", 0, "special"),
    
    # Attaques Poison
    "Toxik": Attaque("Toxik", "Poison", 0, "special"),
    "Dard-Venin": Attaque("Dard-Venin", "Poison", 15, "physique"),
    "Acide": Attaque("Acide", "Poison", 40, "special"),
    "Poudre Toxik": Attaque("Poudre Toxik", "Poison", 0, "special"),
    "Double-Dard": Attaque("Double-Dard", "Poison", 25, "physique"),
    
    # Attaques Électrique
    "Éclair": Attaque("Éclair", "Électrique", 40, "special"),
    "Tonnerre": Attaque("Tonnerre", "Électrique", 95, "special", 100),
    "Fatal-Foudre": Attaque("Fatal-Foudre", "Électrique", 120, "special", 70),
    "Cage-Éclair": Attaque("Cage-Éclair", "Électrique", 0, "special"),
    "Onde de Choc": Attaque("Onde de Choc", "Électrique", 60, "special"),
    "Électroball": Attaque("Électroball", "Électrique", 80, "special", 100),
    
    # Attaques Feu
    "Flammèche": Attaque("Flammèche", "Feu", 40, "special"),
    "Lance-Flammes": Attaque("Lance-Flammes", "Feu", 95, "special", 100),
    "Déflagration": Attaque("Déflagration", "Feu", 120, "special", 85),
    "Danse Flamme": Attaque("Danse Flamme", "Feu", 35, "special"),
    "Roue de Feu": Attaque("Roue de Feu", "Feu", 60, "physique"),
    
    # Attaques Combat
    "Poing-Karaté": Attaque("Poing-Karaté", "Combat", 50, "physique"),
    "Balayage": Attaque("Balayage", "Combat", 65, "physique"),
    "Sacrifice": Attaque("Sacrifice", "Combat", 80, "physique"),
    "Double-Pied": Attaque("Double-Pied", "Combat", 30, "physique"),
    
    # Attaques Psy
    "Choc Mental": Attaque("Choc Mental", "Psy", 50, "special"),
    "Ultrason": Attaque("Ultrason", "Psy", 0, "special"),
    
    # Attaques Sol
    "Tunnel": Attaque("Tunnel", "Sol", 80, "physique"),
    
    # Attaques Insecte
    "Piqûre": Attaque("Piqûre", "Insecte", 60, "physique"),
    "Papillodanse": Attaque("Papillodanse", "Insecte", 0, "special"),
    "Furie": Attaque("Furie", "Insecte", 18, "physique", 80),
    "Sécrétion": Attaque("Sécrétion", "Insecte", 0, "special"),
}

class Pokemon:
    def __init__(self, nom, type_, pv_max, attaque, defense, special, vitesse, attaques_possibles=None):
        self.nom = nom
        self.type = type_
        self.pv_max = pv_max
        self.pv = pv_max
        self.attaque = attaque
        self.defense = defense
        self.special = special
        self.vitesse = vitesse
        self.attaques_possibles = attaques_possibles if attaques_possibles else []
        self.attaques = []  # Les 4 attaques actuellement équipées

    def apprendre_attaque(self, nom_attaque):
        """Ajoute une attaque aux 4 attaques équipées si possible"""
        if len(self.attaques) >= 4:
            return False
        if nom_attaque not in ATTAQUES:
            print(f"Erreur: L'attaque {nom_attaque} n'existe pas")
            return False
        if nom_attaque not in self.attaques_possibles:
            print(f"Erreur: {self.nom} ne peut pas apprendre {nom_attaque}")
            return False
        
        # Vérifier si l'attaque n'est pas déjà apprise
        if any(attaque.nom == nom_attaque for attaque in self.attaques):
            print(f"Erreur: {self.nom} connaît déjà {nom_attaque}")
            return False
            
        self.attaques.append(ATTAQUES[nom_attaque])
        return True

    def oublier_attaque(self, index):
        """Retire une attaque des attaques équipées"""
        if 0 <= index < len(self.attaques):
            self.attaques.pop(index)
            return True
        return False

    def est_ko(self):
        return self.pv <= 0

    def subir_degats(self, degats):
        self.pv = max(0, self.pv - degats)

    def soigner(self):
        self.pv = self.pv_max

    def __str__(self):
        liste_attaques = "\n  ".join(str(a) for a in self.attaques)
        return (
            f"{self.nom} ({self.type}) - {self.pv}/{self.pv_max} PV\n"
            f"ATK: {self.attaque} | DEF: {self.defense} | SPE: {self.special}\n"
            f"Attaques apprises:\n  {liste_attaques if liste_attaques else 'Aucune'}"
        )

# === Définition des Pokémon de base ===
POKEMONS_DISPONIBLES = {
    "Bulbizarre": {
        "base": Pokemon("Bulbizarre", "Plante", 45, 49, 49, 65, 45,
                     ["Fouet Lianes", "Charge", "Tranch'Herbe", "Lance-Soleil", "Méga-Sangsue", "Toxik"]),
        "niveau": 50
    },
    "Herbizarre": {
        "base": Pokemon("Herbizarre", "Plante", 60, 62, 63, 80, 60,
                     ["Fouet Lianes", "Tranch'Herbe", "Lance-Soleil", "Méga-Sangsue", "Toxik", "Damoclès"]),
        "niveau": 50
    },
    "Florizarre": {
        "base": Pokemon("Florizarre", "Plante", 80, 82, 83, 100, 80,
                     ["Fouet Lianes", "Tranch'Herbe", "Lance-Soleil", "Méga-Sangsue", "Toxik", "Damoclès"]),
        "niveau": 50
    },
    "Salamèche": {
        "base": Pokemon("Salamèche", "Feu", 39, 52, 43, 60, 65,
                     ["Flammèche", "Griffe", "Lance-Flammes", "Déflagration", "Danse Flamme", "Tranche"]),
        "niveau": 50
    },
    "Reptincel": {
        "base": Pokemon("Reptincel", "Feu", 58, 64, 58, 80, 80,
                     ["Flammèche", "Lance-Flammes", "Déflagration", "Danse Flamme", "Tranche", "Griffe"]),
        "niveau": 50
    },
    "Dracaufeu": {
        "base": Pokemon("Dracaufeu", "Feu", 78, 84, 78, 109, 100,
                     ["Lance-Flammes", "Déflagration", "Danse Flamme", "Tranche", "Cru-Aile", "Ultralaser"]),
        "niveau": 50
    },
    "Carapuce": {
        "base": Pokemon("Carapuce", "Eau", 44, 48, 65, 60, 43,
                     ["Pistolet à O", "Charge", "Bulles d'O", "Surf", "Hydrocanon", "Morsure"]),
        "niveau": 50
    },
    "Carabaffe": {
        "base": Pokemon("Carabaffe", "Eau", 59, 63, 80, 75, 58,
                     ["Pistolet à O", "Bulles d'O", "Surf", "Hydrocanon", "Morsure", "Plaquage"]),
        "niveau": 50
    },
    "Tortank": {
        "base": Pokemon("Tortank", "Eau", 79, 83, 100, 95, 78,
                     ["Surf", "Hydrocanon", "Morsure", "Plaquage", "Ultralaser", "Cascade"]),
        "niveau": 50
    },
    "Chenipan": {
        "base": Pokemon("Chenipan", "Insecte", 45, 30, 35, 20, 45,
                     ["Charge", "Sécrétion", "Piqûre", "Dard-Venin"]),
        "niveau": 50
    },
    "Chrysacier": {
        "base": Pokemon("Chrysacier", "Insecte", 50, 20, 55, 25, 30,
                     ["Armure", "Sécrétion", "Piqûre", "Dard-Venin"]),
        "niveau": 50
    },
    "Papilusion": {
        "base": Pokemon("Papilusion", "Insecte", 60, 45, 50, 90, 70,
                     ["Choc Mental", "Poudre Toxik", "Tornade", "Ultrason", "Dard-Venin", "Sécrétion","Poudre Dodo","Papillodanse"]),
        "niveau": 50
    },
    "Aspicot": {
        "base": Pokemon("Aspicot", "Insecte", 40, 35, 30, 20, 50,
                     ["Dard-Venin", "Sécrétion"]),
        "niveau": 50
    },
    "Coconfort": {
        "base": Pokemon("Coconfort", "Insecte", 45, 25, 50, 25, 35,
                     ["Armure"]),
        "niveau": 50
    },
    "Dardargnan": {
        "base": Pokemon("Dardargnan", "Insecte", 65, 90, 40, 45, 75,
                     ["Dard-Venin", "Double-Dard", "Furie"]),
        "niveau": 50
    },
    "Roucool": {
        "base": Pokemon("Roucool", "Normal", 40, 45, 40, 35, 56,
                     ["Charge", "Tornade", "Cru-Aile", "Aéropique", "Plaquage"]),
        "niveau": 50
    },
    "Roucoups": {
        "base": Pokemon("Roucoups", "Normal", 63, 60, 55, 50, 71,
                     ["Tornade", "Cru-Aile", "Aéropique", "Plaquage", "Damoclès"]),
        "niveau": 50
    },
    "Roucarnage": {
        "base": Pokemon("Roucarnage", "Vol", 83, 80, 75, 70, 91,
                     ["Tornade", "Cru-Aile", "Aéropique", "Plaquage", "Damoclès", "Ultralaser"]),
        "niveau": 50
    },
    "Rattata": {
        "base": Pokemon("Rattata", "Normal", 30, 56, 35, 25, 72,
                     ["Charge", "Morsure", "Plaquage", "Damoclès", "Tranche"]),
        "niveau": 50
    },
    "Rattatac": {
        "base": Pokemon("Rattatac", "Normal", 55, 81, 60, 50, 97,
                     ["Morsure", "Plaquage", "Damoclès", "Tranche", "Ultralaser"]),
        "niveau": 50
    },
    "Piafabec": {
        "base": Pokemon("Piafabec", "Vol", 40, 60, 30, 31, 70,
                     ["Picpic", "Tornade", "Cru-Aile", "Aéropique", "Tranche"]),
        "niveau": 50
    },
    "Rapasdepic": {
        "base": Pokemon("Rapasdepic", "Vol", 65, 90, 65, 61, 100,
                     ["Picpic", "Tornade", "Cru-Aile", "Aéropique", "Tranche", "Ultralaser"]),
        "niveau": 50
    },
    "Abo": {
        "base": Pokemon("Abo", "Poison", 35, 60, 44, 40, 55,
                     ["Morsure", "Dard-Venin", "Acide", "Toxik", "Plaquage"]),
        "niveau": 50
    },
    "Arbok": {
        "base": Pokemon("Arbok", "Poison", 60, 95, 69, 65, 80,
                     ["Morsure", "Dard-Venin", "Acide", "Toxik", "Plaquage", "Ultralaser"]),
        "niveau": 50
    },
    "Pikachu": {
        "base": Pokemon("Pikachu", "Électrique", 35, 55, 40, 50, 90,
                     ["Éclair", "Tonnerre", "Fatal-Foudre", "Cage-Éclair", "Onde de Choc"]),
        "niveau": 50
    },
    "Raichu": {
        "base": Pokemon("Raichu", "Électrique", 60, 90, 55, 90, 110,
                     ["Éclair", "Tonnerre", "Fatal-Foudre", "Cage-Éclair", "Onde de Choc", "Électroball"]),
        "niveau": 50
    },
    "Sabelette": {
        "base": Pokemon("Sabelette", "Sol", 50, 75, 85, 30, 40,
                     ["Charge", "Griffe", "Tunnel", "Tranche"]),
        "niveau": 50
    },
    "Sablaireau": {
        "base": Pokemon("Sablaireau", "Sol", 75, 100, 110, 45, 65,
                     ["Griffe", "Tunnel", "Tranche", "Ultralaser"]),
        "niveau": 50
    },
    "Nidoran♀": {
        "base": Pokemon("Nidoran♀", "Poison", 55, 47, 52, 40, 41,
                     ["Dard-Venin", "Griffe", "Double-Pied", "Morsure"]),
        "niveau": 50
    },
    "Nidorina": {
        "base": Pokemon("Nidorina", "Poison", 70, 62, 67, 55, 56,
                     ["Dard-Venin", "Griffe", "Double-Pied", "Morsure", "Plaquage"]),
        "niveau": 50
    },
    "Nidoqueen": {
        "base": Pokemon("Nidoqueen", "Poison", 90, 92, 87, 75, 76,
                     ["Dard-Venin", "Double-Pied", "Plaquage", "Ultralaser"]),
        "niveau": 50
    },
    "Nidoran♂": {
        "base": Pokemon("Nidoran♂", "Poison", 46, 57, 40, 40, 50,
                     ["Dard-Venin", "Griffe", "Double-Pied", "Morsure"]),
        "niveau": 50
    },
    "Nidorino": {
        "base": Pokemon("Nidorino", "Poison", 61, 72, 57, 55, 65,
                     ["Dard-Venin", "Griffe", "Double-Pied", "Morsure", "Plaquage"]),
        "niveau": 50
    },
    "Nidoking": {
        "base": Pokemon("Nidoking", "Poison", 81, 102, 77, 85, 85,
                     ["Dard-Venin", "Double-Pied", "Plaquage", "Ultralaser"]),
        "niveau": 50
    },
    "Mélofée": {
        "base": Pokemon("Mélofée", "Normal", 70, 45, 48, 60, 35,
                     ["Écras'Face", "Métronome", "Tornade", "Plaquage"]),
        "niveau": 50
    },
    "Mélodelfe": {
        "base": Pokemon("Mélodelfe", "Normal", 95, 70, 73, 95, 60,
                     ["Métronome", "Tornade", "Plaquage", "Ultralaser"]),
        "niveau": 50
    },
    "Goupix": {
        "base": Pokemon("Goupix", "Feu", 38, 41, 40, 50, 65,
                     ["Flammèche", "Vive-Attaque", "Lance-Flammes", "Déflagration"]),
        "niveau": 50
    },
    "Feunard": {
        "base": Pokemon("Feunard", "Feu", 73, 76, 75, 100, 100,
                     ["Lance-Flammes", "Déflagration", "Plaquage", "Ultralaser"]),
        "niveau": 50
    },
    "Rondoudou": {
        "base": Pokemon("Rondoudou", "Normal", 115, 45, 20, 45, 20,
                     ["Écras'Face", "Berceuse", "Plaquage", "Double-Slap"]),
        "niveau": 50
    },
    "Grodoudou": {
        "base": Pokemon("Grodoudou", "Normal", 140, 70, 45, 85, 45,
                     ["Berceuse", "Plaquage", "Double-Slap", "Ultralaser"]),
        "niveau": 50
    },
}

def creer_pokemon(nom_pokemon):
    """Crée une nouvelle instance d'un Pokémon à partir des données de base"""
    if nom_pokemon in POKEMONS_DISPONIBLES:
        pokemon_base = POKEMONS_DISPONIBLES[nom_pokemon]["base"]
        nouveau_pokemon = Pokemon(
            pokemon_base.nom,
            pokemon_base.type,
            pokemon_base.pv_max,
            pokemon_base.attaque,
            pokemon_base.defense,
            pokemon_base.special,
            pokemon_base.vitesse,
            pokemon_base.attaques_possibles.copy()
        )
        return nouveau_pokemon
    return None 
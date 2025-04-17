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


class Pokemon:
    def __init__(self, nom, type_, pv_max, attaque, defense, special, attaques=None):
        self.nom = nom
        self.type = type_
        self.pv_max = pv_max
        self.pv = pv_max
        self.attaque = attaque
        self.defense = defense
        self.special = special
        self.attaques = attaques if attaques else []

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
            f"Attaques:\n  {liste_attaques if liste_attaques else 'Aucune'}"
        )
# === Définition des attaques ===

eclair = Attaque("Éclair", "Électrique", 40, "special")
charge = Attaque("Charge", "Normal", 35, "physique")
pistolet_eau = Attaque("Pistolet à O", "Eau", 40, "special")
tacle = Attaque("Tacle", "Normal", 30, "physique")
fouet_lianes = Attaque("Fouet Lianes", "Plante", 45, "physique")

# === Définition de Pokémon ===

pikachu = Pokemon("Pikachu", "Électrique", 100, 55, 30, 50, attaques=[eclair, charge])
carapuce = Pokemon("Carapuce", "Eau", 120, 45, 40, 50, attaques=[pistolet_eau, tacle])
bulbizarre = Pokemon("Bulbizarre", "Plante", 110, 48, 42, 60, attaques=[fouet_lianes, charge])

# === Dictionnaire de référence ===

POKEMONS_DE_BASE = {
    "Pikachu": pikachu,
    "Carapuce": carapuce,
    "Bulbizarre": bulbizarre,
}
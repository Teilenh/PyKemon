class Pokemon:
    def __init__(self, nom, type_, pv_max, attaque, defense, special):
        self.nom = nom
        self.type = type_
        self.pv_max = pv_max
        self.pv = pv_max
        self.attaque = attaque
        self.defense = defense
        self.special = special  # Atk.Sp/Def.Sp regroupée, pkm 1G

    def est_ko(self):
        return self.pv <= 0

    def subir_degats(self, degats):
        self.pv = max(0, self.pv - degats)

    def soigner(self):
        self.pv = self.pv_max

    def __str__(self):
        return (
            f"{self.nom} ({self.type}) - {self.pv}/{self.pv_max} PV | "
            f"ATK: {self.attaque} DEF: {self.defense} SPE: {self.special}"
        )

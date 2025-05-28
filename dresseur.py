class Dresseur:
    def __init__(self, nom):
        self.nom = nom
        self.equipe = []

    def ajouter_pokemon(self, pokemon):
        if len(self.equipe) < 6:
            self.equipe.append(pokemon)

    def equipe_ko(self):
        return all(p.est_ko() for p in self.equipe)

    def choisir_pokemon_actif(self):
        for p in self.equipe:
            if not p.est_ko():
                return p
        return None

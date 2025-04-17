from PKMtypes import get_multiplicateur

def calcul_degats(attacker, defender, attaque):
    niveau = 50

    # Choix des statistiques selon la catégorie d'attaque
    if attaque.categorie == "physique":
        stat_attaquant = attacker.attaque
        stat_defenseur = defender.defense
    elif attaque.categorie == "special":
        stat_attaquant = attacker.special
        stat_defenseur = defender.special
    else:
        raise ValueError("Catégorie d'attaque inconnue")
    multiplicateur_type = get_multiplicateur(attaque.type, defender.type)

    # Formule des dégâts (génération 1 simplifiée)
    degats = (((2 * niveau + 10) / 250) * (stat_attaquant / stat_defenseur) * attaque.puissance + 2) * multiplicateur_type
    return max(1, int(degats))

def tour_combat(attacker, defender, attaque):
    degats = calcul_degats(attacker, defender, attaque)
    defender.subir_degats(degats)
    return f"{attacker.nom} utilise {attaque.nom} sur {defender.nom} et inflige {degats} dégâts !"

def choisir_attaque(pokemon):
    print(f"\n{pokemon.nom} - Attaques disponibles :")
    for idx, atk in enumerate(pokemon.attaques, 1):
        print(f"{idx}. {atk.nom} ({atk.type}, {atk.categorie}, Puissance: {atk.puissance})")
    
    while True:
        choix = input("Choisissez une attaque (numéro) : ")
        if choix.isdigit():
            index = int(choix) - 1
            if 0 <= index < len(pokemon.attaques):
                return pokemon.attaques[index]
        print("Choix invalide. Réessayez.")
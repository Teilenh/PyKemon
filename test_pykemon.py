import sys
import os

# Ajout du dossier courant au path pour les imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.core.pokemon import creer_pokemon, POKEMONS_DISPONIBLES
from src.core.team_builder import TeamBuilder
from src.core.combat import calcul_degats

def tester_teambuilder():
    print("=== TEST TEAM BUILDER ===")
    tb = TeamBuilder()
    
    # S'assurer que le fichier précédent est purgé pour le test
    if os.path.exists(tb.fichier_equipe):
        os.remove(tb.fichier_equipe)
        
    print("1. Ajout de Dracaufeu :", tb.ajouter_pokemon("Dracaufeu"))
    print("2. Ajout de Florizarre :", tb.ajouter_pokemon("Florizarre"))
    
    # Configuration des attaques
    print("3. Configuration des attaques de Dracaufeu...")
    if len(tb.equipe) > 0:
        poke = tb.equipe[0]
        # On lui donne les 4 premières attaques disponibles
        attaques_dispo = poke.attaques_possibles[:4]
        tb.configurer_attaques(0, attaques_dispo)
        print(f"Dracaufeu attaques: {[a.nom for a in poke.attaques]}")
        
    # Sauvegarde et Chargement
    print("4. Sauvegarde de l'équipe :", tb.sauvegarder_equipe()[1])
    
    tb2 = TeamBuilder()
    print("5. Chargement de l'équipe dans un nouveau builder :", tb2.charger_equipe()[1])
    print("Équipe chargée :", [p.nom for p in tb2.equipe])
    print()

def tester_combat():
    print("=== TEST COMBAT & STATS ===")
    dracaufeu = creer_pokemon("Dracaufeu")
    florizarre = creer_pokemon("Florizarre")
    
    # Attribution d'attaques
    dracaufeu.apprendre_attaque("Ultimapoing")
    
    # Modification des stats
    print("1. Attaque initiale de Dracaufeu :", dracaufeu.get_stat("attaque"))
    dracaufeu.modify_stat("attaque", 2) # Ex: Danse Lames x2
    print("2. Attaque après un buff de +2 niveaux :", dracaufeu.get_stat("attaque"))
    
    # Calcul des dégâts
    attaque = next(a for a in dracaufeu.attaques if a.nom == "Ultimapoing")
    degats = calcul_degats(dracaufeu, florizarre, attaque)
    print(f"3. Dégâts calculés de Ultimapoing avec buff : {degats}")
    
    florizarre.subir_degats(degats)
    print(f"4. Florizarre a subi l'attaque. Est-il K.O. ? {florizarre.est_ko()} (Reste {florizarre.pv}/{florizarre.pv_max} PV)")
    print()

if __name__ == "__main__":
    tester_teambuilder()
    tester_combat()

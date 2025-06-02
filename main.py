#!/usr/bin/env python3
import sys
from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QPalette, QColor
from src.gui import *

def main():
    # Création de l'application Qt
    app = QApplication(sys.argv)
    
    # Application du style moderne
    app.setStyle("Fusion")
    
    # Configuration de la palette de couleurs
    palette = QPalette()
    palette.setColor(QPalette.ColorRole.Window, QColor("#f5f6fa"))
    palette.setColor(QPalette.ColorRole.WindowText, QColor("#2f3640"))
    app.setPalette(palette)
    
    # Création et affichage de la fenêtre principale
    window = MenuPrincipal()
    window.show()
    
    # Exécution de la boucle d'événements
    sys.exit(app.exec())

if __name__ == "__main__":
    main()

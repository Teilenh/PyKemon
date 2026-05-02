#!/usr/bin/env python3
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QStackedWidget
from src.gui.main_menu import MenuPrincipal
from src.gui.team_builder_GUI import TeamBuilderGUI
from src.gui.combat import CombatGUI
from src.gui.theme import get_platform_style

class ApplicationWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyKemon")
        self.setMinimumSize(1000, 750)
        self.setStyleSheet(get_platform_style())

        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        self.menu_principal = MenuPrincipal(self)
        self.stacked_widget.addWidget(self.menu_principal)

    def show_menu(self):
        # Supprime toutes les autres fenêtres pour libérer la mémoire et forcer l'actualisation à la prochaine ouverture
        for i in range(self.stacked_widget.count() - 1, 0, -1):
            widget = self.stacked_widget.widget(i)
            self.stacked_widget.removeWidget(widget)
            widget.deleteLater()
        self.stacked_widget.setCurrentIndex(0)
        self.setStyleSheet(get_platform_style())

    def show_team_builder(self):
        tb = TeamBuilderGUI(self)
        self.stacked_widget.addWidget(tb)
        self.stacked_widget.setCurrentWidget(tb)

    def show_combat(self):
        combat = CombatGUI(self)
        self.stacked_widget.addWidget(combat)
        self.stacked_widget.setCurrentWidget(combat)

def main():
    app = QApplication(sys.argv)
    
    window = ApplicationWindow()
    window.show()
    
    sys.exit(app.exec())

if __name__ == "__main__":
    main()

from PyQt6.QtCore import QSettings
from PyQt6.QtWidgets import QPushButton, QApplication
from PyQt6.QtCore import Qt
import platform
import os

class ThemeManager:
    """Gestionnaire de thème pour l'application"""
    def __init__(self):
        self.settings = QSettings('PyKemon', 'Theme')
        self._is_dark = self.settings.value('is_dark', True, type=bool)

    @property
    def is_dark(self):
        return self._is_dark

    @is_dark.setter
    def is_dark(self, value):
        self._is_dark = value
        self.settings.setValue('is_dark', value)
        self.settings.sync()

    def toggle_theme(self):
        self.is_dark = not self.is_dark
        return self.is_dark

class ThemeSwitchButton(QPushButton):
    """Bouton de changement de thème"""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("theme_switch")
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.update_icon()
        self.clicked.connect(self.toggle_theme)

    def update_icon(self):
        # Utilisation d'émojis Unicode pour les icônes
        self.setText("🌙" if theme_manager.is_dark else "☀️")

    def toggle_theme(self):
        is_dark = theme_manager.toggle_theme()
        self.update_icon()
        # Mettre à jour le style de toutes les fenêtres
        for widget in QApplication.topLevelWidgets():
            widget.setStyleSheet(get_platform_style())
            # Forcer la mise à jour visuelle
            widget.style().unpolish(widget)
            widget.style().polish(widget)
            widget.update()

# Instance globale du gestionnaire de thème
theme_manager = ThemeManager()

def is_dark_theme_active():
    """Détecte si le thème sombre est actif sur le système"""
    if platform.system().lower() == 'linux':
        # Détection pour GTK
        try:
            import subprocess
            result = subprocess.run(
                ['gsettings', 'get', 'org.gnome.desktop.interface', 'gtk-theme'],
                capture_output=True,
                text=True
            )
            theme_name = result.stdout.strip().lower().replace("'", "")
            return 'dark' in theme_name
        except:
            # Si gsettings n'est pas disponible, on vérifie la variable d'environnement
            return os.environ.get('GTK_THEME', '').lower().endswith(':dark')
    return False

def get_platform_style():
    """Retourne le style approprié selon la plateforme et le thème"""
    system = platform.system().lower()
    
    # Utilisation du thème forcé si on est sous Linux
    if system == 'linux':
        is_dark = theme_manager.is_dark
    else:
        is_dark = True  # Toujours sombre pour Windows et autres

    if is_dark:
        # Couleurs du thème sombre
        colors = {
            'background': '#36393f',
            'secondary': '#2f3136',
            'surface': '#40444b',
            'accent': '#5865f2',
            'accent_hover': '#4752c4',
            'text': '#dcddde',
            'text_secondary': '#96989d',
            'success': '#43b581',
            'danger': '#f04747',
            'border': '#202225'
        }
    else:
        # Thème clair avec intégration système
        colors = {
            'background': 'palette(window)',
            'secondary': 'palette(base)',
            'surface': 'palette(button)',
            'accent': 'palette(highlight)',
            'accent_hover': 'palette(highlight)',
            'text': 'palette(text)',
            'text_secondary': 'palette(text)',
            'success': '#43b581',
            'danger': '#f04747',
            'border': 'palette(mid)'
        }

    return f"""
        /* Style global */
        QWidget {{
            font-family: system-ui;
            background-color: {colors['background']};
            color: {colors['text']};
        }}
        
        /* Style des fenêtres */
        QMainWindow, QDialog {{
            background-color: {colors['background']};
        }}
        
        /* Style des boutons standard */
        QPushButton.custom-button {{
            background-color: {colors['surface']};
            color: {colors['text']};
            border: none;
            border-radius: 4px;
            padding: 8px 16px;
            font-weight: 500;
            min-height: 38px;
        }}
        
        QPushButton.custom-button:hover {{
            background-color: {colors['accent']};
            color: palette(light);
        }}
        
        QPushButton.custom-button:pressed {{
            background-color: {colors['accent_hover']};
        }}
        
        /* Style des frames */
        QFrame.custom-frame {{
            background-color: {colors['secondary']};
            border: 1px solid {colors['border']};
            border-radius: 8px;
        }}
        
        /* Style des labels */
        QLabel.title {{
            color: {colors['text']};
            font-size: 24px;
            font-weight: bold;
        }}
        
        QLabel.subtitle {{
            color: {colors['text_secondary']};
            font-size: 16px;
        }}
        
        /* Style des listes */
        QListWidget {{
            background-color: {colors['secondary']};
            border: 1px solid {colors['border']};
            border-radius: 4px;
        }}
        
        QListWidget::item {{
            color: {colors['text']};
            border-radius: 2px;
            padding: 6px;
        }}
        
        QListWidget::item:hover {{
            background-color: {colors['surface']};
        }}
        
        QListWidget::item:selected {{
            background-color: {colors['accent']};
            color: palette(light);
        }}
        
        /* Style des boutons spéciaux */
        QPushButton#btn_sauvegarder {{
            background-color: {colors['success']};
            color: white;
        }}
        
        QPushButton#btn_quitter {{
            background-color: {colors['danger']};
            color: white;
        }}
        
        /* Style de la barre de vie */
        QFrame#barre_vie {{
            background-color: {colors['danger']};
            border-radius: 4px;
        }}
        
        QFrame#barre_vie > QFrame {{
            background-color: {colors['success']};
            border-radius: 4px;
        }}
        
        /* Style du bouton de thème */
        QPushButton#theme_switch {{
            font-size: 20px;
            border-radius: 15px;
            min-width: 30px;
            min-height: 30px;
            padding: 5px;
            background-color: {colors['surface']};
            color: {colors['text']};
        }}
        
        QPushButton#theme_switch:hover {{
            background-color: {colors['accent']};
        }}
    """ 
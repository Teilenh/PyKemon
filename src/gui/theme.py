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
        # Utilisation d'émojis Unicode pour les icônes (Soleil en mode sombre pour passer au clair, Lune en mode clair)
        self.setText("☀️" if theme_manager.is_dark else "🌙")

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
        # Thème GTK Adwaita Dark
        colors = {
            'background': '#242424',
            'secondary': '#303030',
            'surface': '#383838',
            'surface_hover': '#424242',
            'surface_active': '#4a4a4a',
            'accent': '#3584e4',
            'accent_hover': '#4a90d9',
            'text': '#ffffff',
            'text_secondary': '#9a9996',
            'success': '#2ec27e',
            'danger': '#e01b24',
            'border': '#1e1e1e',
            'border_light': '#383838'
        }
    else:
        # Thème GTK Adwaita Light
        colors = {
            'background': '#fafafa',
            'secondary': '#ffffff',
            'surface': '#f6f5f4',
            'surface_hover': '#f0f0f0',
            'surface_active': '#e8e8e8',
            'accent': '#3584e4',
            'accent_hover': '#1b6acb',
            'text': '#242424',
            'text_secondary': '#77767b',
            'success': '#2ec27e',
            'danger': '#e01b24',
            'border': '#deddda',
            'border_light': '#e5e5e5'
        }

    return f"""
        /* Style global */
        QWidget {{
            font-family: "Cantarell", system-ui, sans-serif;
            color: {colors['text']};
            font-size: 14px;
        }}
        
        /* Style des fenêtres */
        QMainWindow, QDialog, QStackedWidget {{
            background-color: {colors['background']};
        }}
        
        QLabel {{
            background: transparent;
        }}
        
        /* Style des boutons standard */
        QPushButton.custom-button, QPushButton {{
            background-color: {colors['surface']};
            color: {colors['text']};
            border: 1px solid {colors['border_light']};
            border-radius: 6px;
            padding: 8px 16px;
            font-weight: 600;
            min-height: 24px;
        }}
        
        QPushButton.custom-button:hover, QPushButton:hover {{
            background-color: {colors['surface_hover']};
        }}
        
        QPushButton.custom-button:pressed, QPushButton:pressed {{
            background-color: {colors['surface_active']};
        }}
        
        /* Style des frames (comme des listbox ou des conteneurs) */
        QFrame.custom-frame {{
            background-color: {colors['secondary']};
            border: 1px solid {colors['border']};
            border-radius: 12px;
        }}
        
        /* Style des labels */
        QLabel.title {{
            color: {colors['text']};
            font-size: 28px;
            font-weight: 800;
            padding-bottom: 8px;
        }}
        
        QLabel.subtitle {{
            color: {colors['text_secondary']};
            font-size: 15px;
            font-weight: 500;
        }}
        
        /* Style des listes (PC Boîte) */
        QListWidget {{
            background-color: {colors['secondary']};
            border: 1px solid {colors['border']};
            border-radius: 8px;
            outline: none;
        }}
        
        QListWidget::item {{
            color: {colors['text']};
            border-radius: 6px;
            padding: 6px;
            margin: 2px;
        }}
        
        QListWidget::item:hover {{
            background-color: {colors['surface']};
        }}
        
        QListWidget::item:selected {{
            background-color: {colors['accent']};
            color: #ffffff;
        }}
        
        /* Style des boutons spéciaux */
        QPushButton#btn_sauvegarder {{
            background-color: {colors['success']};
            color: white;
            border: 1px solid {colors['success']};
        }}
        
        QPushButton#btn_sauvegarder:hover {{
            background-color: #33d188;
        }}
        
        QPushButton#btn_quitter {{
            background-color: {colors['danger']};
            color: white;
            border: 1px solid {colors['danger']};
        }}
        
        QPushButton#btn_quitter:hover {{
            background-color: #ed2b34;
        }}
        
        /* Style de la barre de vie */
        QFrame#barre_vie {{
            background-color: {colors['surface']};
            border-radius: 6px;
            border: 1px solid {colors['border']};
        }}
        
        QFrame#barre_vie > QFrame {{
            background-color: {colors['success']};
            border-radius: 5px;
        }}
        
        /* Style du bouton de thème */
        QPushButton#theme_switch {{
            font-family: "Noto Color Emoji", "Apple Color Emoji", "Segoe UI Emoji", sans-serif;
            font-size: 18px;
            border-radius: 18px;
            min-width: 36px;
            min-height: 36px;
            max-width: 36px;
            max-height: 36px;
            padding: 0px;
            background-color: {colors['surface']};
            border: 1px solid {colors['border_light']};
            color: {colors['text']};
        }}
        
        QPushButton#theme_switch:hover {{
            background-color: {colors['surface_hover']};
        }}
    """ 
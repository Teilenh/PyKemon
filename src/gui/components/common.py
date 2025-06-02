from PyQt6.QtWidgets import QPushButton, QFrame
from PyQt6.QtCore import QPropertyAnimation, QRect, QEasingCurve

class BoutonAttaque(QPushButton):
    def __init__(self, text="", parent=None):
        super().__init__(text, parent)
        self.setMinimumHeight(50)
        self.setProperty("class", "custom-button")
        self.setStyleSheet("""
            QPushButton {
                font-size: 14px;
            }
        """)

class BarreVie(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMinimumHeight(20)
        self.setMaximumHeight(20)
        self.value = 100
        self.setObjectName("barre_vie")
        
        # Création de la barre interne
        self.barre_interne = QFrame(self)
        self.barre_interne.setGeometry(0, 0, self.width(), self.height())
        
        self.animation = QPropertyAnimation(self.barre_interne, b"geometry")
        self.animation.setDuration(500)
        self.animation.setEasingCurve(QEasingCurve.Type.OutCubic)

    def setValue(self, value):
        self.value = max(0, min(100, value))
        nouvelle_largeur = int(self.width() * (self.value / 100))
        
        self.animation.setStartValue(self.barre_interne.geometry())
        self.animation.setEndValue(QRect(0, 0, nouvelle_largeur, self.height()))
        self.animation.start()

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.barre_interne.setGeometry(0, 0, int(self.width() * (self.value / 100)), self.height()) 
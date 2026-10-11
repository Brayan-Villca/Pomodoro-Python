from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import Qt

class RelojWidget(QWidget):
    """Muestra el modo actual y el tiempo en formato MM:SS"""
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignCenter)

        self.lbl_estado = QLabel("MODO: TRABAJO")
        self.lbl_estado.setObjectName("estado")
        self.lbl_estado.setAlignment(Qt.AlignCenter)

        self.lbl_tiempo = QLabel("25:00")
        self.lbl_tiempo.setObjectName("reloj")
        self.lbl_tiempo.setAlignment(Qt.AlignCenter)

        layout.addWidget(self.lbl_estado)
        layout.addWidget(self.lbl_tiempo)

    def actualizar_tiempo(self, segundos):
        minutos = segundos // 60
        segs = segundos % 60
        self.lbl_tiempo.setText(f"{minutos:02d}:{segs:02d}")

    def cambiar_estado(self, texto):
        self.lbl_estado.setText(texto)


class ControlesWidget(QWidget):
    """Contiene la fila de botones de control"""
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QHBoxLayout(self)

        self.btn_iniciar = QPushButton("Iniciar")
        self.btn_pausar = QPushButton("Pausar")
        self.btn_reiniciar = QPushButton("Reiniciar")

        layout.addWidget(self.btn_iniciar)
        layout.addWidget(self.btn_pausar)
        layout.addWidget(self.btn_reiniciar)

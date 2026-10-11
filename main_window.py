from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QMessageBox
from PyQt5.QtCore import QTimer
import config
from widgets import RelojWidget, ControlesWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mi Pomodoro Modular")
        self.setFixedSize(320, 240)
        self.setStyleSheet(config.ESTILO_VENTANA)

        # Variables de estado
        self.tiempo_restante = config.TIEMPO_TRABAJO
        self.en_descanso = False

        # Configuración del temporizador
        self.timer = QTimer(self)
        self.timer.setInterval(1000)  # 1 segundo
        self.timer.timeout.connect(self.actualizar_segundo)

        self.init_ui()

    def init_ui(self):
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Instanciar y agregar los sub-widgets
        self.reloj = RelojWidget()
        self.controles = ControlesWidget()

        layout.addWidget(self.reloj)
        layout.addWidget(self.controles)

        # Conectar señales de los botones
        self.controles.btn_iniciar.clicked.connect(self.iniciar)
        self.controles.btn_pausar.clicked.connect(self.pausar)
        self.controles.btn_reiniciar.clicked.connect(self.reiniciar)

        # Mostrar tiempo inicial
        self.reloj.actualizar_tiempo(self.tiempo_restante)

    def iniciar(self):
        self.timer.start()

    def pausar(self):
        self.timer.stop()

    def reiniciar(self):
        self.pausar()
        self.en_descanso = False
        self.tiempo_restante = config.TIEMPO_TRABAJO
        self.reloj.cambiar_estado("MODO: TRABAJO")
        self.reloj.actualizar_tiempo(self.tiempo_restante)

    def actualizar_segundo(self):
        if self.tiempo_restante > 0:
            self.tiempo_restante -= 1
            self.reloj.actualizar_tiempo(self.tiempo_restante)
        else:
            self.alternar_fase()

    def alternar_fase(self):
        self.pausar()
        if not self.en_descanso:
            self.en_descanso = True
            self.tiempo_restante = config.TIEMPO_DESCANSO
            self.reloj.cambiar_estado("MODO: DESCANSO")
            QMessageBox.information(self, "¡Buen trabajo!", "Momento de tomar un descanso.")
        else:
            self.en_descanso = False
            self.tiempo_restante = config.TIEMPO_TRABAJO
            self.reloj.cambiar_estado("MODO: TRABAJO")
            QMessageBox.information(self, "A trabajar", "Fin del descanso, volvamos a la tarea.")
        
        self.reloj.actualizar_tiempo(self.tiempo_restante)

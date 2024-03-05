import sys, os

from qt_core import *

from gui.windows.main_window.ui_main_window import *


# MAIN WINDOW

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Program-Name")

        # SETUP MAIN WINDOW
        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)

        # EXIBIR APLICAÇÂO
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
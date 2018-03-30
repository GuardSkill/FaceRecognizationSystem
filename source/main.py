import sys
from PyQt5.QtWidgets import *
import FaceRecSystem

if __name__ == '__main__':
    app = QApplication(sys.argv)
    Window = QMainWindow()
    ui = FaceRecSystem.Ui_MainWindow()
    ui.setupUi(Window)
    Window.show()
    sys.exit(app.exec_())

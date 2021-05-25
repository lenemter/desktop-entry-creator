from MainWindow import MainWindow
from PyQt5.QtWidgets import QApplication
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    main_window = MainWindow()

    main_window.show()
    app.exec_()
    sys.exit()

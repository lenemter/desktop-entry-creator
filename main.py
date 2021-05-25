from MainWindow import MainWindow
from PyQt5.QtWidgets import QApplication
import sys
import platform

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    main_window = MainWindow()

    main_window.show()
    if platform.system() != "Linux":
        main_window.show_error("Not Linux")
        main_window.close()
        sys.exit()
    app.exec_()
    sys.exit()

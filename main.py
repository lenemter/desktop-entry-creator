from MainWindow import MainWindow
from PyQt5.QtWidgets import QApplication
import sys

# PyInstaller can't get styles from file
styles = """#container {background-color: #eee;}
QDialog {background-color:  #eee;}
QTableWidget {border-color:  #999;}
QTableWidget::item {selection-background-color:  #6fb2dc;}
QPushButton {background-color: #fff; padding: 4px 10px 4px 10px; color: #333;}
QToolButton {background-color: #fff; padding: 6px 6px 6px 6px; color: #333;}
QLineEdit {padding: 6px;}"""

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    app.setStyleSheet(styles)
    main_window = MainWindow()

    main_window.show()
    app.exec_()
    sys.exit()

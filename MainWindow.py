from MainWindow_ui import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from pathlib import Path
from os.path import isfile


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.submitButton.pressed.connect(self.create_file)

    def create_file(self):
        name = self.ui.nameLineEdit.text()
        comment = self.ui.commentLineEdit.text()
        icon = self.ui.iconLineEdit.text()
        command = self.ui.commandLineEdit.text()
        if any([not name, not command]):
            dialog = QMessageBox(self)
            dialog.setText("Name or Command field is empty")
            dialog.setIcon(QMessageBox.Warning)
            dialog.show()
        else:
            filepath = f"{str(Path.home())}/.local/share/applications/{name.lower().replace(' ', '-')}.desktop"
            if isfile(filepath):
                dialog = QMessageBox(self)
                dialog.setText(f"File {name.lower().replace(' ', '-')}.desktop already exists")
                dialog.setIcon(QMessageBox.Warning)
                dialog.show()
            else:
                try:
                    with open(filepath, 'w') as file:
                        file.writelines(["[Desktop Entry]\n",
                                         f"Name={name}\n",
                                         f"Comment={comment}\n",
                                         f"Icon={icon}\n",
                                         f"Exec={command}\n",
                                         "Type=Application"])
                except Exception as exception:
                    dialog = QMessageBox(self)
                    dialog.setText(exception)
                    dialog.setIcon(QMessageBox.Critical)
                    dialog.show()
                else:
                    dialog = QMessageBox(self)
                    dialog.setText("Success")
                    dialog.setIcon(QMessageBox.Warning)
                    dialog.show()

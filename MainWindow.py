from MainWindow_ui import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QFileDialog
from pathlib import Path
from os.path import isfile


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.submitButton.pressed.connect(self.create_file)
        self.ui.iconButton.pressed.connect(self.open_icon)

    def create_file(self):
        name = self.ui.nameLineEdit.text()
        comment = self.ui.commentLineEdit.text()
        icon = self.ui.iconLineEdit.text()
        command = self.ui.commandLineEdit.text()
        filepath = f"{str(Path.home())}/.local/share/applications/{name.lower().replace(' ', '-')}.desktop"

        if any([not name, not command]):
            self.show_message("Error", "Name or Command field is empty", QMessageBox.Warning)
        elif isfile(filepath):
            self.show_message("Error", f"{filepath} already exists", QMessageBox.Warning)
        else:
            if command.startswith("~/"):
                command = str(Path.home()) + command[1:]
            try:
                file = open(filepath, 'w')
                file.writelines(["[Desktop Entry]\n",
                                 f"Encoding=UTF-8\n"
                                 f"Name={name}\n",
                                 f"Comment={comment}\n",
                                 f"Icon={icon}\n",
                                 f"Exec={command}\n",
                                 "Type=Application"])
            except Exception as exception:
                self.show_message("Error", exception, QMessageBox.Critical)
            else:
                self.show_message("Success", "Success", QMessageBox.Information)
                self.clear_line_edits()

    def open_icon(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Select icon")
        if filename:
            self.ui.iconLineEdit.setText(filename)

    def show_message(self, title, text, icon):
        dialog = QMessageBox(self)
        dialog.setWindowTitle(title)
        dialog.setText(text)
        dialog.setIcon(icon)
        dialog.show()

    def clear_line_edits(self):
        self.ui.nameLineEdit.clear()
        self.ui.commentLineEdit.clear()
        self.ui.iconLineEdit.clear()
        self.ui.commandLineEdit.clear()

from MainWindow_ui import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QFileDialog
from pathlib import Path
from os.path import isfile


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.icon_button.pressed.connect(self.open_icon)
        self.command_button.pressed.connect(self.open_command)
        self.create_button.pressed.connect(self.create_file)

    def create_file(self):
        name = self.name_lineEdit.text()
        comment = self.comment_lineEdit.text()
        icon = self.icon_lineEdit.text()
        command = self.command_lineEdit.text()
        categories = self.categories_lineEdit.text()
        launch_in_terminal = self.launch_in_terminal_checkBox.isChecked()
        send_notification = self.send_notification_checkBox.isChecked()
        filepath = f"{str(Path.home())}/.local/share/applications/{name.lower().replace(' ', '-')}.desktop"

        if not (name and command):
            self.show_error("Name or Command field is empty")
        elif isfile(filepath):
            self.show_error(f"{filepath} already exists")
        else:
            if "~/" in command:
                if self.ask_question('Replace "~/"?', f'Replace "~/" to "{str(Path.home())}/" in the command?'):
                    command.replace("~/", str(Path.home()) + "/")  # replace "~/" to home directory path
            try:
                file = open(filepath, 'w')
                file.writelines(["[Desktop Entry]\n",
                                 f"Name={name}\n",
                                 f"Comment={comment}\n",
                                 f"Icon={icon}\n",
                                 f"Exec={command}\n",
                                 f"Categories={categories}\n"
                                 f"Terminal={str(launch_in_terminal).lower()}\n"
                                 f"StartupNotify={str(send_notification).lower()}\n"
                                 "Type=Application"])
            except Exception as exception:
                self.show_error(str(exception))
            else:
                self.show_message("Success", "Success")
                self.clear_line_edits()

    def open_icon(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Select icon")
        if filename:
            self.icon_lineEdit.setText(f'"{filename}"')

    def open_command(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Select file")
        if filename:
            self.command_lineEdit.setText(f'"{filename}"')

    def show_message(self, title: str, text: str):
        message_box = QMessageBox(self)
        message_box.setWindowTitle(title)
        message_box.setText(text)
        message_box.setIcon(QMessageBox.Information)
        message_box.setStandardButtons(QMessageBox.Ok)
        message_box.exec_()

    def show_error(self, message: str):
        message_box = QMessageBox(self)
        message_box.setWindowTitle("Error")
        message_box.setText(message)
        message_box.setIcon(QMessageBox.Critical)
        message_box.setStandardButtons(QMessageBox.Ok)
        message_box.exec_()

    def ask_question(self, title: str, message: str) -> bool:
        message_box = QMessageBox()
        answer = message_box.question(self, title, message, QMessageBox.No | QMessageBox.Yes)
        return answer == QMessageBox.Yes

    def clear_line_edits(self):
        self.name_lineEdit.clear()
        self.comment_lineEdit.clear()
        self.icon_lineEdit.clear()
        self.command_lineEdit.clear()
        self.categories_lineEdit.clear()

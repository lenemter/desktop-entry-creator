# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(550, 380)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(450, 380))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 380))
        MainWindow.setStyleSheet("* {\n"
"    color: #333;\n"
"}\n"
"\n"
"QMainWindow {\n"
"    background-color: #eee;\n"
"}\n"
"\n"
"QPushButton {\n"
"    padding: 6.5px 12px;\n"
"    border-radius: 4px;\n"
"    background-color: #fff;\n"
"    border: 1px solid #bbb;\n"
"}\n"
"\n"
"#icon_button, #command_button {\n"
"    padding: 8px 6px;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    padding: 6px;\n"
"    border-radius: 5px;\n"
"    border: 1px solid #bbb;\n"
"}")
        self.central_widget = QtWidgets.QWidget(MainWindow)
        self.central_widget.setObjectName("central_widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.central_widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.name_container = QtWidgets.QHBoxLayout()
        self.name_container.setObjectName("name_container")
        self.name_lable = QtWidgets.QLabel(self.central_widget)
        self.name_lable.setMinimumSize(QtCore.QSize(100, 0))
        self.name_lable.setMaximumSize(QtCore.QSize(100, 16777215))
        self.name_lable.setObjectName("name_lable")
        self.name_container.addWidget(self.name_lable)
        self.name_lineEdit = QtWidgets.QLineEdit(self.central_widget)
        self.name_lineEdit.setObjectName("name_lineEdit")
        self.name_container.addWidget(self.name_lineEdit)
        self.verticalLayout.addLayout(self.name_container)
        self.comment_container = QtWidgets.QHBoxLayout()
        self.comment_container.setObjectName("comment_container")
        self.comment_lable = QtWidgets.QLabel(self.central_widget)
        self.comment_lable.setMinimumSize(QtCore.QSize(100, 0))
        self.comment_lable.setMaximumSize(QtCore.QSize(100, 16777215))
        self.comment_lable.setObjectName("comment_lable")
        self.comment_container.addWidget(self.comment_lable)
        self.comment_lineEdit = QtWidgets.QLineEdit(self.central_widget)
        self.comment_lineEdit.setObjectName("comment_lineEdit")
        self.comment_container.addWidget(self.comment_lineEdit)
        self.verticalLayout.addLayout(self.comment_container)
        self.icon_container = QtWidgets.QHBoxLayout()
        self.icon_container.setObjectName("icon_container")
        self.icon_label = QtWidgets.QLabel(self.central_widget)
        self.icon_label.setMinimumSize(QtCore.QSize(100, 0))
        self.icon_label.setMaximumSize(QtCore.QSize(100, 16777215))
        self.icon_label.setObjectName("icon_label")
        self.icon_container.addWidget(self.icon_label)
        self.icon_lineEdit = QtWidgets.QLineEdit(self.central_widget)
        self.icon_lineEdit.setObjectName("icon_lineEdit")
        self.icon_container.addWidget(self.icon_lineEdit)
        self.icon_button = QtWidgets.QPushButton(self.central_widget)
        icon = QtGui.QIcon.fromTheme("document-open")
        self.icon_button.setIcon(icon)
        self.icon_button.setObjectName("icon_button")
        self.icon_container.addWidget(self.icon_button)
        self.verticalLayout.addLayout(self.icon_container)
        self.command_container = QtWidgets.QHBoxLayout()
        self.command_container.setObjectName("command_container")
        self.command_label = QtWidgets.QLabel(self.central_widget)
        self.command_label.setMinimumSize(QtCore.QSize(100, 0))
        self.command_label.setMaximumSize(QtCore.QSize(100, 16777215))
        self.command_label.setObjectName("command_label")
        self.command_container.addWidget(self.command_label)
        self.command_lineEdit = QtWidgets.QLineEdit(self.central_widget)
        self.command_lineEdit.setObjectName("command_lineEdit")
        self.command_container.addWidget(self.command_lineEdit)
        self.command_button = QtWidgets.QPushButton(self.central_widget)
        icon = QtGui.QIcon.fromTheme("document-open")
        self.command_button.setIcon(icon)
        self.command_button.setObjectName("command_button")
        self.command_container.addWidget(self.command_button)
        self.verticalLayout.addLayout(self.command_container)
        self.categories_container = QtWidgets.QHBoxLayout()
        self.categories_container.setObjectName("categories_container")
        self.categories_label = QtWidgets.QLabel(self.central_widget)
        self.categories_label.setMinimumSize(QtCore.QSize(100, 0))
        self.categories_label.setMaximumSize(QtCore.QSize(100, 16777215))
        self.categories_label.setObjectName("categories_label")
        self.categories_container.addWidget(self.categories_label)
        self.categories_lineEdit = QtWidgets.QLineEdit(self.central_widget)
        self.categories_lineEdit.setObjectName("categories_lineEdit")
        self.categories_container.addWidget(self.categories_lineEdit)
        self.verticalLayout.addLayout(self.categories_container)
        self.launch_in_terminal_checkBox = QtWidgets.QCheckBox(self.central_widget)
        self.launch_in_terminal_checkBox.setObjectName("launch_in_terminal_checkBox")
        self.verticalLayout.addWidget(self.launch_in_terminal_checkBox)
        self.send_notification_checkBox = QtWidgets.QCheckBox(self.central_widget)
        self.send_notification_checkBox.setObjectName("send_notification_checkBox")
        self.verticalLayout.addWidget(self.send_notification_checkBox)
        self.submit_button_container = QtWidgets.QHBoxLayout()
        self.submit_button_container.setObjectName("submit_button_container")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.submit_button_container.addItem(spacerItem)
        self.create_button = QtWidgets.QPushButton(self.central_widget)
        self.create_button.setObjectName("create_button")
        self.submit_button_container.addWidget(self.create_button)
        self.verticalLayout.addLayout(self.submit_button_container)
        MainWindow.setCentralWidget(self.central_widget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Desktop Entry Creator"))
        self.name_lable.setText(_translate("MainWindow", "Name:"))
        self.comment_lable.setText(_translate("MainWindow", "Comment:"))
        self.icon_label.setText(_translate("MainWindow", "Icon:"))
        self.command_label.setText(_translate("MainWindow", "Command:"))
        self.categories_label.setText(_translate("MainWindow", "Categories:"))
        self.launch_in_terminal_checkBox.setText(_translate("MainWindow", "Launch in terminal"))
        self.send_notification_checkBox.setText(_translate("MainWindow", "Send notification on startup"))
        self.create_button.setText(_translate("MainWindow", "Create"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

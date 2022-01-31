from controller.Frame import Frame
from PyQt5.QtCore import pyqtSignal
from controller.LoginValidationController import LoginValidationController
from controller.PathSelectionController import PathSelectionController
from service.BusinessModel import BusinessModel
from PyQt5.QtWidgets import QMessageBox


class LoginController(Frame):

    def __new__(cls, container):
        if not hasattr(cls, 'instance'):
            cls.instance = super(LoginController, cls).__new__(cls)
        return cls.instance

    def __init__(self, container):  
        self.ui_file_location = 'resources\\LoginView.ui'
        super().__init__(container)
        self.button_login.clicked.connect(self.button_login_on_action)

    def button_login_on_action(self):
        LoginValidationController.instance.show()
        username = self.textfield_username.text()
        password = self.textfield_password.text()
        if BusinessModel.instance.username_and_password_are_valid(username, password):
            BusinessModel.instance.set_username_and_password(username, password)
            PathSelectionController.instance.show()
        else:
            self.show()
            self.show_login_failure_dialog()

    def show_login_failure_dialog(self):
        dialog = QMessageBox()
        dialog.setWindowTitle("Anmeldeproblem")
        dialog.setText("Dein Benutzername oder dein Passwort war falsch.")
        dialog.exec_()

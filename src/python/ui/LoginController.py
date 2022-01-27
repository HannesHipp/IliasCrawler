from controller.Frame import Frame
from controller.Window import Window
from controller.PathSelectionController import PathSelectionController
from service.Database import Database
from service.Session import Session
from PyQt5.QtWidgets import QMessageBox

class LoginController(Frame):
    
    # Constructor

    def __new__(cls, container):
        if not hasattr(cls, 'instance'):
            cls.instance = super(LoginController, cls).__new__(cls)
        return cls.instance

    def __init__(self, container):  
        self.ui_file_location = 'C:\\Users\\Hannes\\Code Projekte\\IliasCrawler\\IliasCrawler\\view\\LoginView.ui'
        super().__init__(container)
        self.button_login.clicked.connect(self.button_login_on_action)

    # Button wiring

    def button_login_on_action(self):
        username = self.textfield_username.text()
        password = self.textfield_password.text()
        test_session = Session(username, password)
        if test_session.is_valid():
            Database.get_instance("login_data").add(username, password)
            PathSelectionController.instance.show()
        else:
            LoginController.show_login_failure_dialog()

    @staticmethod
    def show_login_failure_dialog():
        dialog = QMessageBox()
        dialog.setWindowTitle("Anmeldeproblem")
        dialog.setText("Dein Benutzername oder dein Passwort war falsch oder du hast keine Internetverbindung.")
        dialog.exec_()

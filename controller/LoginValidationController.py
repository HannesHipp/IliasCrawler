from controller.Frame import Frame
from controller.PathSelectionController import PathSelectionController
from service.Database import Database
from service.Session import Session
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import pyqtSignal

class LoginValidationController(Frame):

    request_validation = pyqtSignal()

    def __new__(cls, container):
        if not hasattr(cls, 'instance'):
            cls.instance = super(LoginValidationController, cls).__new__(cls)
        return cls.instance

    def __init__(self, container):   
        self.ui_file_location = 'C:\\Users\\Hannes\\Code Projekte\\IliasCrawler\\IliasCrawler\\resources\\LoginValidationView.ui'
        super().__init__(container)
        self.login_controller = None
        self.username = None
        self.password = None
        self.request_validation.connect(self.validate)

    def show(self):
        super().show()
        self.container.app.processEvents()
        self.request_validation.emit()
    
    def validate(self):
        print(self.username, self.password)
        test_session = Session(self.username, self.password)
        if test_session.is_valid:
            Database.instance.set_login_data(self.username, self.password)
            PathSelectionController.instance.show()
        else:
            self.login_controller.show()
            LoginValidationController.show_login_failure_dialog()

    @staticmethod
    def show_login_failure_dialog():
        dialog = QMessageBox()
        dialog.setWindowTitle("Anmeldeproblem")
        dialog.setText("Dein Benutzername oder dein Passwort war falsch oder du hast keine Internetverbindung.")
        dialog.exec_()


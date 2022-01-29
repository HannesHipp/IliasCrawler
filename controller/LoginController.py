from controller.Frame import Frame
from PyQt5.QtCore import pyqtSignal
from controller.LoginValidationController import LoginValidationController


class LoginController(Frame):
    
    send_login_data = pyqtSignal(str, str)

    def __new__(cls, container):
        if not hasattr(cls, 'instance'):
            cls.instance = super(LoginController, cls).__new__(cls)
        return cls.instance

    def __init__(self, container):  
        self.ui_file_location = 'C:\\Users\\Hannes\\Code Projekte\\IliasCrawler\\IliasCrawler\\resources\\LoginView.ui'
        super().__init__(container)
        self.button_login.clicked.connect(self.button_login_on_action)

    def button_login_on_action(self):
        LoginValidationController.instance.username = self.textfield_username.text()
        LoginValidationController.instance.password = self.textfield_password.text()
        LoginValidationController.instance.login_controller = self
        LoginValidationController.instance.show()

from controller.Frame import Frame
from PyQt5.QtCore import pyqtSignal


class LoginController(Frame):

    signal_request_login_data_validation = pyqtSignal(str, str)

    def __init__(self):  
        self.ui_file_location = 'resources\\LoginView.ui'
        super().__init__()
        self.button_login.clicked.connect(self.button_login_on_action)

    def button_login_on_action(self):
        username = self.textfield_username.text()
        password = self.textfield_password.text()
        self.signal_request_login_data_validation.emit(username, password)

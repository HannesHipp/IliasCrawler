from PyQt5.QtCore import pyqtSignal, QObject

from controller.Window import Window

class UIController(QObject):

    request_login_data_signal = pyqtSignal()

    def __init__(self, q_app):
        super().__init__()
        self.q_app = q_app
        self.window = Window()
        

    def process_request_user_data(self):
        self.request_login_data_signal.emit()

from controller.Frame import Frame
from controller.PathSelectionController import PathSelectionController
from service.Database import Database
from service.Session import Session
from PyQt5.QtWidgets import QMessageBox, QLabel
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QMovie

class LoginValidationController(Frame):

    def __new__(cls, container):
        if not hasattr(cls, 'instance'):
            cls.instance = super(LoginValidationController, cls).__new__(cls)
        return cls.instance

    def __init__(self, container):   
        self.ui_file_location = 'resources\\LoginValidationView.ui'
        super().__init__(container)






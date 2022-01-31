import time
from controller.Frame import Frame
from PyQt5.QtWidgets import QWidget
from PyQt5.uic import loadUi


class AutoStartController(QWidget):

    def __new__(cls, container):
        if not hasattr(cls, 'instance'):
            cls.instance = super(AutoStartController, cls).__new__(cls)
        return cls.instance

    def __init__(self, app):
        super().__init__()
        self.ui_file_location = 'resources\\AutoStartView.ui'
        loadUi(self.ui_file_location, self)
        self.app = app


             
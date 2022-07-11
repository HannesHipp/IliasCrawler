from PyQt5.QtWidgets import QWidget
from PyQt5.uic import loadUi
import resources.resources


class Frame(QWidget):
    
    def __init__(self):
        super().__init__()
        self.index = None
        loadUi(self.ui_file_location, self)


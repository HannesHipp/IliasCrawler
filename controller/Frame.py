from PyQt5.QtWidgets import QWidget
from PyQt5.uic import loadUi
import resources.resources


class Frame(QWidget):
    
    def __init__(self, container):
        super().__init__()
        self.index = None
        self.container = container
        loadUi(self.ui_file_location, self)

    def show(self):
        if self.index is None:
            self.container.add_frame(self)
        self.container.stackedWidget.setCurrentIndex(self.index)
        self.container.app.processEvents()


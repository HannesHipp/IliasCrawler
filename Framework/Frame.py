from functools import partial

import IliasCrawler.resources.resources

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget
from PyQt5.uic import loadUi


class Frame(QWidget):

    request = pyqtSignal()
    display = pyqtSignal(object)

    def __init__(self, path, *args, **kwargs):
        super().__init__()
        self.index = None
        loadUi(path)
        self.validationFrame = kwargs.pop('validatorFrame', None)
        if self.validationFrame:
            pass
            # set next frames
        self.uiElements = []
        for uiElement in args:
            self.uiElements.append(uiElement)
            uiElement.setQtElements(self)
        self.nextFrames = {}
        self.request.connect(self.handleRequest)

    def handleRequest(self):
        pass

    def show(self):
        self.display.emit(self)            

    def showNextFrame(self):
        self.nextFrame.request.emit()     
from functools import partial

import IliasCrawler.resources.resources

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget
from PyQt5.uic import loadUi


class Frame(QWidget):

    display = pyqtSignal(object)

    def __init__(self, path, *args, **kwargs):
        super().__init__()
        loadUi(path)
        self.index = None
        self.nextFrame = None
        self.uiElements = []
        for uiElement in args:
            self.uiElements.append(uiElement)
            uiElement.setQtElements(self)

        self.validationFrame = kwargs.pop('validatorFrame', None)
        self.function = kwargs.pop('validatorFrame', None)
        if self.function:
            self.function.done.connect(self.showNextFrame)
            self.function.error

    def show(self):
        self.display.emit(self)
        if self.function:
            self.function.run.emit()

    def showNextFrame(self):
        self.nextFrame.show()

    def showErrorMessage(self):
        print

    def connect(self, frame, button_name=None):
        if button_name:
            getattr(self, button_name).clicked.connect(frame.show)
        else:
            if not self.nextFrame:
                self.nextFrame = frame
            else:
                raise Exception("A default next frame has already been set.")

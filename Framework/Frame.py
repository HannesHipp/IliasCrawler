from functools import partial

import IliasCrawler.resources.resources

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget
from PyQt5.uic import loadUi


class Frame(QWidget):

    display = pyqtSignal(object)

    def __init__(self, path, *args, **kwargs):
        super().__init__()
        loadUi(path, self)
        self.index = None
        self.nextFrame = None
        self.prevFrame = None
        self.uiElements = []
        for uiElement in args:
            self.uiElements.append(uiElement)
            uiElement.setQtElements(self)

        self.validationFrame = kwargs.pop('validationFrame', None)
        self.function = kwargs.pop('function', None)
        if self.function:
            self.function.done.connect(self.showNextFrame)
            # self.function.error

    def show(self):
        self.display.emit(self)
        if self.function:
            self.function.start.emit()

    def showNextFrame(self):
        self.nextFrame.show()

    def showErrorMessage(self):
        print

    def connect(self, frame, button_name=None):
        if self.validationFrame:
            self.validationFrame.nextFrame = frame
            self.validationFrame.prevFrame = self
            frame = self.validationFrame
        if button_name:
            getattr(self, button_name).clicked.connect(frame.show)
        else:
            if self.nextFrame:
                raise Exception("A default next frame has already been set.")
            self.nextFrame = frame

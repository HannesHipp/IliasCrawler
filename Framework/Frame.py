import IliasCrawler.resources.resources

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget, QPushButton
from PyQt5.uic import loadUi

from Framework.Window import Window


class Frame(QWidget):

    display = pyqtSignal(object)

    def __init__(self, path, datapoints, buttonNames):
        super().__init__()
        loadUi(path, self)
        self.index = None
        self.buttons = self.getButtons(buttonNames)
        self.conditionButtons(self.buttons)
        self.datapoints = datapoints
        self.display.connect(Window.instance.selectFrame)
        self.prevFrame = None

    def getButtons(self, buttonNames: list[str]) -> list[QPushButton]:
        result = []
        for buttonName in buttonNames:
            button = getattr(self, buttonName)
            result.append(button)
        return result

    def conditionButtons(self, buttons: list[QPushButton]):
        for button in buttons:
            button.setCheckable(True)
            button.pressed.connect(self.finalize)

    def resetButtons(self):
        for button in self.buttons:
            button.setChecked(False)

    def finalize(self):
        nextFrame = self.decideNextFrame()
        self.resetButtons()
        errors = self.validateFrame()
        if len(errors) == 0:
            nextFrame.prevFrame = self
            nextFrame.show()
        else:
            self.showErrorMessage(errors)

    def validateFrame(self):
        errors = []
        for datapoint in self.datapoints:
            validationResult = datapoint.validate()
            if validationResult != True:
                errors.append(validationResult)
        return errors

    def showErrorMessage(self, errorMessages):
        print(errorMessages)

    def decideNextFrame(self):
        raise Exception(
            f"decideNextFrame method not implemented in {self.__class__.__name__}"
        )

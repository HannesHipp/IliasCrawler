from Framework.Datapoint import Datapoint
from Framework.Function import Function
from Framework.GuiModuls.GuiModul import GuiModul
import IliasCrawler.resources.resources

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget, QPushButton
from PyQt5.uic import loadUi

from Framework.Window import Window


class InputFrame(QWidget):

    display = pyqtSignal(object)

    def __init__(self, path: str, buttonNames: list[str]):
        super().__init__()
        loadUi(path, self)
        self.index = None
        self.buttons = self.setButtons(buttonNames)
        self.guiModuls = []
        self.display.connect(Window.instance.selectFrame)

    def setButtons(self, buttonNames: list[str]) -> list[QPushButton]:
        result = []
        for buttonName in buttonNames:
            button = getattr(self, buttonName)
            button.pressed.connect(self.finalize)
            result.append(button)
        return result

    def setGuiModuls(self, *guiModuls: GuiModul):
        self.guiModuls = guiModuls

    def show(self):
        for guiModul in self.guiModuls:
            guiModul.update()
        self.display.emit(self)

    def finalize(self):
        sender = self.sender()
        nextFrame = self.decideNextFrame(sender)
        errors = self.validateFrame()
        if len(errors) == 0:
            nextFrame.show()
        else:
            self.showErrorMessage(errors)

    def validateFrame(self):
        errors = []
        for guimodul in self.guiModuls:
            errors.extend(guimodul.validate())
        return errors

    def showErrorMessage(self, errorMessages):
        print(errorMessages)

    def decideNextFrame(self):
        raise Exception(
            f"decideNextFrame method not implemented in {self.__class__.__name__}"
        )

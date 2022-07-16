import os
import sys
from PyQt5.QtCore import QObject, pyqtSignal, QThreadPool
from PyQt5.QtWidgets import QApplication
from Framework.InputDatapoint import InputDatapoint

from Framework.Window import Window
from Framework.Validator import Validator



class App(QObject):

    def __init__(self) -> None:
        super().__init__()
        os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
        self.qApp = QApplication(sys.argv)
        self.window = Window()
        self.threadpool = QThreadPool()
        self.functions = []
        self.validators = []
        self.inputDatapoints = []
        self.outputDatapoints = []

    def addFunction(self, function):
        function.threadpool = self.threadpool
        if isinstance(function, Validator):
            self.validators.append(function)
        else:
            self.functions.append(function)
        self.makeConnections(function)
        if function.outputDatapoint:
            self.addOutputDatapoint(function.outputDatapoint)
        for datapoint in function.inputDatapoints:
            if isinstance(datapoint, InputDatapoint) and datapoint not in self.inputDatapoints:
                self.addInputDatapoint(datapoint)

    def addOutputDatapoint(self, datapoint):
        self.outputDatapoints.append(datapoint)
        self.makeConnections(datapoint)

    def addInputDatapoint(self, datapoint):
        self.inputDatapoints.append(datapoint)
        self.makeConnections(datapoint)

    def makeConnections(self, object):
        object.display.connect(self.window.selectFrame)
        object.sendError.connect(self.showError)
        object.done.connect(self.decideWhatToDo)

    def start(self):
        self.decideWhatToDo()
        sys.exit(self.qApp.exec_())

    def decideWhatToDo(self):
        result = None
        for option in [self.validators, self.inputDatapoints, self.functions, self.outputDatapoints]:
            if result is not None:
                break
            else:
                for element in option:
                    if result is not None:
                        break
                    else:
                        if element.canBeRequested():
                            result = element
        result.request.emit()

    def showError(self, message):
        print(message)
    
    def cock(self):
        print("""p n the v wird freigesetzt
        #doityourself
        #freecock
        #ANDFUCKINGFREEBOOOOOOOOBS
        SHOW BOOBS PICS AND print
        .vars""")



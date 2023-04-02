from Framework.Frame import Frame
from Framework.Function import Function

from PyQt5.QtCore import QThreadPool


class OutputFrame(Frame):

    def __init__(self, path, datapoints, buttonNames, function: Function):
        super().__init__(path, datapoints, buttonNames)
        self.function = function
        self.function.setAutoDelete(False)
        self.function.signals.done.connect(self.finalize)
        self.function.signals.error.connect(self.showErrorMessage)

    def show(self):
        self.display.emit(self)
        QThreadPool.globalInstance().start(self.function)

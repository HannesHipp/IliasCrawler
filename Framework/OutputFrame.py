from Framework.InputFrame import InputFrame
from Framework.Function import Function

from PyQt5.QtCore import QThreadPool


class OutputFrame(InputFrame):

    def __init__(self, path, function: Function, buttonNames=[]):
        super().__init__(path, buttonNames)
        self.function = function
        self.function.setAutoDelete(False)
        self.function.signals.done.connect(self.finalize)
        self.function.signals.error.connect(self.showErrorMessage)

    def show(self):
        super().show()
        QThreadPool.globalInstance().start(self.function)

    def finalize(self):
        self.function.cancel = True
        super().finalize()

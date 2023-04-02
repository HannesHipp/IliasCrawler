import sys
import traceback
from PyQt5.QtCore import QObject, QRunnable, pyqtSignal, pyqtSlot


class FunctionSignals(QObject):

    error = pyqtSignal(str)
    done = pyqtSignal()


class Function(QRunnable):

    def __init__(self) -> None:
        super().__init__()
        self.signals = FunctionSignals()

    @pyqtSlot()
    def run(self):
        try:
            self.execute()
            self.signals.done.emit()
        except:
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit(
                str(exctype, value, traceback.format_exc()))

    def execute(self):
        raise Exception(
            f"execute-method not implemented for function {self.__class__.__name__}")

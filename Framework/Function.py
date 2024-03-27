import sys
import traceback
from PyQt5.QtCore import QObject, QRunnable, pyqtSignal, pyqtSlot, QThreadPool


class FunctionSignals(QObject):

    ended = pyqtSignal()


class Function(QRunnable):

    def __init__(self) -> None:
        super().__init__()
        self.signals = FunctionSignals()
        self.canceled = False
        self.error = None

    def start_execution(self):
        QThreadPool.globalInstance().start(self)

    @pyqtSlot()
    def run(self):
        try:
            self.execute()
        except:
            traceback.print_exc()
            value = sys.exc_info()[:2]
            self.error = str((value, traceback.format_exc()))
        self.signals.ended.emit()

    def cancel_execution(self):
        self.canceled = True

    def execute(self):
        raise Exception(
            f"execute-method not implemented for function {self.__class__.__name__}")

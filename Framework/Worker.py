import sys
import traceback
from PyQt5.QtCore import QObject, QRunnable, pyqtSignal, pyqtSlot
from Framework.Validator import ValidationError


class WorkerSignals(QObject):

    error = pyqtSignal(str)
    done = pyqtSignal(object)


class Worker(QRunnable):

    def __init__(self, function, datapoints):
        super(Worker, self).__init__()
        self.fn = function
        self.datapoints = datapoints
        self.signals = WorkerSignals()

    @pyqtSlot()
    def run(self):
        try:
            self.fn(*self.datapoints)
            self.signals.done.emit()
        except ValidationError:
            message =
        except:
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit((exctype, value, traceback.format_exc()))

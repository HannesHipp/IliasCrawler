from PyQt5.QtCore import QObject, QRunnable, pyqtSignal, pyqtSlot


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
        self.fn(*self.datapoints)
        self.signals.done.emit()

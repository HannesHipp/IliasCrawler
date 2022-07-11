from PyQt5.QtCore import QObject, QRunnable, pyqtSignal, pyqtSlot

class WorkerSignals(QObject):

    result = pyqtSignal(object)
    progress = pyqtSignal(tuple)


class Worker(QRunnable):

    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()
        self.fn = fn
        self.signals = WorkerSignals()

    @pyqtSlot()
    def run(self):
        result = self.fn(progress_signal=self.signals.progress)
        self.signals.result.emit(result)
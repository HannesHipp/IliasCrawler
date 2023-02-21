from PyQt5.QtCore import QObject, pyqtSignal, QThreadPool


from Framework.Worker import Worker


class Function(QObject):

    start = pyqtSignal()
    error = pyqtSignal(str)
    done = pyqtSignal()

    def __init__(self, *datapoints) -> None:
        super().__init__()
        self.worker = Worker(self.execute, *datapoints)
        self.worker.signals.done.connect(self.finishedThread)
        self.start.connect(self.run)

    def run(self):
        QThreadPool.globalInstance().start(self.worker)

    def finishedThread(self):
        self.done.emit()

    def errorOccured(self, message):
        self.error.emit(message)

    def execute(self):
        raise Exception(
            f"execute-method not implemented for function {self.__class__.__name__}")

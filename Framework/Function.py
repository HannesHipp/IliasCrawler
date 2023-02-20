from PyQt5.QtCore import QObject, pyqtSignal, QThreadPool


from Framework.Worker import Worker


class Function(QObject):

    run = pyqtSignal()
    error = pyqtSignal(str)
    done = pyqtSignal()

    def __init__(self, *datapoints) -> None:
        super().__init__()
        self.datapoints = datapoints
        self.run.connect(self.runFunction)

    def runFunction(self):
        worker = Worker(self.execute, self.datapoints)
        worker.signals.done.connect(self.finishedThread)
        threadpool = QThreadPool.globalInstance()
        threadpool.start(worker)

    def finishedThread(self):
        self.done.emit()

    def errorOccured(self, message):
        self.error.emit(message)

    def execute(self):
        raise Exception(
            f"execute-method not implemented for function {self.__class__.__name__}")

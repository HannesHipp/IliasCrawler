from PyQt5.QtCore import QObject, pyqtSignal, QThreadPool


from Framework.Worker import Worker


class Function(QObject):

    done = pyqtSignal()

    def __init__(self, *args) -> None:
        super().__init__()
        self.args = args

    def handleRequest(self):
        threadpool = QThreadPool.globalInstance()
        worker = Worker(self.execute)
        worker.signals.result.connect(self.finishedThread)
        worker.signals.progress.connect(self.updateFrame)
        threadpool.start(worker)

    def finishedThread(self):
        self.done.emit()
    
    def updateFrame(self, tuple):
        pass

    def execute(self):
        raise Exception(f"execute-method not implemented for function {self.__class__.__name__}")

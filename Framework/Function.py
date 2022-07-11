from PyQt5.QtCore import QObject, pyqtSignal

from Framework.Worker import Worker


class Function(QObject):

    request = pyqtSignal()
    display = pyqtSignal(object)
    sendError = pyqtSignal(str)
    done = pyqtSignal()

    def __init__(self, **kwargs) -> None:
        super().__init__()
        self.outputDatapoint = kwargs.pop('result', None)
        self.frame = kwargs.pop('frame')
        self.inputDatapoints = [kwargs[arg] for arg in kwargs]
        self.threadpool = None
        self.request.connect(self.startThread)

    def canBeRequested(self):
        result = True
        for datapoint in self.inputDatapoints:
            result = result and datapoint.value is not None
        return result

    def startThread(self):
        self.displayFrame()
        worker = Worker(self.execute)
        worker.signals.result.connect(self.saveResult)
        worker.signals.progress.connect(self.updateFrame)
        self.threadpool.start(worker)

    def saveResult(self, result):
        self.outputDatapoint.calculatedValue = result

    def displayFrame(self):
        self.display.emit(self.frame)
    
    def updateFrame(self, tuple):
        pass

    def execute(self):
        raise Exception(f"execute-method not implemented for function {self.__class__.__name__}")

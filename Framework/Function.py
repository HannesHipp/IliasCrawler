from PyQt5.QtCore import QObject, pyqtSignal
from Framework.Datapoint import Datapoint
from Framework.OutputDatapoint import OutputDatapoint

from Framework.Worker import Worker


class Function(QObject):

    request = pyqtSignal()
    display = pyqtSignal(object)
    sendError = pyqtSignal(str)
    done = pyqtSignal()

    def __init__(self, **kwargs) -> None:
        super().__init__()
        outputDatapoint = kwargs.pop('result', None)
        if outputDatapoint:
            if not isinstance(outputDatapoint, OutputDatapoint):
                raise Exception(f"Output datapoint of {self.__class__.__name__} function is not of type OutputDatapoint")
        self.outputDatapoint = outputDatapoint
        self.frame = kwargs.pop('frame')
        inputDatapoints = [kwargs[arg] for arg in kwargs]
        for datapoint in inputDatapoints:
            if type(datapoint) is Datapoint:
                raise Exception(f"Input datapoint of {self.__class__.__name__} function must be either of type InputDatapoint or OutputDatapoint")
        self.inputDatapoints = inputDatapoints
        self.threadpool = None
        self.request.connect(self.startThread)

    def canBeRequested(self):
        result = True
        for datapoint in self.inputDatapoints:
            result = result and datapoint.value is not None
        if self.outputDatapoint:
            result = result and self.outputDatapoint.calculatedValue is None
        return result

    def startThread(self):
        self.displayFrame()
        worker = Worker(self.execute)
        worker.signals.result.connect(self.saveResult)
        worker.signals.progress.connect(self.updateFrame)
        self.threadpool.start(worker)

    def saveResult(self, result):
        self.outputDatapoint.calculatedValue = result
        self.outputDatapoint.request.emit()

    def displayFrame(self):
        self.display.emit(self.frame)
    
    def updateFrame(self, tuple):
        pass

    def execute(self):
        raise Exception(f"execute-method not implemented for function {self.__class__.__name__}")

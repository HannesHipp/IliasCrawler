from PyQt5.QtCore import pyqtSignal

from Framework.Function import Function

class Validator(Function):

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    def canBeRequested(self):
        result = True
        for datapoint in self.inputDatapoints:
            result = result and datapoint.valueToBeValidated is not None
        return result

    def execute(self, progress_signal):
        valid, error = self.validate()
        return (valid, error)
        
    def saveResult(self, result):
        (valid, error) = result
        if valid:
            for datapoint in self.inputDatapoints:
                datapoint.setValue(datapoint.valueToBeValidated)  
                datapoint.valueToBeValidated = None 
        else:
            for datapoint in self.inputDatapoints:
                datapoint.valueToBeValidated = None
            self.sendError.emit(error)
        self.done.emit()
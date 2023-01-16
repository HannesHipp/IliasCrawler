from PyQt5.QtCore import pyqtSignal

from Framework.Function import Function

class Validator(Function):

    done = pyqtSignal(tuple)

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    def execute(self, progress_signal):
        valid, error = self.validate(*self.valuesToValidate)
        return (valid, error)
        
    def finishedThread(self, result):
        (valid, error) = result
        for 
        self.done.emit()
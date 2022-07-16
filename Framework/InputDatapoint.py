from PyQt5.QtCore import QObject, pyqtSignal
from Framework.Datapoint import Datapoint


class InputDatapoint(Datapoint):

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    def canBeRequested(self):
        return self.value is None and self.valueToBeValidated is None

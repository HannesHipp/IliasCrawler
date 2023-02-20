from Framework.Datapoint import Datapoint
from PyQt5.QtWidgets import QTextEdit


class TextField:

    def __init__(self, datapoint: Datapoint, qtElementName: str) -> None:
        self.datapoint = datapoint
        self.qtElement = None
        self.qtElementName = qtElementName

    def setQtElements(self, frame):
        self.qtElement = getattr(frame, self.qtElementName)
        self.qtElement.textChanged.connect(self.datapoint.setValue)

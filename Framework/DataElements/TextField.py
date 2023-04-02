from Framework.Datapoint import Datapoint
from PyQt5.QtWidgets import QTextEdit


class TextField:

    def __init__(self, datapoint: Datapoint, qtElement: QTextEdit) -> None:
        qtElement.textChanged.connect(datapoint.updateValue)

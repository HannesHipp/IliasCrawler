from easygui import diropenbox
from Framework.Datapoint import Datapoint
from PyQt5.QtWidgets import QLabel, QPushButton, QWidget
from PyQt5.QtCore import QObject, Qt


class PathSelector:

    def __init__(self, datapoint: Datapoint, qtLineEdit: QLabel, qtButton: QPushButton) -> None:
        self.datapoint = datapoint
        self.qtLineEdit = qtLineEdit
        datapoint.valueChanged.connect(self.updateLineEdit)
        qtButton.clicked.connect(self.selectPath)

    def selectPath(self):
        path = diropenbox()
        self.datapoint.updateValue(path)

    def updateLineEdit(self):
        self.qtLineEdit.setText(str(self.datapoint.value))

from easygui import diropenbox
from Framework.Datapoint import Datapoint
from PyQt5.QtWidgets import QLabel, QPushButton, QWidget
from PyQt5.QtCore import QObject, Qt

from Framework.GuiModuls.GuiModul import GuiModul


class PathSelector(GuiModul):

    def __init__(self, datapoint: Datapoint, qtLineEdit: QLabel, qtButton: QPushButton) -> None:
        super().__init__([datapoint])
        self.datapoint = datapoint
        self.qtLineEdit = qtLineEdit
        qtButton.clicked.connect(self.publish)

    def publish(self):
        path = diropenbox()
        self.datapoint.updateValue(path)
        self.qtLineEdit.setText(str(path))

    def update(self):
        self.qtLineEdit.setText(str(self.datapoint.value))

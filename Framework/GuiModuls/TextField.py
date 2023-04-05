from Framework.Datapoint import Datapoint
from PyQt5.QtWidgets import QLineEdit

from Framework.GuiModuls.GuiModul import GuiModul


class TextField(GuiModul):

    def __init__(self, datapoint: Datapoint, qtTextEdit: QLineEdit) -> None:
        super().__init__([datapoint])
        self.datapoint = datapoint
        self.qtTextEdit = qtTextEdit
        qtTextEdit.textChanged.connect(self.publish)

    def publish(self):
        self.datapoint.updateValue(self.qtTextEdit.text())

    def update(self):
        self.qtTextEdit.setText(self.datapoint.value)

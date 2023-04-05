from Framework.Datapoint import Datapoint
from PyQt5.QtWidgets import QLabel
from Framework.GuiModuls.GuiModul import GuiModul


class TextLabel(GuiModul):

    def __init__(self, datapoint: Datapoint, qtLabel: QLabel, func) -> None:
        super().__init__([datapoint])
        self.datapoint = datapoint
        self.qtLabel = qtLabel
        self.func = func
        self.datapoint.valueChanged.connect(self.update)

    def update(self):
        value = self.func(self.datapoint.value)
        self.qtLabel.setText(str(value))

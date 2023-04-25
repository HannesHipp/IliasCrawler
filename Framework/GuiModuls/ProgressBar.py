from Framework.Datapoint import Datapoint
from PyQt5.QtWidgets import QProgressBar, QLabel
from PyQt5.QtCore import Qt

from Framework.GuiModuls.GuiModul import GuiModul


class ProgressBar(GuiModul):

    def __init__(self, datapoint: Datapoint, qtProgressBar: QProgressBar, qtPercentageLabel: QLabel, function) -> None:
        super().__init__([datapoint])
        datapoint.valueChanged.connect(self.update)
        self.datapoint = datapoint
        self.qtProgressbar = qtProgressBar
        self.qtPercentageLabel = qtPercentageLabel
        self.function = function

    def update(self):
        value = self.function(self.datapoint.value)
        self.qtPercentageLabel.setText(str(value))
        self.qtProgressbar.setValue(value)

from Framework.Datapoint import Datapoint
from PyQt5.QtWidgets import QProgressBar, QLabel
from PyQt5.QtCore import Qt

from Framework.GuiModuls.GuiModul import GuiModul


class ProgressBar(GuiModul):

    def __init__(self, datapoint: Datapoint, qtProgressBar: QProgressBar, qtPercentageLabel: QLabel, func) -> None:
        super().__init__(
            datapoint=datapoint
        )
        self.qtProgressbar = qtProgressBar
        self.qtPercentageLabel = qtPercentageLabel
        self.func = func

    def set_value(self, value):
        percentage = self.func(value)
        self.qtPercentageLabel.setText(str(percentage))
        self.qtProgressbar.setValue(percentage)

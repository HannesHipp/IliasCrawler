from Framework.Datapoint import Datapoint
from PyQt5.QtWidgets import QProgressBar, QLabel
from PyQt5.QtCore import Qt

from Framework.GuiModuls.GuiModul import GuiModul


class ProgressBar(GuiModul):

    def __init__(self, percentage: Datapoint, qtProgressBar: QProgressBar, qtPercentageLabel: QLabel) -> None:
        super().__init__(
            datapoint=percentage
        )
        self.qtProgressbar = qtProgressBar
        self.qtPercentageLabel = qtPercentageLabel

    def set_value(self, value):
        if not value:
            value = 0
        self.qtPercentageLabel.setText(str(value))
        self.qtProgressbar.setValue(value)

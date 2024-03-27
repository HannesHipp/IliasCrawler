from Framework.Datapoint import Datapoint
from PyQt5.QtWidgets import QLabel
from Framework.GuiModuls.GuiModul import GuiModul


class TextLabel(GuiModul):

    def __init__(self, datapoint: Datapoint, qtLabel: QLabel, func) -> None:
        super().__init__(
            datapoint=datapoint
        )
        self.qtLabel = qtLabel
        self.func = func

    def set_value(self, value):
        self.qtLabel.setText(str(self.func(value)))

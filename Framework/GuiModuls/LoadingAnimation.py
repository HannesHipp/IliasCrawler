from Framework.Datapoint import Datapoint
from Framework.GuiModuls.GuiModul import GuiModul


class LoadingAnimation(GuiModul):

    def __init__(self, datapoint: Datapoint, qtAnimation) -> None:
        super().__init__([datapoint])
        self.datapoint = datapoint
        self.qtAnimation = qtAnimation

    def update(self):
        pass

from Framework.Datapoint import Datapoint
from Framework.GuiModuls.GuiModul import GuiModul


class LoadingAnimation(GuiModul):

    def __init__(self, function, qtAnimation) -> None:
        super().__init__([])
        self.function = function
        self.qtAnimation = qtAnimation

    def update(self):
        pass

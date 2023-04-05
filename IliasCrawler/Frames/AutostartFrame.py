from Framework.GuiModuls.TextLabel import TextLabel
from Framework.OutputFrame import OutputFrame
from Framework.Function import Function
from Framework.Datapoint import Datapoint
from time import sleep


class AutostartCountdown(Function):

    def __init__(self, timer: Datapoint) -> None:
        super().__init__()
        self.timer = timer

    def execute(self):
        time = 10
        while time != 0:
            sleep(1.0)
            time = time - 1
            self.timer.updateValue(time)


class AutostartFrame(OutputFrame):

    def __init__(self):
        autostartTimer = Datapoint(save=False)
        super().__init__(
            path="IliasCrawler\\resources\\AutoStartView.ui",
            function=AutostartCountdown(autostartTimer),
            buttonNames=['button_cancel', 'button_start']
        )
        self.setGuiModuls(
            TextLabel(autostartTimer,  self.label_timer, lambda x: x))

    def addNextFrames(self, courseSelectionFrame, crawlingFrame):
        self.courseSelectionFrame = courseSelectionFrame
        self.crawlingFrame = crawlingFrame

    def decideNextFrame(self):
        if self.button_cancel.checked:
            return self.courseSelectionFrame
        return self.crawlingFrame

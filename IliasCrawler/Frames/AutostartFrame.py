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
        while time != 0 and not self.cancel:
            print(time)
            self.timer.submit_value(time)
            sleep(1.0)
            time = time - 1


class AutostartFrame(OutputFrame):

    def __init__(self):
        autostartTimer = Datapoint(save=False)
        super().__init__(
            path="IliasCrawler\\resources\\AutoStartView.ui",
            function=AutostartCountdown(autostartTimer),
            next_frame_button_names=['button_cancel', 'button_start']
        )
        self.add_module(
            TextLabel(autostartTimer,  self.label_timer, lambda x: x)
        )

    def addNextFrames(self, courseSelectionFrame, crawlingFrame):
        self.courseSelectionFrame = courseSelectionFrame
        self.crawlingFrame = crawlingFrame

    def decide_next_frame(self, pressedButton):
        if pressedButton == self.button_cancel:
            return self.courseSelectionFrame
        return self.crawlingFrame

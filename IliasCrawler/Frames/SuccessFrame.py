from Framework.Datapoint import Datapoint
from Framework.Frame import Frame
from Framework.GuiModuls.TextLabel import TextLabel
from IliasCrawler.Datapoints.Courses import Courses
from IliasCrawler.Datapoints.FilesAndVideos import FilesAndVideos


class SuccessFrame(Frame):

    def __init__(self):
        super().__init__(
            path="IliasCrawler\\resources\\SuccessView.ui",
        )

    def decide_next_frame(self, pressedButton):
        return None
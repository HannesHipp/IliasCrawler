from Framework.GuiModuls.ObjectSelectionList import ObjectSelectionList
from Framework.Frame import Frame

from IliasCrawler.Datapoints.Courses import Courses


class CourseSelectionFrame(Frame):

    def __init__(self, courses: Courses):
        super().__init__(
            path="IliasCrawler\\resources\\CourseSelectionView.ui",
            next_frame_button_names=['button_select_choice']
        )
        self.courses = courses
        self.add_module(
            ObjectSelectionList(courses, self.listView,
                                'name', "to_download", "is_new")
        )

    def addNextFrames(self, crawlingFrame):
        self.crawlingFrame = crawlingFrame

    def decide_next_frame(self, pressedButton):
        return self.crawlingFrame

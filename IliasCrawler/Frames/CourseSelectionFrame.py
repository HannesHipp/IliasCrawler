from Framework.GuiModuls.ObjectSelectionList import ObjectSelectionList
from Framework.InputFrame import Frame

from IliasCrawler.Datapoints.Courses import Courses


class CourseSelectionFrame(Frame):

    def __init__(self, courses: Courses):
        super().__init__(
            path="IliasCrawler\\resources\\CourseSelectionView.ui",
            buttonNames=['button_select_choice']
        )
        self.courses = courses
        self.addModule(
            ObjectSelectionList(courses, self.listView,
                                'name', "shouldBeDownloaded", "isNew")
        )

    def addNextFrames(self, crawlingFrame):
        self.crawlingFrame = crawlingFrame

    def decideNextFrame(self, pressedButton):
        return self.crawlingFrame

from Framework.GuiModuls.ObjectSelectionList import ObjectSelectionList
from Framework.InputFrame import InputFrame

from IliasCrawler.Datapoints.Courses import Courses


class CourseSelectionFrame(InputFrame):

    def __init__(self, courses: Courses):
        super().__init__(
            path="IliasCrawler\\resources\\CourseSelectionView.ui",
            buttonNames=['button_select_choice']
        )
        self.courses = courses
        self.setGuiModuls(
            ObjectSelectionList(courses, self.listView,
                                'name', "shouldBeDownloaded", "isNew")
        )

    def addNextFrames(self, courseSelectionFrame, autostartFrame):
        self.courseSelectionFrame = courseSelectionFrame
        self.autostartFrame = autostartFrame

    def decideNextFrame(self):
        hasNewCourses = False
        for course in self.courses.value:
            if course.isNew:
                hasNewCourses = True
                break
        if not hasNewCourses and self.autostart.value:
            return self.autostartFrame
        else:
            return self.courseSelectionFrame

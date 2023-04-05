from Framework.OutputFrame import OutputFrame

from IliasCrawler.Functions.GetCourses import GetCourses


class GetCoursesFrame(OutputFrame):

    def __init__(self, username, password, courses, autostart):
        super().__init__(
            path="IliasCrawler\\resources\\CourseLoadingView.ui",
            function=GetCourses(username, password, courses)
        )
        self.courses = courses
        self.autostart = autostart

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

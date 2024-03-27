from Framework.OutputFrame import OutputFrame

from IliasCrawler.Functions.GetCourses import GetCourses


class GetCoursesFrame(OutputFrame):

    def __init__(self, username, password, courses, autostart):
        super().__init__(
            path="IliasCrawler\\resources\\GetCoursesView.ui",
            function=GetCourses(username, password, courses)
        )
        self.courses = courses
        self.autostart = autostart

    def addNextFrames(self, courseSelectionFrame, autostartFrame):
        self.courseSelectionFrame = courseSelectionFrame
        self.autostartFrame = autostartFrame

    def decide_next_frame(self, pressed_button):
        has_new_courses = False
        for course in self.courses.value:
            if course.is_new:
                has_new_courses = True
                break
        if not has_new_courses and self.autostart.value:
            return self.autostartFrame
        else:
            return self.courseSelectionFrame

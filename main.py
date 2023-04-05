from Framework.App import App

from IliasCrawler.Datapoints.Username import Username
from IliasCrawler.Datapoints.Password import Password
from IliasCrawler.Datapoints.Courses import Courses
from IliasCrawler.Datapoints.FilesAndVideos import FilesAndVideos
from IliasCrawler.Datapoints.Path import Path
from IliasCrawler.Datapoints.Autostart import Autostart

from IliasCrawler.Frames.LoginFrame import LoginFrame
from IliasCrawler.Frames.LoginValidationFrame import LoginValidationFrame
from IliasCrawler.Frames.PathFrame import PathFrame
from IliasCrawler.Frames.GetCoursesFrame import GetCoursesFrame
from IliasCrawler.Frames.CourseSelectionFrame import CourseSelectionFrame
from IliasCrawler.Frames.AutostartFrame import AutostartFrame

app = App()

username = Username()
password = Password()
path = Path()
courses = Courses()
autostart = Autostart()
autostart.updateValue(True)
# filesAndVideos = FilesAndVideos()


loginFrame = LoginFrame(username, password)
loginValidationFrame = LoginValidationFrame(username, password)
pathFrame = PathFrame(path)
getCoursesFrame = GetCoursesFrame(username, password, courses, autostart)
courseSelectionFrame = CourseSelectionFrame(courses)
autostartFrame = AutostartFrame()


loginFrame.addNextFrames(loginValidationFrame)
loginValidationFrame.addNextFrames(pathFrame)
pathFrame.addNextFrames(getCoursesFrame)
getCoursesFrame.addNextFrames(courseSelectionFrame, autostartFrame)
courseSelectionFrame.addNextFrames(autostartFrame, autostartFrame)
autostartFrame.addNextFrames(courseSelectionFrame, courseSelectionFrame)

app.startWith(autostartFrame)

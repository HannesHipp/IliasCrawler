from Framework.App import App

from IliasCrawler.Datapoints.Username import Username
from IliasCrawler.Datapoints.Password import Password
from IliasCrawler.Datapoints.Courses import Courses
from IliasCrawler.Datapoints.FilesAndVideos import FilesAndVideos
from IliasCrawler.Datapoints.Path import Path
from IliasCrawler.Datapoints.Autostart import Autostart

from IliasCrawler.Frames.CrawlingFrame import CrawlingFrame
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
autostart.updateValue(False)
filesAndVideos = FilesAndVideos()


loginFrame = LoginFrame(username, password)
loginValidationFrame = LoginValidationFrame(username, password)
pathFrame = PathFrame(path)
getCoursesFrame = GetCoursesFrame(username, password, courses, autostart)
courseSelectionFrame = CourseSelectionFrame(courses)
autostartFrame = AutostartFrame()
crawlingFrame = CrawlingFrame(courses, filesAndVideos)


loginFrame.addNextFrames(loginValidationFrame)
loginValidationFrame.addNextFrames(loginFrame, pathFrame)
pathFrame.addNextFrames(getCoursesFrame)
getCoursesFrame.addNextFrames(courseSelectionFrame, autostartFrame)
courseSelectionFrame.addNextFrames(crawlingFrame)
autostartFrame.addNextFrames(courseSelectionFrame, crawlingFrame)

if username.value and password.value and path.value:
    app.startWith(getCoursesFrame)
else:
    app.startWith(loginFrame)

# adfgbadfb

from Framework.App import App

from IliasCrawler.Datapoints.Username import Username
from IliasCrawler.Datapoints.Password import Password
from IliasCrawler.Datapoints.Courses import Courses
from IliasCrawler.Datapoints.FilesAndVideos import FilesAndVideos
from IliasCrawler.Datapoints.Path import Path

from IliasCrawler.Frames.LoginFrame import LoginFrame
from IliasCrawler.Frames.LoginValidationFrame import LoginValidationFrame
from IliasCrawler.Frames.PathFrame import PathFrame

from IliasCrawler.Functions.ValidateLogin import ValidateLogin


app = App()

username = Username()
password = Password()
path = Path()
# courses = Courses()
# filesAndVideos = FilesAndVideos()


loginFrame = LoginFrame(username, password)
loginValidationFrame = LoginValidationFrame(username, password)
pathFrame = PathFrame(path)


loginFrame.addNextFrames(loginValidationFrame)
loginValidationFrame.addNextFrames(pathFrame)

app.startWith(loginFrame)

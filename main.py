from Framework.App import App
from Framework.Frame import Frame
from Framework.InputFrame import InputFrame
from Framework.NoUiFrame import NoUiFrame
from Framework.OutputFrame import OutputFrame

from IliasCrawler.Datapoints.Username import Username
from IliasCrawler.Datapoints.Password import Password
from IliasCrawler.Datapoints.Courses import Courses
from IliasCrawler.Datapoints.FilesAndVideos import FilesAndVideos
from IliasCrawler.Datapoints.Path import Path

from IliasCrawler.Functions.GetCourses import GetCourses
from IliasCrawler.Functions.Crawl import Crawl
from IliasCrawler.Functions.Download import Download

from IliasCrawler.Validators.ValidateLogin import ValidateLogin


app = App()

username = Username()
password = Password()
path = Path()
courses = Courses()
filesAndVideos = FilesAndVideos()


loginFrame = Frame(
    path = "IliasCrawler\\resources\\LoginView.ui",
    textfield_username = username, 
    textfield_password = password,
    validators = [ValidateLogin(username, password)]
)
pathFrame = Frame(
    path = "IliasCrawler\\resources\\PathSelectionView.ui",
    button_select_path = path
)
getCoursesFrame = Frame(
    path = "IliasCrawler\\resources\\CourseLoadingView.ui",
    function = GetCourses(username, password)
)
coursesFrame = Frame(
    path = "IliasCrawler\\resources\\CourseSelectionView.ui",
    listView = courses
)
crawlingFrame = Frame(
    path = "IliasCrawler\\resources\\CrawlingView.ui",
    function = Crawl(username, courses, password)
)
filesAndVideosFrame = Frame(
    filesAndVideos
)
downloadingFrame = Frame(
    path = "IliasCrawler\\resources\\DownloadingView.ui",
    function = Download(username, password, path, filesAndVideos)
)

loginFrame.connect(pathFrame, 'button_login')
pathFrame.connect(getCoursesFrame, 'button_select_path')
getCoursesFrame.connect(coursesFrame)
coursesFrame.connect(crawlingFrame, 'button_select_choice')
crawlingFrame.connect(filesAndVideosFrame)
filesAndVideosFrame.connect(downloadingFrame)

app.addFrame(loginFrame)
app.addFrame(pathFrame)
app.addFrame(getCoursesFrame)
app.addFrame(coursesFrame)
app.addFrame(crawlingFrame)
app.addFrame(filesAndVideosFrame)
app.addFrame(downloadingFrame)

app.startWith(loginFrame)

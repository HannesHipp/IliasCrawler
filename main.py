from Framework.App import App
from Framework.Frame import Frame

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

loginFrame = Frame(
    framePath = "IliasCrawler\\resources\\LoginView.ui",
    triggerButtonName = "button_login"
)
username = Username(
    frame = loginFrame
)
password = Password(
    frame = loginFrame
)
courses = Courses(
    frame = Frame(
        framePath = "IliasCrawler\\resources\\CourseSelectionView.ui",
        triggerButtonName = "button_select_choice"
    )
)
path = Path(
    frame = Frame(
        framePath = "IliasCrawler\\resources\\PathSelectionView.ui",
        triggerButtonName = "button_select_path"
    )
)
filesAndVideos = FilesAndVideos()

app.addFunction(
    ValidateLogin(
        username = username,
        password = password,
        frame = Frame(framePath = "IliasCrawler\\resources\\LoginValidationView.ui")
    )
)
app.addFunction(
    GetCourses(
        username = username, 
        password = password, 
        result = courses,
        frame = Frame(framePath = "IliasCrawler\\resources\\CourseLoadingView.ui")
    )
)

app.addFunction(
    Crawl(
        courses = courses,
        result = filesAndVideos,
        frame = Frame(framePath = "IliasCrawler\\resources\\CrawlingView.ui")
    )
)
app.addFunction(
    Download(
        filesAndVideos = filesAndVideos,
        path = path,
        frame = Frame(framePath = "IliasCrawler\\resources\\DownloadingView.ui")
    )
)

app.start()

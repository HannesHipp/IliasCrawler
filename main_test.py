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


loginFrame = Frame(framePath = "IliasCrawler\\resources\\LoginView.ui", 
                   textfield_username = Username(), 
                   textfield_password = Password()
)
loginValidationFrame = Frame(framePath = "IliasCrawler\\resources\\LoginValidationView.ui", 
                             function = ValidateLogin()
)
pathFrame = Frame(framePath = "IliasCrawler\\resources\\PathSelectionView.ui", 
                  button_select_path = Path()
)
getCoursesFrame = Frame(framePath = "IliasCrawler\\resources\\CourseLoadingView.ui", 
                        function = GetCourses()
)
coursesFrame = Frame(framePath = "IliasCrawler\\resources\\CourseSelectionView.ui", 
                     list_view = Courses()
)
crawlingFrame = Frame(framePath = "IliasCrawler\\resources\\CrawlingView.ui", 
                      function = Crawl()
)
filesAndVideosFrame = Frame(filesAndVideos = FilesAndVideos()
)
downloadingFrame = Frame(framePath = "IliasCrawler\\resources\\DownloadingView.ui", 
                         function = Download()
)

loginFrame.connect('button_login', loginValidationFrame)
loginValidationFrame.connect(pathFrame)
pathFrame.connect('button_select_path', getCoursesFrame)
getCoursesFrame.connect(coursesFrame)
coursesFrame.connect('button_select_choice', crawlingFrame)
crawlingFrame.connect(filesAndVideosFrame)
filesAndVideosFrame.connect(downloadingFrame)

app.addFrame(loginFrame)
app.addFrame(loginValidationFrame)
app.addFrame(pathFrame)
app.addFrame(getCoursesFrame)
app.addFrame(coursesFrame)
app.addFrame(crawlingFrame)
app.addFrame(filesAndVideosFrame)
app.addFrame(downloadingFrame)

app.start(loginFrame)

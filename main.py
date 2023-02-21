from Framework.App import App
from Framework.Frame import Frame
from Framework.DataElements.TextField import TextField
from Framework.DataElements.LoadingAnimation import LoadingAnimation

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
    "IliasCrawler\\resources\\LoginView.ui",
    TextField(username, name="textfield_username"),
    TextField(password, name="textfield_password"),
    validationFrame=Frame(
        "IliasCrawler\\resources\\LoginValidationView.ui",
        # LoadingAnimation(username, name="loading_animation"),
        function=ValidateLogin(username, password)
    )
)
pathFrame = Frame(
    "IliasCrawler\\resources\\PathSelectionView.ui",
    # PathSelector(path, "select_path")
)
# getCoursesFrame = Frame(
#     "IliasCrawler\\resources\\CourseLoadingView.ui",
#     LoadingAnimation(courses, bar="progress_bar", label="progress_bar_text_label"),
#     function = GetCourses(username, password, courses)
# )
# coursesFrame = Frame(
#     "IliasCrawler\\resources\\CourseSelectionView.ui",
#     ListCheckable(courses, "listView")
# )
# crawlingFrame = Frame(
#     "IliasCrawler\\resources\\CrawlingView.ui",
#     ProgressBarWithText(Crawl(username, password, courses), "progress_bar", "progress_bar_text_label")
# )
# filesAndVideosFrame = Frame(
#     filesAndVideos
# )
# downloadingFrame = Frame(
#     "IliasCrawler\\resources\\DownloadingView.ui",
#     ProgressBarWithText(Download(username, password, path, filesAndVideos), "progress_bar", "progress_bar_text_label")
# )

loginFrame.connect(pathFrame, 'button_login')
# pathFrame.connect(getCoursesFrame, 'button_select_path')
# getCoursesFrame.connect(coursesFrame)
# coursesFrame.connect(crawlingFrame, 'button_select_choice')
# crawlingFrame.connect(filesAndVideosFrame)
# filesAndVideosFrame.connect(downloadingFrame)

app.addFrame(loginFrame)
# app.addFrame(pathFrame)
# app.addFrame(getCoursesFrame)
# app.addFrame(coursesFrame)
# app.addFrame(crawlingFrame)
# app.addFrame(filesAndVideosFrame)
# app.addFrame(downloadingFrame)

app.startWith(loginFrame)

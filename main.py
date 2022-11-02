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


loginFrame = InputFrame("IliasCrawler\\resources\\LoginView.ui",
                        textfield_username = Username(), 
                        textfield_password = Password(),
                    	validationFrame = OutputFrame("IliasCrawler\\resources\LoginValidationView.ui",
                                                      ValidateLogin())
)
pathFrame = InputFrame("IliasCrawler\\resources\\PathSelectionView.ui",
                       button_select_path = Path()
)
getCoursesFrame = OutputFrame("IliasCrawler\\resources\\CourseLoadingView.ui",
                              GetCourses()
)
coursesFrame = InputFrame("IliasCrawler\\resources\\CourseSelectionView.ui",
                          listView = Courses()
)
crawlingFrame = OutputFrame("IliasCrawler\\resources\\CrawlingView.ui",
                            Crawl()
)
filesAndVideosFrame = NoUiFrame(FilesAndVideos()
)
downloadingFrame = OutputFrame("IliasCrawler\\resources\\DownloadingView.ui",
                               Download()
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

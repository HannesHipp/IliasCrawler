from Framework.App import App

from IliasCrawler.Datapoints.Username import Username
from IliasCrawler.Datapoints.Password import Password
from IliasCrawler.Datapoints.Courses import Courses
from IliasCrawler.Datapoints.FilesAndVideos import FilesAndVideos
from IliasCrawler.Datapoints.Path import Path
from IliasCrawler.Datapoints.Autostart import Autostart

from IliasCrawler.Frames.CrawlingFrame import CrawlingFrame
from IliasCrawler.Frames.DownloadingFrame import DownloadingFrame
from IliasCrawler.Frames.LoginFrame import LoginFrame
from IliasCrawler.Frames.LoginValidationFrame import LoginValidationFrame
from IliasCrawler.Frames.PathFrame import PathFrame
from IliasCrawler.Frames.GetCoursesFrame import GetCoursesFrame
from IliasCrawler.Frames.CourseSelectionFrame import CourseSelectionFrame
from IliasCrawler.Frames.AutostartFrame import AutostartFrame
from IliasCrawler.Frames.SuccessFrame import SuccessFrame

app = App()

username = Username()
password = Password()
path = Path()
courses = Courses()
autostart = Autostart()
autostart.submit_value(True)
files_and_videos = FilesAndVideos()


login_frame = LoginFrame(username, password)
login_validation_frame = LoginValidationFrame(username, password)
path_frame = PathFrame(path)
get_courses_frame = GetCoursesFrame(username, password, courses, autostart)
course_selection_frame = CourseSelectionFrame(courses)
autostart_frame = AutostartFrame()
crawling_frame = CrawlingFrame(courses, files_and_videos)
downloading_frame = DownloadingFrame(path, files_and_videos)
success_frame = SuccessFrame()


login_frame.addNextFrames(login_validation_frame)
login_validation_frame.addNextFrames(login_frame, path_frame)
path_frame.addNextFrames(get_courses_frame)
get_courses_frame.addNextFrames(course_selection_frame, autostart_frame)
course_selection_frame.addNextFrames(crawling_frame)
autostart_frame.addNextFrames(course_selection_frame, crawling_frame)
crawling_frame.add_next_frames(downloading_frame)
downloading_frame.add_next_frames(success_frame)

if username.value and password.value and path.value:
    app.startWith(get_courses_frame)
else:
    app.startWith(login_frame)

# TO-DO
    # Herruntergeladene Items werden nicht gespeichert
    # Auflösung Laptop Michi
    # Verkehrstechnik nicht vollständig
    # Kurse Ausklappmenü
    # 
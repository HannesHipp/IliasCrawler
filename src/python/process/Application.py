import os
from controller.CourseLoadingController import CourseLoadingController
from controller.CourseSelectionController import CourseSelectionController
from controller.LoginController import LoginController
from controller.PathSelectionController import PathSelectionController
from controller.Window import Window
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt
import sys
from service.Database import Database
from service.EventsManagement import EventsManager


def initialize(window):
    # setting up databases
    Database("login_data", "username", "password")
    Database("storage_path", "storage_path")
    Database("files", "hash")
    Database("all_courses", "course_number", "should_be_downloaded")

    # Setting up Event Management
    # EventsManager.get_instance().attach_listener("download", DownloadView())
    # EventsManager.get_instance().attach_listener("crawl", CrawlingView())

    # Setting up all Controllers
    LoginController(window)
    PathSelectionController(window)
    CourseLoadingController(window)
    CourseSelectionController(window)

os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
app = QApplication(sys.argv)
app.setAttribute(Qt.AA_EnableHighDpiScaling)
window = Window()
initialize(window)
window.show()
if len(Database.get_instance("login_data").get_all()) == 0 or len(Database.get_instance("storage_path").get_all()) == 0:
    Database.get_instance("login_data").clear_table()
    Database.get_instance("storage_path").clear_table()
    LoginController.instance.show()
else:   
    CourseSelectionController.instance.first_time_execution = False
    CourseLoadingController.instance.show()
sys.exit(app.exec_())

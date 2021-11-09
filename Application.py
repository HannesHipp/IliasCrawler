from controller import Service
from controller.CourseSelectionController import CourseSelectionController
from controller.DownloadController import DownloadController
from controller.CrawlingController import CrawlingController
from controller.SetupController import SetupController
from service.Database import Database
from service.EventsManagement import EventsManager
from view.CrawlingView import CrawlingView
from view.DownloadView import DownloadView


def initialize():
    # setting up databases
    Database("userdata", "username", "password", "downloadpath")
    Database("files", "hash")
    Database("course_exceptions", "course_number")
    Database("all_courses", "course_number", "name")

    # Setting up Event Management
    EventsManager.get_instance().attach_listener("download", DownloadView())
    EventsManager.get_instance().attach_listener("crawl", CrawlingView())


initialize()
if len(Database.get_instance("userdata").get_all()) == 0:
    SetupController.run()
courses = CourseSelectionController.run()
data = CrawlingController.run(courses)
DownloadController.run(data)
Service.quit_program()


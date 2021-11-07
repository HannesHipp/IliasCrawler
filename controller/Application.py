from controller import Service
from controller.DownloadController import DownloadController
from controller.CrawlingController import CrawlingController
from controller.SetupController import SetupController
from service.Database import Field, Database
from service.EventsManagement import EventsManager
from view.CrawlingView import CrawlingView
from view.DownloadView import DownloadView


def initialize():
    containsdata = Field("containsdata", "text")
    username = Field("username", "text")
    password = Field("password", "text")
    downloadpath = Field("downloadpath", "text")
    Database("userdata", containsdata, username, password, downloadpath)
    hash = Field("hash", "text")
    Database("files", hash)

    # Setting up Event Management
    EventsManager.get_instance().attach_listener("download", DownloadView())
    EventsManager.get_instance().attach_listener("crawl", CrawlingView())



initialize()
user_data_present = Database.get_instance("userdata").key_exists("true")
if not user_data_present:
    SetupController.run()
data = CrawlingController.run()
DownloadController.run(data)
Service.quit_program()


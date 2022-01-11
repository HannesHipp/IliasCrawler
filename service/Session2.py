from service.Database import Database
from service.EventsManagement import EventsManager
from view.DownloadView import DownloadView
from view.CrawlingView import CrawlingView



class Session:

    @staticmethod
    def setUp():
        # setting up databases
        Database("userdata", "username", "password", "downloadpath")
        Database("files", "hash")
        Database("courses_to_download", "course_number")
        Database("all_courses", "course_number")

        # Setting up Event Management
        EventsManager.get_instance().attach_listener("download", DownloadView())
        EventsManager.get_instance().attach_listener("crawl", CrawlingView())
    
    @staticmethod
    def username():
        

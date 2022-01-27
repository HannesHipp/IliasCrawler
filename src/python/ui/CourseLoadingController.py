import time
from controller.Frame import Frame
from controller.CourseSelectionController import CourseSelectionController
from model.Ilias import Ilias
from model.Course import Course
from controller.Window import Window
from PyQt5.QtCore import pyqtSignal, QObject, QThread


class Crawler(QObject):

    finished_crawling = pyqtSignal()

    def crawl(self):
        print("start")
        time.sleep(10)
        CourseSelectionController.instance.courses = [Course("test", "https:", None)]
        # CourseSelectionController.instance.courses = Ilias.create().get_new_pages()
        self.finished_crawling.emit()



class CourseLoadingController(Frame):

    crawl_requested = pyqtSignal()

    def __new__(cls, container):
        if not hasattr(cls, 'instance'):
            cls.instance = super(CourseLoadingController, cls).__new__(cls)
        return cls.instance

    def __init__(self, container):   
        self.ui_file_location = 'C:\\Users\\Hannes\\Code Projekte\\IliasCrawler\\IliasCrawler\\view\\CourseLoadingView.ui'
        super().__init__(container)
        
        self.crawler = Crawler()
        self.crawler_thread = QThread()
        self.crawler.moveToThread(self.crawler_thread)
        self.crawler_thread.start()
        self.crawler.finished_crawling.connect(self.show_results)
        self.crawl_requested.connect(self.crawler.crawl)

    def show(self):
        super().show()
        self.crawl_requested.emit()

    def show_results(self):
        CourseSelectionController.instance.show()

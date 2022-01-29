from PyQt5.QtCore import QObject, pyqtSignal, QThread
from src.python.business.BusinessModel import BusinessModel
from src.python.ui.UI import UI
from src.python.process.Crawler import Crawler
from src.python.process.Downloader import Downloader


class Application(QObject):

    request_crawling = pyqtSignal(list)
    request_login_data = pyqtSignal()
    request_login_data_validation = pyqtSignal(str, str)

    def __init__(self) -> None:
        super().__init__()
        
        self.crawler = Crawler()
        self.downloader = Downloader()
        self.business_model = BusinessModel()

        # setup threading
        self.worker_thread = QThread()
        self.crawler.moveToThread(self.worker_thread)
        self.downloader.moveToThread(self.worker_thread)
        self.worker_thread.start()  

        # setup connections
        self.request_crawling.connect(self.crawler.crawl)
        self.crawler.send_crawling_results.connect(self.business_model.setCourses)
        self.request_login_data_validation.connect(self.business_model.setSession)

    def run(self):
        if self.business_model.is_valid:
            self.request_crawling.emit()
        else:
            self.request_login_data.emit()

    def validateLoginData(self, username, password):
        self.request_login_data_validation.emit(username, password)
    
from PyQt5.QtCore import pyqtSignal, QObject
from controller.Crawler import Crawler
from controller.CrawlingController import CrawlingController
from model.Ilias import Ilias
from service.BusinessModel import BusinessModel



class ApplicationController(QObject):

    signal_request_user_data = pyqtSignal()
    signal_login_data_validation_successful = pyqtSignal()
    signal_login_data_validation_failed = pyqtSignal()
    signal_start_crawling_for_courses = pyqtSignal()
    signal_crawling_for_courses_finished = pyqtSignal(list, dict)
    signal_start_downloading = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.business_model = None
        self.crawler = None

    def process_setup_finished(self):
        self.business_model = BusinessModel()
        if self.business_model.is_valid:
            self.signal_start_crawling_for_courses.emit()
            self.process_start_crawling_for_courses()
        else:
            self.signal_request_user_data.emit()

    def process_request_login_data_validation(self, username, password):
        if self.business_model.set_username_and_password(username, password):
            self.signal_login_data_validation_successful.emit()
        else:
            self.signal_login_data_validation_failed.emit()

    def process_send_storage_path(self, path):
        self.business_model.set_storage_path(path)
        self.process_start_crawling_for_courses()

    def process_start_crawling_for_courses(self):
        ilias = Ilias(name='Ilias', url='https://ilias3.uni-stuttgart.de/ilias.php?baseClass=ilDashboardGUI&cmd=jumpToSelectedItems', parent=None)
        ilias.set_content()
        fresh_courses = ilias.get_new_pages()
        saved_courses_dict = self.business_model.safed_courses_dict
        self.signal_crawling_for_courses_finished.emit(fresh_courses, saved_courses_dict)

    def process_request_crawl(self):
        self.crawler = Crawler(self.business_model.session, self.business_model.fresh_courses)
        self.crawler.signal_send_crawl_information.connect(CrawlingController.instance.update_displayed_information)
        files_to_download = self.crawler.get_files_to_download()
        self.signal_start_downloading.emit()

    def process_send_course_selection(self, courses):
        self.business_model.set_fresh_courses(courses)


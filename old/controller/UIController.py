from PyQt5.QtCore import pyqtSignal, QObject
from controller.AutoStartController import AutoStartController
from controller.CourseSelectionController import CourseSelectionController
from controller.CrawlingController import CrawlingController
from controller.DownloadingController import DownloadingController
from controller.LoadingScreenController import LoadingScreenController
from controller.LoginController import LoginController
from controller.LoginValidationController import LoginValidationController
from controller.PathSelectionController import PathSelectionController
from controller.CourseLoadingController import CourseLoadingController
from PyQt5.QtWidgets import QMessageBox
from controller.Window import Window
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QBrush, QColor
from PyQt5.QtCore import Qt


class UIController(QObject):

    signal_request_login_data_validation = pyqtSignal(str, str)
    signal_send_storage_path = pyqtSignal(str)
    signal_request_crawl = pyqtSignal()
    signal_send_course_selection = pyqtSignal(list)

    def __init__(self, q_app):
        super().__init__()
        self.window = Window(q_app)
        self.first_time_execution = False

        self.window.select_frame(LoadingScreenController())

        self.login_controller = LoginController()
        self.login_controller.signal_request_login_data_validation.connect(self.process_request_login_data_validation)

        self.login_validation_controller = LoginValidationController()

        self.path_selection_controller = PathSelectionController()
        self.path_selection_controller.signal_send_storage_path.connect(self.process_send_storage_path)

        self.course_loading_controller = CourseLoadingController()

        self.course_selection_controller = CourseSelectionController()
        self.course_selection_controller.signal_request_crawl.connect(self.process_request_crawl)

        self.autostart_controller = AutoStartController(q_app)
        self.autostart_controller.signal_request_crawl.connect(self.process_request_crawl)
        
        self.crawling_controller = CrawlingController()

        self.downloading_controller = DownloadingController()
        
    def process_request_user_data(self):
        self.window.select_frame(self.login_controller)
        self.first_time_execution = True

    def process_request_login_data_validation(self, username, password):
        self.window.select_frame(self.login_validation_controller)
        self.signal_request_login_data_validation.emit(username, password)

    def process_login_data_validation_successful(self):
        self.window.select_frame(self.path_selection_controller)

    def process_login_data_validation_failed(self):
        self.window.select_frame(self.login_controller)
        dialog = QMessageBox()
        dialog.setWindowTitle("Anmeldeproblem")
        dialog.setText("Dein Benutzername oder dein Passwort war falsch.")
        dialog.exec_()

    def process_send_storage_path(self, path):
        self.process_start_crawling_for_courses()
        self.signal_send_storage_path.emit(path)

    def process_start_crawling_for_courses(self):
        self.window.select_frame(self.course_loading_controller)

    def process_crawling_for_courses_finished(self, fresh_courses, saved_courses_dict):
        course_model = self.construct_course_model(fresh_courses, saved_courses_dict)
        self.course_selection_controller.set_model(course_model)
        self.window.select_frame(self.course_selection_controller)
        if not self.first_time_execution:
            self.autostart_controller.show()

    def construct_course_model(self, fresh_courses, saved_courses_dict):
        result = QStandardItemModel()
        for course in fresh_courses:
            item = QStandardItem(course.name)
            item.setCheckable(True)
            item.setData(course)
            item.setCheckState(Qt.Unchecked)
            if not course.get_hash() in saved_courses_dict:
                item.setBackground(QBrush(QColor(113,217,140)))
                result.insertRow(0, item)
            else:
                if saved_courses_dict[course.get_hash()]:
                    item.setCheckState(Qt.Checked)
                result.appendRow(item)
        return result

    def process_request_crawl(self):
        self.window.select_frame(self.crawling_controller)
        course_model = self.course_selection_controller.course_model
        courses = []
        for i in range(course_model.rowCount()):
            item = course_model.item(i)
            course = item.data()
            if item.checkState() == Qt.Checked:
                course.should_be_downloaded = True
            else: 
                course.should_be_downloaded = False
            courses.append(course)
        self.signal_send_course_selection.emit(courses)
        self.signal_request_crawl.emit()

    def process_start_downloading(self):
        self.window.select_frame(self.downloading_controller)
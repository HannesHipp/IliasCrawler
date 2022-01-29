import time
from controller.Frame import Frame
from controller.CourseSelectionController import CourseSelectionController
from model.Ilias import Ilias
from model.Course import Course
from controller.Window import Window
from PyQt5.QtCore import pyqtSignal, QObject, QThread, Qt
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QBrush, QColor

from service.Database import Database
from service.Session import Session


class CourseLoadingController(Frame):

    crawl_requested = pyqtSignal()
    crawl_finished = pyqtSignal()

    def __new__(cls, container):
        if not hasattr(cls, 'instance'):
            cls.instance = super(CourseLoadingController, cls).__new__(cls)
        return cls.instance

    def __init__(self, container):   
        self.ui_file_location = 'C:\\Users\\Hannes\\Code Projekte\\IliasCrawler\\IliasCrawler\\resources\\CourseLoadingView.ui'
        super().__init__(container)
        self.courses = None
        
        self.crawl_requested.connect(self.crawl)
        self.crawl_finished.connect(self.show_results)

    def show(self):
        super().show()
        self.container.app.processEvents()
        username = Database.instance.get_username()
        password = Database.instance.get_password()
        Session(username, password)
        self.crawl_requested.emit()

    def show_results(self):
        model = self.construct_item_model(self.courses)
        CourseSelectionController.instance.model = model
        CourseSelectionController.instance.show()

    def construct_item_model(self, courses):
        result = QStandardItemModel()
        for course in courses:
            item = QStandardItem(course.name)
            item.setCheckable(True)
            item.setData(course)
            if not Database.instance.course_in_database(course):
                item.setBackground(QBrush(QColor(113,217,140)))
                result.insertRow(0, item)
                item.setCheckState(Qt.Checked)
            else:
                if Database.instance.course_should_be_downloaded():
                    item.setCheckState(Qt.Checked)
                result.appendRow(item)
        return result

    def crawl(self):
        self.courses = Ilias.create().get_new_pages()
        self.crawl_finished.emit()

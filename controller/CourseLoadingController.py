import time
from controller.Frame import Frame
from controller.CourseSelectionController import CourseSelectionController
from model.Ilias import Ilias
from model.Course import Course
from controller.Window import Window
from PyQt5.QtCore import pyqtSignal, QObject, QThread, Qt
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QBrush, QColor
from service.BusinessModel import BusinessModel

from service.Database import Database
from service.Session import Session


class CourseLoadingController(Frame):

    def __new__(cls, container):
        if not hasattr(cls, 'instance'):
            cls.instance = super(CourseLoadingController, cls).__new__(cls)
        return cls.instance

    def __init__(self, container):   
        self.ui_file_location = 'C:\\Users\\Hannes\\Code Projekte\\IliasCrawler\\IliasCrawler\\resources\\CourseLoadingView.ui'
        super().__init__(container)

    def show(self):
        super().show()
        BusinessModel.instance.initialize()
        BusinessModel.instance.set_fresh_courses(self.crawl())
        CourseSelectionController.instance.show()  

    def crawl(self):
        return Ilias.create().get_new_pages()


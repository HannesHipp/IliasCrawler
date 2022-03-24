from controller.Frame import Frame
from PyQt5.QtCore import pyqtSignal


class CourseSelectionController(Frame):

    signal_request_crawl = pyqtSignal()

    def __init__(self):
        self.ui_file_location = 'C:\\Users\\Hannes\\Code Projekte\\IliasCrawler\\IliasCrawler\\resources\\CourseSelectionView.ui'
        super().__init__()
        self.course_model = None
        self.button_select_choice.clicked.connect(self.button_select_choice_on_action)

    def button_select_choice_on_action(self):
        self.signal_request_crawl.emit()

    def set_model(self, course_model):
        self.listView.setModel(course_model)
        self.course_model = course_model

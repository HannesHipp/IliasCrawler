from PyQt5.QtCore import pyqtSignal, QObject
from service.BusinessModel import BusinessModel

class ApplicationController(QObject):

    setup_finished_signal = pyqtSignal()
    start_crawling_for_courses_signal = pyqtSignal()
    request_user_data_signal = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.business_model = None
        self.setup_finished_signal.connect(self.initialize)

    def initialize(self):
        self.business_model = BusinessModel()
        if self.business_model.is_valid:
            self.start_crawling_for_courses_signal.emit()
        else:
            self.request_user_data_signal.emit()

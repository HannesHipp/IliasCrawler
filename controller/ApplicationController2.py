import os
import sys
from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QApplication
from controller.DataPoint import DataPoint
from controller.UIController import UIController
from service.BusinessModel import BusinessModel
from controller.Worker import Worker

class AppController(QObject):

    def __init__(self):
        super().__init__()
        os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
        self.q_app = QApplication(sys.argv)
        # q_app.setAttribute(Qt.AA_EnableHighDpiScaling)
        self.ui = UIController(self.q_app)
        self.business_model = BusinessModel()
        self.first_time_execution = not self.business_model.user_data_is_present
        sys.exit(self.q_app.exec_())

    def start(self):
        login_data = DataPoint()
        login_data.get_and_then(self.get_storage_path)

    def get_storage_path(self):
        storage_path = DataPoint()
        storage_path.get_and_then(self.crawl_for_courses)

    def crawl_for_courses(self):
        

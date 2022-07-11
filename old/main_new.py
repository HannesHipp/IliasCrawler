import os
from PyQt5.QtWidgets import QApplication
import sys
from PyQt5.QtCore import QThread, QObject, pyqtSignal
from controller.ApplicationController import ApplicationController
from controller.UIController import UIController

class Main(QObject):

    signal_setup_finished = pyqtSignal()

    def __init__(self) -> None:
        super().__init__()
        self.app_controller = ApplicationController()
        self.ui_controller = UIController(q_app)

        self.signal_setup_finished.connect(self.app_controller.process_setup_finished)

        self.app_controller.signal_request_user_data.connect(self.ui_controller.process_request_user_data)
        self.app_controller.signal_login_data_validation_successful.connect(self.ui_controller.process_login_data_validation_successful)
        self.app_controller.signal_login_data_validation_failed.connect(self.ui_controller.process_login_data_validation_failed)
        self.app_controller.signal_start_crawling_for_courses.connect(self.ui_controller.process_start_crawling_for_courses)
        self.app_controller.signal_crawling_for_courses_finished.connect(self.ui_controller.process_crawling_for_courses_finished)
        self.app_controller.signal_start_downloading.connect(self.ui_controller.process_start_downloading)

        self.ui_controller.signal_request_login_data_validation.connect(self.app_controller.process_request_login_data_validation)
        self.ui_controller.signal_send_storage_path.connect(self.app_controller.process_send_storage_path)
        self.ui_controller.signal_request_crawl.connect(self.app_controller.process_request_crawl)
        self.ui_controller.signal_send_course_selection.connect(self.app_controller.process_send_course_selection)

        self.app_thread = QThread()
        self.app_controller.moveToThread(self.app_thread)
        self.app_thread.start()
        self.signal_setup_finished.emit()


os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
q_app = QApplication(sys.argv)
# q_app.setAttribute(Qt.AA_EnableHighDpiScaling)
main = Main()
sys.exit(q_app.exec_())

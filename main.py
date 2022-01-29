import os
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication

from controller.Window import Window
from controller.LoginController import LoginController
from controller.LoginValidationController import LoginValidationController
from controller.PathSelectionController import PathSelectionController
from controller.CourseLoadingController import CourseLoadingController
from controller.CourseSelectionController import CourseSelectionController
from service.Database import Database
from service.Session import Session

def initializeUI(app):
    window = Window(app)
    LoginController(window)
    LoginValidationController(window)
    PathSelectionController(window)
    CourseLoadingController(window)
    CourseSelectionController(window)


os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
q_app = QApplication(sys.argv)
q_app.setAttribute(Qt.AA_EnableHighDpiScaling)
initializeUI(q_app)
database = Database()
if database.user_data_is_present():
    CourseLoadingController.instance.show()    
else:
    LoginController.instance.show()
sys.exit(q_app.exec_())





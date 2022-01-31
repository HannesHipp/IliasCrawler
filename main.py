import os
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication
from controller.AutoStartController import AutoStartController

from controller.Window import Window
from controller.LoginController import LoginController
from controller.LoginValidationController import LoginValidationController
from controller.PathSelectionController import PathSelectionController
from controller.CourseLoadingController import CourseLoadingController
from controller.CourseSelectionController import CourseSelectionController
from service.BusinessModel import BusinessModel
from service.Database import Database
from service.Session import Session

def initializeUI(app):
    window = Window(app)
    AutoStartController(app)
    LoginController(window)
    LoginValidationController(window)
    PathSelectionController(window)
    CourseLoadingController(window)
    CourseSelectionController(window)


os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
q_app = QApplication(sys.argv)
# q_app.setAttribute(Qt.AA_EnableHighDpiScaling)
initializeUI(q_app)
BusinessModel()
if BusinessModel.instance.first_time_execution:
    LoginController.instance.show()
else:
    CourseLoadingController.instance.show()  
sys.exit(q_app.exec_())





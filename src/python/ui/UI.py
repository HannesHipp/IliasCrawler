# from src.python.ui.frame_controller.CourseSelectionController import CourseSelectionController
# from src.python.ui.frame_controller.CourseLoadingController import CourseLoadingController
# from src.python.ui.frame_controller.PathSelectionController import PathSelectionController
from src.python.ui.frame_controller.LoginValidationController import LoginValidationController
from src.python.ui.frame_controller.LoginController import LoginController
from src.python.ui.Window import Window
from PyQt5.QtCore import pyqtSignal, QObject


class UI(QObject):

    

    def __init__(self, app):
        super().__init__()
        self.app = app
        self.window = Window()
        self.login_controller = LoginController(self.window)
        self.login_validation_controller = LoginValidationController()
        # self.path_selection_controller = PathSelectionController(self.window)
        # self.course_loading_controller = CourseLoadingController(self.window)
        # self.course_selection_controller = CourseSelectionController(self.window)

        self.app.request_login_data.connect(self.showLogin)
        self.login_controller.send_login_data.connect(self.showLoginValidation)
        self.login_controller.send_login_data.connect(self.app.validateLoginData)

    def showLogin(self):
        self.login_controller.show()

    def showLoginValidation(self):
        self.login_validation_controller.show()


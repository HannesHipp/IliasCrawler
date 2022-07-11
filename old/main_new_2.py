from PyQt5.QtWidgets import QWidget, QVBoxLayout, QWidget, QStackedWidget
from PyQt5.uic import loadUi
import os
import sys
import resources.resources
from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QApplication


class AppController(QObject):

    def __init__(self):
        super().__init__()
        os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
        self.q_app = QApplication(sys.argv)
        # q_app.setAttribute(Qt.AA_EnableHighDpiScaling)
        self.window = Window(self.q_app)
        a = DataPoint(str, 'username', 'resources\LoginView.ui',
                      'textfield_username', 'text', 'button_login')
        a.get()
        sys.exit(self.q_app.exec_())


class Window(QWidget):

    def __init__(self, q_app):
        super().__init__()
        self.q_app = q_app
        self.stackedWidget = QStackedWidget()
        mainLayout = QVBoxLayout()
        mainLayout.setSpacing(0)
        mainLayout.setContentsMargins(0, 0, 0, 0)
        mainLayout.addWidget(self.stackedWidget)
        self.setFixedSize(800, 500)
        self.setLayout(mainLayout)
        self.show()

    def add_frame(self, frame):
        index = self.stackedWidget.count()
        frame.index = index
        self.stackedWidget.addWidget(frame)

    def select_frame(self, frame):
        if frame.index is None:
            self.add_frame(frame)
        self.stackedWidget.setCurrentIndex(frame.index)
        self.q_app.processEvents()


class Frame(QWidget):

    def __init__(self, ui_file_location):
        super().__init__()
        self.index = None
        loadUi(ui_file_location, self)


class Database():

    def __init__(self, name, type_) -> None:
        pass


class DataPoint():

    def __init__(self, type_, uniqueName, framePath, dataElementName, dataElementRetreavalFunctionName, triggerElementName):
        self.database = Database(uniqueName, type_)
        self.frame = Frame(framePath)
        self.dataElement = getattr(self.frame, dataElementName)
        self.dataElementRetreavalFunctionName = dataElementRetreavalFunctionName
        self.triggerElement = getattr(self.frame, triggerElementName)
        self.triggerElement.clicked.connect(self.validate)


    def get(self):
        self.frame.show()

    def validate(self):
        data = getattr(self.dataElement, self.dataElementRetreavalFunctionName)()
        


AppController()

import os
import sys

from PyQt5.QtCore import QObject, QThreadPool
from PyQt5.QtWidgets import QApplication
from Framework.Window import Window


class App(QObject):

    def __init__(self) -> None:
        super().__init__()
        os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
        self.qApp = QApplication(sys.argv)
        self.window = Window()

    def addFrame(self, frame):
        frame.display.connect(self.window.selectFrame)

    def startWith(self, frame):
        frame.request.emit()
        sys.exit(self.qApp.exec_())

    def showPopup(self, path):
        pass
    
    def cock(self):
        print("""p n the v wird freigesetzt
        #doityourself
        #freecock
        #ANDFUCKINGFREEBOOOOOOOOBS
        SHOW BOOBS PICS AND print
        .vars""")



import os
from PyQt5.QtWidgets import QApplication
import sys
from PyQt5.QtCore import QThread

from controller.ApplicationController import ApplicationController
from controller.UIController import UIController

os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
q_app = QApplication(sys.argv)
# q_app.setAttribute(Qt.AA_EnableHighDpiScaling)

app_controller = ApplicationController()
ui_controller = UIController(q_app)
app_controller.request_user_data_signal.connect(ui_controller.process_request_user_data)


app_thread = QThread()
app_controller.moveToThread(app_thread)
app_thread.start()
app_controller.setup_finished.emit()

sys.exit(q_app.exec_())

import time
from PyQt5.QtWidgets import QWidget
from PyQt5.uic import loadUi
from PyQt5.QtCore import pyqtSignal


class AutoStartController(QWidget):

    signal_request_crawl = pyqtSignal()

    def __init__(self, q_app):
        super().__init__()
        self.ui_file_location = 'resources\\AutoStartView.ui'
        loadUi(self.ui_file_location, self)
        self.button_start.clicked.connect(self.button_start_on_action)
        self.button_cancel.clicked.connect(self.button_cancel_on_action)
        self.canceled = False
        self.q_app = q_app

    def button_start_on_action(self):
        self.close()
        self.signal_request_crawl.emit()

    def button_cancel_on_action(self):
        print("cancel")
        self.close()
        self.canceled = True

    def show(self):
        super().show()
        sec = 20
        while sec >= 0:
            self.description.setText(
                f"Das Programm wird in {sec}s deine bereits auswählten Kurse durchsuchen und neue Dateien automatisch herunterladen. Wenn du deine Kurse ändern möchtest, klicke einfach auf 'Abbrechen'.")
            self.button_start.setText(f"Starten ({sec})")
            time.sleep(1)
            sec -= 1
            self.q_app.processEvents()
            if self.canceled:
                break
        if not self.canceled:
            self.button_start_on_action()
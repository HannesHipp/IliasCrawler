from src.python.persistance.Database import Database
from src.python.persistance.Session import Session
from PyQt5.QtCore import pyqtSignal


class BusinessModel:

    business_model_changed = pyqtSignal()

    def __init__(self):
        self.database = Database
        self.is_valid


    def setCourses(self, crawling_result):
        pass

    def setSession(self, username, password):
        








from service.Database import Database
from service.Session import Session
from PyQt5.QtCore import pyqtSignal, QObject


class BusinessModel(QObject):

    business_model_changed = pyqtSignal()

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(BusinessModel, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        super().__init__()
        self.business_model_changed.connect(self.save_changes_to_database)
        self.database = Database()
        self.first_time_execution = not self.database.user_data_is_present()
        self.username = None
        self.password = None
        self.storage_path = None
        self.fresh_courses = None
        self.downloadable_data = None
        if not self.first_time_execution:
            self.username = self.database.get_username()
            self.password = self.database.get_password()
            self.storage_path = self.database.get_storage_path()

    def username_and_password_are_valid(self, username, password):
        if Session(username, password).is_valid():
            return True
        else:
            return False

    def set_username_and_password(self, username, password):
        self.username = username
        self.password = password
        self.business_model_changed.emit()

    def set_storage_path(self, storage_path):
        self.storage_path = storage_path
        self.business_model_changed.emit()

    def initialize(self):
        self.session = Session(self.username, self.password)
        self.safed_courses_dict = self.database.get_saved_course_dict()

    def set_fresh_courses(self, courses):
        self.fresh_courses = courses

    def set_fresh_courses(self, courses):
        self.fresh_courses = courses
        self.business_model_changed.emit()

    def save_changes_to_database(self):
        if self.username is not None:
            self.database.save_login_data(self.username, self.password)
        if self.storage_path is not None:
            self.database.save_storage_path(self.storage_path)
        if self.fresh_courses is not None:
            self.database.save_fresh_courses(self.fresh_courses)

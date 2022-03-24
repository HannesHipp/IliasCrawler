from service.Database import Database
from service.Session import Session
from PyQt5.QtCore import QObject


class BusinessModel(QObject):

    def __init__(self):
        super().__init__()
        self.database = Database()
        self.username = self.database.get_username()
        self.password = self.database.get_password()
        self.storage_path = self.database.get_storage_path()
        self.user_data_is_present = True
        if self.username is None or self.password is None or self.storage_path is None:
            self.user_data_is_present = False
        self.safed_courses_dict = self.database.get_saved_course_dict()
        self.fresh_courses = None
        self.downloadable_data = None

    def set_username_and_password(self, username, password):
        self.username = username
        self.password = password
        self.database.save_username_and_password(username, password)

    def set_storage_path(self, storage_path):
        self.storage_path = storage_path
        self.database.save_storage_path(storage_path)

    def set_fresh_courses(self, fresh_courses):
        self.fresh_courses = fresh_courses
        self.database.save_fresh_courses(fresh_courses)

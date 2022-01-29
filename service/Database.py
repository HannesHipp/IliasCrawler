from service.SQLAdapter import SQLTable
from PyQt5.QtCore import QObject, pyqtSignal


class Database():

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Database, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self.login_data_table = SQLTable("login_data", "username", "password")
        self.storage_path_table = SQLTable("storage_path", "storage_path")
        self.courses_table = SQLTable(
            "courses", "hash", "should_be_downloaded")
        self.files_table = SQLTable("files", "hash")

    def user_data_is_present(self):
        if not self.login_data_table.table_is_empty():
            if not self.storage_path_table.table_is_empty():
                return True
        return False

    def get_username(self):
        return self.login_data_table.get_all()[0][0]

    def get_password(self):
        return self.login_data_table.get_all()[0][1]

    def set_login_data(self, username, password):
        self.login_data_table.clear_table()
        self.login_data_table.add(username, password)

    def set_storage_path(self, storage_path):
        self.storage_path_table.clear_table()
        self.storage_path_table.add(storage_path)

    def course_in_database(self, course):
        self.courses_table.key_exists(course.get_hash())

    def course_should_be_downloaded(self, course):
        should_be_downloaded = self.courses_table.find("hash", course.get_hash())[0][1]
        if should_be_downloaded == "False":
            return False
        else:
            return True

    def clear_course_table(self):
        self.courses_table.clear_table()

    def add_course(self, course):
        self.courses_table.add(course.get_hash(), str(course.should_be_downloaded))
        
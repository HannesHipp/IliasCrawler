from service.SQLAdapter import SQLTable


class Database(): 

    """penisapp - the best app in the whole f**** world mothafocka"""

    def __init__(self):
        self.login_data_table = SQLTable("login_data", "username", "password")
        self.storage_path_table = SQLTable("storage_path", "storage_path")
        self.courses_table = SQLTable("courses", "hash", "should_be_downloaded")
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

    def get_storage_path(self):
        return self.storage_path_table.get_all()[0][0]
        
    def get_saved_course_dict(self):
        result = {}
        list_of_course_tuples = self.courses_table.get_all()
        for course_tuple in list_of_course_tuples:
            if course_tuple[1] == "True":
                result[course_tuple[0]] = True
            else:
                result[course_tuple[0]] = False
        return result

    def save_username_and_password(self, username, password):
        self.login_data_table.clear_table()
        self.login_data_table.add(username, password)

    def save_storage_path(self, storage_path):
        self.storage_path_table.clear_table()
        self.storage_path_table.add(storage_path)

    def save_fresh_courses(self, fresh_courses):
        self.courses_table.clear_table()
        for course in fresh_courses:
            self.courses_table.add(course.get_hash(), str(course.should_be_downloaded))
            

import sqlite3


class Field:

    def __init__(self, name, type):
        self.name = name
        self.type = type


class Database:

    __instances = []

    @staticmethod
    def get_instance(name):
        for instance in Database.__instances:
            if name == instance.name:
                return instance

    def __init__(self, name, key, *additional_fields):
        for instance in Database.__instances:
            if name == instance.name:
                raise Exception("Eine Datenbank mit diesem Namen steht bereits über get_instance zur Verfügung.")
        self.name = name
        self.key = key
        self.additional_fields = additional_fields
        self.connection = sqlite3.connect("database.db")
        self.cursor = self.connection.cursor()

        # Create string dynamically depending on number of fields
        fields_to_string = " (" + self.key.name + " " + self.key.type + ","
        for field in self.additional_fields:
            fields_to_string = fields_to_string + field.name + " " + field.type + ","
        fields_to_string = fields_to_string[:-1] + ")"

        try:
            with self.connection:
                self.cursor.execute("CREATE TABLE " + self.name + fields_to_string)
        except sqlite3.OperationalError:
            pass

        Database.__instances.append(self)


    def add(self, list):
        if len(list) == (len(self.additional_fields) + 1):
            if not self.key_exists(list[0]):
                placeholder = "("
                for element in list:
                    placeholder = placeholder + "?, "
                placeholder = placeholder[:-2] + ")"
                with self.connection:
                    self.cursor.execute("INSERT INTO " + self.name + " VALUES " + placeholder, tuple(list))
            else:
                raise Exception(
                    str(list[0])
                    + " ist bereits in der Datenbank!"
                )
        else:
            raise Exception(
                "Datenbank hat " + str(len(self.additional_fields) + 1) + " Felder, übergebenes Objekt hat "
                + str(len(list)) + " Felder."
            )

    def key_exists(self, key):
        with self.connection:
            self.cursor.execute("SELECT * FROM " + self.name + " WHERE " + self.key.name + "='" + key + "'")
            if len(self.cursor.fetchall()) == 0:
                return False
            else:
                return True

    def find(self, field, text):
        with self.connection:
            self.cursor.execute("SELECT * FROM " + self.name + " WHERE " + field.name + "='" + text + "'")
            return self.cursor.fetchall()

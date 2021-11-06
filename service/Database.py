import sqlite3


class Field:

    def __init__(self, name, type):
        self.name = name
        self.type = type


class Database:

    table_name = " data "

    def __init__(self, id, *additional_fields):
        self.id = id
        self.additional_fields = additional_fields
        fields_to_string = "(" + self.id.name + " " + self.id.type + ","
        for field in self.additional_fields:
            fields_to_string = fields_to_string + field.name + " " + field.type + ","
        fields_to_string = fields_to_string[:-1] + ")"
        self.file_name = fields_to_string + ".db"
        self.connection = sqlite3.connect(self.file_name)
        self.cursor = self.connection.cursor()
        try:
            with self.connection:
                self.cursor.execute("CREATE TABLE" + Database.table_name + fields_to_string)
        except sqlite3.OperationalError:
            pass

    def add(self, list):
        if len(list) == (len(self.additional_fields)+1):
            if not self.id_exists(list[0]):
                string = "("
                for element in list:
                    string = string + "?, "
                string = string[:-2] + ")"
                with self.connection:
                    self.cursor.execute("INSERT INTO" + Database.table_name + "VALUES " + string, list)
            else:
                raise Exception(
                    str(list[0])
                    + " ist bereits in der Datenbank!"
                )
        else:
            raise Exception(
                "Datenbank hat "
                + str(len(self.additional_fields)+1)
                + " Felder, übergebenes Objekt hat "
                + str(len(list))
                + " Felder."
            )

    def id_exists(self, id):
        with self.connection:
            self.cursor.execute("SELECT * FROM" + Database.table_name + "WHERE " + self.id.name + "='" + id + "'")
            if len(self.cursor.fetchall()) == 0:
                return False
            else:
                return True

    def find(self, field, text):
        with self.connection:
            self.cursor.execute("SELECT * FROM" + Database.table_name + "WHERE " + field.name + "='" + text + "'")
            return self.cursor.fetchall()
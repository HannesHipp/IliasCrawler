import sqlite3
from Framework.Exceptions import ItemAlreadyExists, WrongFieldLength


class SQLTable:

    def __init__(self, name, key, *additional_fields):
        self.name = name
        self.key = key
        self.additional_fields = additional_fields
        self.connection = sqlite3.connect("database.db")
        self.cursor = self.connection.cursor()

        fields_to_string = f"({self.key} text"
        for field in self.additional_fields:
            fields_to_string = f"{fields_to_string},{field} text"
        fields_to_string = f"{fields_to_string})"

        try:
            self.execute(f"CREATE TABLE {self.name} {fields_to_string}")
        except sqlite3.OperationalError:
            pass

    def execute(self, command, data=None):
        with self.connection:
            if data is None:
                self.cursor.execute(command)
            else:
                self.cursor.execute(command, data)
            return self.cursor.fetchall()

    def add(self, tuple):
        if len(tuple) == (len(self.additional_fields) + 1):
            if not self.keyExists(tuple[0]):
                placeholder = "("
                for element in tuple:
                    placeholder = f"{placeholder} ?, "
                placeholder = f"{placeholder[:-2]})"
                self.execute("INSERT INTO " + self.name + " VALUES " + placeholder, tuple)
            else:
                raise ItemAlreadyExists(
                    f"Item {tuple[0]} already exists in Table {self.name}."
                )
        else:
            raise WrongFieldLength(
                f"Table {self.name} has {str(len(self.additional_fields) + 1)} field(s), given tuple has {str(len(tuple))} field(s)."
            )

    def keyExists(self, key_text):
        result = self.execute(f"SELECT * FROM {self.name} WHERE {self.key}='{key_text}'")
        if len(result) == 0:
            return False
        else:
            return True

    def getAll(self):
        result = self.execute("SELECT * FROM " + self.name)
        if len(result) == 0:
            result = None           
        return result

    def updateTable(self, tupleList):
        self.clearTable()
        for tuple in tupleList:
            self.add(tuple)

    def clearTable(self):
        self.execute("DELETE FROM " + self.name) 

    # def find(self, field, text):
    #     result = self.execute(f"SELECT * FROM {self.name} WHERE {field}='{text}'")
    #     if len(result) == 0:
    #         result = None
    #     return result

    # def updateItem(self, key_text, field, field_text):
    #     self.execute("UPDATE " + self.name + " SET " + field + "='" + field_text + "' WHERE " + self.key + "='" + key_text + "'")

    # def deleteKey(self, key_text):
    #     self.execute("DELETE FROM " + self.name + " WHERE " + self.key + "='" + key_text + "'")
    
    # def tableIsEmpty(self):
    #     if len(self.getAll()) == 0:
    #         return True
    #     else:
    #         False
import sqlite3
from service.Exceptions import ItemAlreadyExists, WrongFieldLength


class SQLTable:

    def execute(self, command, data=None):
        with self.connection:
            if data is None:
                self.cursor.execute(command)
            else:
                self.cursor.execute(command, data)
            return self.cursor.fetchall()

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

    def add(self, *data):
        if len(data) == (len(self.additional_fields) + 1):
            if not self.key_exists(data[0]):
                placeholder = "("
                for element in data:
                    placeholder = f"{placeholder} ?, "
                placeholder = f"{placeholder[:-2]})"
                self.execute("INSERT INTO " + self.name + " VALUES " + placeholder, tuple(data))
            else:
                raise ItemAlreadyExists(
                    f"Item {data[0]} already exists in Table {self.name}."
                )
        else:
            raise WrongFieldLength(
                f"Table {self.name} has {str(len(self.additional_fields) + 1)} field(s), given object has {str(len(data))} field(s)."
            )

    def key_exists(self, key_text):
        result = self.execute(f"SELECT * FROM {self.name} WHERE {self.key}='{key_text}'")
        if len(result) == 0:
            return False
        else:
            return True

    def find(self, field, text):
        result = self.execute(f"SELECT * FROM {self.name} WHERE {field}='{text}'")
        if len(result) == 0:
            result = None
        return result

    def update_item(self, key_text, field, field_text):
        self.execute("UPDATE " + self.name + " SET " + field + "='" + field_text + "' WHERE " + self.key + "='" + key_text + "'")

    def get_all(self):
        result = self.execute("SELECT * FROM " + self.name)
        if len(result) == 0:
            result = None           
        return result

    def delete_key(self, key_text):
        self.execute("DELETE FROM " + self.name + " WHERE " + self.key + "='" + key_text + "'")
    
    def update_table(self, data):
        self.clear_table()
        for item in data:
            self.add(item)

    def clear_table(self):
        self.execute("DELETE FROM " + self.name) 

    def table_is_empty(self):
        if len(self.get_all()) == 0:
            return True
        else:
            False

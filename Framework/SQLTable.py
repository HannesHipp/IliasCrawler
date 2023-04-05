import sqlite3
from Framework.Exceptions import ItemAlreadyExists, WrongFieldLength


class SQLTable:

    FILENAME = "database.db"

    def __init__(self, name: str, numOfFields: int):
        self.name = name
        self.connection = sqlite3.connect(SQLTable.FILENAME)
        self.cursor = self.connection.cursor()
        self.fieldLength = numOfFields
        letters = [chr(i) for i in range(97, 97 + numOfFields)]
        fieldsStr = SQLTable.createTupleStr(
            [f"{letter} text" for letter in letters])
        try:
            self.execute(f"CREATE TABLE {self.name} {fieldsStr}")
        except sqlite3.OperationalError:
            pass

    @staticmethod
    def createTupleStr(elements):
        result = "("
        for element in elements:
            result = f"{result}{element}, "
        result = f"{result[:-2]})"
        return result

    def execute(self, command, data=None):
        with self.connection:
            if data is None:
                self.cursor.execute(command)
            else:
                self.cursor.execute(command, data)
            return self.cursor.fetchall()

    def add(self, tuple):
        if len(tuple) != self.fieldLength:
            raise WrongFieldLength(
                f"Table {self.name} has {str(self.fieldLength)} field(s), given tuple was {str(tuple)}"
            )
        if self.keyExists(tuple[0]):
            raise ItemAlreadyExists(
                f"Key {tuple[0]} already exists in table {self.name}."
            )
        placeholder = SQLTable.createTupleStr(
            [f"?" for field in range(len(tuple))])
        self.execute(f"INSERT INTO {self.name} VALUES {placeholder}", tuple)

    def keyExists(self, key_text):
        # a=keyName
        result = self.execute(
            f"SELECT * FROM {self.name} WHERE a=?", (key_text,))
        if len(result) == 0:
            return False
        else:
            return True

    def getAll(self):
        return self.execute(f"SELECT * FROM {self.name}")

    def updateTable(self, tupleList):
        self.clearTable()
        for tuple in tupleList:
            self.add(tuple)

    def clearTable(self):
        self.execute(f"DELETE FROM {self.name}")

    def deleteTable(self):
        self.execute(f"DROP TABLE {self.name}")

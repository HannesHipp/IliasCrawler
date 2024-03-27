import sqlite3


class Database():

    FILENAME = "database.db"
    connection = None
    cursor = None

    @staticmethod
    def execute(command, data=None):
        with Database.connection:
            if data is None:
                Database.cursor.execute(command)
            else:
                Database.cursor.execute(command, data)
            return Database.cursor.fetchall()

    def __init__(self, name):
        if not Database.connection or Database.cursor:
            Database.connection = sqlite3.connect(Database.FILENAME)
            Database.cursor = self.connection.cursor()
        self.name = name

    def getTuplelist(self):
        if not self.tableExists():
            return []
        tupleList = self.getAll()
        return tupleList

    def tableExists(self):
        result = Database.execute(f"PRAGMA table_info({self.name})")
        if len(result) == 0:
            return False
        else:
            return True

    def saveTuplelist(self, tuplelist):
        if not self.tableExists():
            fieldsStr = createFieldsStr(tuplelist[0])
            Database.execute(f"CREATE TABLE {self.name} {fieldsStr}")
        self.updateTable(tuplelist)

    def updateTable(self, tupleList):
        self.clearTable()
        for tuple in tupleList:
            self.add(tuple)

    def clearTable(self):
        Database.execute(f"DELETE FROM {self.name}")

    def getAll(self):
        return Database.execute(f"SELECT * FROM {self.name}")

    def add(self, tuple):
        if len(tuple) != self.numOfColumns():
            raise Exception(
                f"Number of columns of table {self.name} does not match {str(tuple)}"
            )
        if self.keyExists(tuple[0]):
            raise Exception(
                f"Key {tuple[0]} already exists in table {self.name}."
            )
        placeholder = createTupleStr(
            [f"?" for field in range(len(tuple))])
        Database.execute(
            f"INSERT INTO {self.name} VALUES {placeholder}", tuple)

    def numOfColumns(self):
        return Database.execute(f"SELECT count(*) FROM pragma_table_info('{self.name}')")[0][0]

    def keyExists(self, key_text):
        # a=keyName
        result = Database.execute(
            f"SELECT * FROM {self.name} WHERE a=?", (key_text,))
        if len(result) == 0:
            return False
        else:
            return True


def createTupleStr(elements):
    result = "("
    for element in elements:
        result = f"{result}{element}, "
    result = f"{result[:-2]})"
    return result


def createFieldsStr(tuple):
    return createTupleStr(
        [f"{letter} text" for letter in
         [chr(i) for i in range(97, 97 + len(tuple))
          ]
         ]
    )

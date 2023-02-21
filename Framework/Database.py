from Framework.SQLTable import SQLTable


class Database():

    """penisapp - the best app in the whole f**** world mothafocka"""

    def __init__(self, name):
        self.name = name
        self.table = None

    def initializeTable(self, tuplelist):
        self.table = SQLTable(self.name, len(tuplelist[0]))

    def getTuplelist(self):
        if self.table:
            return self.table.getAll()
        return None

    def saveTuplelist(self, tuplelist):
        if not self.table:
            self.initializeTable(tuplelist)
        self.table.updateTable(tuplelist)

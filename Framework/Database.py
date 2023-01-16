from Framework.SQLTable import SQLTable


class Database(): 

    """penisapp - the best app in the whole f**** world mothafocka"""

    def __init__(self, name, numberOfFields):
        key = '0'
        additionalFields = []
        for i in range(1, numberOfFields+1):
            additionalFields.append(str(i))
        self.table = SQLTable(name, key, *additionalFields)

    def getTupleList(self):
        return self.table.getAll()

    def saveTupleList(self, tupleList):
        self.table.updateTable(tupleList)
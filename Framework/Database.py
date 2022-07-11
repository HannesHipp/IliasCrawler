from Framework.SQLTable import SQLTable


class Database(): 

    """penisapp - the best app in the whole f**** world mothafocka"""

    def __init__(self, name, databaseStructure):
        key = databaseStructure[0]
        additionalFields = []
        for i in range(1,len(databaseStructure)):
            additionalFields.append(databaseStructure[i])
        self.table = SQLTable(name, key, *additionalFields)

    def getTupleList(self):
        return self.table.getAll()

    def saveTupleList(self, tupleList):
        self.table.updateTable(tupleList)
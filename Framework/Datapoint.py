from PyQt5.QtCore import QObject, pyqtSignal
from Framework.Frame import Frame
from Framework.Database import Database


class Datapoint(QObject):

    def __init__(self, **kwargs) -> None:
        super().__init__()
        self.value = None
        self.valid = False
        self.name = self.__class__.__name__.lower()
        self.database = Database(self.name, kwargs['numberOfDatabaseFields'])

    def handleRequest(self):
        savedValue = self.valueFromDatabaseFormat_(self.database.getTupleList())
        calculatedValue = self.value
        value, displayRequested = self.getValue(savedValue, calculatedValue)
        if value and not displayRequested:
            self.setValue(value)
        else:
            self.value = value
        return displayRequested

    def setValueWithDataFrom(self, dataElement):
        self.value = self.readFrom(dataElement)

    def valueFromDatabaseFormat_(self, tupleList):
        if len(tupleList) == 0:
            return None
        else:
            return self.valueFromDatabaseFormat(tupleList)

    def finalize(self):
        self.valid = True
        self.database.saveTupleList(self.valueToDatabaseFormat(self.value))

    def howToGetValue(self):
        raise Exception(f"howToGetValue method not implemented for {self.__class__.__name__}")

    def valueFromDatabaseFormat(self, tupleList):
        raise Exception(f"valueFromDatabaseFormat method not implemented for {self.__class__.__name__}")

    def valueToDatabaseFormat(self, data):
        raise Exception(f"valueToDatabaseFormat method not implemented for {self.__class__.__name__}")

from PyQt5.QtCore import QObject, pyqtSignal
from Framework.Frame import Frame
from Framework.Database import Database


class Datapoint(QObject):

    valueChanged = pyqtSignal()

    def __init__(self, **kwargs) -> None:
        super().__init__()
        name = self.__class__.__name__.lower()
        self.database = Database(name, kwargs['numberOfDatabaseFields'])
        self.value = self.databaseTupleToValue(self.database.getTupleList())
        self.valid = False
        if self.value:
            self.valid = True

    def setValue(self, value):
        self.value = value
        self.valueChanged.emit()

    def isValid(self):
        self.valid = True
        self.database.saveTupleList(self.databaseValueToTuple(self.value))

    def databaseTupleToValue(self, tupleList):
        raise Exception(
            f"valueFromDatabaseFormat method not implemented for {self.__class__.__name__}")

    def databaseValueToTuple(self, data):
        raise Exception(
            f"valueToDatabaseFormat method not implemented for {self.__class__.__name__}")

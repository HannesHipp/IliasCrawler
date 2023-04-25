from PyQt5.QtCore import QObject, pyqtSignal
from Framework.Database import Database


class Datapoint(QObject):

    valueChanged = pyqtSignal()

    def __init__(self, save=True) -> None:
        super().__init__()
        value = None
        if save:
            database = Database(self.__class__.__name__.lower())
            if savedTuplelist := database.getTuplelist():
                value = self.databaseTuplelistToValue(savedTuplelist)
        else:
            database = None
        self.database = database
        self.value = value
        self.error = None

    def updateValue(self, value):
        result = self.isValid(value)
        if result == True:
            self.value = value
        else:
            self.value = None
            self.error = result
        self.valueChanged.emit()

    def save(self):
        if self.database:
            self.database.saveTuplelist(
                self.databaseValueToTuplelist(self.value))

    # overwritten by subclasses
    def isValid(self, value):
        return True

    def databaseTuplelistToValue(self, tupleList):
        raise Exception(
            f"valueFromDatabaseFormat method not implemented for {self.__class__.__name__}"
        )

    def databaseValueToTuplelist(self, data):
        raise Exception(
            f"valueToDatabaseFormat method not implemented for {self.__class__.__name__}"
        )

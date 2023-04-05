from PyQt5.QtCore import QObject, pyqtSignal
from Framework.Database import Database


class Datapoint(QObject):

    valueChanged = pyqtSignal()

    def __init__(self, save=True) -> None:
        super().__init__()
        value = None
        if save:
            self.database = Database(self.__class__.__name__.lower())
            if savedTuplelist := self.database.getTuplelist():
                value = self.databaseTuplelistToValue(savedTuplelist)
        self.value = value

    def validate(self):
        valid = self.isValid(self.value)
        if valid == True:
            self.database.saveTuplelist(
                self.databaseValueToTuplelist(self.value))
        return valid

    def updateValue(self, value):
        self.value = value
        if self.isValid(value) == True:
            self.valueChanged.emit()

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

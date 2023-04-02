from PyQt5.QtCore import QObject, pyqtSignal
from Framework.Database import Database


class Datapoint(QObject):

    valueChanged = pyqtSignal()

    def __init__(self) -> None:
        super().__init__()
        self.database = Database(self.__class__.__name__.lower())
        if savedTuplelist := self.database.getTuplelist():
            self.value = self.databaseTuplelistToValue(savedTuplelist)
            self.valid = True
        else:
            self.value = None
            self.valid = False

    def validate(self):
        valid = self.isValid(self.value)
        if valid == True:
            self.valid = True
            self.database.saveTuplelist(
                self.databaseValueToTuplelist(self.value))
        return valid

    def updateValue(self, value):
        if self.isValid(value) == True:
            self.value = value
            self.valueChanged.emit()

    def databaseTuplelistToValue(self, tupleList):
        raise Exception(
            f"valueFromDatabaseFormat method not implemented for {self.__class__.__name__}"
        )

    def databaseValueToTuplelist(self, data):
        raise Exception(
            f"valueToDatabaseFormat method not implemented for {self.__class__.__name__}"
        )

from Framework.Database import Database
from Framework.Datapoint import Datapoint
from easygui import diropenbox


class Path(Datapoint):

    def __init__(self) -> None:
        super().__init__()

    def getValue(self, savedValue, calculatedValue):
        if savedValue is None:
            return None, True
        else:
            return savedValue, False

    def readFrom(self, dataElement):
        return diropenbox()

    def writeTo(self, dataElement, data):
        pass

    def valueFromDatabaseFormat(self, tupleList):
        return tupleList[0][0]

    def valueToDatabaseFormat(self, data):
        return [(data,)]

    def validate(self, data):
        if data is not None:
            return True, ""
        else:
            return False, "Es muss ein Pfad ausgewählt werden."

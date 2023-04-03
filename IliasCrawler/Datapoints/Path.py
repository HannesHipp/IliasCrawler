from Framework.Database import Database
from Framework.Datapoint import Datapoint
from easygui import diropenbox


class Path(Datapoint):

    def __init__(self) -> None:
        super().__init__()

    def isValid(self, value):
        if value:
            return True
        else:
            return "Es muss ein Pfad ausgewählt werden."

    def databaseTuplelistToValue(self, tupleList):
        return tupleList[0][0]

    def databaseValueToTuplelist(self, path):
        return [(path,)]

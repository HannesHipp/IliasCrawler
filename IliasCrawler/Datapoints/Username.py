from Framework.Database import Database
from Framework.Datapoint import Datapoint


class Username(Datapoint):

    def __init__(self) -> None:
        super().__init__()

    def databaseTuplelistToValue(self, tupleList):
        return tupleList[0][0]

    def databaseValueToTuplelist(self, username):
        return [(username,)]

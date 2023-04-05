from Framework.Datapoint import Datapoint


class Username(Datapoint):

    def __init__(self) -> None:
        super().__init__()

    def isValid(self, value):
        if value:
            return True
        else:
            return "Der Benutzername ist nicht korrekt."

    def databaseTuplelistToValue(self, tupleList):
        return tupleList[0][0]

    def databaseValueToTuplelist(self, username):
        return [(username,)]

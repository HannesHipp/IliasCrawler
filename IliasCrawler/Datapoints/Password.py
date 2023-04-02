from Framework.Datapoint import Datapoint


class Password(Datapoint):

    def __init__(self) -> None:
        super().__init__()

    def isValid(self, value):
        if value:
            return True
        else:
            return "Das Passwort ist nicht korrekt."

    def databaseTuplelistToValue(self, tupleList):
        return tupleList[0][0]

    def databaseValueToTuplelist(self, password):
        return [(password,)]

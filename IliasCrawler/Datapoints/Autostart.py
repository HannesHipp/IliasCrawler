from Framework.Datapoint import Datapoint


class Autostart(Datapoint):

    def __init__(self) -> None:
        super().__init__()

    def isValid(self, value):
        return True

    def databaseTuplelistToValue(self, tupleList):
        if tupleList[0][0] == '1':
            return True
        else:
            return False

    def databaseValueToTuplelist(self, autostart):
        if autostart:
            return [('1',)]
        else:
            return [('0',)]

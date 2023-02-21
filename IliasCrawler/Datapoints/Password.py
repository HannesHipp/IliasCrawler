from Framework.Datapoint import Datapoint


class Password(Datapoint):

    def __init__(self) -> None:
        super().__init__()

    def getValue(self, savedValue, calculatedValue):
        if savedValue is None:
            return None, True
        else:
            return savedValue, False

    def readFrom(self, dataElement):
        return dataElement.text()

    def writeTo(self, dataElement, data):
        dataElement.setText(data)

    def valueFromDatabaseFormat(self, tupleList):
        return tupleList[0][0]

    def valueToDatabaseFormat(self, data):
        return [(data,)]

    def validate(self, data):
        if data is None:
            return False, "Es muss ein Nutzername eingegeben werden."
        else:
            return True, ""

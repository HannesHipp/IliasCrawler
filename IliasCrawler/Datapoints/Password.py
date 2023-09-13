from Framework.Datapoint import Datapoint


class Password(Datapoint):

    def __init__(self) -> None:
        super().__init__()

    def is_valid(self, value):
        if value:
            return True
        else:
            return "Das Passwort ist nicht korrekt."

    def tuple_list_to_value(self, tupleList):
        return tupleList[0][0]

    def value_to_tuple_list(self, password):
        return [(password,)]

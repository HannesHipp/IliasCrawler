from Framework.Datapoint import Datapoint


class Autostart(Datapoint):

    def __init__(self) -> None:
        super().__init__()

    def is_valid(self, value):
        return True

    def tuple_list_to_value(self, tupleList):
        if tupleList[0][0] == '1':
            return True
        else:
            return False

    def value_to_tuple_list(self, autostart):
        if autostart:
            return [('1',)]
        else:
            return [('0',)]

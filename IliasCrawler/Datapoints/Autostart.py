from Framework.Datapoint import Datapoint


class Autostart(Datapoint):

    def __init__(self) -> None:
        super().__init__()

    def is_valid(self, value):
        return True

    def tuple_list_to_value(self, tuple_list):
        if not tuple_list:
            return False
        if tuple_list[0][0] == '0':
            return False
        return True

    def value_to_tuple_list(self, autostart):
        if autostart:
            return [('1',)]
        else:
            return [('0',)]

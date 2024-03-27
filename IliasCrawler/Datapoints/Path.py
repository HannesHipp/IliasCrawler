import pathlib
from Framework.Datapoint import Datapoint


class Path(Datapoint):

    def __init__(self) -> None:
        super().__init__()

    def is_valid(self, value):
        if value:
            return True
        else:
            return "Es muss ein Pfad ausgewählt werden."

    def tuple_list_to_value(self, tuple_list):
        if not tuple_list:
            return None
        return pathlib.Path(tuple_list[0][0])

    def value_to_tuple_list(self, path):
        return [(str(path),)]

from PyQt5.QtCore import QObject, pyqtSignal
from Framework.Database import Database


class Datapoint(QObject):

    value_changed = pyqtSignal()
    invalidate = pyqtSignal()

    def __init__(self, save=True) -> None:
        super().__init__()
        value = None
        database = None
        if save:
            database = Database(self.__class__.__name__.lower())
            if savedTuplelist := database.getTuplelist():
                value = self.tuple_list_to_value(savedTuplelist)
        self.database = database
        self.value = value
        self.invalidate.connect(self._invalidate)

    def _set_value(self, value):
        self.value = value
        self.value_changed.emit()

    def submit_value(self, value):
        error = self.has_error(value)
        if not error:
            self._set_value(value)
        return error
    
    def _invalidate(self):
        self._set_value(None)
        if self.database:
            self.database.clearTable()

    def save_to_db(self):
        if self.database:
            self.database.saveTuplelist(
                self.value_to_tuple_list(self.value))

    def has_error(self, value):
        response = self.is_valid(value)
        if response is True:
            return None
        return response
    
    def is_valid(self, value):
        return True

    def tuple_list_to_value(self, tupleList):
        raise Exception(
            f"tuple_list_to_value() method not implemented for {self.__class__.__name__}"
        )

    def value_to_tuple_list(self, value):
        raise Exception(
            f"value_to_tuple_list() method not implemented for {self.__class__.__name__}"
        )

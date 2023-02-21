from PyQt5.QtCore import pyqtSignal
from Framework.Datapoint import Datapoint

from Framework.Function import Function


class ValidationError(Exception):

    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class Validator(Function):

    done = pyqtSignal(tuple)

    def __init__(self, *datapoints) -> None:
        super().__init__(*datapoints)

    @staticmethod
    def execute(*datapoints: Datapoint):
        pass
        # valid, error = self.validate(*datapoints)
        # if valid:
        #     for datapoint in datapoints:
        #         datapoint.isValid()
        # else:
        #     raise Exception()

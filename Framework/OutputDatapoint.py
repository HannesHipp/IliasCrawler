from Framework.Datapoint import Datapoint


class OutputDatapoint(Datapoint):

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.calculatedValue = None

    def canBeRequested(self):
        return self.value is None and self.calculatedValue is not None

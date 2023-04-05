from Framework.Datapoint import Datapoint


class GuiModul:

    def __init__(self, datapoints: list[Datapoint]) -> None:
        self.datapoints = datapoints

    def update(self):
        raise Exception(
            f"update-method not implemented for {self.__class__.__name__}"
        )

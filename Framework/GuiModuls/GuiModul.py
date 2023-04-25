from Framework.Datapoint import Datapoint


class GuiModul:

    def __init__(self, datapoints: list[Datapoint]) -> None:
        self.datapoints = datapoints

    def validate(self) -> list[str]:
        result = []
        for datapoint in self.datapoints:
            if not datapoint.error:
                datapoint.save()
            else:
                result.append(datapoint.error)
        return result

    def update(self):
        raise Exception(
            f"update-method not implemented for {self.__class__.__name__}"
        )

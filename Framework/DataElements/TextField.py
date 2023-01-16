from Framework.Datapoint import Datapoint


class TextField:

    def __init__(self, datapoint: Datapoint, guiElementName: str) -> None:
        self.datapoint = datapoint
        self.guiElementName = guiElementName

    
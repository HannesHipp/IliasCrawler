from Framework.Datapoint import Datapoint


class LoadingAnimation:

    def __init__(self, datapoint: Datapoint, name) -> None:
        self.datapoint = datapoint
        self.qtElement = None
        self.qtElementName = name

    def setQtElements(self, frame):
        self.qtElement = getattr(frame, self.qtElementName)
        # set up start and stop

from PyQt5.QtCore import QObject, pyqtSignal
from Framework.Frame import Frame
from Framework.Database import Database


class Datapoint(QObject):

    request = pyqtSignal()
    done = pyqtSignal()
    display = pyqtSignal(object)
    sendError = pyqtSignal(str)

    def __init__(self, **kwargs) -> None:
        super().__init__()
        self.value = None
        self.savedValue = None
        self.calculatedValue = None
        self.valueToBeValidated = None
       
        self.database = Database(
            self.__class__.__name__,
            kwargs['databaseStructure']
        )
        frame = kwargs.pop('frame', None)
        if frame:
            self.frame = frame
            frame.datapoints.append(self)
            self.dataElement = getattr(frame, kwargs['dataElementName'])
        self.request.connect(self.getValue)

    def canBeRequested(self):
        return self.value is None and self.valueToBeValidated is None

    def getValue(self):
        self.savedValue = self.getSavedValue()
        self.howToGetValue()

    def displayFrame(self):
        self.display.emit(self.frame)

    def toDoAfterTrigger(self):
        data = self.extractFromDataElement()
        try:
            valid, error = self.validate(data)
            if valid:
                self.setValue(data)
            else:
                self.showError(error)
            self.done.emit()
        except:
            self.valueToBeValidated = data        

    def setValue(self, value):
        self.value = value
        self.saveValue()

    def getSavedValue(self):
        raise Exception(f"getSavedValue method not implemented for {self.__class__.__name__}")

    def howToGetValue(self):
        raise Exception(f"howToGetValue method not implemented for {self.__class__.__name__}")

    def saveValue(self, value):
        raise Exception(f"saveValue method not implemented for {self.__class__.__name__}")

    def extractFromDataElement(self):
        raise Exception(f"extractFromDataElement method not implemented for {self.__class__.__name__}")



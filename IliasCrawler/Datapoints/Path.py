from Framework.Database import Database
from Framework.InputDatapoint import InputDatapoint
from easygui import diropenbox


class Path(InputDatapoint):

    def __init__(self, **kwargs) -> None:
        super().__init__(
            databaseStructure = ('path',),
            dataElementName = "button_select_path",
            **kwargs
        )

    def howToGetValue(self):
        if self.savedValue is None:
            self.displayFrame()
        else:
            self.setValue(self.savedValue)
    
    def extractFromDataElement(self):
        return diropenbox()

    def validate(self, data):
        if data is not None:
            return True, ""
        else:
            return False, "Es muss ein Pfad ausgewählt werden."

    def getSavedValue(self):
        tupleList = self.database.getTupleList()
        if tupleList is None:
            return None
        else:
            return tupleList[0][0]

    def saveValue(self):
        self.database.saveTupleList([(self.value,)])

from Framework.InputDatapoint import InputDatapoint


class Password(InputDatapoint):

    def __init__(self, **kwargs) -> None:
        super().__init__(
            databaseStructure = ('password',),
            dataElementName = "textfield_password",
            **kwargs
            )

    def howToGetValue(self):
        if self.savedValue is None:
            self.display.emit(self.frame)
        else:
            self.setValue(self.savedValue)
    
    def extractFromDataElement(self):
        return self.dataElement.text()

    def getSavedValue(self):
        tupleList = self.database.getTupleList()
        if tupleList is None:
            return None
        else:
            return tupleList[0][0]

    def saveValue(self):
        self.database.saveTupleList([(self.value,)])
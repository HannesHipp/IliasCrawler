from Framework.Database import Database
from Framework.Datapoint import Datapoint



class FilesAndVideos(Datapoint):

    def __init__(self, **kwargs) -> None:
        super().__init__(
            databaseStructure = ('hash', 'shouldBeDownloaded'),
            **kwargs
        )

    def howToGetValue(self):
        filesOnDisk = self.savedValue
        allFiles = self.calculatedValue
        result = []
        for file in allFiles:
            if file.getHash() not in filesOnDisk:
                result.append(file)
        self.setValue(result)

    def getSavedValue(self):
        tupleList = self.database.getTupleList()
        result = []
        for tuple in tupleList:
            result.append(tuple[0])
        return result

    def saveValue(self):
        allFiles = self.calculatedValue
        result = []
        for file in allFiles:
            result.append((file.getHash(),))
        self.database.saveTupleList(result)
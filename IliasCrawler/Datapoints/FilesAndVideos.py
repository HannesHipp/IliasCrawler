from Framework.Datapoint import Datapoint


class FilesAndVideos(Datapoint):

    def __init__(self, **kwargs) -> None:
        super().__init__(
            **kwargs,
            numberOfDatabaseFields = 1
        )

    def getValue(self, savedValue, calculatedValue):
        filesOnDisk = savedValue
        allFiles = calculatedValue
        for file in allFiles:
            if file.get_hash() not in filesOnDisk:
                file.shouldBeDownloaded = True
            else: 
                file.shouldBeDownloaded = False
        return allFiles, False

    def valueFromDatabaseFormat(self, tupleList):
        result = []
        for tuple in tupleList:
            result.append(tuple[0])
        return result

    def valueToDatabaseFormat(self, allFiles):
        result = []
        for file in allFiles:
            result.append((file.getHash(),))
        return result
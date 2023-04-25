from Framework.Datapoint import Datapoint


class FilesAndVideos(Datapoint):

    def __init__(self) -> None:
        super().__init__()

    def databaseTuplelistToValue(self, tupleList):
        result = []
        for tuple in tupleList:
            result.append(tuple[0])
        return result

    def databaseValueToTuplelist(self, allFiles):
        result = []
        for file in allFiles:
            result.append((file.getHash(),))
        return result

from Framework.Datapoint import Datapoint


class FilesAndVideos(Datapoint):

    def __init__(self) -> None:
        super().__init__()

    def tuple_list_to_value(self, tupleList):
        result = []
        for tuple in tupleList:
            result.append(tuple[0])
        return result

    def value_to_tuple_list(self, allFiles):
        result = []
        for file in allFiles:
            result.append((file.getHash(),))
        return result

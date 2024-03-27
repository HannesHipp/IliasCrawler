from Framework.Datapoint import Datapoint


class FilesAndVideos(Datapoint):

    def __init__(self) -> None:
        super().__init__()

    def tuple_list_to_value(self, tupleList):
        result = {
            'files': [],
            'videos': []
        }
        for tuple in tupleList:
            if tuple[0] == 'file':
                result['files'].append(tuple[1])
            elif tuple[0] == 'video':
                result['videos'].append(tuple[1])
        return result

    def value_to_tuple_list(self, files_and_videos):
        result = []
        for file in files_and_videos:
            if file.type.name == 'file':
                result.append(('file', get_file_hash(file)))
            elif file.type.name == 'video':
                result.append(('video', get_video_hash(file)))
        return result


def get_file_hash(file):
        return file.url.split("_file_")[1][:7]

def get_video_hash(video):
        return video.url.split("/")[6]
from Framework.Datapoint import Datapoint
from distutils.util import strtobool


class Courses(Datapoint):

    def __init__(self) -> None:
        super().__init__()

    def tuple_list_to_value(self, tupleList: list[tuple]):
        result = []
        # for tuple in tupleList:
        #     course = Course(name=tuple[1], url=tuple[0], parent=None)
        #     course.should_be_downloaded = strtobool(tuple[2])
        #     result.append(course)
        return result

    def value_to_tuple_list(self, courses):
        result = []
        for course in courses:
            result.append(
                (course.url, course.name, str(course.shouldBeDownloaded)))
        return result

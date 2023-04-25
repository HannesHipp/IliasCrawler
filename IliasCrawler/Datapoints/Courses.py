from Framework.Datapoint import Datapoint
from IliasCrawler.model.Course import Course
from distutils.util import strtobool


class Courses(Datapoint):

    def __init__(self) -> None:
        super().__init__()

    def databaseTuplelistToValue(self, tupleList: list[tuple]):
        result = []
        for tuple in tupleList:
            course = Course(tuple[1], tuple[0], None)
            course.shouldBeDownloaded = strtobool(tuple[2])
            result.append(course)
        return result

    def databaseValueToTuplelist(self, courses):
        result = []
        for course in courses:
            result.append(
                (course.url, course.name, str(course.shouldBeDownloaded)))
        return result

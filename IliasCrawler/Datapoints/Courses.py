from Framework.Datapoint import Datapoint
from IliasCrawler.model.Course import Course
from distutils.util import strtobool


class Courses(Datapoint):

    def __init__(self) -> None:
        super().__init__()

    def isValid(self, value: list[Course]):
        for course in value:
            if course.shouldBeDownloaded:
                return True
        return "Es muss mindestens ein Kurs ausgewählt werden."

    def databaseTuplelistToValue(self, tupleList: list[tuple]):
        result = []
        for tuple in tupleList:
            course = Course(tuple[0], tuple[1], None)
            course.shouldBeDownloaded = strtobool(tuple[2])
            result.append(course)
        return result

    def databaseValueToTuplelist(self, courses):
        result = []
        for course in courses:
            result.append(
                (course.name, course.url, str(course.shouldBeDownloaded)))
        return result

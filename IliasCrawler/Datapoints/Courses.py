from Framework.Datapoint import Datapoint


class Courses(Datapoint):

    def __init__(self) -> None:
        super().__init__()

    def tuple_list_to_value(self, tuple_list: list[tuple]):
        result = {}
        for tuple in tuple_list:
            result[tuple[0]] = True if tuple[1] == '1' else False
        return result

    def value_to_tuple_list(self, courses):
        result = []
        for course in courses:
            result.append((
                course.get_hash(), 
                '1' if course.to_download else '0'
            ))
        return result


class Course:

    def __init__(self, element) -> None:
        self.element = element
        self.name = element.name
        self.to_download = False
        self.is_new = False
        self.was_crawled = False

    def get_hash(self):
        return self.element.url.split("crs_")[1].split(".html")[0]
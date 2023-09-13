from Framework.Function import Function
from IliasCrawler.Datapoints.Courses import Courses
from IliasCrawler.Datapoints.Username import Username
from IliasCrawler.Datapoints.Password import Password
from IliasCrawler.Session import Session
from IliasCrawler.models.ilias.Element import Element, convertDictToElementTree
from IliasCrawler.models.Extractor import Extractor


class GetCourses(Function):

    def __init__(self, username: Username, password: Password, courses: Courses) -> None:
        super().__init__()
        self.username = username
        self.password = password
        self.courses = courses

    def execute(self):
        COURSES_URL = 'https://ilias3.uni-stuttgart.de/ilias.php?baseClass=ilDashboardGUI&cmd=jumpToSelectedItems'
        Session.set_session(self.username.value, self.password.value)
        htmlSoup = Session.get_content(COURSES_URL)
        extractor = Extractor('IliasCrawler\models\ilias\model.json')
        data = extractor.start_extraction(htmlSoup)
        root = Element('Ilias', None, 0)
        convertDictToElementTree(data, root)
        if self.courses.value:
            hashToDownload = {
                course.getHash(): course.shouldBeDownloaded for course in self.courses.value}
        else:
            hashToDownload = {}
        allCourses = root.get_new_pages()
        for course in allCourses:
            hash = course.getHash()
            shouldBeDownloaded = False
            if hash in hashToDownload:
                course.isNew = False
                if hashToDownload[hash]:
                    shouldBeDownloaded = True
            else:
                course.isNew = True
            course.shouldBeDownloaded = shouldBeDownloaded
        self.courses.submit_value(allCourses)

from Framework.Function import Function
from IliasCrawler.Datapoints.Courses import Courses
from IliasCrawler.Datapoints.Username import Username
from IliasCrawler.Datapoints.Password import Password
from IliasCrawler.Session import Session
from IliasCrawler.model.Ilias import Ilias


class GetCourses(Function):

    def __init__(self, username: Username, password: Password, courses: Courses) -> None:
        super().__init__()
        self.username = username
        self.password = password
        self.courses = courses

    def execute(self):
        Session(self.username.value, self.password.value)
        root = Ilias('Ilias',
                     'https://ilias3.uni-stuttgart.de/ilias.php?baseClass=ilDashboardGUI&cmd=jumpToSelectedItems',
                     None)
        root.content = Session.get_content(root.url)
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
        self.courses.updateValue(allCourses)

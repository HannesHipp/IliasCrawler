from Framework.Function import Function
from IliasCrawler.Session import Session
from IliasCrawler.model.Ilias import Ilias
from IliasCrawler.model.Course import Course
import time


class GetCourses(Function):

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.username = kwargs['username']
        self.password = kwargs['password']

    def execute(self, progress_signal):
        Session.setGlobalSession(Session(self.username.value, self.password.value))
        root = Ilias('Ilias',
                    'https://ilias3.uni-stuttgart.de/ilias.php?baseClass=ilDashboardGUI&cmd=jumpToSelectedItems',
                    None)
        root.content = Session.get_content(root.url)
        return root.get_new_pages()
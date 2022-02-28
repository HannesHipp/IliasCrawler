from controller.Frame import Frame
from controller.CourseSelectionController import CourseSelectionController
from model.Ilias import Ilias
from service.BusinessModel import BusinessModel

from service.Database import Database
from service.Session import Session


class CourseLoadingController(Frame):

    def __new__(cls, container):
        if not hasattr(cls, 'instance'):
            cls.instance = super(CourseLoadingController, cls).__new__(cls)
        return cls.instance

    def __init__(self, container):   
        self.ui_file_location = 'C:\\Users\\Hannes\\Code Projekte\\IliasCrawler\\IliasCrawler\\resources\\CourseLoadingView.ui'
        super().__init__(container)

    def show(self):
        super().show()
        BusinessModel.instance.initialize()
        BusinessModel.instance.set_fresh_courses(self.crawl_courses())
        CourseSelectionController.instance.show()  

    def crawl_courses(self):
        ilias = Ilias(name='Ilias', url='https://ilias3.uni-stuttgart.de/ilias.php?baseClass=ilDashboardGUI&cmd=jumpToSelectedItems', parent=None)
        ilias.set_content()
        return ilias.get_new_pages()


from model.Page import Page
from model.Course import Course
from service.Session import Session


class Ilias(Page):

    downloadable_types = []

    @staticmethod
    def get_sub_page_types():
        return [Course]

    @staticmethod
    def create():
        url = 'https://ilias3.uni-stuttgart.de/ilias.php?cmdClass=ilmembershipoverviewgui&cmdNode=k2&baseClass=ilmembershipoverviewgui'
        return Ilias('Ilias',
                     url,
                     None)

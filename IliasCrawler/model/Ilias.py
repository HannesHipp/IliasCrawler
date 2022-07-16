from IliasCrawler.model.Page import Page
from IliasCrawler.model.Course import Course


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

from IliasCrawler.model.Element import Element
from IliasCrawler.model.Page import Page
from IliasCrawler.model.File import File
from IliasCrawler.model.Video import Video


class Lm(Page):

    url_markers = ['_lm_', 'ilLMPresentationGUI']
    downloadable_types = [File, Video]

    @staticmethod
    def get_sub_page_types():
        return [Lm]

    def __init__(self, name, url, parent, number):
        super().__init__(name, url, parent)
        self.number = number

    @staticmethod
    def create(name, url, parent):
        if type(parent) is Lm:
            number = parent.number + 1
            parent = Lm.get_parent(parent)
            name = f"{number} {name}"
        else:
            url = "https://ilias3.uni-stuttgart.de/" \
                  "ilias.php?ref_id=" + url.split("_")[4].split(".")[0] + \
                  "&obj_id=1&cmd=layout&cmdClass=illmpresentationgui&cmdNode=gw&baseClass=ilLMPresentationGUI"
            parent = Lm(name,
                        url,
                        parent,
                        0)
            name = "1"
            number = 1
        return Lm(name,
                  url,
                  parent,
                  number)

    @staticmethod
    def get_raw_elements(page):
        if type(page) is Lm:
            return [page.content.find(class_='ilc_page_rnavlink_RightNavigationLink')]
        else:
            return Element.get_raw_elements(page)

    @staticmethod
    def get_parent(lm_page):
        if lm_page.number == 0:
            return lm_page
        else:
            return Lm.get_parent(lm_page.parent)

    @staticmethod
    def is_valid(bs4_element):
        if any(x in Lm.get_url(bs4_element) for x in Lm.url_markers):
            return True
        return False

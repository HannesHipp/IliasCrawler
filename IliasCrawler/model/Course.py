from IliasCrawler.model.Page import Page
from IliasCrawler.model.Element import Element
from IliasCrawler.model.File import File
from IliasCrawler.model.Folder import Folder
from IliasCrawler.model.Lm import Lm
from IliasCrawler.model.MCH import MCH
from IliasCrawler.model.OPD import OPD
from IliasCrawler.model.Video import Video


class Course(Element):

    url_markers = ['_crs_']
    downloadable_types = [File, Video]

    @staticmethod
    def get_sub_page_types():
        return [Folder, Lm, OPD, MCH]

    def __init__(self, name, url, parent):
        super().__init__(name, url, parent)
        self.is_new = None
        self.should_be_downloaded = None

    def getHash(self):
        return self.url.split("crs_")[1].split(".html")[0]

    @staticmethod
    def create(name, url, parent):
        return Course(name,
                      url,
                      parent)

    @staticmethod
    def is_valid(bs4_element):
        if any(x in Course.get_url(bs4_element) for x in Course.url_markers):
            return True
        return False
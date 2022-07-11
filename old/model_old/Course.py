from model.Element import Element
from model.File import File
from model.Folder import Folder
from model.Lm import Lm
from model.MCH import MCH
from model.OPD import OPD
from model.Video import Video
from service.EventsManagement import EventsManager


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

    def get_hash(self):
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
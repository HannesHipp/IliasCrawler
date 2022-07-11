from model.Page import Page
from model.File import File
from model.Video import Video
from model.Lm import Lm
from model.OPD import OPD
from model.MCH import MCH
from service.Exceptions import NoUrlException


class Folder(Page):

    url_markers = ['_fold_', 'Cmd=showSeries']
    downloadable_types = [File, Video]

    @staticmethod
    def get_sub_page_types():
        return [Folder, Lm, OPD, MCH]

    @staticmethod
    def create(name, url,  parent):
        return Folder(name,
                      url,
                      parent)

    @staticmethod
    def is_valid(bs4_element):
        if any(x in Folder.get_url(bs4_element) for x in Folder.url_markers):
            return True
        return False
        

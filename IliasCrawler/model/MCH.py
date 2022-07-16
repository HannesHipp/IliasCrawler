from IliasCrawler.model.Page import Page
from IliasCrawler.model.File import File
from IliasCrawler.model.Video import Video


class MCH(Page):

    url_markers = ['MediaCastHandler']
    downloadable_types = [File, Video]

    @staticmethod
    def get_sub_page_types():
        return []

    @staticmethod
    def create(name, url, parent):
        return MCH(name,
                   url,
                   parent)

    @staticmethod
    def is_valid(bs4_element):
        if any(x in MCH.get_url(bs4_element) for x in MCH.url_markers):
            return True
        return False

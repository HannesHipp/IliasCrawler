from model.Downloadable import Downloadable
from service.Exceptions import NoNameException, NoUrlException

class Video(Downloadable):

    url_markers = ['.mp4', 'webm']
    url_prefixes = {'Uni_Stuttgart/mobs/' : 'https://ilias3.uni-stuttgart.de/', 'mh_default_org/api' : 'https://occdn1.tik.uni-stuttgart.de/'}

    @staticmethod
    def create(name, url, parent):
        return Video(name,
                     url,
                     parent)

    def get_hash(self):
        return self.url.split("/")[6]

    @staticmethod
    def get_name(bs4_element):
        try:
            return bs4_element.attrs['src'].split('?il_wac_token')[0].split('/')[-1]
        except (KeyError, AttributeError):
            return NoNameException

    @staticmethod
    def get_url(bs4_element):
        try:    
            return bs4_element.attrs['src']
        except (KeyError, AttributeError):
            return NoUrlException

    @staticmethod
    def get_raw_elements(page):
        return page.content.findAll('source')

    @staticmethod
    def is_valid(bs4_element):
        if any(x in Video.get_url(bs4_element) for x in Video.url_markers):
            return True
        return False
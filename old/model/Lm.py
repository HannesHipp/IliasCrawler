from model.File import File
from model.HTML_Extractor import HTML_Extractor
from model.LmSubPage import LmSubPage
from model.Page import Page
from model.Video import Video
from model.LmSubPageContainer import LmSubPageContainer


class Lm(Page):
    
    extractor = HTML_Extractor(
        {'href' : {'contains' : '_lm_'}},
        'text',
        'href'
    )
    on_page_container_types = []
    downloadable_types = [File, Video]
    tree_importance = 0

    @staticmethod
    def sub_page_types():
        return [LmSubPage]
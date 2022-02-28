from model.File import File
from model.HTML_Extractor import HTML_Extractor
from model.IlContainerBlock import IlContainerBlock
from model.Lm import Lm
from model.Page import Page
from model.Video import Video


class Folder(Page):
    
    extractor = HTML_Extractor(
        {'href' : {'contains' : '_fold_'}},
        'text',
        'href'
    )
    on_page_container_types = [IlContainerBlock]
    downloadable_types = [File, Video]
    tree_importance = 1

    @staticmethod
    def sub_page_types():
        return [Lm]
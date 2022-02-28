from model.File import File
from model.Folder import Folder
from model.HTML_Extractor import HTML_Extractor
from model.IlContainerBlock import IlContainerBlock
from model.Lm import Lm
from model.Page import Page
from model.Video import Video


class Course(Page):
    
    extractor = HTML_Extractor(
        {'href' : {'contains' : '_crs_'}},
        'text',
        'href'
    )
    on_page_container_types = [IlContainerBlock]
    downloadable_types = [File, Video]
    tree_importance = 0

    @staticmethod
    def sub_page_types():
        return [Lm, Folder]

    def __init__(self, **parameters):
        super().__init__(**parameters)
        self.is_new = None
        self.should_be_downloaded = None

    def get_hash(self):
        return self.url.split("crs_")[1].split(".html")[0]
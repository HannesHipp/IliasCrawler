from model.File import File
from model.HTML_Extractor import HTML_Extractor
from model.Page import Page
from model.Video import Video


class LmSubPage(Page):

    extractor = HTML_Extractor(
        {'and' : (
            {'name' : {'equals' : 'a'}},
            {'parent' : {'and' : (
                {'name' : {'equals' : 'li'}},
                {'not' : (
                    {'contents' : {'contains' : {'name' : {'equals' : 'ul'}}}},
                )},
                {'id' : {'contains' : 'exp_node_lm_exp'}}
            )}}
        )},
        'text',
        'href',
        {'class' : {'contains' : 'ilExp2NodeContent'}}
    )
    on_page_container_types = []
    downloadable_types = [File, Video]
    tree_importance = 0

    @staticmethod
    def sub_page_types():
        return []

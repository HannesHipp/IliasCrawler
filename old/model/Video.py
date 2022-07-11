from model.Downloadable import Downloadable
from model.HTML_Extractor import HTML_Extractor


class Video(Downloadable):
    
    extractor = HTML_Extractor(
        {'and': (
            {'name' : {'equals' : 'source'}},
            {'src' : {'or' : (
                {'contains' : '.mp4'},
                {'contains' : 'webm'}
            )}}
        )},
        '',
        'src'
    )
    url_prefixes = {'Uni_Stuttgart/mobs/' : 'https://ilias3.uni-stuttgart.de/', 'mh_default_org/api' : 'https://occdn1.tik.uni-stuttgart.de/'}
    tree_importance = 0

    def get_name(self, bs4_element):
        return type(self).extractor.extract_url_from(bs4_element).split('?il_wac_token')[0].split('/')[-1]

    def get_hash(self):
        return self.url.split("/")[6]
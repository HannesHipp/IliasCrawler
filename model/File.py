from model.Downloadable import Downloadable
from model.HTML_Extractor import HTML_Extractor


class File(Downloadable):
    
    extractor = HTML_Extractor(
        {'href' : {'contains' : '_file_'}},
        'text',
        'href'
    )
    tree_importance = 0
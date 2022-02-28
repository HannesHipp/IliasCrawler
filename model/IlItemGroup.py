from model.HTML_Extractor import HTML_Extractor
from model.OnPageContainer import OnPageContainer


class IlItemGroup(OnPageContainer):

    extractor = HTML_Extractor(
        {'class' : {'equals' : 'il-item-group'}},
        'text',
        'href',
        {'name' : {'equals' : 'h3'}}
    )
    tree_importance = 0

    def get_name(self, bs4_element):
        name_element = type(self).extractor.extract_name_from(bs4_element)[0]
        return name_element.text

    def get_url(self, bs4_element):
        return "http"
from model.OnPageContainer import OnPageContainer
from model.HTML_Extractor import HTML_Extractor


class LmSubPageContainer(OnPageContainer):
    
    extractor = HTML_Extractor(
        {'and' : (
            {'name' : {'equals' : 'li'}},
            {'contents' : {'contains' : {'name' : {'equals' : 'ul'}}}},
            {'id' : {'contains' : 'exp_node_lm_exp'}}
        )},
        'text',
        'href',
        {'class' : {'equals' : 'ilExp2NodeContent'}}
    )
    tree_importance = 0

from model.HTML_Extractor import HTML_Extractor
from model.OnPageContainer import OnPageContainer


class IlContainerBlock(OnPageContainer):
    
    extractor = HTML_Extractor(
        {'class' : {'equals' : 'ilContainerBlock container-fluid form-inline'}},
        'text',
        'href',
        {'class' : {'equals' : 'ilHeader ilContainerBlockHeader'}}
    )
    tree_importance = 2

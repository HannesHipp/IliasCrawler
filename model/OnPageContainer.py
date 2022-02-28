from model.Container import Container


class OnPageContainer(Container):
    
    def __init__(self, bs4_element, parent):
        super().__init__(bs4_element = bs4_element, parent = parent)
        self.id = id(bs4_element)

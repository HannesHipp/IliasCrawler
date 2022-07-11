from model.Element import Element


class Container(Element):
    
    def __init__(self, **parameters):
        super().__init__(**parameters)
        self.children = []
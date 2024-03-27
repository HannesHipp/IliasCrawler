from IliasCrawler.models.extractor.DynamicAttribute import DynamicAttribute
from IliasCrawler.models.extractor.Locator import Locator
from IliasCrawler.models.extractor.Element import Element

class Type:

    def __init__(self, name, instructions) -> None:
        self.name = name
        self.is_leaf = 'is_leaf' in instructions
        self.child_types = []
        if self.name == 'root':
            self.extraction_strategy = None
        elif 'locator' in instructions:
            self.extraction_strategy = XMLExtractionStrategy(instructions)
        else:
            self.extraction_strategy = FunctionExtractionStrategy(instructions)
    
    def add_child_type(self, child_type):
        self.child_types.append(child_type)

    def extract(self, parent):
        elements = self.extraction_strategy.extract(parent.soup)
        for element in elements:
            element.type = self
            element.parent = parent
        return elements
    


class XMLExtractionStrategy:

    def __init__(self, instructions) -> None:
        self.locator: Locator = Locator(instructions['locator'])
        self.static_attrs = {}
        self.dynamic_attrs = []
        if attrs := instructions.get('attrs', None):
            for attr in attrs:
                name = list(attr.keys())[0]
                value = attr[name]
                if isinstance(value, dict) and 'attrName' in value:
                    self.dynamic_attrs.append(DynamicAttribute(name, value))
                else:
                    self.static_attrs[name] = value       

    def extract(self, parent_soup):
        canidates = self.locator.find_elements(parent_soup)
        elements = self.add_dynamic_attrs(canidates)
        elements = self.add_static_attrs(elements)
        return elements
        
    def add_dynamic_attrs(self, canidates):
        elements = []
        for canidate in canidates:
            element = Element()
            valid = True
            for attr in self.dynamic_attrs:
                value = attr.get_value(canidate)
                if not value:
                    valid = False
                    break
                setattr(element, attr.name, value)
            if valid:
                element.set_soup(canidate.extract())
                elements.append(element)
        return elements

    def add_static_attrs(self, elements):
        for element in elements:
            for attr, value in self.static_attrs.items():
                setattr(element, attr, value)
        return elements


class FunctionExtractionStrategy:

    def __init__(self, instructions) -> None:
        self.function = None
        
    def extract(self, parent_soup):
        return self.function(parent_soup)
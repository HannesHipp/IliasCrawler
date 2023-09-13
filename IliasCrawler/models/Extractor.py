import json
from bs4 import BeautifulSoup, Tag


class Element:

    def __init__(self, type: str, parent) -> None:
        self.type = type
        self.soup = None
        self.parent = parent

    def set_soup(self, soup):
        self.soup = soup

    def delete_soup(self):
        self.soup = None


class Extractor:

    def __init__(self, jsonPath: str) -> None:
        self.model = json.load(open(jsonPath))

    def extract_data(self, parent: Element):
        leafs = []
        childTypes = self.model[parent.type]['childTypes']
        for child_type in childTypes:
            locator = self.model[child_type]['locator']
            elements = Extractor.find_elements(parent.soup, locator)
            elements = self.add_attributes(elements, child_type, parent)
            if self.model[child_type]['endpoint']:
                leafs.extend(elements)
            else:
                for element in elements:
                    leafs.extend(self.extract_data(element))
                    element.delete_soup()
        return leafs

    @staticmethod
    def find_elements(soup: BeautifulSoup, locator: dict) -> list[Tag]:
        exact, name, contains, subitem = Extractor.parse_locator(locator)
        if exact:
            matches = soup.find_all(attrs=exact)
            if name:
                matches = [tag for tag in matches if tag.name == name]
        else:
            if name:
                matches = soup.find_all(name)
            else:
                matches = soup.find_all(
                    attrs={key: True for key in contains})
        if contains:
            matches = [tag for tag in matches if Extractor.tag_matches_contains(tag, contains)]
        if subitem:
            matches = Extractor.find_elements(matches[0], subitem)
        return matches

    @staticmethod
    def parse_locator(locator: dict):
        name = locator.get('name', None)
        contains = locator.get('contains', None)
        subitem = locator.get('subitem', None)
        exact = {k: v for k, v in locator.items() if k not in (
            'name', 'contains', 'subitem')}
        if not exact:
            exact = None
        return exact, name, contains, subitem
    

    @staticmethod
    def tag_matches_contains(tag, contains):
        matches = True
        for attr, value_list in contains.items():
            tag_value = Extractor.get_attr(tag, attr)
            for value in value_list:
                if value not in tag_value:
                    matches = False
                    break
        return matches

    def add_attributes(self, canidates: list[Tag], child_type: str, parent):
        elements = []
        fix, variable = self.get_attr_dicts(child_type)
        for canidate in canidates:
            element = Element(child_type, parent)
            for attr in variable:
                soup_attr_name = list(variable[attr].keys())[0]
                locator = variable[attr][soup_attr_name]
                sub_element = Extractor.get_sub_element(canidate, locator)
                if not sub_element:
                    element = None
                    break
                value = Extractor.get_attr(sub_element, soup_attr_name)
                if not value:
                    element = None
                    break
                setattr(element, attr, value)
            if element:
                element.set_soup(canidate.extract())
                for attr, value in fix.items():
                    setattr(element, attr, value)
                elements.append(element)
        return elements

    def get_attr_dicts(self, type):
        type_descr = self.model[type]
        fix = type_descr['fix']
        variable = {k: v for k, v in type_descr.items() if k not in (
            'endpoint', 'childTypes', 'locator', 'fix')}
        return fix, variable

    @staticmethod
    def get_sub_element(tag, locator):
        if locator:
            elements = Extractor.find_elements(tag, locator)
            if elements:
                elements = elements[0]
            return elements
        else:
            return tag

    @staticmethod
    def get_attr(tag, attrName):
        result = tag.get(attrName)
        if not result and hasattr(tag, attrName):
            result = getattr(tag, attrName)
        if isinstance(result, list):
            result = result[0]
        return result

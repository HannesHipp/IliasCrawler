from bs4 import BeautifulSoup
import IliasCrawler.models.extractor.service as service



class ExactFilter:

    def __init__(self, attrs_dict) -> None:
        self.attrs_dict = attrs_dict

    @classmethod
    def create(cls, instructions):
        attrs_dict = {}
        for key, value in instructions.items():
            if key != 'name' and not isinstance(value, dict):
                attrs_dict[key] = value
        if attrs_dict:
            return cls(attrs_dict)
        return None

    def soup(self, soup: BeautifulSoup):
        return soup.find_all(attrs=self.attrs_dict)
    

class NameFilter:

    def __init__(self, name) -> None:
        self.name = name

    @classmethod
    def create(cls, instructions: dict):
        if name := instructions.get('name', None):
            return cls(name)
        else:
            return None
    
    def soup(self, soup: BeautifulSoup):
        return soup.find_all(self.name)
    
    def list(self, soup_or_list):
        return [tag for tag in soup_or_list if tag.name == self.name]
        


class ContainsFilter:

    def __init__(self, contains_dict) -> None:
        self.contains_dict = contains_dict

    @classmethod
    def create(cls, instructions):
        contains_dict = {}
        for key, value in instructions.items():
            if isinstance(value, dict) and 'contains' in value:
                contains_dict[key] = value['contains']
        if contains_dict:
            return cls(contains_dict)
        return None

    def soup(self, soup: BeautifulSoup):
        list = soup.find_all(attrs={key: True for key in self.contains_dict})
        return self.list(list)

    def list(self, list: list):
        return [tag for tag in list if self.tag_matches(tag)]
    
    def tag_matches(self, tag):
        for attr_name, value in self.contains_dict.items():
            tag_value = service.get_attr(tag, attr_name)
            if not tag_value:
                return False
            if value not in tag_value:
                return False
        return True



class HasNoChildrenFilter:

    def __init__(self, locators) -> None:
        self.locators = locators

    @classmethod
    def create(cls, instructions):
        locators = []
        for key, value in instructions.items():
            if key == 'hasNoChildren':
                locators.append(Locator(value))
        if locators:
            return cls(locators)
        return None

    def soup(self, soup):
        raise Exception("hasNoChildren can't be only locator attribute.")

    def list(self, list):
        result = []
        for tag in list:
            tag_valid = True
            for locator in self.locators:
                children = locator.find_elements(tag)
                if children:
                    tag_valid = False
                    break
            if tag_valid:
                result.append(tag)
        return result
            



class Locator:

    FILTER_TYPES = [
        ExactFilter,
        NameFilter,
        ContainsFilter,
        HasNoChildrenFilter
    ]

    def __init__(self, instructions) -> None:
        self.filters = self.initialize_filters(instructions)
        self.sub_item_locator = None
        self.scope = None
        if subitem:= instructions.get('subitem', None):
            self.sub_item_locator = Locator(subitem)
        if scope:= instructions.get('scope', None):
            self.scope = Locator(scope)

    def initialize_filters(self, instructions):
        result = []
        for filter_type in Locator.FILTER_TYPES:
            if obj := filter_type.create(instructions):
                result.append(obj)
        return result

    def find_elements(self, parent_soup):
        if self.scope:
            if scope_soup := self.scope.find_elements(parent_soup):
                parent_soup = scope_soup[0]
        matches = self.filters[0].soup(parent_soup)
        for filter in self.filters[1:]:
            matches = filter.list(matches)
        if matches and self.sub_item_locator:
            matches = self.sub_item_locator.find_elements(matches[0])
        return matches

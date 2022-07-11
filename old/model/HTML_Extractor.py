from bs4.element import Tag as bs4_tag

from service.Exceptions import DoesNotContainNecessaryAttributesException


class HTML_Extractor():

    def __init__(self, find_on_page_dict, name_attribute, url_attribute, find_name_element_dict = None, find_url_element_dict = None):
        self.find_on_page_dict = find_on_page_dict
        self.name_attribute = name_attribute
        self.url_attribute = url_attribute
        self.find_name_element_dict = find_name_element_dict
        self.find_url_element_dict = find_url_element_dict

    def extract_name_from(self, bs4_element):
        if self.find_name_element_dict is None:
            name_element = bs4_element
        else:
            name_element = bs4_element.find(self.extract_name_matches)
        return HTML_Extractor.get_attribute(self.name_attribute, name_element)

    def extract_name_matches(self, bs4_element):
        return HTML_Extractor.matches(self.find_name_element_dict, bs4_element)


    def extract_url_from(self, bs4_element):
        if self.find_url_element_dict is None:
            url_element = bs4_element
        else:
            url_element = bs4_element.find(self.extract_url_matches)
        return HTML_Extractor.get_attribute(self.url_attribute, url_element)

    def extract_url_matches(self, bs4_element):
        return HTML_Extractor.matches(self.find_url_element_dict, bs4_element)


    def extract_from_page(self, bs4_element):
        return bs4_element.findAll(self.extract_from_page_matches)

    def extract_from_page_matches(self, bs4_element):
        return HTML_Extractor.matches(self.find_on_page_dict, bs4_element)

    @staticmethod
    def matches(criterion, element):
        try:
            key = list(criterion.keys())[0]
            criterion = criterion[key]
            if key == 'and':
                result = HTML_Extractor.and_(criterion, element)
            elif key == 'or':
                result = HTML_Extractor.or_(criterion , element)
            elif key == 'not':
                result = HTML_Extractor.not_(criterion, element)
            elif key == 'equals':
                result = HTML_Extractor.equals(criterion, element)
            elif key == 'contains':
                result = HTML_Extractor.contains(criterion, element)
            else:
                attribute_data = HTML_Extractor.get_attribute(key, element)
                result = HTML_Extractor.matches(criterion, attribute_data)
            return result
        except DoesNotContainNecessaryAttributesException:
            return False

    @staticmethod
    def and_(tuple, element):
        result = True
        for dict_ in tuple:
            result = result and HTML_Extractor.matches(dict_, element)
        return result

    @staticmethod
    def or_(tuple, element):
        result = False
        for dict_ in tuple:
            result = result or HTML_Extractor.matches(dict_, element)
        return result

    @staticmethod
    def not_(tuple, element):
        return not HTML_Extractor.matches(tuple[0], element)

    @staticmethod
    def contains(criterion, element):
        result = False
        if type(criterion) == str:
            if type(element) == list:
                element = element[0]
            if criterion in element:
                result = True
        else:
            try:
                for item in list(element):
                    if type(item) is bs4_tag:
                        result = result or HTML_Extractor.matches(criterion, item)
                return result
            except TypeError:
                raise Exception(f"Type of element is not str or list, but {type(element)}")
        return result

    @staticmethod
    def equals(criterion, attribute_data):
        return criterion == attribute_data

    @staticmethod
    def get_attribute(attribute, element):
        result = None
        try:
            result = element.attrs[attribute]
        except:
            if hasattr(element, attribute):
                result = getattr(element, attribute)
        if result:
            return result
        else:
            raise DoesNotContainNecessaryAttributesException
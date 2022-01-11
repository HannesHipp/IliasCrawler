from model.Element import Element as Element
from service.Exceptions import NoNameException, NoUrlException
from service.Session import Session


class Page(Element):

    def __init__(self, name, url, parent):
        super().__init__(name, url, parent)
        self.content = self.get_content()

    def get_files_and_videos(self):
        return self.extract_elements(type(self).downloadable_types)

    def get_new_pages(self):
        return self.extract_elements(type(self).get_sub_page_types())

    def extract_elements(self, types):
        result = []
        for _type in types:
            raw_elements = _type.get_raw_elements(self)
            for raw_element in raw_elements:
                try:
                    if _type.is_valid(raw_element):
                        url = _type.get_url(raw_element)
                        name = _type.get_name(raw_element)
                        if url not in [element.url for element in result]:
                            result.append(_type.create(name, url, self))
                except (NoNameException, NoUrlException):
                    pass       
        return result

    def get_content(self):
        return Session.get_content(self.url)

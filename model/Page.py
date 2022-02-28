from model.Container import Container
from service.BusinessModel import BusinessModel
from service.Exceptions import DoesNotContainNecessaryAttributesException


class Page(Container):

    def crawl(self):
        self.set_content()
        files_and_videos = self.get_files_and_videos()
        new_pages = self.get_new_pages()
        self.content = None
        for new_page in new_pages:
            files_and_videos += new_page.crawl()
        return files_and_videos
    
    def get_files_and_videos(self):
        return self.extract_types(type(self).downloadable_types)

    def get_new_pages(self):
        return self.extract_types(type(self).sub_page_types())

    def extract_types(self, types):
        result = []
        for type_ in types:
            for bs4_element in type_.extractor.extract_from_page(self.content):
                try:
                    parent = self.construct_parents(bs4_element)
                    result.append(type_(bs4_element=bs4_element, parent=parent))
                except DoesNotContainNecessaryAttributesException:
                    pass
        return result

    def construct_parents(self, bs4_element):
        current = bs4_element
        parent_found = False
        while not parent_found:
            if current.parent is None:
                return self
            else:
                current = current.parent
                for on_page_container_type in type(self).on_page_container_types:
                    parent_found = on_page_container_type.extractor.extract_from_page_matches(current) 
        for child in self.children:
            if hasattr(child, 'id'):
                if id(current) == child.id:
                    return child
        return on_page_container_type(current, self.construct_parents(current))

    def set_content(self):
        self.content = BusinessModel.instance.session.get_content(self.url)
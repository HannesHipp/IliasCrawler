import model.Service as Service
from model.Element import Element as Element


class Page(Element):

    def __init__(self, name, url, parent, content):
        super().__init__(name, url, parent)
        self.content = None

    def get_files_and_videos(self):
        pass

    def get_new_pages(self):
        pass

    @staticmethod
    def extract_from_page(content, parent):
        pass

    @staticmethod
    def create(element, parent):
        pass
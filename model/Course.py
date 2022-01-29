from tkinter import E
from model.Element import Element
from model.Folder import Folder
from service.Database import Database
from service.EventsManagement import EventsManager


class Course(Element):

    url_markers = ['_crs_']

    def __init__(self, name, url, parent):
        super().__init__(name, url, parent)
        self.is_new = None
        self.should_be_downloaded = None

    def get_hash(self):
        return self.url.split("crs_")[1].split(".html")[0]
    
    def convert_to_folder(self):
        EventsManager.get_instance().notify_listeners("crawl", (0, 1))
        return Folder(self.name, self.url, self.parent)

    @staticmethod
    def create(name, url, parent):
        return Course(name,
                      url,
                      parent)

    @staticmethod
    def is_valid(bs4_element):
        if any(x in Course.get_url(bs4_element) for x in Course.url_markers):
            return True
        return False
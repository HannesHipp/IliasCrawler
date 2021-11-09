from model.Element import Element as Element
import os
import pickle
import model.Service as Service
import re

from service.Database import Database
from service.Session import Session

pattern = re.compile(r"\.[a-z0-9]{1,4}")

class Downloadable(Element):

    def download(self):
        path = self.get_path()
        if not os.path.isdir(path):
            os.makedirs(path)
        open(path + "\\" + self.name, 'wb').write(Session.get_file_content(self.url))


class File(Downloadable):

    @staticmethod
    def create(element, parent):
        name = str(element.text)
        if '.mp4' in name:
            name = name.split('.mp4')[0] + '.mp4'
        else:
            name = name + '.pdf'
        # try:
        #     name = pattern.split(name)[0] + pattern.search(name)[0]
        # except:
        #     pass
        return File(name,
                    element['href'],
                    parent)

    @staticmethod
    def extract_from_page(content, parent):
        result = []
        raw_items = Service.get_items_where_href_contains_markers(content, '_file_')
        for element in Service.remove_duplicates_and_clear(raw_items):
            result.append(File.create(element, parent))
        return result


class Video(Downloadable):

    @staticmethod
    def create(element, parent):
        name = element.attrs['src'].split('/')[5].split('?')[0]
        return Video(name,
                     element.attrs['src'],
                     parent)

    @staticmethod
    def extract_from_page(content, parent):
        result = []
        raw_items = Service.get_items_where_src_contains_markers(content, '.mp4', 'webm')
        for element in Service.remove_duplicates_and_clear(raw_items):
            result.append(Video.create(element, parent))
        return result

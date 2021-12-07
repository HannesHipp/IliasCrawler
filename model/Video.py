from model.Element import Element
from model.Downloadable import Downloadable
import model.Service as Service

class Video(Downloadable):

    @staticmethod
    def create(element, parent):
        name = element.attrs['src'].split('/')[5].split('?')[0]
        url = element.attrs['src']
        url = Element.correct_url(url)
        return Video(name,
                     url,
                     parent)

    @staticmethod
    def extract_from_page(content, parent):
        result = []
        raw_items = Service.get_items_where_src_contains_markers(
            content, '.mp4', 'webm')
        for element in Service.remove_duplicates_and_clear(raw_items):
            result.append(Video.create(element, parent))
        return result

    def get_hash(self):
        return self.url.split("/")[6]
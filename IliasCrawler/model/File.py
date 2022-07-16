from IliasCrawler.model.Downloadable import Downloadable
import re
from IliasCrawler.model.Element import Element
from IliasCrawler.Exceptions import NoNameException

pattern = re.compile(r"\.[a-z0-9]{1,4}")

class File(Downloadable):

    url_markers = ['_file_']

    @staticmethod
    def create(name, url, parent):
        return File(name,
                    url,
                    parent)

    def get_hash(self):
        return self.url.split("_file_")[1][:7]

    @staticmethod
    def get_name(bs4_element):
        name = Element.get_name(bs4_element)
        try:
            extension = pattern.search(name)[0][1:]
            name = pattern.split(name)[0]
        except:
            try:
                extension = bs4_element.parent.parent.parent.find(class_="il_ItemProperty").text.replace(
                    "\n", "").replace("\t", "").replace("\xa0", "")
            except AttributeError:
                raise NoNameException
        return f"{name}.{extension}"

    @staticmethod
    def is_valid(bs4_element):
        pass

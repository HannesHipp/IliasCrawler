from service.Database import Database
from service.Exceptions import NoNameException, NoUrlException


class Element:

    url_prefixes = {'ilias.php?': 'https://ilias3.uni-stuttgart.de/',
                    'Uni_Stuttgart/mobs/': 'https://ilias3.uni-stuttgart.de/'}

    def __init__(self, name, url, parent):
        self.__set_name(name)
        self.__set_url(url)
        self.parent = parent

    def __set_name(self, name):
        for char in ['/', '\\', ':', '*', '?', '"', '<', '>', '|', '...']:
            name = " ".join(name.split(char))
        self.name = " ".join(name.split())

    def __set_url(self, url):
        if 'http' not in url:
            url_needs_correction = True
            for key in type(self).url_prefixes.keys():
                if url_needs_correction:
                    if key in url:
                        if url[:2] == "./":
                            url = url[2:]
                        url = type(self).url_prefixes[key] + url
                        url_needs_correction = False
            if url_needs_correction:
                raise Exception(
                    f"Url does not match prefixes. type = {str(type(self))} url = {url}")
        self.url = url

    def get_path(self):
        if self.parent is None:
            return Database.get_instance("userdata").get_all()[0][2]
        else:
            parentpath = self.parent.get_path()
            return parentpath + "\\" + self.parent.name

    @staticmethod
    def get_name(bs4_element):
        try:
            name = bs4_element.text
            if name.strip():
                return name
            else:
                raise NoNameException
        except (KeyError, AttributeError):
            raise NoNameException

    @staticmethod
    def get_url(bs4_element):
        try:
            return bs4_element.attrs['href']
        except (KeyError, AttributeError):
            raise NoUrlException

    @staticmethod
    def get_raw_elements(page):
        return page.content.findAll('a')


import UserData
import hashlib


class Element:

    def __init__(self, name, url, parent):
        self.name = Element.__clear_name(name)
        self.url = Element.__correct_url(url)
        self.parent = parent
        # print(self.name + ' | ' + self.url)

    def get_path(self):
        if self.parent is None:
            return ""
        else:
            result = self.parent.name
            pointer = self.parent
            while pointer.parent is not None:
                pointer = pointer.parent
                result = pointer.name + "\\" + result
            result = UserData.getSpeicherpfad() + "\\" + result
        return result

    @staticmethod
    def __clear_name(name):
        for char in [' ', '/', '\\', ':', '*', '?', '"', '<', '>', '|', '...']:
            name = "".join(name.split(char))
        name = "".join(name.split())
        if len(name) > 100:
            name = name[:45] + '___' + name[-45:]
        return name

    @staticmethod
    def __correct_url(url):
        if 'https://ilias3.uni-stuttgart.de/' not in url:
            if url[:2] == "./":
                url = url[2:]
            url = 'https://ilias3.uni-stuttgart.de/' + url
        return url

    @staticmethod
    def extract_from_page(content, parent):
        raise Exception("Page extraction method not implemented.")

    def element_hash(self):
        result = int(hashlib.sha1(self.name.encode("utf-8")).hexdigest(), 16) % (10 ** 4)
        if self.parent is not None:
            result = result * self.parent.element_hash()
        return result


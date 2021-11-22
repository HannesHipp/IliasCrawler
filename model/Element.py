from service.Database import Database


class Element:

    def __init__(self, name, url, parent):
        self.name = Element.__clear_name(name)
        self.url = Element.__correct_url(url)
        self.parent = parent
        # print(self.name + ' | ' + self.url)

    def get_path(self):
        if self.parent is None:
            return Database.get_instance("userdata").get_all()[0][2]
        else:
            parentpath = self.parent.get_path()
            return parentpath + "\\" + self.parent.name

    @staticmethod
    def __clear_name(name):
        for char in ['/', '\\', ':', '*', '?', '"', '<', '>', '|', '...']:
            name = " ".join(name.split(char))
        return " ".join(name.split())

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

    def get_hash(self):
        result = self.name + self.parent.name + self.parent.parent.name
        return str(result)


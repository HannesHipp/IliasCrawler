from service.Exceptions import DoesNotContainNecessaryAttributesException


class Element:

    url_prefixes = {'ilias.php?': 'https://ilias3.uni-stuttgart.de/',
                    'Uni_Stuttgart/mobs/': 'https://ilias3.uni-stuttgart.de/'}

    def __init__(self, **parameters):
        if 'name' in list(parameters.keys()):
            name = parameters['name']
            url = parameters['url']
            parent = parameters['parent']
            if parent is not None:
                parent.children.append(self)
        else:
            name = self.get_name(parameters['bs4_element'])
            url = self.get_url(parameters['bs4_element'])
            parent = parameters['parent']
            parent.children.append(self)
        if not name.strip() and url.strip():
            raise DoesNotContainNecessaryAttributesException 
        self.name = self.filter_name(name)
        self.url = self.filter_url(url)
        self.parent = parent

    def get_path(self):
        if self.parent is None:
            return "C:\\Users\\Hannes\\Desktop"
        else:
            parentpath = self.parent.get_path()
            return parentpath + "\\" + self.parent.name

    def filter_name(self, name):
        for char in ['/', '\\', ':', '*', '?', '"', '<', '>', '|', '...']:
            name = " ".join(name.split(char))
        return " ".join(name.split())

    def filter_url(self, url):
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
        return url

    def get_name(self, bs4_element):
        return type(self).extractor.extract_name_from(bs4_element)

    def get_url(self, bs4_element):
        return type(self).extractor.extract_url_from(bs4_element)
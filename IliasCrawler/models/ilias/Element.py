class Element:

    def __init__(self, type, name, parent, treeImportance, url, urlFormat):
        self.type = type
        self.name = self.postprocessName(name)
        self.parent = parent
        self.treeImportance = treeImportance
        if url:
            url = self.postprocessURL(url, urlFormat, type)
        self.url = url

    def postprocessName(self, name):
        for char in ['/', '\\', ':', '*', '?', '"', '<', '>', '|', '...']:
            name = " ".join(name.split(char))
        return " ".join(name.split())

    def postprocessURL(self, url, urlFormat):
        if 'http' not in url:
            url_needs_correction = True
            for key in urlFormat:
                if url_needs_correction:
                    if key in url:
                        if url[:2] == "./":
                            url = url[2:]
                        url = urlFormat[key] + url
                        url_needs_correction = False
            if url_needs_correction:
                raise Exception(
                    f"Url does not match prefixes. type = {self.type} url = {url}")
        return url

    def get_path(self):
        if self.parent is None:
            return ""
        else:
            parentpath = self.parent.get_path()
            return parentpath + "\\" + self.parent.name


def convertDictToElementTree(dataList: list[dict], parent):
    endPoints = []
    for dict in dataList:
        element = Element(dict['type'], dict['name'], parent, dict['tree-importance'], dict.get(
            'url', None), dict.get('urlFormat', None))
        if len(dict['children']) != 0:
            for child in dict['children']:
                endPoints.extend(convertDictToElementTree(child, element))
        else:
            endPoints.extend(element)
    return endPoints

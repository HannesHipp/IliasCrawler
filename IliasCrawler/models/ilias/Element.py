from IliasCrawler.models.Extractor import Element





class IliasElement(Element):

    def __init__(self, type: str, parent) -> None:
        super().__init__(type, parent)

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

from IliasCrawler.model.Element import Element
import os
from IliasCrawler.Session import Session


class Downloadable(Element):

    def download(self, systemPath):
        path = self.getPath()
        if not os.path.isdir(path):
            os.makedirs(path)
        with open(path + "\\" + self.name, 'wb') as file:
            file.write(Session.get().get_file_content(self.url))
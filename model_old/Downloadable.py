from model.Element import Element
import os
from service.BusinessModel import BusinessModel
from service.Session import Session


class Downloadable(Element):

    def download(self):
        path = self.get_path()
        if not os.path.isdir(path):
            os.makedirs(path)
        with open(path + "\\" + self.name, 'wb') as file:
            file.write(BusinessModel.instance.session.get_file_content(self.url))
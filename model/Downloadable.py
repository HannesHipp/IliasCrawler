import os
from model.Element import Element


class Downloadable(Element):

    def __init__(self, **parameters):
        super().__init__(**parameters)
        self.file_extension = ""

    def download(self):
        path = self.get_path()
        if not os.path.isdir(path):
            os.makedirs(path)
        # with open(path + "\\" + self.name, 'wb') as file:
            # file.write(session.get_file_content(self.url))
        with open(f"{path}\\{self.name}.{self.file_extension}", 'w') as file:
            file.write("Hello")
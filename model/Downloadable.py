import Element
import os
import pickle

class Downloadable(Element):

    def download(self, session):
        path = self.get_path()
        if not os.path.isdir(path):
            os.makedirs(path)
        r = session.get(self.url)
        open(path + "\\" + self.name, 'wb').write(r.content)
        print("Downloaded to: " + path + "\\" + self.name)

    def write_to_log(self):
        with open('logdatei.txt', 'rb') as logdatei:
            downloaded = pickle.load(logdatei)
            downloaded.append(self.get_path())
            with open('logdatei.txt', 'wb') as logdatei:
                pickle.dump(downloaded, logdatei)
                print('Geloggt')


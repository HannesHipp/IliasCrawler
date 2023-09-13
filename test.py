import os
from IliasCrawler.Session import Session
from IliasCrawler.models.Extractor import Extractor, Element



def crawl(page, extractor):
    result = []
    page.set_soup(Session.get_content(page.url))
    leafs = extractor.extract_data(page)
    for leaf in leafs:
        if extractor.model[leaf.type]['childTypes']:
            print(f"crawling {leaf.name}")
            result.extend(crawl(leaf, extractor))
        else:
            result.append(leaf)
    return result


def postprocess_names(leafs):
    for leaf in leafs:
        current = leaf
        while current.parent is not None:
            current.name = postprocess_str(current.name)
            current = current.parent
    return leafs


def postprocess_str(str):
    for char in ['/', '\\', ':', '*', '?', '"', '<', '>', '|', '...']:
        str = " ".join(str.split(char))
    return " ".join(str.split())


def download(leaf, dir):
    path = get_path(leaf)
    path = f"{dir}\\{path}"
    if not os.path.isdir(path):
        os.makedirs(path)
    # with open(path + "\\" + self.name, 'wb') as file:
        # file.write(session.get_file_content(self.url))
    with open(f"{path}\\{leaf.name}.txt", 'w') as file:
        file.write("Hello")


def get_path(leaf):
    if leaf.parent is None:
            return ""
    else:
        parentpath = get_path(leaf.parent)
        return parentpath + "\\" + leaf.parent.name

DOWNLOAD_DIR = "C:\\Users\\hanne\\Desktop\\test"
Session.set_session('st162876', '90.0kg@Sommer')
print("has session")
extractor = Extractor('IliasCrawler\models\ilias\model.json')
print("extraction start")
root = Element('root', None)
root.name = "Ilias"
root.url = 'https://ilias3.uni-stuttgart.de/ilias.php?baseClass=ilDashboardGUI&cmd=jumpToSelectedItems'
leafs = crawl(root, extractor)
print("extraction finished")
leafs = postprocess_names(leafs)
print("postprocessing done")
for leaf in leafs:
    download(leaf, DOWNLOAD_DIR)


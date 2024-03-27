import os
from IliasCrawler.Session import Session
from IliasCrawler.models.extractor.Extractor import Extractor, Element



def crawl(page, extractor):
    result = []
    if 'http' not in page.url:
        print(f"page_type: {page.type.name}")
        print(f"url: {page.url}")
        print("")
        return []
    page.set_soup(Session.get_content(page.url))
    pages = extractor.extract_data(page)
    for page in pages:
        if page.type.child_types:
            print(f"crawling {page.name}")
            result.extend(crawl(page, extractor))
        else:
            result.append(page)
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

def postprocess_url(page):
    url = page.url
    url_format = page.url_format
    if 'http' not in url:
        url_needs_correction = True
        for key in url_format:
            if url_needs_correction:
                if key in url:
                    if url[:2] == "./":
                        url = url[2:]
                    url = url_format[key] + url
                    url_needs_correction = False
        if url_needs_correction:
            raise Exception(
                f"Url does not match prefixes. type = {page.type.name} url = {url}")
    return url

def download(leaf, dir):
    path = get_path(leaf)
    path = f"{dir}\\{path}"
    if not os.path.isdir(path):
        os.makedirs(path)
    # with open(path + "\\" + self.name, 'wb') as file:
        # file.write(session.get_file_content(self.url))
    with open(f"{path}\\{leaf.name}.txt", 'w') as file:
        file.write(leaf.url)

def get_path(leaf):
    if leaf.parent is None:
            return ""
    else:
        parentpath = get_path(leaf.parent)
        return parentpath + "\\" + leaf.parent.name

DOWNLOAD_DIR = "C:\\Users\\hanne\\Desktop\\test"
COURSE_NO = "2093098"

valid = Session.set_session('st162876', '90.0kg@Sommer')
print(f"Session valid: {valid}")
extractor = Extractor('IliasCrawler\\models\\ilias')
print("extraction start")
root = Element(extractor.root_type, None)
root.name = "Ilias"
root.set_soup(Session.get_content('https://ilias3.uni-stuttgart.de/ilias.php?baseClass=ilDashboardGUI&cmd=jumpToSelectedItems'))
courses = extractor.extract_data(root)
course = [course for course in courses if COURSE_NO in course.url][0]
leafs = crawl(course, extractor)
print("extraction finished")
leafs = postprocess_names(leafs)
print("postprocessing done")
for leaf in leafs:
    download(leaf, DOWNLOAD_DIR)

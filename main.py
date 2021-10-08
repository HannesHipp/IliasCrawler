from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pickle
import os
import requests

# Selenium Code:
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(executable_path=PATH)

# Input-Variablen:
laufwerkbuchstabe = 'D:'

class Element:

    def __init__(self, name, url, parent):
        self.name = Element.clear_name(name)
        self.url = url
        self.parent = parent
        print(self.name)

    def get_path(self):
        if self.parent is None:
            return ""
        else:
            result = self.parent.name
            pointer = self.parent
            while pointer.parent is not None:
                pointer = pointer.parent
                result = pointer.name + "\\" + result
            result = laufwerkbuchstabe + "\\" + result
        return result

    @staticmethod
    def create(element, parent):
        pass

    @staticmethod
    def clear_name(name):
        for char in [' ', '/', '\\', ':', '*', '?', '"', '<', '>', '|', '...']:
            name = "".join(name.split(char))
        name = "".join(name.split())
        if len(name) > 100:
            name = name[:45] + '___' + name[-45:]
        return name


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


class File(Downloadable):

    @staticmethod
    def create(element, parent):
        name = element.get_attribute("textContent")
        if '.mp4' in name:
            name = name.split('.mp4')[0] + '.mp4'
        else:
            name = name + '.pdf'
        return File(name,
                    element.get_attribute("href"),
                    parent)


class Video(Downloadable):

    @staticmethod
    def create(element, parent):
        name = element.get_attribute("src")
        if '.webm' in name:
            name = name.split('.webm')[0].split('/')[-1] + '.webm'
        else:
            name = name.split('.mp4')[0].split('/')[-1] + '.mp4'
        return Video(name,
                     element.get_attribute("src"),
                     parent)


class Folder(Element):

    def get_files_and_videos(self):
        result = []
        file_items = remove_duplicates_and_clear(get_items_where_href_contains_markers('_file_'))
        for element in file_items:
            result.append(File.create(element, self))
        video_items = remove_duplicates_and_clear(get_items_where_src_contains_markers('.mp4',
                                                                                       '.webm'))
        for element in video_items:
            result.append(Video.create(element, self))
        return result

    def get_new_pages(self):
        result = []
        fold_elements = remove_duplicates_and_clear(get_items_where_href_contains_markers('_fold_',
                                                                                          '_crs_',
                                                                                          'Cmd=showSeries'))
        for element in fold_elements:
            result.append(Folder.create(element, self))
        lm_elements = remove_duplicates_and_clear(get_items_where_href_contains_markers('_lm_'))
        for element in lm_elements:
            result.append(Lm.create(element, self, 0))
        OPD_elements = remove_duplicates_and_clear(get_items_where_href_contains_markers('showEpisode'))
        for element in OPD_elements:
            result.append(OPD.create(element, self))
        MCH_elements = remove_duplicates_and_clear(get_items_where_href_contains_markers('MediaCastHandler'))
        for element in MCH_elements:
            result.append(MCH.create(element, self))
        return result

    @staticmethod
    def create(element, parent):
        return Folder(element.get_attribute("textContent"),
                      element.get_attribute("href"),
                      parent)


class Lm(Folder):

    def __init__(self, name, url, parent, number):
        super().__init__(name, url, parent)
        self.number = number

    @staticmethod
    def create(element, parent, number):
        if number == 0:
            return Lm(element.get_attribute("textContent"),
                      element.get_attribute("href"),
                      parent,
                      number)
        else:
            return Lm(str(number) + element.get_attribute("textContent"),
                      element.get_attribute("href"),
                      parent,
                      number)

    def get_new_pages(self):
        result = []
        try:
            element = driver.find_element_by_xpath("//*[@class='ilc_page_tnav_TopNavigation']//*[@class='ilc_page_rnavlink_RightNavigationLink']")
            if self.number == 0:
                result.append(Lm.create(element, self, self.number + 1))
            else:
                result.append(Lm.create(element, self.parent, self.number + 1))
        except:
            pass
        return result


class OPD(Folder):

    def get_files_and_videos(self):
        result = []
        found = False
        while not found:
            video_elements = remove_duplicates_and_clear(get_items_where_src_contains_markers('.mp4'))
            if len(video_elements) != 0:
                found = True
        for element in video_elements:
            if 'presenter' in element.get_attribute("id"):
                pass
            else:
                result.append(Video(self.name + '.mp4', element.get_attribute('src'), self))
        return result


    @staticmethod
    def create(element, parent):
        return OPD(element.get_attribute("textContent"),
                   element.get_attribute("href"),
                   parent)


class MCH(Folder):

    def get_new_pages(self):
        # damit Oberklassenmethode nicht aufgerufen wird
        return []


    @staticmethod
    def create(element, parent):
        return MCH(element.get_attribute("textContent"),
                   element.get_attribute("href"),
                   parent)


def get_items_where_href_contains_markers(*markers):
    result = []
    for marker in markers:
        result += driver.find_elements_by_xpath("//main//*[contains(@href,'" + marker + "')]")
    return result


def get_items_where_src_contains_markers(*markers):
    result = []
    for marker in markers:
        result += driver.find_elements_by_xpath("//main//*[contains(@src,'" + marker + "')]")
    return result


def login(username, password):
    driver.get(
        "https://ilias3.uni-stuttgart.de/login.php?target=root_1&client_id=Uni_Stuttgart&cmd=force_login&lang=de")
    klick = driver.find_element_by_name("username")
    klick.send_keys(username)
    klick = driver.find_element_by_name("password")
    klick.send_keys(password)
    klick.send_keys(Keys.RETURN)


def crawl(page):
    driver.get(page.url)
    files_and_videos = page.get_files_and_videos()
    new_pages = page.get_new_pages()
    if len(new_pages) == 1 and len(files_and_videos) == 0:
        new_pages[0].parent = page.parent
    if len(new_pages) == 0 and len(files_and_videos) == 1:
        files_and_videos[0].parent = page.parent
    for newPage in new_pages:
        files_and_videos += crawl(newPage)
    return files_and_videos


def remove_duplicates_and_clear(raw_list):
    # entfernt Duplicate und Elemente ohne Text
    result = {}
    for element in raw_list:
        if element.get_attribute("href") is not None:
            if element.get_attribute("href") not in result:
                if element.get_attribute("textContent") is not None:
                    if element.get_attribute("textContent").strip():
                        result[element.get_attribute("href")] = element
        elif element.get_attribute("src") not in result:
            result[element.get_attribute("src")] = element
    return list(result.values())


login("st162876", "76kg@Sommer")
ilias = Folder('Ilias',
               'https://ilias3.uni-stuttgart.de/ilias.php?cmd=show&cmdClass=ildashboardgui&cmdNode=9x&baseClass=ilDashboardGUI',
               None)
data = crawl(ilias)
if not os.path.isfile('logdatei.txt'):
    with open('logdatei.txt', 'wb') as logdatei:
        pickle.dump([],logdatei)
newitems = []
with open('logdatei.txt', 'rb') as logdatei:
    oldpaths = pickle.load(logdatei)
    for item in data:
        if item.get_path() not in oldpaths:
            newitems.append(item)
            print('Neue Datei: ' + item.name)
with requests.session() as s:
    # Vorgehensweise siehe https://pybit.es/articles/requests-session/
    url = 'https://ilias3.uni-stuttgart.de/ilias.php?lang=de&client_id=Uni_Stuttgart&cmd=post&cmdClass=ilstartupgui&cmdNode=123&baseClass=ilStartUpGUI&rtoken='
    r = s.post(url,
               data={
                   'username': 'st162876',
                   'password': '76kg@Sommer',
                   'cmd[doStandardAuthentication]': 'Anmelden'
               }
               )
    for item in newitems:
        try:
            item.download(s)
            item.write_to_log()
        except Exception as e:
            print("Fehler beim Download von: " + item.get_path() + "\\" + item.name + " " + e)

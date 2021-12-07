from service.Session import Session
from model.File import File as File
from model.Video import Video as Video
import model.Service as Service
from model.Element import Element as Element
from json import loads


class Folder(Element):

    def __init__(self, name, url, parent):
        super().__init__(name, url, parent)
        if 'https://ilias3.uni-stuttgart.de/' not in url:
            if url[:2] == "./":
                url = url[2:]
            url = 'https://ilias3.uni-stuttgart.de/' + url
        self.url = url
        self.content = None

    #get_files_and_videos and get_new_pages are polymophically overwritten in subclasses of Folder
    def get_files_and_videos(self):
        result = []
        result += File.extract_from_page(self.content, self)
        result += Video.extract_from_page(self.content, self)
        return result

    def get_new_pages(self):
        result = []
        result += Folder.extract_from_page(self.content, self)
        result += Lm.extract_from_page(self.content, self)
        result += OPD.extract_from_page(self.content, self)
        result += MCH.extract_from_page(self.content, self)
        return result

    @staticmethod
    def extract_from_page(content, parent):
        result = []
        raw_items = Service.get_items_where_href_contains_markers(content, '_fold_',
                                                                           '_crs_',
                                                                           'Cmd=showSeries')
        for element in Service.remove_duplicates_and_clear(raw_items):
            result.append(Folder.create(element, parent))
        return result

    @staticmethod
    def create(element, parent):
        url = element.attrs['href']
        url = Element.correct_url(url)
        return Folder(str(element.text),
                      url,
                      parent)


class Ilias(Folder):

    def get_new_pages(self):
        result = Course.extract_from_page(self.content, self)
        return result


class Course(Folder):

    @staticmethod
    def extract_from_page(content, parent):
        result = []
        raw_items = Service.get_items_where_href_contains_markers(content, '_crs_')
        for element in Service.remove_duplicates_and_clear(raw_items):
            result.append(Course.create(element, parent))
        return result

    def get_course_number(self):
        return self.url.split("crs_")[1].split(".html")[0]

    @staticmethod
    def create(element, parent):
        return Course(str(element.text),
                      element.attrs['href'],
                      parent)


class Lm(Folder):

    def __init__(self, name, url, parent, number):
        super().__init__(name, url, parent)
        self.number = number

    def get_new_pages(self):
        result = []
        try:
            element = self.content.find(class_='ilc_page_rnavlink_RightNavigationLink')
            if self.number == 0:
                result.append(Lm.create(element, self, self.number + 1))
            else:
                result.append(Lm.create(element, self.parent, self.number + 1))
        except:
            pass
        return result

    @staticmethod
    def extract_from_page(content, parent):
        result = []
        raw_items = Service.get_items_where_href_contains_markers(content, '_lm_')
        for element in Service.remove_duplicates_and_clear(raw_items):
            result.append(Lm.create(element, parent, 0))
        return result

    @staticmethod
    def create(element, parent, number):
        # print(element.attrs['href'])
        if number == 0:
            # Calculate first lm page to crawl
            url = "https://ilias3.uni-stuttgart.de/" \
                  "ilias.php?ref_id=" + element.attrs['href'].split("_")[4].split(".")[0] + \
                  "&obj_id=1&cmd=layout&cmdClass=illmpresentationgui&cmdNode=gw&baseClass=ilLMPresentationGUI"
            return Lm(str(element.text),
                      url,
                      parent,
                      number)
        else:
            return Lm(str(number) + str(element.text),
                      element.attrs['href'],
                      parent,
                      number)


class MCH(Folder):

    def get_new_pages(self):
        # damit Oberklassenmethode nicht aufgerufen wird
        return []

    @staticmethod
    def extract_from_page(content, parent):
        result = []
        raw_items = Service.get_items_where_href_contains_markers(content, 'MediaCastHandler')
        for element in Service.remove_duplicates_and_clear(raw_items):
            result.append(MCH.create(element, parent))
        return result

    @staticmethod
    def create(element, parent):
        return MCH(str(element.text),
                   element.attrs['href'],
                   parent)


class OPD(Folder):

    def get_files_and_videos(self):
        id = self.url.split("&id=")[1].split("&cmd")[0]
        id1 = id.split("/")[0]
        id2 = id.split("/")[1]
        json_url = f'https://ilias3.uni-stuttgart.de/Customizing/global/plugins/Services/Repository/RepositoryObject/Opencast/api.php/episode.json?id={id1}%2F{id2}'
        json = Session.get_file_content(json_url)
        url = loads(json)["search-results"]["result"]["mediapackage"]["media"]["track"][0]["url"]
        return [Video(f"{self.name}.mp4", url, self)]
    
    def get_new_pages(self):
        return []

    @staticmethod
    def extract_from_page(content, parent):
        result = []
        raw_items = Service.get_items_where_href_contains_markers(content, 'showEpisode')
        for element in Service.remove_duplicates_and_clear(raw_items):
            result.append(OPD.create(element, parent))
        return result

    @staticmethod
    def create(element, parent):
        url = element.attrs['href']
        url = Element.correct_url(url)
        return OPD(str(element.text),
                   url,
                   parent)


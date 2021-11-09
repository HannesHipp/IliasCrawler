from service.Session import Session
from model.Files import File as File
from model.Files import Video as Video
import model.Service as Service
from model.Element import Element as Element


class Folder(Element):

    def __init__(self, name, url, parent):
        super().__init__(name, url, parent)
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
        return Folder(str(element.text),
                      element.attrs['href'],
                      parent)


class Root(Folder):

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
        result = []
        # found = False
        # while not found:
        #     video_elements = remove_duplicates_and_clear(self.get_items_where_src_contains_markers('.mp4'))
        #     if len(video_elements) != 0:
        #         found = True
        # for element in video_elements:
        #     if 'presenter' in element.get_attribute("key"):
        #         pass
        #     else:
        #         result.append(Video(self.name + '.mp4', element.get_attribute('src'), self))
        return result

    @staticmethod
    def extract_from_page(content, parent):
        result = []
        raw_items = Service.get_items_where_href_contains_markers(content, 'showEpisode')
        for element in Service.remove_duplicates_and_clear(raw_items):
            result.append(OPD.create(element, parent))
        return result

    @staticmethod
    def create(element, parent):
        return OPD(str(element.text),
                   element.attrs['href'],
                   parent)


import Element
import File
import Video
import Lm
import OPD
import MCH

class Folder(Element):

    def __init__(self, name, url, parent):
        super().__init__(name, url, parent)
        self.content = None

    def get_files_and_videos(self):
        result = []
        result += File.extract_from_page()
        result += Video.extract_files()
        return result

    def get_new_pages(self):
        result = []
        result += Folder
        result += self.get_lm_folders()
        result += self.get_opd_folders()
        result += self.get_mch_folders()
        return result

    def get_files(self):
        result = []
        raw_items = self.get_items_where_href_contains_markers('_file_')
        for element in Folder.remove_duplicates_and_clear(raw_items):
            result.append(File.File.create(element, self))
        return result

    def get_videos(self):
        result = []
        raw_items = self.get_items_where_href_contains_markers('.mp4',
                                                               '.webm')
        for element in Folder.remove_duplicates_and_clear(raw_items):
            result.append(Video.Video.create(element, self))
        return result

    def get_folders(self):
        result = []
        raw_items = self.get_items_where_href_contains_markers('_fold_',
                                                               '_crs_',
                                                               'Cmd=showSeries')
        for element in Folder.remove_duplicates_and_clear(raw_items):
            result.append(Folder.create(element, self))
        return result

    def get_lm_folders(self):
        result = []
        raw_items = self.get_items_where_href_contains_markers('_lm_')
        for element in Folder.remove_duplicates_and_clear(raw_items):
            result.append(Lm.Lm.create(element, self, 0))
        return result

    def get_opd_folders(self):
        result = []
        raw_items = self.get_items_where_href_contains_markers('showEpisode')
        for element in Folder.remove_duplicates_and_clear(raw_items):
            result.append(OPD.OPD.create(element, self))
        return result

    def get_mch_folders(self):
        result = []
        raw_items = self.get_items_where_href_contains_markers('MediaCastHandler')
        for element in Folder.remove_duplicates_and_clear(raw_items):
            result.append(MCH.MCH.create(element, self))
        return result

    def get_items_where_href_contains_markers(self, *markers):
        result = []
        all_a_elements = self.content.findAll('a')
        for a_element in all_a_elements:
            try:
                if any(x in a_element.attrs['href'] for x in markers):
                    result.append(a_element)
            except KeyError:
                pass
        return result

    def get_items_where_src_contains_markers(self, *markers):
        result = []
        all_video_elements = self.content.findAll('source')
        for video_element in all_video_elements:
            try:
                if any(x in video_element.attrs['src'] for x in markers):
                    video_element.attrs['src'] = 'https://ilias3.uni-stuttgart.de' + video_element.attrs['src'][1:]
                    result.append(video_element)
            except KeyError:
                pass
        return result

    @staticmethod
    def remove_duplicates_and_clear(raw_list):
        # entfernt Duplicate und Elemente ohne Text
        result = {}
        for element in raw_list:
            try:
                if element.attrs['href'] not in result:
                    if str(element.text) is not None:
                        if str(element.text).strip():
                            result[element.attrs['href']] = element
            except KeyError:
                if element.attrs['src'] not in result:
                    result[element.attrs['src']] = element
        return list(result.values())

    @staticmethod
    def create(element, parent):
        return Folder(str(element.text),
                      element['href'],
                      parent)
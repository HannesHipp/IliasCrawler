import Folder

class OPD(Folder):

    def get_files_and_videos(self):
        result = []
        # found = False
        # while not found:
        #     video_elements = remove_duplicates_and_clear(self.get_items_where_src_contains_markers('.mp4'))
        #     if len(video_elements) != 0:
        #         found = True
        # for element in video_elements:
        #     if 'presenter' in element.get_attribute("id"):
        #         pass
        #     else:
        #         result.append(Video(self.name + '.mp4', element.get_attribute('src'), self))
        return result

    @staticmethod
    def create(element, parent):
        url = element['href']
        content = BeautifulSoup(session.get(url).text, 'lxml')
        return OPD(str(element.text),
                   element['href'],
                   parent,
                   content)
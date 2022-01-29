class Extractor():

    def __init__(self, *markers):
        self.markers = markers


class HrefExtractor(Extractor):

    def extract_raw_bs4_elements(self, content):
        result = []
        all_a = content.findAll('a')
        for a in all_a:
            try:
                if any(x in a.attrs['href'] for x in self.markers):   
                    result.append(a)
            except (KeyError, AttributeError):
                pass
        return result


class ClassExtractor(Extractor):
    
    pass


# --------------------------------------------------

class Element:

    def __init__(self, name, url, parent):
        self.name = name
        self.url = url
        self.parent = parent

    def get_path(self):
        if self.parent is None:
            return ""
        else:
            parentpath = self.parent.get_path()
            return parentpath + "\\" + self.parent.name

    @staticmethod
    def get_name(bs4_element):
        try:
            name = bs4_element.text
            if name.strip():
                return name
        except (KeyError, AttributeError):
            pass
        return None

    @staticmethod
    def get_url(bs4_element):
        try:
            return bs4_element.attrs['href']
        except (KeyError, AttributeError):
            pass
        return None


class Container(Element):
    pass



class Downloadable(Element):
    pass



class Page(Container):

    def __init__(self, name, url, parent):
        super().__init__(name, url, parent)
        self.content = None
    
    def get_files_and_videos(self):
        return self.extract_types(type(self).downloadable_types)

    def get_new_pages(self):
        return self.extract_types(type(self).get_sub_page_types())

    def extract_types(self, types):
        result = []
        for type_ in types:
            unfiltered_bs4_elements = type_.extractor.extract_raw_bs4_items(type_, self.content)
            for bs4_element in unfiltered_bs4_elements:
                name = type_.get_name_from_bs4(bs4_element)
                url = type_.get_url_from_bs4(bs4_element)
                parent = self.contruct_parent_structure(bs4_element)
                if name and url and parent:
                    result.append(type_.create(name, url, parent))
        return result

    def construct_parent_structure(self, bs4_element):
        # on_page_container_types = type(self).on_page_container_types
        # parent
        # while parent
        pass

class OnPageContainer(Container):
    pass


#---------------------------------------------------

class IlContainerBlock(OnPageContainer):
    
    pass

class File(Downloadable):
    
    extractor = HrefExtractor('_file_')


class Video(Downloadable):
    
    extractor = HrefExtractor('.mp4', 'webm')


class Lm(Page):
    
    extractor = HrefExtractor('_lm_')
    on_page_container_types = []
    downloadable_types = [File, Video]

    @staticmethod
    def sub_page_types():
        return [Lm]

class Course(Page):
    
    extractor = HrefExtractor('_crs_')
    on_page_container_types = [IlContainerBlock]
    downloadable_types = [File, Video]

    @staticmethod
    def sub_page_types():
        return [Lm]
# -------------------------------------------------

def crawl(page):
    files_and_videos = page.get_files_and_videos()
    new_pages = page.get_new_pages()
    for new_page in new_pages:
        files_and_videos += crawl(new_page)
    return files_and_videos

from model.Ilias import Ilias
from PyQt5.QtCore import pyqtSignal, QObject, QThread


class Crawler(QObject):

    signal_send_crawl_information = pyqtSignal(int, int, int, int)

    def __init__(self, session, fresh_courses) -> None:
        super().__init__()
        self.session = session
        self.fresh_courses = fresh_courses
        self.total_courses_to_be_crawled = 0
        self.courses_crawled = 0
        self.files_crawled = 0
        self.pages_crawled = 0

    def get_files_to_download(self):
        print(F"Crawler: {QThread.currentThread()}")
        result = []
        courses_to_be_crawled = [course for course in self.fresh_courses if course.should_be_downloaded]
        self.total_courses_to_be_crawled = len(courses_to_be_crawled)
        for course in courses_to_be_crawled:
            result += self.crawl(course)
            self.courses_crawled += 1
            self.signal_send_crawl_information.emit(
                self.total_courses_to_be_crawled, 
                self.courses_crawled,
                self.files_crawled,
                self.pages_crawled
            )
        result = Crawler.postprocess_data(result)
        return result

    def crawl(self, page):
        page.set_content()
        files_and_videos = page.get_files_and_videos()
        new_pages = page.get_new_pages()
        self.files_crawled += len(files_and_videos)
        self.pages_crawled += len(new_pages)
        self.signal_send_crawl_information.emit(
            self.total_courses_to_be_crawled, 
            self.courses_crawled,
            self.files_crawled,
            self.pages_crawled
        )
        page.content = None
        for new_page in new_pages:
            files_and_videos += self.crawl(new_page)
        return files_and_videos

    @staticmethod
    def postprocess_data(data):
        data = Crawler.clean_tree(data)
        data = Crawler.shorten_long_item_paths(data)
        return data

    @staticmethod
    def clean_tree(downloadables):
        for downloadable in downloadables:
            current = downloadable.parent
            while current.parent is not None:
                if len(current.children) == 1:
                    item_to_delete = Crawler.decide_which_item_to_delete(current)
                    Crawler.delete_item_from_tree(item_to_delete)
                current = current.parent
        return downloadables

    @staticmethod
    def decide_which_item_to_delete(current):
        if type(current).tree_importance < type(current.children[0]).tree_importance:
            return current.children[0]
        else:
            return current

    @staticmethod
    def delete_item_from_tree(item):
        # tree_importance
        # 0 = necessary, don't delete
        # 1, 2, 3, ... = not necessary, delete if appropriate
        if type(item).tree_importance != 0:
            for child in item.children:
                child.parent = item.parent
                item.parent.children.append(child)
            item.parent.children.remove(item)

    @staticmethod
    def shorten_long_item_paths(data):
        windows_max_path_length = 248
        for item in data:
            item_path = f"{item.get_path()}\\{item.name}.{item.file_extension}"
            if len(item_path) > windows_max_path_length:
                component_dict = Crawler.get_component_dict(item)
                number_of_components = len(component_dict)
                number_of_separators = number_of_components - 1
                file_extension_length = len(item.file_extension) + 1
                userpath_plus_ilias_length = len(item_path.split('\\Ilias\\')[0] + "\\Ilias\\")
                available_string_length = windows_max_path_length - file_extension_length - userpath_plus_ilias_length - number_of_separators
                for component_name in component_dict:
                    allowed_component_length = int(available_string_length/number_of_components)
                    if (len(component_name) - allowed_component_length) > 0:
                        number = int(allowed_component_length / 2) - 1
                        name = f"{component_name[:number]}_{component_name[-number:]}"
                        component_dict[component_name].name = name
                    else:
                        name = component_name
                    available_string_length = available_string_length - len(name)
                    number_of_components = number_of_components - 1
        return data

    @staticmethod
    def get_component_dict(item):
        d = {}
        while type(item) is not Ilias:
            d[item.name] = item
            item = item.parent
        result = {}
        for k in sorted(d, key=len, reverse=False):
            result[k] = d[k]
        return result
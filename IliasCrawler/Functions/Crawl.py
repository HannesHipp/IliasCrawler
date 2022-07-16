import time
from Framework.Function import Function
from IliasCrawler.Session import Session
from IliasCrawler.model.File import File


class Crawl(Function):

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.courses = kwargs['courses']
        self.path = kwargs['path']

    def execute(self, progress_signal):
        result = []
        coursesCrawled = 0
        for course in self.courses.value:
            if course.shouldBeDownloaded:
                progress_signal.emit((coursesCrawled, course.name))
                result += self.crawl(course)
                coursesCrawled += 1
        result = self.detect_items_with_long_path(result)
        return result

    def updateFrame(self, tuple):
        coursesCrawled = tuple[0]
        currentCourseName = tuple[1]
        percentage_of_courses_crawled = int((coursesCrawled/len(self.courses.value))*100)
        self.frame.progress_bar.setValue(percentage_of_courses_crawled)
        self.frame.progress_bar_label.setText(f"{currentCourseName} wird gerade durchsucht...")


    def crawl(self, page):
        page.content = Session.get_content(page.url)
        files_and_videos = page.get_files_and_videos()
        new_pages = page.get_new_pages()
        page.content = None
        if len(new_pages) == 1 and len(files_and_videos) == 0:
            new_pages[0].name = page.name
            new_pages[0].parent = page.parent
        if len(new_pages) == 0 and len(files_and_videos) == 1:
            files_and_videos[0].parent = page.parent
        for new_page in new_pages:
            files_and_videos += self.crawl(new_page)
        return files_and_videos

    def detect_items_with_long_path(self, data):
        file_ex_length = 5
        userpath_plus_ilias_length = len(self.path.value + "\\Ilias\\")
        available_string_length = 256 - userpath_plus_ilias_length - file_ex_length
        for item in data:
            removal_path = (item.get_path() + "\\" + item.name).split("\\Ilias\\")[1]
            number_of_chars_to_remove = len(removal_path) - available_string_length
            too_long = number_of_chars_to_remove > 0
            if too_long:
                removal_positions = self.get_removal_positions(removal_path)
                self.correct_path(item, removal_positions, number_of_chars_to_remove)
        return data

    def get_removal_positions(self, removal_path):
        result = []
        positions_list = removal_path.split("\\")
        avrg_chars_per_position = int(len(removal_path)/len(positions_list))
        for position in positions_list:
            if len(position) > avrg_chars_per_position:
                result.append(position)
        return result

    def correct_path(self, item, removal_positions, total_number_of_chars_to_remove):
        if any(x == item.name for x in removal_positions):
            number_of_chars_to_remove = int(total_number_of_chars_to_remove/len(removal_positions))
            length = int((len(item.name) - number_of_chars_to_remove - 1)/2)
            item.name = item.name[:length] + '_' + item.name[-length:]
        if item.parent is not None:
            self.correct_path(item.parent, removal_positions, total_number_of_chars_to_remove)
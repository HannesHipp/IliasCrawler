import time
from Framework.Datapoint import Datapoint
from Framework.Function import Function
from IliasCrawler.Datapoints.Courses import Courses
from IliasCrawler.Datapoints.FilesAndVideos import FilesAndVideos, get_file_hash, get_video_hash
from IliasCrawler.Functions.Download import filter_url
from IliasCrawler.Session import Session
from IliasCrawler.models.extractor.Extractor import Extractor


class Crawl(Function):

    def __init__(
            self, 
            courses: Courses, 
            files_and_videos: FilesAndVideos, 
            current_course_name: Datapoint,
            percentage_crawled: Datapoint
        ) -> None:
        super().__init__()
        self.courses = courses
        self.files_and_videos = files_and_videos
        self.current_courses_name = current_course_name
        self.percentage_crawled = percentage_crawled

    def execute(self):
        files_and_videos = []
        extractor = Extractor('IliasCrawler\\models\\ilias')
        to_crawl = [course for course in self.courses.value if course.to_download]
        crawled = 0
        for course in to_crawl:
            self.current_courses_name.submit_value(course.name)
            files_and_videos += self.crawl(course.element, extractor)
            crawled += 1
            self.percentage_crawled.submit_value(
                int(crawled/len(to_crawl)*100)
            )
        result = []
        existing_files_and_videos = self.files_and_videos.value
        for element in files_and_videos:
            if element.type.name == 'file':
                if not get_file_hash(element) in existing_files_and_videos['files']:
                    result.append(element)
            elif element.type.name == 'video':
                if not get_video_hash(element) in existing_files_and_videos['videos']:
                    result.append(element)
        self.files_and_videos.submit_value(result)
    
    def crawl(self, page, extractor):
        result = []
        page.set_soup(Session.get_content(filter_url(page)))
        pages = extractor.extract_data(page)
        for page in pages:
            if page.type.child_types:
                result.extend(self.crawl(page, extractor))
            else:
                result.append(page)
        return result
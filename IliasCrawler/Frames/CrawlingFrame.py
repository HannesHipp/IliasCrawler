from Framework.Datapoint import Datapoint
from Framework.GuiModuls.ProgressBar import ProgressBar
from Framework.GuiModuls.TextLabel import TextLabel
from Framework.OutputFrame import OutputFrame

from IliasCrawler.Datapoints.Courses import Courses
from IliasCrawler.Datapoints.FilesAndVideos import FilesAndVideos
from IliasCrawler.Functions.Crawl import Crawl


class CrawlingFrame(OutputFrame):

    def __init__(self, courses: Courses, files_and_videos: FilesAndVideos):
        current_course_name = Datapoint(save=False)
        percentage_crawled = Datapoint(save=False)
        function = Crawl(courses, files_and_videos, current_course_name, percentage_crawled)
        super().__init__(
            path="IliasCrawler\\resources\\CrawlingView.ui",
            function=function
        )
        self.courses = courses
        self.files_and_videos = files_and_videos
        self.add_module(
            ProgressBar(percentage_crawled, self.progress_bar, self.label_percentage)
        )
        self.add_module(
            TextLabel(current_course_name, self.label_current_course_name, lambda x: x)
        )

    def add_next_frames(self, downloading_frame):
        self.downloading_frame = downloading_frame

    def decide_next_frame(self, pressedButton):
        return self.downloading_frame

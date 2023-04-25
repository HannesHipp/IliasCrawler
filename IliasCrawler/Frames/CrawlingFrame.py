from Framework.Datapoint import Datapoint
from Framework.GuiModuls.ProgressBar import ProgressBar
from Framework.GuiModuls.TextLabel import TextLabel
from Framework.OutputFrame import OutputFrame

from IliasCrawler.Datapoints.Courses import Courses
from IliasCrawler.Datapoints.FilesAndVideos import FilesAndVideos

from IliasCrawler.Functions.Crawl import Crawl


class CrawlingFrame(OutputFrame):

    def __init__(self, courses: Courses, filesAndVideos: FilesAndVideos):
        currentCourseName = Datapoint(save=False)
        function = Crawl(courses, filesAndVideos, currentCourseName)
        super().__init__(
            path="IliasCrawler\\resources\\CrawlingView.ui",
            function=function
        )
        self.courses = courses
        self.filesAndVideos = filesAndVideos
        self.setGuiModuls(
            ProgressBar(courses, self.progress_bar,
                        self.label_percentage, percentageOfCrawledCourses),
            TextLabel(currentCourseName,
                      self.label_aktueller_kurs, lambda x: x)
        )

    def addNextFrames(self, crawlingFrame):
        self.crawlingFrame = crawlingFrame

    def decideNextFrame(self, pressedButton):
        return self.crawlingFrame


def percentageOfCrawledCourses(courses):
    coursesToCrawl = 0
    coursesCrawled = 0
    for course in courses:
        if course.shouldBeDownloaded:
            coursesToCrawl = coursesToCrawl + 1
        if course.hasBeenCrawled:
            coursesCrawled = coursesCrawled + 1
    if coursesToCrawl == 0:
        return 100
    return int(coursesCrawled/coursesToCrawl)

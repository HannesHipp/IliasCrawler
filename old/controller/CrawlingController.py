from controller.Frame import Frame
from PyQt5.QtCore import QThread


class CrawlingController(Frame):

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(CrawlingController, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self.ui_file_location = 'C:\\Users\\Hannes\\Code Projekte\\IliasCrawler\\IliasCrawler\\resources\\CrawlingView.ui'
        super().__init__()
        self.progress_bar.setValue(0)
        print(F"CrawlingController: {QThread.currentThread()}")

    def update_displayed_information(self, total_courses, courses_crawled, files_crawled, pages_crawled):
        print(F"Crawler: {QThread.currentThreadId()}")
        percentage_of_courses_crawled = int((courses_crawled/total_courses)*100)
        self.progress_bar.setValue(percentage_of_courses_crawled)
        self.progress_bar_label.setText(f"{pages_crawled} Ordner und {files_crawled} Dateien gefunden...")
        self.repaint()


    

        
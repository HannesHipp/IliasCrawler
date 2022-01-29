from PyQt5.QtCore import QObject, pyqtSignal

class Crawler(QObject):

    send_crawling_results = pyqtSignal(list)

    def crawl(self):
        result = []
        # bla bla
        self.send_crawling_results.emit(result)

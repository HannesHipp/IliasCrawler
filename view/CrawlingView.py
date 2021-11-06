import time

from service.EventsManagement import EventListener
import view.Service as Service
import sys


class CrawlingView(EventListener):

    __number_of_crawled_files = 0
    __number_of_crawled_folders = 0

    @staticmethod
    def show():
        print("Ilias wird durchsucht. Dies kann je nach Anzahl deiner Kurse ein bisschen dauern...")

    @staticmethod
    def update(number_of_files_and_folders):
        CrawlingView.__number_of_crawled_files += number_of_files_and_folders[0]
        CrawlingView.__number_of_crawled_folders += number_of_files_and_folders[1]
        sys.stdout.write("\r")
        sys.stdout.write("Es wurden bisher %s Dateien und %s Ordner gefunden." %
                         (CrawlingView.__number_of_crawled_files, CrawlingView.__number_of_crawled_folders))
        sys.stdout.flush()

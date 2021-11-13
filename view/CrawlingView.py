from service.EventsManagement import EventListener
from view import Service


class CrawlingView(EventListener):

    __number_of_crawled_files = 0
    __number_of_crawled_folders = 0

    @staticmethod
    def crawling_starts_promt():
        print("\nIlias wird nach neuen Dateien in deinen ausgewählten Kursen durchsucht. \n"
              "Dies kann je nach Anzahl deiner Kurse ein bisschen dauern...")

    @staticmethod
    def update(number_of_files_and_folders):
        CrawlingView.__number_of_crawled_files += number_of_files_and_folders[0]
        CrawlingView.__number_of_crawled_folders += number_of_files_and_folders[1]
        Service.write_with_carrige_return("Es wurden bisher %s Elemente und %s Ordner auf Ilias gefunden." %
                                          (CrawlingView.__number_of_crawled_files,
                                           CrawlingView.__number_of_crawled_folders))

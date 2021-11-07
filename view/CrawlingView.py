from service.EventsManagement import EventListener
import sys


class CrawlingView(EventListener):

    __number_of_crawled_files = 0
    __number_of_crawled_folders = 0

    @staticmethod
    def ask_for_crawl():
        while True:
            result = input("Möchtest du damit beginnen Ilias nach neuen Dateien zu durchsuchen? Gib 'j' für Ja und 'n' für Nein ein.")
            if result == "j":
                return True
            elif result == "n":
                return False
            else:
                print("Falsche Antwort. Probieren wir es noch einmal...")

    @staticmethod
    def crawling_starts_promt():
        print("Ilias wird durchsucht. Dies kann je nach Anzahl deiner Kurse ein bisschen dauern...")

    @staticmethod
    def update(number_of_files_and_folders):
        CrawlingView.__number_of_crawled_files += number_of_files_and_folders[0]
        CrawlingView.__number_of_crawled_folders += number_of_files_and_folders[1]
        sys.stdout.write("\r")
        sys.stdout.write("Es wurden bisher %s Dateien und %s Ordner gefunden." %
                         (CrawlingView.__number_of_crawled_files, CrawlingView.__number_of_crawled_folders))
        sys.stdout.flush()

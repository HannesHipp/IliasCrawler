from service.Database import Database, ItemAlreadyExists
from service.EventsManagement import EventsManager
from view.DownloadView import DownloadView


class DownloadController:

    @staticmethod
    def run(data):
        print("")
        # Comparison between hashes in database and data. New items are added to list 'newitems'
        newitems = []
        for item in data:
            hash = item.get_hash()
            if not Database.get_instance("files").key_exists(hash):
                newitems.append(item)

        DownloadView.show(newitems)

        # Downloading every element of 'newitems' and writing to database after download
        downloaded_already = 0
        errors = []
        for item in newitems:
            try:
                item.download()
                Database.get_instance("files").add(item.get_hash())
                downloaded_already += 1
                EventsManager.get_instance().notify_listeners("download", (downloaded_already, item.name))
            except Exception as e:
                if not Exception is ItemAlreadyExists:
                    errors.append(item.get_path() + "\\" + item.name + ", Grund: " + str(e))
        if len(errors) != 0:
            print("\nFolgende Dateien konnten nicht herruntergeladen werden:")
            for error in errors:
                print(error)

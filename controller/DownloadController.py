from service.Database import Database
from service.EventsManagement import EventsManager
from view.DownloadView import DownloadView


class DownloadController:

    @staticmethod
    def run(data):
        print("")
        # Comparison between paths in logdatei and data. New items are added to list 'newitems'
        newitems = []
        for item in data:
            hash = item.element_hash()
            if not Database.get_instance("files").key_exists(str(hash)):
                newitems.append(item)
                print('Neue Datei: ' + item.name)

        DownloadView.show(len(newitems))

        # Downloading every element of 'newitems' and writing to log after download
        downloaded_already = 0
        errors = []
        for item in newitems:
            try:
                item.download()
                downloaded_already += 1
                EventsManager.get_instance().notify_listeners("download", downloaded_already)
            except Exception as e:
                errors.append(item.get_path() + "\\" + item.name + " ," + str(e))
        if len(errors) != 0:
            print("\nFolgende Dateien konnten nicht herruntergeladen werden:")
            for error in errors:
                print(error)

from service.EventsManagement import EventListener
import view.Service as Service


class DownloadView(EventListener):

    __number_of_new_files = None

    @staticmethod
    def show(new_files):
        DownloadView.__number_of_new_files = len(new_files)
        if DownloadView.__number_of_new_files == 0:
            print("\nDeine Dateien sind bereits up-to-date.")
        else:
            print("\nDavon sind " + str(DownloadView.__number_of_new_files) + " Dateien noch nicht in deinem lokalen "
                  "Speicher. Diese Dateien werden jetzt herruntergeladen:")
        for file in new_files:
            print(file.name)

    @staticmethod
    def update(data):
        downloaded_already = data[0]
        file_name = data[1]
        percentage = downloaded_already / DownloadView.__number_of_new_files * 100
        Service.drawProgressBar(percentage, file_name)

    @staticmethod
    def new_files_promt():
        print("Davon befinden sich folgende Dateien noch nicht in ihrem lokalen Speicher:")

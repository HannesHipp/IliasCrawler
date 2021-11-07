from service.EventsManagement import EventListener
import view.Service as Service


class DownloadView(EventListener):

    __number_of_new_files = None

    @staticmethod
    def show(number_of_new_files):
        DownloadView.__number_of_new_files = number_of_new_files
        if number_of_new_files == 0:
            print("\nDeine Dateien sind bereits up-to-date.")
        else:
            print("\nEs wurden " + str(DownloadView.__number_of_new_files) + " neue Dateien gefunden. Diese werden jetzt "
                                                                           "herruntergeladen.")

    @staticmethod
    def update(downloaded_already):
        percentage = downloaded_already / DownloadView.__number_of_new_files * 100
        Service.drawProgressBar(percentage)

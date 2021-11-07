import pickle
import os
from service.Session import Session
from model.Folders import Folder as Folder
from service.EventsManagement import EventsManager
from view.CrawlingView import CrawlingView
from view.DownloadView import DownloadView
from view.SetupView import SetupView


def crawl(page):
    page.content = Session.get_content(page.url)
    files_and_videos = page.get_files_and_videos()
    new_pages = page.get_new_pages()
    EventsManager.get_instance().notify_listeners("crawl", (len(files_and_videos), len(new_pages)))
    if len(new_pages) == 1 and len(files_and_videos) == 0:
        new_pages[0].name = page.name
        new_pages[0].parent = page.parent
    if len(new_pages) == 0 and len(files_and_videos) == 1:
        files_and_videos[0].parent = page.parent
    for new_page in new_pages:
        files_and_videos += crawl(new_page)
    return files_and_videos


# Setting up Event Management
EventsManager.get_instance().attach_listener("download", DownloadView())
EventsManager.get_instance().attach_listener("crawl", CrawlingView())

# Starting folder of the crawling process
CrawlingView.crawling_starts_promt()

ilias = Folder('Ilias',
               'https://ilias3.uni-stuttgart.de/ilias.php?cmd=show&cmdClass=ildashboardgui&cmdNode=9x&baseClass=ilDashboardGUI',
               None)

# All found files and videos are saved in list-object 'data'
data = crawl(ilias)

# Creation of logdatei if logdatei does not exist
if not os.path.isfile('logdatei.txt'):
    with open('logdatei.txt', 'wb') as logdatei:
        pickle.dump([], logdatei)

# Comparison between paths in logdatei and data. New items are added to list 'newitems'
newitems = []
with open('logdatei.txt', 'rb') as logdatei:
    oldpaths = pickle.load(logdatei)
    for item in data:
        if item.get_path() not in oldpaths:
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
        errors.append(item.get_path() + "\\" + item.name + " " + e)
if len(errors) != 0:
    print("Folgende Dateien konnten nicht herruntergeladen werden:")
    for error in errors:
        print(error)
print("Programm beendet. Vielen Dank und bis bald :)")

import pickle
import os
from bs4 import BeautifulSoup
from Session import Session
from model.Folder import Folder

def crawl(page):
    page.content = Session.get_content()
    files_and_videos = page.get_files_and_videos()
    new_pages = page.get_new_pages()
    if len(new_pages) == 1 and len(files_and_videos) == 0:
        new_pages[0].parent = page.parent
    if len(new_pages) == 0 and len(files_and_videos) == 1:
        files_and_videos[0].parent = page.parent
    for new_page in new_pages:
        files_and_videos += crawl(new_page)
    return files_and_videos

Session()
ilias = Folder('Ilias',
               'https://ilias3.uni-stuttgart.de/ilias.php?cmd=show&cmdClass=ildashboardgui&cmdNode=9x&baseClass=ilDashboardGUI',
               None)
data = crawl(ilias)
if not os.path.isfile('logdatei.txt'):
    with open('logdatei.txt', 'wb') as logdatei:
        pickle.dump([],logdatei)
newitems = []
with open('logdatei.txt', 'rb') as logdatei:
    oldpaths = pickle.load(logdatei)
    for item in data:
        if item.get_path() not in oldpaths:
            newitems.append(item)
            print('Neue Datei: ' + item.name)
for item in newitems:
    try:
        item.download()
        item.write_to_log()
    except Exception as e:
        print("Fehler beim Download von: " + item.get_path() + "\\" + item.name + " " + e)
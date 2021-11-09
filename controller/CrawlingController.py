from service.Database import Database
from controller import Service
from model.Folders import Folder
from service.EventsManagement import EventsManager
from service.Session import Session
from view.CrawlingView import CrawlingView

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


class CrawlingController:

    @staticmethod
    def run(courses):
        CrawlingView.crawling_starts_promt()
        result = []
        for course in courses:
            if not Database.get_instance("course_exceptions").key_exists(course.get_course_number()):
                result += crawl(course)
        return result

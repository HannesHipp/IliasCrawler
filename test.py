# import pprint
# from bs4 import BeautifulSoup

# from IliasCrawler.models.Extractor import Extractor
# from IliasCrawler.models.ilias.Element import Element, convertDictToElementTree


# html_str = """<html><head><title>The Dormouse's story</title></head>
#     <body>
#     <p class="title"><b>The Dormouse's story</b></p>

#     <p class="story">Once upon a time there were three little sisters; and their names were
#     <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
#     <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
#     <a href="http://example.com/tillie" class="brother" id="link3">Tillie</a>;
#     and they lived at the bottom of a well.</p>

#     <p class="story">...</p>
#     """
# soup = BeautifulSoup(html_str, 'lxml')
# extractor = Extractor('test.json')
# root = Element('ilias', 'ilias', None, 0, None, None)
# pprint.pprint(convertDictToElementTree(extractor.start_extraction(soup), root))

def execute(self):
    COURSES_URL = 'https://ilias3.uni-stuttgart.de/ilias.php?baseClass=ilDashboardGUI&cmd=jumpToSelectedItems'
    Session(self.username.value, self.password.value)
    htmlSoup = Session.get_content(COURSES_URL)
    extractor = Extractor('IliasCrawler\models\ilias\model.json')
    data = extractor.start_extraction(htmlSoup)
    root = Element('Ilias', None, 0)
    convertDictToElementTree(data, root)
    if self.courses.value:
        hashToDownload = {
            course.getHash(): course.shouldBeDownloaded for course in self.courses.value}
    else:
        hashToDownload = {}
    allCourses = root.get_new_pages()
    for course in allCourses:
        hash = course.getHash()
        shouldBeDownloaded = False
        if hash in hashToDownload:
            course.isNew = False
            if hashToDownload[hash]:
                shouldBeDownloaded = True
        else:
            course.isNew = True
        course.shouldBeDownloaded = shouldBeDownloaded
    self.courses.updateValue(allCourses)
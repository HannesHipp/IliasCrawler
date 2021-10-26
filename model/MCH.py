import Folder

class MCH(Folder):

    def get_new_pages(self):
        # damit Oberklassenmethode nicht aufgerufen wird
        return []


    @staticmethod
    def create(element, parent):
        url = element['href']
        content = BeautifulSoup(session.get(url).text, 'lxml')
        return MCH(str(element.text),
                   element['href'],
                   parent,
                   content)
class Element:

    def __init__(self, type=None, parent=None) -> None:
        self.type = type
        self.parent = parent
        self.soup = None

    def set_soup(self, soup):
        self.soup = soup

    def delete_soup(self):
        self.soup = None
from Element import Element


class Element:

    userpath = "C:"

    def __init__(self, name: str, parent: Element):
        self.name = name
        self.parent = parent

    def get_path(self):
        if self.parent is None:
            return Element.userpath
        else:
            parentpath = self.parent.get_path()
            return parentpath + "\\" + self.parent.name

def get_number_of_path_items(item):
    if item.parent is None:
        return 1
    else:
        parent_path_items = get_number_of_path_items(item.parent)
        return parent_path_items + 1

def detect_items_with_long_path(data):
    for item in data:
        if len(item.get_path()) > 240:
            chars_per_path_item = 240 / get_number_of_path_items(item)
            correct_path(item, chars_per_path_item)

def correct_path(item, chars_per_path_item):
    if len(item.name) > chars_per_path_item:
        length = int(chars_per_path_item / 2) - 2
        item.name = item.name[:length] + '___' + item.name[-length:]
    if item.parent is not None:
        correct_path(item.parent, chars_per_path_item)


e1 = Element("a", None)
e2 = Element("b", e1)
e3 = Element("c", e2)
e4 = Element("d", e3)
e5 = Element("e", e4)
e6 = Element("f", e5)
e7 = Element("g.pdf", e6)
#
# detect_items_with_long_path([e7])
print(e7.get_path())




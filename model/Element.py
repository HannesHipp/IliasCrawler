import UserData

class Element:

    def __init__(self, name, url, parent):
        self.name = Element.__clear_name(name)
        self.url = url
        self.parent = parent
        print(self.name)

    def get_path(self):
        if self.parent is None:
            return ""
        else:
            result = self.parent.name
            pointer = self.parent
            while pointer.parent is not None:
                pointer = pointer.parent
                result = pointer.name + "\\" + result
            result = UserData.getLaufwerksbuchstabe() + ":\\" + result
        return result

    @staticmethod
    def __clear_name(name):
        for char in [' ', '/', '\\', ':', '*', '?', '"', '<', '>', '|', '...']:
            name = "".join(name.split(char))
        name = "".join(name.split())
        if len(name) > 100:
            name = name[:45] + '___' + name[-45:]
        return name


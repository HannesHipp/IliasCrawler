import Downloadable

class File(Downloadable):

    @staticmethod
    def create(element, parent):
        name = str(element.text)
        if '.mp4' in name:
            name = name.split('.mp4')[0] + '.mp4'
        else:
            name = name + '.pdf'
        return File(name,
                    element['href'],
                    parent)

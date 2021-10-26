import Downloadable

class Video(Downloadable):

    @staticmethod
    def create(element, parent):
        name = element.attrs['src']
        if '.webm' in name:
            name = name.split('.webm')[0].split('/')[-1] + '.webm'
        else:
            name = name.split('.mp4')[0].split('/')[-1] + '.mp4'
        return Video(name,
                     element.attrs['src'],
                     parent)
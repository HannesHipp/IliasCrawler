from model.Page import Page
from service.BusinessModel import BusinessModel
from service.Session import Session
from json import loads
from model.Video import Video


class OPD(Page):

    url_markers = ['showEpisode']

    @staticmethod
    def get_sub_page_types():
        return []

    def get_files_and_videos(self):
        id = self.url.split("&id=")[1].split("&cmd")[0]
        id1 = id.split("/")[0]
        id2 = id.split("/")[1]
        json_url = f'https://ilias3.uni-stuttgart.de/Customizing/global/plugins/Services/Repository/RepositoryObject/Opencast/api.php/episode.json?id={id1}%2F{id2}'
        json = BusinessModel.instance.session.get_file_content(json_url)
        videos = loads(json)["search-results"]["result"]["mediapackage"]["media"]["track"]
        print([video["type"] for video in videos])
        video = [video for video in videos if "presentation" in video["type"]][0]
        extenstion = video['mimetype'].split('/')[1]
        return [Video(f"{self.name}.{extenstion}", video["url"], self.parent)]

    @staticmethod
    def create(name, url, parent):
        return OPD(name,
                   url,
                   parent)

    @staticmethod
    def is_valid(bs4_element):
        if any(x in OPD.get_url(bs4_element) for x in OPD.url_markers):
            return True
        return False

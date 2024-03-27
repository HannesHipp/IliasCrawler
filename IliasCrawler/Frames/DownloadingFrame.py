from Framework.Datapoint import Datapoint
from Framework.GuiModuls.ProgressBar import ProgressBar
from Framework.GuiModuls.TextLabel import TextLabel
from Framework.OutputFrame import OutputFrame

from IliasCrawler.Datapoints.FilesAndVideos import FilesAndVideos
from IliasCrawler.Datapoints.Path import Path
from IliasCrawler.Functions.Download import Download


class DownloadingFrame(OutputFrame):

    def __init__(self, path: Path, files_and_videos: FilesAndVideos):
        current_file = Datapoint(save=False)
        percentage_downloaded = Datapoint(save=False)
        function = Download(path, files_and_videos, current_file, percentage_downloaded)
        super().__init__(
            path="IliasCrawler\\resources\\DownloadingView.ui",
            function=function
        )
        self.path = path
        self.files_and_videos = files_and_videos
        self.add_module(
            ProgressBar(percentage_downloaded, self.progress_bar, self.label_percentage)
        )
        self.add_module(
            TextLabel(current_file, self.label_current_file_name, lambda x: x)
        )

    def add_next_frames(self, success_frame):
        self.success_frame = success_frame

    def decide_next_frame(self, pressedButton):
        return self.success_frame

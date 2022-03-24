from controller.Frame import Frame

class DownloadingController(Frame):

    def __init__(self):
        self.ui_file_location = 'resources\DownloadingView.ui'
        super().__init__()
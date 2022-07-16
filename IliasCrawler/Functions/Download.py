from Framework.Function import Function


class Download(Function):

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.path = kwargs['path']
        self.filesAndVideos = kwargs['filesAndVideos']

    def execute(self, progress_signal):
        downloaded_already = 0
        errors = []
        for item in self.filesAndVideos.value:
            try:
                item.download()
                self.filesAndVideos.saveValue(item.get_hash())
                downloaded_already += 1
                progress_signal.emit((downloaded_already, item.name))
            except Exception as e:
                # implement logging
                # if not Exception is ItemAlreadyExists:
                #     errors.append(item.get_path() + "\\" + item.name + ", Grund: " + str(e))
                pass

# Crawl --> FilesToDownload --> Download --> filesDownloaded

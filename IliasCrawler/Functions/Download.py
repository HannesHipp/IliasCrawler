from Framework.Function import Function


class Download(Function):

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.path = kwargs['path']
        self.filesAndVideos = kwargs['filesAndVideos']

    def execute(self):
        print("download executed")

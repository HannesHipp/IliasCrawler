from Framework.Function import Function


class Crawl(Function):

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.courses = kwargs['courses']

    def execute(self):
        print("crawl executed")
        self.outputDatapoint.value = 'fv'
        self.executionFinished.emit()
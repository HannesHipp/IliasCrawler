from Framework.Frame import Frame


class InputFrame(Frame):

    def __init__(self, path, datapoints, buttonNames):
        super().__init__(path, datapoints, buttonNames)

    def show(self):
        self.display.emit(self)

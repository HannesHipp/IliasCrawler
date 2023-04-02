from Framework.DataElements.PathSelector import PathSelector
from Framework.Frame import Frame


class PathFrame(Frame):

    def __init__(self, path):
        super().__init__(
            path="IliasCrawler\\resources\\PathSelectionView.ui",
            datapoints=[path],
            buttonNames=['button_continue']
        )
        self.path = path
        PathSelector(path, self.lineedit_path, self.button_select_path)

    def decideNextFrame(self):
        return None

from Framework.GuiModuls.PathSelector import PathSelector
from Framework.InputFrame import Frame


class PathFrame(Frame):

    def __init__(self, path):
        super().__init__(
            path="IliasCrawler\\resources\\PathSelectionView.ui",
            buttonNames=['button_continue']
        )
        self.path = path
        self.addModule(
            PathSelector(path, self.lineedit_path, self.button_select_path)
        )

    def addNextFrames(self, getCoursesFrame):
        self.getCoursesFrame = getCoursesFrame

    def decideNextFrame(self, pressedButton):
        return self.getCoursesFrame

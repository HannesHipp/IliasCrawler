from Framework.GuiModuls.PathSelector import PathSelector
from Framework.InputFrame import InputFrame


class PathFrame(InputFrame):

    def __init__(self, path):
        super().__init__(
            path="IliasCrawler\\resources\\PathSelectionView.ui",
            buttonNames=['button_continue']
        )
        self.path = path
        self.setGuiModuls(
            PathSelector(path, self.lineedit_path, self.button_select_path)
        )

    def addNextFrames(self, getCoursesFrame):
        self.getCoursesFrame = getCoursesFrame

    def decideNextFrame(self, pressedButton):
        return self.getCoursesFrame
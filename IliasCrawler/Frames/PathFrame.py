from Framework.GuiModuls.PathSelector import PathSelector
from Framework.Frame import Frame


class PathFrame(Frame):

    def __init__(self, path):
        super().__init__(
            path="IliasCrawler\\resources\\PathSelectionView.ui",
            next_frame_button_names=['button_continue']
        )
        self.path = path
        self.add_module(
            PathSelector(path, self.lineedit_path, self.button_select_path)
        )

    def addNextFrames(self, getCoursesFrame):
        self.getCoursesFrame = getCoursesFrame

    def decide_next_frame(self, pressedButton):
        return self.getCoursesFrame

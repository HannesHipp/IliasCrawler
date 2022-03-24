from controller.Frame import Frame
from PyQt5.QtCore import pyqtSignal
from easygui import diropenbox


class PathSelectionController(Frame):

    signal_send_storage_path = pyqtSignal(str)
    
    def __init__(self):   
        self.ui_file_location = 'C:\\Users\\Hannes\\Code Projekte\\IliasCrawler\\IliasCrawler\\resources\\PathSelectionView.ui'
        super().__init__()
        self.button_select_path.clicked.connect(self.button_select_path_on_action)

    def button_select_path_on_action(self):
        path = diropenbox()
        if path is not None:
            self.signal_send_storage_path.emit(path)


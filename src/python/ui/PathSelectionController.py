from controller.CourseLoadingController import CourseLoadingController
from controller.Frame import Frame
from controller.Window import Window
from easygui import diropenbox
from service.Database import Database


class PathSelectionController(Frame):
    
    def __new__(cls, container):
        if not hasattr(cls, 'instance'):
            cls.instance = super(PathSelectionController, cls).__new__(cls)
        return cls.instance
    
    def __init__(self, container):   
        self.ui_file_location = 'C:\\Users\\Hannes\\Code Projekte\\IliasCrawler\\IliasCrawler\\view\\PathSelectionView.ui'
        super().__init__(container)
        self.button_select_path.clicked.connect(self.button_select_path_on_action)

    def button_select_path_on_action(self):
        path = diropenbox()
        if path is not None:
            Database.get_instance("storage_path").add(path)
            CourseLoadingController.instance.first_time_execution = True
            CourseLoadingController.instance.show()

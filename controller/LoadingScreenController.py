from controller.Frame import Frame

class LoadingScreenController(Frame):

    def __init__(self):
        self.ui_file_location = 'resources\LoadingScreenView.ui'
        super().__init__()
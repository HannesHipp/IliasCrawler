from Framework.Frame import Frame
from Framework.Function import Function

from PyQt5.QtCore import QThreadPool


class OutputFrame(Frame):

    def __init__(self, path, function: Function, next_frame_button_names=[], start_button_name=None, cancel_button_name=None):
        super().__init__(path, next_frame_button_names)
        self.function = function
        self.function.setAutoDelete(False)
        if not next_frame_button_names:
            self.function.signals.ended.connect(self.finalize)
        self.start_button = None   
        if start_button_name:
            self.start_button = getattr(self, start_button_name)
            self.start_button.pressed.connect(self.function.start_execution)
        if cancel_button_name:
            getattr(self, cancel_button_name).pressed.connect(self.function.cancel_execution)

    def show(self):
        if not self.start_button:
            self.function.start_execution()
        super().show()
        
    def finalize(self):
        self.function.cancel_execution()
        super().finalize()

    def get_module_errors(self):
        module_errors = super().get_module_errors()
        if self.function.error:
            module_errors.extend(self.function.error)
        return module_errors

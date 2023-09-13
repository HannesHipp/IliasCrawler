from Framework.Datapoint import Datapoint
from PyQt5.QtCore import pyqtBoundSignal


class GuiModul:

    def __init__(self, datapoint: Datapoint, changed_signal=None) -> None:
        self.datapoint = datapoint
        self.error = None
        if changed_signal:
            changed_signal.connect(self.publish)
        self.datapoint.value_changed.connect(self.update)

    def publish(self):
        value = self.get_value()
        error = self.datapoint.submit_value(value)
        self.error = error
    
    def update(self):
        value = self.datapoint.value
        self.set_value(value)

    def save_datapoint(self):
        self.datapoint.save_to_db()

    def get_value(self):
        return None
    
    def set_value(self, value):
        raise Exception(
            f"set_value() method not implemented for {self.__class__.__name__}"
        )


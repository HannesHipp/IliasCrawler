from PyQt5.QtWidgets import QWidget, QWidget
from PyQt5.uic import loadUi
import IliasCrawler.resources.resources


class Frame(QWidget):

    def __init__(self, **kwargs):
        super().__init__()
        self.index = None
        loadUi(kwargs['framePath'], self)
        if 'triggerButtonName' in kwargs:
            triggerButton = getattr(self, kwargs['triggerButtonName'])
            triggerButton.clicked.connect(self.toDoAfterTrigger)
        self.datapoints = []

    def toDoAfterTrigger(self):
        for datapoint in self.datapoints:
            datapoint.toDoAfterTrigger()
        self.datapoints[0].done.emit()

    def getValues(self):
        allHaveValue = True
        for datapoint in self.datapoints:
            datapoint.getValue()
            allHaveValue = allHaveValue and datapoint.value
        if allHaveValue:
            self.datapoints[0].done.emit()
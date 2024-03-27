from PyQt5.QtWidgets import QListView
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QBrush, QColor

from Framework.Datapoint import Datapoint
from Framework.GuiModuls.GuiModul import GuiModul


class ObjectSelectionList(GuiModul):

    def __init__(self, datapoint: Datapoint, list_view: QListView, name_attr: str, checked_attr: str, colored_attr: str) -> None:
        list_view.setModel(QStandardItemModel())
        super().__init__(
            datapoint=datapoint,
            changed_signal=list_view.model().dataChanged
        )
        self.list_view = list_view
        self.name_attr = name_attr
        self.checked_attr = checked_attr
        self.colored_attr = colored_attr

    def get_value(self):
        model = self.list_view.model()
        result = []
        for i in range(model.rowCount()):
            item = model.item(i)
            object = item.data()
            if item.checkState() == Qt.Checked:
                setattr(object, self.checked_attr, True)
            else:
                setattr(object, self.checked_attr, False)
            result.append(object)
        return result

    def set_value(self, value):
        model = self.list_view.model()
        if model.rowCount() > 0: 
            pass
        else:
            self.initialize(value) 

    def initialize(self, objects):
        model = self.list_view.model()
        for object in objects:
            item = QStandardItem(getattr(object, self.name_attr))
            item.setData(object)
            item.setCheckable(True)
            item.setCheckState(Qt.Unchecked)
            if getattr(object, self.checked_attr):
                item.setCheckState(Qt.Checked)
            if getattr(object, self.colored_attr):
                item.setBackground(QBrush(QColor(113, 217, 140)))
                model.insertRow(0, item)
            else:
                model.appendRow(item)

    # def update_incrementally(self, objects):
    #     model = self.list_view.model()
    #     for object in objects:
    #         item = QStandardItem(getattr(object, self.name_attr))
    #         item.setData(object)
    #         item.setCheckable(True)
    #         item.setCheckState(Qt.Unchecked)
    #         if getattr(object, self.checked_attr):
    #             item.setCheckState(Qt.Checked)
    #         if getattr(object, self.colored_attr):
    #             item.setBackground(QBrush(QColor(113, 217, 140)))
    #             model.insertRow(0, item)
    #         else:
    #             model.appendRow(item)
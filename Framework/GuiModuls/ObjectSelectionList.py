from Framework.Datapoint import Datapoint
from PyQt5.QtWidgets import QListView
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QBrush, QColor

from Framework.GuiModuls.GuiModul import GuiModul


class ObjectSelectionList(GuiModul):

    def __init__(self, datapoint: Datapoint, qtListView: QListView, nameAttr: str, checkedAttr: str, coloredAttr: str) -> None:
        super().__init__([datapoint])
        qtListView.setModel(QStandardItemModel())
        self.datapoint = datapoint
        self.qtListView = qtListView
        self.nameAttr = nameAttr
        self.checkedAttr = checkedAttr
        self.coloredAttr = coloredAttr

    def publish(self):
        model = self.qtListView.model()
        result = []
        for i in range(model.rowCount()):
            item = model.item(i)
            object = item.data()
            if item.checkState() == Qt.Checked:
                setattr(object, self.checkedAttr, True)
            else:
                setattr(object, self.checkedAttr, False)
            result.append(object)
        self.datapoint.updateValue(result)

    def update(self):
        model = self.qtListView.model()
        for object in self.datapoint.value:
            item = QStandardItem(getattr(object, self.nameAttr))
            item.setData(object)
            item.setCheckable(True)
            item.setCheckState(Qt.Unchecked)
            if getattr(object, self.checkedAttr):
                item.setCheckState(Qt.Checked)
            if getattr(object, self.coloredAttr):
                item.setBackground(QBrush(QColor(113, 217, 140)))
                model.insertRow(0, item)
            else:
                model.appendRow(item)

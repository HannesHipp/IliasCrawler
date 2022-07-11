from Framework.Database import Database
from Framework.Datapoint import Datapoint
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QBrush, QColor
from PyQt5.QtCore import Qt
from distutils.util import strtobool

class Courses(Datapoint):

    def __init__(self, **kwargs) -> None:
        super().__init__(
            databaseStructure = ('hash', 'shouldBeDownlaoded'),
            dataElementName = "listView",
            **kwargs
            )

    def howToGetValue(self):
        hashToDownloadIs = self.savedValue
        allCourses = self.calculatedValue
        model = QStandardItemModel()
        for course in allCourses:
            item = QStandardItem(course.name)
            item.setData(course)
            item.setCheckable(True)
            item.setCheckState(Qt.Unchecked)
            hash = course.getHash()
            if hash in hashToDownloadIs:
                if hashToDownloadIs[hash]:
                    item.setCheckState(Qt.Checked)
                model.appendRow(item)
            else:
                item.setBackground(QBrush(QColor(113,217,140)))
                model.insertRow(0, item)
        self.dataElement.setModel(model)
        self.display.emit(self.frame)

    def extractFromDataElement(self):
        model = self.dataElement.model()
        result = []
        for i in range(model.rowCount()):
            item = model.item(i)
            course = item.data()
            if item.checkState() == Qt.Checked:
                course.shouldBeDownloaded = True
            else: 
                course.shouldBeDownloaded = False
            result.append(course)
        return result

    def validate(self, value):
        for course in value:
            if course.shouldBeDownloaded:
                return True
        return False, "Es muss mindestens ein Kurs ausgewählt werden."

    def getSavedValue(self):
        result = {}
        tupleList = self.database.getTupleList()
        if tupleList is None:
            return None
        else:
            for tuple in tupleList:
                result[tuple[0]] = strtobool(tuple[1])
        return result

    def saveValue(self):
        result = []
        for course in self.value:
            result.append((str(course.getHash()), str(course.shouldBeDownloaded)))
        self.database.saveTupleList(result)
from Framework.Datapoint import Datapoint
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QBrush, QColor
from PyQt5.QtCore import Qt
from distutils.util import strtobool

class Courses(Datapoint):

    def __init__(self, **kwargs) -> None:
        super().__init__(
            **kwargs,
            numberOfDatabaseFields = 2
        )

    def getValue(self, savedValue, calculatedValue):
        hashToDownloadIs = savedValue
        allCourses = calculatedValue
        for course in allCourses:
            shouldBeDownloaded = False
            hash = course.getHash()
            if hash in hashToDownloadIs:
                course.isNew = False
                if hashToDownloadIs[hash]:
                    shouldBeDownloaded = True
            else:
                course.isNew = True
            course.shouldBeDownloaded = shouldBeDownloaded
        return allCourses, True
        
    def readFrom(self, dataElement):
        model = dataElement.model()
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
    
    def writeTo(self, dataElement, courses):
        model = QStandardItemModel()
        for course in courses:
            item = QStandardItem(course.name)
            item.setData(course)
            item.setCheckable(True)
            item.setCheckState(Qt.Unchecked)
            if course.shouldBeDownloaded:
                item.setCheckState(Qt.Checked)
            if course.isNew:
                item.setBackground(QBrush(QColor(113,217,140)))
                model.insertRow(0, item)
            else:
                model.appendRow(item)
        dataElement.setModel(model)

    def valueFromDatabaseFormat(self, tupleList):
        result = {}
        for tuple in tupleList:
            result[tuple[0]] = strtobool(tuple[1])
        return result

    def valueToDatabaseFormat(self, courses):
        result = []
        for course in courses:
            result.append((str(course.getHash()), str(course.shouldBeDownloaded)))
        return result
    
    def validate(self, value):
        for course in value:
            if course.shouldBeDownloaded:
                return True, ""
        return False, "Es muss mindestens ein Kurs ausgewählt werden."
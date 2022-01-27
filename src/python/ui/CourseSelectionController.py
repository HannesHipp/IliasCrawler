import time
from controller.Frame import Frame
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QBrush, QColor
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox

from service.Database import Database


class CourseSelectionController(Frame):

    def __new__(cls, container):
        if not hasattr(cls, 'instance'):
            cls.instance = super(CourseSelectionController, cls).__new__(cls)
        return cls.instance

    def __init__(self, container):
        self.ui_file_location = 'C:\\Users\\Hannes\\Code Projekte\\IliasCrawler\\IliasCrawler\\view\\CourseSelectionView.ui'
        super().__init__(container)
        self.button_select_choice.clicked.connect(
            self.button_select_choice_on_action)
        self.model = QStandardItemModel()
        self.listView.setModel(self.model)
        self.courses = None
        self.first_time_execution = None

    def show(self):
        super().show()
        self.set_model()
        if not self.first_time_execution:
            # CourseSelectionController.show_intervention_dialog()
            a = 2
            
    def button_select_choice_on_action(self):
        self.save_selection_to_database()
        # print(self.get_selection())

    def set_model(self):
        for course in self.courses:
            item = QStandardItem(course.name)
            item.setCheckable(True)
            item.setData(course)
            if course.should_be_downloaded:
                item.setCheckState(Qt.Checked)
            if course.is_new:
                item.setBackground(QBrush(QColor(113,217,140)))
                self.model.insertRow(0, item)
            else:
                self.model.appendRow(item)

    def save_selection_to_database(self):
        database = Database.get_instance("all_courses")
        database.clear_table()
        for i in range(self.model.rowCount()):
            item = self.model.item(i)
            course = item.data()
            should_be_downloaded = "False"
            if item.checkState() == Qt.Checked:
                should_be_downloaded = "True"
            database.add(course.get_hash(), should_be_downloaded)

    @staticmethod
    def show_intervention_dialog():
        dialog = QMessageBox()
        dialog.setWindowTitle("AutoStart")
        dialog.exec_()
        sec = 10
        while sec >= 0:
            dialog.setText(
                f"IliasCrawler wird in {sec} Sekunden beginnen, in den zuvor ausgewählten Kursen nach neuen Dateien zu suchen. Wenn du deine Kurse anpassen möchtest, dann wähle bitte \"Abbrechen\".")
            time.sleep(1)
            sec -= 1

    def get_selection(self):
        return [self.model.item(i).text() for i in range(
            self.model.rowCount()) if self.model.item(i).checkState() == Qt.Checked]

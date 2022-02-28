import time
from controller.AutoStartController import AutoStartController
from controller.CrawlingController import CrawlingController
from controller.Frame import Frame
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QBrush, QColor
from PyQt5.QtCore import Qt
from service.BusinessModel import BusinessModel



class CourseSelectionController(Frame):

    def __new__(cls, container):
        if not hasattr(cls, 'instance'):
            cls.instance = super(CourseSelectionController, cls).__new__(cls)
        return cls.instance

    def __init__(self, container):
        self.ui_file_location = 'C:\\Users\\Hannes\\Code Projekte\\IliasCrawler\\IliasCrawler\\resources\\CourseSelectionView.ui'
        super().__init__(container)
        self.button_select_choice.clicked.connect(
            self.button_select_choice_on_action)
        AutoStartController.instance.button_start.clicked.connect(
            self.start_autostart_on_action
        )
        AutoStartController.instance.button_cancel.clicked.connect(
            self.cancel_autostart_on_action
        )
        self.canceled = False

    def button_select_choice_on_action(self):
        BusinessModel.instance.set_fresh_courses(self.get_updated_course_list())
        CrawlingController.instance.show()

    def show(self):
        super().show()
        fresh_courses = BusinessModel.instance.fresh_courses
        saved_course_dict = BusinessModel.instance.safed_courses_dict
        self.model = self.construct_item_model(fresh_courses, saved_course_dict)
        self.listView.setModel(self.model)
        if not BusinessModel.instance.first_time_execution:
            self.show_autostart_dialog()

    def construct_item_model(self, fresh_courses, safed_courses_dict):
        result = QStandardItemModel()
        for course in fresh_courses:
            item = QStandardItem(course.name)
            item.setCheckable(True)
            item.setData(course)
            item.setCheckState(Qt.Unchecked)
            if not course.get_hash() in safed_courses_dict:
                item.setCheckState(Qt.Checked)
                item.setBackground(QBrush(QColor(113,217,140)))
                result.insertRow(0, item)
            else:
                if safed_courses_dict[course.get_hash()]:
                    item.setCheckState(Qt.Checked)
                result.appendRow(item)
        return result   

    def get_updated_course_list(self):
        result = []
        for i in range(self.model.rowCount()):
            item = self.model.item(i)
            course = item.data()
            if item.checkState() == Qt.Checked:
                course.should_be_downloaded = True
            else: 
                course.should_be_downloaded = False
            result.append(course)
        return result

    def show_autostart_dialog(self):
        autostart = AutoStartController.instance
        autostart.show()
        sec = 20
        while sec >= 0:
            autostart.description.setText(
                f"Das Programm wird in {sec}s deine bereits auswählten Kurse durchsuchen und neue Dateien automatisch herunterladen. Wenn du deine Kurse ändern möchtest, klicke einfach auf 'Abbrechen'.")
            autostart.button_start.setText(f"Starten ({sec})")
            time.sleep(1)
            sec -= 1
            autostart.app.processEvents()
            if self.canceled:
                break
        if not self.canceled:
            AutoStartController.instance.button_start.clicked.emit()

    def start_autostart_on_action(self):
        AutoStartController.instance.close()
        self.button_select_choice.clicked.emit()


    def cancel_autostart_on_action(self):
        self.canceled = True
        AutoStartController.instance.close()

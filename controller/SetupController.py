from view.CourseSelectionView import CourseSelectionView
from controller.CourseSelectionController import CourseSelectionController
from service.Database import Database
from view.SetupView import SetupView


class SetupController:

    @staticmethod
    def run():
        # get username and password and save to to database
        username, password = SetupView.login_data_promt()
        path = SetupView.storage_place_promt()
        Database.get_instance("userdata").add(username, password, path)

from service.Database import Database
from view.SetupView import SetupView


class SetupController:

    @staticmethod
    def run():
        # get username and password and save to to database
        username, password = SetupView.get_username_and_password()
        path = SetupView.get_storage_place()
        SetupView.setup_info()
        Database.get_instance("userdata").add(username, password, path)

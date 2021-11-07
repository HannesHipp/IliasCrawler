from service.Database import Database
from view.SetupView import SetupView


class SetupController:

    @staticmethod
    def run():
        username, password = SetupView.login_data_promt()
        path = SetupView.storage_place_promt()
        Database.get_instance("userdata").add(["true", username, password, path])

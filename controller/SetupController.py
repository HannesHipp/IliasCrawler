from service.Session import Session
from service.Database import Database
from view.SetupView import SetupView
from bs4 import BeautifulSoup


class SetupController:

    @staticmethod
    def run():
        # get username and password and save to to database
        SetupView.login_info_promt()
        valid = False
        while not valid:
            username, password = SetupView.login_data_promt()
            try:
                Session.get_session(username, password)
                valid = True
            except ConnectionError:
                SetupView.login_failed_promt()
                valid = False
        path = SetupView.storage_place_promt()
        if path[-1] == "\\":
            path = path[:-1]
        Database.get_instance("userdata").add(username, password, path)




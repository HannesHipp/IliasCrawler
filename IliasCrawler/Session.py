from bs4 import BeautifulSoup
import requests


class Session:

    __instance = None
    LOGINURL = "https://ilias3.uni-stuttgart.de/ilias.php?lang=de&client_id=Uni_Stuttgart&cmd=post&cmdClass=ilstartupgui&cmdNode=12g&baseClass=ilStartUpGUI&rtoken="
    COURSESURL = "https://ilias3.uni-stuttgart.de/ilias.php?baseClass=ilDashboardGUI&cmd=jumpToSelectedItems"

    def __init__(self, username, password):
        session = requests.session()
        data = {
            'username': username,
            'password': password,
            'cmd[doStandardAuthentication]': 'Anmelden'
        }
        session.post(Session.LOGINURL, data=data)
        self.session = session

    def is_valid(self):
        test_content = BeautifulSoup(
            self.session.get(Session.COURSESURL).text, "lxml")
        # If "Anmelden" button is present, then we are not already logged in
        if test_content.find(attrs={"aria-label": "Anmelden"}) is not None:
            return False
        else:
            return True

    @staticmethod
    def setGlobalSession(session):
        Session.__instance = session.session

    @staticmethod
    def get_content(url):
        if Session.__instance is None:
            raise Exception("No global session is set")
        return BeautifulSoup(Session.__instance.get(url).text, 'lxml')

    @staticmethod
    def get_file_content(url):
        if Session.__instance is None:
            raise Exception("No global session is set")
        return Session.__instance.get(url).content

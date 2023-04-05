from bs4 import BeautifulSoup
import requests


class Session:

    __instance = None

    def __init__(self, username, password):
        LOGINURL = "https://ilias3.uni-stuttgart.de/ilias.php?lang=de&client_id=Uni_Stuttgart&cmd=post&cmdClass=ilstartupgui&cmdNode=12f&baseClass=ilStartUpGUI&rtoken="
        session = requests.session()
        data = {
            'username': username,
            'password': password,
            'cmd[doStandardAuthentication]': 'Anmelden'
        }
        session.post(LOGINURL, data=data)
        self.session = session
        if Session.__instance is None and self.is_valid():
            Session.__instance = self

    def is_valid(self):
        TESTURL = "https://ilias3.uni-stuttgart.de/ilias.php?baseClass=ilDashboardGUI&cmd=jumpToSelectedItems"
        test_content = BeautifulSoup(self.session.get(TESTURL).text, "lxml")
        # If "Anmelden" button is present, then we are not already logged in
        if test_content.find(attrs={"aria-label": "Anmelden"}) is not None:
            return False
        else:
            return True

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

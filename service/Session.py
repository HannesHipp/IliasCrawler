from bs4 import BeautifulSoup
import requests
from service.Database import Database


class Session:
    __instance = None

    def __init__(self, username, password):
        self.session = requests.session()
        self.session.post('https://ilias3.uni-stuttgart.de/ilias.php?lang=de&client_id=Uni_Stuttgart'
                          '&cmd=post&cmdClass=ilstartupgui&cmdNode=123&baseClass=ilStartUpGUI&rtoken=',
                          data={
                              'username': username,
                              'password': password,
                              'cmd[doStandardAuthentication]': 'Anmelden'
                          }
                          )

    @staticmethod
    def get_instance():
        if Session.__instance is None:
            userdata = Database.get_instance("userdata").get_all()[0]
            username = userdata[0]
            password = userdata[1]
            Session.__instance = Session(username, password).session
        return Session.__instance

    @staticmethod
    def get_content(url):
        return BeautifulSoup(Session.get_instance().get(url).text, 'lxml')

    @staticmethod
    def get_file_content(url):
        return Session.get_instance().get(url).content

    def is_valid(self):
        test_content = BeautifulSoup(self.session.get("https://ilias3.uni-stuttgart.de/ilias.php?baseClass=ilDashboard"
                                                      "GUI&cmd=jumpToSelectedItems").text, "lxml")

        # If "Anmelden" button is present, then we are not already logged in
        if test_content.find(attrs={"aria-label": "Anmelden"}) is not None:
            return False
        else:
            return True

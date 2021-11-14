from bs4 import BeautifulSoup
import requests
from service.Database import Database


class Session:
    __instance = None

    @staticmethod
    def get_session(username="", password=""):
        if Session.__instance is None:
            if len(Database.get_instance("userdata").get_all()) != 0:
                userdata = Database.get_instance("userdata").get_all()[0]
            else:
                userdata = [username, password]
            session = requests.session()
            session.post('https://ilias3.uni-stuttgart.de/ilias.php?lang=de&client_id=Uni_Stuttgart'
                         '&cmd=post&cmdClass=ilstartupgui&cmdNode=123&baseClass=ilStartUpGUI&rtoken=',
                         data={
                             'username': userdata[0],
                             'password': userdata[1],
                             'cmd[doStandardAuthentication]': 'Anmelden'
                         }
                         )
            test_content = BeautifulSoup(session.get("https://ilias3.uni-stuttgart.de/ilias.php?baseClass=ilDashboard"
                                                "GUI&cmd=jumpToSelectedItems").text, "lxml")
            # If "Anmelden" button is present, then we are not already logged in
            if test_content.find(attrs={"aria-label": "Anmelden"}) is not None:
                raise ConnectionError
            Session.__instance = session
        return Session.__instance

    def __init__(self):
        if Session.__instance is not None:
            raise Exception("Bitte getSession verwenden")

    @staticmethod
    def get_content(url):
        return BeautifulSoup(Session.get_session().get(url).text, 'lxml')

    @staticmethod
    def get_file_content(url):
        return Session.get_session().get(url).content

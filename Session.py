import requests
from bs4 import BeautifulSoup
import UserData

class Session:
    __instance = None

    @staticmethod
    def getSession():
        if Session.__instance is None:
            Session.__instance = Session()
        return Session.__instance

    def __init__(self):
        if Session.__instance is not None:
            raise Exception("Bitte getSession verwenden")
        self.session = requests.session()
        self.session.post('https://ilias3.uni-stuttgart.de/ilias.php?lang=de&client_id=Uni_Stuttgart&cmd=post&cmdClass'
                          '=ilstartupgui&cmdNode=123&baseClass=ilStartUpGUI&rtoken=',
                          data={
                            'username': UserData.getUsername(),
                            'password': UserData.getPassword(),
                            'cmd[doStandardAuthentication]': 'Anmelden'
                          }
                          )

    @staticmethod
    def get_content(url):
        return BeautifulSoup(Session.__instance.get(url).text, 'lxml')
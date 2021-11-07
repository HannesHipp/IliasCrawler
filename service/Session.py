import requests
from bs4 import BeautifulSoup
import UserData
from service.Database import Database, Field


class Session:
    __instance = None

    @staticmethod
    def getSession():
        if Session.__instance is None:
            Session.__instance = Session()
            Session.__instance.session = requests.session()
            userdata = Database.get_instance("userdata").find(Field("containsdata", "text"), "true")[0]
            Session.__instance.session.post('https://ilias3.uni-stuttgart.de/ilias.php?lang=de&client_id=Uni_Stuttgart'
                                            '&cmd=post&cmdClass=ilstartupgui&cmdNode=123&baseClass=ilStartUpGUI&rtoken=',
                                            data={
                                                  'username': userdata[1],
                                                  'password': userdata[2],
                                                  'cmd[doStandardAuthentication]': 'Anmelden'
                                            }
                                            )
        return Session.__instance.session

    def __init__(self):
        if Session.__instance is not None:
            raise Exception("Bitte getSession verwenden")


    @staticmethod
    def get_content(url):
        return BeautifulSoup(Session.getSession().get(url).text, 'lxml')

    @staticmethod
    def get_file_content(url):
        return Session.getSession().get(url)
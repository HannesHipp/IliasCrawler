import threading
from bs4 import BeautifulSoup
import requests


class Session:


    __instance = None
    __semaphore = threading.Semaphore()
        

    @staticmethod
    def set_session(username, password):
        if Session.__instance is not None:
            return True
        session = requests.session()
        cmdNode = Session.get_cmdNode(session)
        LOGINURL = f"https://ilias3.uni-stuttgart.de/ilias.php?lang=de&client_id=Uni_Stuttgart&cmd=post&cmdClass=ilstartupgui&cmdNode={cmdNode}&baseClass=ilStartUpGUI&rtoken="
        data = {
            'username': username,
            'password': password,
            'cmd[doStandardAuthentication]': 'Anmelden'
        }
        session.post(LOGINURL, data=data)
        if Session.is_valid(session):
            Session.__instance = session
            return True
        return False
    

    @staticmethod
    def get_cmdNode(session):
        LANDING_PAGE_URL = "https://ilias3.uni-stuttgart.de/login.php?target=root_1&client_id=Uni_Stuttgart&cmd=force_login&lang=de"
        soup = BeautifulSoup(session.get(LANDING_PAGE_URL).text, 'lxml')
        url = soup.find(attrs={'class':'il_ContainerItemCommand'}).get('href')
        return url.split('cmdNode=')[1].split('&')[0]
    

    @staticmethod
    def is_valid(session):
        TESTURL = "https://ilias3.uni-stuttgart.de/ilias.php?baseClass=ilDashboardGUI&cmd=jumpToSelectedItems"
        test_content = BeautifulSoup(session.get(TESTURL).text, "lxml")
        # If "Anmelden" button is present, then we are not already logged in
        if test_content.find(attrs={"aria-label": "Anmelden"}) is not None:
            return False
        else:
            return True


    @staticmethod
    def get_content(url):
        with Session.__semaphore:
            if Session.__instance is None:
                raise Exception("No global session is set")
            return BeautifulSoup(Session.__instance.get(url).text, 'lxml')

    @staticmethod
    def get_file_content(url):
        with Session.__semaphore:
            if Session.__instance is None:
                raise Exception("No global session is set")
            return Session.__instance.get(url).content

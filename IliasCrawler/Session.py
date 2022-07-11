from bs4 import BeautifulSoup
import requests


class Session:

    def __init__(self, username, password):
        self.session = requests.session()
        self.session.post('https://ilias3.uni-stuttgart.de/ilias.php?lang=de&client_id='
                     'Uni_Stuttgart&cmd=post&cmdClass=ilstartupgui&cmdNode=12g&base'
                     'Class=ilStartUpGUI&rtoken=',
                        data={
                            'username': username,
                            'password': password,
                            'cmd[doStandardAuthentication]': 'Anmelden'
                        }
                        )

    def get_content(self, url):
        return BeautifulSoup(self.session.get(url).text, 'lxml')

    def get_file_content(self, url):
        return self.session.get(url).content

    def is_valid(self):
        test_content = BeautifulSoup(self.session.get("https://ilias3.uni-stuttgart.de/ilias.php?baseClass=ilDashboardGUI&cmd=jumpToSelectedItems").text, "lxml")

        # If "Anmelden" button is present, then we are not already logged in
        if test_content.find(attrs={"aria-label": "Anmelden"}) is not None:
            return False
        else:
            return True


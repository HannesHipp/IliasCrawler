import requests
from bs4 import BeautifulSoup

username = "st162876"
password = "76kg@Sommer"

with requests.session() as session:
    # Vorgehensweise siehe https://pybit.es/articles/requests-session/
    session.post('https://ilias3.uni-stuttgart.de/ilias.php?lang=de&client_id=Uni_Stuttgart&cmd=post&cmdClass=il'
               'startupgui&cmdNode=123&baseClass=ilStartUpGUI&rtoken=',
               data={
                   'username': username,
                   'password': password,
                   'cmd[doStandardAuthentication]': 'Anmelden'
               }
               )
    soup = BeautifulSoup(session.get('https://ilias3.uni-stuttgart.de/ilias.php?cmd=show&cmdClass=ildashboardgui&cmdNode=9x&baseClass=ilDashboardGUI').text, 'lxml')
    article = soup.findAll('a')
    for ele in article:
        print(ele.text)


def get
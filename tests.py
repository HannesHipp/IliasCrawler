import requests
from bs4 import BeautifulSoup
import os
import re

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
    soup = session.get('https://ilias3.uni-stuttgart.de/goto_Uni_Stuttgart_file_2135161_download.html')
    print(soup.text)
    # content = soup.findAll('video')
    # for ele in content:
    #     print(ele.attrs['src'])

#
# s = 'https://ilias3.uni-stuttgart.de/data/Uni_Stuttgart/mobs/mm_2817249/WS2020_Intro_CRT1_UT.mp4?il_wac_token=08fa859bd4b630902f1d0a5ad898125657f0810b&'
# pattern = re.compile(r"\.[a-z0-9]{1,4}")
# seatch = pattern.search(s)
# print(seatch)


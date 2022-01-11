# from io import BytesIO
# from PIL import Image, ImageDraw
# import PySimpleGUI as sg


# def icon(check):
#     box = (20, 20)
#     background = (255, 255, 255, 0)
#     rectangle = (3, 3, 29, 29)
#     line = ((4, 12), (10, 18), (18, 4))
#     im = Image.new('RGBA', box, background)
#     draw = ImageDraw.Draw(im, 'RGBA')
#     draw.rectangle(rectangle, outline='black', width=3)
#     if check == 1:
#         draw.line(line, fill='black', width=3, joint='curve')
#     elif check == 2:
#         draw.line(line, fill='grey', width=3, joint='curve')
#     with BytesIO() as output:
#         im.save(output, format="PNG")
#         png = output.getvalue()
#     return png


# check = [icon(0), icon(1), icon(2)]

# headings = ['President', 'Date of Birth', '1', '2', '3']
# data = [
#     ['Ronald Reagan', 'February 6'],
#     ['Abraham Lincoln', 'February 12'],
#     ['George Washington', 'February 22'],
#     ['Andrew Jackson', 'March 15'],
#     ['Thomas Jefferson', 'April 13'],
#     ['Harry Truman', 'May 8'],
#     ['John F. Kennedy', 'May 29'],
#     ['George H. W. Bush', 'June 12'],
#     ['George W. Bush', 'July 6'],
#     ['John Quincy Adams', 'July 11'],
#     ['Garrett Walker', 'July 18'],
#     ['Bill Clinton', 'August 19'],
#     ['Jimmy Carter', 'October 1'],
#     ['John Adams', 'October 30'],
#     ['Theodore Roosevelt', 'October 27'],
#     ['Frank Underwood', 'November 5'],
#     ['Woodrow Wilson', 'December 28'],
# ]

# treedata = sg.TreeData()
# for president, birthday in data:
#     treedata.Insert('', president, president, values=[birthday]+[1, 2, 3],
#                     icon=check[0])

# sg.theme('LightPurple')
# sg.set_options(font=('Helvetica', 16))
# layout = [
#     [sg.Input("hello")],
#     [sg.Tree(data=treedata, headings=headings[1:], auto_size_columns=True,
#              num_rows=10, col0_width=20, key='-TREE-', row_height=48, metadata=[],
#              show_expanded=False, enable_events=True,
#              select_mode=sg.TABLE_SELECT_MODE_BROWSE)],
#     [sg.Button('Quit')]
# ]
# window = sg.Window('Tree as Table', layout, finalize=True)
# tree = window['-TREE-']
# tree.Widget.heading("#0", text=headings[0])  # Set heading for column #0

# while True:
#     event, values = window.read()
#     if event in (sg.WIN_CLOSED, 'Quit'):
#         break
#     elif event == '-TREE-':
#         president = values['-TREE-'][0]
#         print(president)
#         if president in tree.metadata:
#             tree.metadata.remove(president)
#             tree.update(key=president, icon=check[0])
#         else:
#             tree.metadata.append(president)
#             tree.update(key=president, icon=check[1])

# window.close()

##################

# from typing import ClassVar


# class Element:

#     def get_new_pages(self):
#         result = []
#         for page_type in type(self).get_sub_page_types():
#             result += page_type.extract_from_page()
#         return result

#     def get_files_and_videos(self):
#         result = []
#         for page_type in type(self).downloadable_types:
#             result += page_type.extract_from_page()
#         return result


# class Lm(Element):

#     sub_page_types = []

#     @staticmethod
#     def extract_from_page():
#         print("created LM")
#         return [Lm()]


# class OPD(Lm):

#     sub_page_types = []

#     # @staticmethod
#     # def extract_from_page():
#     #     print("created OPD")
#     #     return [OPD()]


# class Folder(Element):

#     @staticmethod
#     def get_sub_page_types():
#         return [Folder, Lm, OPD]

#     @staticmethod
#     def extract_from_page():
#         print("created Folder")
#         return [Folder()]


# Folder().get_new_pages()

###################

# from model.Element import Element
# from model.Folder import Folder
# from controller.CrawlingController import crawl
# from model.Lm import Lm
# from service.Database import Database
# from service.EventsManagement import EventsManager
# from view.DownloadView import DownloadView
# from view.CrawlingView import CrawlingView

# Database("userdata", "username", "password", "downloadpath")
# Database("files", "hash")
# Database("courses_to_download", "course_number")
# Database("all_courses", "course_number")

# # Setting up Event Management
# EventsManager.get_instance().attach_listener("download", DownloadView())
# EventsManager.get_instance().attach_listener("crawl", CrawlingView())
# b = Element('tesss', "http", None)
# a = Lm.create("test", "https://ilias3.uni-stuttgart.de/goto_Uni_Stuttgart_lm_2480642.html", b)
# crawl(a)

###################

# from model.Video import Video
# from service.Session import Session
# from json import loads
# from pprint import pprint
# from service.Database import Database

# Database("userdata", "username", "password", "downloadpath")
# Database("files", "hash")
# Database("courses_to_download", "course_number")
# Database("all_courses", "course_number")


# def get_files_and_videos(self):
#     id = self.url.split("&id=")[1].split("&cmd")[0]
#     id1 = id.split("/")[0]
#     id2 = id.split("/")[1]
#     json_url = f'https://ilias3.uni-stuttgart.de/Customizing/global/plugins/Services/Repository/RepositoryObject/Opencast/api.php/episode.json?id={id1}%2F{id2}'
#     json = Session.get_file_content(json_url)
#     videos = loads(json)["search-results"]["result"]["mediapackage"]["media"]["track"]
#     print([video["type"] for video in videos])
#     video = [video for video in videos if "presentation" in video["type"]][0]
#     extenstion = video['mimetype'].split('/')[1]
#     return Video(f"{self.name}.{extenstion}", video["url"], self.parent)


# print(get_files_and_videos('https://ilias3.uni-stuttgart.de/ilias.php?ref_id=2168474&id=606c72af-53f5-415e-9b00-9f3c15cec347/63e901c0-edd1-4daa-a566-5d954a684b62&cmd=showEpisode&cmdClass=ilobjopencastgui&cmdNode=r5:qx&baseClass=ilObjPluginDispatchGUI'))

# a = {'media':
#      {'track':
#       [
#           {'audio': {'id': 'audio-1'},
#            'duration': 1076017,
#            'id': 'ae2c9746-98d0-4bce-8b50-43c297cccfdd',
#            'mimetype': 'video/mp4',
#            'tags': {'tag': ['default', 'ilias-download']},
#            'type': 'presenter/delivery',
#            'url': 'https://occdn1.tik.uni-stuttgart.de/mh_default_org/api/57562e01-0e01-4feb-ab64-bed5aced737e/667d53df-2ad5-4b5d-83a2-9b1210cf18e4/9ec4931d_9aec_401b_a3e5_0e34e9fc6554.mp4?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvaWxpYXMzLnVuaS1zdHV0dGdhcnQuZGVcL0N1c3RvbWl6aW5nXC9nbG9iYWxcL3BsdWdpbnNcL1NlcnZpY2VzXC9SZXBvc2l0b3J5XC9SZXBvc2l0b3J5T2JqZWN0XC9PcGVuY2FzdCIsImF1ZCI6Imh0dHBzOlwvXC9vY2NkbjEudGlrLnVuaS1zdHV0dGdhcnQuZGUiLCJpYXQiOjE2Mzk2Nzk2ODksIm5iZiI6MTYzOTY3OTY3OSwiZXhwIjoxNjM5NzAxMjg5LCJ1cmwiOiJcL21oX2RlZmF1bHRfb3JnXC9hcGlcLzU3NTYyZTAxLTBlMDEtNGZlYi1hYjY0LWJlZDVhY2VkNzM3ZVwvNjY3ZDUzZGYtMmFkNS00YjVkLTgzYTItOWIxMjEwY2YxOGU0XC85ZWM0OTMxZF85YWVjXzQwMWJfYTNlNV8wZTM0ZTlmYzY1NTQubXA0In0.M4SCuOngwhJAl76_lvnvlF_6uZAUFM4JWDQ26k5av6w',
#            'video': {'id': 'video-1', 'resolution': '1280x720'}},
#           {'audio': {'id': 'audio-1'},
#            'duration': 1076017,
#            'id': '1d98c47d-e6f2-4854-b167-e01cb5f4c736',
#            'mimetype': 'video/mp4',
#            'tags': {'tag': ['default', 'ilias-download']},
#            'type': 'presentation/delivery',
#            'url': 'https://occdn1.tik.uni-stuttgart.de/mh_default_org/api/57562e01-0e01-4feb-ab64-bed5aced737e/a19b0590-5cdc-4820-84bd-283e013e0277/d44ffbc8_29f3_484f_8146_88f42ebd4766.mp4?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvaWxpYXMzLnVuaS1zdHV0dGdhcnQuZGVcL0N1c3RvbWl6aW5nXC9nbG9iYWxcL3BsdWdpbnNcL1NlcnZpY2VzXC9SZXBvc2l0b3J5XC9SZXBvc2l0b3J5T2JqZWN0XC9PcGVuY2FzdCIsImF1ZCI6Imh0dHBzOlwvXC9vY2NkbjEudGlrLnVuaS1zdHV0dGdhcnQuZGUiLCJpYXQiOjE2Mzk2Nzk2ODksIm5iZiI6MTYzOTY3OTY3OSwiZXhwIjoxNjM5NzAxMjg5LCJ1cmwiOiJcL21oX2RlZmF1bHRfb3JnXC9hcGlcLzU3NTYyZTAxLTBlMDEtNGZlYi1hYjY0LWJlZDVhY2VkNzM3ZVwvYTE5YjA1OTAtNWNkYy00ODIwLTg0YmQtMjgzZTAxM2UwMjc3XC9kNDRmZmJjOF8yOWYzXzQ4NGZfODE0Nl84OGY0MmViZDQ3NjYubXA0In0.eFdaEAUnN6OKfBK-oAHTfzDF7OW00NafdmF6FJXU3dI',
#            'video': {'id': 'video-1', 'resolution': '1920x1080'}
#            }
#       ]
#       }
#      }

# ############################

# from service.Session import Session
# from service.Database import Database
# from pprint import pprint

# Database("userdata", "username", "password", "downloadpath")
# Database("files", "hash")
# Database("courses_to_download", "course_number")
# Database("all_courses", "course_number")


# content = Session.get_content("https://ilias3.uni-stuttgart.de/goto_Uni_Stuttgart_crs_2093097.html")

import PySimpleGUI as sg
import easygui

sg.theme('DarkTeal9')

layout = [
    [sg.Text('Damit wir deine Dateien herrunterladen können müssen wir uns über deinen Ilias-Account anmelden.\n'
              'Deine Daten bleiben auf deinem Gerät und werden selbstverständlich nicht weitergegeben.')],
    [sg.Text('Benutzername', size=(10,1)), sg.InputText(key='username')],
    [sg.Text('Passwort', size=(10,1)), sg.InputText(key='password')],
    [sg.Text('Wähle bitte zusätzlich noch den Ordner, in dem deine Kurse gespeichert werden sollen:')],
    [sg.Button('Zielordner wählen', key = 'downloadpath')],
    [sg.Button('Speichern', key = 'save')]
]

window = sg.Window('Setup', layout)
window2 = sg.Window('Hallo', layout2)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'downloadpath':
        easygui.diropenbox()
    if event == 'save':
        window.close()
        window = window2
window.close()

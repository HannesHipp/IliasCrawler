from service.Session import Session
from service.Database import Database
import model.Service
from pprint import pprint
import unicodedata

Database("userdata", "username", "password", "downloadpath")
bs4 = Session.get_content("https://ilias3.uni-stuttgart.de/goto_Uni_Stuttgart_fold_2135264.html")
list = model.Service.get_items_where_href_contains_markers(bs4, "_file_")
result = []
for item in list:
    ex = item.parent.parent.parent.find(class_="il_ItemProperty").text.replace("\n", "").replace("\t", "").replace("\xa0", "")
    pprint(ex)

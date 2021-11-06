import os
from view.SetupView import SetupView

database_exists = os.path.isfile('logdatei.txt')
if not database_exists:
    SetupView.show()
MainView.show()

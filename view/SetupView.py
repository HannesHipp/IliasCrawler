class SetupView():

    @staticmethod
    def login_data_promt():
        print("Damit wir deine Dateien herrunterladen können müssen wir uns über deinen Ilias-Account anmelden."
              "\nDeine Daten bleiben auf deinem Gerät und werden selbstverständlich nicht weitergegeben.")
        username = input("Benutzername: ")
        password = input("Passwort: ")
        print("")
        return username, password

    @staticmethod
    def storage_place_promt():
        print("Gib nun bitte den Speicherpfad ein, an dem deine Ilias-Dateien gespeichert werden sollen. \n"
              "Bsp.: C:\\Users\\hanne\\PycharmProjects\\IliasCrawler")
        pfad = input("Speicherpfad: ")
        print("")
        return pfad





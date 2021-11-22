from PyInquirer import prompt
from service.Session import Session
import easygui


class SetupView():

    @staticmethod
    def get_username_and_password():
        print("Damit wir deine Dateien herrunterladen können müssen wir uns über deinen Ilias-Account anmelden."
              "\nDeine Daten bleiben auf deinem Gerät und werden selbstverständlich nicht weitergegeben.")
        questions = [
            {
                'type': 'input',
                'qmark': '',
                'message': 'Bitte gib deinen Ilias-Benutzernamen ein:',
                'name': 'username',
                'validate': lambda answer: 'Du musst einen Benutzernamen eingeben.'
                if len(answer) == 0 else True
            },
            {
                'type': 'password',
                'qmark': '',
                'message': 'Bitte gib dein Ilias-Passwort ein:',
                'name': 'password',
                'validate': lambda answer: 'Du musst ein Passwort eingeben.'
                if len(answer) == 0 else True
            }
        ]
        valid = False
        while not valid:
            user_input = prompt(questions)
            valid = Session(user_input['username'],
                            user_input['password']).is_valid()
            if not valid:
                print(
                    "Deine Anmeldedaten waren nicht korrekt. Bitte versuche es nocheinmal.")
        username = user_input['username']
        password = user_input['password']
        return username, password

    @staticmethod
    def get_storage_place():
        print("\nWähle nun bitte den Ordner aus, in dem deine Ilias-Dateien gespeichert werden sollen.")
        print("Die Ordnerstruktur wird der von Ilias entsprechen:")
        print("├── Ausgewählter Ordner")
        print("|    |")
        print("|    └── Ilias")
        print("|        |")
        print("|        ├── Kurs 1")
        print("|        |")
        print("|        ├── Kurs 2")
        print("|        |")
        input("\nDrücke Enter wenn du bereit bist den Ordner auszuwählen...")
        return easygui.diropenbox()

    @staticmethod
    def setup_info():
        print("\nVielen Dank, deine Eingaben wurden gespeichert. Du musst sie in Zukunft nicht nochmal eingeben.")

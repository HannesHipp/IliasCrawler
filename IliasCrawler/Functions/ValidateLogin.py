from Framework.Function import Function
from IliasCrawler.Session import Session


class ValidateLogin(Function):

    def __init__(self, username, password) -> None:
        super().__init__()
        self.username = username
        self.password = password

    def execute(self):
        print("Hello")
        valid = True
        # session = Session(self.username.value, self.password.value)
        # if session.is_valid():
        if valid:
            self.username.valid = True
            self.password.valid = True
        else:
            self.username.valid = False
            self.password.valid = False
            self.signals.error.emit(
                'Der Benutzername oder das Passwort ist falsch.')

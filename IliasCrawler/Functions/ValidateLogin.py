from Framework.Function import Function
from IliasCrawler.Session import Session

from IliasCrawler.Datapoints.Username import Username
from IliasCrawler.Datapoints.Password import Password


class ValidateLogin(Function):

    def __init__(self, username: Username, password: Password) -> None:
        super().__init__()
        self.username = username
        self.password = password

    def execute(self):
        session = Session(self.username.value, self.password.value)
        if session.is_valid():
            return True
        else:
            self.signals.error.emit(
                'Der Benutzername oder das Passwort ist falsch.')
            return False

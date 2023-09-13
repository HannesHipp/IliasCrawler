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
        if Session.set_session(self.username.value, self.password.value):
            return True
        else:
            self.username.invalidate.emit()
            self.password.invalidate.emit()
            raise Exception('Der Benutzername oder das Passwort ist falsch.')

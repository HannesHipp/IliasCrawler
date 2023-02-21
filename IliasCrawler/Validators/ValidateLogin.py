from Framework.Validator import Validator
from IliasCrawler.Session import Session


class ValidateLogin(Validator):

    def __init__(self, *datapoints) -> None:
        super().__init__(*datapoints)

    def validate(self, username, password):
        session = Session(username.value, password.value)
        if session.is_valid():
            return True, ''
        else:
            return False, 'Der Benutzername oder das Passwort ist falsch.'

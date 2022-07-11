from Framework.Validator import Validator
from IliasCrawler.Session import Session


class ValidateLogin(Validator):

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.username = kwargs['username']
        self.password = kwargs['password']

    def validate(self):
        session = Session(self.username.valueToBeValidated, self.password.valueToBeValidated)
        if session.is_valid():
            return True, ''
        else:
            return False, 'Der Benutzername oder das Passwort war falsch.'
    

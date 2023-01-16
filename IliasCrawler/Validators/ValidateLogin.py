from Framework.Validator import Validator
from IliasCrawler.Session import Session


class ValidateLogin(Validator):

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    def validate(self, **datapoints):
        return True, ''
        # session = Session('', '')
        # if session.is_valid():
        #     return True, ''
        # else:
        #     return False, 'Der Benutzername oder das Passwort war falsch.'
    

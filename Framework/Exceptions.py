class DoesNotContainNecessaryAttributesException(Exception):
    pass


class ItemAlreadyExists(Exception):
    pass


class WrongFieldLength(Exception):
    pass


class NoNameException(Exception):
    pass


class NoUrlException(Exception):
    pass


class ValidationFailed(Exception):

    def __init__(self, message) -> None:
        super().__init__(message)

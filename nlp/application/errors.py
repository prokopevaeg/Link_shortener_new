from nlp.domain.errors import HandlingError


class ApplicationError(HandlingError):
    pass


class UserAlreadyExists(ApplicationError):
    pass

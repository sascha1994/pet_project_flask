class BaseServiceError(Exception):
    pass


class GenreNotFound(BaseServiceError):
    pass


class UserNotFound(BaseServiceError):
    pass


class WrongPassword(BaseServiceError):
    pass


class ItemNotFound(BaseServiceError):
    pass


class WrongPasswords(BaseServiceError):
    pass

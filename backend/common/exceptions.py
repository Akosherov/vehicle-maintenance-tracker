class AppException(Exception):
    status_code: int

    def __init__(self, message: str):
        self.message = message
        super().__init__(message)


class Unauthorized(AppException):
    status_code = 401


class Forbidden(AppException):
    status_code = 403


class NotFoundError(AppException):
    status_code = 404


class ConflictError(AppException):
    status_code = 409


class BusinessRuleViolation(AppException):
    status_code = 409

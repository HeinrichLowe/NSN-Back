from .http_error import HttpError

class HttpBadRequestError(HttpError):
    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message
        self.name = 'Bad Request'
        self.status_code = 400
